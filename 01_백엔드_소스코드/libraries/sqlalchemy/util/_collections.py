# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _collections.pyc (Python 3.11)

'''Collection classes and helpers.'''
from __future__ import annotations
import operator
import threading
import types
import typing
from typing import Any
from typing import Callable
from typing import cast
from typing import Container
from typing import Dict
from typing import FrozenSet
from typing import Generic
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import NoReturn
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import TypeVar
from typing import Union
from typing import ValuesView
import weakref
from _has_cy import HAS_CYEXTENSION
from typing import is_non_string_iterable
from typing import Literal
from typing import Protocol
if not typing.TYPE_CHECKING or HAS_CYEXTENSION:
    from _py_collections import immutabledict
    from _py_collections import IdentitySet
    from _py_collections import ReadOnlyContainer
    from _py_collections import ImmutableDictBase
    from _py_collections import OrderedSet
    from _py_collections import unique_list
else:
    from sqlalchemy.cyextension.immutabledict import ReadOnlyContainer
    from sqlalchemy.cyextension.immutabledict import ImmutableDictBase
    from sqlalchemy.cyextension.immutabledict import immutabledict
    from sqlalchemy.cyextension.collections import IdentitySet
    from sqlalchemy.cyextension.collections import OrderedSet
    from sqlalchemy.cyextension.collections import unique_list
_T = TypeVar('_T', bound = Any)
_KT = TypeVar('_KT', bound = Any)
_VT = TypeVar('_VT', bound = Any)
_T_co = TypeVar('_T_co', covariant = True)
EMPTY_SET: 'FrozenSet[Any]' = frozenset()
NONE_SET: 'FrozenSet[Any]' = frozenset([
    None])

def merge_lists_w_ordering(a = None, b = None):
    '''merge two lists, maintaining ordering as much as possible.

    this is to reconcile vars(cls) with cls.__annotations__.

    Example::

        >>> a = ["__tablename__", "id", "x", "created_at"]
        >>> b = ["id", "name", "data", "y", "created_at"]
        >>> merge_lists_w_ordering(a, b)
        [\'__tablename__\', \'id\', \'name\', \'data\', \'y\', \'x\', \'created_at\']

    This is not necessarily the ordering that things had on the class,
    in this case the class is::

        class User(Base):
            __tablename__ = "users"

            id: Mapped[int] = mapped_column(primary_key=True)
            name: Mapped[str]
            data: Mapped[Optional[str]]
            x = Column(Integer)
            y: Mapped[int]
            created_at: Mapped[datetime.datetime] = mapped_column()

    But things are *mostly* ordered.

    The algorithm could also be done by creating a partial ordering for
    all items in both lists and then using topological_sort(), but that
    is too much overhead.

    Background on how I came up with this is at:
    https://gist.github.com/zzzeek/89de958cf0803d148e74861bd682ebae

    '''
    overlap = set(a).intersection(b)
    result = []
    other = iter(b)
    current = iter(a)
    for element in current:
        if element in overlap:
            overlap.discard(element)
            current = other
            other = current
        else:
            result.append(element)
        result.extend(other)
    continue
    return result


def coerce_to_immutabledict(d = None):
    if not d:
        return EMPTY_DICT
    if None(d, immutabledict):
        return d
    return None(d)

EMPTY_DICT: 'immutabledict[Any, Any]' = immutabledict()

def FacadeDict():
    '''FacadeDict'''
    __doc__ = 'A dictionary that is not publicly mutable.'
    
    def __new__(cls = None, *args):
        new = ImmutableDictBase.__new__(cls)
        return new

    
    def copy(self = None):
        raise NotImplementedError("an immutabledict shouldn't need to be copied.  use dict(d) if you need a mutable dictionary.")

    
    def __reduce__(self = None):
        return (FacadeDict, (dict(self),))

    
    def _insert_item(self = None, key = None, value = None):
        '''insert an item into the dictionary directly.'''
        dict.__setitem__(self, key, value)

    
    def __repr__(self = None):
        return 'FacadeDict(%s)' % dict.__repr__(self)


FacadeDict = <NODE:27>(FacadeDict, 'FacadeDict', ImmutableDictBase[(_KT, _VT)])
_DT = TypeVar('_DT', bound = Any)
_F = TypeVar('_F', bound = Any)

def Properties():
    '''Properties'''
    pass
# WARNING: Decompyle incomplete

Properties = <NODE:27>(Properties, 'Properties', Generic[_T])

def OrderedProperties():
    '''OrderedProperties'''
    __doc__ = 'Provide a __getattr__/__setattr__ interface with an OrderedDict\n    as backing store.'
    __slots__ = ()
    
    def __init__(self):
        Properties.__init__(self, OrderedDict())


OrderedProperties = <NODE:27>(OrderedProperties, 'OrderedProperties', Properties[_T])

def ReadOnlyProperties():
    '''ReadOnlyProperties'''
    __doc__ = 'Provide immutable dict/object attribute to an underlying dictionary.'
    __slots__ = ()

ReadOnlyProperties = <NODE:27>(ReadOnlyProperties, 'ReadOnlyProperties', ReadOnlyContainer, Properties[_T])

def _ordered_dictionary_sort(d, key = (None,)):
    '''Sort an OrderedDict in-place.'''
    pass
# WARNING: Decompyle incomplete

OrderedDict = dict
sort_dictionary = _ordered_dictionary_sort

def WeakSequence():
    '''WeakSequence'''
    
    def __init__(self = None, _WeakSequence__elements = None):
        pass
    # WARNING: Decompyle incomplete

    
    def append(self, item):
        self._storage.append(weakref.ref(item, self._remove))

    
    def __len__(self):
        return len(self._storage)

    
    def __iter__(self):
        return self._storage()()

    
    def __getitem__(self, index):
        
        try:
            obj = self._storage[index]
            return obj()
        except KeyError:
            raise IndexError('Index %s out of range' % index)



WeakSequence = <NODE:27>(WeakSequence, 'WeakSequence', Sequence[_T])

class OrderedIdentitySet(IdentitySet):
    
    def __init__(self = None, iterable = None):
        IdentitySet.__init__(self)
        self._members = OrderedDict()
        if iterable:
            for o in iterable:
                self.add(o)
                return None
                return None



def PopulateDict():
    '''PopulateDict'''
    __doc__ = 'A dict which populates missing values via a creation function.\n\n    Note the creation function takes a key, unlike\n    collections.defaultdict.\n\n    '
    
    def __init__(self = None, creator = None):
        self.creator = creator

    
    def __missing__(self = None, key = None):
        self[key] = self.creator(key)
        val = self.creator(key)
        return val


PopulateDict = <NODE:27>(PopulateDict, 'PopulateDict', Dict[(_KT, _VT)])

def WeakPopulateDict():
    '''WeakPopulateDict'''
    __doc__ = 'Like PopulateDict, but assumes a self + a method and does not create\n    a reference cycle.\n\n    '
    
    def __init__(self = None, creator_method = None):
        self.creator = creator_method.__func__
        weakself = creator_method.__self__
        self.weakself = weakref.ref(weakself)

    
    def __missing__(self = None, key = None):
        self[key] = self.creator(self.weakself(), key)
        val = self.creator(self.weakself(), key)
        return val


WeakPopulateDict = <NODE:27>(WeakPopulateDict, 'WeakPopulateDict', Dict[(_KT, _VT)])
column_set = set
column_dict = dict
ordered_column_set = OrderedSet

def UniqueAppender():
    '''UniqueAppender'''
    __doc__ = 'Appends items to a collection ensuring uniqueness.\n\n    Additional appends() of the same object are ignored.  Membership is\n    determined by identity (``is a``) not equality (``==``).\n    '
    _unique: 'Dict[int, Literal[True]]' = ('data', '_data_appender', '_unique')
    
    def __init__(self = None, data = None, via = None):
        self.data = data
        self._unique = { }
        if via:
            self._data_appender = getattr(data, via)
            return None
        if None(data, 'append'):
            self._data_appender = cast('List[_T]', data).append
            return None
        if None(data, 'add'):
            self._data_appender = cast('Set[_T]', data).add
            return None

    
    def append(self = None, item = None):
        id_ = id(item)
        if id_ not in self._unique:
            self._data_appender(item)
            self._unique[id_] = True
            return None

    
    def __iter__(self = None):
        return iter(self.data)


UniqueAppender = <NODE:27>(UniqueAppender, 'UniqueAppender', Generic[_T])

def coerce_generator_arg(arg = None):
    if len(arg) == 1 and isinstance(arg[0], types.GeneratorType):
        return list(arg[0])
    return None('List[Any]', arg)


def to_list(x = None, default = None):
    pass
# WARNING: Decompyle incomplete


def has_intersection(set_ = None, iterable = None):
    """return True if any items of set\\_ are present in iterable.

    Goes through special effort to ensure __hash__ is not called
    on items in iterable that don't support it.

    """
    pass
# WARNING: Decompyle incomplete


def to_set(x):
    pass
# WARNING: Decompyle incomplete


def to_column_set(x = None):
    pass
# WARNING: Decompyle incomplete


def update_copy(d = None, _new = None, **kw):
    '''Copy the given dict and update with the given values.'''
    d = d.copy()
    if _new:
        d.update(_new)
# WARNING: Decompyle incomplete


def flatten_iterator(x = None):
    '''Given an iterator of which further sub-elements may also be
    iterators, flatten the sub-elements into a single iterator.

    '''
    pass
# WARNING: Decompyle incomplete


def LRUCache():
    '''LRUCache'''
    __doc__ = 'Dictionary with \'squishy\' removal of least\n    recently used items.\n\n    Note that either get() or [] should be used here, but\n    generally its not safe to do an "in" check first as the dictionary\n    can change subsequent to that call.\n\n    '
    size_alert: 'Optional[Callable[[LRUCache[_KT, _VT]], None]]' = ('capacity', 'threshold', 'size_alert', '_data', '_counter', '_mutex')
    
    def __init__(self = None, capacity = None, threshold = None, size_alert = (100, 0.5, None)):
        self.capacity = capacity
        self.threshold = threshold
        self.size_alert = size_alert
        self._counter = 0
        self._mutex = threading.Lock()
        self._data = { }

    
    def _inc_counter(self):
        return self._counter

    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = overload: pass)()
    
    def get(self = None, key = None, default = None):
        item = self._data.get(key)
    # WARNING: Decompyle incomplete

    
    def __getitem__(self = None, key = None):
        item = self._data[key]
        item[2][0] = self._inc_counter()
        return item[1]

    
    def __iter__(self = None):
        return iter(self._data)

    
    def __len__(self = None):
        return len(self._data)

    
    def values(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self._data.items()())

    
    def __setitem__(self = None, key = None, value = None):
        self._data[key] = (key, value, [
            self._inc_counter()])
        self._manage_size()

    
    def __delitem__(self = None, _LRUCache__v = None):
        del self._data[_LRUCache__v]

    size_threshold = (lambda self = None: self.capacity + self.capacity * self.threshold)()
    
    def _manage_size(self = None):
        if not self._mutex.acquire(False):
            return None
    # WARNING: Decompyle incomplete


LRUCache = <NODE:27>(LRUCache, 'LRUCache', typing.MutableMapping[(_KT, _VT)])

def _CreateFuncType():
    '''_CreateFuncType'''
    
    def __call__(self = None):
        pass


_CreateFuncType = <NODE:27>(_CreateFuncType, '_CreateFuncType', Protocol[_T_co])

class _ScopeFuncType(Protocol):
    
    def __call__(self = None):
        pass



def ScopedRegistry():
    '''ScopedRegistry'''
    __doc__ = 'A Registry that can store one or multiple instances of a single\n    class on the basis of a "scope" function.\n\n    The object implements ``__call__`` as the "getter", so by\n    calling ``myregistry()`` the contained object is returned\n    for the current scope.\n\n    :param createfunc:\n      a callable that returns a new object to be placed in the registry\n\n    :param scopefunc:\n      a callable that will return a key to store/retrieve an object.\n    '
    registry: 'Any' = ('createfunc', 'scopefunc', 'registry')
    
    def __init__(self = None, createfunc = None, scopefunc = None):
        '''Construct a new :class:`.ScopedRegistry`.

        :param createfunc:  A creation function that will generate
          a new value for the current scope, if none is present.

        :param scopefunc:  A function that returns a hashable
          token representing the current scope (such as, current
          thread identifier).

        '''
        self.createfunc = createfunc
        self.scopefunc = scopefunc
        self.registry = { }

    
    def __call__(self = None):
        key = self.scopefunc()
        
        try:
            return self.registry[key]
        except KeyError:
            return 


    
    def has(self = None):
        '''Return True if an object is present in the current scope.'''
        return self.scopefunc() in self.registry

    
    def set(self = None, obj = None):
        '''Set the value for the current scope.'''
        self.registry[self.scopefunc()] = obj

    
    def clear(self = None):
        '''Clear the current scope, if any.'''
        
        try:
            del self.registry[self.scopefunc()]
            return None
        except KeyError:
            return None



ScopedRegistry = <NODE:27>(ScopedRegistry, 'ScopedRegistry', Generic[_T])

def ThreadLocalRegistry():
    '''ThreadLocalRegistry'''
    __doc__ = 'A :class:`.ScopedRegistry` that uses a ``threading.local()``\n    variable for storage.\n\n    '
    
    def __init__(self = None, createfunc = None):
        self.createfunc = createfunc
        self.registry = threading.local()

    
    def __call__(self = None):
        
        try:
            return self.registry.value
        except AttributeError:
            val = self.createfunc()
            self.registry.value = self.createfunc()
            return 


    
    def has(self = None):
        return hasattr(self.registry, 'value')

    
    def set(self = None, obj = None):
        self.registry.value = obj

    
    def clear(self = None):
        
        try:
            del self.registry.value
            return None
        except AttributeError:
            return None



ThreadLocalRegistry = <NODE:27>(ThreadLocalRegistry, 'ThreadLocalRegistry', ScopedRegistry[_T])

def has_dupes(sequence, target):
