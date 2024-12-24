
from pathlib import Path

import typer

from todo import __app_name__, DB_WRITE_ERROR, SUCCESS, DIR_ERROR, FILE_ERROR
import configparser

CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))

# ~/.config/todo

CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.ini"

def init_app(db_path):

    config_code = _init_config_file()
    if config_code != SUCCESS:
        return config_code
    database_code = _create_database(db_path)
    if database_code != SUCCESS:
        return database_code
    
    return SUCCESS



def _init_config_file():
    try:
        CONFIG_DIR_PATH.mkdir(exist_ok=True)
    except OSError:
        return DIR_ERROR
    try:
        CONFIG_FILE_PATH.touch(exist_ok=True)
    except OSError:
        return FILE_ERROR


def _create_database(db_path):
    config_parser = configparser.ConfigParser()
    config_parser["General"] = {"database": db_path}

    try:
        with CONFIG_FILE_PATH.open("w") as file:
            config_parser.write(file)
    except OSError:
        return DB_WRITE_ERROR
    return SUCCESS

