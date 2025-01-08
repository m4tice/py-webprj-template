from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.development import development_bp
    app.register_blueprint(development_bp, url_prefix='/development')

    from app.parameter import parameter_bp
    app.register_blueprint(parameter_bp, url_prefix='/parameter')

    from app.table import table_bp
    app.register_blueprint(table_bp, url_prefix='/table')

    from app.get_request import get_request_bp
    app.register_blueprint(get_request_bp, url_prefix='/get-request')

    from app.cards import cards_bp
    app.register_blueprint(cards_bp, url_prefix='/cards')

    from app.table_js import table_js_bp
    app.register_blueprint(table_js_bp, url_prefix='/table-js')
    
    return app

