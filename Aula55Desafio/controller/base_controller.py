from flask_restful import Resource

from Aula55.dao.base_dao import BaseDao

class BaseController(Resource):
    def __init__(self, dao:BaseDao):
        self.dao = dao

    def get(self, id=None):
        if id:
            return self.dao.get_by_id(id)
        return self.dao.list_all()

    def post(self, model):
        return  self.dao.insert(model)

    def put(self, model):
        return self.dao.update(model)

    def delete(self, id):
        return self.dao.delete(id)
