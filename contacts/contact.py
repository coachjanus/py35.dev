import pickle

def contact_list(contacts):
    if len(contacts) > 0:
        for item in contacts:
            for k, v in item.items():
                print(k, '=>', v)

    else:
        print("Your contact list is empty. Go back to menu yo add a new contact.")


def add_contact():
    contact = {}
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input("Enter phone number: ").strip()
    contact['first_name'] = first_name
    contact['last_name'] = last_name
    contact['phone_number'] = phone_number
    return contact


def update_contact(contact):
    old_phone_number = contact['phone_number']
    old_first_name = contact['first_name']
    old_last_name = contact['last_name']

    phone_number = input(f"Edit phone number: ({old_phone_number}) => ").strip() or old_phone_number
    print(phone_number)
    first_name = input(f"Edit first name: ({old_first_name}) => ").strip() or old_first_name
    last_name = input(f"Edit last name: ({old_last_name}) => ").strip() or old_last_name

    return {'first_name': first_name.lower(), 'last_name': last_name.lower(), 'phone_number': phone_number}


def remove_contact(contacts, contact):
    index = contacts.index(contact)
    confirm = input("Are You sure You want to delete this  contact? (y/n): ").strip()
    if confirm.lower() in ('yes', 'y'):
        contacts.pop(index)


def lookup_contact(contacts, name):

    first_name = ''
    last_name = ''
    words = name.split()
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


def save_contact(contacts):
    with open('db.pkl', 'wb') as f:
        pickle.dump(contacts, f)

def load_contact():
    list_unpickled = []
    with open('db.pkl', 'rb') as f:
        list_unpickled = pickle.load(f)
    return list_unpickled
