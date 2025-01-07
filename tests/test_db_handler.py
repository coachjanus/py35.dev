import pytest

from todo.db_handler import DBHandler
from pathlib import Path
from unittest.mock import mock_open

test_db_path = Path.home().joinpath('.' + Path.home().stem + "_todo.json")

def test_read_todos_success(mocker):
    mocker.patch('builtins.open', mock_open(read_data='''[{
        "task": "T o   D o   S o m e t h i n g   O t h e r.",
        "category": "Work",
        "status": 2,
        "position": 1
    }]'''))
    db_handler = DBHandler(Path(test_db_path))
    response = db_handler.read_todos()
    assert len(response.todo_list) == 1
    assert response.todo_list[0]['task'] == "T o   D o   S o m e t h i n g   O t h e r."
    assert response.todo_list[0]['category'] == "Work"