import MySQLdb


class BaseDao:
    def __init__(self, nome_tabela):
        host = '127.0.0.1'
        database = 'aula1'
        user = 'root'
        self.tabela = nome_tabela
        self.connection = MySQLdb.connect(host= host, database= database, user= user)
        self.cursor = self.connection.cursor()

    def list_all(self):
        self.cursor.execute(f"SELECT * FROM {self.tabela}")
        tuplas = self.cursor.fetchall()
        return tuplas

    def get_by_id(self,id):
        self.cursor.execute(f"SELECT * FROM {tabela} WHERE ID={id}")
        model = self.cursor.fetchone()
        return model

    def insert(self,id):
        self.connection.commit()
        id = self.cursor.lastrowid
