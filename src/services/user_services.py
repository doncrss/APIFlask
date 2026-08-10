from src.models.user_models import UsuarioModel
from connection import db

def criar_usuario(nome, email, senha):
    usuario = UsuarioModel(
        nome=nome,
        email=email
    )
    usuario.gen_senha(senha)

    db.session.add(usuario)
    db.session.commit()

    return usuario


def buscar_usuario(id):
    return UsuarioModel.query.get(id)

def listar_usuario():
    return UsuarioModel.query.all()

def atualizar_usuario(id):
    return UsuarioModel.query.get(id)

    if not usuario:
        return None

    usuario.nome = nome
    usuario.email = email

    db.session.commit()

    return usuario


def atualizar_senha(id, senha):
    usuario = UsuarioModel.query.get(id)

    if not usuario:
        return None

    usuario.gen_senha(senha)

    db.session.commit()

    return usuario

def autenticar_usuario(email, senha):
    usuario = UsuarioModel.query.filter_by(email=email).first()

    if not usuario:
        return None

    if not usuario.verify_senha(senha):
        return None

    return usuario


def deletar_usuario(id):
    usuario = UsuarioModel.query.get(id)

    if not usuario:
        return False

    db.session.delete(usuario)
    db.session.commit()

    return True