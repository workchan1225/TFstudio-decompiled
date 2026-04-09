# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _py_collections.pyc (Python 3.11)

from __future__ import annotations
from itertools import filterfalse
from typing import AbstractSet
from typing import Any
from typing import Callable
from typing import cast
from typing import Collection
from typing import Dict
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import Set
from typing import Tuple
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union
from util.typing import Self
_T = TypeVar('_T', bound = Any)
_S = TypeVar('_S', bound = Any)
_KT = TypeVar('_KT', bound = Any)
_VT = TypeVar('_VT', bound = Any)

class ReadOnlyContainer:
    __slots__ = ()
    
    def _readonly(self = None, *arg, **kw):
        raise TypeError('%s object is immutable and/or readonly' % self.__class__.__name__)

    
    def _immutable(self = None, *arg, **kw):
        raise TypeError('%s object is immutable' % self.__class__.__name__)

    
    def __delitem__(self = None, key = None):
        self._readonly()

    
    def __setitem__(self = None, key = None, value = None):
        self._readonly()

    
    def __setattr__(self = None, key = None, value = None):
        self._readonly()



def ImmutableDictBase():
    '''ImmutableDictBase'''
    if TYPE_CHECKING:
        
        def __new__(cls = None, *args):
            pass

        
        def __init__(cls = None, *args):
            pass

    
    def _readonly(self = None, *arg, **kw):
        self._immutable()

    
    def clear(self = None):
        self._readonly()

    
    def pop(self = None, key = None, default = None):
        self._readonly()

    
    def popitem(self = None):
        self._readonly()

    
    def setdefault(self = None, key = None, default = None):
        self._readonly()

    
    def update(self = None, *arg, **kw):
        self._readonly()


ImmutableDictBase = <NODE:27>(ImmutableDictBase, 'ImmutableDictBase', ReadOnlyContainer, Dict[(_KT, _VT)])

def immutabledict():
    '''immutabledict'''
    pass
# WARNING: Decompyle incomplete

immutabledict = <NODE:27>(immutabledict, 'immutabledict', ImmutableDictBase[(_KT, _VT)])

def OrderedSet():
    '''OrderedSet'''
    pass
# WARNING: Decompyle incomplete

OrderedSet = <NODE:27>(OrderedSet, 'OrderedSet', Set[_T])

class IdentitySet:
    _members: 'Dict[int, Any]' = "A set that considers only object id() for uniqueness.\n\n    This strategy has edge cases for builtin types- it's possible to have\n    two 'foo' strings in one of these sets, for example.  Use sparingly.\n\n    "
    
    def __init__(self = None, iterable = None):
        self._members = dict()
        if iterable:
            self.update(iterable)
            return None

    
    def add(self = None, value = None):
        self._members[id(value)] = value

    
    def __contains__(self = None, value = None):
        return id(value) in self._members

    
    def remove(self = None, value = None):
        del self._members[id(value)]

    
    def discard(self = None, value = None):
        
        try:
            self.remove(value)
            return None
        except KeyError:
            return None


    
    def pop(self = None):
        
        try:
            pair = self._members.popitem()
            return pair[1]
        except KeyError:
            raise KeyError('pop from an empty set')


    
    def clear(self = None):
        self._members.clear()

    
    def __eq__(self = None, other = None):
        if isinstance(other, IdentitySet):
            return self._members == other._members

    
    def __ne__(self = None, other = None):
        if isinstance(other, IdentitySet):
            return self._members != other._members

    
    def issubset(self = None, iterable = None):
        if isinstance(iterable, self.__class__):
            other = iterable
        else:
            other = self.__class__(iterable)
        if len(self) > len(other):
            return False
        for m in None(other._members.__contains__, iter(self._members.keys())):
            return False
            return True

    
    def __le__(self = None, other = None):
        if not isinstance(other, IdentitySet):
            return NotImplemented
        return None.issubset(other)

    
    def __lt__(self = None, other = None):
