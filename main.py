var = "string"
print(type (var))
print(id (var))
True
False
None

# print(2**10000)

import math

print(math.tan(math.pi))

from decimal import *

getcontext().prec = 20

print(Decimal(3.14))

print ("""
Hello 
World

""" )

print ('''

Hello 
World
''')

print("hello \t world")


print("hello \t \"world\"")

print(r'Hi\nHello\tworld')
print("Hello" + "World")

print("_" * 80)

hello = "Hello World"""

print(hello[7])
print(hello[0])
print(hello[len(hello) -1])
print(min(hello))
print(max(hello))

print(hello[2:7])

print(hello.split())

print("My first name {} my last name {}".format("Tom", "Cat"))

name = "John"
last_name = "Doe"

print(f"My name {name} {last_name}")


def hell(p):
    print(f"Hello {p}")

hell("World")

i = 0
while i < 20:
    # if i > 10:
    #     continue
    print(i)
    i = i + 1

for c in hello:
    print(c)


while True:
    o = input("Ender operation: ")
    if o == 'q':
        break

