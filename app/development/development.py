"""
Routes module
"""
from flask import render_template

from . import development_bp
from app.model import headers_weapon, data_weapons, operators, dummy_operators, operator_instance

@development_bp.route('/')
def home():
    """
    home page for the app
    """
    return render_template('development/home.html')

@development_bp.route('/weapons')
def weapons_endpoint():
    """
    warzone's weapone page
    """
    return render_template('development/weapons.html', headers=headers_weapon, data=data_weapons)

@development_bp.route('/operators')
def operators_endpoint():
    """
    warzone's operators page
    """
    return render_template('development/operators.html', operators=dummy_operators)

@development_bp.route('/table')
def table_endpoint():
    return render_template('development/table.html')

@development_bp.route('/rq1')
def rq1_endpoint():
    return render_template('development/rq1.html')

@development_bp.route('/catalogue1')
def catalogue1_endpoint():
    return render_template('development/catalogue_01.html')

@development_bp.route('/catalogue2')
def catalogue2_endpoint():
    return render_template('development/catalogue_02.html')

@development_bp.route('/card<card_number>')
def card1_endpoint(card_number):
    return render_template(f'development/card{card_number}.html', operator=operator_instance)