#Aula 7 
#Dicionarios

lista = []
# dicionario = {'Nome':'Matheus', 'Sobrenome': 'Schuetz' }
# print(dicionario)
# print(dicionario['Sobrenome'])


nome = 'Maria'
lista_notas = [10,20,50,70]
media = sum(lista_notas)/len(lista_notas)
situacao = 'Reprovado'
if media >=7:
    situacao = 'Aprovado'
dicionario_alunos = {'Nome':nome, 'Lista_Notas':lista_notas, 'Media':media, 'Situacao':situacao}
print(f"{dicionario_alunos['Nome']} - {dicionario_alunos['Situacao']}")

