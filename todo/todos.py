from todo.model import Todo
from todo.db_handler import DBHandler
from pathlib import Path
import datetime

from todo import DB_READ_ERROR, DB_WRITE_ERROR, ID_ERROR

from todo.current_todo import CurrentTodo
from typing import Any, Dict, List, NamedTuple

class TodoList:

    def __init__(self, db_path: Path) -> None:
        self._db_handler = DBHandler(db_path)

    def add(self, task: List[str], category: str) -> CurrentTodo:
        """Add a new to-do to the database."""
        task = " ".join(task)
        if not task.endswith("."):
            task += "."
        
        read = self._db_handler.read_todos()
        
        if read.error == DB_READ_ERROR:
            return CurrentTodo(self.todo, read.error)
        
        count = len(read.todo_list)

        todo = Todo(task=task, category=category, position=count)
        # print("New TODO: ", todo)

        read.todo_list.append(todo)

        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)
   

    def get_todo_list(self) -> List[Dict[str, Any]]:
        read = self._db_handler.read_todos()
        return read
    
    # def complete(self, position):
    #     self.todo_lost[position - 1]._status = 2

    # def delete(self, position):
    #     self.todo_lost.pop(position - 1)

    def set_done(self, todo_id: int) -> CurrentTodo:
        """Set a to-do as done."""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentTodo({}, read.error)
        try:
            todo = read.todo_list[todo_id - 1]
        except IndexError:
            return CurrentTodo({}, ID_ERROR)
        todo["Done"] = True
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)

    def remove(self, todo_id: int) -> CurrentTodo:
        """Remove a to-do from the database using its id or index."""
        read = self._db_handler.read_todos()
        if read.error:
            return CurrentTodo({}, read.error)
        try:
            todo = read.todo_list.pop(todo_id - 1)
        except IndexError:
            return CurrentTodo({}, ID_ERROR)
        write = self._db_handler.write_todos(read.todo_list)
        return CurrentTodo(todo, write.error)

    def remove_all(self) -> CurrentTodo:
        """Remove all to-dos from the database."""
        write = self._db_handler.write_todos([])
        return CurrentTodo({}, write.error)
