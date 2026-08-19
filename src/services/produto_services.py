from src.models.produtos_models import ProdutoModel
from connection import db


def criar_produto(produto):
    """Recebe uma instância `ProdutoModel` (via schema) e persiste no DB."""
    db.session.add(produto)
    db.session.commit()
    return produto


def buscar_produto(id):
    return ProdutoModel.query.get(id)


def listar_produtos():
    return ProdutoModel.query.all()


def atualizar_produto(id, data: dict):
    produto = ProdutoModel.query.get(id)
    if not produto:
        return None

    for k, v in data.items():
        if hasattr(produto, k) and k != 'id':
            setattr(produto, k, v)

    db.session.commit()
    return produto


def deletar_produto(id):
    produto = ProdutoModel.query.get(id)
    if not produto:
        return False

    db.session.delete(produto)
    db.session.commit()
    return True