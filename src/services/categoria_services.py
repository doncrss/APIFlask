from src.models.categoria_models import CategoriaModel
from connection import db


def criar_categoria(categoria):
    db.session.add(categoria)
    db.session.commit()
    return categoria


def listar_categorias():
    return CategoriaModel.query.all()


def buscar_categoria(id):
    return CategoriaModel.query.get(id)


def editar_categoria(id, data: dict):
    categoria = CategoriaModel.query.get(id)
    if not categoria:
        return None

    for campo, valor in data.items():
        if hasattr(categoria, campo) and campo != 'id':
            setattr(categoria, campo, valor)

    db.session.commit()
    return categoria


def deletar_categoria(id):
    categoria = CategoriaModel.query.get(id)
    if not categoria:
        return False

    db.session.delete(categoria)
    db.session.commit()
    return True
