
from Dao.endereco_dao import EnderecoDao
from Model.endereco import Endereco

class EnderecoController:
    dao = EnderecoDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, endereco:Endereco):
        return self.dao.salvar(endereco)

    def alterar(self, endereco:Endereco):
        self.dao.alterar(endereco)

    def deletar(self, id):
        self.dao.deletar(id)
