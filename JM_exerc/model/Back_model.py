class BackEnd:
    def __init__(self, id, Nome, Descricao, Versao):
        self.ID = id
        self.Nome = Nome
        self.Descricao = Descricao
        self.Versao = Versao

    def __str__(self):
        return  f"{self.ID},{self.Nome},{self.Descricao},{self.Versao}"