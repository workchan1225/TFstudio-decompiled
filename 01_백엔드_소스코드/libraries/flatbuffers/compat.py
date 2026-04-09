# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compat.pyc (Python 3.11)

'''A tiny version of `six` to help with backwards compability.

Also includes compatibility helpers for numpy.
'''
import sys
PY2 = sys.version_info[0] == 2
PY26 = sys.version_info[0:2] == (2, 6)
PY27 = sys.version_info[0:2] == (2, 7)
PY275 = sys.version_info[0:3] >= (2, 7, 5)
PY3 = sys.version_info[0] == 3
PY34 = sys.version_info[0:2] >= (3, 4)
if PY3:
    import importlib.machinery as importlib
    string_types = (str,)
    binary_types = (bytes, bytearray)
    range_func = range
    memoryview_type = memoryview
    struct_bool_decl = '?'
else:
    import imp
    string_types = (unicode,)
    if PY26 or PY27:
        binary_types = (str, bytearray)
    else:
        binary_types = (str,)
    range_func = xrange
    if not (PY26 or PY27) and PY275:
        memoryview_type = buffer
        struct_bool_decl = '<b'
    else:
        memoryview_type = memoryview
        struct_bool_decl = '?'

def import_numpy():
    '''Returns the numpy module if it exists on the system,

  otherwise returns None.
  '''
    if PY3:
        numpy_exists = importlib.machinery.PathFinder.find_spec('numpy') is not None
    else:
        
        try:
            imp.find_module('numpy')
            numpy_exists = True
        except ImportError:
            numpy_exists = False

        if numpy_exists:
            import numpy as np
        else:
            np = None
    return np


class NumpyRequiredForThisFeature(RuntimeError):
    '''Error raised when user tries to use a feature that

  requires numpy without having numpy installed.
  '''
    pass
