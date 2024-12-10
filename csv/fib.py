
def fibo(n):
    if n in (0,1):
        return n
    return fibo(n-1) + fibo(n-2)

print([fibo(n) for n in range(44)])