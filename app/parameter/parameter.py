from flask import render_template

from . import parameter_bp

@parameter_bp.route('/<item_id>')
def parameter(item_id):
    return render_template('parameter/parameter.html', item_id=item_id)