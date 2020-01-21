import sys 
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula37')
import MySQLdb
from model.model_squad import Squad

class SquadDb:
    #Criando Conexao
    conexao = MySQLdb.connect(host= '127.0.0.1', database='aula37', user='root')
    #Salvando conexao no cursor
    cursor = conexao.cursor()
    #Listar todos os dados
    def listar_todos(self):
        comando_sql_select = "SELECT * FROM aula37.squads"
        #Executando comando 
        self.cursor.execute(comando_sql_select)
        #Seleciona todos os resultados
        resultado = self.cursor.fetchall()
        lista_squad_resultado = self.converter_tabela_classe(resultado)
        return lista_squad_resultado
        
    def buscar_por_ID(self,ID):
        #criação do comando para passar o id para o cursor
        comando_sql_select =  f"SELECT * FROM aula37.squads WHERE ID={ID}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado

    def converter_tabela_classe(self, lista_tuplas):
        #cria uma lista para armazenar os dicionarios
        lista_squads = []
        for s in lista_tuplas:
            #criação do objeto da classe pessoa
            s1 = Squad()
            #pega cada posição da tupla e atribui a uma chave
            s1.ID = s[0]
            s1.Nome = s[1]
            s1.Descricao = s[2]
            s1.NumeroPessoas = s[3]
            s1.LinguagemBackEnd = s[4]
            s1.FrameworkFrontEnd = s[5]
            lista_squads.append(s1)
            print(s1)
        return lista_squads
    
    def salvar(self, squad = Squad):
        comando = 




