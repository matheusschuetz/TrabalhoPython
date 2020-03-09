class VendinhaDoZe:
    def __init__(self):
        self.salgado = ''
        self.quantidade_de_salgados = 0
        self.valor_do_salgado = 3.50
        self.refrigerante = ''
        self.quantidade_de_refrigerantes = 0
        self.valor_do_refrigerante = 2.50


    def imprime_pedido(self):
        valor_total_dos_refrigerantes = calculo_valor_total_refrigerantes(self.quantidade_de_refrigerantes, self.valor_do_refrigerante)
        valor_total_dos_salgados = calculo_valor_total_salgados(self.quantidade_de_salgados, self.valor_do_salgado)
        valor_total_da_compra = calculo_valor_total_da_compra(valor_total_dos_salgados, valor_total_dos_refrigerantes)
        print('Seu pedido é: ')
        print(f'{self.quantidade_de_salgados} unidades de {self.salgado} no valor de {valor_total_dos_salgados}')
        print(f'{self.quantidade_de_refrigerantes} unidades de {self.refrigerante} no valor de {valor_total_dos_refrigerantes}')
        print(f'O valor total da compra é de R$ {valor_total_da_compra}')

    def realizar_pedido(self):
        self.salgado = input('Informe um salgado [coxinha/pastel/enroladinho]: ')
        self.quantidade_de_salgados = input('Informe quantas unidades de salgado: ')
        self.refrigerante = input('Informe um refrigerante [pepsi/sukita/guaraná]: ')
        self.quantidade_de_refrigerantes = input('Informe quantas unidades de refrigerante: ')

def calculo_valor_total_da_compra(valor_total_dos_salgados, valor_total_dos_refrigerantes):
    valor_total_da_compra = valor_total_dos_salgados + valor_total_dos_refrigerantes
    return valor_total_da_compra


def calculo_valor_total_salgados(quantidade_de_salgados, valor_do_salgado):
    valor_total_dos_salgados = quantidade_de_salgados * valor_do_salgado
    return valor_total_dos_salgados


def calculo_valor_total_refrigerantes(quantidade_de_refrigerantes, valor_do_refrigerante):
    valor_total_dos_refrigerantes = quantidade_de_refrigerantes * valor_do_refrigerante
    return valor_total_dos_refrigerantes
