from . import db
from .abc import BaseModel, MetaBaseModel


class Event(db.Model, BaseModel, metaclass=MetaBaseModel):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)
    venue = db.Column(db.String(200), unique=False, nullable=False)
