
# IS is used to test the identity
# == is used to test the equality

a = 'pub'
b = ''.join(['p', 'u', 'b'])
c = 'pub'

# behind the scene python reference the same object for a and c

print('a == b: {}'.format(a == b)) # result True
print('a is b: {}'.format(a is b)) # result False
print('a == c: {}'.format(a == c)) # result True
print('a is c: {}'.format(a is c)) # result True

# for boolean values, you shouldn't be doing comparisons at all. Instead of:
x = True
if x == True:
    pass
#write:
if x:
    pass

# For comparing against None, is None is preferred over == None.