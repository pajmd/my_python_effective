
# -*- coding: utf-8 -*-

nums = [(1,3),(23,3),(4,65),(7,9),(4,56)]

def func(numbers, k):
    return next(t for t in numbers if t[0] + t[1] == k)

print('func(numbers,69) = {}'.format(func(nums, 69)))

st = "ksjdkajsdkajksjdalsdjaksda"

def dedup(s):
    res = ""
    for item in s:
        if item not in res:
            res = res + item
    return res

print('dedup("ksjdkajsdkajksjdalsdjaksda") = {}'.format(dedup("ksjdkajsdkajksjdalsdjaksda")))


def dedup2(s):
    for c in s:
        s = c + s.replace(c, '')
    return s

print('dedup2("ksjdkajsdkajksjdalsdjaksda") = {}'.format(dedup2("ksjdkajsdkajksjdalsdjaksda")))

def dedup3(s, out=''):
    s0, s = s[0], s.replace(s[0], '')
    return dedup3(s, out + s0) if s else out + s0

print('dedup3("ksjdkajsdkajksjdalsdjaksda") = {}'.format(dedup3("ksjdkajsdkajksjdalsdjaksda")))


keys = {'red', 'green', 'blue', 'yellow', 'orange', 'pink', 'black'}
d = dict.fromkeys(keys)
print('d={}'.format(d))
# Update the dictionary with the key/value pairs from other, overwriting existing keys.
d.update(dict(d))
print('d={}'.format(d))

import string
allChar = string.uppercase + string.lowercase
charToSoundex = string.maketrans(allChar, "91239129922455912623919292" * 2)
# print('allchars={}\ncharToSoundex={}'.format(allChar, charToSoundex))

def f( x = [7] ):
    if 10 < x[0] < 20:
        pass
    else:
        modifier = "not "
    print("%s is %sbetween 10 and 20" % (x[0], modifier))
    x[0] += 5
f()
#f()

def f( x = 7 ):
    if 10 < x < 20:
        pass
    else:
        modifier = "not "
    print("%s is %sbetween 10 and 20" % (x, modifier))
    x += 5
f()
f()

i = 2
a = i
print('a = {} i = {} a is i = {}'.format(a, i, a is i))
i += 2
print('a = {} i = {} a is i = {}'.format(a, i, a is i))



def foo(x):
    if x> 4:
        y = 5
    print y

foo(10)
try:
    foo(1)
except UnboundLocalError:
    print('y was never assigned so is not konw!!!')


def func(  ):
    x = 4
    action = (lambda n: x ** n)          # x remembered from enclosing def
    return action

x = func()
print type(x)
#print x(2)

# tuple are compared in lexicograpical order
print((1,3) > (0,3))
print((1,3) > (4,3))
print((1,3) > (1,4))
print((1,3) > (1,2))
print((1,3) > (3, 1))


# https://docs.python.org/3/howto/unicode.html
#
# Software should only work with Unicode strings internally, decoding the input data as soon as possible and encoding the output only at the end.
# unicode to ouput
# bytes = unicode.encode('utf-8)
# write bytes to a file.
#
# bytes from the input
# unicode = bytes.decode(utf-8)
#
u = u'\u6211' # \u says this unicode string contains a unincode wich is a chinese character
print "u'\u6211'=",u
print "len(u'\u6211') = ",len(u)
u = u'6211' # this unicode string contains string 6211
print "u'6211' = ", u

chinese = u'\u6211'
encoded = chinese.encode('utf-8')
print "u'\u6211'.encode('utf-8') = ", encoded

ch = u'\u9FCC'
print(u'chinese char {} len={}'.format(ch, len(ch)))
#print(u'chinese char {}'.format(ch))
utf8 = ch.encode('utf-8')
print('utf8 = {} len = {}'.format(utf8, len(utf8)))
glyph = u'鿌'
print (u'glyph: {}'.format(glyph))
#       1234567890123456789012345678
val = u'Ознакомьтесь с документацией'
print(u'russe {}: lentgth = {} type={}'.format(val, len(val), type(val)))
print val.split(',')
b=val.encode('utf-8')
print(u'russe bytes:')
print(b, type(b), len(b))
print b.split(',')

from io import open
filename = 'file_of_characters.txt'
with open(filename, 'w', encoding='utf-8') as f:
    f.write(val)
filename = 'file_of_characters2.txt'
with open(filename, 'w') as f:
    f.write(val)

with open(filename, 'r') as f:
    for line in f:
        print 'line', line, type(line)

filename = 'file_of_characters.txt'
with open(filename, 'r', encoding='utf-8') as f:
    for line in f:
        print 'line uft8', line, type(line)


# sum function
l=[1,2,3]
print 'should be empty list ',l[6:], l[6:] is None, l[7:] is None
def mysum(l):
    if not len(l):
        return 0
    return l[0] + mysum(l[1:])
print 'sum should be 6', mysum(l)

def mysum2(l):
    s = ''
    if len(l) > 0:
        for el in l:
            s += el
    return s
#print 'sum should be 6', mysum2(l)
l=['s','p','a','m',]
print 'sum should be spam', mysum2(l)

while l:
    l = l[1:]

l = [1, [2, [3, 4], 5], 6, [7, 8]]
# [1, [2, [3, 4], 5], 6, [7, 8]]
# [[2, [3, 4], 5], 6, [7, 8]]
# [2, [3, 4], 5]
# [[3, 4], 5]
def mysum3(lst):
    s = 0
    for l in lst:
        if isinstance(l, list):
            s += mysum3(l)
        else:
            s += l
    return s

print 'sum should be 36', mysum3(l)
print(mysum3([1, [2, [3, [4, [5]]]]]))
print(mysum3([[[[[1], 2], 3], 4], 5]))


from random import sample
from random import seed
from random import randrange

seed(1234)
population = [randrange(10,100,1) for i in range(100)]
print('population = {}'.format(population))
datapoints = [tuple(sample(population, 3)) for i in range(10)]
abitrary_dp = sample(datapoints,2)
print('abitrary datpoits = {}'.format(abitrary_dp))