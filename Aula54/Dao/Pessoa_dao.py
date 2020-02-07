from Aula54.Model.Pessoa_model import Pessoa
from Aula54.Dao.Base_dao import BaseDao

class PessoaDao(BaseDao):
    def list_all(self):
        return self.sessao.query(Pessoa).all()
    def buscar_por_id(self,ID):
        return self.sessao.query(Pessoa).filter_by(id=ID).one()
    def deletar(self,ID):
        model = self.sessao.query(Pessoa).filter_by(id=ID).one()
        self.sessao.delete(model)
        self.sessao.commit()
        return f"Deletado obj ID = {ID}"

    def inserir(self, model : Pessoa):
        self.sessao.add(model)
        self.sessao.commit()
        return f"Pessoa de id: {model.ID} criada"

    def alterar(self, model : Pessoa):
        self.sessao.merge(model)
        self.sesssao.commit()
        return f"Pessoa {model.Nome} alterada com suecesso"