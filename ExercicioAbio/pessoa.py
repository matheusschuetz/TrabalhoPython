from ExercicioAbio.endereco import Endereco


class Pessoa:
    def __init__(self):
        self.__nome = ''
        self.__sobrenome = ''
        self.__idade = 0
        self.__endereco = Endereco()

    def get_nome(self) -> str:
        return self.__nome

    def get_sobrenome(self) -> str:
        return self.__sobrenome

    def get_idade(self) -> int:
        return self.__idade

    def set_nome(self, nome: str) -> None:
        self.__nome = nome

    def set_sobrenome(self, sobrenome: str) -> None:
        self.__sobrenome = sobrenome

    def set_idade(self, idade: int) -> None:
        self.__idade = idade

    def salario(self,valor,numero_horas):
        custo = valor * numero_horas
        return custo

    # def salario(self):
    #     pass