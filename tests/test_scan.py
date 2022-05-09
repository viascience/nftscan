from compose.cli.command import project_from_options
import pathlib
import pytest
from compose.service import ImageType
from typer.testing import CliRunner
import time
import re

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
    time.sleep(2)
    yield project
    project.down(ImageType.none, include_volumes=True)


def test_hello_world():
    print("Hello World!")


def test_php(docker_compose):
    result = runner.invoke(app, ["test.php.jpg"])
    assert result.exit_code == 0
    output = result.stdout
    assert "malware detected: True" in output
    assert "Found passphrase: \"123\"" in output
    assert "Original filename: \"testtext2.txt\"" in output

    print(output)
    for file in DATA_DIR.glob("test.php_*"):
        file.unlink()