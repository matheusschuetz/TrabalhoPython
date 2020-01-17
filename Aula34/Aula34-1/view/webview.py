from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula34/Aula34-1')
from controller.endereco_controller import EnderecoController
from controller.pessoa_controller import PessoaController

app = Flask(__name__)
pc = PessoaController()
ec = EnderecoController()



@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    enderecos = ec.listar_todos()
    return render_template('index.html', lista = enderecos, lista2 = pessoas)

app.run()