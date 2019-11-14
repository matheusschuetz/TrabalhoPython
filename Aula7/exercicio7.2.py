#Escreva um programa  que leia os dados de 11 jogadores
#Jogador: Nome, Posicao, Numero, PernaBoa
#Crie um dicionario para armazenar os dados
# Imprima os jogadores e seus dados


lista_jogadores = []
for i in range(1,12):
    jogador = {}
    jogador['Nome'] = input('Digite o nome do jogador')
    jogador['Posicao'] = input('Digite a Posicao')
    jogador['Numero'] = input('Digite o Numero')
    jogador['PernaBoa'] = input('Digite o lado da PernaBoa')
    lista_jogadores.append(jogador)
print('\n')
for i in lista_jogadores:
    print('Nome:',i['Nome'],'Posicao:',i['Posicao'],'Numero:',i['Numero'], 'Lado da Perna',i['PernaBoa'])


