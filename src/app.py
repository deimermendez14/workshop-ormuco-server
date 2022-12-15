# Importing the Flask object, the config file, the routes and the CORS object.
from flask import Flask

from config import config

from routes import nova, neutron, glance

from flask_cors import CORS

# Creating a Flask object and then enabling CORS on it.
app = Flask(__name__)
CORS(app)


def page_not_found(error):
    """
    It returns a string with the text "Not found page" and a 404 status code

    :param error: The error that occurred
    :return: A tuple of the response and the status code.
    """
    return "<h1>Not found page</h1>", 404


if __name__ == '__main__':

    app.config.from_object(config['development'])

    app.register_blueprint(nova.nova, url_prefix="/api/nova")

    app.register_blueprint(neutron.neutron, url_prefix="/api/neutron")

    app.register_blueprint(glance.glance, url_prefix="/api/glance")

    app.register_error_handler(404, page_not_found)

    app.run()
