
from Aula41.dao.BaseDao import BaseDao
from Aula41.Model.pessoaModel import PessoaModel
class PessoaDao(BaseDao):
    def __init__(self):
        super().__init__("pessoa")
    def list_all(self):
        tuplas = super().list_all()
        lista_pessoa = []
        for p in tuplas:
            pessoa = PessoaModel(p[1], p[2], p[3], p[0])
            lista_pessoa.append(pessoa.__dict__)
        return lista_pessoa


    def get_by_id(self, id):
        model = super().get_by_id(id)
        p = PessoaModel(model[1], model[2], model[3], model[0])
        return p.__dict__

    def insert(self, pessoa : PessoaModel):
        self.cursor.execute(f"INSERT INTO pessoa(Nome, Sobrenome, Idade) VALUES('{pessoa.nome}', '{pessoa.sobrenome}',{pessoa.idade})")
        super().insert(id)
        pessoa.id = id
        return pessoa.__dict__

    def update(self, pessoa : PessoaModel):
        self.cursor.execute(f"UPDATE pessoa SET Nome = '{pessoa.nome}', Sobrenome = '{pessoa.sobrenome}', Idade = {pessoa.idade} WHERE ID = {pessoa.id}")
        self.connection.commit()
        return pessoa.__dict__


    def delete(self,id):
        self.cursor.execute(f"DELETE FROM pessoa WHERE ID = {id}")
        self.connection.commit()
        return f'Removido a pessoa de id : {id}'