# Exercicio 2 - for
#Escreva um programa que leia um numero inteiro
numero = int(input('Digite um numero:'))
#Calcule a taboada do número informado
for i in range(0,11):
    print(f'{i} x {numero} = { i * numero}')
#Imprima a taboada com a conta completa (n * i = r)