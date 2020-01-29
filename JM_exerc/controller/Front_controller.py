from dao.Front_dao import FrontDb
from model.Front_model import FrontEnd


class FrontController:
    def __init__(self):
        self.dao = FrontDb()

    def select_all(self):
        lista = self.dao.select_all()
        lista_retorno = []
        for b in lista:
            ba = FrontEnd(b[0], b[1], b[2], b[3])
            lista_retorno.append(ba)
        return lista_retorno
        
    
    def select_by_id(self):
        lista = self.dao.select_by_id()
        b = FrontEnd(lista[0],lista[1],lista[2],lista[3])
        return b
    
    def update(self, front : FrontEnd):
        self.dao.update(front)

    def save(self, front : FrontEnd):
        self.dao.save(front)
        
    def delete(self, id):
        self.dao.delete(id)

        