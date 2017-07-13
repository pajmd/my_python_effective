
# generator can only be itereated once
l=[1,3,4,5,6,7]
g = (x for x in l)
for i in g:
    print i
print('Will print nothing')
for i in g:
    print i

# the yield statement is used to define generators, replacing the return of a function
# to provide a result to its caller without destroying local variables.
# Unlike a function, where on each call it starts with new set of variables,
# a generator will resume the execution where it was left off
# Generators do their calculation on the fly, consume little memory

# difference between xange and range is xrange returns a generator
def g(x):
    print('g is entering')
    c = 3
    for i in range(x):
        print('g is yielding')
        yield i * c
    print('g is done')

print('Using yield')
for i in g(5):
    print i

print('Iterate using next on the generator')
try:
    gen = g(7)
    while True:
        print(next(gen))
except StopIteration as ex:
    print('generator exhausted')

def g(x):
    print('g is entering')
    for c in range(2,4):
        for i in range(x):
            print('g is yielding')
            yield i * c
        print('series * by {}'.format(c))
    print('g is done')

print('Will print 2 series')
try:
    gen = g(4)
    while True:
        print(next(gen))
except StopIteration as ex:
    print('generator exhausted')