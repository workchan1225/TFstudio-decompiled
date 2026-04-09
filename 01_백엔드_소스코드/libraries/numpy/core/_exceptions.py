# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

"""
Various richly-typed exceptions, that also help us deal with string formatting
in python where it's easier.

By putting the formatting in `__str__`, we also avoid paying the cost for
users who silence the exceptions.
"""
from _utils import set_module

def _unpack_tuple(tup):
    if len(tup) == 1:
        return tup[0]


def _display_as_base(cls):
    '''
    A decorator that makes an exception class look like its base.

    We use this to hide subclasses that are implementation details - the user
    should catch the base type, which is what the traceback will show them.

    Classes decorated with this decorator are subject to removal without a
    deprecation warning.
    '''
    pass
# WARNING: Decompyle incomplete


class UFuncTypeError(TypeError):
    ''' Base class for all ufunc exceptions '''
    
    def __init__(self, ufunc):
        self.ufunc = ufunc


_UFuncNoLoopError = <NODE:12>()
_UFuncBinaryResolutionError = <NODE:12>()
_UFuncCastingError = <NODE:12>()
_UFuncInputCastingError = <NODE:12>()
_UFuncOutputCastingError = <NODE:12>()
_ArrayMemoryError = <NODE:12>()
