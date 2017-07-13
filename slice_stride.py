
# a=[0,1,2,3,4,5]
# b = a[start:end:stride] stride beind a step
#
# slicing returns a new object
# b = a[:]
# a == b True, a is b False
# postive start n = from n (first item n = 0)
# positive end n = goes up to rank n -1
# negative n start = goes to the end takes the last n items to the end
# negative n end   = goes to the end and removes n items
# positive stride = takes every n item starting from 0 relative to the slice
# negative stride -n =  works its way backward takes every n item
#                       if a start is spcified it, start backward from start

print('[0,1,2,3,4,5][:]={}'.format([0,1,2,3,4,5][:])) # [0,1,2,3,4,5][:]=[0, 1, 2, 3, 4, 5]
print('[0,1,2,3,4,5][-1:]={}'.format([0,1,2,3,4,5][-1:])) # [0,1,2,3,4,5][-1:]=[5]
print('[0,1,2,3,4,5][-6:]={}'.format([0,1,2,3,4,5][-6:])) # [0,1,2,3,4,5][-6:]=[0, 1, 2, 3, 4, 5]

print('[0,1,2,3,4,5][2:]={}'.format([0,1,2,3,4,5][2:])) # [0,1,2,3,4,5][2:]=[2, 3, 4, 5]
print('[0,1,2,3,4,5][2:4]={}'.format([0,1,2,3,4,5][2:4])) # [0,1,2,3,4,5][2:4]=[2, 3]
print('[0,1,2,3,4,5][-3:]={}'.format([0,1,2,3,4,5][-3:])) # [0,1,2,3,4,5][-3:]=[3, 4, 5]
print('[0,1,2,3,4,5][:-2]={}'.format([0,1,2,3,4,5][:-2])) # [0,1,2,3,4,5][:-2]=[0, 1, 2, 3]

print('[0,1,2,3,4,5][::1]={}'.format([0,1,2,3,4,5][::1])) # [0,1,2,3,4,5][::1]=[0, 1, 2, 3, 4, 5]
print('[0,1,2,3,4,5][::2]={}'.format([0,1,2,3,4,5][::2])) # [0,1,2,3,4,5][::2]=[0, 2, 4]
print('[0,1,2,3,4,5][::3]={}'.format([0,1,2,3,4,5][::3])) # [0,1,2,3,4,5][::3]=[0, 3]
print('[0,1,2,3,4,5][1::1]={}'.format([0,1,2,3,4,5][1::1])) # [0,1,2,3,4,5][::1]=[1, 2, 3, 4, 5]

print('[0,1,2,3,4,5][2::-1]={}'.format([0,1,2,3,4,5][2::-1])) # 0,1,2,3,4,5][2::-1]=[2, 1, 0]
print('[0,1,2,3,4,5][-2::-1]={}'.format([0,1,2,3,4,5][-2::-1])) # [0,1,2,3,4,5][-2::-1]=[4, 3, 2, 1, 0]


print('[0,1,2,3,4,5][:]={}'.format([0,1,2,3,4,5][:]))
print('[0,1,2,3,4,5][:]={}'.format([0,1,2,3,4,5][:]))
print('[0,1,2,3,4,5][:]={}'.format([0,1,2,3,4,5][:]))
