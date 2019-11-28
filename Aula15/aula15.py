#------Aula15
#------Manipulação de Arquivos
#----- O 'x' Serve para abrr um novo arquivo para nós escrevermos
#----- Salvamos o arquivo em uma variável, pois é necessário guardar o arquivo em algum local
#----- O 'w' Subscreve tudo que tem no arquivo, mantendo apenas aquilo que você esrever no 'w'
#-----O 'a' Adiciona tudo na mesma linha, podendo ser diversas vezes
# arquivo = open('aula.txt','a')
#----- Usamos o write para poder escrever no arquivo
# arquivo.write('Matheus Schuetz\n')
#----- Usamos arquivo.close usamos para fechar o arquvivo
# arquivo.close()

arquivo = open('aula.txt','r')
#-----Usamos o for para ler cada linha do arquivo
for linha in arquivo:
    print(linha)
arquivo.close()