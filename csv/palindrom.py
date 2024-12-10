def palindrom(num):
    if num // 10 == 0:
        return False
    temp = num
    rev_num = 0

    while temp != 0:
        rev_num = (rev_num * 10) + (temp % 10)
        temp = temp // 10

    if num == rev_num:
        return num
    else:
        return False
    
def infinite_s():
    n = 0
    while True:
        yield n
        n += 1

for i in infinite_s():
    p = palindrom(i)
    if p:
        print(i)
