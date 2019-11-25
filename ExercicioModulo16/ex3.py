#--- Exercício 3  - Funções - 1
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)
#--- Deve ser impresso apenas duas cadas após a vírgula
from Funções import media

x = float(input('Digite um numero aqui por obsequio:'))
y = float(input('Digita mais um por favore:'))
z = float(input('Digita um terceiro plis:'))

print(f'A Média entre esses 3 grandes números é:{media(x,y,z):.2f}')
