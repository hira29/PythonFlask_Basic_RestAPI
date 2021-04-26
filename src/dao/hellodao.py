from src.model.hellomodel import HelloModel

Model = HelloModel()
todo = Model.hello

class HelloDao(object):
    def __init__(self):
        self.counter = 0
        self.todos = []

    def getall(self):
        return self.todos

    def get(self, id):
        for todo in self.todos:
            if todo['id'] == id:
                return todo
        response = {
            'status': 'fail',
            'message': 'error',
        }
        return response, 409

    def create(self, data):
        todo = data
        todo['id'] = self.counter = self.counter + 1
        self.todos.append(todo)
        return todo

    def update(self, id, data):
        todo = self.get(id)
        todo.update(data)
        return todo

    def delete(self, id):
        todo = self.get(id)
        self.todos.remove(todo)
        return todo