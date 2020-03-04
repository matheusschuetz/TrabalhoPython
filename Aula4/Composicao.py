#Composicao pode ser a criação de um objeto numa outra classe, conforme o exemplo

from Aula4.Classe import Pessoa

class Cores:
    def __init__(self):
        self.__cor = ''
        #Composição do objeto da classe Pessoa
        self.__pessoa = Pessoa()

    def get_cor(self):
        return self.__cor

    def set_cor(self, cor):
        self.__cor = cor
