class Endereco:
    ID = 0
    Logradouro = ''
    Numero = ''
    Complemento = ''
    Bairro = ''
    Cidade = ''

    def exportar_txt(self, lista_endereco):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('Aula34/Aula34-1/endereco.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for p in lista_endereco:
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.ID};{self.Logradouro};{self.Numero};{self.Complemento};{self.Bairro};{self.Cidade}'