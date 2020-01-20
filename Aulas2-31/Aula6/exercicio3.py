# Exercicio 3 - foreach
#Escreva um programa que leia as notas (4) de 10 alunos
#Armazene as notas e os nomes em listas
#Imprima:
 #       1- o nome do aluno
 #       2- Média do aluno
 #       3-Resultado (Aprovado>=7.0)

lista1 = []
nota1 = []
nota2 = []
nota3 = []
nota4 = []

for i in range(1,5):
    nome = input(f'digite o nome do aluno em sequencia nome{i}: ')
    lista1.append(nome)
for i in range(1,5):
    valor = int(input(f'Digite a nota{i} do aluno1: '))
    nota1.append(valor)
for i in range(1,5):
    valor = int(input(f'Digite a nota{i} do aluno2: '))
    nota2.append(valor)
for i in range(1,5):
    valor = int(input(f'Digite a nota{i} do aluno3: '))
    nota3.append(valor)
for i in range(1,5):
    valor = int(input(f'Digite a nota{i} do aluno4: '))
    nota4.append(valor)    


resultadoaluno1 = (nota1[0] + nota2[1] + nota3[2] + nota4[3]) / 4
print('A média do aluno1 foi:', resultadoaluno1 )
resultadoaluno2 = (nota1[1] + nota2[1] + nota3[1] + nota4[1]) / 4
print('A média do aluno2 foi:', resultadoaluno2)
resultadoaluno3 = (nota1[2] + nota2[2] + nota3[2] + nota4[2]) / 4
print('A média do aluno3 foi:', resultadoaluno3)
resultadoaluno4 = (nota1[3] + nota2[3] + nota3[3] + nota4[3]) / 4
print('A média do aluno3 foi:', resultadoaluno4)