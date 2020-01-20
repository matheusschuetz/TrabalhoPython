#Aula16 
#??????
#As variaveis ficam salvas na memoria RAM
#Cadastro de playlist
#lendo musica, artista e album
#Dar sempre um Ctrl + Espaço para ver se esta identificando
from faixa import criar_faixa,salvar_faixa, ler_faixa

musica = input('Digite uma musica:')
album = input('Digite o nome do album:')  
artista = input('Digite o artista:')
                  

faixa1 = criar_faixa(musica, album, artista)
salvar_faixa(faixa1)
lista = ler_faixa()

for faixa in lista:
    print(f'{faixa["musica"]} - {faixa["album"]} - {faixa["artista"]}')