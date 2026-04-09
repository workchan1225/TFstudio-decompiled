# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mixins.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import typing as t
from functools import update_wrapper
from itertools import repeat
from _internal import _missing
if t.TYPE_CHECKING:
    import typing_extensions as te
K = t.TypeVar('K')
V = t.TypeVar('V')
T = t.TypeVar('T')
F = t.TypeVar('F', bound = cabc.Callable[(..., t.Any)])

def _immutable_error(self = None):
    raise TypeError(f'''{type(self).__name__!r} objects are immutable''')


class ImmutableListMixin:
    '''Makes a :class:`list` immutable.

    .. versionadded:: 0.5

    :private:
    '''
    _hash_cache: 'int | None' = None
    
    def __hash__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce_ex__(self = None, protocol = None):
        return (type(self), (list(self),))

    
    def __delitem__(self = None, key = None):
        _immutable_error(self)

    
    def __iadd__(self = None, other = None):
        _immutable_error(self)

    
    def __imul__(self = None, other = None):
        _immutable_error(self)

    
    def __setitem__(self = None, key = None, value = None):
        _immutable_error(self)

    
    def append(self = None, item = None):
        _immutable_error(self)

    
    def remove(self = None, item = None):
        _immutable_error(self)

    
    def extend(self = None, iterable = None):
        _immutable_error(self)

    
    def insert(self = None, pos = None, value = None):
        _immutable_error(self)

    
    def pop(self = None, index = None):
        _immutable_error(self)

    
    def reverse(self = None):
        _immutable_error(self)

    
    def sort(self = None, key = None, reverse = None):
        _immutable_error(self)



def ImmutableDictMixin():
    '''ImmutableDictMixin'''
    pass
# WARNING: Decompyle incomplete

ImmutableDictMixin = <NODE:27>(ImmutableDictMixin, 'ImmutableDictMixin', t.Generic[(K, V)])

def ImmutableMultiDictMixin():
    '''ImmutableMultiDictMixin'''
    __doc__ = 'Makes a :class:`MultiDict` immutable.\n\n    .. versionadded:: 0.5\n\n    :private:\n    '
    
    def __reduce_ex__(self = None, protocol = None):
        return (type(self), (list(self.items(multi = True)),))

    
    def _iter_hashitems(self = None):
        return self.items(multi = True)

    
    def add(self = None, key = None, value = None):
        _immutable_error(self)

    
    def popitemlist(self = None):
        _immutable_error(self)

    
    def poplist(self = None, key = None):
        _immutable_error(self)

    
    def setlist(self = None, key = None, new_list = None):
        _immutable_error(self)

    
    def setlistdefault(self = None, key = None, default_list = None):
        _immutable_error(self)


ImmutableMultiDictMixin = <NODE:27>(ImmutableMultiDictMixin, 'ImmutableMultiDictMixin', ImmutableDictMixin[(K, V)])

class ImmutableHeadersMixin:
    '''Makes a :class:`Headers` immutable.  We do not mark them as
    hashable though since the only usecase for this datastructure
    in Werkzeug is a view on a mutable structure.

    .. versionchanged:: 3.1
        Disallow ``|=`` operator.

    .. versionadded:: 0.5

    :private:
    '''
    
    def __delitem__(self = None, key = None, **kwargs):
        _immutable_error(self)

    
    def __setitem__(self = None, key = None, value = None):
        _immutable_error(self)

    
    def set(self = None, key = None, value = None, **kwargs):
        _immutable_error(self)

    
    def setlist(self = None, key = None, values = None):
        _immutable_error(self)

    
    def add(self = None, key = None, value = None, **kwargs):
        _immutable_error(self)

    
    def add_header(self = None, key = None, value = None, **kwargs):
        _immutable_error(self)

    
    def remove(self = None, key = None):
        _immutable_error(self)

    
    def extend(self = None, arg = None, **kwargs):
        _immutable_error(self)

    
    def update(self = None, arg = None, **kwargs):
        _immutable_error(self)

    
    def __ior__(self = None, other = None):
        _immutable_error(self)

    
    def insert(self = None, pos = None, value = None):
        _immutable_error(self)

    
    def pop(self = None, key = None, default = None):
        _immutable_error(self)

    
    def popitem(self = None):
        _immutable_error(self)

    
    def setdefault(self = None, key = None, default = None):
        _immutable_error(self)

    
    def setlistdefault(self = None, key = None, default = None):
        _immutable_error(self)



def _always_update(f = None):
    pass
# WARNING: Decompyle incomplete


def UpdateDictMixin():
    '''UpdateDictMixin'''
    pass
# WARNING: Decompyle incomplete

UpdateDictMixin = <NODE:27>(UpdateDictMixin, 'UpdateDictMixin', dict[(K, V)])
