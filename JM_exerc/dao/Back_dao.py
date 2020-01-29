import MySQLdb
import sys 
sys.path.append('C:/Users/900152/Documents/Dados/TrabalhoPython/JM_exerc')
from model.Back_model import BackEnd

class BackDb:
    def select_all(self):
        comand = 'SELECT * FROM topskills01.02_JM_BackEnd;'
        selectcomand =  self.cursor.execute(comand)
        return selectcomand

    def select_by_id(self,id):
        comand = f"SELECT * FROM topskills01.02_JM_BackEnd WHERE ID={id}"
        idcomand =  self.cursor.execute(comand)
        return idcomand
        
    def update(self, back : BackEnd):
        comand = f"UPDATE topskills01.02_JM_BackEnd  SET Nome = {back.Nome}, Descricao = '{back.Descricao}', Versao = '{back.Versao}' WHERE ID = {back.id}"
        self.conexao.commit()

    def save(self, back: BackEnd):
        comand = f"""INSERT INTO topskills01.02_JM_BackEnd
        ( 
            Nome
           ,Descricao
           ,Versao
        )
        VALUES(
            '{back.Nome}'
            ,'{back.Descricao}'
            ,'{back.Versao}'
        )"""
        savecomand = self.cursor.execute(comand)
        return savecomand
    
    def delete(self,id):
        comand = f"DELETE FROM topskills01.02_JM_BackEnd WHERE ID={id}"
        deletecomand = self.cursor.execute(comand)
        return deletecomand
        
