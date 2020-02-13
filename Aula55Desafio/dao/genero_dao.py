from Aula55.dao.base_dao import BaseDao
from Aula55.model.genero import Genero

class GeneroDao(BaseDao):
    def __init__(self):
        super().__init__(Genero)
