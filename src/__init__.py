from flask import Flask, Blueprint
from flask_restx import Api

from .config import config_name

from .controller.hellocontroller import api as hello_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK REST API ',
          version='1.0',
          description='service for CV'
          )

api.add_namespace(hello_ns, path='/hello')


def main_app(config):
    app = Flask(__name__)
    app.config.from_object(config_name[config])

    return app
