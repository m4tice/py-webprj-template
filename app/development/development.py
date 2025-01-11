"""
Routes module
"""
from flask import render_template, jsonify

from . import development_bp
from app.model import model_rq1, headers_weapon, data_weapons, dummy_operators, operator_instance, packages

def test_func():
    return 'hello'

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

# @development_bp.route('/button2')
# def rq1_endpoint():
#     return render_template('development/button2.html', packages=packages, headers=model_rq1.get_headers(), data=model_rq1.get_all_items())

@development_bp.route('/rq1')
def rq1_endpoint():
    return render_template('development/rq1.html', packages=packages, headers=model_rq1.get_headers(), data=model_rq1.get_all_items())

# @development_bp.route('/button')
# def button_endpoint():
#     return render_template(f'development/button2.html')

# @development_bp.route('/test-func', methods=['POST'])
# def trigger_test_func():
#     result = test_func()
#     return jsonify({'message': result})

# @development_bp.route('/button-click', methods=['POST'])
# def button_click():
#     project = 'ComServices'
#     filtered_data = model_rq1.get_entry_by_project(project)
#     return jsonify({'success': True})

@development_bp.route('/rq1/<package>', methods=['GET'])
def query_random_item(package):
    return jsonify({'message': package})

@development_bp.route('/rq12')
def rq12_endpoint():
    return render_template('development/rq12.html')

@development_bp.route('/rq12-data')
def rq12_data_endpoint():
    return jsonify({'packages': packages, 'headers': model_rq1.get_headers(), 'data': model_rq1.get_all_items()})
