from flask import Blueprint

get_request_bp = Blueprint('get_request', __name__, template_folder='templates', static_folder='static')

from . import get_request
