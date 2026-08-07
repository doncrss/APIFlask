from src import ma
from src.models import categoria_models
from marshmallow import fields

class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = categoria_models.CategoriaModel
        load_instance = True
