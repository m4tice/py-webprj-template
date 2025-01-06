from flask import Blueprint

cards_bp = Blueprint('cards_bp', __name__, template_folder='templates', static_folder='static')

from . import cards
