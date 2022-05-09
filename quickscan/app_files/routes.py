import random
import string
import subprocess
import binascii
import os.path as path 
from pathlib import Path
from app_files import app
from flask import request


@app.route('/')
def index():
    image = request.args.get("image")
    if image is None:
        response_dict = {
            "info": "Image name not provided."
        }
        return response_dict, 400
    else:
        image_path = f"/dataImages/{image}"

        if not path.exists(image_path):
            response_dict = {
                "info": f"{image_path} not found"
            }
            return response_dict, 404   

        letters = string.ascii_lowercase
        random_string =  ''.join(random.choice(letters) for i in range(10))
        image_name = Path(image_path).stem
        output_file = f"{image_name}_{random_string}"

        # Specific logic for quickscan
        # Quick scan for injected php or JS comments
        malware = False
        outcome = {}
        with open(image_path, 'rb') as f: 
            content = f.read() 
            if binascii.hexlify(b'<?php') in binascii.hexlify(content): 
                malware = True
                outcome = 'PHP found' 
            
            #if binascii.hexlify(b'/*') in binascii.hexlify(content) and binascii.hexlify(b'*/') in binascii.hexlify(content): 
            #    malware = True
            #    outcome = 'Javascript found'
    
    response_dict = {
        "malware": malware,
        "info": outcome,
        "output": None
    }
    
    return response_dict, 200


@app.route('/health')
def healthcheck():
    return 'Healthy!'
