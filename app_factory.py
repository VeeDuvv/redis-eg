# app_factory.py
# The purpose of this file is to initialize the Flask app instance and any other parts of the app that need to be initialized.
# The function create_app will return a new Flask app instance.
# This is a factory function for creating an instance of your Flask application.

from flask import Flask


def create_app():
    app = Flask(__name__)
    # Initialize other parts of the app here if needed
    return app
