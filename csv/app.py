# 

import csv

data = [
    [1,2,3],
    ['morning', 'evening', 'afternoon']
]

with open('test.csv', newline='\n') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


with open('data1.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
