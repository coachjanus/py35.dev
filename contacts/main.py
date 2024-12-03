# main module

contacts = [] # list

contact = {
    'first_name': "john",
    'last_name':  "doe",
    'phone_number': "1234567"
}

contacts.append(contact)

TITLE = "phone book"

def hi():
    print(f"Hi! It's me, {TITLE.upper()}")

def bye():
    print(f"Thanks for using {TITLE}")

def your_choice():
    return input(f"Please make Your choice (l, a, u, r, h or q )>>> ")

def help_me():
    print("""
    All that You can do:
          l: List existing contacts
          a: Add new contact
          u: Update existing contact
          r: Remove existing contact
          h: Print this help
          q: Exit
    """)

def contact_list():
    if len(contacts) > 0:
        for item in contacts:
            for k, v in item.items():
                print(k, ' => ', v)
    else:
        print("Your contact list is empty. Go back to menu and add new contact.")

def add_contact():
    contact = {}
    first_name = input("Enter first name: ").strip().lower()
    last_name = input("Enter last name: ").strip().lower()
    phone_number = input("Enter phone number: ").strip()
    contact['first_name'] = first_name
    contact['last_name'] = last_name
    contact['phone_number'] = phone_number
    return contact

def lookup_contact(name):
    first_name = ''
    last_name = ""
    words = name.split()
    if len(words) == 2:
        first_name, last_name = words
    elif len(words) == 1:
        first_name = words[0]
    for d in contacts:
        if d['first_name'] == first_name.lower() and d['last_name'] == last_name.lower():
            return d
        elif d['first_name'] == first_name.lower() and last_name == '':
            return d

def remove_contact(contact):
    index = contacts.index(contact)
    confirm = input("Are You sure You want to delete this contact? (y/n): ").strip()
    if confirm.lower() in ('yes', 'y'):
        contacts.pop(index)

def update_contact(contact):
    old_phone_number = contact['phone_number']
    old_first_name = contact['first_name']
    old_last_name = contact['last_name']

    first_name = input(f"Enter first name: ({old_first_name}) >>> ").strip().lower() or old_first_name
    last_name = input(f"Enter last name:  ({old_last_name}) >>> ").strip().lower() or old_last_name
    phone_number = input(f"Enter phone number:  ({old_phone_number}) >>> ").strip() or old_phone_number

    return {'first_name': first_name.lower(), 'last_name': last_name.lower(), 'phone_number': phone_number}

def main():
    hi()

    while True:
        match your_choice():
            case 'a':
                contacts.append(add_contact())
            case 'l':
                contact_list()
            case 'u':
                name = input ("What name You looking for: ")
                contact = lookup_contact(name)
                contact.update(update_contact(contact))
            case 'r':
                name = input ("What name You looking for: ")
                contact = lookup_contact(name)
                # print(contact)
                remove_contact(contact)
            case 'q':
                bye()
                break
            case _:
                help_me()


main()

