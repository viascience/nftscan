### GitHub Repository Status

This repository is only available to maintain previous public references to the repository but the support is discontinued and under no active development.

--------------------------------------------------------

The following repository contains a NFT malware scanner as an API and CLI. Thanks to this scanner, you can test if your favorite NFTs contain any malware or secret hidden within the image.

The current version of the scanner supports the following algorithms for JPG malware detection:



* **quickscan**: PHP scanner
* **jsteg**: Reveals data hiding inside the image and indicates JPGs formatting that could contain malware. Reference repository: https://github.com/lukechampine/jsteg
* **stegseek**: Fast steghide cracker that can extract hidden data from files. Considered to be thousands of times faster than other crackers. Reference repository: https://github.com/RickdeJager/stegseek

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


2. Download the rockyou.txt dictionary and copy it to the stegseek directory under:

```

nftscan

│   README.md

│

└───stegseek

│   │ rockyou.txt

```

**Note**: The dataset can be downloaded from: https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt


3. Build API and services

`cd ./nftscan && docker-compose up --build -d`



4. Install `typer` into your environment

`pip install typer`



5. Go to the root directory and execute the CLI

`python main.py <image_name> <algorithm: opt> <address: opt> <port: opt>`

### Run tests

To make sure that the software is running correctly before testing your NFTs, follow these steps to test the API:



1. `poetry install`
2. `poetry shell`
3. From root directory: `pytest`

### How to add new services



Flask has been chosen as the API because it is lightweight. Other APIs could be used, but are not recommended.


1. Please create a new directory in the root directory with the name of the service.
2. The directory will need:
    1. app_files directory with a Flask API.
    2. Dockerfile running Flask as the last step: `CMD ["flask", "run", "-h", "0.0.0.0", "--port=5001"]`
    3. *Note: Any of the services can be used as a template, but don't forget to add your specific logic to call your algorithm!*
3. Add the service to the docker-compose.yml in the nftscan directory:

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



