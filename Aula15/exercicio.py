#---Criar um arquivo txt
#---ler do console
#---Armazenar numa variavel 
arquivo = open('exercicio.txt', 'a')

#----- Coloquei o for para a pessoa escrever mais vezes seguidas sem ter que executar o programa de novo
#-----Eu poderia colocar o input dentro do arquivo.write pra não precisar criar uma variavel(porém prestar atenção nas aspas)
for i in range(2):
    texto = input('Digite algo que queira colocar em um arquivo texto:')
    arquivo.write(f'{texto}\n')


arquivo = open('exercicio.txt', 'r')
for linha in arquivo:
    print(linha)
arquivo.close()
