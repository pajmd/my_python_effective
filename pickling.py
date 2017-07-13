
# pickle used to de/serialize python objects is unsafe bc payload can tempered with when deserialing
# because it exposes the program used to deserialzed
# a safer approach is to use the json module

# There is a marsal module that is unsafe as well and and mainly used to read/write pseudo-compiled python
# which implementation can change at any time and pretty much reserved to the python maintainers

class MyClass(object):
    def __init__(self, name, width=0, length=0):
        self.width = width
        self.length = length
        self.name = name

    def get_surface_area(self):
        return self.length * self.width

    def __repr__(self):
        return self.name+' L='+str(self.length)+' x W='+str(self.width)


football_pitch = MyClass('football', width=50, length=100)
tennis_court = MyClass('tennis', width=10, length=20)

print('Pitch {} - Surface Area = {}'.format(football_pitch, football_pitch.get_surface_area()))

file_path = 'pitches.txt'

import pickle

with open(file_path, mode='w') as fd:
    pickle.dump(football_pitch, fd)
    pickle.dump(tennis_court, fd)

with open(file_path, mode='r') as fd:
    some_pitch = pickle.load(fd)
    some_other_pitch = pickle.load(fd)
print('Some other Pitch {} - Surface Area = {}'.format(some_other_pitch, some_pitch.get_surface_area()))
print('Some Pitch {} - Surface Area = {}'.format(some_pitch, some_pitch.get_surface_area()))

print('Some Pitch attributes {} '.format(some_pitch.__dict__))

