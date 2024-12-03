"""contacts/__init__.py
Top-level package for contacts.

визначення двох імен на рівні модуля, 
які містять назву та версію програми

__app_name__ = "contacts"
__version__ = "0.1.0"

Ініціалізація пакета
Якщо файл __init__.py присутній у каталозі пакета, 
він викликається під час імпорту пакета або модуля в пакеті. 
Це можна використовувати для виконання коду ініціалізації пакета, 
наприклад ініціалізації даних на рівні пакета.

"""
from pathlib import Path
import os
# import contacts.views

__app_name__ = "contacts"
__version__ = "0.1.0"

TITLE = "Your Contacts book"

# DATABASE_PATH = "db"

def init_dir(path):
   if not os.path.isdir(path):
      os.mkdir(path)

# home_dir = os.path.expanduser("~")
# print(home_dir)

# The pathlib module provides Path.home() 
# to get the home directory in Python. 
# This function works fine if your Python version is Python 3.4+. 
# It returns a new path object having the user’s home directory.
# home = str(Path.home())

DATABASE_PATH = str(Path.home())
# print(DATABASE_PATH)

init_dir(DATABASE_PATH + '/.config/contacts')

DATABASE = f"{DATABASE_PATH}/{__app_name__}.pkl"
