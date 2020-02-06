import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseAlchemy = declarative_base()
class PessoaModel(BaseAlchemy):
    __tablename__ = "pessoa"
    ID = db.Column(db.Integer, primary_key=True)
    Nome = db.Column(db.String(length=100))
    Sobrenome = db.Column(db.String(length=100))
    Idade = db.Column(db.Integer)
    def __str__(self):
        return "{}-{}-{}--{}".format(self.ID, self.Nome,self.Sobrenome, self.Idade)

