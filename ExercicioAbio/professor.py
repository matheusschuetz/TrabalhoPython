from ExercicioAbio.pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self):
        super().__init__()
        self.__numero_registro = 0
        self.__valor_hora = 25.0

    def get_numero_registro(self) -> int:
        return self.__numero_registro

    def get_valor_hora(self) -> float:
        return self.__valor_hora

    def set_numero_registro(self, numero_registro: str) -> None:
        self.__numero_registro = numero_registro

    def set_valor_hora(self, valor_hora: str) -> None:
        self.__valor_hora = valor_hora

    def salario(self, horas: float) -> float:
        return horas * self.__valor_hora