# Importing the requests library, the Blueprint and request functions from the flask library, and the
# login function from the login.py file.
import requests
from flask import Blueprint
from .login import login

env = "https://api-uat-001.ormuco.com"
neutron_port = "9696"

# Calling the login function from the login.py file and passing the token to the headers variable.
headers = {"X-Auth-Token": login()}

# Creating a blueprint for the neutron API.
neutron = Blueprint("neutron_blueprint", __name__)


@neutron.route("/networks")
def find_networks():
    # Making a request to the Neutron API to get the list of networks.
    networks = requests.get(url=f"{env}:{neutron_port}/v2.0/networks",
                            headers=headers).json().get('networks')
    return networks


@neutron.route("/seguritys_groups")
def find_seguritys_groups():
    # Making a request to the Neutron API to get the list of security groups.
    seguritys_groups = requests.get(
        url=f"{env}:{neutron_port}/v2.0/security-groups", headers=headers).json().get("security_groups")
    return seguritys_groups
