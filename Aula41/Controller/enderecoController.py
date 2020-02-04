from flask_restful import Resource
from flask import request

from Aula41.Model.enderecoModel import Endereco
from Aula41.dao.enderecoDao import EnderecoDao

class EnderecoController(Resource):
    def __init__(self):
        self.dao = EnderecoDao()

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        endereco = Endereco(logradouro, numero, complemento, bairro, cidade)
        return = self.dao.insert(endereco)

    def put(self,id):
        logradouro = request.json['logradouro']
        numero = request.json['numero']
        complemento = request.json['complemento']
        bairro = request.json['bairro']
        cidade = request.json['cidade']
        endereco = Endereco(logradouro, numero, complemento, bairro, cidade, id)
        msg = self.dao.update(endereco)
        return msg

    def delete(self,id):
        return self.dao.delete(id)


