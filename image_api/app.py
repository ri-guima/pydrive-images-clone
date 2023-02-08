from flask import Flask
from dotenv import load_dotenv

from .views import bp


def create_app(testing=False):
    load_dotenv('.env')
    app = Flask(__name__)
    app.testing = testing
    app.register_blueprint(bp)
    return app
