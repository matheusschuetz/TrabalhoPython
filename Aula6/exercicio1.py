# Exercicio 1 - Listas
#Escreva um programa que leia o nome de 10 alunos #Armazene os nomes em uma lista #Imprima a lista
lista1 = []
for i in range(1,11):
    nome = input(f'digite o nome do aluno em sequencia nome{i}: ')
    lista1.append(nome)
print(lista1)
    
