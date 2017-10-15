import timeit

# https://stackoverflow.com/questions/472000/usage-of-slots
# By default, instances of both old and new-style classes, i.e inheriting from object, have a dictionary for attribute
# storage.
# This wastes space for objects having very few instance variables.
# The space consumption can become acute when creating large numbers of instances.
# The default can be overridden by defining __slots__ in a new-style class definition.
# The __slots__ declaration takes a sequence of instance variables and reserves just enough space in each instance
# to hold a value for each variable. Space is saved because __dict__ is not created for each instance.

a = 3,

class Foo(object):
    __slots__ = 'foo',

    def __init__(self):
        #self.foo = 300
        pass

class Bar(object): pass

slotted = Foo()
slotted2 = Foo()

not_slotted = Bar()

slotted.foo = 'un'
slotted2.foo = 'deux'

print(dir(slotted))
print(dir(slotted2))
not_slotted.foo = 'foo'
print(dir(not_slotted))

not_slotted.bar = 'bar'

def get_set_delete_fn(obj):
    def get_set_delete():
        obj.foo = 'foo'
        obj.foo
        del obj.foo
    return get_set_delete


print(min(timeit.repeat(get_set_delete_fn(slotted),  repeat=1, number=1000)))
print(min(timeit.repeat(get_set_delete_fn(not_slotted), repeat=1, number=1000)))