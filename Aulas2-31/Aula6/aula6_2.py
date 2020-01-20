#Estruturas de repetição - FOR


#--- for simples usando range com incremento padrao 1
    for i in range(0,10):
    print(f'{i}-Padawans HbPy')

#--- for simples usando range com incremento padrao 1
for i in range(0,100,2):
    print(f'{i}-Pares')

#for em lista usando range
lista = ['Matheus', 'Matheus','Marcela','Nicole','Tonho', 'Pablo']
for i in range(0,6):
    print(lista[i])

lista.append('Natan')
for sortudo in lista:
    print(sortudo)

#for usando os elementos da própria lista (foreach)
numero = 10
for i in range(0,11):
    print(f'{i} x {numero} = {i * numero}')

