from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula34/Aula34-1')
from controller.endereco_controller import EnderecoController

app = Flask(__name__)
ec = EnderecoController()

@app.route('/')
def inicio():
    enderecos = ec.listar_todos()
    return render_template('index.html', lista = enderecos)

app.run()