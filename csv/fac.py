def y_fac(x):
    a = 1
    for i in range(1, x+1):
        a *= i
        yield a

for x in y_fac(100):
    print(x)