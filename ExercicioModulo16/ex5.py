#--- Exercício 5 - Funções - 1
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console e armazene em uma variável
#--- Realize o calculo da raiz e armazene em uma segunda variável
#--- Imprima o resultado e uma mensagem usando f-string (módulo 3)
from Funções import raiz
x = int(input('Digite um número muito legal para calcular a raiz:'))
y = int(input( 'Digite o indice da raiz:'))

print(f'O resultado da raiz é pelos meus calculos{raiz(x,y)}')
