from flask import Flask
from flask_restful import Api


from Aula41.Controller.pessoacontroller import PessoaController
from Aula41.Controller.enderecoController import EnderecoController
app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')
api.add_resource(EnderecoController, '/api/endereco', endpoint='enderecos')
api.add_resource(EnderecoController, '/api/endereco/<int:id>', endpoint='endereco')

@app.route('/')
def inicio():
    return "Atividade Pessoa/Endereco"

app.run(debug=True, port=80)
