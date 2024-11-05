"""
Routes module
"""
from flask import render_template

from app import app
from app.data_manager import DataManager

wzw_data_manager = DataManager('app/wz.db')
headers = wzw_data_manager.get_headers_alternative()
data = wzw_data_manager.get_all_data()

@app.route('/')
def home():
    """
    home page for the app
    """
    return render_template('home.html')

@app.route('/wzw')
def wzw():
    """
    warzone's weapone page
    """
    return render_template('wzw.html', headers=headers, data=data)
