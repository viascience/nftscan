from flask import Flask

app = Flask(__name__)

from app_files import routes
