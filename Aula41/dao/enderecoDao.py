import MySQLdb

from Aula41.Model.enderecoModel import Endereco

class EnderecoDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute("SELECT * FROM endereco")
        enderecos = self.cursor.fetchall()
        lista_enderecos = []
        for e in enderecos:
            endereco = Endereco(e[1], e[2], e[3],e[4], e[5], e[0])
            lista_enderecos.append(endereco.__dict__)
        return lista_enderecos
    def get_by_id(self, id):
        self.cursor.execute(f"SELECT * FROM endereco WHERE ID={id}")
        endereco = self.cursor.fetchone()
        e = Endereco(endereco[1], endereco[2], endereco[3],endereco[4], endereco[5], endereco[0])
        return e.__dict__
    def insert(self, endereco : Endereco):
        self.cursor.execute(f"INSERT INTO endereco(Logradouro, Numero, Complemento, Bairro, Cidade) VALUES('{endereco.logradouro}', '{endereco.numero}', '{endereco.complemento}', '{endereco.bairro}', '{endereco.cidade}')")
        self.connection.commit()
        id = self.cursor.lastrowid
        endereco.id = id
        return endereco.__dict__
    def update(self, endereco : Endereco):
        self.cursor.execute(f"UPDATE endereco SET Logradouro = '{endereco.logradouro}', Numero = '{endereco.numero}', Complemento = '{endereco.complemento}', Bairro = '{endereco.bairro}', Cidade = '{endereco.cidade}' WHERE ID={endereco.id};")
        self.connection.commit()
        return endereco.__dict__
    def delete(self, id):
        self.cursor.execute(f"DELETE FROM endereco WHERE ID={id}")
        self.connection.commit()
        return f"Removido o ID:{id}"


a = EnderecoDao()

print(a.get_by_id(1))