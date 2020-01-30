class PessoaDao:
    def list_all(self):
        return 'Listando todos'
    def get_by_id(self, id):
        return f'Selecionando pelo ID {id}'
    def insert(self, pessoa):
        return "Pessoa inserida"
    def update(self,pessoa):
        return "Atualizado"
    def delete(self,id):
        return "Pessoa Deletada"