#Encapsulamento é usado para tornar a variavel de uma classe privada, para nao haver modo de ser usada externamente. para se ter acesso
#É utilizado metodos get e set

class Pessoa:
    def __init__(self):
        self.__nome = ''

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


p = Pessoa()
#Para poder definir o nome usamos o metodo set_nome
p.set_nome('Matheus')
#Para termos acesso a esse nome utilizamos o metodo get
print(p.get_nome())