aviao = []
passageiro = []
piloto = []
vaero = False
terminal = ['comissaria1','comissaria2', 'piloto', 'oficial1', 'oficial2', 'chefe de serviço','policial', 'presidiario']
def adicinar_motorista(opcao, passeiro, vaero):   
    if opcao == '1':
        if vaero == False:
            contador = 0
            for i in terminal:
                print(contador, i)
                contador += 1
            motorista = int(input(f'''Quem você gostaria de adicionar?'''))
            piloto.append(terminal[motorista])
            print(f'{piloto[0]} embarcou no veiculo')
            terminal.remove(terminal[motorista])
            
        elif vaero == True:
            contador = 0
            for i in aviao:
                print(contador, i)
                contador += 1
            motorista = int(input(f'Quem você gostaria de adicionar?'))
            piloto.append(aviao[motorista])
            print(f'{piloto[0]} embarcou no veiculo')
            aviao.remove(aviao[motorista])   
                
    escolha = input('''Deseja adicionar passageiro?
            1 - Sim
            2 - Não''')
    if escolha == '1':
        contador = 0
        for i in terminal:
            print(contador, i)
            contador += 1
        escolhadnv = int(input('Quem você gostaria de adicionar?'))
        passageiro.append(terminal[escolhadnv])
        print(f'{terminal[escolhadnv]} embarcou no veículo')            
        terminal.remove(terminal[escolhadnv])
    elif escolha == '2':
        pass
    print('Veiculo esta andando')
    vaero = True
    print(f'1 - {piloto}\n2 - {passageiro}')
    desembarque = input('Quem vai desembarcar?')
    if desembarque == '1':
        aviao.append(piloto)
        aviao.append(passageiro)
        piloto.clear()
        passageiro.clear()
    else:
        pass
    

       
        






while True:
    opcao = input('''##################################HBSIS AIRLINES##################################   
            Digite abaixo oque você gostaria de fazer...
            1 - adicionar piloto ao veiculo
            2 - mostrar pessoas do aviao
            3 - mostrar pessoas no terminal
            4 - mostrar quem esta no veiculo
    ''')
   
    if opcao == '1':
        adicinar_motorista(opcao, passageiro, vaero)
    elif opcao == '4':
        print(passageiro, piloto)