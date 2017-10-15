'''
partial is used to create a new callable based on a callable and frozen argument from this callable
'''

from functools import partial

def func(a, c, d, e, f=None):
    print('(c+d) * a = {} e={} f={}'.format((c+d) * a, e, f))

cdfunc = partial(func, 2)

cdfunc(3,4,5, f='stuff')