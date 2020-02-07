#--- Importação do pacote e nomeando para db
import sqlalchemy as db
from sqlalchemy.orm.session import sessionmaker



class BaseDao:
    def __init__(self):
        #Criando engine com o banco e passando a string de conexão = (SGBD+conector://user:passwd@url:port/database
        conexao = db.create_engine("mysql+mysqlconnector://root:@127.0.0.1:3306/aula1")
        criador_de_sessao = db.orm.sessionmaker()
        criador_de_sessao.configure(bind=conexao)
        self.sessao = criador_de_sessao()