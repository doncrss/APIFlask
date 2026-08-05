from sqlalchemy.orm import relationship
from connection import db
from datetime import datetime

class Registro(db.Model):
    __tablename__ = 'registros'

    id = Column(Integer, primary_key=True)
    tipo = Column(bool, nullable=False)
    dth_registro: = Column(datetime)
    fk_produto = Column(Integer, Foreign_key ("produtos.id"))
    registro = relationship("Produto", back_populates = "Registro")


    