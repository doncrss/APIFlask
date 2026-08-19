from src import ma
from src.models import registro_models
from marshmallow import fields


class RegistroSchema(ma.SQLAlchemyAutoSchema):
    tipo = fields.Boolean(required=True)
    dth_registro = fields.DateTime(required=False, dump_only=True)
    fk_produto = fields.Integer(required=True)

    class Meta:
        model = registro_models.RegistroModel
        load_instance = True
        fields = ('id', 'tipo', 'dth_registro', 'fk_produto')


registro_schema = RegistroSchema()
registros_schema = RegistroSchema(many=True)
