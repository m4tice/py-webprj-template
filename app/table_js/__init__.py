from flask import Blueprint

table_js_bp = Blueprint('table_js', __name__, template_folder='templates', static_folder='static')

from . import table_js
