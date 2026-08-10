from src.models.produtos_models import ProdutoModel
from connection import db

def criar_produto(nome, preco, uni_medida, qtd_estoque, id_categoria):
    produto = ProdutoModel(
        nome=nome,
        preco=preco,
        uni_medida=uni_medida,
        qtd_estoque=qtd_estoque,
        id_categoria=id_categoria
    )

    db.session.add(produto)
    db.session.commit()

    return produto


def buscar_produto(id):
    return ProdutoModel.query.get(id)

def listar_produtos():
    return ProdutoModel.query.all()

def atualizar_produto(id, nome, preco, uni_medida, qtd_estoque, id_categoria):
    produto = ProdutoModel.get.query(id)
    if not produto:
        return None 


    produto.nome=nome
    produto.preco=preco
    produto.uni_medida=uni_medida
    produto.qtd_estoque=qtd_estoque
    produto.id_categoria=id_categoria


def deletar_produto(id):
    produto = ProdutoModel.query.get(id)
    

    if not produto:
        return False

    db.session.delete(produto)
    db.session.commit()

    return True