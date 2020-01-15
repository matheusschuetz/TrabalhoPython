class Pessoa:
    ID = 0 
    Nome = ''
    Sobrenome = ''
    Idade = 0 
    Endereco_ID = 0 

    def exportar_txt(self, lista_pessoas):
        #-----Cria um arquivo e salva cada dicionario dentro dele
        with open('Aula33\Aula33-4pessoas33.txt', 'a') as arquivo:
            for p in lista_pessoas:
                arquivo.write(f"{str(p)}\n")
    def __str__(self):
        return f'{self.ID};{self.Nome};{self.Sobrenome};{self.Idade};{self.Endereco_ID}'