from flask_restx import Namespace, fields

class HelloModel():
    ns = Namespace('hello', description = 'hello namespace')
    hello = ns.model('hello', {
        'id' : fields.Integer(readonly=True, description='The task unique identifier'),
        'text' : fields.String(required=True, description='text')
    })