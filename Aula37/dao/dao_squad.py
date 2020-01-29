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
        comando = f"SELECT * FROM aula37.squads"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
        
    def buscar_por_ID(self,ID):
        #criação do comando para passar o id para o cursor
        comando_sql_select =  f"SELECT * FROM aula37.squads WHERE ID={ID}"
        self.cursor.execute(comando_sql_select)
        resultado = self.cursor.fetchone()
        return resultado
    
    def salvar(self, squad = Squad):
        comando = f"""INSERT INTO aula37.squads
        (ID, Nome, Descricao, NumeroPessoas, LinguagemBackEnd, FrameworkFrontEnd)
        VALUES({squad.ID},'{squad.Nome}','{squad.Descricao}',{squad.NumeroPessoas},'{squad.LinguagemBackEnd}','{squad.FrameworkFrontEnd}')"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, squad = Squad):
        comando = f"""UPDATE aula37.squads
        SET 
            Nome = '{squad.Nome}',
            Descricao ='{squad.Descricao}',
            NumeroPessoas = {squad.NumeroPessoas},
            LinguagemBackEnd = {squad.LinguagemBackEnd}
            FrameworkFrontEnd = {squad.FrameworkFrontEnd}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando = f"DELETE FROM aula37.squads WHERE ID = {ID}"
        self.cursor.execute(comando)
        self.conexao.commit()



s = SquadDb

print(s)