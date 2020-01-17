import MySQLdb
from Model.pessoa import Pessoa

class PessoaDao:
    conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM pessoa AS P LEFT JOIN endereco AS E ON P.Endereco_ID = E.ID"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM pessoa AS P LEFT JOIN endereco AS E ON P.Endereco_ID = E.ID WHERE P.ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, pessoa:Pessoa):
        comando = f""" INSERT INTO pessoa
        (
            Nome,
            Sobrenome,
            Idade,
            Endereco_ID
        )
        VALUES
        (
            '{pessoa.nome}',
            '{pessoa.sobrenome}',
            {pessoa.idade},
            {pessoa.endereco.id}

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, pessoa:Pessoa):
        comando = f""" UPDATE pessoa
        SET
            Nome = '{pessoa.nome}',
            Sobrenome ='{pessoa.sobrenome}',
            Idade = {pessoa.idade},
            ENDERECO_ID = {pessoa.endereco.id}
        WHERE ID = {pessoa.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM pessoa WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()