from src.models.registro_models import RegistroModel
from datetime import datetime


def criar_registro(tipo, fk_produto):
    registro = RegistroModel(
        tipo=tipo,
        fk_produto=fk_produto,
        dth_registro=datetime.now()
    )

    db.session.add(registro)
    db.session.commit()

    return registro


def buscar_registro(id):
    return RegistroModel.query.get(id)


def listar_registros():
    return RegistroModel.query.all()


def atualizar_registro(id, tipo, fk_produto):
    registro = RegistroModel.query.get(id)

    if not registro:
        return None

    registro.tipo = tipo
    registro.fk_produto = fk_produto

    db.session.commit()

    return registro


def deletar_registro(id):
    registro = RegistroModel.query.get(id)

    if not registro:
        return False

    db.session.delete(registro)
    db.session.commit()

    return True