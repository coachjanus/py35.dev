# decoretors

def my_decor(fn):
    def wrapper():
        func = fn()
        make_upper_case = func.upper()
        return make_upper_case
    return wrapper

def hi():
    return f'hello there'

decorate = my_decor(hi)
print(decorate())

import sys

def command_decor(fn):
    def wrapper(arg=None):
        if arg == None:
            print(f"""You  get an error, You are missing NAME.
                  Usage: app.py [OPTIONS] NAME""")
            raise sys.exit("Missing argument NAME")
        func = fn(arg)
        make_upper_case = func.upper()
        return make_upper_case
    return wrapper

@command_decor
def hi_name(name):
    return f"hello there {name}"

print(hi_name('Decorator'))


def my_decorator(fn):
    def wrapper(arg1, arg2):
        print("The args are: {0}, {1}".format(arg1, arg2))
        fn(arg1, arg2)
    return wrapper

@my_decorator
def names(first_name, last_name):
    print("Your fist name and last name are: {0} and {1}".format(first_name, last_name))

print(names("Tom", "Cat"))

def fn_decor(fn):
    def wrapper(*args, **kwargs):
        print('Positional args: ', args)
        print('Keyword args: ', kwargs)
        if args:
            fn(*args)
        else:
            fn(**kwargs)
    return wrapper

@fn_decor
def fn_without_args():
    print('No args')

fn_without_args()

@fn_decor
def fn_with_args(x, y, z):
    print(x, y, z)

fn_with_args(123, 456, 666)

@fn_decor
def fn_with_kwargs(first_name, last_name):
    print(first_name, last_name)

fn_with_kwargs(first_name="John", last_name= "Doe")