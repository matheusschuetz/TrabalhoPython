aviao = []
passageiro = []
vaero = False
piloto = []
terminal = []

with open('Lucas_Matheus\Terminal.txt', 'r') as d:
    for i in d:
        terminal.append(i.strip())
with open('Lucas_Matheus\Aviao.txt', 'r') as e:
    for i in e:
        terminal.append(i.strip())






def adicinar_motorista(opcao, passeiro, vaero, aviao) :   
    
    if opcao == '1':
        if vaero == False:
            contador = 0
            for i in terminal:
                print(contador, i)
                contador += 1
            motorista = int(input(f'''Quem você gostaria de adicionar?'''))
            piloto.append(terminal.pop(motorista))
            print(f'=================\n{piloto[0]} embarcou no veiculo\n=================')
            
        elif vaero == True:
            contador = 0
            for i in aviao:
                print(contador, i)
                contador += 1
            motorista = int(input(f'Quem você gostaria de adicionar?'))
            piloto.append(aviao[motorista])
            print(f'=================\n{piloto[0]} embarcou no veiculo\n=================')
            aviao.remove(aviao[motorista])   
def adicionar_passageiro(terminal):
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
        print(f'=================\n{passageiro[0]} embarcou no veiculo\n=================')          
        
    elif escolha == '2':
        pass
def veicuolo_movimento():
    import time
    print('Veiculo esta andando')
    for i in range(3):
        time.sleep(1)
        print('.')
        
    
def desembarque(piloto, passageiro,vaero):   
    if vaero == False:
        aviao.append(piloto.pop(0))
        print(f'{aviao[-1]} embarcou no avião')
        if passageiro:
            aviao.append(passageiro.pop(0))
            print(f'{aviao[-1]} embarcou no avião')
    
        vaero = True
            
    elif vaero == True:
        terminal.append(piloto.pop(0))
        print(f'{terminal[-1]} desembarcou no terminal')
        if passageiro: 
            terminal.append(passageiro.pop(0))
            print(f'{terminal[-1]} desembarcou no terminal')
        
        
        vaero = False
    return vaero
    


while True:
    opcao = input('''##################################HBSIS AIRLINES##################################   
            Digite abaixo oque você gostaria de fazer...
            1 - adicionar piloto ao veiculo
            2 - mostrar pessoas do aviao
            3 - mostrar pessoas no terminal
            4 - mostrar quem esta no veiculo
##################################HBSIS AIRLINES##################################
    ''')
   
    if opcao == '1':
        adicinar_motorista(opcao, passageiro,vaero, aviao)
        adicionar_passageiro(terminal)
        veicuolo_movimento()
        vaero = desembarque(piloto, passageiro,vaero)
        
    elif opcao == '2':
        print(aviao)
    elif opcao == '3':
        print(terminal)
    elif opcao == '4':
        print(passageiro, piloto)


    a = open('Lucas_Matheus\Terminal.txt', 'w') 
    for i in terminal:
        a.write(i)
        a.write('\n')
    a.close()
    b = open('Lucas_Matheus\Aviao.txt', 'w') 
    for j in aviao:
        b.write(j)
        b.write('\n')
    b.close()


