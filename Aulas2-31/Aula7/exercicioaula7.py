#Escreva um programa que leia dados de cerveja
#Cerveja: marca, Tipo, IBU, AVB, EBC, Volume
#Crie um dicionario para armazenar dados
#Imprima os dados do dicionário (não dicionario completo)

cerveja = {}

cerveja['nome'] = input('Digite o nome da cerveja:')
cerveja['Tipo'] = input('Digite o tipo da cerveja')
cerveja['IBU'] = float(input('Digite o IBU da cerveja:'))
cerveja['ABV'] = float(input('Digite o ABV da cerveja:'))
cerveja['EBC'] = float(input('Digite o EBC da cerveja:'))
cerveja['Volume'] = float(input('Digite o Volume da cerv] eja:'))

print(f"Nome:{cerveja['nome']}\n Tipo: {cerveja['Tipo']}\n IBU: {cerveja['IBU']}\n ABV: {cerveja['ABV']}\n EBC: {cerveja['EBC']}\n Volume: {cerveja['Volume']}")



dicionario_bandas = {}
dicionario_bandas['Nome'] = 'Calipso'
print(dicionario_bandas)

dicionario = {'Nome':'Matheus', 'Sobrenome': 'Schuetz' }
dicionario['Sobrenome'] = 'Aviz'
dicionario['CPF'] = '120.053.953-32'  
print(dicionario)

dicionario_pessoa = {'Nome':'', 'Sobrenome':'', 'CPF':'', 'RG':''}
lsta_pessoas = []
for i in range(1,11):
    dicionario_pessoa['Nome'] = input('Digite o nome:')
    dicionario_pessoa['Sobrenome'] = input('Digite o Sobrenom:')
    dicionario_pessoa['CPF'] = input('Digite o CPF:')
    dicionario_pessoa['RG'] = input('Digite o RG:')
    lista_pessoas.append(dicionario_pessoa)

