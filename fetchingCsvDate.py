import csv
from pprint import pprint
from collections import defaultdict

def read():
    a = defaultdict(list)
    with open('phones.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
              a[line[-2]].append(line)
    return a

def find(inp, c):
        for l in c:
            try:
                if l[-2]==inp:
                    print(l)
            except:
                return "No such element"
a = "voice"
b = "fax"
data = read()
pprint(data['voice'])
# find(a, data)
# find(b , data)
