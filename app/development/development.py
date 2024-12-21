"""
Routes module
"""
from flask import render_template

from . import development_bp
from app.model import headers_weapon, data_weapons

@development_bp.route('/')
def home():
    """
    home page for the app
    """
    return render_template('development/home.html')

@development_bp.route('/weapons')
def wzw():
    """
    warzone's weapone page
    """
    return render_template('development/weapons.html', headers=headers_weapon, data=data_weapons)
