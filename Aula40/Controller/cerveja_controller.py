from flask_restful import Resource

class CervejaController(Resource):
    def get(self):
        return 'Acessando controladora pelo metodo HTTP GET'

    def post(self):
        return 'Acessando controladora pelo metodo HTTP POST'

    def put(self):
        return 'Acessando controladora pelo metodo HTTP PUT'

    def delete(self):
        return 'Acessando controladora pelo metodo HTTP DELETE'
