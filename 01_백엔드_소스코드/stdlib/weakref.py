# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: weakref.pyc (Python 3.11)

'''Weak reference support for Python.

This module is an implementation of PEP 205:

https://peps.python.org/pep-0205/
'''
from _weakref import getweakrefcount, getweakrefs, ref, proxy, CallableProxyType, ProxyType, ReferenceType, _remove_dead_weakref
from _weakrefset import WeakSet, _IterationGuard
import _collections_abc
import sys
import itertools
ProxyTypes = (ProxyType, CallableProxyType)
__all__ = [
    'ref',
    'proxy',
    'getweakrefcount',
    'getweakrefs',
    'WeakKeyDictionary',
    'ReferenceType',
    'ProxyType',
    'CallableProxyType',
    'ProxyTypes',
    'WeakValueDictionary',
    'WeakSet',
    'WeakMethod',
    'finalize']
_collections_abc.MutableSet.register(WeakSet)

class WeakMethod(ref):
    pass
# WARNING: Decompyle incomplete


class WeakValueDictionary(_collections_abc.MutableMapping):
    '''Mapping class that references values weakly.

    Entries in the dictionary will be discarded when no strong
    reference to the value exists anymore
    '''
    
    def __init__(self, other = ((),), **kw):
        
        def remove(wr, selfref, _atomic_removal = (ref(self), _remove_dead_weakref)):
            self = selfref()
        # WARNING: Decompyle incomplete

        self._remove = remove
        self._pending_removals = []
        self._iterating = set()
        self.data = { }
    # WARNING: Decompyle incomplete

    
    def _commit_removals(self, _atomic_removal = (_remove_dead_weakref,)):
        pop = self._pending_removals.pop
        d = self.data
        
        try:
            key = pop()
        except IndexError:
            return None

        _atomic_removal(d, key)
        continue

    
    def __getitem__(self, key):
        if self._pending_removals:
            self._commit_removals()
        o = self.data[key]()
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        if self._pending_removals:
            self._commit_removals()
        del self.data[key]

    
    def __len__(self):
        if self._pending_removals:
            self._commit_removals()
        return len(self.data)

    
    def __contains__(self, key):
        if self._pending_removals:
            self._commit_removals()
        
        try:
            o = self.data[key]()
        except KeyError:
            return False

        return o is not None

    
    def __repr__(self):
        return '<%s at %#x>' % (self.__class__.__name__, id(self))

    
    def __setitem__(self, key, value):
        if self._pending_removals:
            self._commit_removals()
        self.data[key] = KeyedRef(value, self._remove, key)

    
    def copy(self):
        if self._pending_removals:
            self._commit_removals()
        new = WeakValueDictionary()
        _IterationGuard(self)
    # WARNING: Decompyle incomplete

    __copy__ = copy
    
    def __deepcopy__(self, memo):
        deepcopy = deepcopy
        import copy
        if self._pending_removals:
            self._commit_removals()
        new = self.__class__()
        _IterationGuard(self)
    # WARNING: Decompyle incomplete

    
    def get(self, key, default = (None,)):
        if self._pending_removals:
            self._commit_removals()
    # WARNING: Decompyle incomplete

    
    def items(self):
        pass
    # WARNING: Decompyle incomplete

    
    def keys(self):
        pass
    # WARNING: Decompyle incomplete

    __iter__ = keys
    
    def itervaluerefs(self):
        """Return an iterator that yields the weak references to the values.

        The references are not guaranteed to be 'live' at the time
        they are used, so the result of calling the references needs
        to be checked before being used.  This can be used to avoid
        creating references that will cause the garbage collector to
        keep the values around longer than needed.

        """
        pass
    # WARNING: Decompyle incomplete

    
    def values(self):
        pass
    # WARNING: Decompyle incomplete

    
    def popitem(self):
        if self._pending_removals:
            self._commit_removals()
        (key, wr) = self.data.popitem()
        o = wr()
    # WARNING: Decompyle incomplete

    
    def pop(self, key, *args):
        if self._pending_removals:
            self._commit_removals()
        
        try:
            o = self.data.pop(key)()
        except KeyError:
            o = None

    # WARNING: Decompyle incomplete

    
    def setdefault(self, key, default = (None,)):
        
        try:
            o = self.data[key]()
        except KeyError:
            o = None

    # WARNING: Decompyle incomplete

    
    def update(self, other = (None,), **kwargs):
        if self._pending_removals:
            self._commit_removals()
        d = self.data
    # WARNING: Decompyle incomplete

    
    def valuerefs(self):
        """Return a list of weak references to the values.

        The references are not guaranteed to be 'live' at the time
        they are used, so the result of calling the references needs
        to be checked before being used.  This can be used to avoid
        creating references that will cause the garbage collector to
        keep the values around longer than needed.

        """
        if self._pending_removals:
            self._commit_removals()
        return list(self.data.values())

    
    def __ior__(self, other):
        self.update(other)
        return self

    
    def __or__(self, other):
        if isinstance(other, _collections_abc.Mapping):
            c = self.copy()
            c.update(other)
            return c

    
    def __ror__(self, other):
        if isinstance(other, _collections_abc.Mapping):
            c = self.__class__()
            c.update(other)
            c.update(self)
            return c



class KeyedRef(ref):
    pass
# WARNING: Decompyle incomplete


class WeakKeyDictionary(_collections_abc.MutableMapping):
    ''' Mapping class that references keys weakly.

    Entries in the dictionary will be discarded when there is no
    longer a strong reference to the key. This can be used to
    associate additional data with an object owned by other parts of
    an application without adding attributes to those objects. This
    can be especially useful with objects that override attribute
    accesses.
    '''
    
    def __init__(self, dict = (None,)):
        self.data = { }
        
        def remove(k, selfref = (ref(self),)):
            self = selfref()
        # WARNING: Decompyle incomplete

        self._remove = remove
        self._pending_removals = []
        self._iterating = set()
        self._dirty_len = False
    # WARNING: Decompyle incomplete

    
    def _commit_removals(self):
        pop = self._pending_removals.pop
        d = self.data
        
        try:
            key = pop()
        except IndexError:
            return None

        
        try:
            del d[key]
        except KeyError:
            pass

        continue

    
    def _scrub_removals(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __delitem__(self, key):
        self._dirty_len = True
        del self.data[ref(key)]

    
    def __getitem__(self, key):
        return self.data[ref(key)]

    
    def __len__(self):
        if self._dirty_len and self._pending_removals:
            self._scrub_removals()
        return len(self.data) - len(self._pending_removals)

    
    def __repr__(self):
        return '<%s at %#x>' % (self.__class__.__name__, id(self))

    
    def __setitem__(self, key, value):
        self.data[ref(key, self._remove)] = value

    
    def copy(self):
        new = WeakKeyDictionary()
        _IterationGuard(self)
    # WARNING: Decompyle incomplete

    __copy__ = copy
    
    def __deepcopy__(self, memo):
        deepcopy = deepcopy
        import copy
        new = self.__class__()
        _IterationGuard(self)
    # WARNING: Decompyle incomplete

    
    def get(self, key, default = (None,)):
        return self.data.get(ref(key), default)

    
    def __contains__(self, key):
        
        try:
            wr = ref(key)
        except TypeError:
            return False

        return wr in self.data

    
    def items(self):
        pass
    # WARNING: Decompyle incomplete

    
    def keys(self):
        pass
    # WARNING: Decompyle incomplete

    __iter__ = keys
    
    def values(self):
        pass
    # WARNING: Decompyle incomplete

    
    def keyrefs(self):
        """Return a list of weak references to the keys.

        The references are not guaranteed to be 'live' at the time
        they are used, so the result of calling the references needs
        to be checked before being used.  This can be used to avoid
        creating references that will cause the garbage collector to
        keep the keys around longer than needed.

        """
        return list(self.data)

    
    def popitem(self):
        self._dirty_len = True
        (key, value) = self.data.popitem()
        o = key()
    # WARNING: Decompyle incomplete

    
    def pop(self, key, *args):
        self._dirty_len = True
    # WARNING: Decompyle incomplete

    
    def setdefault(self, key, default = (None,)):
        return self.data.setdefault(ref(key, self._remove), default)

    
    def update(self, dict = (None,), **kwargs):
        d = self.data
    # WARNING: Decompyle incomplete

    
    def __ior__(self, other):
        self.update(other)
        return self

    
    def __or__(self, other):
        if isinstance(other, _collections_abc.Mapping):
            c = self.copy()
            c.update(other)
            return c

    
    def __ror__(self, other):
        if isinstance(other, _collections_abc.Mapping):
            c = self.__class__()
            c.update(other)
            c.update(self)
            return c



class finalize:
    '''Class for finalization of weakrefable objects

    finalize(obj, func, *args, **kwargs) returns a callable finalizer
    object which will be called when obj is garbage collected. The
    first time the finalizer is called it evaluates func(*arg, **kwargs)
    and returns the result. After this the finalizer is dead, and
    calling it just returns None.

    When the program exits any remaining finalizers for which the
    atexit attribute is true will be run in reverse order of creation.
    By default atexit is true.
    '''
    __slots__ = ()
    _registry = { }
    _shutdown = False
    _index_iter = itertools.count()
    _dirty = False
    _registered_with_atexit = False
    
    class _Info:
        __slots__ = ('weakref', 'func', 'args', 'kwargs', 'atexit', 'index')

    
    def __init__(self, obj, func, *args, **kwargs):
