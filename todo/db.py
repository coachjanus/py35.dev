from pathlib import Path

from todo import SUCCESS, DB_WRITE_ERROR
import configparser

DEFAULT_DB_FILE_PATH = Path.home().joinpath("." + Path.home().stem + "_todo.json")

def init_database(db_path):
    try:
        db_path.write_text("[]")
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR

def get_database_path(config_file):
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])
