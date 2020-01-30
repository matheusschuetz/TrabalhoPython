from flask_restful import Resource

class PessoaController(Resource):
    def get(self):
        return "Retornando com o metodo GET"
    def post(self):
        return "Retornando com o metodo POST"
    def put(self):
        return "Retornando com o metodo PUT"
    def delete(self):
        return "Retornando com o Metodo DELETE"