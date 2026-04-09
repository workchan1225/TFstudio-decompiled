# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extension.pyc (Python 3.11)

import re
import functools
import distutils.core as distutils
import distutils.errors as distutils
import distutils.extension as distutils
from monkey import get_unpatched

def _have_cython():
    '''
    Return True if Cython can be imported.
    '''
    cython_impl = 'Cython.Distutils.build_ext'
    
    try:
        __import__(cython_impl, fromlist = [
            'build_ext']).build_ext
        return True
    except Exception:
        pass

    return False

have_pyrex = _have_cython
_Extension = get_unpatched(distutils.core.Extension)

class Extension(_Extension):
    pass
# WARNING: Decompyle incomplete


class Library(Extension):
    '''Just like a regular Extension, but built as a library instead'''
    pass
