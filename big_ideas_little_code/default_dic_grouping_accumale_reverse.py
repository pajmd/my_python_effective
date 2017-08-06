from collections import defaultdict
from pprint import pprint

# data accumulation
d = defaultdict(list)
d['paul'].append('black')
d['marie'].append('pink')
d['philippe'].append('red')
d['paul'].append('mac')
d['marie'].append('pc')
d['philippe'].append('ubuntu')

print(d)

# one (scalar key) to many relationship
e2s = {
    'one': ['uno'],
    'two': ['dos'],
    'three': ['tres'],
    'trio': ['tres'],
    'free': ['libre','gratis']
}

# reverse one to many dict
s2e = defaultdict(list)
for k,v in e2s.iteritems():
    for word in v:
        s2e[word].append(k)
print s2e

# reversing a one 2 one
e2s = {
    'one': 'uno',
    'two': 'dos',
    'three': 'tres',
}

s2e = dict((v,k) for k, v in e2s.iteritems())
print s2e
