banda= []
album = []
musica = []

menu = '''
=======================================================================================================
#                                    Rock In Rio                                                      #
=======================================================================================================
(1)Cadastro de Banda
(2)Cadastro do album
(3)Cadastro da musica
=======================================================================================================
(4)Sair
=======================================================================================================
Digite a opção que você gostaria
'''

while True:
    opcao = input(menu)
    if opcao == '1':
        nomeBanda = input('Insira o nome da banda que Você quer cadastrar\n')
        banda.append(nomeBanda)
    elif opcao == '2':
        nomeAlbum = input('Digite o nome do Album que você gostaria de cadastrar\n')
        album.append(nomeAlbum)
    elif opcao == '3':
        nomeMusica = input('Digite o nome da musica que você gostaria de Cadastrar\n')
        musica.append(nomeMusica)
    elif opcao == '4':
        print(f'Nome das bandas {banda}\nNomes dos Albuns {album}\nNome das Musicas{musica}')
        break
    else:
        print('Valor invalido, tente novamente')

