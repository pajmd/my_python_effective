
# map applies a function to each item of an iterable and returnsa ?list?

l = [1,2,3,4,5]
the_function = lambda x: x*x
m = map(the_function, l)
print('map = {}'.format(m))
print('map[2:4] = {}'.format(m[2:4]))


d = {
    'a': 0,
    'b': 1,
    'c': 2
}

def f(t):
    # here I was trying to filter it won't work bc it returns none for
    # the item I am trying to exclude. What I can do is modify the value
    #if t[1] % 2 == 0:
    #    return t
    # t[1] = t[1] % 2  You can't modify a tuple
    return (t[0], t[1] % 2)

d2 = map(lambda (k,v) : (k, v) , d.iteritems())
print('d2 = {}'.format(d2))
print('d2 = {}'.format(dict(d2)))

d3 = dict(map(f , d.iteritems()))
print('d3 = {}'.format(d3))
#print('d3 = {}'.format(dict(d2)))

# list comprehensions are better when maps if filter is necessary (or filter will need to be applied)
print('list_comp = {}'.format([x*x for x in l if x%2 == 0]))


#Filter takes a function returning True or False
# and applies it to a sequence, returning a list of only those members of the sequence
# for which the function returned True

df = filter(lambda t: not t[1] % 2, d.iteritems())
print('df = {}'.format(df))

# reduces a list to a single value by combining elements via a supplied function.
# At each step, reduce passes the current result, along with the next item from the iterator,
rl = reduce(lambda x,y: x + y, l)
print('rl = {}'.format(rl))

# iterating over a dictionary returns the item key only
# use iteritems to get the tuple key, value
rk = reduce(lambda x,y: x + y, d)
print('rk = {}'.format(rk))

def rf(tr, t):
    return tr[0] + t[0], tr[1] + t[1]

# rd = reduce(lambda tr, t: tr + t, d.iteritems())
rd = reduce(rf, d.iteritems())
print('rd = {}'.format(dict([rd])))

#considering to keep the order of the key with an order dict
from collections import OrderedDict
od = OrderedDict(sorted(d.iteritems(), key = lambda t: t[0] )
)
rod = reduce(rf, od.iteritems())
print('rod = {}'.format(dict([rod])))

# creating a dictionary from a tuple of tuples (pairs) is weird you need to
# put the tuple in a tuple followed by a comma
# it's easier to do it from a list of tuples
t = (('res', 3),)
print('t2d = {}'.format(dict(t)))

even_list = [['a', 1]]
print('d_from_l = {}'.format(dict(even_list)))