#Classe é um tipo definido pelo usuario
#Ex

class Pessoa:
    def __init__(self):
        self.nome = ''
        self.sobrenome =''

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_sobrenome(self):
        return self.sobrenome

    def set_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome

    def cadastro(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p = Pessoa()
p.set_nome('Matheus')
print(p.get_nome())


