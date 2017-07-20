
# all explicitly exports a and b with the form: from module import *
# if __all__ was commented out from module import * would bring a,b,and c
__all__ = ['a','b']

a = 11
b = 22
c = 33
_d = 44 # <= even if __all__ was commented ou from module_explicitly_exports_thru__all__.py import * in hte importer
        # would not see it