from Aula55.dao.base_dao import BaseDao
from Aula55.model.livro import Livro

class LivroDao(BaseDao):
    def __init__(self):
        super().__init__(Livro)
