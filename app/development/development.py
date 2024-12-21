"""
Routes module
"""
from flask import render_template

from . import development_bp
from app.model import headers_weapon, data_weapons, operators

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
    return render_template('development/operators.html', operators=operators)
