# Importing the requests library, the Blueprint and request functions from the flask library, and the
# login function from the login.py file.
import requests
from flask import Blueprint, request
from .login import login

env = "https://api-uat-001.ormuco.com"
nova_port = "8774"

# Calling the login function from the login.py file and passing the token to the headers variable.
headers = {"X-Auth-Token": login()}

# Creating a blueprint for the nova API.
nova = Blueprint("nova_blueprint", __name__)


@nova.route("/flavors")
def find_flavors():
    # Making a request to the Nova API to get the list of flavors.
    flavors = requests.get(
        url=f"{env}:{nova_port}/v2.1/flavors", headers=headers).json().get("flavors")
    return flavors


@nova.route("/keypairs")
def find_keypais():
    # Making a request to the Nova API to get the list of keypairs.
    keypairs = requests.get(
        url=f"{env}:{nova_port}/v2.1/os-keypairs", headers=headers).json().get("keypairs")
    return keypairs


@nova.route("/create-instace", methods=['POST'])
def create_instance():

    content = request.get_json()

    new_instance = requests.post(
        url=f"{env}:{nova_port}/v2/servers", headers=headers, json=content
    ).json()

    return new_instance
