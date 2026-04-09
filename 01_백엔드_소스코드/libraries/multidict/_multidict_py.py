# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _multidict_py.pyc (Python 3.11)

import enum
import functools
import reprlib
import sys
from array import array
from collections.abc import ItemsView, Iterable, Iterator, KeysView, Mapping, ValuesView
from dataclasses import dataclass
from typing import TYPE_CHECKING, Any, ClassVar, Generic, NoReturn, Optional, TypeVar, Union, cast, overload
from _abc import MDArg, MultiMapping, MutableMultiMapping, SupportsKeys
if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

class istr(str):
    '''Case insensitive str.'''
    __is_istr__ = True
    __istr_identity__: Optional[str] = None

_V = TypeVar('_V')
_T = TypeVar('_T')
_SENTINEL = enum.Enum('_SENTINEL', 'sentinel')
sentinel = _SENTINEL.sentinel
_version = array('Q', [
    0])

def _Iter():
    '''_Iter'''
    __slots__ = ('_size', '_iter')
    
    def __init__(self = None, size = None, iterator = None):
        self._size = size
        self._iter = iterator

    
    def __iter__(self = None):
        return self

    
    def __next__(self = None):
        return next(self._iter)

    
    def __length_hint__(self = None):
        return self._size


_Iter = <NODE:27>(_Iter, '_Iter', Generic[_T])

def _ViewBase():
    '''_ViewBase'''
    
    def __init__(self = None, md = None):
        self._md = md

    
    def __len__(self = None):
        return len(self._md)


_ViewBase = <NODE:27>(_ViewBase, '_ViewBase', Generic[_V])

def _ItemsView():
    '''_ItemsView'''
    
    def __contains__(self = None, item = None):
        if isinstance(item, (tuple, list)) or len(item) != 2:
            return False
        (key, value) = None
        
        try:
            identity = self._md._identity(key)
        except TypeError:
            return False

        hash_ = hash(identity)
        for slot, idx, e in self._md._keys.iter_hash(hash_):
            if e.identity == identity and value == e.value:
                return True
            return False

    
    def __iter__(self = None):
        return _Iter(len(self), self._iter(self._md._version))

    
    def _iter(self = None, version = None):
        pass
    # WARNING: Decompyle incomplete

    __repr__ = (lambda self = None: lst = []for e in self._md._keys.iter_entries():
lst.append(f'''\'{e.key}\': {e.value!r}''')body = ', '.join(lst)f'''<{self.__class__.__name__}({body})>''')()
    
    def _parse_item(self = None, arg = None):
        if not isinstance(arg, tuple):
            return None
        if None(arg) != 2:
            return None
        
        try:
            identity = self._md._identity(arg[0])
            return (hash(identity), identity, arg[0], arg[1])
        except TypeError:
            return None


    
    def _tmp_set(self = None, it = None):
        tmp = set()
    # WARNING: Decompyle incomplete

    
    def __and__(self = None, other = None):
        ret = set()
        
        try:
            it = iter(other)
        except TypeError:
            return 

    # WARNING: Decompyle incomplete

    
    def __rand__(self = None, other = None):
        ret = set()
        
        try:
            it = iter(other)
        except TypeError:
            return 

    # WARNING: Decompyle incomplete

    
    def __or__(self = None, other = None):
        ret = set(self)
        
        try:
            it = iter(other)
        except TypeError:
            return 

    # WARNING: Decompyle incomplete

    
    def __ror__(self = None, other = None):
        
        try:
            ret = set(other)
        except TypeError:
            return 

        for None in self._md._keys.iter_entries():
            if (e.identity, e.value) not in tmp:
                ret.add((e.key, e.value))
            return ret

    
    def __sub__(self = None, other = None):
        ret = set()
        
        try:
            it = iter(other)
        except TypeError:
            return 

        for None in self._md._keys.iter_entries():
            if (e.identity, e.value) not in tmp:
                ret.add((e.key, e.value))
            return ret

    
    def __rsub__(self = None, other = None):
        ret = set()
        
        try:
            it = iter(other)
        except TypeError:
            return 

    # WARNING: Decompyle incomplete

    
    def __xor__(self = None, other = None):
        
        try:
            rgt = set(other)
        except TypeError:
            return 

        ret |= rgt - self = self - rgt
        return ret

    __rxor__ = __xor__
    
    def isdisjoint(self = None, other = None):
        pass
    # WARNING: Decompyle incomplete


_ItemsView = <NODE:27>(_ItemsView, '_ItemsView', _ViewBase[_V], ItemsView[(str, _V)])

def _ValuesView():
    '''_ValuesView'''
    
    def __contains__(self = None, value = None):
        for e in self._md._keys.iter_entries():
            if e.value == value:
                return True
            return False

    
    def __iter__(self = None):
        return _Iter(len(self), self._iter(self._md._version))

    
    def _iter(self = None, version = None):
        pass
    # WARNING: Decompyle incomplete

    __repr__ = (lambda self = None: lst = []for e in self._md._keys.iter_entries():
lst.append(repr(e.value))body = ', '.join(lst)f'''<{self.__class__.__name__}({body})>''')()

_ValuesView = <NODE:27>(_ValuesView, '_ValuesView', _ViewBase[_V], ValuesView[_V])

def _KeysView():
    '''_KeysView'''
    
    def __contains__(self = None, key = None):
        if not isinstance(key, str):
            return False
        identity = None._md._identity(key)
        hash_ = hash(identity)
        for slot, idx, e in self._md._keys.iter_hash(hash_):
            if e.identity == identity:
                return True
            return False

    
    def __iter__(self = None):
        return _Iter(len(self), self._iter(self._md._version))

    
    def _iter(self = None, version = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        lst = []
        for e in self._md._keys.iter_entries():
            lst.append(f'''\'{e.key}\'''')
        body = ', '.join(lst)
        return f'''<{self.__class__.__name__}({body})>'''

    
    def __and__(self = None, other = None):
        ret = set()
        
        try:
            it = iter(other)
        except TypeError:
            return 

        for self._md._identity(key) in it:
            if not isinstance(key, str):
                continue
            hash_ = hash(identity)
            for slot, idx, e in self._md._keys.iter_hash(hash_):
                if e.identity == identity:
                    ret.add(e.key)
                
                return ret

    
    def __rand__(self = None, other = None):
        ret = set()
        
        try:
            it = iter(other)
        except TypeError:
            return 

        for None in it:
            if not isinstance(key, str):
                continue
            if key in self._md:
                ret.add(key)
            return cast(set[_T], ret)

    
    def __or__(self = None, other = None):
        ret = set(self)
        
        try:
            it = iter(other)
        except TypeError:
            return 

        for None in it:
            if not isinstance(key, str):
                ret.add(key)
                continue
            if key not in self._md:
                ret.add(key)
            return ret

    
    def __ror__(self = None, other = None):
        
        try:
            ret = set(other)
        except TypeError:
            return 

        for None in ret:
            if not isinstance(key, str):
                continue
            identity = self._md._identity(key)
            tmp.add(identity)
            for e in self._md._keys.iter_entries():
                if e.identity not in tmp:
                    ret.add(e.key)
                return ret

    
    def __sub__(self = None, other = None):
        ret = set(self)
        
        try:
            it = iter(other)
        except TypeError:
            return 

        for self._md._identity(key) in it:
            if not isinstance(key, str):
                continue
            hash_ = hash(identity)
            for slot, idx, e in self._md._keys.iter_hash(hash_):
                if e.identity == identity:
                    ret.discard(e.key)
                
                return ret

    
    def __rsub__(self = None, other = None):
        
        try:
            ret = set(other)
        except TypeError:
            return 

        for None in other:
            if not isinstance(key, str):
                continue
            if key in self._md:
                ret.discard(key)
            return ret

    
    def __xor__(self = None, other = None):
        
        try:
            rgt = set(other)
        except TypeError:
            return 

        ret |= rgt - self = self - rgt
        return ret

    __rxor__ = __xor__
    
    def isdisjoint(self = None, other = None):
        for key in other:
            if not isinstance(key, str):
                continue
            if key in self._md:
                return False
            return True


_KeysView = <NODE:27>(_KeysView, '_KeysView', _ViewBase[_V], KeysView[str])

class _CSMixin:
    _ci: ClassVar[bool] = False
    
    def _key(self = None, key = None):
        return key

    
    def _identity(self = None, key = None):
        if isinstance(key, str):
            return key
        raise None('MultiDict keys should be either str or subclasses of str')



class _CIMixin:
    _ci: ClassVar[bool] = True
    
    def _key(self = None, key = None):
        if type(key) is istr:
            return key
        return None(key)

    
    def _identity(self = None, key = None):
        pass
    # WARNING: Decompyle incomplete



def estimate_log2_keysize(n = None):
    return ((n * 3 + 1) // 2 | 7).bit_length()


def _Entry():
    '''_Entry'''
    value: _V = '_Entry'

_Entry = <NODE:27>(_Entry, '_Entry', Generic[_V])()

def _HtKeys():
    '''_HtKeys'''
    LOG_MINSIZE: ClassVar[int] = 3
    MINSIZE: ClassVar[int] = 8
    entries: list[Optional[_Entry[_V]]] = range(3, 10)()
    nslots = (lambda self = None: 1 << self.log2_size)()
    mask = (lambda self = None: self.nslots - 1)()
    if sys.implementation.name != 'pypy':
        
        def __sizeof__(self = None):
            return object.__sizeof__(self) + sys.getsizeof(self.indices) + sys.getsizeof(self.entries)

    new = (lambda cls = None, log2_size = None, entries = classmethod: size = 1 << log2_sizeusable = (size << 1) // 3if log2_size < 10:
indices = cls.PREALLOCATED_INDICES[log2_size].__copy__()elif log2_size < 16:

def <genexpr>(.0):
pass# WARNING: Decompyle incomplete
indices = 'h'(<genexpr>, range(size)())elif log2_size < 32:

def <genexpr>(.0):
pass# WARNING: Decompyle incomplete
indices = 'l'(<genexpr>, range(size)())else:

def <genexpr>(.0):
pass# WARNING: Decompyle incomplete
indices = 'q'(<genexpr>, range(size)())ret = cls(log2_size = log2_size, usable = usable, indices = indices, entries = entries)ret)()
    
    def clone(self = None):
        entries = self.entries()
        return _HtKeys(log2_size = self.log2_size, usable = self.usable, indices = self.indices.__copy__(), entries = entries)

    
    def build_indices(self = None, update = None):
        mask = self.mask
        indices = self.indices
    # WARNING: Decompyle incomplete

    
    def find_empty_slot(self = None, hash_ = None):
        mask = self.mask
        indices = self.indices
        i = hash_ & mask
        perturb = hash_ & sys.maxsize
        ix = indices[i]
    # WARNING: Decompyle incomplete

    
    def iter_hash(self = None, hash_ = None):
        pass
    # WARNING: Decompyle incomplete

    
    def del_idx(self = None, hash_ = None, idx = None):
        mask = self.mask
        indices = self.indices
        i = hash_ & mask
        perturb = hash_ & sys.maxsize
        ix = indices[i]
    # WARNING: Decompyle incomplete

    
    def iter_entries(self = None):
        return filter(None, self.entries)

    
    def restore_hash(self = None, hash_ = None):
        mask = self.mask
        indices = self.indices
        entries = self.entries
        i = hash_ & mask
        perturb = hash_ & sys.maxsize
        ix = indices[i]
    # WARNING: Decompyle incomplete


_HtKeys = <NODE:27>(_HtKeys, '_HtKeys', Generic[_V])()

def MultiDict():
    '''MultiDict'''
    __doc__ = 'Dictionary with the support for duplicate keys.'
    __slots__ = ('_keys', '_used', '_version')
    
    def __init__(self = None, arg = None, **kwargs):
        self._used = 0
        v = _version
        v[0] = None
    # WARNING: Decompyle incomplete

    
    def _from_md(self = None, md = None):
        self._keys = md._keys.clone()
        self._used = md._used

    getall = (lambda self = None, key = None: pass)()
    getall = (lambda self = None, key = None, default = overload: pass)()
    
    def getall(self = None, key = None, default = None):
        '''Return a list of all values matching the key.'''
        identity = self._identity(key)
        hash_ = hash(identity)
        res = []
        restore = []
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                res.append(e.value)
                e.hash = -1
                restore.append(idx)
            if res:
                entries = self._keys.entries
                for idx in restore:
                    entries[idx].hash = hash_
                    return res
                    if res and default is not sentinel:
                        return default
                    raise None('Key not found: %r' % key)

    getone = (lambda self = None, key = None: pass)()
    getone = (lambda self = None, key = None, default = overload: pass)()
    
    def getone(self = None, key = None, default = None):
        '''Get first value matching the key.

        Raises KeyError if the key is not found and no default is provided.
        '''
        identity = self._identity(key)
        hash_ = hash(identity)
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                
                return None, e.value
            if default is not sentinel:
                return default
            raise None('Key not found: %r' % key)

    
    def __getitem__(self = None, key = None):
        return self.getone(key)

    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = overload: pass)()
    
    def get(self = None, key = None, default = None):
        '''Get first value matching the key.

        If the key is not found, returns the default (or None if no default is provided)
        '''
        return self.getone(key, default)

    
    def __iter__(self = None):
        return iter(self.keys())

    
    def __len__(self = None):
        return self._used

    
    def keys(self = None):
        """Return a new view of the dictionary's keys."""
        return _KeysView(self)

    
    def items(self = None):
        """Return a new view of the dictionary's items *(key, value) pairs)."""
        return _ItemsView(self)

    
    def values(self = None):
        """Return a new view of the dictionary's values."""
        return _ValuesView(self)

    
    def __eq__(self = None, other = None):
        if not isinstance(other, Mapping):
            return NotImplemented
        if None(other, MultiDictProxy):
            return self == other._md
        if None(other, MultiDict):
            lft = self._keys
            rht = other._keys
            if self._used != other._used:
                return False
            for e1, e2 in None(lft.iter_entries(), rht.iter_entries()):
                if e1.identity != e2.identity or e1.value != e2.value:
                    return False
                return True
                if self._used != len(other):
                    return False
                for k, v in None.items():
                    nv = other.get(k, sentinel)
                    if v != nv:
                        return False
                    return True

    
    def __contains__(self = None, key = None):
        if not isinstance(key, str):
            return False
        identity = None._identity(key)
        hash_ = hash(identity)
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                return True
            return False

    __repr__ = (lambda self = None: body = (lambda .0: pass# WARNING: Decompyle incomplete
)(self._keys.iter_entries()())
        return f'''<{self.__class__.__name__}({body})>'''
)()
    if sys.implementation.name != 'pypy':
        
        def __sizeof__(self = None):
            return object.__sizeof__(self) + sys.getsizeof(self._keys)

    
    def __reduce__(self = None):
        return (self.__class__, (list(self.items()),))

    
    def add(self = None, key = None, value = None):
        identity = self._identity(key)
        hash_ = hash(identity)
        self._add_with_hash(_Entry(hash_, identity, key, value))
        self._incr_version()

    
    def copy(self = None):
        '''Return a copy of itself.'''
        cls = self.__class__
        return cls(self)

    __copy__ = copy
    
    def extend(self = None, arg = None, **kwargs):
        '''Extend current MultiDict with more values.

        This method must be used instead of update.
        '''
        it = self._parse_args(arg, kwargs)
        newsize = self._used + cast(int, next(it))
        self._resize(estimate_log2_keysize(newsize), False)
        self._extend_items(cast(Iterator[_Entry[_V]], it))

    
    def _parse_args(self = None, arg = None, kwargs = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _extend_items(self = None, items = None):
        for e in items:
            self._add_with_hash(e)
            self._incr_version()
            return None

    
    def clear(self = None):
        '''Remove all items from MultiDict.'''
        self._used = 0
        self._keys = _HtKeys.new(_HtKeys.LOG_MINSIZE, [])
        self._incr_version()

    
    def __setitem__(self = None, key = None, value = None):
        identity = self._identity(key)
        hash_ = hash(identity)
        found = False
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                if not found:
                    e.key = key
                    e.value = value
                    e.hash = -1
                    found = True
                    self._incr_version()
                    continue
                if e.hash != -1:
                    self._del_at(slot, idx)
            if not found:
                self._add_with_hash(_Entry(hash_, identity, key, value))
                return None
            None._keys.restore_hash(hash_)
            return None

    
    def __delitem__(self = None, key = None):
        found = False
        identity = self._identity(key)
        hash_ = hash(identity)
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                self._del_at(slot, idx)
                found = True
            if not found:
                raise KeyError(key)
            self._incr_version()
            return None

    setdefault = (lambda self = None, key = None, default = overload: pass)()
    setdefault = (lambda self = None, key = None, default = overload: pass)()
    
    def setdefault(self = None, key = None, default = None):
        '''Return value for key, set value to default if key is not present.'''
        identity = self._identity(key)
        hash_ = hash(identity)
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                
                return None, e.value
            self.add(key, default)
            return default

    popone = (lambda self = None, key = None: pass)()
    popone = (lambda self = None, key = None, default = overload: pass)()
    
    def popone(self = None, key = None, default = None):
        '''Remove specified key and return the corresponding value.

        If key is not found, d is returned if given, otherwise
        KeyError is raised.

        '''
        identity = self._identity(key)
        hash_ = hash(identity)
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                value = e.value
                self._del_at(slot, idx)
                self._incr_version()
                
                return None, value
            if default is sentinel:
                raise KeyError(key)
            return default

    if not TYPE_CHECKING:
        pop = popone
    popall = (lambda self = None, key = None: pass)()
    popall = (lambda self = None, key = None, default = overload: pass)()
    
    def popall(self = None, key = None, default = None):
        '''Remove all occurrences of key and return the list of corresponding
        values.

        If key is not found, default is returned if given, otherwise
        KeyError is raised.

        '''
        found = False
        identity = self._identity(key)
        hash_ = hash(identity)
        ret = []
        for slot, idx, e in self._keys.iter_hash(hash_):
            if e.identity == identity:
                found = True
                ret.append(e.value)
                self._del_at(slot, idx)
                self._incr_version()
            if not found:
                if default is sentinel:
                    raise KeyError(key)
                return default
            return None

    
    def popitem(self = None):
        '''Remove and return an arbitrary (key, value) pair.'''
        if self._used <= 0:
            raise KeyError('empty multidict')
        pos = len(self._keys.entries) - 1
        entry = self._keys.entries.pop()
    # WARNING: Decompyle incomplete

    
    def update(self = None, arg = None, **kwargs):
        '''Update the dictionary, overwriting existing keys.'''
        it = self._parse_args(arg, kwargs)
        newsize = self._used + cast(int, next(it))
        log2_size = estimate_log2_keysize(newsize)
        if log2_size > 17:
            log2_size = 17
        if log2_size > self._keys.log2_size:
            self._resize(log2_size, False)
        
        try:
            self._update_items(cast(Iterator[_Entry[_V]], it))
            self._post_update()
            return None
        except:
            self._post_update()


    
    def _update_items(self = None, items = None):
        for entry in items:
            found = False
            hash_ = entry.hash
            identity = entry.identity
            for slot, idx, e in self._keys.iter_hash(hash_):
                if e.identity == identity:
                    if not found:
                        found = True
                        e.key = entry.key
                        e.value = entry.value
                        e.hash = -1
                        continue
                    self._del_at_for_upd(e)
                if not found:
                    self._add_with_hash_for_upd(entry)
            return None

    
    def _post_update(self = None):
        keys = self._keys
        indices = keys.indices
        entries = keys.entries
    # WARNING: Decompyle incomplete

    
    def merge(self = None, arg = None, **kwargs):
        '''Merge into the dictionary, adding non-existing keys.'''
        it = self._parse_args(arg, kwargs)
        newsize = self._used + cast(int, next(it))
        log2_size = estimate_log2_keysize(newsize)
        if log2_size > 17:
            log2_size = 17
        if log2_size > self._keys.log2_size:
            self._resize(log2_size, False)
        
        try:
            self._merge_items(cast(Iterator[_Entry[_V]], it))
            self._post_update()
            return None
        except:
            self._post_update()


    
    def _merge_items(self = None, items = None):
        for entry in items:
            hash_ = entry.hash
            identity = entry.identity
            for slot, idx, e in self._keys.iter_hash(hash_):
                if e.identity == identity:
                    pass
                
                self._add_with_hash_for_upd(entry)
                return None

    
    def _incr_version(self = None):
        v = _version
        v[0] = None

    
    def _resize(self = None, log2_newsize = None, update = None):
        oldkeys = self._keys
        newentries = self._used
        newkeys = _HtKeys.new(log2_newsize, entries)
        newkeys.build_indices(update)
        newkeys = newkeys, newkeys.usable -= newentries, .usable

    
    def _add_with_hash(self = None, entry = None):
        if self._keys.usable <= 0:
            self._resize((self._used * 3 | _HtKeys.MINSIZE - 1).bit_length(), False)
        keys = self._keys
        slot = keys.find_empty_slot(entry.hash)
        keys.indices[slot] = len(keys.entries)
        keys.entries.append(entry)
        self._incr_version()

    
    def _add_with_hash_for_upd(self = None, entry = None):
        if self._keys.usable <= 0:
            self._resize((self._used * 3 | _HtKeys.MINSIZE - 1).bit_length(), True)
        keys = self._keys
        slot = keys.find_empty_slot(entry.hash)
        keys.indices[slot] = len(keys.entries)
        entry.hash = -1
        keys.entries.append(entry)
        self._incr_version()

    
    def _del_at(self = None, slot = None, idx = None):
        self._keys.entries[idx] = None
        self._keys.indices[slot] = -2

    
    def _del_at_for_upd(self = None, entry = None):
        entry.key = None
        entry.value = None


MultiDict = <NODE:27>(MultiDict, 'MultiDict', _CSMixin, MutableMultiMapping[_V])

def CIMultiDict():
    '''CIMultiDict'''
    __doc__ = 'Dictionary with the support for duplicate case-insensitive keys.'

CIMultiDict = <NODE:27>(CIMultiDict, 'CIMultiDict', _CIMixin, MultiDict[_V])

def MultiDictProxy():
    '''MultiDictProxy'''
    __doc__ = 'Read-only proxy for MultiDict instance.'
    _md: MultiDict[_V] = ('_md',)
    
    def __init__(self = None, arg = None):
        if not isinstance(arg, (MultiDict, MultiDictProxy)):
            raise TypeError(f'''ctor requires MultiDict or MultiDictProxy instance, not {type(arg)}''')
        if isinstance(arg, MultiDictProxy):
            self._md = arg._md
            return None
        self._md = None

    
    def __reduce__(self = None):
        raise TypeError(f'''can\'t pickle {self.__class__.__name__} objects''')

    getall = (lambda self = None, key = None: pass)()
    getall = (lambda self = None, key = None, default = overload: pass)()
    
    def getall(self = None, key = None, default = None):
        '''Return a list of all values matching the key.'''
        if default is not sentinel:
            return self._md.getall(key, default)
        return None._md.getall(key)

    getone = (lambda self = None, key = None: pass)()
    getone = (lambda self = None, key = None, default = overload: pass)()
    
    def getone(self = None, key = None, default = None):
        '''Get first value matching the key.

        Raises KeyError if the key is not found and no default is provided.
        '''
        if default is not sentinel:
            return self._md.getone(key, default)
        return None._md.getone(key)

    
    def __getitem__(self = None, key = None):
        return self.getone(key)

    get = (lambda self = None, key = None: pass)()
    get = (lambda self = None, key = None, default = overload: pass)()
    
    def get(self = None, key = None, default = None):
        '''Get first value matching the key.

        If the key is not found, returns the default (or None if no default is provided)
        '''
        return self._md.getone(key, default)

    
    def __iter__(self = None):
        return iter(self._md.keys())

    
    def __len__(self = None):
        return len(self._md)

    
    def keys(self = None):
        """Return a new view of the dictionary's keys."""
        return self._md.keys()

    
    def items(self = None):
        """Return a new view of the dictionary's items *(key, value) pairs)."""
        return self._md.items()

    
    def values(self = None):
        """Return a new view of the dictionary's values."""
        return self._md.values()

    
    def __eq__(self = None, other = None):
        return self._md == other

    
    def __contains__(self = None, key = None):
        return key in self._md

    __repr__ = (lambda self = None: body = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.items()())
        return f'''<{self.__class__.__name__}({body})>'''
)()
    
    def copy(self = None):
        '''Return a copy of itself.'''
        return MultiDict(self._md)


MultiDictProxy = <NODE:27>(MultiDictProxy, 'MultiDictProxy', _CSMixin, MultiMapping[_V])

def CIMultiDictProxy():
    '''CIMultiDictProxy'''
    pass
# WARNING: Decompyle incomplete

CIMultiDictProxy = <NODE:27>(CIMultiDictProxy, 'CIMultiDictProxy', _CIMixin, MultiDictProxy[_V])

def getversion(md = None):
    if isinstance(md, MultiDictProxy):
        md = md._md
    elif not isinstance(md, MultiDict):
        raise TypeError('Parameter should be multidict or proxy')
    return md._version
