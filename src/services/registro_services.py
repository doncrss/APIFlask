from datetime import datetime
from src.models.registro_models import RegistroModel
from connection import db


def criar_registro(registro):
    db.session.add(registro)
    db.session.commit()
    return registro


def buscar_registro(id):
    return RegistroModel.query.get(id)


def listar_registros():
    return RegistroModel.query.all()


def atualizar_registro(id, data: dict):
    registro = RegistroModel.query.get(id)
    if not registro:
        return None

    for campo, valor in data.items():
        if hasattr(registro, campo) and campo != 'id':
            setattr(registro, campo, valor)

    db.session.commit()
    return registro


def deletar_registro(id):
    registro = RegistroModel.query.get(id)
    if not registro:
        return False

    db.session.delete(registro)
    db.session.commit()
    return True