# Exercicio 3 - foreach
#Escreva um programa que leia as notas (4) de 10 alunos
#Armazene as notas e os nomes em listas
#Imprima:
 #       1- o nome do aluno
 #       2- Média do aluno
 #       3-Resultado (Aprovado>=7.0)

nomes = []
notas = []


for i in range(3):
    aluno = input(f'digite o nome do aluno{i}: ')
    nomes.append(aluno)
    listaVazia = []
    for j in range(4):
        notaAluno = float(input(f'Digite a nota{j} do {aluno}: '))
        listaVazia.append(notaAluno)
    notas.append(listaVazia)

for numeroAluno
    media = 0 
    for notaAluno2 in listaNotas:
        media = media + notaAluno2 
    media = media / 4

    if media >= 7:
        print(f'O Aluno {nomeAluno2} com a média{media} foi Aprovado')
    else:
        print(f'O aluno {nomeAluno2} com a média{media} foi Reprovado') 


print(nomes)
print(notas)

    
    