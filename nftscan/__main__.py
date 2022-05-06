import yaml
import os.path as path 
from configparsers import ConfigParser
from importlib import resources 

from nftscan import scan


def main():
    cfg = ConfigParser()
    cfg.read_string(resources.read_text('reader', 'config.txt'))
    path_compose = cfg.get('tools', 'path')
    if not path.exists(path_compose):
    	raise Except(f"{path_compose} doesnot exists.")
    with open(path_compose, "r") as stream:
    	libraries = yaml.safe_load(stream)
    services = [i for i in libraries['services']]

    if len(sys.argv) == 1:
        image_name = sys.argv[1]
        scan('all', image_name)

    elif len(sys.argv) > 2:
        algorithm = sys.argv[2]
        image_url = sys.argv[1]

        image_path = downloader(image_url)
        scan(algorithm, image_path)
        
    
if ___name__ == "__main__":
	main()
