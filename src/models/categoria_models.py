from sqlalchemy.orm import relationship
from connection import db
from sqlalchemy import Column, String, Integer


class CategoriaModel(db.Model):
    __tablename__ = 'categoria'

    id = Column(Integer, primary_key=True)
    descricao = Column(String(50), nullable=False)
    produtos = relationship("ProdutoModel", back_populates="categoria", cascade="all, delete-orphan")

    