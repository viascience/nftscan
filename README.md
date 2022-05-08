The following repository is aiming to create an easy to use python library and cli to download and scan malware NFTs.

List of algorithms supported for NFTs with JPG scanning:
+ Script to catch php and JS in image

+ jsteg reveal <image> <output_file>:
    0 found secret - malware
    1 not found secret
       a. could not decode jpeg:invalid JPEG format: missing 0xff00 sequence -> mapped to 0
       b. jpeg does not contain hidden data

+ steghide info <image>:
    0 extracted file - malware
    1 could not extract files 

+ Stegseek
docker run --rm -it -v "$(pwd):/steg" rickdejager/stegseek <image> rockyou.txt
    0  Extracting to <image>.out
    1 [!] error: Could not find a valid passphrase.


Currently not supported methods:
- verbose (only info - no error)
 
- stegdetect 

- stegbreak 

- stegoveritas -exif -meta -xmp -carve -imageTransform  -extractLSB -trailing <image>

- jhead -ce

# There is a CLI for quick use 
# There is an API calling the services 
# API allows for image in volume or dynamic download


# Steps to use NFTscan CLI

Build API and services 
`cd ./nftscan && docker-compose build .`

Install typer
`pip install typer`

Go to the root directory and execute the CLI
`python main.py <image_name> <algorithm: opt> <address: opt> <port: opt>` 