
class Endereco:
    def __init__(self,logradouro, numero, complemento, bairro, cidade, id=  None):
        self.id = id
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade