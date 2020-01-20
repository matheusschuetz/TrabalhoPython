#---Elaborar uma manipulação de arquivo para marca, tipo e teor da cerveja
#---Usar dicionario e listas(semelhante ao 15.2)

def salvar_cerveja(cerveja_dicionario):
    arquivo = open('exercicio2.txt','x')
    arquivo.write(f"{cerveja_dicionario['marca']};{cerveja_dicionario['tipo']};{cerveja_dicionario['teor']}\n")
    arquivo.close()


def ler():
    lista = []
    arquivo = open('exercicio2.txt','r')
    for linha in arquivo:
        linha = linha.strip()
        lista_linha = linha.split(';')
        cerveja = {'marca':lista_linha[0],'tipo':lista_linha[1],'teor':lista_linha[2]}
        lista.append(cerveja)
    arquivo.close()
    return lista


marca = input('Digite a marca da sua cerveja: ')
tipo = input('Digite o tipo da cerveja: ')
teor = float(input('Digite o teor da cerveja:'))


cerveja = {'marca':marca,'tipo':tipo,'teor':teor}
salvar_cerveja(cerveja)

for i in ler():
    print(f"{i['marca']} - {i['tipo']} - {i['teor']}")


