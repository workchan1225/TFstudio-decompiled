# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

"""This module implements specialized container datatypes providing
alternatives to Python's general purpose built-in containers, dict,
list, set, and tuple.

* namedtuple   factory function for creating tuple subclasses with named fields
* deque        list-like container with fast appends and pops on either end
* ChainMap     dict-like class for creating a single view of multiple mappings
* Counter      dict subclass for counting hashable objects
* OrderedDict  dict subclass that remembers the order entries were added
* defaultdict  dict subclass that calls a factory function to supply missing values
* UserDict     wrapper around dictionary objects for easier dict subclassing
* UserList     wrapper around list objects for easier list subclassing
* UserString   wrapper around string objects for easier string subclassing

"""
__all__ = [
    'ChainMap',
    'Counter',
    'OrderedDict',
    'UserDict',
    'UserList',
    'UserString',
    'defaultdict',
    'deque',
    'namedtuple']
import _collections_abc
import sys as _sys
from itertools import chain as _chain
from itertools import repeat as _repeat
from itertools import starmap as _starmap
from keyword import iskeyword as _iskeyword
from operator import eq as _eq
from operator import itemgetter as _itemgetter
from reprlib import recursive_repr as _recursive_repr
from _weakref import proxy as _proxy

try:
    from _collections import deque
    _collections_abc.MutableSequence.register(deque)
except ImportError:
    pass


try:
    from _collections import defaultdict
except ImportError:
    pass


class _OrderedDictKeysView(_collections_abc.KeysView):
    
    def __reversed__(self):
        pass
    # WARNING: Decompyle incomplete



class _OrderedDictItemsView(_collections_abc.ItemsView):
    
    def __reversed__(self):
        pass
    # WARNING: Decompyle incomplete



class _OrderedDictValuesView(_collections_abc.ValuesView):
    
    def __reversed__(self):
        pass
    # WARNING: Decompyle incomplete



class _Link(object):
    __slots__ = ('prev', 'next', 'key', '__weakref__')


class OrderedDict(dict):
    '''Dictionary that remembers insertion order'''
    
    def __new__(cls, *args, **kwds):
        '''Create the ordered dict object and set up the underlying structures.'''
        self = dict.__new__(cls)
        self._OrderedDict__hardroot = _Link()
        self._OrderedDict__root = _proxy(self._OrderedDict__hardroot)
        root = _proxy(self._OrderedDict__hardroot)
        root.prev = root
        root.next = root
        self._OrderedDict__map = { }
        return self

    
    def __init__(self, other = ((),), **kwds):
        '''Initialize an ordered dictionary.  The signature is the same as
        regular dictionaries.  Keyword argument order is preserved.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, key, value, dict_setitem, proxy, Link = (dict.__setitem__, _proxy, _Link)):
        '''od.__setitem__(i, y) <==> od[i]=y'''
        if key not in self:
            self._OrderedDict__map[key] = Link()
            link = Link()
            root = self._OrderedDict__root
            last = root.prev
            link.prev, link.next, link.key = last, root, key
            last.next = link
            root.prev = proxy(link)
        dict_setitem(self, key, value)

    
    def __delitem__(self, key, dict_delitem = (dict.__delitem__,)):
        '''od.__delitem__(y) <==> del od[y]'''
        dict_delitem(self, key)
        link = self._OrderedDict__map.pop(key)
        link_prev = link.prev
        link_next = link.next
        link_prev.next = link_next
        link_next.prev = link_prev
        link.prev = None
        link.next = None

    
    def __iter__(self):
        '''od.__iter__() <==> iter(od)'''
        pass
    # WARNING: Decompyle incomplete

    
    def __reversed__(self):
        '''od.__reversed__() <==> reversed(od)'''
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self):
        '''od.clear() -> None.  Remove all items from od.'''
        root = self._OrderedDict__root
        root.prev = root
        root.next = root
        self._OrderedDict__map.clear()
        dict.clear(self)

    
    def popitem(self, last = (True,)):
        '''Remove and return a (key, value) pair from the dictionary.

        Pairs are returned in LIFO order if last is true or FIFO order if false.
        '''
        if not self:
            raise KeyError('dictionary is empty')
        root = self._OrderedDict__root
        if last:
            link = root.prev
            link_prev = link.prev
            link_prev.next = root
            root.prev = link_prev
        else:
            link = root.next
            link_next = link.next
            root.next = link_next
            link_next.prev = root
        key = link.key
        del self._OrderedDict__map[key]
        value = dict.pop(self, key)
        return (key, value)

    
    def move_to_end(self, key, last = (True,)):
        '''Move an existing element to the end (or beginning if last is false).

        Raise KeyError if the element does not exist.
        '''
        link = self._OrderedDict__map[key]
        link_prev = link.prev
        link_next = link.next
        soft_link = link_next.prev
        link_prev.next = link_next
        link_next.prev = link_prev
        root = self._OrderedDict__root
        if last:
            last = root.prev
            link.prev = last
            link.next = root
            root.prev = soft_link
            last.next = link
            return None
        first = None.next
        link.prev = root
        link.next = first
        first.prev = soft_link
        root.next = link

    
    def __sizeof__(self):
        sizeof = _sys.getsizeof
        n = len(self) + 1
        size = sizeof(self.__dict__)
        size += sizeof(self._OrderedDict__map) * 2
        size += sizeof(self._OrderedDict__hardroot) * n
        size += sizeof(self._OrderedDict__root) * n
        return size

    update = _collections_abc.MutableMapping.update
    __update = _collections_abc.MutableMapping.update
    
    def keys(self):
        """D.keys() -> a set-like object providing a view on D's keys"""
        return _OrderedDictKeysView(self)

    
    def items(self):
        """D.items() -> a set-like object providing a view on D's items"""
        return _OrderedDictItemsView(self)

    
    def values(self):
        """D.values() -> an object providing a view on D's values"""
        return _OrderedDictValuesView(self)

    __ne__ = _collections_abc.MutableMapping.__ne__
    __marker = object()
    
    def pop(self, key, default = (__marker,)):
        '''od.pop(k[,d]) -> v, remove specified key and return the corresponding
        value.  If key is not found, d is returned if given, otherwise KeyError
        is raised.

        '''
        marker = self.__marker
        result = dict.pop(self, key, marker)
        if result is not marker:
            link = self._OrderedDict__map.pop(key)
            link_prev = link.prev
            link_next = link.next
            link_prev.next = link_next
            link_next.prev = link_prev
            link.prev = None
            link.next = None
            return result
        if None is marker:
            raise KeyError(key)
        return default

    
    def setdefault(self, key, default = (None,)):
        '''Insert key with a value of default if key is not in the dictionary.

        Return the value for key if key is in the dictionary, else default.
        '''
        if key in self:
            return self[key]
        self[key] = None
        return default

    __repr__ = (lambda self: if not self:
f'''{self.__class__.__name__!s}()'''f'''{None.__class__.__name__!s}({list(self.items())!r})''')()
    
    def __reduce__(self):
        '''Return state information for pickling'''
        state = self.__getstate__()
        if state:
            if isinstance(state, tuple):
                (state, slots) = state
            else:
                slots = { }
            state = state.copy()
            slots = slots.copy()
            for k in vars(OrderedDict()):
                state.pop(k, None)
                slots.pop(k, None)
                if slots:
                    state = (state, slots)
                elif not state:
                    state = None
                    return (self.__class__, (), state, None, iter(self.items()))

    
    def copy(self):
        '''od.copy() -> a shallow copy of od'''
        return self.__class__(self)

    fromkeys = (lambda cls, iterable, value = (None,): self = cls()for key in iterable:
self[key] = valueself)()
    
    def __eq__(self, other):
