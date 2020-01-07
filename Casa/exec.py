aviao = []
passageiro = []
vaero = False
piloto = []
terminal = ['comissaria1','comissaria2', 'piloto', 'oficial1', 'oficial2', 'chefe de serviço','policial', 'presidiario']
def adicinar_motorista(opcao, passeiro, vaero, aviao) :   
    if opcao == '1':
        if vaero == False:
            contador = 0
            for i in terminal:
                print(contador, i)
                contador += 1
            motorista = int(input(f'''Quem você gostaria de adicionar?'''))
            piloto.append(terminal.pop(motorista))
            print(f'{piloto[0]} embarcou no veiculo')
            
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
        passageiro.append(terminal.pop(escolhadnv))
        print(f'{passageiro[0]} embarcou no veículo')          
        
    elif escolha == '2':
        pass
    
    print('Veiculo esta andando')
    
    
    if vaero == False:
        print(f'1 - {piloto}\n2 - {passageiro}\n3 - todos')
        desembarque = input('Quem vai desembarcar?')
        if desembarque == '1':
            aviao.append(piloto.pop(0))
            print(f'{aviao[-1]} embarcou no avião')
        elif desembarque == '2':
            aviao.append(passageiro.pop(0))
        elif desembarque == '3':
            aviao.append(piloto.pop(0))
            aviao.append(passageiro.pop(0))
        
    elif vaero == True:
        print(f'1 - {piloto}\n2 - {passageiro}\n3 - todos')
        desembarque = input('Quem vai desembarcar?')
        if desembarque == '1':
            terminal.append(piloto.pop(0))
            print(f'{terminal[-1]} desembarcou no terminal')
            vaero = False
        elif desembarque == '2':
            terminal.append(passageiro.pop(0))
        elif desembarque == '3':
            terminal.append(piloto.pop(0))
            terminal.append(passageiro.pop(0))
        
    
    
    

    

       
        






while True:
    opcao = input('''##################################HBSIS AIRLINES##################################   
            Digite abaixo oque você gostaria de fazer...
            1 - adicionar piloto ao veiculo
            2 - mostrar pessoas do aviao
            3 - mostrar pessoas no terminal
            4 - mostrar quem esta no veiculo
    ''')
   
    if opcao == '1':
        adicinar_motorista(opcao, passageiro,vaero, aviao)
    elif opcao == '2':
        print(aviao)
    elif opcao == '3':
        print(terminal)
    elif opcao == '4':
        print(passageiro, piloto)