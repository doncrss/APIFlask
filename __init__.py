from flask import Flask
from connection import db, Config

from src import ma, api
from flasgger import Swagger

from src.models.user_models import UsuarioModel
from src.views import user_view, produto_view, categoria_view, registro_view

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    swagger = Swagger(app, config={
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
        "specs_route": "/docs"
    })

    # opcional pra verificar funcionamento do server
    @app.get('/')
    def home():
        return {"mensagem" : "Api flask funcionando!"}, 200

    
    return app