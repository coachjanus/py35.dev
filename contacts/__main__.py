
import argparse
import sys

from .contact import contact_list, add_contact, update_contact, remove_contact, lookup_contact, save_contact, load_contact

from .helper import hello, help_me, bye, make_your_choice

def main():
    parser = argparse.ArgumentParser(
        prog="Phone Book",
        description="List of my contacts",
        epilog="Thanks for using %(prog)s! :)"
    )
    general = parser.add_argument_group("general output")
    general.add_argument(
        "path",
        nargs="?",
        default="db.pkl",
        help="take the path to the target database file (default: %(default)s)"
    )
    args = parser.parse_args()
    print(args)
    print(sys.path)

    hello()
    
    contacts = load_contact()

    while True:
        match make_your_choice():
            case 'a':
                new_contact = add_contact()
                contacts.append(new_contact)
                save_contact(contacts)
            case 'l':
                contact_list(contacts)

            case 'u':
                name = input("What name You looking for: ")
                contact = lookup_contact(name)
                # print(contact)
                contact.update(update_contact(contact))

            case 'r':
                name = input("What name You looking for: ")
                contact = lookup_contact(contacts, name)
                remove_contact(contacts, contact)

            case 'q':
                bye()
                break
            case _:
                help_me()

if __name__ == "__main__":
    main()