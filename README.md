The following repository contains a NFT malware scanner API and CLI. Thanks to this scanner you can test if your favorite NFTs contain any malware or secret hidden within the image.

The current version of the canner support the following algorithms for JPG malware detection:



* **quickscan**: Php scanner
* **jsteg**: Reveals data hiding inside the image and indicates JPGs formatting that could contain malware. Reference repository: https://github.com/lukechampine/jsteg
* **stegseek**: Fast steghide cracker that can extract hidden data from files. Considered to be thousands of times faster than other crackers Reference repository: https://github.com/RickdeJager/stegseek

### Steps to use NFTscan CLI



1. Download the NFT that you would like to scan and copy it under:

```

nftscan

│   README.md

│

└───nftscan

│   └───data

│       │  image.jpg

```

**Note**: The current version is only available for JPGs.



2. Build API and services

`cd ./nftscan && docker-compose build .`



3. Install typer

`pip install typer`



4. Go to the root directory and execute the CLI

`python main.py <image_name> <algorithm: opt> <address: opt> <port: opt>`

### Run tests

To make sure that the software is running correctly before testing your NFTs. Test the library running the following commands:



1. `poetry install`
2. `poetry shell`
3. From root directory: `pytest`

### How to add new services



1. Please create a new directory on the root directory with the name of the service.
2. The directory will need:
    1. app_files directory with a flask API.
    2. Dockerfile running flask as the last step: `CMD ["flask", "run", "-h", "0.0.0.0", "--port=5001"]`
    3. Note: It can be used any of the other services as a template, but don't forget to add your specific business logic to call your algorithm.
3. Add the service to the docker-compose.yml under nftscan:

```

nftscan

│   README.md

│

└───nftscan

│   │   docker-compose.yml

│   

└───New Service

│   │   Dockerfile

│   │

│   └───app_files

│       │   __init__.py

│       │   routes.py

│       │   ...

```



