import sys

print (__name__, 'path=', sys.path)
import sub.spam                 # <== Works if move modules to pkg below main file

