#listas 
#Toda lista começa em 0 
lista1 = []
lista2 = ['Marcela', 'Nicole', '*Matheus', 10]
lista3 = [1,2,3,5]

#impressao das listas
print(lista1)
print(lista2)
print(lista3)

#adicionar uma lista dentro da outra(ou qualquer outro dado)
lista1.append(lista2)
lista1.append(lista3)

#impressao da lista alterada
print(lista1)

#fazer com que o usuário coloque dados dentro da lista
lista1.append(input('Digite aqui seu animal favorito:'))
print(lista1)

#pegar um dado especifico
print(lista2[2])

#usuario solicitar um dado em posição especifica
posicao = int(input('digite a posicao que voce deseja escolher:'))
print(lista2[posicao - 1])