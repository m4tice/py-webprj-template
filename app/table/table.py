from flask import render_template

from . import table_bp

@table_bp.route('/')
def table():
    return render_template('table/table.html')