import csv

input_file = 'Dennis Bruce Contacts.csv'
output_file = 'Dennis Bruce Contacts.csv'
unwanted_domains = ['name@hotmail.com', 'name@live.com']

with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.reader(input_csv)
    writer = csv.writer(output_csv)
    for row in reader:
        if not any(cell.endswith(tuple(unwanted_domains)) for cell in row):
            writer.writerow(row)
