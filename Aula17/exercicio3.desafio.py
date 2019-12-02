#Pedir os dados: Cod do cliente, CPF, Nome completo, data de nascimento, Estado, CEP, bairro, rua, Numero da casa, complemento

def cadastro_cliente(numero):
    dados_cliente = ['Codigo_cliente', 'CPF', 'nome_completo', 'data de nascimento', 'Estado', 'Cidade', 'cep', 'bairro', 'rua', 'numero_da_casa', 
                    'complemento']
    lista = []
    for j in range(numero):
        dicionario = {}
        for i in dados_cliente:
            dicionario[i]=input(f'{i}: ')
        lista.append(dicionario)
    return lista

numero = int(input('Digite numero de cadastros:'))
lista_cadastro = cadastro_cliente(numero)

#Criar uma função para salvar em arquivo:

arquivo = open('Dados_clientes.txt','a')
for clientes in lista:
        cliente_chave = list(cliente.keys())
    for chaves in cliente:
        salva = 'f'{clientes[chaves]}'

arquivo.write(lista_cadastro)
arquivo.close
