#Metodos definem um comportamento, podendo ser soma, subtração, concatenação e etc...
#Ex:
class Soma:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def adicao(self):
        resultado = self.n1 + self.n2
        return resultado

s = Soma(1, 2)
print(s.adicao())
