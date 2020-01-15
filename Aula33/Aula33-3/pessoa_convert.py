def converter_pessoas_dicionario(lista_tuplas):
    #-----criação de uma lista que adiciona os dicionarios
    lista_pessoas = []
    for p in lista_tuplas:
        #-----Criação do dicionario que representa o nome pessoa
        dicionario_pessoa = {'ID':0,'Nome':'','Sobrenome':'','Idade':0,'Endereco_ID':0}
        #-----Pega cada dicionario e atribui a uma posição
        dicionario_pessoa['ID'] = p[0]
        dicionario_pessoa['Nome'] = p[1]
        dicionario_pessoa['Sobrenome'] = p[2]
        dicionario_pessoa['Idade'] = p[3]
        dicionario_pessoa['Endereco_ID'] = p[4]
        #-----Adiciona cada dicionario na lista
        lista_pessoas.append(dicionario_pessoa)
    return lista_pessoas