# Exercicio 3 - foreach
#Escreva um programa que leia as notas (4) de 10 alunos
#Armazene as notas e os nomes em listas
#Imprima:
 #       1- o nome do aluno
 #       2- Média do aluno
 #       3-Resultado (Aprovado>=7.0)

lista1 = []
lista2 = []
for i in range(1,11):
    nome = input(f'digite o nome do aluno em sequencia nome{i}: ')
    lista1.append(nome)
    nota1 = input(f'Digite a nota1 do aluno{i}:')
    lista2.append(nota1)
print(lista1)
print(lista2)