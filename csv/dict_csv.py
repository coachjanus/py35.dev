import csv

fields = ['country', 'capital']


with open('data2.csv', 'w') as f:

    writer = csv.DictWriter(f, fieldnames=fields)

    writer.writeheader()

    writer.writerow(
        {
            'country': 'France',
            'capital': 'Paris'
        }
    )
    writer.writerow(
        {
            'country': 'Italy',
            'capital': 'Rome'
        }
    )
    writer.writerow(
        {
            'country': 'Spain',
            'capital': 'Madrid'
        }
    )

with open('data2.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['country'], row['capital']) 