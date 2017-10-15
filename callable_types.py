
# Not much to do with callable types which as functio, method, callable calss instances (__call__),
# generatos, builtin funcations ....
# the exmaple shows __closure__ which contains the list of cells i.e. bound variables

def func(x, z=[]):
    '''
    this is a function
    :return:
    '''
    def some_closure(y):
        res = x*y
        print('{x}*{y}={}'.format(res, x=x,y=y))
        z.append(res)
        print('list of results = {}'.format(res))
    return some_closure


# the default argument is assigned when def is encouter, i.e. when the module is loaded
# and NOT when the function is called. So be care with mutable default argument
def careful_with_default_args(v, l=[]):
    v = v * 3
    l.append(v)
    print('list = {}'.format(l))


if __name__ == '__main__':
    print(func.__doc__)
    print(func.func_doc)
    f = func(5)
    f(2)
    print('shows the bindings f.__closure__ = {}'.format(f.func_closure))
    print('func.__closure__ = {}'.format(func.func_closure))
    print('func.__code__ = {}'.format(func.__code__))
    f(3)
    f(4)
    careful_with_default_args(1); careful_with_default_args(2); careful_with_default_args(3)
