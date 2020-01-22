from dao.Back_dao import BackDb
from model.Back_model import BackEnd


class BackController:
    def __init__(self):
        self.dao = BackDb()

    def select_all(self):
        lista = self.dao.select_all()
        lista_retorno = []
        for b in lista:
            ba = BackEnd(b[0], b[1], b[2], b[3])
            lista_retorno.append(ba)
        return lista_retorno
        
    
    def select_by_id(self):
        lista = self.dao.select_by_id()
        b = BackEnd(lista[0],lista[1],lista[2],lista[3])
        return b
    
    def update(self, back : BackEnd):
        self.dao.update(back)

    def save(self, back : BackEnd):
        self.dao.save(back)
        
    def delete(self, id):
        self.dao.delete(id)

        