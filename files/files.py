# lecture 05
reader = None

try:
    writer = open("data.txt", 'w')
    print("file open for writing")
except FileNotFoundError:
    print("File Not Found Error")
finally:
    if writer:
        writer.close()
    print("file closed")

try:
    reader = open("data.txt")
except FileNotFoundError:
    print("File Not Found Error")
finally:
    if reader:
        reader.close()
    print("file closed")

with open("data.txt", 'w') as f:
    data = "Some data to be written to the file\n"
    f.write(data)
    data = "Bla bls bla\n"
    f.write(data)
    data = "And Some data to be written to the file\n"
    f.write(data)

with open('data.txt') as f:
    print(f.read())

with open('data.txt') as f:
    for l in f:
        print(l)


def search_str(fl, w):
    with open(fl) as f:
        content = f.read()
        if w in content:
            print(f"word {w} exosts in the {fl}")

search_str('data.txt', 'Bla')