from flask import render_template, jsonify

from . import table_js_bp

data = [
    ['John Doe', 'Engineer', '45'],
    ['Jane Doe', 'Designer', '30'],
    ['John Smith', 'Manager', '55'],
    ['Jane Smith', 'Accountant', '40']
]

@table_js_bp.route('/')
def table_js_endpoint():
    return render_template('table_js/table_js.html')
                           
@table_js_bp.route('/data')
def get_data():
    return jsonify(data)
