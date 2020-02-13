import sqlalchemy as db

from Aula55.model.base import Base

class Editora(Base):
    __tablename__ = 'LIVRARIA_EDITORA'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))