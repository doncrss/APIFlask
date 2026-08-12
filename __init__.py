from flask import Flask
from connection import db, Config, ma
from flask_marshmallow import Marshmallow
from flask_restful import Api

ma = Marshmallow()
api = Api()

from src.models.user_models import UsuarioModel
from src.views import user_view

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    api.init_app(app)

    # opcional pra verificar funcionamento do server
    @app.get('/')
    def home():
        return {"mensagem" : "Api flask funcionando!"}, 200

    
    return app