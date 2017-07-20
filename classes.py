class SuperToto(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def do(self, p1):
        return self.v1 + p1

    # def __getattribute__(self, item):
    #     print("It seems like __getattribute__ is always called: {}".format(item))
    #     self.__dict__[item]



class Toto(SuperToto):
    def __init__(self, v1, v2, v3):
        SuperToto.__init__(self, v1, v2)
        self.v3 = v3

if __name__ == '__main__':
    print 'Simple Inheritance'

    s = SuperToto('do ', "don't")
    print s.do('stuff')
    t = Toto('do ', "don't", 'what')
    print t.do('other stuff ')

class Super1(object):
    x = 1
    z = 11
    def __init__(self):
        self.v1 = 14
        self.v2 = 15


class Super2(object):
    y = 2
    z = 22
    def __init__(self):
        self.v3 = 24
        self.v2 = 25


class Child(Super1, Super2):

    a_class_attribute = 99

    def __init__(self):
        Super1.__init__(self)
        Super2.__init__(self)
        self.v1 = 4

    def do_somethin(self):
        pass

    def __pseudo_private_class_attr(self):
        '''
        :return: the double _ prefix makes python append internally the class name to the attribute
        '''
        pass


if __name__ == '__main__':
    print '\n\nMultiple Inheritance Search tree order:\n"' \
          ' from bottom (instance) up (class, super classes left to right'
    child = Child()
    print('child v1 {}'.format(child.v1))
    print('child v2 {}'.format(child.v2))
    print('child v3 {}'.format(child.v3))
    print('child x {}'.format(child.x))
    print('child y {}'.format(child.y))
    print('child z {}'.format(child.z)) # 11 is printed bc it is found first in Super1
    print child.__class__
    print child.__class__.__name__
    print dir(child.__class__)
    print('\n__dict__ only contains the instance attribute')
    print('Child dict = {}'.format(child.__class__.__dict__))
    print('child dict = {}'.format(child.__dict__))

    print('\ndir shows the entire namespace')
    print ('dir on child = {}'.format(dir(child)))
    print ("child's module = {}".format(child.__module__))
    print ('dir on Child = {}'.format(dir(Child)))


#######################################################################################################################

#  __getattr__ becomes very handy when composition is used instead of inheritence

class UsedAsComposite(object):
    def __init__(self, v1):
        self.v1 = v1

    def meth1(self, p):
        return self.v1 + p

    def __repr__(self):
        return 'Composite v1: {}'.format(self.v1)

class Compositer(object):

    def __init__(self, v, v0):
        self.v = v
        self.used_as_composite = UsedAsComposite(v0)

    def meth2(self, p):
        return self.v1 + self.v - p

    def __getattr__(self, item):
        '''Called when an attribute lookup has not found the attribute in the usual places (i.e. it is not
        an instance attribute nor is it found in the class tree for self).
        Note that if the attribute is found through the normal mechanism, __getattr__() is not called'''
        # lambda works if attribute is a function call
        print('%s was not found on the instance or the class tree so __getattr__ is called'%item)
        return getattr(self.used_as_composite, item, lambda x : 'unknown attribute: {} param: {}'.format(item, x))

    def __repr__(self):
        return 'Compositer v: {} {}'.format(self.v, str(self.used_as_composite))

if __name__ == '__main__':
    print '\n\nComposites or Delegation:'

    c = Compositer(10, 100)
    print('Compositer meth2', c.meth2(50))
    print('Compositer meth1', c.meth1(30))
    print('Compositer call to unknown method', c.godknows(22))
    print('Compositer use unknown "stuff" attribute', c.stuff)
    c.some_other_attibute = 'I was defined on the instance so __getattr__ will not be call to find me'
    print('Compositer instance attribute', c.some_other_attibute)
    print c


print '\n\nClass atttibute:'

class ObjectCount(object):
    count = 0

    def stuff(self):
        pass

c1 = ObjectCount()
c2 = ObjectCount()

print('ObjectCount={} c1={} c2={}'.format(ObjectCount.count, c1.count, c2.count))
c2.count += 1
print('ObjectCount={} c1={} c2={}'.format(ObjectCount.count, c1.count, c2.count))
c1.count = c1.count + 1
print('ObjectCount={} c1={} c2={}'.format(ObjectCount.count, c1.count, c2.count))


#######################################################################################################################

print '\n\nAbstract Super class: a class that expects parts of its behavior to be provided by its subclasses. '

class AbstractSuperClass(object):

    def do_stuff(self):
        print('I am doing stuff')

    def delgate(self):
        self.do_real_work()

    def do_real_work(self):
        '''to make it more obvious we are defining and abstract we define do_real_work and assert false which
        causes the programme to raise an AssertioError exit(1) or we raise an NotImplementedError'''
        # assert False
        raise NotImplementedError('Error: do_real_work should be implemented in a sub class')

class SubClass(AbstractSuperClass):
    def do_real_work(self):
        print ('{} Doing the real work'.format(self.__class__.__name__))

class SubClass2(AbstractSuperClass):
    pass

asc = AbstractSuperClass()
try:
    asc.delgate()
except NotImplementedError as ex:
    print ex.message
sb = SubClass()
sb.delgate()
sb2 = SubClass2()
try:
    sb2.delgate()
except Exception as ex:
    print(ex.message)


print('\nUsing the new syntax in 2.7 (similar in 3.3)')

from abc import ABCMeta, abstractmethod

class AbstractSuperClassNew(object):
    __metaclass__ = ABCMeta
    def do_stuff(self):
        print('I am doing stuff')

    def delgate(self):
        self.do_real_work()

    @abstractmethod
    def do_real_work(self):
        pass


try:
    absn = AbstractSuperClassNew()
except Exception as ex:
    print('{} Fails as soon as the super class is instantiated: {}'.format(type(ex).__name__, ex))


class SubAbstractSuperClassNew(AbstractSuperClassNew):
    pass

try:
    sabsn = SubAbstractSuperClassNew()
except TypeError as ex:
    print('Fails as soon as the sub class is instantiated: {}'.format(ex))

#######################################################################################################################


print('\n\nOverriding __call__: the __call__ method is called when an instance of a class is called '
      '\npassing along whatever positional or keyword arguments were sent'
      '\nIt is a great to pass the state of an object')

class Button(object):
    def __init__(self, color):
        self.color = color

    def __call__(self, *arg, **kwarg):
        print('{} {}'.format(self.color, arg[0]))

b1 = Button('green')
b2 = Button('red')

def on(button):
    button('turn on')

def off(button):
    button('turn off')

on(b1)
off(b2)


#######################################################################################################################
print('\n\nBound and ubound method')

class Spam(object):
    def do_it(self,p):
        print('Doing it {}'.format(p))

spam = Spam()
bound_method = spam.do_it # bound to an instance
bound_method(54)

unbound_method = Spam.do_it # bound to a class
unbound_method(spam, 99)

#######################################################################################################################

print('\n\nParticular method can be called without an instance: static methods'
      'work roughly like simple instance-less functions inside a class, '
      'and class methods are passed a class instead of an instance.'
      '\Usage could be keeping track of the number of instances created from a class')

class OneSolution(object):
    counter = 0
    def __init__(self):
        OneSolution.counter += 1

    def do_it(self):
        print('Doing it {}'.format(OneSolution.counter))

os1 = OneSolution()
os1.do_it()
os2 = OneSolution()
os2.do_it()

print('we could use a function')

def printNumInstances():
    print("Number of instances created: %s" % Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances = Spam.numInstances + 1

a = Spam()
b = Spam()
c = Spam()
printNumInstances()           # But function may be too far removed
                                  # And cannot be changed via inheritance
print('Spam.numInstances {}'.format(Spam.numInstances))

print('Using static/class methods')
class Methods:
    initial_val = 10
    def imeth(self, x):            # Normal instance method: passed a self
        print([self, x])

    def smeth(x):                  # Static: no instance passed
        print([x+ Methods.initial_val])

    def cmeth(cls, x):             # Class: gets class, not instance
        print([cls, x + Methods.initial_val])

    smeth = staticmethod(smeth)    # Make smeth a static method (or @: ahead)
    cmeth = classmethod(cmeth)     # Make cmeth a class method (or @: ahead)

Methods.cmeth(44) # class is automatically passed
clsm = Methods()
clsm.cmeth(33)

Methods.smeth(11)
stm = Methods()
stm.smeth(22)

class Methods:
    def imeth(self, x):            # Normal instance method: passed a self
        print([self, x])

    @staticmethod
    def smeth(x):                  # Static: no instance passed
        print([x])

    @classmethod
    def cmeth(cls, x):             # Class: gets class, not instance
        print([cls, x])

Methods.cmeth(99)
i = Methods()
i.cmeth(77)

# because class methods always receive the lowest class in an instance's tree:
# Static methods and explicit class names may be a better solution for processing data local to a class.
# Class methods may be better suited to processing data that may differ for each class in a hierarchy.
class Spam:
    numInstances = 0
    def count(cls):                    # Per-class instance counters
        cls.numInstances += 1          # cls is lowest class above instance
    def __init__(self):
        self.count()                   # Passes self.__class__ to count
    count = classmethod(count)

class Sub(Spam):
    numInstances = 0                    # if numInstances was commented out it the final display would 3 for the ys
    def __init__(self):                # Redefines __init__
        Spam.__init__(self)

class Other(Spam):                     # Inherits __init__
    numInstances = 0

x = Spam()
y1, y2 = Sub(), Sub()
z1, z2, z3, z4 = Other(), Other(), Other(), Other()
print(x.numInstances, y1.numInstances, z1.numInstances)             # Per-class data! (1, 2, 4)

print(Spam.numInstances, Sub.numInstances, Other.numInstances) # (1, 2, 4)
