from src.models.user_models import UsuarioModel
from connection import db


def criar_usuario(usuario):
    """Recebe uma instância `UsuarioModel` (via schema) e persiste no DB."""
    db.session.add(usuario)
    db.session.commit()
    return usuario


def listar_usuario():
    return UsuarioModel.query.all()


def listar_usuario_email(email):
    return UsuarioModel.query.filter_by(email=email).first()


def listar_usuario_id(id):
    return UsuarioModel.query.get(id)


def editar_usuario(id, data: dict):
    usuario = UsuarioModel.query.get(id)
    if not usuario:
        return None

    if 'nome' in data:
        usuario.nome = data['nome']
    if 'email' in data:
        usuario.email = data['email']
    if 'senha' in data and data['senha']:
        usuario.gen_senha(data['senha'])

    db.session.commit()
    return usuario


def deletar_usuario(id):
    usuario = UsuarioModel.query.get(id)
    if not usuario:
        return False

    db.session.delete(usuario)
    db.session.commit()
    return True