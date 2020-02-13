from Aula55.dao.base_dao import BaseDao
from Aula55.model.pessoa import Pessoa

class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__(Pessoa)
