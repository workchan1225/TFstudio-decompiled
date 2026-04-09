# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _cmp.pyc (Python 3.11)

import functools
import types
from _make import __ne__
_operation_names = {
    'eq': '==',
    'lt': '<',
    'le': '<=',
    'gt': '>',
    'ge': '>=' }

def cmp_using(eq, lt, le, gt, ge, require_same_type, class_name = (None, None, None, None, None, True, 'Comparable')):
    '''
    Create a class that can be passed into `attrs.field`\'s ``eq``, ``order``,
    and ``cmp`` arguments to customize field comparison.

    The resulting class will have a full set of ordering methods if at least
    one of ``{lt, le, gt, ge}`` and ``eq``  are provided.

    Args:
        eq (typing.Callable | None):
            Callable used to evaluate equality of two objects.

        lt (typing.Callable | None):
            Callable used to evaluate whether one object is less than another
            object.

        le (typing.Callable | None):
            Callable used to evaluate whether one object is less than or equal
            to another object.

        gt (typing.Callable | None):
            Callable used to evaluate whether one object is greater than
            another object.

        ge (typing.Callable | None):
            Callable used to evaluate whether one object is greater than or
            equal to another object.

        require_same_type (bool):
            When `True`, equality and ordering methods will return
            `NotImplemented` if objects are not of the same type.

        class_name (str | None): Name of class. Defaults to "Comparable".

    See `comparison` for more details.

    .. versionadded:: 21.1.0
    '''
    pass
# WARNING: Decompyle incomplete


def _make_init():
    '''
    Create __init__ method.
    '''
    
    def __init__(self, value):
        '''
        Initialize object with *value*.
        '''
        self.value = value

    return __init__


def _make_operator(name, func):
    '''
    Create operator method.
    '''
    pass
# WARNING: Decompyle incomplete


def _is_comparable_to(self, other):
    '''
    Check whether `other` is comparable to `self`.
    '''
    pass
# WARNING: Decompyle incomplete


def _check_same_type(self, other):
    '''
    Return True if *self* and *other* are of the same type, False otherwise.
    '''
    return other.value.__class__ is self.value.__class__
