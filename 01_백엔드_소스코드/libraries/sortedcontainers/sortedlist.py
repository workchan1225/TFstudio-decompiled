# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sortedlist.pyc (Python 3.11)

'''Sorted List
==============

:doc:`Sorted Containers<index>` is an Apache2 licensed Python sorted
collections library, written in pure-Python, and fast as C-extensions. The
:doc:`introduction<introduction>` is the best way to get started.

Sorted list implementations:

.. currentmodule:: sortedcontainers

* :class:`SortedList`
* :class:`SortedKeyList`

'''
from __future__ import print_function
import sys
import traceback
from bisect import bisect_left, bisect_right, insort
from itertools import chain, repeat, starmap
from math import log
from operator import add, eq, ne, gt, ge, lt, le, iadd
from textwrap import dedent

try:
    from collections.abc import Sequence, MutableSequence
except ImportError:
    from collections import Sequence, MutableSequence

from functools import wraps
from sys import hexversion
if hexversion < 50331648:
    from itertools import imap as map
    from itertools import izip as zip
    
    try:
        from thread import get_ident
    except ImportError:
        from dummy_thread import get_ident
    except:
        from functools import reduce
        
        try:
            from _thread import get_ident
        except ImportError:
            from _dummy_thread import get_ident

        
        def recursive_repr(fillvalue = ('...',)):
            '''Decorator to make a repr function return fillvalue for a recursive call.'''
            pass
        # WARNING: Decompyle incomplete

        
        class SortedList(MutableSequence):
            '''Sorted list is a sorted mutable sequence.

    Sorted list values are maintained in sorted order.

    Sorted list values must be comparable. The total ordering of values must
    not change while they are stored in the sorted list.

    Methods for adding values:

    * :func:`SortedList.add`
    * :func:`SortedList.update`
    * :func:`SortedList.__add__`
    * :func:`SortedList.__iadd__`
    * :func:`SortedList.__mul__`
    * :func:`SortedList.__imul__`

    Methods for removing values:

    * :func:`SortedList.clear`
    * :func:`SortedList.discard`
    * :func:`SortedList.remove`
    * :func:`SortedList.pop`
    * :func:`SortedList.__delitem__`

    Methods for looking up values:

    * :func:`SortedList.bisect_left`
    * :func:`SortedList.bisect_right`
    * :func:`SortedList.count`
    * :func:`SortedList.index`
    * :func:`SortedList.__contains__`
    * :func:`SortedList.__getitem__`

    Methods for iterating values:

    * :func:`SortedList.irange`
    * :func:`SortedList.islice`
    * :func:`SortedList.__iter__`
    * :func:`SortedList.__reversed__`

    Methods for miscellany:

    * :func:`SortedList.copy`
    * :func:`SortedList.__len__`
    * :func:`SortedList.__repr__`
    * :func:`SortedList._check`
    * :func:`SortedList._reset`

    Sorted lists use lexicographical ordering semantics when compared to other
    sequences.

    Some methods of mutable sequences are not supported and will raise
    not-implemented error.

    '''
            DEFAULT_LOAD_FACTOR = 1000
            
            def __init__(self, iterable, key = (None, None)):
                '''Initialize sorted list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted list.

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList()
        >>> sl
        SortedList([])
        >>> sl = SortedList([3, 1, 2, 5, 4])
        >>> sl
        SortedList([1, 2, 3, 4, 5])

        :param iterable: initial values (optional)

        '''
                pass
            # WARNING: Decompyle incomplete

            
            def __new__(cls, iterable, key = (None, None)):
                '''Create new sorted list or sorted-key list instance.

        Optional `key`-function argument will return an instance of subtype
        :class:`SortedKeyList`.

        >>> sl = SortedList()
        >>> isinstance(sl, SortedList)
        True
        >>> sl = SortedList(key=lambda x: -x)
        >>> isinstance(sl, SortedList)
        True
        >>> isinstance(sl, SortedKeyList)
        True

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)
        :return: sorted list or sorted-key list instance

        '''
                pass
            # WARNING: Decompyle incomplete

            key = (lambda self: pass)()
            
            def _reset(self, load):
                """Reset sorted list load factor.

        The `load` specifies the load-factor of the list. The default load
        factor of 1000 works well for lists from tens to tens-of-millions of
        values. Good practice is to use a value that is the cube root of the
        list size. With billions of elements, the best load factor depends on
        your usage. It's best to leave the load factor at the default until you
        start benchmarking.

        See :doc:`implementation` and :doc:`performance-scale` for more
        information.

        Runtime complexity: `O(n)`

        :param int load: load-factor for sorted list sublists

        """
                values = reduce(iadd, self._lists, [])
                self._clear()
                self._load = load
                self._update(values)

            
            def clear(self):
                '''Remove all values from sorted list.

        Runtime complexity: `O(n)`

        '''
                self._len = 0
                del self._lists[:]
                del self._maxes[:]
                del self._index[:]
                self._offset = 0

            _clear = clear
            
            def add(self, value):
                '''Add `value` to sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.add(3)
        >>> sl.add(1)
        >>> sl.add(2)
        >>> sl
        SortedList([1, 2, 3])

        :param value: value to add to sorted list

        '''
                _lists = self._lists
                _maxes = self._maxes
                if _maxes:
                    pos = bisect_right(_maxes, value)
                    if pos == len(_maxes):
                        pos -= 1
                        _lists[pos].append(value)
                        _maxes[pos] = value
                    else:
                        insort(_lists[pos], value)
                    self._expand(pos)
                else:
                    _lists.append([
                        value])
                    _maxes.append(value)

            
            def _expand(self, pos):
                '''Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        '''
                _load = self._load
                _lists = self._lists
                _index = self._index
                if len(_lists[pos]) > _load << 1:
                    _maxes = self._maxes
                    _lists_pos = _lists[pos]
                    half = _lists_pos[_load:]
                    del _lists_pos[_load:]
                    _maxes[pos] = _lists_pos[-1]
                    _lists.insert(pos + 1, half)
                    _maxes.insert(pos + 1, half[-1])
                    del _index[:]
                    return None
            # WARNING: Decompyle incomplete

            
            def update(self, iterable):
                '''Update sorted list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList()
        >>> sl.update([3, 1, 2])
        >>> sl
        SortedList([1, 2, 3])

        :param iterable: iterable of values to add

        '''
                pass
            # WARNING: Decompyle incomplete

            _update = update
            
            def __contains__(self, value):
                '''Return true if `value` is an element of the sorted list.

        ``sl.__contains__(value)`` <==> ``value in sl``

        Runtime complexity: `O(log(n))`

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> 3 in sl
        True

        :param value: search for value in sorted list
        :return: true if `value` in sorted list

        '''
                _maxes = self._maxes
                if not _maxes:
                    return False
                pos = None(_maxes, value)
                if pos == len(_maxes):
                    return False
                _lists = None._lists
                idx = bisect_left(_lists[pos], value)
                return _lists[pos][idx] == value

            
            def discard(self, value):
                '''Remove `value` from sorted list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.discard(5)
        >>> sl.discard(0)
        >>> sl == [1, 2, 3, 4]
        True

        :param value: `value` to discard from sorted list

        '''
                _maxes = self._maxes
                if not _maxes:
                    return None
                pos = None(_maxes, value)
                if pos == len(_maxes):
                    return None
                _lists = None._lists
                idx = bisect_left(_lists[pos], value)
                if _lists[pos][idx] == value:
                    self._delete(pos, idx)
                    return None

            
            def remove(self, value):
                '''Remove `value` from sorted list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 3, 4, 5])
        >>> sl.remove(5)
        >>> sl == [1, 2, 3, 4]
        True
        >>> sl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted list
        :raises ValueError: if `value` is not in sorted list

        '''
                _maxes = self._maxes
                if not _maxes:
                    raise ValueError('{0!r} not in list'.format(value))
                pos = bisect_left(_maxes, value)
                if pos == len(_maxes):
                    raise ValueError('{0!r} not in list'.format(value))
                _lists = self._lists
                idx = bisect_left(_lists[pos], value)
                if _lists[pos][idx] == value:
                    self._delete(pos, idx)
                    return None
                raise None('{0!r} not in list'.format(value))

            
            def _delete(self, pos, idx):
                '''Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        '''
                _lists = self._lists
                _maxes = self._maxes
                _index = self._index
                _lists_pos = _lists[pos]
                del _lists_pos[idx]
                len(_lists_pos) = self, self._len -= 1, ._len
            # WARNING: Decompyle incomplete

            
            def _loc(self, pos, idx):
                '''Convert an index pair (lists index, sublist index) into a single
        index number that corresponds to the position of the value in the
        sorted list.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree from a leaf node to the root. The
        parent of each node is easily computable at ``(pos - 1) // 2``.

        Left-child nodes are always at odd indices and right-child nodes are
        always at even indices.

        When traversing up from a right-child node, increment the total by the
        left-child node.

        The final index is the sum from traversal and the index in the sublist.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Converting an index pair (2, 3) into a single index involves iterating
        like so:

        1. Starting at the leaf node: offset + alpha = 3 + 2 = 5. We identify
           the node as a left-child node. At such nodes, we simply traverse to
           the parent.

        2. At node 9, position 2, we recognize the node as a right-child node
           and accumulate the left-child in our total. Total is now 5 and we
           traverse to the parent at position 0.

        3. Iteration ends at the root.

        The index is then the sum of the total and sublist index: 5 + 3 = 8.

        :param int pos: lists index
        :param int idx: sublist index
        :return: index in sorted list

        '''
                if not pos:
                    return idx
                _index = None._index
                if not _index:
                    self._build_index()
                total = 0
                pos += self._offset
            # WARNING: Decompyle incomplete

            
            def _pos(self, idx):
                '''Convert an index into an index pair (lists index, sublist index)
        that can be used to access the corresponding lists position.

        Many queries require the index be built. Details of the index are
        described in ``SortedList._build_index``.

        Indexing requires traversing the tree to a leaf node. Each node has two
        children which are easily computable. Given an index, pos, the
        left-child is at ``pos * 2 + 1`` and the right-child is at ``pos * 2 +
        2``.

        When the index is less than the left-child, traversal moves to the
        left sub-tree. Otherwise, the index is decremented by the left-child
        and traversal moves to the right sub-tree.

        At a child node, the indexing pair is computed from the relative
        position of the child node as compared with the offset and the remaining
        index.

        For example, using the index from ``SortedList._build_index``::

            _index = 14 5 9 3 2 4 5
            _offset = 3

        Tree::

                 14
              5      9
            3   2  4   5

        Indexing position 8 involves iterating like so:

        1. Starting at the root, position 0, 8 is compared with the left-child
           node (5) which it is greater than. When greater the index is
           decremented and the position is updated to the right child node.

        2. At node 9 with index 3, we again compare the index to the left-child
           node with value 4. Because the index is the less than the left-child
           node, we simply traverse to the left.

        3. At node 4 with index 3, we recognize that we are at a leaf node and
           stop iterating.

        4. To compute the sublist index, we subtract the offset from the index
           of the leaf node: 5 - 3 = 2. To compute the index in the sublist, we
           simply use the index remaining from iteration. In this case, 3.

        The final index pair from our example is (2, 3) which corresponds to
        index 8 in the sorted list.

        :param int idx: index in sorted list
        :return: (lists index, sublist index) pair

        '''
                if idx < 0:
                    last_len = len(self._lists[-1])
                    if -idx <= last_len:
                        return (len(self._lists) - 1, last_len + idx)
                    None += self._len
                    if idx < 0:
                        raise IndexError('list index out of range')
                elif idx >= self._len:
                    raise IndexError('list index out of range')
                if idx < len(self._lists[0]):
                    return (0, idx)
                _index = None._index
                if not _index:
                    self._build_index()
                pos = 0
                child = 1
                len_index = len(_index)
            # WARNING: Decompyle incomplete

            
            def _build_index(self):
                '''Build a positional index for indexing the sorted list.

        Indexes are represented as binary trees in a dense array notation
        similar to a binary heap.

        For example, given a lists representation storing integers::

            0: [1, 2, 3]
            1: [4, 5]
            2: [6, 7, 8, 9]
            3: [10, 11, 12, 13, 14]

        The first transformation maps the sub-lists by their length. The
        first row of the index is the length of the sub-lists::

            0: [3, 2, 4, 5]

        Each row after that is the sum of consecutive pairs of the previous
        row::

            1: [5, 9]
            2: [14]

        Finally, the index is built by concatenating these lists together::

            _index = [14, 5, 9, 3, 2, 4, 5]

        An offset storing the start of the first row is also stored::

            _offset = 3

        When built, the index can be used for efficient indexing into the list.
        See the comment and notes on ``SortedList._pos`` for details.

        '''
                row0 = list(map(len, self._lists))
                if len(row0) == 1:
                    self._index[:] = row0
                    self._offset = 0
                    return None
                head = None(row0)
                tail = iter(head)
                row1 = list(starmap(add, zip(head, tail)))
                if len(row0) & 1:
                    row1.append(row0[-1])
                if len(row1) == 1:
                    self._index[:] = row1 + row0
                    self._offset = 1
                    return None
                size = None ** (int(log(len(row1) - 1, 2)) + 1)
                row1.extend(repeat(0, size - len(row1)))
                tree = [
                    row0,
                    row1]
            # WARNING: Decompyle incomplete

            
            def __delitem__(self, index):
                """Remove value at `index` from sorted list.

        ``sl.__delitem__(index)`` <==> ``del sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> del sl[2]
        >>> sl
        SortedList(['a', 'b', 'd', 'e'])
        >>> del sl[:2]
        >>> sl
        SortedList(['d', 'e'])

        :param index: integer or slice for indexing
        :raises IndexError: if index out of range

        """
                if isinstance(index, slice):
                    (start, stop, step) = index.indices(self._len)
                    if step == 1 and start < stop:
                        if start == 0 and stop == self._len:
                            return self._clear()
                        if None._len <= 8 * (stop - start):
                            values = self._getitem(slice(None, start))
                            if stop < self._len:
                                values += self._getitem(slice(stop, None))
                            self._clear()
                            return self._update(values)
                        indices = None(start, stop, step)
                        if step > 0:
                            indices = reversed(indices)
                    _delete = self._delete
                    _pos = self._pos
                    for index in indices:
                        (pos, idx) = _pos(index)
                        _delete(pos, idx)
                        return None
                        (pos, idx) = self._pos(index)
                        self._delete(pos, idx)
                        return None

            
            def __getitem__(self, index):
                """Lookup value at `index` in sorted list.

        ``sl.__getitem__(index)`` <==> ``sl[index]``

        Supports slicing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl[1]
        'b'
        >>> sl[-1]
        'e'
        >>> sl[2:5]
        ['c', 'd', 'e']

        :param index: integer or slice for indexing
        :return: value or list of values
        :raises IndexError: if index out of range

        """
                pass
            # WARNING: Decompyle incomplete

            _getitem = __getitem__
            
            def __setitem__(self, index, value):
                '''Raise not-implemented error.

        ``sl.__setitem__(index, value)`` <==> ``sl[index] = value``

        :raises NotImplementedError: use ``del sl[index]`` and
            ``sl.add(value)`` instead

        '''
                message = 'use ``del sl[index]`` and ``sl.add(value)`` instead'
                raise NotImplementedError(message)

            
            def __iter__(self):
                '''Return an iterator over the sorted list.

        ``sl.__iter__()`` <==> ``iter(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        '''
                return chain.from_iterable(self._lists)

            
            def __reversed__(self):
                '''Return a reverse iterator over the sorted list.

        ``sl.__reversed__()`` <==> ``reversed(sl)``

        Iterating the sorted list while adding or deleting values may raise a
        :exc:`RuntimeError` or fail to iterate over all values.

        '''
                return chain.from_iterable(map(reversed, reversed(self._lists)))

            
            def reverse(self):
                '''Raise not-implemented error.

        Sorted list maintains values in ascending sort order. Values may not be
        reversed in-place.

        Use ``reversed(sl)`` for an iterator over values in descending sort
        order.

        Implemented to override `MutableSequence.reverse` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``reversed(sl)`` instead

        '''
                raise NotImplementedError('use ``reversed(sl)`` instead')

            
            def islice(self, start, stop, reverse = (None, None, False)):
                """Return an iterator that slices sorted list from `start` to `stop`.

        The `start` and `stop` index are treated inclusive and exclusive,
        respectively.

        Both `start` and `stop` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.islice(2, 6)
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param int start: start index (inclusive)
        :param int stop: stop index (exclusive)
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
                _len = self._len
                if not _len:
                    return iter(())
                (start, stop, _) = None(start, stop).indices(self._len)
                if start >= stop:
                    return iter(())
                _pos = None._pos
                (min_pos, min_idx) = _pos(start)
                if stop == _len:
                    max_pos = len(self._lists) - 1
                    max_idx = len(self._lists[-1])
                else:
                    (max_pos, max_idx) = _pos(stop)
                return self._islice(min_pos, min_idx, max_pos, max_idx, reverse)

            
            def _islice(self, min_pos, min_idx, max_pos, max_idx, reverse):
                '''Return an iterator that slices sorted list using two index pairs.

        The index pairs are (min_pos, min_idx) and (max_pos, max_idx), the
        first inclusive and the latter exclusive. See `_pos` for details on how
        an index is converted to an index pair.

        When `reverse` is `True`, values are yielded from the iterator in
        reverse order.

        '''
                _lists = self._lists
                if min_pos > max_pos:
                    return iter(())
                if None == max_pos:
                    if reverse:
                        indices = reversed(range(min_idx, max_idx))
                        return map(_lists[min_pos].__getitem__, indices)
                    indices = None(min_idx, max_idx)
                    return map(_lists[min_pos].__getitem__, indices)
                next_pos = None + 1
                if next_pos == max_pos:
                    if reverse:
                        min_indices = range(min_idx, len(_lists[min_pos]))
                        max_indices = range(max_idx)
                        return chain(map(_lists[max_pos].__getitem__, reversed(max_indices)), map(_lists[min_pos].__getitem__, reversed(min_indices)))
                    min_indices = None(min_idx, len(_lists[min_pos]))
                    max_indices = range(max_idx)
                    return chain(map(_lists[min_pos].__getitem__, min_indices), map(_lists[max_pos].__getitem__, max_indices))
                if None:
                    min_indices = range(min_idx, len(_lists[min_pos]))
                    sublist_indices = range(next_pos, max_pos)
                    sublists = map(_lists.__getitem__, reversed(sublist_indices))
                    max_indices = range(max_idx)
                    return chain(map(_lists[max_pos].__getitem__, reversed(max_indices)), chain.from_iterable(map(reversed, sublists)), map(_lists[min_pos].__getitem__, reversed(min_indices)))
                min_indices = None(min_idx, len(_lists[min_pos]))
                sublist_indices = range(next_pos, max_pos)
                sublists = map(_lists.__getitem__, sublist_indices)
                max_indices = range(max_idx)
                return chain(map(_lists[min_pos].__getitem__, min_indices), chain.from_iterable(sublists), map(_lists[max_pos].__getitem__, max_indices))

            
            def irange(self, minimum, maximum, inclusive, reverse = (None, None, (True, True), False)):
                """Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> sl = SortedList('abcdefghij')
        >>> it = sl.irange('c', 'f')
        >>> list(it)
        ['c', 'd', 'e', 'f']

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        """
                _maxes = self._maxes
                if not _maxes:
                    return iter(())
                _lists = None._lists
            # WARNING: Decompyle incomplete

            
            def __len__(self):
                '''Return the size of the sorted list.

        ``sl.__len__()`` <==> ``len(sl)``

        :return: size of sorted list

        '''
                return self._len

            
            def bisect_left(self, value):
                '''Return an index to insert `value` in the sorted list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_left(12)
        2

        :param value: insertion index of value in sorted list
        :return: index

        '''
                _maxes = self._maxes
                if not _maxes:
                    return 0
                pos = None(_maxes, value)
                if pos == len(_maxes):
                    return self._len
                idx = None(self._lists[pos], value)
                return self._loc(pos, idx)

            
            def bisect_right(self, value):
                '''Return an index to insert `value` in the sorted list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([10, 11, 12, 13, 14])
        >>> sl.bisect_right(12)
        3

        :param value: insertion index of value in sorted list
        :return: index

        '''
                _maxes = self._maxes
                if not _maxes:
                    return 0
                pos = None(_maxes, value)
                if pos == len(_maxes):
                    return self._len
                idx = None(self._lists[pos], value)
                return self._loc(pos, idx)

            bisect = bisect_right
            _bisect_right = bisect_right
            
            def count(self, value):
                '''Return number of occurrences of `value` in the sorted list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        >>> sl.count(3)
        3

        :param value: value to count in sorted list
        :return: count

        '''
                _maxes = self._maxes
                if not _maxes:
                    return 0
                pos_left = None(_maxes, value)
                if pos_left == len(_maxes):
                    return 0
                _lists = None._lists
                idx_left = bisect_left(_lists[pos_left], value)
                pos_right = bisect_right(_maxes, value)
                if pos_right == len(_maxes):
                    return self._len - self._loc(pos_left, idx_left)
                idx_right = None(_lists[pos_right], value)
                if pos_left == pos_right:
                    return idx_right - idx_left
                right = None._loc(pos_right, idx_right)
                left = self._loc(pos_left, idx_left)
                return right - left

            
            def copy(self):
                '''Return a shallow copy of the sorted list.

        Runtime complexity: `O(n)`

        :return: new sorted list

        '''
                return self.__class__(self)

            __copy__ = copy
            
            def append(self, value):
                '''Raise not-implemented error.

        Implemented to override `MutableSequence.append` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        '''
                raise NotImplementedError('use ``sl.add(value)`` instead')

            
            def extend(self, values):
                '''Raise not-implemented error.

        Implemented to override `MutableSequence.extend` which provides an
        erroneous default implementation.

        :raises NotImplementedError: use ``sl.update(values)`` instead

        '''
                raise NotImplementedError('use ``sl.update(values)`` instead')

            
            def insert(self, index, value):
                '''Raise not-implemented error.

        :raises NotImplementedError: use ``sl.add(value)`` instead

        '''
                raise NotImplementedError('use ``sl.add(value)`` instead')

            
            def pop(self, index = (-1,)):
                """Remove and return value at `index` in sorted list.

        Raise :exc:`IndexError` if the sorted list is empty or index is out of
        range.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.pop()
        'e'
        >>> sl.pop(2)
        'c'
        >>> sl
        SortedList(['a', 'b', 'd'])

        :param int index: index of value (default -1)
        :return: value
        :raises IndexError: if index is out of range

        """
                if not self._len:
                    raise IndexError('pop index out of range')
                _lists = self._lists
                if index == 0:
                    val = _lists[0][0]
                    self._delete(0, 0)
                    return val
                if None == -1:
                    pos = len(_lists) - 1
                    loc = len(_lists[pos]) - 1
                    val = _lists[pos][loc]
                    self._delete(pos, loc)
                    return val
                if  <= None, index or None, index < len(_lists[0]):
                    pass
                
                self._delete(0, index)
                return val
                len(_lists[-1]) = _lists[0][index]
                if  < -len_last, index or -len_last, index < 0:
                    pass
                
                len_last + index = len(_lists) - 1
                val = _lists[pos][loc]
                self._delete(pos, loc)
                return val
                (pos, idx) = self._pos(index)
                val = _lists[pos][idx]
                self._delete(pos, idx)
                return val

            
            def index(self, value, start, stop = (None, None)):
                """Return first index of value in sorted list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> sl = SortedList('abcde')
        >>> sl.index('d')
        3
        >>> sl.index('z')
        Traceback (most recent call last):
          ...
        ValueError: 'z' is not in list

        :param value: value in sorted list
        :param int start: start index (default None, start of sorted list)
        :param int stop: stop index (default None, end of sorted list)
        :return: index of value
        :raises ValueError: if value is not present

        """
                _len = self._len
                if not _len:
                    raise ValueError('{0!r} is not in list'.format(value))
            # WARNING: Decompyle incomplete

            
            def __add__(self, other):
                """Return new sorted list containing all values in both sequences.

        ``sl.__add__(other)`` <==> ``sl + other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(n*log(n))`

        >>> sl1 = SortedList('bat')
        >>> sl2 = SortedList('cat')
        >>> sl1 + sl2
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: new sorted list

        """
                values = reduce(iadd, self._lists, [])
                values.extend(other)
                return self.__class__(values)

            __radd__ = __add__
            
            def __iadd__(self, other):
                """Update sorted list with values from `other`.

        ``sl.__iadd__(other)`` <==> ``sl += other``

        Values in `other` do not need to be in sorted order.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> sl = SortedList('bat')
        >>> sl += 'cat'
        >>> sl
        SortedList(['a', 'a', 'b', 'c', 't', 't'])

        :param other: other iterable
        :return: existing sorted list

        """
                self._update(other)
                return self

            
            def __mul__(self, num):
                """Return new sorted list with `num` shallow copies of values.

        ``sl.__mul__(num)`` <==> ``sl * num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl * 3
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: new sorted list

        """
                values = reduce(iadd, self._lists, []) * num
                return self.__class__(values)

            __rmul__ = __mul__
            
            def __imul__(self, num):
                """Update the sorted list with `num` shallow copies of values.

        ``sl.__imul__(num)`` <==> ``sl *= num``

        Runtime complexity: `O(n*log(n))`

        >>> sl = SortedList('abc')
        >>> sl *= 3
        >>> sl
        SortedList(['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'c'])

        :param int num: count of shallow copies
        :return: existing sorted list

        """
                values = reduce(iadd, self._lists, []) * num
                self._clear()
                self._update(values)
                return self

            
            def __make_cmp(seq_op, symbol, doc):
                '''Make comparator method.'''
                pass
            # WARNING: Decompyle incomplete

            __eq__ = __make_cmp(eq, '==', 'equal to')
            __ne__ = __make_cmp(ne, '!=', 'not equal to')
            __lt__ = __make_cmp(lt, '<', 'less than')
            __gt__ = __make_cmp(gt, '>', 'greater than')
            __le__ = __make_cmp(le, '<=', 'less than or equal to')
            __ge__ = __make_cmp(ge, '>=', 'greater than or equal to')
            __make_cmp = staticmethod(__make_cmp)
            
            def __reduce__(self):
                values = reduce(iadd, self._lists, [])
                return (type(self), (values,))

            __repr__ = (lambda self: '{0}({1!r})'.format(type(self).__name__, list(self)))()
            
            def _check(self):
                '''Check invariants of sorted list.

        Runtime complexity: `O(n)`

        '''
                pass
            # WARNING: Decompyle incomplete


        
        def identity(value):
            '''Identity function.'''
            return value

        
        class SortedKeyList(SortedList):
            '''Sorted-key list is a subtype of sorted list.

    The sorted-key list maintains values in comparison order based on the
    result of a key function applied to every value.

    All the same methods that are available in :class:`SortedList` are also
    available in :class:`SortedKeyList`.

    Additional methods provided:

    * :attr:`SortedKeyList.key`
    * :func:`SortedKeyList.bisect_key_left`
    * :func:`SortedKeyList.bisect_key_right`
    * :func:`SortedKeyList.irange_key`

    Some examples below use:

    >>> from operator import neg
    >>> neg
    <built-in function neg>
    >>> neg(1)
    -1

    '''
            
            def __init__(self, iterable, key = (None, identity)):
                """Initialize sorted-key list instance.

        Optional `iterable` argument provides an initial iterable of values to
        initialize the sorted-key list.

        Optional `key` argument defines a callable that, like the `key`
        argument to Python's `sorted` function, extracts a comparison key from
        each value. The default is the identity function.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl
        SortedKeyList([], key=<built-in function neg>)
        >>> skl = SortedKeyList([3, 1, 2], key=neg)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: initial values (optional)
        :param key: function used to extract comparison key (optional)

        """
                self._key = key
                self._len = 0
                self._load = self.DEFAULT_LOAD_FACTOR
                self._lists = []
                self._keys = []
                self._maxes = []
                self._index = []
                self._offset = 0
            # WARNING: Decompyle incomplete

            
            def __new__(cls, iterable, key = (None, identity)):
                return object.__new__(cls)

            key = (lambda self: self._key)()
            
            def clear(self):
                '''Remove all values from sorted-key list.

        Runtime complexity: `O(n)`

        '''
                self._len = 0
                del self._lists[:]
                del self._keys[:]
                del self._maxes[:]
                del self._index[:]

            _clear = clear
            
            def add(self, value):
                '''Add `value` to sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.add(3)
        >>> skl.add(1)
        >>> skl.add(2)
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param value: value to add to sorted-key list

        '''
                _lists = self._lists
                _keys = self._keys
                _maxes = self._maxes
                key = self._key(value)
                if _maxes:
                    pos = bisect_right(_maxes, key)
                    if pos == len(_maxes):
                        pos -= 1
                        _lists[pos].append(value)
                        _keys[pos].append(key)
                        _maxes[pos] = key
                    else:
                        idx = bisect_right(_keys[pos], key)
                        _lists[pos].insert(idx, value)
                        _keys[pos].insert(idx, key)
                    self._expand(pos)
                else:
                    _lists.append([
                        value])
                    _keys.append([
                        key])
                    _maxes.append(key)

            
            def _expand(self, pos):
                '''Split sublists with length greater than double the load-factor.

        Updates the index when the sublist length is less than double the load
        level. This requires incrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        '''
                _lists = self._lists
                _keys = self._keys
                _index = self._index
                if len(_keys[pos]) > self._load << 1:
                    _maxes = self._maxes
                    _load = self._load
                    _lists_pos = _lists[pos]
                    _keys_pos = _keys[pos]
                    half = _lists_pos[_load:]
                    half_keys = _keys_pos[_load:]
                    del _lists_pos[_load:]
                    del _keys_pos[_load:]
                    _maxes[pos] = _keys_pos[-1]
                    _lists.insert(pos + 1, half)
                    _keys.insert(pos + 1, half_keys)
                    _maxes.insert(pos + 1, half_keys[-1])
                    del _index[:]
                    return None
            # WARNING: Decompyle incomplete

            
            def update(self, iterable):
                '''Update sorted-key list by adding all values from `iterable`.

        Runtime complexity: `O(k*log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList(key=neg)
        >>> skl.update([3, 1, 2])
        >>> skl
        SortedKeyList([3, 2, 1], key=<built-in function neg>)

        :param iterable: iterable of values to add

        '''
                pass
            # WARNING: Decompyle incomplete

            _update = update
            
            def __contains__(self, value):
                '''Return true if `value` is an element of the sorted-key list.

        ``skl.__contains__(value)`` <==> ``value in skl``

        Runtime complexity: `O(log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> 3 in skl
        True

        :param value: search for value in sorted-key list
        :return: true if `value` in sorted-key list

        '''
                _maxes = self._maxes
                if not _maxes:
                    return False
                key = None._key(value)
                pos = bisect_left(_maxes, key)
                if pos == len(_maxes):
                    return False
                _lists = None._lists
                _keys = self._keys
                idx = bisect_left(_keys[pos], key)
                len_keys = len(_keys)
                len_sublist = len(_keys[pos])
                if _keys[pos][idx] != key:
                    return False
                if None[pos][idx] == value:
                    return True
                None += 1
                if idx == len_sublist:
                    pos += 1
                    if pos == len_keys:
                        return False
                    len_sublist = None(_keys[pos])
                    idx = 0
                continue

            
            def discard(self, value):
                '''Remove `value` from sorted-key list if it is a member.

        If `value` is not a member, do nothing.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.discard(1)
        >>> skl.discard(0)
        >>> skl == [5, 4, 3, 2]
        True

        :param value: `value` to discard from sorted-key list

        '''
                _maxes = self._maxes
                if not _maxes:
                    return None
                key = None._key(value)
                pos = bisect_left(_maxes, key)
                if pos == len(_maxes):
                    return None
                _lists = None._lists
                _keys = self._keys
                idx = bisect_left(_keys[pos], key)
                len_keys = len(_keys)
                len_sublist = len(_keys[pos])
                if _keys[pos][idx] != key:
                    return None
                if None[pos][idx] == value:
                    self._delete(pos, idx)
                    return None
                None += 1
                if idx == len_sublist:
                    pos += 1
                    if pos == len_keys:
                        return None
                    len_sublist = None(_keys[pos])
                    idx = 0
                continue

            
            def remove(self, value):
                '''Remove `value` from sorted-key list; `value` must be a member.

        If `value` is not a member, raise ValueError.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([1, 2, 3, 4, 5], key=neg)
        >>> skl.remove(5)
        >>> skl == [4, 3, 2, 1]
        True
        >>> skl.remove(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 not in list

        :param value: `value` to remove from sorted-key list
        :raises ValueError: if `value` is not in sorted-key list

        '''
                _maxes = self._maxes
                if not _maxes:
                    raise ValueError('{0!r} not in list'.format(value))
                key = self._key(value)
                pos = bisect_left(_maxes, key)
                if pos == len(_maxes):
                    raise ValueError('{0!r} not in list'.format(value))
                _lists = self._lists
                _keys = self._keys
                idx = bisect_left(_keys[pos], key)
                len_keys = len(_keys)
                len_sublist = len(_keys[pos])
                if _keys[pos][idx] != key:
                    raise ValueError('{0!r} not in list'.format(value))
                if _lists[pos][idx] == value:
                    self._delete(pos, idx)
                    return None
                None += 1
                if idx == len_sublist:
                    pos += 1
                    if pos == len_keys:
                        raise ValueError('{0!r} not in list'.format(value))
                    len_sublist = len(_keys[pos])
                    idx = 0
                continue

            
            def _delete(self, pos, idx):
                '''Delete value at the given `(pos, idx)`.

        Combines lists that are less than half the load level.

        Updates the index when the sublist length is more than half the load
        level. This requires decrementing the nodes in a traversal from the
        leaf node to the root. For an example traversal see
        ``SortedList._loc``.

        :param int pos: lists index
        :param int idx: sublist index

        '''
                _lists = self._lists
                _keys = self._keys
                _maxes = self._maxes
                _index = self._index
                keys_pos = _keys[pos]
                lists_pos = _lists[pos]
                del keys_pos[idx]
                del lists_pos[idx]
                len(keys_pos) = self, self._len -= 1, ._len
            # WARNING: Decompyle incomplete

            
            def irange(self, minimum, maximum, inclusive, reverse = (None, None, (True, True), False)):
                '''Create an iterator of values between `minimum` and `maximum`.

        Both `minimum` and `maximum` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange(14.5, 11.5)
        >>> list(it)
        [14, 13, 12]

        :param minimum: minimum value to start iterating
        :param maximum: maximum value to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        '''
                pass
            # WARNING: Decompyle incomplete

            
            def irange_key(self, min_key, max_key, inclusive, reverse = (None, None, (True, True), False)):
                '''Create an iterator of values between `min_key` and `max_key`.

        Both `min_key` and `max_key` default to `None` which is automatically
        inclusive of the beginning and end of the sorted-key list.

        The argument `inclusive` is a pair of booleans that indicates whether
        the minimum and maximum ought to be included in the range,
        respectively. The default is ``(True, True)`` such that the range is
        inclusive of both minimum and maximum.

        When `reverse` is `True` the values are yielded from the iterator in
        reverse order; `reverse` defaults to `False`.

        >>> from operator import neg
        >>> skl = SortedKeyList([11, 12, 13, 14, 15], key=neg)
        >>> it = skl.irange_key(-14, -12)
        >>> list(it)
        [14, 13, 12]

        :param min_key: minimum key to start iterating
        :param max_key: maximum key to stop iterating
        :param inclusive: pair of booleans
        :param bool reverse: yield values in reverse order
        :return: iterator

        '''
                _maxes = self._maxes
                if not _maxes:
                    return iter(())
                _keys = None._keys
            # WARNING: Decompyle incomplete

            _irange_key = irange_key
            
            def bisect_left(self, value):
                '''Return an index to insert `value` in the sorted-key list.

        If the `value` is already present, the insertion point will be before
        (to the left of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_left(1)
        4

        :param value: insertion index of value in sorted-key list
        :return: index

        '''
                return self._bisect_key_left(self._key(value))

            
            def bisect_right(self, value):
                '''Return an index to insert `value` in the sorted-key list.

        Similar to `bisect_left`, but if `value` is already present, the
        insertion point will be after (to the right of) any existing values.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_right(1)
        5

        :param value: insertion index of value in sorted-key list
        :return: index

        '''
                return self._bisect_key_right(self._key(value))

            bisect = bisect_right
            
            def bisect_key_left(self, key):
                '''Return an index to insert `key` in the sorted-key list.

        If the `key` is already present, the insertion point will be before (to
        the left of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_left(-1)
        4

        :param key: insertion index of key in sorted-key list
        :return: index

        '''
                _maxes = self._maxes
                if not _maxes:
                    return 0
                pos = None(_maxes, key)
                if pos == len(_maxes):
                    return self._len
                idx = None(self._keys[pos], key)
                return self._loc(pos, idx)

            _bisect_key_left = bisect_key_left
            
            def bisect_key_right(self, key):
                '''Return an index to insert `key` in the sorted-key list.

        Similar to `bisect_key_left`, but if `key` is already present, the
        insertion point will be after (to the right of) any existing keys.

        Similar to the `bisect` module in the standard library.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedList([5, 4, 3, 2, 1], key=neg)
        >>> skl.bisect_key_right(-1)
        5

        :param key: insertion index of key in sorted-key list
        :return: index

        '''
                _maxes = self._maxes
                if not _maxes:
                    return 0
                pos = None(_maxes, key)
                if pos == len(_maxes):
                    return self._len
                idx = None(self._keys[pos], key)
                return self._loc(pos, idx)

            bisect_key = bisect_key_right
            _bisect_key_right = bisect_key_right
            
            def count(self, value):
                '''Return number of occurrences of `value` in the sorted-key list.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([4, 4, 4, 4, 3, 3, 3, 2, 2, 1], key=neg)
        >>> skl.count(2)
        2

        :param value: value to count in sorted-key list
        :return: count

        '''
                _maxes = self._maxes
                if not _maxes:
                    return 0
                key = None._key(value)
                pos = bisect_left(_maxes, key)
                if pos == len(_maxes):
                    return 0
                _lists = None._lists
                _keys = self._keys
                idx = bisect_left(_keys[pos], key)
                total = 0
                len_keys = len(_keys)
                len_sublist = len(_keys[pos])
                if _keys[pos][idx] != key:
                    return total
                if None[pos][idx] == value:
                    total += 1
                idx += 1
                if idx == len_sublist:
                    pos += 1
                    if pos == len_keys:
                        return total
                    len_sublist = None(_keys[pos])
                    idx = 0
                continue

            
            def copy(self):
                '''Return a shallow copy of the sorted-key list.

        Runtime complexity: `O(n)`

        :return: new sorted-key list

        '''
                return self.__class__(self, key = self._key)

            __copy__ = copy
            
            def index(self, value, start, stop = (None, None)):
                '''Return first index of value in sorted-key list.

        Raise ValueError if `value` is not present.

        Index must be between `start` and `stop` for the `value` to be
        considered present. The default value, None, for `start` and `stop`
        indicate the beginning and end of the sorted-key list.

        Negative indices are supported.

        Runtime complexity: `O(log(n))` -- approximate.

        >>> from operator import neg
        >>> skl = SortedKeyList([5, 4, 3, 2, 1], key=neg)
        >>> skl.index(2)
        3
        >>> skl.index(0)
        Traceback (most recent call last):
          ...
        ValueError: 0 is not in list

        :param value: value in sorted-key list
        :param int start: start index (default None, start of sorted-key list)
        :param int stop: stop index (default None, end of sorted-key list)
        :return: index of value
        :raises ValueError: if value is not present

        '''
                _len = self._len
                if not _len:
                    raise ValueError('{0!r} is not in list'.format(value))
            # WARNING: Decompyle incomplete

            
            def __add__(self, other):
                '''Return new sorted-key list containing all values in both sequences.

        ``skl.__add__(other)`` <==> ``skl + other``

        Values in `other` do not need to be in sorted-key order.

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl1 = SortedKeyList([5, 4, 3], key=neg)
        >>> skl2 = SortedKeyList([2, 1, 0], key=neg)
        >>> skl1 + skl2
        SortedKeyList([5, 4, 3, 2, 1, 0], key=<built-in function neg>)

        :param other: other iterable
        :return: new sorted-key list

        '''
                values = reduce(iadd, self._lists, [])
                values.extend(other)
                return self.__class__(values, key = self._key)

            __radd__ = __add__
            
            def __mul__(self, num):
                '''Return new sorted-key list with `num` shallow copies of values.

        ``skl.__mul__(num)`` <==> ``skl * num``

        Runtime complexity: `O(n*log(n))`

        >>> from operator import neg
        >>> skl = SortedKeyList([3, 2, 1], key=neg)
        >>> skl * 2
        SortedKeyList([3, 3, 2, 2, 1, 1], key=<built-in function neg>)

        :param int num: count of shallow copies
        :return: new sorted-key list

        '''
                values = reduce(iadd, self._lists, []) * num
                return self.__class__(values, key = self._key)

            
            def __reduce__(self):
                values = reduce(iadd, self._lists, [])
                return (type(self), (values, self.key))

            __repr__ = (lambda self: type_name = type(self).__name__'{0}({1!r}, key={2!r})'.format(type_name, list(self), self._key))()
            
            def _check(self):
                '''Check invariants of sorted-key list.

        Runtime complexity: `O(n)`

        '''
                pass
            # WARNING: Decompyle incomplete


        SortedListWithKey = SortedKeyList
        return None
