from glob import glob
# in python 3 open would suffice to open with encoding
# in python 2.7 we need to imprt io
from io import open

# globule wild card expansion
print(glob('*.py'))

# read file with encoding

with open( 'congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    print(f.read())

it = iter('abcdefd')
print(next(it))
print(next(it))
# we consume 2 chars and put the rest in a list
l = list(it)
print(l)

import csv # is must faster than a split
def unicode_csv_reader(unicode_csv_data, dialect=csv.excel, **kwargs):
    # csv.py doesn't do Unicode; encode temporarily as UTF-8:
    csv_reader = csv.reader(utf_8_encoder(unicode_csv_data),
                            dialect=dialect, **kwargs)
    for row in csv_reader:
        # decode UTF-8 back to Unicode, cell by cell:
        yield [unicode(cell, 'utf-8') for cell in row]

def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')

with open( 'congress_votes_114-2016_s20.csv', encoding='utf-8') as f:
    #next(csv.reader(f))
    #next(csv.reader(f))
    it = unicode_csv_reader(f)
    next(it)
    next(it)
    # in python 3 I could have use directly csv.reader to read utf-8 ended data
    for row in unicode_csv_reader(f):
        print(row)

colors = ['blue', 'red', 'green']
for color in colors[::-1]:
    print color

print(sorted(colors, key=lambda x : x[1]))

from collections import Counter

c = Counter()
print(c['cars'])
c['cars'] += 1
print(c['cars'])
print(c)
c['bicycle'] = 2
print(c.most_common(1))
print(list(c.elements()))


