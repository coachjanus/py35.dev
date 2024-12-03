# 

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

def hello(TITLE):
    print(F"Hi! It’s me, {TITLE.upper()}")

def make_your_choice():
    return input(F"Please make Your choice (l,a,u,r,h or q) here >>> ")

def bye(TITLE):
	print(f'Thanks for using {TITLE}')
