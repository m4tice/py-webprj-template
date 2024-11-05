"""
init file for the app package
"""
from flask import Flask

app = Flask(__name__)

# app's modules importation is placed here to prevent circular imports
# pylint: disable=wrong-import-position
from app import routes
