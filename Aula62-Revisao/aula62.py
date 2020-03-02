class Operacoes:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def soma(self):
        resultado = self.n1 + self.n2
        return resultado


numero_1 = int(input('Digite um numero:\n'))
numero_2 = int(input('Digite mais um numero:\n'))
objeto = Operacoes(numero_1, numero_2)
print(f'O resultado da soma de {numero_1} + {numero_2} é = {objeto.soma()}')
