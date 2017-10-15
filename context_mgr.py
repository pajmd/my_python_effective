from contextlib import contextmanager, closing


#
# https://jeffknupp.com/blog/2016/03/07/python-with-context-managers/

class Ctx(object):
    def __init__(self, val):
        print('__init__: {}'.format(val))



    def do(self, par):
        print(par)

    def __enter__(self):
        print('__enter__')
        def func(x):
            return 'Doing: {}'.format(x)
        return func


    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__')


class Do(object):

    def __init__(self, stuff):
        print('class Do')
        self.stuff = stuff

    def close(self):
        print('closing {}: {}'.format(self.__class__, self.stuff))

    def get(self, var):
        print('getting : {}'.format(var))


def try_it():
    with Ctx(999) as c:
        print(c('stuff'))
    print('Fin')

if __name__ == '__main__':
    try_it()
    with closing(Do('using closing')) as d:
        d.get('some data')
    print('fininshed with closing')
