from flask import Flask
from flask_restful import Api
from Aula41.Controller.pessoacontroller import PessoaController
app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa')

@app.route('/')
def inicio():
    return "Atividade Pessoa"

app.run(debug=True, port=80)
