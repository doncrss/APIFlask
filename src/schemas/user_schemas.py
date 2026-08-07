from src import ma
from src.models import user_models
from marshmallow import fields

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_models.UsuarioModel
        fields = ('id' , 'nome', 'email' , 'senha')
    
    nome = fields.String(required=True)
    email = fields.Email(required=True)
    senha = fields.String(required=True)
