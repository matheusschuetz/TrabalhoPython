import MySQLdb
import sys 
sys.path.append('C:/Users/900152/Documents/Dados/TrabalhoPython/JM_exerc')
from model.Front_model import FrontEnd

class FrontDb:
    def select_all(self):
        comand = 'SELECT * FROM topskills01.02_JM_FrontEnd;'
        selectcomand =  self.cursor.execute(comand)
        return selectcomand

    def select_by_id(self,id):
        comand = f"SELECT * FROM topskills01.02_JM_FrontEnd WHERE ID={id}"
        idcomand =  self.cursor.execute(comand)
        return idcomand
        
    def update(self, back : FrontEnd):
        comand = f"UPDATE topskills01.02_JM_FrontEnd  SET Nome = {front.Nome}, Descricao = '{front.Descricao}', Versao = '{front.Versao}' WHERE ID = {front.id}"
        self.conexao.commit()

    def save(self, front: FrontEnd):
        comand = f"""INSERT INTO topskills01.02_JM_FrontEnd
        ( 
            Nome
           ,Descricao
           ,Versao
        )
        VALUES(
            '{front.Nome}'
            ,'{front.Descricao}'
            ,'{front.Versao}'
        )"""
        savecomand = self.cursor.execute(comand)
        return savecomand
    
    def delete(self,id):
        comand = f"DELETE FROM topskills01.02_JM_frontEnd WHERE ID={id}"
        deletecomand = self.cursor.execute(comand)
        return deletecomand
        
