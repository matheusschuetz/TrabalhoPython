import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula34/Aula34-1')
from controller.endereco_controller import EnderecoController
from controller.pessoa_controller import PessoaController
ec = EnderecoController()
pc = PessoaController()
for e in ec.listar_todos():
    print(e)
for p in pc.listar_todos():
    print(p)