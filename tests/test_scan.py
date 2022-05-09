from compose.cli.command import project_from_options
import pathlib
import pytest
from compose.service import ImageType

FILE_PATH = pathlib.Path(__file__)
TEST_DIR = FILE_PATH.parent
ROOT_DIR = TEST_DIR.parent
NFTSCAN_DIR = ROOT_DIR.joinpath("nftscan")

@pytest.fixture(scope="session")
def docker_compose():
    docker_compose_path = NFTSCAN_DIR.joinpath("docker-compose.yml")
    assert docker_compose_path.is_file()
    project = project_from_options(project_dir=NFTSCAN_DIR, options={"--file": [docker_compose_path]})
    project.build()
    project.up()
    yield project
    project.down(ImageType.none, include_volumes=True)


def test_hello_world():
    print("Hello World!")


def test_php(docker_compose):

    print("test")