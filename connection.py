from dotenv import load_dotenv
import os

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

load_dotenv()

db = SQLAlchemy()
ma = Marshmallow()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv('URL_DATABASE')

    SQLALCHEMY_TRACK_MODIFICATIONS = False