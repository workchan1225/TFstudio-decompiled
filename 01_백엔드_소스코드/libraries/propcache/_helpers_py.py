# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _helpers_py.pyc (Python 3.11)

'''Various helper functions.'''
import sys
from collections.abc import Mapping
from functools import cached_property
from typing import Any, Callable, Generic, Optional, Protocol, TypeVar, Union, overload
__all__ = ('under_cached_property', 'cached_property')
if sys.version_info >= (3, 11):
    from typing import Self
else:
    Self = Any
_T = TypeVar('_T')
_Cache = TypeVar('_Cache', bound = Mapping[(str, Any)])

def _CacheImpl():
    '''_CacheImpl'''
    _cache: _Cache = '_CacheImpl'

_CacheImpl = <NODE:27>(_CacheImpl, '_CacheImpl', Protocol[_Cache])

def under_cached_property():
    '''under_cached_property'''
    __doc__ = 'Use as a class method decorator.\n\n    It operates almost exactly like\n    the Python `@property` decorator, but it puts the result of the\n    method it decorates into the instance dict after the first call,\n    effectively replacing the function it decorates with an instance\n    variable.  It is, in Python parlance, a data descriptor.\n    '
    
    def __init__(self = None, wrapped = None):
        self.wrapped = wrapped
        self.__doc__ = wrapped.__doc__
        self.name = wrapped.__name__

    __get__ = (lambda self = None, inst = None, owner = overload: pass)()
    __get__ = (lambda self = None, inst = None, owner = overload: pass)()
    
    def __get__(self = None, inst = None, owner = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __set__(self = None, inst = None, value = None):
        raise AttributeError('cached property is read-only')


under_cached_property = <NODE:27>(under_cached_property, 'under_cached_property', Generic[_T])
