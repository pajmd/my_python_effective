from pkg import *

# print i # <== would work if __all__ is commented out
print exported_a.a
print exported_b.b
# print not_exported_c.c # <== will never work even if __all__ is commented out