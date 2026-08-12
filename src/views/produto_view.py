from flask_restful import Resource
from flask import request, jsonify, make_response
from src.schemas.produto_schema import (ProdutoSchema, produtos_schema)
from marshmallow import ValidationError
from src.services.produto_services import produto
from src import api

class ProdutoList(Resource):
    def get(self):
        usuarios = user.service