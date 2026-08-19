from sqlalchemy.orm import relationship
from connection import db
from datetime import datetime
from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey


class RegistroModel(db.Model):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True)
    tipo = Column(Boolean, nullable=False)
    dth_registro = Column(DateTime, default=datetime.utcnow, nullable=False)
    fk_produto = Column(Integer, ForeignKey("produtos.id"), nullable=False)

    produto = relationship("ProdutoModel", back_populates="registros")
