# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _asarray.pyc (Python 3.11)

'''
Functions in the ``as*array`` family that promote array-likes into arrays.

`require` fits this category despite its name not matching this pattern.
'''
from overrides import array_function_dispatch, set_array_function_like_doc, set_module
from multiarray import array, asanyarray
__all__ = [
    'require']
POSSIBLE_FLAGS = {
    'C': 'C',
    'C_CONTIGUOUS': 'C',
    'CONTIGUOUS': 'C',
    'F': 'F',
    'F_CONTIGUOUS': 'F',
    'FORTRAN': 'F',
    'A': 'A',
    'ALIGNED': 'A',
    'W': 'W',
    'WRITEABLE': 'W',
    'O': 'O',
    'OWNDATA': 'O',
    'E': 'E',
    'ENSUREARRAY': 'E' }
require = (lambda a = set_module('numpy'), dtype = (None, None), requirements = {
    'like': None }, *, like, subok = None, order = None: pass# WARNING: Decompyle incomplete
)()()
_require_with_like = array_function_dispatch()(require)
