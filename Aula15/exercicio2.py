#---Elaborar uma manipulação de arquivo para marca, tipo e teor da cerveja
#---Usar dicionario e listas(semelhante ao 15.2)




def salvar_cerveja(conjunto):
    cerveja = conjunto 
    arquivo = open('exercicio2.txt','a')
    arquivo.write(cerveja)
    

marca = input('Digite a marca da cerveja:')
tipo = input('Digite o tipo da cerveja:')
teor = float(input('Digite o teor de alcool da bebida:'))
cerveja = f'{marca};{tipo};{teor}'
    
salvar_cerveja(cerveja)



