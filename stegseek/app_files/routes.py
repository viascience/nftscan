import random
import string
import subprocess
import os.path as path
from pathlib import Path
from app_files import app
from flask import request


@app.route("/")
def index():
    image = request.args.get("image")
    if image is None:
        response_dict = {"info": "Image name not provided."}
        return response_dict, 400
    else:
        image_path = f"/dataImages/{image}"

        if not path.exists(image_path):
            response_dict = {"info": f"{image_path} not found"}
            return response_dict, 404

        letters = string.ascii_lowercase
        random_string = "".join(random.choice(letters) for i in range(10))
        image_name = Path(image_path).stem
        output_file = f"{image_name}_{random_string}"

        # Specific logic for Stegseek
        response = subprocess.run(
            ["stegseek", image_path, "rockyou.txt", "-xf", output_file],
            capture_output=True,
        )

        # False means found malware, True means malware not found
        status = response.returncode

        # outcome = response.stderr if status == True else response.stdout
        malware = False if status == True else True
        outcome = {
            "stdout": response.stdout.decode(),
            "stderr": response.stderr.decode(),
        }

    response_dict = {"malware": malware, "info": outcome, "output": output_file}

    return response_dict, 200


@app.route("/health")
def healthcheck():
    return "Healthy!"
