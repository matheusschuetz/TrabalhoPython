from Aula53.Model.Pessoa_model import PessoaModel
from Aula53.Dao.Base_dao import BaseDao

class PessoaDao(BaseDao):
    def list_all(self):
        return self.sessao.query(PessoaModel).all()




