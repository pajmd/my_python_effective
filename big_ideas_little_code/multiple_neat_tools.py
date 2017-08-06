
# unicode
print(u'The answer is \u0664\u0662 today')
# uninf a named unicode
print(u'using named unicode\N{trade mark sign}')
print(u'using named unicode\N{macron}')
print(u'using named unicode\N{PLUS-MINUS SIGN}')

# two different unicodes may look the same ex:
lowis1 = u'L'+unichr(246) + u'wis'
lowis2 = u'L'+unichr(111) + unichr(776) + u'wis'

print(lowis1)
print(lowis2)
print(lowis1 == lowis2) # false

# Normalize to make sure they are treated the same way
# NFC is one normalization method
import unicodedata
lowis1 = unicodedata.normalize('NFC', lowis1)
lowis2 = unicodedata.normalize('NFC', lowis2)
print(lowis1)
print(lowis2)
print(lowis1 == lowis2) # true

# bisect is about searching ranges
import bisect
cuts = [60,70,80,90]
grades = 'FDCBA'
# bisect.bisect reurns the section number for a particular value
print(grades[bisect.bisect(cuts, 76)])
print(grades[bisect.bisect(cuts, 36)])
print(grades[bisect.bisect(cuts, 66)])

# heapq.merge is a perfect to to merge sorted list in a sorted list
# merge creates an iterator: calling next returns the smallest fisrt element
# out the the n lists, the moves to the 2nd elt of the list it found
# the next next will compare the fist elts of the n-1 lists to the 2nd of the
# first list and returns the smallest and so one.
# it does the work only when next is called so it's very economical
import heapq
a = [33, 45, 100]
b = [10,20,40]
c = [5, 9, 15]
l = heapq.merge(a,b,c)
print(l)
it = heapq.merge(a,b,c)
for v in it:
    print v

# itertools islice slices in only one directin on an iterator
# the difference with slice is that it produces an iterator
# good for just ine time work, on demand
from itertools import islice
print(list(islice('abcdefg', 3)))
print(list(islice('abcdefg', None, 3)))


# sys.intern allows to make sure that one string has only one
# representaion or id:
# when internaling a string it checks if it was already internalized and if so
# uses this one.
# helps save memory
# in python2 intern is builtin
hello = 'hello'
he = 'he'
llo = 'llo'
he_llo = he + llo
print(hello == he_llo)
print(id(hello) == id(he_llo))
try:
    from sys import intern
except:
    pass
print('Interned string')

hello = intern('hello')
he = 'he'
llo = 'llo'
he_llo = intern(he + llo)
print(hello == he_llo)
print(id(hello) == id(he_llo))

# expovariate
import random
print(random.uniform(1000, 1100))
# random toward the center
print(random.triangular(1000, 1100))
# expovariate to simulate arrival time
# ex: simulate arrivle time of 5 customers
# the output average is around 5
print(random.expovariate(1/5.0))
print(random.expovariate(1/5.0))
print(random.expovariate(1/5.0))
print(random.expovariate(1/5.0))
import numpy
print('Proof; ', numpy.mean([random.expovariate(1/5.0) for i in xrange(1000)]))

# time
import time
time.sleep(3)
print('Num of sec since epoch:', time.time())
print('Readable time:', time.ctime())

# hashlib for hashing
import hashlib

# obsolete md5 because not strong enough
# better use sah1 or better sha256
# to make it readable hexdigest()
print(hashlib.md5('some string').hexdigest())
print(hashlib.sha256('some string').hexdigest())
# but it still possible to guess the passowrd with these.
# A better technic is to hash the result of the hash several time
# or just use:
print(hashlib.pbkdf2_hmac('sha256','some string',
                          salt='random phrase',
                          iterations=1000))


# python return the value that makes a condition True of False
# not like the other language that return true or false

print (True and 'hi') # hi is evaluated to true because not empty string
print('hi' and True)
print('bye' and 'hi')
print('bye' or 'hi')

# technic used in function definition
def func(par, some=None):
    some = some or 'some default value'
    print(par, some)
func('a')
func('a', 'b')

