#Web2
#Crie um programa que:
# Leia dois numeros inteiros
# Calcule a soma entre os dois numeros atraves de um metodo
# Calcule a subtração entre os dois numeros atraves de um metodo
# Calcule a multiplicação entre os dois numeros atraves de um metodo
# Calcule a divisão inteira entre os dois numeros atraves de um metodo
# Calcule resto da divisao entre os dois numeros atraves de um metodo
# Calcule a raiz fracionada entre os dois numeros atraves de um metodo
# Separa os metodos em outro arquivo


from calculoExercicio import soma,sub, multi, div,div_fra, rest_div,raiz
cabeçalho = '=' * 50

x = int(input('Digite um número qualquer:'))
y = int(input('Digite outro número qualquer:'))

print(f'Soma:{soma(x,y)}\n{cabeçalho}\nSubtração:{sub(x,y)}\n{cabeçalho}\nMultiplicação:{multi(x,y)}\n{cabeçalho}\nDivisão:{div(x,y)}\n{cabeçalho}\nDivisão Francionada:{div_fra(x,y)}\n{cabeçalho}\nResto da Divisão:{rest_div(x,y)}\n{cabeçalho}\nRaiz Entre os dois números:{raiz(x,y)}\n{cabeçalho}')
