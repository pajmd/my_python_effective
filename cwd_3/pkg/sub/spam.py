import sys

print (__name__, 'path=', sys.path)
from . import eggs  # <== running python pkg/sub/spam.py fails because span is considered as a script not a module
                    # A top-level file is run but not imported
                    # <== running python pkg/main.py works, python will find package/module under pkg and spam is
                    # a module therefore a relative import can be done.
import imp
#imp.find_module('eggs')
#import sub.eggs as eggs # <== when run python/3 pkg/main.py this works
print(eggs.X)
