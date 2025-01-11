from flask import Blueprint

catalogue_bp = Blueprint('catalogue_bp', __name__, template_folder='templates', static_folder='static')

from . import catalogue
