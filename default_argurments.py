
# the default argument is assigned when def is encouter, i.e. when the module is loaded
# and NOT when the function is called. So be care with mutable default argument
# in this, the list is not "created" each time the functio is called but when the function
# is defined so it keeps growing

def careful_with_default_args(v, l=[]):
    v = v * 3
    l.append(v)
    print('list = {}'.format(l))

careful_with_default_args(1); careful_with_default_args(2); careful_with_default_args(3)
