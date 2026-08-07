from src import ma
from src.models import registro_models
from marshmallow import fields

class RegistroSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = registro_models.RegistroModel
        fields = ('id' , 'tipo', 'dth_registro')
    
    tipo = fields.String(required=True)
    dth_registro = fields.Date(required=True)
    


