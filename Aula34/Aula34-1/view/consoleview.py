import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula34/Aula34-1')
from controller.endereco_controller import EnderecoController

ec = EnderecoController()

for e in ec.listar_todos():
    print(e)