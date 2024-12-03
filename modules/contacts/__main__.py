""" Contacts entry point script."""
# contacts/__main__.py

from pathlib import Path
import sys
import os
import argparse


# SyntaxError: імпорт * дозволено лише на рівні модуля
# оператор try із реченням Except ImportError можна 
# використовувати для захисту від невдалих спроб імпорту:

# >>> try:
# ...     # Non-existent module
# ...     import baz
# ... except ImportError:
# ...     print('Module not found')
# ...
# Module not found

# >>> try:
# ...     # Existing module, but non-existent object
# ...     from mod import baz
# ... except ImportError:
# ...     print('Object not found in module')
# ...
# Object not found in module

from contacts import views, helpers, __app_name__, TITLE, DATABASE


# def init_dir(path):
#    if not os.path.isdir(path):
#       os.mkdir(path)


def main():
    helpers.hello(TITLE)
   #  contacts = load_contact()
   #  print(contacts)
    while True:
        match helpers.make_your_choice():
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
                helpers.bye(TITLE)
                break
            case _:
                helpers.help_me()


if __name__ == "__main__":
   parser = argparse.ArgumentParser(
      prog="phone book",
      description="List of my contact",
      epilog="Thanks for using %(prog)s! :)",
   )

   general = parser.add_argument_group("general output")
   general.add_argument(
      "path",
      nargs="?",
      default="db.pkl",
      help="take the path to the target database file (default: %(default)s)",
   )
   args = parser.parse_args()

   print(args)
   print(sys.path)

   execution_dir = os.getcwd()

   # Find the directory in which the current script resides:
   # file_dir = os.path.dirname(os.path.realpath(__file__))
   file_dir = os.path.dirname(os.path.realpath(__file__))


   print(f"Execution dir: {execution_dir}")
   print(f"File dir: {file_dir}")
   print(f"File: {os.path.realpath(file_dir/Path(args.path))}")
   database_file = Path(os.path.realpath(file_dir/Path(args.path)))
   print(database_file)

   
#    views.app(prog_name=__app_name__)


   main()

