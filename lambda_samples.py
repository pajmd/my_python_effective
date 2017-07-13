
# a lambda is an expression to works like a function, but because it
# it is an expression, it can be used were function can't, in list as ex.
# a lambda function can take o to several arguments and return some computation
# in can contain only one statement
# lambda are some kind of anonymous functions

f = lambda x: x*x

# equivalent to
def g(x):
    return x*x

print('f(2) = {}'.format(f(2)))

f = lambda x,y: {'x':x, 'y': y, 'x+y':x+y, 'x-y':x-y, 'y-x':y-x}

print('f(5, 7) = {}'.format(f(5,7)))