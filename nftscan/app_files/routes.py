import random
import string
import subprocess
import os.path as path 
from pathlib import Path

from app_files import app
from flask import request
from app_files import scan
from app_files import services_config

@app.route('/')
def index():

    if 'image' not in request.args:
        response_dict = {
            "info": "Image name not provided."
        }
        return response_dict, 400

    elif 'algorithm' not in request.args:
        algorithm = "all"

    image_name = request.args.get("image")
    algorithm = request.args.get("algorithm")

    try:
        services = services_config.parser_services()
        scan_results = scan(algorithm, image_name, services)
    except Exception as exp:
        return exp, 400
        
    return scan_results, 200

@app.route('/health')
def healthcheck():
    return 'Healthy!'
