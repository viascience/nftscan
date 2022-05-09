import os.path as path
import random
import string
import subprocess
from pathlib import Path

from app_files import app, scan, services_config
from flask import request


@app.route("/")
def index():

    if "image" not in request.args:
        response_dict = {"info": "Image name not provided."}
        return response_dict, 400

    if "algorithm" not in request.args:
        algorithm = "all"
    else:
        algorithm = request.args.get("algorithm")

    image_name = request.args.get("image")

    try:
        services = services_config.parser_services()
        scan_results = scan.malware_review(algorithm, image_name, services)
    except Exception as exp:
        return {"info": str(exp)}, 400

    return scan_results, 200


@app.route("/health")
def healthcheck():
    return "Healthy!"
