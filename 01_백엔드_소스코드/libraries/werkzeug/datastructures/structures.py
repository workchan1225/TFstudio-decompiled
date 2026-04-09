# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: structures.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import typing as t
from copy import deepcopy
from  import exceptions
from _internal import _missing
from mixins import ImmutableDictMixin
from mixins import ImmutableListMixin
from mixins import ImmutableMultiDictMixin
from mixins import UpdateDictMixin
if t.TYPE_CHECKING:
    import typing_extensions as te
K = t.TypeVar('K')
V = t.TypeVar('V')
T = t.TypeVar('T')

def iter_multi_items(mapping = None):
    '''Iterates over the items of a mapping yielding keys and values
    without dropping any from more complex structures.
    '''
    pass
# WARNING: Decompyle incomplete


def ImmutableList():
    '''ImmutableList'''
    __doc__ = 'An immutable :class:`list`.\n\n    .. versionadded:: 0.5\n\n    :private:\n    '
    
    def __repr__(self = None):
        return f'''{type(self).__name__}({list.__repr__(self)})'''


ImmutableList = <NODE:27>(ImmutableList, 'ImmutableList', ImmutableListMixin, list[V])

def TypeConversionDict():
    '''TypeConversionDict'''
    __doc__ = 'Works like a regular dict but the :meth:`get` method can perform\n    type conversions.  :class:`MultiDict` and :class:`CombinedMultiDict`\n    are subclasses of this class and provide the same feature.\n\n    .. versionadded:: 0.5\n    '
    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = t.overload: pass)()
    get = (lambda self = None, key = None, default = t.overload: pass)()
    get = (lambda self = None, key = None, type = t.overload: pass)()
    get = (lambda self = None, key = None, default = t.overload, type = ('key', 'str', 'default', 'T', 'type', 'cabc.Callable[[V], T]', 'return', 'T'): pass)()
    
    def get(self = None, key = None, default = None, type = (None, None)):
        """Return the default value if the requested data doesn't exist.
        If `type` is provided and is a callable it should convert the value,
        return it or raise a :exc:`ValueError` if that is not possible.  In
        this case the function will return the default as if the value was not
        found:

        >>> d = TypeConversionDict(foo='42', bar='blub')
        >>> d.get('foo', type=int)
        42
        >>> d.get('bar', -1, type=int)
        -1

        :param key: The key to be looked up.
        :param default: The default value to be returned if the key can't
                        be looked up.  If not further specified `None` is
                        returned.
        :param type: A callable that is used to cast the value in the
                     :class:`MultiDict`.  If a :exc:`ValueError` or a
                     :exc:`TypeError` is raised by this callable the default
                     value is returned.

        .. versionchanged:: 3.0.2
           Returns the default value on :exc:`TypeError`, too.
        """
        
        try:
            rv = self[key]
        except KeyError:
            return 

    # WARNING: Decompyle incomplete


TypeConversionDict = <NODE:27>(TypeConversionDict, 'TypeConversionDict', dict[(K, V)])

def ImmutableTypeConversionDict():
    '''ImmutableTypeConversionDict'''
    __doc__ = 'Works like a :class:`TypeConversionDict` but does not support\n    modifications.\n\n    .. versionadded:: 0.5\n    '
    
    def copy(self = None):
        """Return a shallow mutable copy of this object.  Keep in mind that
        the standard library's :func:`copy` function is a no-op for this class
        like for any other python immutable type (eg: :class:`tuple`).
        """
        return TypeConversionDict(self)

    
    def __copy__(self = None):
        return self


ImmutableTypeConversionDict = <NODE:27>(ImmutableTypeConversionDict, 'ImmutableTypeConversionDict', ImmutableDictMixin[(K, V)], TypeConversionDict[(K, V)])

def MultiDict():
    '''MultiDict'''
    pass
# WARNING: Decompyle incomplete

MultiDict = <NODE:27>(MultiDict, 'MultiDict', TypeConversionDict[(K, V)])

def _omd_bucket():
    '''_omd_bucket'''
    __doc__ = 'Wraps values in the :class:`OrderedMultiDict`.  This makes it\n    possible to keep an order over multiple different keys.  It requires\n    a lot of extra memory and slows down access a lot, but makes it\n    possible to access elements in O(1) and iterate in O(n).\n    '
    __slots__ = ('prev', 'key', 'value', 'next')
    
    def __init__(self = None, omd = None, key = None, value = ('omd', '_OrderedMultiDict[K, V]', 'key', 'K', 'value', 'V', 'return', 'None')):
        self.prev = omd._last_bucket
        self.key = key
        self.value = value
        self.next = None
    # WARNING: Decompyle incomplete

    
    def unlink(self = None, omd = None):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        if omd._first_bucket is self:
            omd._first_bucket = self.next
        if omd._last_bucket is self:
            omd._last_bucket = self.prev
            return None


_omd_bucket = <NODE:27>(_omd_bucket, '_omd_bucket', t.Generic[(K, V)])

def _OrderedMultiDict():
    '''_OrderedMultiDict'''
    pass
# WARNING: Decompyle incomplete

_OrderedMultiDict = <NODE:27>(_OrderedMultiDict, '_OrderedMultiDict', MultiDict[(K, V)])

def CombinedMultiDict():
    '''CombinedMultiDict'''
    pass
# WARNING: Decompyle incomplete

CombinedMultiDict = <NODE:27>(CombinedMultiDict, 'CombinedMultiDict', ImmutableMultiDictMixin[(K, V)], MultiDict[(K, V)])

def ImmutableDict():
    '''ImmutableDict'''
    __doc__ = 'An immutable :class:`dict`.\n\n    .. versionadded:: 0.5\n    '
    
    def __repr__(self = None):
        return f'''{type(self).__name__}({dict.__repr__(self)})'''

    
    def copy(self = None):
        """Return a shallow mutable copy of this object.  Keep in mind that
        the standard library's :func:`copy` function is a no-op for this class
        like for any other python immutable type (eg: :class:`tuple`).
        """
        return dict(self)

    
    def __copy__(self = None):
        return self


ImmutableDict = <NODE:27>(ImmutableDict, 'ImmutableDict', ImmutableDictMixin[(K, V)], dict[(K, V)])

def ImmutableMultiDict():
    '''ImmutableMultiDict'''
    __doc__ = 'An immutable :class:`MultiDict`.\n\n    .. versionadded:: 0.5\n    '
    
    def copy(self = None):
        """Return a shallow mutable copy of this object.  Keep in mind that
        the standard library's :func:`copy` function is a no-op for this class
        like for any other python immutable type (eg: :class:`tuple`).
        """
        return MultiDict(self)

    
    def __copy__(self = None):
        return self


ImmutableMultiDict = <NODE:27>(ImmutableMultiDict, 'ImmutableMultiDict', ImmutableMultiDictMixin[(K, V)], MultiDict[(K, V)])

def _ImmutableOrderedMultiDict():
    '''_ImmutableOrderedMultiDict'''
    pass
# WARNING: Decompyle incomplete

_ImmutableOrderedMultiDict = <NODE:27>(_ImmutableOrderedMultiDict, '_ImmutableOrderedMultiDict', ImmutableMultiDictMixin[(K, V)], _OrderedMultiDict[(K, V)])

def CallbackDict():
    '''CallbackDict'''
    pass
# WARNING: Decompyle incomplete

CallbackDict = <NODE:27>(CallbackDict, 'CallbackDict', UpdateDictMixin[(K, V)], dict[(K, V)])

def HeaderSet():
    '''HeaderSet'''
    __doc__ = "Similar to the :class:`ETags` class this implements a set-like structure.\n    Unlike :class:`ETags` this is case insensitive and used for vary, allow, and\n    content-language headers.\n\n    If not constructed using the :func:`parse_set_header` function the\n    instantiation works like this:\n\n    >>> hs = HeaderSet(['foo', 'bar', 'baz'])\n    >>> hs\n    HeaderSet(['foo', 'bar', 'baz'])\n    "
    
    def __init__(self = None, headers = None, on_update = None):
