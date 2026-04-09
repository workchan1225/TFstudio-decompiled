# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _weakrefset.pyc (Python 3.11)

from _weakref import ref
from types import GenericAlias
__all__ = [
    'WeakSet']

class _IterationGuard:
    
    def __init__(self, weakcontainer):
        self.weakcontainer = ref(weakcontainer)

    
    def __enter__(self):
        w = self.weakcontainer()
    # WARNING: Decompyle incomplete

    
    def __exit__(self, e, t, b):
        w = self.weakcontainer()
    # WARNING: Decompyle incomplete



class WeakSet:
    
    def __init__(self, data = (None,)):
        self.data = set()
        
        def _remove(item, selfref = (ref(self),)):
            self = selfref()
        # WARNING: Decompyle incomplete

        self._remove = _remove
        self._pending_removals = []
        self._iterating = set()
    # WARNING: Decompyle incomplete

    
    def _commit_removals(self):
        pop = self._pending_removals.pop
        discard = self.data.discard
        
        try:
            item = pop()
        except IndexError:
            return None

        discard(item)
        continue

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        return len(self.data) - len(self._pending_removals)

    
    def __contains__(self, item):
        
        try:
            wr = ref(item)
        except TypeError:
            return False

        return wr in self.data

    
    def __reduce__(self):
        return (self.__class__, (list(self),), self.__getstate__())

    
    def add(self, item):
        if self._pending_removals:
            self._commit_removals()
        self.data.add(ref(item, self._remove))

    
    def clear(self):
        if self._pending_removals:
            self._commit_removals()
        self.data.clear()

    
    def copy(self):
        return self.__class__(self)

    
    def pop(self):
        if self._pending_removals:
            self._commit_removals()
        
        try:
            itemref = self.data.pop()
        except KeyError:
            raise KeyError('pop from empty WeakSet'), None

        item = itemref()
    # WARNING: Decompyle incomplete

    
    def remove(self, item):
        if self._pending_removals:
            self._commit_removals()
        self.data.remove(ref(item))

    
    def discard(self, item):
        if self._pending_removals:
            self._commit_removals()
        self.data.discard(ref(item))

    
    def update(self, other):
        if self._pending_removals:
            self._commit_removals()
        for element in other:
            self.add(element)
            return None

    
    def __ior__(self, other):
        self.update(other)
        return self

    
    def difference(self, other):
        newset = self.copy()
        newset.difference_update(other)
        return newset

    __sub__ = difference
    
    def difference_update(self, other):
        self.__isub__(other)

    
    def __isub__(self, other):
        if self._pending_removals:
            self._commit_removals()
        return self

    
    def intersection(self, other):
        pass
    # WARNING: Decompyle incomplete

    __and__ = intersection
    
    def intersection_update(self, other):
        self.__iand__(other)

    
    def __iand__(self, other):
        if self._pending_removals:
            self._commit_removals()
        (lambda .0: pass# WARNING: Decompyle incomplete
)(other())
        return self

    
    def issubset(self, other):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(other())

    __le__ = issubset
    
    def __lt__(self, other):
        return self.data < set(map(ref, other))

    
    def issuperset(self, other):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(other())

    __ge__ = issuperset
    
    def __gt__(self, other):
        return self.data > set(map(ref, other))

    
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return None.data == set(map(ref, other))

    
    def symmetric_difference(self, other):
        newset = self.copy()
        newset.symmetric_difference_update(other)
        return newset

    __xor__ = symmetric_difference
    
    def symmetric_difference_update(self, other):
        self.__ixor__(other)

    
    def __ixor__(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def union(self, other):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)((self, other)())

    __or__ = union
    
    def isdisjoint(self, other):
        return len(self.intersection(other)) == 0

    
    def __repr__(self):
        return repr(self.data)

    __class_getitem__ = classmethod(GenericAlias)
