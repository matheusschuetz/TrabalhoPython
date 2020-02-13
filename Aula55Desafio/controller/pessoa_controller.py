from flask import request

from Aula55.controller.base_controller import BaseController
from Aula55.dao.pessoa_dao import PessoaDao
from Aula55.model.pessoa import Pessoa

class PessoaController(BaseController):
    def __init__(self):
        super().__init__(PessoaDao())

    def post(self):
        return super().post(self.carrega_parametros())

    def put(self, id):
        model = self.carrega_parametros()
        model.id = id
        return super().put(model)

    def carrega_parametros(self):
        model = Pessoa()
        model.nome = request.json['nome']
        model.sobrenome = request.json['sobrenome']
        model.data_nascimento = request.json['data_nascimento']
        model.naturalidade = request.json['naturalidade']
        return model
