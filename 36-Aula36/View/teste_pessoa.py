import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/36-Aula36')
from Controller.pessoa_controller import PessoaController
from Model.pessoa import Pessoa

pessoa = Pessoa()
pessoa.nome = 'Draeta1'
pessoa.sobrenome = 'Lindao'
pessoa.idade = 49
pessoa.endereco.logradouro = 'Rua dos Pombos1'
pessoa.endereco.numero = '0'
pessoa.endereco.complemento = 'casa muito engraçada'
pessoa.endereco.bairro = 'sem nome'
pessoa.endereco.cidade = 'gaspar'


controller = PessoaController()
id_salvo = controller.salvar(pessoa)
pessoa_endereco = controller.buscar_por_id(id_salvo)
print(pessoa_endereco)