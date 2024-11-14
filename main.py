# 

company_name = "My company"

def fn():
    pass

fn()

def getName(name):
    print(name)

getName(company_name)

def sum(a, b):
    return a + b

print(sum(55, 55))

a = int(input("Enter a = "))
b = int(input("Enter b = "))

# print(sum(a, b))

o = input("Enter operation: ")

if o == '+':
    print(sum(a, b))
elif o == '-':
    print(a - b)
elif o == '*':
    print(a * b)
elif o == '/':
    print(a / b)
else:
    print('Ooops! something wrong!')


alert = "division by zero" if a == 0 else "OK"
print(alert)

match o:
    case '+':
        print(sum(a, b))
    case '-':
        print(a - b)
    