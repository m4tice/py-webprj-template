from flask import Blueprint

table_bp = Blueprint('table', __name__, template_folder='templates', static_folder='static')

from . import table
