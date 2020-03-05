class Endereco:
    def __init__(self):
        self.__logradouro = ''
        self.__numero = 0
        self.__cidade = ''
        self.__estado = ''

    def get_logradouro(self) -> str:
        return self.__logradouro

    def get_numero(self) -> int:
        return self.__numero

    def get_cidade(self) -> str:
        return self.__cidade

    def get_estado(self) -> str:
        return self.__estado

    def set_logradouro(self, logradouro: str) -> None:
        self.__logradouro = logradouro

    def set_numero(self, numero: int) -> None:
        self.__numero = numero

    def set_cidade(self, cidade: str) -> None:
        self.__cidade = cidade

    def set_estado(self, estado: str) -> None:
        self.__estado = estado
