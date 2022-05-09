import os.path as path
from configparser import ConfigParser
from importlib import resources

import yaml


def parser_services():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text("app_files", "config.txt"))
    path_compose = cfg.get("tools", "path").strip("'")

    if not path.exists(path_compose):
        raise Exception(f"{path_compose} does not exists.")
    with open(path_compose, "r") as stream:
        libraries = yaml.safe_load(stream)
    services = [i for i in libraries["services"]]

    return services
