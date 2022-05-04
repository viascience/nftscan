The following repository is aiming to create and easy to use python library,
supporting the downloading and scanning of NFTs in JPG format.

List of algorithms supported for JPG scanning:
+ small script to catch php and JS

- not able to find anything + stegdetect 

- not able to find anything + stegbreak (?)

+ jsteg reveal <image> <output_file>:
    0 found secret - malware
    1 not found secret

+ yes | steghide info <image>:
    0 extracted file - malware
    1 could not extract files 

- only info + identify -verbose (only info - no error)

+ jhead -ce (only info - no error)

- partially succesfull + stegoveritas -exif -meta -xmp -carve -imageTransform  -extractLSB -trailing <image>


+ Stegseek
docker run --rm -it -v "$(pwd):/steg" rickdejager/stegseek <image> rockyou.txt
    0  Extracting to <image>.out
    1 [!] error: Could not find a valid passphrase.

 
