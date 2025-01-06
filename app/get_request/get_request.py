from flask import render_template, jsonify

from . import get_request_bp

@get_request_bp.route('/')
def button3_endpoint():
    return render_template('get_request/get_request.html')

@get_request_bp.route('/clicked/<int:count>', methods=['GET'])
def button3_clicked_endpoint(count):
    count = int(count) + 1
    return jsonify({'data': f'{int(count)}'})
