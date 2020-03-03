class Endereco:
    def __init__(self):
        self.__logradouro = ''
        self.__numero = ''
        self.__bairro = ''

    def get_logradouro(self) -> str:
        return self.__logradouro

    def get_numero(self) -> str:
        return self.__numero

    def get_bairro(self) -> str:
        return self.__bairro

    def set_logradouro(self, logradouro: str) -> None:
        self.__logradouro = logradouro

    def set_numero(self, numero: str) -> None:
        self.__numero = numero

    def set_bairro(self, bairro: str) -> None:
        self.__bairro = bairro
