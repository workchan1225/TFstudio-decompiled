# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Utilities for getting information about Numba C extensions
'''
import os

def get_extension_libs():
    '''Return the .c files in the `numba.cext` directory.
    '''
    libs = []
    base = get_path()
    for fn in os.listdir(base):
        if fn.endswith('.c'):
            fn = os.path.join(base, fn)
            libs.append(fn)
        return libs


def get_path():
    '''Returns the path to the directory for `numba.cext`.
    '''
    return os.path.abspath(os.path.join(os.path.dirname(__file__)))
