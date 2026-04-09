# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''
Helper classes / mixins for defining types.
'''
from abstract import ArrayCompatible, Dummy, IterableType, IteratorType
from numba.core.errors import NumbaTypeError, NumbaValueError

class Opaque(Dummy):
    '''
    A type that is a opaque pointer.
    '''
    pass


class SimpleIterableType(IterableType):
    pass
# WARNING: Decompyle incomplete


class SimpleIteratorType(IteratorType):
    pass
# WARNING: Decompyle incomplete


class Buffer(ArrayCompatible, IterableType):
    pass
# WARNING: Decompyle incomplete
