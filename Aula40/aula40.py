#Usar o Where para poder conferir se o pip esta executando no ambiente virtual

from flask import Flask
from flask_restful import Api
from Controller.cerveja_controller import  CervejaController
app = Flask(__name__)
api = Api(app)

api.add_resource(CervejaController, '/api/cerveja')

@app.route('/')
def inicio():
    return 'Bem vindo a API'

app.run(debug=True, port=80)
