import unittest
from todo.db import get_database_path
from pathlib import Path


path_to_config = 'config.ini'
path_to_db = 'db.json'

class TestDb(unittest.TestCase):

    def test_get_db_path(self):
        config_file = Path(path_to_config)
        expected_path = Path(path_to_db)
        db_path = get_database_path(config_file.absolute())
        self.assertEqual(db_path, expected_path.absolute())

if __name__ == "__main__":
    unittest.main()