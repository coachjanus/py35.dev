# 
def inner():
    print("I'm inner-function")
    
def outer(fn):
    fn()

outer(inner)

animals = ["ferret", "vole", "dog", "gecko"]

print(sorted(animals))

print(sorted(animals, key=len))


print(sorted(animals, key=len, reverse=True))

def reverse_len(s):
    return -len(s)

print(sorted(animals, key=reverse_len))


a = [10,4,2,8,1,0]
a.sort()
print(a)