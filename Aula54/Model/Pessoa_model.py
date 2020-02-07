import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Pessoa(Base):
    __tablename__ = "pessoa"
    id = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(length=100))
    Sobrenome = db.Column(db.String(length=100))
    Idade = db.Column(db.Integer)

    def __str__(self):
        return f"{self.id}--{self.Nome}--{self.Sobrenome}--{self.Idade}"

