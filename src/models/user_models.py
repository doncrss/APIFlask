from passlib.context import CryptContext
from connection import db
from sqlalchemy import Column, String, Integer

class UsuarioModel(db.Model):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    senha = Column(String(255), nullable=False)

    pwd_context = CryptContext(schemes=["argon"], deprecated="auto")

    def gen_senha(self, senha):
        self.senha = self.pwd_context.hash(senha)

    def verify_senha(self, senha):
        return self.pwd_context.verify(senha, self.senha)


    