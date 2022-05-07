import yaml
import os.path as path 
from configparser import ConfigParser
from importlib import resources 


def parser_services():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text('app_files', 'config.txt'))
    path_compose = cfg.get('tools', 'path').strip("'")

    if not path.exists(path_compose):
    	raise Exception(f"{path_compose} does not exists.")
    with open(path_compose, "r") as stream:
    	libraries = yaml.safe_load(stream)
    services = [i for i in libraries['services']]

    return services
        

# There is no library to avoid caring the ports
# There is a cli for quick use and doing the download
# There is an API calling the services 
# Next iteration dynamic download
