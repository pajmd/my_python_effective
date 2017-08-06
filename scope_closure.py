def func(x,y=None):
    def func2c():
        if not y:
            return x + 1
        else:
            x = 3
            return x + y
    return func2c


def func1(param=None):
    def func2():
        if not param:
            param = 'default' # this makes param local but the line before
                              # complains because param is not assigned yet
        print param
    # Just return func2.
    return func2


if __name__ == '__main__':
    func1('test')()