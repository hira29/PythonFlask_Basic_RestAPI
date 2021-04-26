import os
import unittest

from src import main_app, blueprint

app = main_app(os.getenv('RUN_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

if __name__ == '__main__':
    app.run()
    
