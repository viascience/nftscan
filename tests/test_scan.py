from compose.cli.command import project_from_options
import pathlib
import pytest
from compose.service import ImageType
from typer.testing import CliRunner
import time

from main import app


FILE_PATH = pathlib.Path(__file__)
TEST_DIR = FILE_PATH.parent
ROOT_DIR = TEST_DIR.parent
NFTSCAN_DIR = ROOT_DIR.joinpath("nftscan")
DATA_DIR = NFTSCAN_DIR.joinpath("data")

runner = CliRunner()

@pytest.fixture(scope="session")
def docker_compose():
    docker_compose_path = NFTSCAN_DIR.joinpath("docker-compose.yml")
    assert docker_compose_path.is_file()
    project = project_from_options(project_dir=NFTSCAN_DIR, options={"--file": [docker_compose_path]})
    project.build()
    project.up()
    # sleep so that the containers are ready.
    time.sleep(2)
    yield project
    project.down(ImageType.none, include_volumes=True)


def test_hello_world():
    print("Hello World!")


def test_php(docker_compose):
    """Test that stegseek detects passphrase."""
    result = runner.invoke(app, ["test.php.jpg"])
    assert result.exit_code == 0
    output = result.stdout
    print(output)
    # malware assert
    assert "malware detected: True" in output
    # jsteg assert
    assert "jpeg does not contain hidden data" in output
    # stegseek assert
    assert "Found passphrase: \"123\"" in output
    assert "Original filename: \"testtext2.txt\"" in output

    for file in DATA_DIR.glob("test.php_*"):
        file.unlink()

def test_jacksparrowpuppylaser(docker_compose):
    """Test that jsteg detects invalid JPEG format."""
    result = runner.invoke(app, ["JackSparrowPuppyLaser.jpg"])
    assert result.exit_code == 0
    output = result.stdout
    print(output)
    # malware assert
    assert "malware detected: True" in output
    # jsteg assert
    assert "could not decode jpeg:invalid JPEG format: missing 0xff00 sequence" in output
    # stegseek assert
    assert "Corrupt JPEG data: premature end of data segment" in output

    for file in DATA_DIR.glob("JackSparrowPuppyLaser_*"):
        file.unlink()

def test_shell(docker_compose):
    """Test that jsteg detects unexpected EOF."""
    result = runner.invoke(app, ["shell.jpg"])
    assert result.exit_code == 0
    output = result.stdout
    print(output)
    # malware assert
    assert "malware detected: True" in output
    # jsteg assert
    assert "could not decode jpeg:unexpected EOF" in output
    # stegseek assert
    assert "Premature end of JPEG file" in output

    for file in DATA_DIR.glob("shell_*"):
        file.unlink()

def test_earth_no_malware(docker_compose):
    """Check that a clean file passes."""
    result = runner.invoke(app, ["earthnomalware.jpg"])
    assert result.exit_code == 0
    output = result.stdout
    print(output)
    # malware assert
    assert "malware detected: False" in output
    # jsteg assert
    assert "jpeg does not contain hidden data" in output
    # stegseek assert
    assert "Progress: 99.42% (132.7 MB) " in output

    for file in DATA_DIR.glob("earthnomalware_*"):
        file.unlink()
