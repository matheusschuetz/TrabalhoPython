from Aula63.Ex9 import Pessoa


class PessoaFisica(Pessoa):
    def __init__(self):
        super().__init__()
        self.__cpf = ''

    def set_cpf(self, cpf: str) -> None:
        self.__cpf = cpf

    def get_cpf(self) -> str:
        return self.__cpf
