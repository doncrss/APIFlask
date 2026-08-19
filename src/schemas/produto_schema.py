from src import ma
from src.models import ProdutoModel
from marshmallow import fields, validate
from .categoria_schemas import CategoriaSchema


class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    nome = fields.String(
        required=True,
        validate=validate.Length(min=3, error='o nome deve ter no mínimo 3 letras')
    )
    preco = fields.Float(required=True, validate=validate.Range(min=0.01))
    uni_medida = fields.String(required=True)
    qtd_estoque = fields.Integer(
        required=True,
        validate=validate.Range(min=0, error='a quantidade não pode ser negativa!')
    )
    id_categoria = fields.Integer(required=False, allow_none=True)
    categoria = fields.Nested(CategoriaSchema, dump_only=True)

    class Meta:
        model = ProdutoModel
        load_instance = True
        fields = ('id', 'nome', 'preco', 'uni_medida', 'qtd_estoque', 'id_categoria', 'categoria')


produto_schema = ProdutoSchema()
produtos_schema = ProdutoSchema(many=True)