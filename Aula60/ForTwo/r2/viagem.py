from Aula60.ForTwo.r2.embarque import embarque
from Aula60.ForTwo.r2.desembarque import desembarque

from Aula60.ForTwo.r2.terminal import Terminal
from Aula60.ForTwo.r2.aviao import Aviao
from Aula60.ForTwo.r2.local import Local
from Aula60.ForTwo.r2.fortwo import Fortwo

terminal = {'descricao':'terminal', 'pessoas': ['piloto','oficial1','oficial2','chefe de serviço','comissário1','comissário2','policial','presidiario']}
aviao = { 'descricao':'aviao', 'pessoas': [] }

def viagem(motorista:str, passageiro:str, saida:dict, chegada:dict):
    fortwo = embarque(motorista, passageiro, saida)
    print(f"Saindo do {saida['descricao']}")
    print('Iniciando a viagem...')
    print(f"Chegando no {chegada['descricao']}")
    print('Finalizando a viagem ...')
    # alto acoplamento
    desembarque(fortwo, chegada)
    print(saida)
    print(chegada)

def viagem2(pessoa1, pessoa2, origem: Local, destino: Local):
    fortwo = Fortwo()
    if origem.saida(pessoa2):
        if origem.saida(pessoa1):
            if fortwo.set_motorista(pessoa1):
                if fortwo.set_passageiro(pessoa2):
                    fortwo.viagem(origem, destino)
                    if destino.entrada(pessoa1):
                        if not destino.entrada(pessoa2):
                            print('Não permitido6')
                    else:
                        print('Não permitido5')
                else:
                    print('Não permitido4')
            else:
                print('Não permitido3')
        else:
            print('Não permitido2')
    else:
        print('Não permitido1')


t = Terminal()
v = Aviao()

viagem2('policial', 'presidiário', t, v)
print('-'*50)
viagem2('policial', '', v, t)
print('-'*50)
viagem2('piloto', 'policial', t, v)
print('-'*50)
viagem2('piloto', '', v, t)
print('-'*50)
viagem2('piloto', 'oficial1', t, v)
print('-'*50)
viagem2('piloto', '', v, t)
print('-'*50)
viagem2('piloto', 'oficial2', t, v)
print('-'*50)
viagem2('piloto', '', v, t)
print('-'*50)
viagem2('chefe de serviço', 'piloto', t, v)
print('-'*50)
viagem2('chefe de serviço', '', v, t)
print('-'*50)
viagem2('chefe de serviço', 'comissário1', t, v)
print('-'*50)
viagem2('chefe de serviço', '', v, t)
print('-'*50)
viagem2('chefe de serviço', 'comissário2', t, v)
