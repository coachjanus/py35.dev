"""This module provides the To-Do database functionality."""

from pathlib import Path
import json

from todo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

from typing import Any, Dict, List, NamedTuple
from todo.db_response import DBResponse

from todo.model import Todo

class TodoEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Todo):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)

class DBHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_todos(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)

                except json.JSONDecodeError:  # Catch wrong JSON format
                    return DBResponse([], JSON_ERROR)

                
        except OSError:  # Catch file IO problems
            return DBResponse([], DB_READ_ERROR)


    def write_todos(self, todo_list: List[Dict[str, Any]]) -> DBResponse:
        self.todo_list = todo_list
        print(todo_list)
        try:
            with self._db_path.open("w") as db:
                json.dump(self.todo_list, db, indent=4, cls=TodoEncoder)
            return DBResponse(todo_list, SUCCESS)

        
        except OSError:  # Catch file IO problems
            return DBResponse(todo_list, DB_WRITE_ERROR)


if __name__ == "__main__":
    import doctest
    doctest.testmod()