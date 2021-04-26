from flask import request
from flask_restx import Resource

from src.model.hellomodel import HelloModel
from src.dao.hellodao import HelloDao

Model = HelloModel()
Dao = HelloDao()
Dao.create({'text': "Hello World"})

api = Model.ns
_hello = Model.hello

@api.route('/')
class HelloList(Resource):
    @api.doc('list_all_hello')
    @api.marshal_list_with(_hello, envelope='data')
    def get(self):
        """List all Hello"""
        return Dao.getall()

    @api.doc('create_hello_greet')
    @api.response(201, 'Hello Greet Created!')
    @api.expect(_hello, validate=True)
    @api.marshal_with(_hello)
    def post(self):
        """Create Hello Greet"""
        data = request.json
        return Dao.create(data)