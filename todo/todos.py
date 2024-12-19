from todo.model import Todo

class TodoList:

    def __init__(self):
        self.todo_lost = []

    def add(self, task, category):
        self.todo = Todo(task, category)

        count = len(self.todo_lost)
        self.todo._position = count if count else 0
        self.todo_lost.append(self.todo)

    def get_todo_list(self):
        return self.todo_lost
    
    def complete(self, position):
        self.todo_lost[position - 1]._status = 2

    def delete(self, position):
        self.todo_lost.pop(position - 1)