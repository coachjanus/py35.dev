from todo.model import Todo

class TodoList:

    def __init__(self):
        self.todo_lost = []

    def add(self, todo: Todo):

        count = len(self.todo_lost)
        todo._position = count if count else 0
        self.todo_lost.append(todo)

    def get_todo_list(self):
        return self.todo_lost
    
    def complete(self, position):
        self.todo_lost[position - 1]._status = 2