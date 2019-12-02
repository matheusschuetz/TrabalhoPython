menu = '''
=======================================================================================================
#                                    Festival da Cerveja de Ituroro                                   #
=======================================================================================================
(1)Cadastro de Clientes
(2)Ver Clientes Cadastrados
(3)Cadastro de Produtos
(4)Ver produtos Cadastrados
(5)Venda de Produtos
(6)Relatório de Vendas
=======================================================================================================
(7)Sair
=======================================================================================================
Digite a opção que você gostaria
'''
while True:
    opcao = input(menu)
    if opcao == '1':
        print('Cadastro de Clientes')
    elif opcao == '2':
        print('Ver Clientes Cadastrados')
    elif opcao == '3':
        print('Cadastro de Produtos')
    elif opcao == '4':
        print('Ver produtos Cadastrados')
    elif opcao == '5':
        print('Venda de Produtos')
    elif opcao =='6':
        print('Relatório de Vendas')
    elif opcao == '7':
        print('Sair')
    else:
        print('Valor invalido')
    break