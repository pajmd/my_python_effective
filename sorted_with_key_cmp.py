
# sorted takes a list and returns a NEW list with those elements in sorted order.
l = [(9,1), (5,3), (4,66), (12,45)]
nl = sorted(l, key= lambda t:t[0])
print('l = {}'.format(l))
print('nl = {}'.format(nl))
rnl = sorted(l, key=lambda t:t[0], reverse=True)
print('reverse sorted rnl = {}'.format(rnl))
cl = sorted(l, cmp=lambda t1, t2: 1 if t1[0]+t1[1] >= t2[0]+t2[1] else -1)
print('with compare function sorted rnl = {}'.format(cl))


# list have a sort function that sorts in place so does not return a new list.
l.sort(key=lambda t:t[1])
print('l = {}'.format(l))