from todo.model import Todo
from todo.db_handler import DBHandler

from todo import DB_READ_ERROR, DB_WRITE_ERROR

class TodoList:

    def __init__(self, db_path):
        self._db_handler = DBHandler(db_path)

    def add(self, task, category):
        self.todo = Todo(task, category)
        self.todo_list, read_error = self._db_handler.read_todos()
        if read_error == DB_READ_ERROR:
            return (self.todo, read_error)

        count = len(self.todo_lost)
        self.todo._position = count if count else 0
        self.todo_lost.append(self.todo)

        write_error = self._db_handler.write_todos(self.todo_list)

        return (self.todo, write_error)

    def get_todo_list(self):
        self.todo_list = self._db_handler.read_todos()
        return self.todo_lost
    
    def complete(self, position):
        self.todo_lost[position - 1]._status = 2

    def delete(self, position):
        self.todo_lost.pop(position - 1)