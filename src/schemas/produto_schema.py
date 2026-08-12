from src import ma
from src.models import ProdutoModel
from marshmallow import fields, validate
from .categoria_schemas import CategoriaSchema


class ProdutoSchema(ma.SQLAlchemyAutoSchema):

    nome = fields.String(
        required=True,
        validate=validate.length(
            min='3',
            error= 'o nome deve ter no mínimo 3 letras'
        ) )

    categoria = fields.Nested(
        CategoriaSchema,
        dump_only = True

    )

    qtd_estoque = fields.Integer(
    required=True,
    validate=validate.Range(
        min=0,
        error='a quantidade não pode ser negativa!'
    ))

    vlr_unitario = fields.Decimal(
        required=True,
        places=2,
        validate=validate.range(    

        ))

    class Meta:
        model = ProdutoModel
        load_instance = True


produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)