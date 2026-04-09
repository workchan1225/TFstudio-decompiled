# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: containers.pyc (Python 3.11)

'''Module for SymPy containers

    (SymPy objects that store other SymPy objects)

    The containers implemented in this module are subclassed to Basic.
    They are supposed to work seamlessly within the SymPy framework.
'''
from collections import OrderedDict
from collections.abc import MutableSet
from typing import Any, Callable
from basic import Basic
from sorting import default_sort_key, ordered
from sympify import _sympify, sympify, _sympy_converter, SympifyError
from sympy.core.kind import Kind
from sympy.utilities.iterables import iterable
from sympy.utilities.misc import as_int

class Tuple(Basic):
    pass
# WARNING: Decompyle incomplete


_sympy_converter[tuple] = lambda tup: pass# WARNING: Decompyle incomplete


def tuple_wrapper(method):
    '''
    Decorator that converts any tuple in the function arguments into a Tuple.

    Explanation
    ===========

    The motivation for this is to provide simple user interfaces.  The user can
    call a function with regular tuples in the argument, and the wrapper will
    convert them to Tuples before handing them to the function.

    Explanation
    ===========

    >>> from sympy.core.containers import tuple_wrapper
    >>> def f(*args):
    ...    return args
    >>> g = tuple_wrapper(f)

    The decorated function g sees only the Tuple argument:

    >>> g(0, (1, 2), 3)
    (0, (1, 2), 3)

    '''
    pass
# WARNING: Decompyle incomplete


class Dict(Basic):
    pass
# WARNING: Decompyle incomplete


_sympy_converter[dict] = lambda d: pass# WARNING: Decompyle incomplete


class OrderedSet(MutableSet):
    
    def __init__(self, iterable = (None,)):
        if iterable:
            self.map = (lambda .0: pass# WARNING: Decompyle incomplete
)(iterable())
            return None
        self.map = None()

    
    def __len__(self):
        return len(self.map)

    
    def __contains__(self, key):
        return key in self.map

    
    def add(self, key):
        self.map[key] = None

    
    def discard(self, key):
        self.map.pop(key)

    
    def pop(self, last = (True,)):
        return self.map.popitem(last = last)[0]

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        if not self.map:
            return f'''{self.__class__.__name__!s}()'''
        return f'''{None.__class__.__name__!s}({list(self.map.keys())!r})'''

    
    def intersection(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def difference(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def update(self, iterable):
        for val in iterable:
            self.add(val)
            return None



class TupleKind(Kind):
    pass
# WARNING: Decompyle incomplete
