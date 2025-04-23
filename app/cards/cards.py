from flask import render_template

from . import cards_bp

from app.model import operator_instance

@cards_bp.route('/')
def cards_endpoint():
    return render_template('cards/cards.html', operator=operator_instance)
