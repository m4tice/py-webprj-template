from flask import Flask


def create_app():
    app = Flask(__name__)

    from app.development import development_bp
    app.register_blueprint(development_bp, url_prefix='/development')

    from app.parameter import parameter_bp
    app.register_blueprint(parameter_bp, url_prefix='/parameter')
    
    return app

