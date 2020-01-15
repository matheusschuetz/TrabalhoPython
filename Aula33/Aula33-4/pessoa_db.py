import MySQLdb
from pessoa import Pessoa
class PessoaDb:
     #-----configurar a conexão
    conexao = MySQLdb.connect(host= '127.0.0.1', database='aula1', user='root')
    #-----Salvar o cursor da conexão em variável
    cursor = conexao.cursor()
    def listar_todos(self):
        #-----criação do comando SQL e passado para o cursor
        comando_sql_select = "SELECT * FROM pessoa"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchall()
        return self.converter_tabela_classe(resultado)

    def buscar_por_ID(self,ID):
        comando_sql_select = f"SELECT * FROM pessoa WHERE ID = {ID}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return(resultado)

    def converter_tabela_classe(lista_tuplas):
        #-----criação de uma lista que adiciona os dicionarios
        lista_pessoas = []
        for p in lista_tuplas:
            #-----Criação do objeto da classe pessoa
            p1 = Pessoa()
            #-----Pega cada dicionario e atribui a uma posição
            p1.ID = p[0]
            p1.Nome = p[1]
            p1.Sobrenome = p[2]
            p1.Idade = p[3]
            p1.Endereco_ID = p[4]
            #-----Adiciona cada dicionario na lista
            lista_pessoas.append(p1)
        return lista_pessoas