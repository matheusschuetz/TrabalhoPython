import MySQLdb

from Aula41.Model.pessoaModel import PessoaModel
class PessoaDao:
    def __init__(self):
        self.conection = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
        self.cursor = self.connection.cursor()
    def list_all(self):
        self.cursor.execute("SELECT * FROM pessoa")
        pessoas = self.cursor.fetchall()
        lista_pessoa = []
        for p in pessoas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa
    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM pessoa WHERE ID={id}")
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p.__dict__



    def insert(self, pessoa : PessoaModel):
        self.cursor.execute(f"INSERT INTO pessoa(Nome, Sobrenome, Idade) VALUES('{pessoa.nome}', '{pessoa.sobrenome}',{pessoa.idade})")
        self.connection.commit()
        id = self.cursor.lastrowid
        pessoa.id = id
        return pessoa.__dict__

    def update(self, pessoa : PessoaModel):
        self.cursor.execute(f"UPDATE pessoa SET Nome = '{pessoa.nome}', Sobrenome = '{pessoa.sobrenome}', Idade = {pessoa.idade} WHERE ID = {pessoa.id}")
        self.connection.commit()
        return pessoa.__dict__


    def delete(self,id):
        self.cursor.execute(f"DELETE FROM pessoa WHERE ID = {id}")
        self.connection.commit()
        return f'Removido a pessoa de id : {id}'



