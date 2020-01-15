def exportar_txt(lista_pessoas):
    #-----Cria um arquivo e salva cada dicionario dentro dele
    with open('Aula33\Aula33-3pessoas33.txt', 'a') as arquivo:
        for p in lista_pessoas:
            arquivo.write(f"{p['ID']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['Endereco_ID']}\n")
