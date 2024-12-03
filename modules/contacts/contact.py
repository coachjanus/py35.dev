import pickle
import argparse
import sys
from pathlib import Path


def full_name(contact):
	return ' '.join([contact['first_name'].title(), contact['last_name'].title()])

def is_valid_phone_number(x):
    return x.isdigit() and len(x) == 12

def is_valid_name(x):
    return len(x) >= 2

def add_item():
    contact = {}
    
    first_name = input('Enter First Name: ').strip().lower()
    
    while not is_valid_name(first_name):
        first_name = input('Please Enter Valid First Name: ').strip().lower()
    else:
        contact['first_name'] = first_name
    
    last_name = input('Enter Last Name: ').strip().lower()
    while not is_valid_name(last_name):
        last_name = input('Please Enter Valid Last Name: ').strip().lower()
    else:
        contact['last_name'] = last_name
    
    home_phone_number = input('Enter a home phone number: ').strip()

    while not is_valid_phone_number(home_phone_number):
        home_phone_number = input('Please Enter a valid home  phone number: ').strip()
    else:
        contact['home_phone_number'] = home_phone_number

    office_phone_number = input('Enter an office phone number: ').strip()

    while not is_valid_phone_number(office_phone_number):
        office_phone_number = input('Please Enter a valid office phone number: ').strip()
    else:
        contact['office_phone_number'] = office_phone_number
        
    return contact

         

def check_contact_item(contacts, new_contact_item):
    for item in contacts:
        if item['home_phone_number'] == new_contact_item['home_phone_number']:
            print("This phone number already is in contacts")
            return False, "This phone number already is in contacts"
        if full_name(item) == full_name(new_contact_item):
            print("This name already is in contacts")
            return False, "This name already is in contacts"
    return True, "Success"


TITLE = "Your Phonebook"

def help_me():
    print("""
    All That You Can Do:
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """)

def hello():
    print(F"Hi! It’s me, {TITLE.upper()}")

def make_your_choice():
    return input(F"Please make Your choice (l,a,u,r,h or q) here >>> ")

def bye():
	print(f'Thanks for using {TITLE}')

def contact_list(contacts):
    if len(contacts) > 0:
        for contact in contacts:
            for k, v in contact.items():
                    print(k, '-->', v)
        # save_contact(contacts)
    # Else inform the user that the contact book is empty
    else:
        print('Your phonebook is empty! Go back to the menu to add a new contact')

def lookup_contact(contacts, query):
    words = query.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
        last_name = ''

    for d in contacts:
        if d['first_name'] == first_name.lower() and d['last_name'] == last_name.lower():
            return d
        elif d['first_name'] == first_name.lower() and last_name == '':
            return d

def search_dictionaries(key, value, list_of_dictionaries):
    return [element for element in list_of_dictionaries if element[key] == value]

def in_dict(key, value, contacts):
    for entry in contacts:
        if entry[key].lower() == value:
            return True
    return False

def update_contact(contacts, contact):
    old_home_phone_number = contact['home_phone_number']
    old_office_phone_number = contact['office_phone_number']
    
    home_phone_number = input(f'Edit home phone number: ({old_home_phone_number}) => ').strip() or old_home_phone_number
    
    if home_phone_number != old_home_phone_number:
        if in_dict('home_phone_number', home_phone_number, contacts):
            print(f'The contact {home_phone_number} is already in the phonebook')
            return
    old_first_name = contact['first_name']
    old_last_name = contact['last_name']
    first_name = input(f'Edit first name ({old_first_name}) => ').strip().title() or old_first_name
    last_name = input(f'Edit surname ({old_last_name}) => ').strip().title() or old_last_name
    
    if full_name(contact) != ' '.join([old_first_name.title(), old_last_name.title()]):
        if in_dict('first_name', first_name.lower(), contacts) and in_dict('last_name', last_name.lower(), contacts):
            print(f'The contact {full_name(first_name, last_name)} is already in the phonebook')
            return

    return {'first_name': first_name.lower(), 'last_name': last_name.lower(), 'home_phone_number': home_phone_number}

def remove_contact(contacts, contact):
    index = contacts.index(contact)
    confirm = input('Are you sure you want to delete this contact? (y/n): ').strip()
    if confirm.lower() in ('yes', 'y'):
        contacts.pop(index)
    else: 
        print('That contact does not exist!')

def save_contact(contacts):
    # Write to the file
    with open('db.pkl', 'wb') as f:
        pickle.dump(contacts, f)

def load_contact():
    # Read the data from existing file
    list_unpickled = []
    with open('db.pkl', 'rb') as file:
        list_unpickled = pickle.load(file)
    return list_unpickled


def main():
    hello()
    contacts = load_contact()
    print(contacts)
    while True:
        match make_your_choice():
            case 'a':
                new_contact_item = add_item()
                state, msg =  check_contact_item(new_contact_item)
                if state:
                    contacts.append(new_contact_item)
                    # printing new contact item
                    print(f"{msg} - Added new contact item: ", str(new_contact_item))
                else: 
                    print(msg)
            case 'l':
                contact_list(contacts)
            case 'u':
                name = input('What name you looking for: ')
                contact = lookup_contact(contacts, name)
                # print(lookup_contact(name))
                # update_contact(contact)
                contact.update(update_contact(contacts, contact))
                
                # print(search_dictionaries('first_name', name.split()[0], contacts))
            case 'r':
                name = input('What name you looking for: ')
                contact = lookup_contact(contacts, name)
                # print(lookup_contact(name))
                remove_contact(contacts, contact)

            case "q":
                bye()
                break
            case _:
                help_me()

# Для обробки аргументів командного рядка в Python 
# ви можете використовувати sys.argv або модуль argparse.

# sys.argv дуже простий і легкий у використанні; 
# однак вам потрібно самостійно керувати кількістю аргументів 
# і виконувати перетворення типів.

# if (args_count := len(sys.argv)) > 2:
#    print(f"One argument expected, got {args_count - 1}")
#    raise SystemExit(2)
# elif args_count < 2:
#    print("You must specify the database name")
#    raise SystemExit(2)

# argparse — аналізатор параметрів командного рядка, 
# аргументів і підкоманд — 
# документація https://docs.python.org/3/library/argparse.html

# Модуль argparse дозволяє визначати типи аргументів, 
# приймати кілька аргументів у вигляді списку 
# та використовувати такі параметри, як -i та -o, 
# для більш гнучкої обробки команд.

# використання модуля argparse вимагає певного коду конфігурації, 
# але він дозволяє використовувати параметри 
# та керувати будь-якою кількістю аргументів.

parser = argparse.ArgumentParser(
    prog="Phone book",
    description="Management the list of contacts",
    epilog="Thanks for using %(prog)s! :)",
)

# Додати аргументи та параметри до аналізатора
parser.add_argument("path")

# print(parser)

# ArgumentParser(prog='contact.py', usage=None, description=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)

args = parser.parse_args()
print(args)

# def main():
#    parser = argparse.ArgumentParser(
#       prog="phone book",
#       description="List of my contact",
#       epilog="Thanks for using %(prog)s! :)",
#    )
#    general = parser.add_argument_group("general output")
#    general.add_argument(
#       "path",
#       nargs="?",
#       default="db.pkl",
#       help="take the path to the target database file (default: %(default)s)",
#    )
#    args = parser.parse_args()
#    print(args)
#    print(sys.path)

# Використання модуля os.path
   # Модуль os Python надає підмодуль під назвою path, який містить кілька методів для виконання операцій з шляхами до файлів. 
   # метод exists() використовується для перевірки існування певного файлу чи каталогу.
   # функція os.path.exists() повертає True, якщо файл або каталог існує, і False в іншому випадку.

   # import os

   # if os.path.exists('sample.txt'):
   #    print('The file exists')
   # else:
   #    print('The file does not exist')


# Використання модуля pathlib
   # модуль pathlib забезпечує об’єктно-орієнтований підхід до обробки шляхів файлової системи. Він поставляється з методом exists(), який перевіряє, чи існує файл або каталог.
   # Функція Path() створює новий об’єкт Path, а метод exists() повертає True, якщо файл або каталог існує, і False в іншому випадку.

   # Інший спосіб перевірити, чи існує файл, — спробувати відкрити файл у блоці try та переловити помилку FileNotFoundError у блоці винятків.

   # try:
   #    with open('sample.txt') as f:
   #       print('The file exists')
   # except FileNotFoundError:
   #    print('The file does not exist')


   # from pathlib import Path

   # if Path('sample.txt').exists():
   #    print('The file exists')
   # else:
   #    print('The file does not exist')

   # execution_dir = os.getcwd()

   # Find the directory in which the current script resides:
   
   # file_dir = os.path.dirname(os.path.realpath(__file__))
   # file_dir = os.path.dirname(os.path.realpath(__file__))

   # print(f"Execution dir: {execution_dir}")
   # print(f"File dir: {file_dir}")
   # print(f"File: {os.path.realpath(file_dir/Path(args.path))}")
   # database_file = Path(os.path.realpath(file_dir/Path(args.path)))
   # print(database_file)

   
   # Виняток SystemExit сигналізує про намір вийти з інтерпретатора.

   # if not database_file.exists():
   #    print("The database file doesn't exist")
   #    raise SystemExit(1)
   
   # Код виходу процесу доступний через 
   # атрибут multiprocessing.Process.exitcode.
   
   # import multiprocessing
   # print(multiprocessing.Process.exitcode)
   
   # Код виходу процесу встановлюється автоматично, наприклад:
   # Якщо процес все ще виконується, код виходу буде None.
   # Якщо процес завершився нормально, код виходу буде 0.
   # Якщо процес завершився з неперехопленим винятком, код виходу буде 1.
   
   # Функція sys.exit() - вихід з інтерпретатора Python.
   # Код виходу також можна встановити за допомогою виклику sys.exit().
   # вихід із помилкою sys.exit('Сталося щось погане')
   

   # home_dir = os.path.expanduser("~")
   # print(home_dir)

   # The pathlib module provides Path.home() to get the home directory in Python. This function works fine if your Python version is Python 3.4+. It returns a new path object having the user’s home directory.

   # home = str(Path.home())
   # print(home)
   # init_dir(home+'/.config/contacts')
   # views.app(prog_name=__app_name__)


database_file = Path(args.path)

if not database_file.exists():
   print("The database file doesn't exist")
   raise SystemExit(1)


# for entry in target_dir.iterdir():
#    print(entry.name)
# Функція dir().
   # Вбудована функція dir() повертає список визначених імен у просторі імен. 
   # Без аргументів створює відсортований за алфавітом список імен у поточній локальній таблиці символів:

   print(dir(views))
   print(dir(views.app))

main()
