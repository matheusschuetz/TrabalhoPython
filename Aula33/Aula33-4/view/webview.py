from flask import Flask, render_template
import sys
sys.path.append('C:/Users/900152/Documents/Github/Dados/TrabalhoPython/Aula33/Aula33-4')
from controller.pessoa_controller import PessoaController

app = Flask(__name__)
pc = PessoaController()

@app.route('/')
def inicio():
    pessoas = pc.listar_todos()
    return render_template('index.html', lista = pessoas)

app.run()