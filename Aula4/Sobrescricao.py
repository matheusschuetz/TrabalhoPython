#Na sobrescricao de metodos utilizamos o metodo de uma classe para complementar um outro codigo, sendo adicioado de um metodo para o outro

from Aula4.Classe import Pessoa

class Adicionar(Pessoa):
    def __init__(self):
        super().__init__()
        self.cpf = ''

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_cpf(self):
        return self.cpf

    def cadastrar(self,nome, sobrenome, cpf):
        #Foi utilizado o metodo cadastrar para complementar no cadastro
        super().cadastro(nome, sobrenome)
        self.cpf = cpf
