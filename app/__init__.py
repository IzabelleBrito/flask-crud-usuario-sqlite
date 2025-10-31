from flask import Flask
from .config import Config
from .extensions import db, swagger
from .controllers.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    swagger.init_app(app)

    app.register_blueprint(users_bp)

    @app.errorhandler(404)
    def not_found(error):
        return {'error': 'Endpoint não encontrado'}, 404

    @app.errorhandler(400)
    def bad_request(error):
        return {'error': 'Requisição inválida'}, 400

    return app
