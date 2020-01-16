import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula34/Aula34-1')

from model.endereco import Endereco
from dao.enderecodb import EnderecoDb

class EnderecoController:
    e = Endereco()
    e_db = EnderecoDb()

    def listar_todos(self):
        return self.e_db.listar_todos()

    def exportar(self):
        lec = self.e_db.listar_todos()
        self.p.exportar_txt(lec)