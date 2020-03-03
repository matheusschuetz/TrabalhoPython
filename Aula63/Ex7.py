# Crie um método que receba dois parâmetros do tipo string
# verifique se o primeiro parâmetro esta dentro da lista
# caso o parâmetro esteja na lista substitua o dado pelo segundo parâmetro dentro da lista
# retorne informando que o dado foi alterado
# caso não encontre retorne informando que o dado não foi encontrado na lista

# Leia o nome de uma pessoa no console para realizar a alteração
# Leia o novo nome da pessoa
# Realize a chamada do método enviando o nome antigo e o novo nome

lista = ['Matheus']
def listagem(par1: str, par2: str):
    if par1 in lista:
        lista[lista.index(par1)] = par2
        print(f'Valor alterado com sucesso!!\n{par1} se tornou {par2}')
        return lista
    print('Valor não encontrado :(')
    return

