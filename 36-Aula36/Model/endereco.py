class Endereco:
    id = 0
    logradouro = ''
    numero = ''
    complemento = ''
    bairro = ''
    cidade = ''

    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade}'