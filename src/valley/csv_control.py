import csv

with open('data/test.csv', 'w') as csv_file:
    fieldnames = ['name', 'count']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'A', 'count': 2})
    writer.writerow({'name': 'B', 'count': 2})
    writer.writerow({'name': 'C', 'count': 2})
