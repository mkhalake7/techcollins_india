import datetime
from . import db
from .abc import BaseModel, MetaBaseModel
import datetime


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), unique=True, nullable=False)
    is_admin = db.Column(db.Boolean, unique=False, nullable=False, default=False)
    is_active = db.Column(db.Boolean, unique=False, nullable=False, default=False)


