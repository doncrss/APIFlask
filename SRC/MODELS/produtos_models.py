from sqlalchemy.orm import relationship
from connection import db
import 

class Produto(db.Model):
    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    preco = Column(Float, nullable=False)
    uni_medida = Column(String(50), nullable=False)
    qtd_estoque = Column(Integer, nullable=False)
    id_categoria = Column(Integer, Foreign_key ("categoria.id"))
    categoria = relationship("Categoria", back_populates = "Produto")
    categoria = relationship("Produto", back_populates = "Registro")

    