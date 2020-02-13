import sqlalchemy as db

from Aula55.model.base import Base

class Genero(Base):
    __tablename__ = "LIVRARIA_GENERO"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(length=100))
    descricao = db.Column(db.String(length=200))