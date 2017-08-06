
# These a DATA DESCRIPTOR  as they define __set__ and __get__ and or __delete__
# If for an attribute we wouldn't want to do a set, we would still define
# __set__ but raise an exception inits body
# The DESCRIPTOR DEFINING ONLY GET are for function, class/staticmethod



class IntDesc(object):
    '''Descriptor that will set and get ints on the 'class instance' users of this descriptor
    '''
    def __init__(self, attribut_name):
        '''The descriptor constructor receives the name of the class instance attribute
        so it can set/get it
        '''
        self.name = attribut_name
        print('IntDesc instance: {}'.format(self))

    def __get__(self, instance, type):
        # print('__get__ was called on IntDesc: {} - for {instance} of {type}'
        #       .format(self, instance=instance, type=type))
        return instance.__dict__.get(self.name) # or getattr(instance, self.name)

    def __set__(self, instance, value):
        # print('__set__ was called on IntDesc: {} - for {instance} value {value}'
        #       .format(self, instance=instance, value=value))
        instance.__dict__[self.name] = value # or setattr(instance, self.name, value)


# Just to show the descriptor could even create the attibute on the instance, ex: numbr
class DescSettingInsatnceValues(object):
    ''' dir(one_instance) should show
        - an_int as a desciptor (desciptor shadows the attribute) on the class
        - vol as a descriptor on the class
        - some_volume as an int on the instance
        - numbr as an int (t,num = 1000) on the instance
    '''
    an_int = IntDesc('an_int')
    vol = IntDesc('some_volume')
    # for num the descriptor will create numbr on the instance
    # t.num = 100
    num = IntDesc('numbr')
    def __init__(self, some_int, volume):
        self.an_int = some_int
        self.vol = volume
        print('UseDesc instance: {} an_int id={}'.format(self, id(self.an_int)))


# class UseDesc(object):
#     def __init__(self):
#         print('UseDesc instance: {}'.format(self))
#         self.IntDesc = 4

t = DescSettingInsatnceValues(10, 100)
print('t: {}'.format(t.an_int))
# t.an_int = 3
# print(t.an_int)
# print(t.an_int)
# t.an_int = 3
# print(t.an_int)
# print(UseDesc.an_int)
v = DescSettingInsatnceValues(5, 50)
print('v: {}'.format(v.an_int))
print('-'*80)
print('t.an_int = {} v.an_int = {}'.format(t.an_int, v.an_int))


# This desctiptor will validate the data
class DescOnlyValidatingInstanceValues(object):
    ''' vaue must be in ]50, 10['''

    def __set__(self, instance, value):
        if not 50 < value <100:
            raise ValueError('value {} must be in ]50, 100['.format(value))
        else:
            setattr(instance,'_value', value)

    def __get__(self, instance, owner):
        return getattr(instance, '_value')


class ToValidate(object):
    value = DescOnlyValidatingInstanceValues()

    def __init__(self, val):
        self.value = val

to_validate = ToValidate(60)
# to_validate._value would be the only way to get to the value of the instance if
# __get__ was not defined
print('to_validate = {}'.format(to_validate._value))
# because __get__ is defined I can just do like value was a regular attribute
print('to_validate = {}'.format(to_validate.value))
try:
    to_validate = ToValidate(20)
except ValueError as er:
    print(er.args[0])