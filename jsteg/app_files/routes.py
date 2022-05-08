import random
import string
import subprocess
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

        # Specific logic for Jsteg
        response = subprocess.run([ "jsteg", "reveal", image_path, f"/dataImages/{output_file}"], capture_output=True)
        
        # False means foud malware, True means malware not found
        status = response.returncode
        
        outcome = response.stderr if status == True else response.stdout
        
        # This will capture when an image is not readable due to miss-format of jpg
        malware = True if b'jpeg does not contain hidden data\n' != response.stderr else False
        
        # Captures if jsteg cant find the path
        if malware == True and b'no such file or directory\\n' in response.stderr:
            response_dict = {
                "info": str(outcome)
            }
            return response_dict, 404            
    
    response_dict = {
        "malware": malware,
        "info": str(outcome),
        "output": output_file
    }
    
    return response_dict, 200

@app.route('/health')
def healthcheck():
    return 'Healthy!'
