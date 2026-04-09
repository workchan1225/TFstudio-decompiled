# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abstract.pyc (Python 3.11)

from abc import ABCMeta, abstractmethod
from typing import Dict as ptDict, Type as ptType
import itertools
import weakref
from functools import cached_property
import numpy as np
from numba.core.utils import get_hashable_key
_typecodes = itertools.count()

def _autoincr():
    n = next(_typecodes)
# WARNING: Decompyle incomplete

_typecache: ptDict[(weakref.ref, weakref.ref)] = { }

def _on_type_disposal(wr, _pop = (_typecache.pop,)):
    _pop(wr, None)


class _TypeMetaclass(ABCMeta):
    pass
# WARNING: Decompyle incomplete


def _type_reconstructor(reconstructor, reconstructor_args, state):
    '''
    Rebuild function for unpickling types.
    '''
    pass
# WARNING: Decompyle incomplete


def Type():
    '''Type'''
    pass
# WARNING: Decompyle incomplete

Type = <NODE:27>(Type, 'Type', metaclass = _TypeMetaclass)

class Dummy(Type):
    '''
    Base class for types that do not really have a representation and are
    compatible with a void*.
    '''
    pass


class Hashable(Type):
    '''
    Base class for hashable types.
    '''
    pass


class Number(Hashable):
    '''
    Base class for number types.
    '''
    
    def unify(self, typingctx, other):
        """
        Unify the two number types using Numpy's rules.
        """
        numpy_support = numpy_support
        import numba.np
        if isinstance(other, Number):
            a = numpy_support.as_dtype(self)
            b = numpy_support.as_dtype(other)
            sel = np.promote_types(a, b)
            return numpy_support.from_dtype(sel)



class Callable(Type):
    '''
    Base class for callables.
    '''
    get_call_type = (lambda self, context, args, kws: pass)()
    get_call_signatures = (lambda self: pass)()
    get_impl_key = (lambda self, sig: pass)()


class DTypeSpec(Type):
    '''
    Base class for types usable as "dtype" arguments to various Numpy APIs
    (e.g. np.empty()).
    '''
    dtype = (lambda self: pass)()()


class IterableType(Type):
    '''
    Base class for iterable types.
    '''
    iterator_type = (lambda self: pass)()()


class Sized(Type):
    '''
    Base class for objects that support len()
    '''
    pass


class ConstSized(Sized):
    '''
    For types that have a constant size
    '''
    __len__ = (lambda self: pass)()


class IteratorType(IterableType):
    pass
# WARNING: Decompyle incomplete


class Container(IterableType, Sized):
    '''
    Base class for container types.
    '''
    pass


class Sequence(Container):
    '''
    Base class for 1d sequence types.  Instances should have the *dtype*
    attribute.
    '''
    pass


class MutableSequence(Sequence):
    '''
    Base class for 1d mutable sequence types.  Instances should have the
    *dtype* attribute.
    '''
    mutable = True


class ArrayCompatible(Type):
    '''
    Type class for Numpy array-compatible objects (typically, objects
    exposing an __array__ method).
    Derived classes should implement the *as_array* attribute.
    '''
    array_priority = 0
    as_array = (lambda self: pass)()()
    ndim = (lambda self: self.as_array.ndim)()
    layout = (lambda self: self.as_array.layout)()
    dtype = (lambda self: self.as_array.dtype)()


class Literal(Type):
    pass
# WARNING: Decompyle incomplete


class TypeRef(Dummy):
    pass
# WARNING: Decompyle incomplete


class InitialValue(object):
    '''
    Used as a mixin for a type will potentially have an initial value that will
    be carried in the .initial_value attribute.
    '''
    
    def __init__(self, initial_value):
        self._initial_value = initial_value

    initial_value = (lambda self: self._initial_value)()


class Poison(Type):
    pass
# WARNING: Decompyle incomplete
