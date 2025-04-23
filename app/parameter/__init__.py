from flask import Blueprint

parameter_bp = Blueprint('parameter', __name__, template_folder='templates', static_folder='static')

from . import parameter