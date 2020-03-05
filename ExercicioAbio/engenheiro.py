from ExercicioAbio.pessoa import Pessoa

class Engenheiro(Pessoa):
    def __init__(self):
        super().__init__()
        self.__numero_registro = 0
        self.__apelido = ''

    def get_numero_registro(self):
        return self.__numero_registro

    def get_apelido(self):
        return self.__apelido
    