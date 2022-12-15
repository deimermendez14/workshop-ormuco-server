import requests

env = "https://api-uat-001.ormuco.com"
keystone_port = "5000"


json = {
    "auth": {
        "identity": {
            "methods": [
                "password"
            ],
            "password": {
                "user": {
                    "name": "workshop2022@utb.edu.co",
                    "domain": {
                        "name": "Default"
                    },
                    "password": "ILOVECLOUD2022"
                }
            }
        }
    }
}


def login():
    # Getting the token id from the response of the request.
    token_id = requests.post(
        url=f"{env}:{keystone_port}/v3/auth/tokens", json=json).json().get('token').get('id')
    return token_id
