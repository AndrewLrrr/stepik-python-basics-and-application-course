import csv
import re
import operator

crimes = {}

with open('task3.5.2/Crimes.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        year = re.search(r'.+/(\d{4})\s.+', row[2])
        if year and year.group(1) == '2016':
            if row[5] in crimes:
                crimes[row[5]] += 1
            else:
                crimes[row[5]] = 1

print(sorted(crimes.items(), key=operator.itemgetter(1)))
