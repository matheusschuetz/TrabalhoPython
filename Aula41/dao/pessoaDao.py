import MySQLdb

from Aula41.Model.pessoaModel import PessoaModel
class PessoaDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
        self.cursor = self.connection.cursor()
    def list_all(self):
        self.cursor.execute("SELECT * FROM pessoa")
        pessoas = self.cursor.fetchall()
        return pessoas

    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM pessoa WHERE ID={id}")
        pessoa = self.cursor.fetchone()
        p = PessoaModel(pessoa[1], pessoa[2], pessoa[3], pessoa[0])
        return p
    def insert(self, pessoa):
        return f"Adicionando pessoa: {pessoa}"
    def update(self,pessoa):
        return "Atualizado"
    def delete(self,id):
        return "Pessoa Deletada"