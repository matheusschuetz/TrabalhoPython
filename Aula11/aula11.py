#Prova

#1-Crie um programa que calcule o imposto ISS de um serviço de desenvolvimento de software
#-utilizar métodos
#2-Crie um programa que calcule a rentabilidade anual de um investimento beasendo-se na rentabilidade mensal(juros compostos)
#-a rentabilidade deve ser apresentada em % e R$
#Utilizar metodos
#3-
#utlizar métodos
#4-
#utilizar métodos
#5-
#utilizar métodos

from calculos import calculo_iss

linha = '=' * 50
print(f'{linha}\nCalculadora de ISS sobre serviços de software\n{linha}')
valor = float(input('Insira o valor do seu serviço:\n'))
valor_iss = calculo_iss(valor)
print(f'O valor do ISS será de:{valor_iss}')