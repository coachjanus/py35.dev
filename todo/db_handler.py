from pathlib import Path
import json

from .db_response import DBResponse

from todo import DB_READ_ERROR, DB_WRITE_ERROR, JSON_ERROR, SUCCESS

class DBHandler:
    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path

    def read_todos(self) -> DBResponse:
        try:
            with self._db_path.open("r") as db:
                try:
                    return DBResponse(json.load(db), SUCCESS)
                    # return (json.load(db), SUCCESS)
                except json.JSONDecodeError:
                    return DBResponse([], JSON_ERROR)
        except OSError:
            return DBResponse([], DB_READ_ERROR)
        
    
    def write_todos(self, todo_list):
        self.todo_list = todo_list

        try:
            with self._db_path.open("w") as db:
                json.dump(self.todo_list, db, indent=4)
            return (SUCCESS)
        except OSError:
            return ([], DB_WRITE_ERROR)
                