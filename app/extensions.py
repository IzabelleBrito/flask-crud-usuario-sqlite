from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

db = SQLAlchemy()

# CONFIGURAÇÃO COMPLETA DO SWAGGER
swagger = Swagger(
    template={
        "info": {
            "title": "API CRUD Usuários - PicPay",
            "description": "Prova Técnica - Engenharia de Dados Júnior",
            "version": "1.0.0"
        },
        "definitions": {
            "User": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "created_at": {"type": "string", "format": "date-time"}
                }
            }
        }
    },
    config={
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs/"
    }
)