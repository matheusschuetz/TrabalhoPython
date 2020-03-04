#A herança é usada principalmente para a reaproveitação de codigo.
#A classe Cores esta herdando a Pessoa, entao dentro da classe Cores tem todos os metodos da Classe Pessoa

from Aula4.Classe import Pessoa


class Cores(Pessoa):
    def __init__(self):
        super().__init__()
        self.__cor = ''

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor

c = Cores()
#É possivel utilizar os metodos de pessoa
c.set_nome('Matheus')
c.set_cor('Azul')
print(f'{c.get_nome()} e {c.get_cor()}')