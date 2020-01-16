class Pessoa:
    ID = 0
    Nome = ''
    Sobrenome = ''
    Idade = 0
    endereco_ID = 0

    def exportar_txt(self, lista_pessoas):
        #----- Cria um arquivo e atribui a uma variável 'arquivo'
        with open('33-Aula33/Aula33-4/pessoas4.txt','a') as arquivo:
            #---- Percorre a lista de dicionário e salva no arquivo em formato pré-definido
            for p in lista_pessoas:
                arquivo.write(f"{str(p)}\n")
    
    def __str__(self):
        return f'{self.ID};{self.Nome};{self.Sobrenome};{self.Idade};{self.endereco_ID}'