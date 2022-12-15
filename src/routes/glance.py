# Importing the requests library, the Blueprint and request functions from the flask library, and the
# login function from the login.py file.
import requests
from flask import Blueprint
from .login import login

env = "https://api-uat-001.ormuco.com"
glance_port = "9292"

# Calling the login function from the login.py file and passing the token to the headers variable.
headers = {"X-Auth-Token": login()}

# Creating a blueprint for the glance API.
glance = Blueprint("glance_blueprint", __name__)


@glance.route("/images",)
def find_images():
    # Making a request to the Glance API to get the list of images.
    images = requests.get(url=f"{env}:{glance_port}/v2/images",
                          headers=headers).json().get('images')
    return images
