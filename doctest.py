
class SomeClass(object):
    default_color = 'black'

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, a_color):
        if a_color in ['red', 'blue']:
            self._color = a_color
        else:
            self._color = SomeClass.default_color

def using():
    '''


    >>> c1 = SomeClass()
    >>> c1.color = 'green'
    >>> print('c1.color ={}'.format(c1.color ))
    c1.color =black
    >>> c1.color = 'blue'
    >>> print('c1.color ={}'.format(c1.color ))
    c1.color =blue
    >>> c1.default_color = 'red'
    >>> print('c1.color ={}'.format(c1.color ))
    c1.color =blue
    >>> c2 = SomeClass()
    >>> c2.color = 'yellow'
    >>> print('c2.color ={}'.format(c2.color ))
    c2.color =black
    '''
    c1 = SomeClass()
    c1.color = 'green'
    print('c1.color ={}'.format(c1.color ))
    c1.color = 'blue'
    print('c1.color ={}'.format(c1.color ))
    c1.default_color = 'red'
    print('c1.color ={}'.format(c1.color ))
    c2 = SomeClass()
    c2.color = 'yellow'
    print('c2.color ={}'.format(c2.color ))

if __name__ == '__main__':
    import doctest
    doctest.testmod()
