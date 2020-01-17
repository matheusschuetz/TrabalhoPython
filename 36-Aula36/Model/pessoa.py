from Model.endereco import Endereco
class Pessoa:
    id = 0
    nome = ''
    sobrenome= ''
    idade = 0
    endereco = Endereco()

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.endereco.id}'