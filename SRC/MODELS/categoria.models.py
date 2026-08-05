from sqlalchemy.orm import relationship
from connection import db

class Categoria(db.Model):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)
    categoria = relationship("Produto", back_populates = "Categoria")

    