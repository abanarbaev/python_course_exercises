from datetime import datetime
import pprint

def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v


pprint.pprint(flights)
print()

flights2 = {}

for k, v in sorted(flights.item()):
    k2 = convert2ampm(k)
    v2 = v.title()
    flights2[k2] = v2








pprint.pprint(flights2)
