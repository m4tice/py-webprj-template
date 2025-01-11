from flask import render_template

from . import catalogue_bp

from app.model import dummy_operators

@catalogue_bp.route('/')
def catalogue1_endpoint():
    return render_template('catalogue/catalogue.html', operators=dummy_operators)
