
# variables (or specifically names) belong to a scope or rather a namespace.
# Regarding variable in def function. The name is "created" when the function is called
# which allows recursive functions to get a new namespace when they are called.
# A variable is define a the time it is defined and become available in its entire namespace
#  i.e. the function or mudule.
# Unlike other languges if while ... don't create a new scope.
# It allow things to work:
# v1 = 10
# if v1 > 9:
#    v2 = 3
# print v2
#
# Scope hierarchy or search for names is:
# Local: within a function
# Enclosing function (ie function wrapping another function)
# Global: i.e. the module = file (not inter modules)
# Built in: at python level (like open, range, tuple -see dir(__builtin__) ...)
#
# For a global variable to be change if a function it has to be defined
# global <varname> in the function


y, z = 1, 2                    # Global variables in module
print('y={} z={}'.format(y,z))
def all_global():
    global x                   # Declare globals assigned
    x = y + z                  # No need to declare y, z: LEGB rule
all_global()
print('x = y + z ={} y={} z={}'.format(x,y,z))

y, z = 1, 2                    # Global variables in module
print('y={} z={}'.format(y,z))
def all_global():
    global x                   # Declare globals assigned
    z = 9                      # the assignment defines z as local to the function
    x = y + z                  # No need to declare y, z: LEGB rule
all_global()
print('x = y + z ={} y={} z={}'.format(x,y,z))

y, z = 1, 2                    # Global variables in module
print('y={} z={}'.format(y,z))
def all_global():
    global x                   # Declare globals assigned
    global z                   # gloabl z give write access to the function
    z = 9
    x = y + z                  # No need to declare y, z: LEGB rule
all_global()
print('x = y + z ={} y={} z={}'.format(x,y,z))


def f():
    try:
	    print s
    except Exception as ex:
        print('Because of the assignment to s inside of f() puthon creates a reference, '
              'but the first print statement throws this error message '
              'because it is not bound yet.\n{}'.format(ex))
	s = "Me too."
	print s
s = "I hate spam."
f()
print s

# enclosed function trying to modify enclosing scope variable
#
# nonlocal use in python 3
#
def enclosing():
    x = 4;
    def enclosed():
        print ('in enclosed function x={}'.format(x))
    print ('in enclosing function x={}'.format(x))
    enclosed()
    print ('in enclosing function after calling enclosed x={}'.format(x))
enclosing()

def enclosing():
    x = 4;
    def enclosed():
        x = 6
        print ('in enclosed function x={}'.format(x))
    print ('in enclosing function x={}'.format(x))
    enclosed()
    print ('in enclosing function after calling enclosed x={}'.format(x))
enclosing()

def enclosing():
    x = [4];
    def enclosed():
        #nonlocal x = 6 # instaead of modifying an object in this case a simple list
        # in python3 I could keep my number and decalre it as nonlocal
        x[0] = 6;
        print ('in enclosed function x={}'.format(x))
    print ('in enclosing function x={}'.format(x))
    enclosed()
    print ('in enclosing function after calling enclosed x={}'.format(x))
enclosing()

# 
# exception or weird case of the loop variable
#
def makeActions(  ):
    acts = []
    for i in range(5):# Tries to remember each i
        acts.append(lambda x: i ** x)    # All remember same last i when the lambda is executed!
                                        # the value the referenced variable had in the last loop iteration.
    return acts

acts = makeActions(  )
print acts[0](2) == acts[1](2) ==  acts[2](2) == acts[3](2) == acts[4](2) # True

def makeActions():
    acts = []
    for i in range(5):# Tries to remember each i
        acts.append(lambda x, j=i: j ** x)    # default are evaluated at definition time
    return acts

acts = makeActions()
print acts[0](2) == acts[1](2) ==  acts[2](2) == acts[3](2) == acts[4](2) # False
