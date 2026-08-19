from src import ma
from src.models import categoria_models
from marshmallow import fields


class CategoriaSchema(ma.SQLAlchemyAutoSchema):
    descricao = fields.String(required=True)

    class Meta:
        model = categoria_models.CategoriaModel
        load_instance = True
        fields = ('id', 'descricao')


categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)
