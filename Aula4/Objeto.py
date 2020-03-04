#Objeto é uma instancia da classe
#Ex

class Pessoa:
    def __init__(self):
        self.__nome = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

#Pessoa é um objeto
p = Pessoa()
print(p)