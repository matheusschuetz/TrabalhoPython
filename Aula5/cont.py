#Solicitar nome  do Funcionario

nome = input('Por favor, insira seu nome:')

#Solicitar idade

idade = int(input('Agora insira sua idade:'))

#Informar se ele pode beber 
if idade >= 18:
    print('Você pode consumir bebidas alcoolicas')
else:
    print('você não pode comprar produtos alcoolicos')

#Solicitar nome do Produto
produto = input('qual produto você deseja consumir?:')

#Solicitar a categoria
print('utilize os números para escolher:')
categoria = int(input('Você quer produtos com alcool(1) ou sem alcool(2)?:'))

#Exibir produto cadastrado
if categoria == 1 and idade >= 18:
   bebida = int(input('Nós temos: \n cerveja(1) \n cachaça(2) \n vinho(3) \n'))
   if bebida == 1:
       print('ok, cerveja comprada')
   if bebida == 2:
        print('ok, cachaça comprada')
   if bebida == 3:
        print('ok, vinho comprado')

if categoria == 2:
    bebida = int(input('nós temos: \n coca-cola(1) \n guaraná(2) \n pepsi(3) \n'))
    if bebida == 1:
       print('ok, coca-cola comprada')
    if bebida == 2:
        print('ok, guaraná comprada')
    if bebida == 3:
        print('ok, pepsi comprada')
