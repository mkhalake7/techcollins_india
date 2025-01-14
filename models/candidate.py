from . import db
from .abc import BaseModel, MetaBaseModel


class Candidate(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'candidate'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    stream = db.Column(db.String(100), unique=False, nullable=False)
    skill_set =db.Column(db.String(100), unique=False, nullable=False)
