import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula34/Aula34-1')
import MySQLdb
from model.pessoa import Pessoa

class PessoaDb:
    #----- Configurar a conexão
    conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
    #----- Salva o cursor da conexão em uma variável
    cursor = conexao.cursor()
    
    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM pessoa"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        lista_pessoas_classe = self.converter_tabela_classe(resultado)
        return lista_pessoas_classe

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM pessoa WHERE ID= {ID}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        #cria uma lista para armazenar os dicionarios
        lista_pessoas = []
        for p in lista_tuplas:
            #----- Criação do objeto da classe pessoa
            p1 = Pessoa()
            #--- pega cada posição da tupla e atribui a uma chave do dicionário
            p1.ID = p[0]
            p1.Nome = p[1]
            p1.Sobrenome= p[2]
            p1.Idade = p[3]
            p1.endereco_ID = p[4]
            lista_pessoas.append(p1)
        return lista_pessoas