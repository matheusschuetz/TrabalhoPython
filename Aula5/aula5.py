# Crie um programa que leia 4 notas
Nota1 = float(input('Digite a primeira nota do aluno:'))
Nota2 = float(input('Digite a segunda nota do aluno:'))
Nota3 = float(input('Digite a terceira nota do aluno:'))
Nota4 = float(input('Digite a quarta nota do aluno:'))
media = (Nota1 + Nota2 + Nota3 + Nota4) / 4
 
# imprima a maior e menor nota              
maior = Nota1                            #(ou você pode usar) Lista = [nota1 + nota2 + nota3 + nota4]
if maior < Nota2:                        #print('a maior nota foi:', max(lista)
    maior = Nota2
if maior < Nota3:
    maior = Nota3
if maior < Nota4:
    maior = Nota4

print('\n A maior nota do aluno foi:', maior)
menor = Nota1                           #(ou você pode usar) Lista = [nota1 + nota2 + nota3 + nota4]
if menor > Nota2:                       #print('a maior nota foi:', min(lista)
    menor = Nota2
if menor > Nota3:
    menor = Nota3
if menor > Nota4:
    menor = Nota4
print('\n A menor nota do aluno foi:', menor)

# Imprime a média
print('\n A média geral do aluno foi:', media)

# Imprima se o aluno foi aprovado ou reprovado (Media 7.0)
if media >= 7:
    print('\n O Aluno foi APROVADO')
else:
    print('\n O Aluno foi REPROVADO')
