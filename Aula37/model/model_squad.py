class Squad:
    ID = 0
    Nome = ''
    Descricao = ''
    NumeroPessoas = 0 
    LinguagemBackEnd = ''
    FrameworkFrontEnd = ''

    def __str__(self):
        return f'{self.ID};{self.Nome};{self.Descricao};{self.NumeroPessoas};{self.LinguagemBackEnd};{self.FrameworkFrontEnd}'



