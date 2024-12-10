def multi_yield():
    yield "This will print the first string"
    yield "This will print the second string"

multi_obj = multi_yield()

print(next(multi_obj)) # This will print the first string
print(next(multi_obj)) # This will print the second string
# print(next(multi_obj)) # 

def fn(n):
    num = 0
    while num < n:
        yield num
        num += 1

# sum_of_n = sum(fn(100000000))
# print(sum_of_n)

def csv_reader(f):
    for row in open(f, 'r'):
        yield row

reader = csv_reader('data.csv')

print(next(reader))


def infinite_s():
    n = 0
    while True:
        yield n
        n += 1

for i in infinite_s():
    print(i, end=" ")