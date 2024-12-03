TITLE = "Your phone book"
def hello():
    print(F"Hi! It's me, {TITLE.upper()}")


def bye():
    print(F"Thanks for using {TITLE}")


def make_your_choice():
    return input(f"Please make Your choice (l,a,u,r,h or q ) here>>> ")


def help_me():
    print("""
    All that You can do:      
        l : List existing contacts
        a : Add new contact
        u : Update existing contact
        r : Remove existing contact
        h : Print this help
        q : Exit
    """)