# lecture 02

my_tuple = ('foo', 'bar')

print(my_tuple)
print(type(my_tuple))
print(id(my_tuple))
print(len(my_tuple))
print(dir(my_tuple))

my_range = range(1, 15, 2)

print(list(my_range))

print(list(my_range))

s1 = list(my_range)
print(s1[-1])

print(s1.index(9))

t1 = 1,2,3,4,5,6,7 # (1,2,3)

x1, *sublist, x2 = t1

print (x1)
print(sublist)