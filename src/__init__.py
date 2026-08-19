from connection import db, ma
from flask_restful import Api

api = Api()

__all__ = [
    'db',
    'ma',
    'api'
]
