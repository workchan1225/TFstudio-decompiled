# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sortedset.pyc (Python 3.11)

'''Sorted Set
=============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted set implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedSet`

'''
from itertools import chain
from operator import eq, ne, gt, ge, lt, le
from textwrap import dedent
from sortedlist import SortedList, recursive_repr

try:
    from collections.abc import MutableSet, Sequence, Set
except ImportError:
    from collections import MutableSet, Sequence, Set


class SortedSet(Sequence, MutableSet):
    '''Sorted set is a sorted mutable set.

    Sorted set values are maintained in sorted order. The design of sorted set
    is simple: sorted set uses a set for set-operations and maintains a sorted
    list of values.

    Sorted set values must be hashable and comparable. The hash and total
    ordering of values must not change while they are stored in the sorted set.

    Mutable set methods:

    * :func:`SortedSet.__contains__`
    * :func:`SortedSet.__iter__`
    * :func:`SortedSet.__len__`
    * :func:`SortedSet.add`
    * :func:`SortedSet.discard`

    Sequence methods:

    * :func:`SortedSet.__getitem__`
    * :func:`SortedSet.__delitem__`
    * :func:`SortedSet.__reversed__`

    Methods for removing values:

    * :func:`SortedSet.clear`
    * :func:`SortedSet.pop`
    * :func:`SortedSet.remove`

    Set-operation methods:

    * :func:`SortedSet.difference`
    * :func:`SortedSet.difference_update`
    * :func:`SortedSet.intersection`
    * :func:`SortedSet.intersection_update`
    * :func:`SortedSet.symmetric_difference`
    * :func:`SortedSet.symmetric_difference_update`
    * :func:`SortedSet.union`
    * :func:`SortedSet.update`

    Methods for miscellany:

    * :func:`SortedSet.copy`
    * :func:`SortedSet.count`
    * :func:`SortedSet.__repr__`
    * :func:`SortedSet._check`

    Sorted list methods available:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.index`
    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList._reset`

    Additional sorted list methods available, if key-function used:

    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Sorted set comparisons use subset and superset relations. Two sorted sets
    are equal if and only if every element of each sorted set is contained in
    the other (each is a subset of the other). A sorted set is less than
    another sorted set if and only if the first sorted set is a proper subset
    of the second sorted set (is a subset, but is not equal). A sorted set is
    greater than another sorted set if and only if the first sorted set is a
    proper superset of the second sorted set (is a superset, but is not equal).

    '''
    
    def __init__(self, iterable, key = (None, None)):
        """Initialize sorted set instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted set.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default, none, compares values directly.

        Runtime complexity: `O(n*log(n))`

        >>> ss = SortedSet([3, 1, 2, 5, 4])
        >>> ss
        SortedSet([1, 2, 3, 4, 5])
        >>> from operator import neg
        >>> ss = SortedSet([3, 1, 2, 5, 4], neg)
        >>> ss
        SortedSet([5, 4, 3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        """
        self._key = key
        if not hasattr(self, '_set'):
            self._set = set()
        self._list = SortedList(self._set, key = key)
        _set = self._set
        self.isdisjoint = _set.isdisjoint
        self.issubset = _set.issubset
        self.issuperset = _set.issuperset
        _list = self._list
        self.bisect_left = _list.bisect_left
        self.bisect = _list.bisect
        self.bisect_right = _list.bisect_right
        self.index = _list.index
        self.irange = _list.irange
        self.islice = _list.islice
        self._reset = _list._reset
    # WARNING: Decompyle incomplete

    _fromset = (lambda cls, values, key = (None,): sorted_set = object.__new__(cls)sorted_set._set = valuessorted_set.__init__(key = key)sorted_set)()
    key = (lambda self: self._key)()
    
    def __contains__(self, value):
        '''Return true if `value` is an element of the sorted set.

        ``ss.__contains__(value)`` <==> ``value in ss``

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> 3 in ss
        True

        :param value: search for value in sorted set
        :return: true if `value` in sorted set

        '''
        return value in self._set

    
    def __getitem__(self, index):
        """Lookup value at `index` in sorted set.

        ``ss.__getitem__(index)`` <==> ``ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss[2]
        'c'
        >>> ss[-1]
        'e'
        >>> ss[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
        return self._list[index]

    
    def __delitem__(self, index):
        """Remove value at `index` from sorted set.

        ``ss.__delitem__(index)`` <==> ``del ss[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> del ss[2]
        >>> ss
        SortedSet(['a', 'b', 'd', 'e'])
        >>> del ss[:2]
        >>> ss
        SortedSet(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        """
        _set = self._set
        _list = self._list
        if isinstance(index, slice):
            values = _list[index]
            _set.difference_update(values)
        else:
            value = _list[index]
            _set.remove(value)
        del _list[index]

    
    def __make_cmp(set_op, symbol, doc):
        '''Make comparator method.'''
        pass
    # WARNING: Decompyle incomplete

    __eq__ = __make_cmp(eq, '==', 'equal to')
    __ne__ = __make_cmp(ne, '!=', 'not equal to')
    __lt__ = __make_cmp(lt, '<', 'a proper subset of')
    __gt__ = __make_cmp(gt, '>', 'a proper superset of')
    __le__ = __make_cmp(le, '<=', 'a subset of')
    __ge__ = __make_cmp(ge, '>=', 'a superset of')
    __make_cmp = staticmethod(__make_cmp)
    
    def __len__(self):
        '''Return the size of the sorted set.

        ``ss.__len__()`` <==> ``len(ss)``

        :return: size of sorted set

        '''
        return len(self._set)

    
    def __iter__(self):
        '''Return an iterator over the sorted set.

        ``ss.__iter__()`` <==> ``iter(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        '''
        return iter(self._list)

    
    def __reversed__(self):
        '''Return a reverse iterator over the sorted set.

        ``ss.__reversed__()`` <==> ``reversed(ss)``

        Iterating the sorted set while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        '''
        return reversed(self._list)

    
    def add(self, value):
        '''Add `value` to sorted set.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet()
        >>> ss.add(3)
        >>> ss.add(1)
        >>> ss.add(2)
        >>> ss
        SortedSet([1, 2, 3])

        :param value: value to add to sorted set

        '''
        _set = self._set
        if value not in _set:
            _set.add(value)
            self._list.add(value)
            return None

    _add = add
    
    def clear(self):
        '''Remove all values from sorted set.

        Runtime complexity: `O(n)`

        '''
        self._set.clear()
        self._list.clear()

    
    def copy(self):
        '''Return a shallow copy of the sorted set.

        Runtime complexity: `O(n)`

        :return: new sorted set

        '''
        return self._fromset(set(self._set), key = self._key)

    __copy__ = copy
    
    def count(self, value):
        '''Return number of occurrences of `value` in the sorted set.

        Runtime complexity: `O(1)`

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.count(3)
        1

        :param value: value to count in sorted set
        :return: count

        '''
        return 1 if value in self._set else 0

    
    def discard(self, value):
        '''Remove `value` from sorted set if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.discard(5)
        >>> ss.discard(0)
        >>> ss == set([1, 2, 3, 4])
        True

        :param value: `value` to discard from sorted set

        '''
        _set = self._set
        if value in _set:
            _set.remove(value)
            self._list.remove(value)
            return None

    _discard = discard
    
    def pop(self, index = (-1,)):
        """Remove and return value at `index` in sorted set.

        Raise :exc:`IndexError` if the sorted set is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet('abcde')
        >>> ss.pop()
        'e'
        >>> ss.pop(2)
        'c'
        >>> ss
        SortedSet(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        """
        value = self._list.pop(index)
        self._set.remove(value)
        return value

    
    def remove(self, value):
        '''Remove `value` from sorted set; `value` must be a member.

        If `value` is not a member, raise :exc:`KeyError`.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.remove(5)
        >>> ss == set([1, 2, 3, 4])
        True
        >>> ss.remove(0)
        Traceback (most recent call last):
          ...
        KeyError: 0

        :param value: `value` to remove from sorted set
        :raises KeyError: if `value` is not in sorted set

        '''
        self._set.remove(value)
        self._list.remove(value)

    
    def difference(self, *iterables):
        '''Return the difference of two or more sets as a new sorted set.

        The `difference` method also corresponds to operator ``-``.

        ``ss.__sub__(iterable)`` <==> ``ss - iterable``

        The difference is all values that are in this sorted set but not the
        other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.difference([4, 5, 6, 7])
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: new sorted set

        '''
        pass
    # WARNING: Decompyle incomplete

    __sub__ = difference
    
    def difference_update(self, *iterables):
        '''Remove all values of `iterables` from this sorted set.

        The `difference_update` method also corresponds to operator ``-=``.

        ``ss.__isub__(iterable)`` <==> ``ss -= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3])

        :param iterables: iterable arguments
        :return: itself

        '''
        _set = self._set
        _list = self._list
    # WARNING: Decompyle incomplete

    __isub__ = difference_update
    
    def intersection(self, *iterables):
        '''Return the intersection of two or more sets as a new sorted set.

        The `intersection` method also corresponds to operator ``&``.

        ``ss.__and__(iterable)`` <==> ``ss & iterable``

        The intersection is all values that are in this sorted set and each of
        the other `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.intersection([4, 5, 6, 7])
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: new sorted set

        '''
        pass
    # WARNING: Decompyle incomplete

    __and__ = intersection
    __rand__ = __and__
    
    def intersection_update(self, *iterables):
        '''Update the sorted set with the intersection of `iterables`.

        The `intersection_update` method also corresponds to operator ``&=``.

        ``ss.__iand__(iterable)`` <==> ``ss &= iterable``

        Keep only values found in itself and all `iterables`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.intersection_update([4, 5, 6, 7])
        >>> ss
        SortedSet([4, 5])

        :param iterables: iterable arguments
        :return: itself

        '''
        _set = self._set
        _list = self._list
    # WARNING: Decompyle incomplete

    __iand__ = intersection_update
    
    def symmetric_difference(self, other):
        '''Return the symmetric difference with `other` as a new sorted set.

        The `symmetric_difference` method also corresponds to operator ``^``.

        ``ss.__xor__(other)`` <==> ``ss ^ other``

        The symmetric difference is all values tha are in exactly one of the
        sets.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.symmetric_difference([4, 5, 6, 7])
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: new sorted set

        '''
        diff = self._set.symmetric_difference(other)
        return self._fromset(diff, key = self._key)

    __xor__ = symmetric_difference
    __rxor__ = __xor__
    
    def symmetric_difference_update(self, other):
        '''Update the sorted set with the symmetric difference with `other`.

        The `symmetric_difference_update` method also corresponds to operator
        ``^=``.

        ``ss.__ixor__(other)`` <==> ``ss ^= other``

        Keep only values found in exactly one of itself and `other`.

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.symmetric_difference_update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 6, 7])

        :param other: `other` iterable
        :return: itself

        '''
        _set = self._set
        _list = self._list
        _set.symmetric_difference_update(other)
        _list.clear()
        _list.update(_set)
        return self

    __ixor__ = symmetric_difference_update
    
    def union(self, *iterables):
        '''Return new sorted set with values from itself and all `iterables`.

        The `union` method also corresponds to operator ``|``.

        ``ss.__or__(iterable)`` <==> ``ss | iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> ss.union([4, 5, 6, 7])
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: new sorted set

        '''
        pass
    # WARNING: Decompyle incomplete

    __or__ = union
    __ror__ = __or__
    
    def update(self, *iterables):
        '''Update the sorted set adding values from all `iterables`.

        The `update` method also corresponds to operator ``|=``.

        ``ss.__ior__(iterable)`` <==> ``ss |= iterable``

        >>> ss = SortedSet([1, 2, 3, 4, 5])
        >>> _ = ss.update([4, 5, 6, 7])
        >>> ss
        SortedSet([1, 2, 3, 4, 5, 6, 7])

        :param iterables: iterable arguments
        :return: itself

        '''
        _set = self._set
        _list = self._list
    # WARNING: Decompyle incomplete

    __ior__ = update
    _update = update
    
    def __reduce__(self):
        '''Support for pickle.

        The tricks played with exposing methods in :func:`SortedSet.__init__`
        confuse pickle so customize the reducer.

        '''
        return (type(self), (self._set, self._key))

    __repr__ = (lambda self: _key = self._key# WARNING: Decompyle incomplete
)()
    
    def _check(self):
        '''Check invariants of sorted set.

        Runtime complexity: `O(n)`

        '''
        pass
    # WARNING: Decompyle incomplete
