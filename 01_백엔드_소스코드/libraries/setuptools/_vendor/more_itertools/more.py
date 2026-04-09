# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: more.pyc (Python 3.11)

import warnings
from collections import Counter, defaultdict, deque, abc
from collections.abc import Sequence
from functools import partial, reduce, wraps
from heapq import merge, heapify, heapreplace, heappop
from itertools import chain, compress, count, cycle, dropwhile, groupby, islice, repeat, starmap, takewhile, tee, zip_longest
from math import exp, factorial, floor, log
from queue import Empty, Queue
from random import random, randrange, uniform
from operator import itemgetter, mul, sub, gt, lt
from sys import hexversion, maxsize
from time import monotonic
from recipes import consume, flatten, pairwise, powerset, take, unique_everseen
__all__ = [
    'AbortThread',
    'adjacent',
    'always_iterable',
    'always_reversible',
    'bucket',
    'callback_iter',
    'chunked',
    'circular_shifts',
    'collapse',
    'collate',
    'consecutive_groups',
    'consumer',
    'countable',
    'count_cycle',
    'mark_ends',
    'difference',
    'distinct_combinations',
    'distinct_permutations',
    'distribute',
    'divide',
    'exactly_n',
    'filter_except',
    'first',
    'groupby_transform',
    'ilen',
    'interleave_longest',
    'interleave',
    'intersperse',
    'islice_extended',
    'iterate',
    'ichunked',
    'is_sorted',
    'last',
    'locate',
    'lstrip',
    'make_decorator',
    'map_except',
    'map_reduce',
    'nth_or_last',
    'nth_permutation',
    'nth_product',
    'numeric_range',
    'one',
    'only',
    'padded',
    'partitions',
    'set_partitions',
    'peekable',
    'repeat_last',
    'replace',
    'rlocate',
    'rstrip',
    'run_length',
    'sample',
    'seekable',
    'SequenceView',
    'side_effect',
    'sliced',
    'sort_together',
    'split_at',
    'split_after',
    'split_before',
    'split_when',
    'split_into',
    'spy',
    'stagger',
    'strip',
    'substrings',
    'substrings_indexes',
    'time_limited',
    'unique_to_each',
    'unzip',
    'windowed',
    'with_iter',
    'UnequalIterablesError',
    'zip_equal',
    'zip_offset',
    'windowed_complete',
    'all_unique',
    'value_chain',
    'product_index',
    'combination_index',
    'permutation_index']
_marker = object()

def chunked(iterable, n, strict = (False,)):
    '''Break *iterable* into lists of length *n*:

        >>> list(chunked([1, 2, 3, 4, 5, 6], 3))
        [[1, 2, 3], [4, 5, 6]]

    By the default, the last yielded list will have fewer than *n* elements
    if the length of *iterable* is not divisible by *n*:

        >>> list(chunked([1, 2, 3, 4, 5, 6, 7, 8], 3))
        [[1, 2, 3], [4, 5, 6], [7, 8]]

    To use a fill-in value instead, see the :func:`grouper` recipe.

    If the length of *iterable* is not divisible by *n* and *strict* is
    ``True``, then ``ValueError`` will be raised before the last
    list is yielded.

    '''
    pass
# WARNING: Decompyle incomplete


def first(iterable, default = (_marker,)):
    """Return the first item of *iterable*, or *default* if *iterable* is
    empty.

        >>> first([0, 1, 2, 3])
        0
        >>> first([], 'some default')
        'some default'

    If *default* is not provided and there are no items in the iterable,
    raise ``ValueError``.

    :func:`first` is useful when you have a generator of expensive-to-retrieve
    values and want any arbitrary one. It is marginally shorter than
    ``next(iter(iterable), default)``.

    """
    
    try:
        return next(iter(iterable))
    except StopIteration:
        e = None
        if default is _marker:
            raise ValueError('first() was called on an empty iterable, and no default value was provided.'), e
        del e
        return None
        None = 
        del e



def last(iterable, default = (_marker,)):
    """Return the last item of *iterable*, or *default* if *iterable* is
    empty.

        >>> last([0, 1, 2, 3])
        3
        >>> last([], 'some default')
        'some default'

    If *default* is not provided and there are no items in the iterable,
    raise ``ValueError``.
    """
    
    try:
        if isinstance(iterable, Sequence):
            return iterable[-1]
        if None(iterable, '__reversed__') and hexversion != 50856176:
            return next(reversed(iterable))
        return None(iterable, maxlen = 1)[-1]
    except (IndexError, TypeError, StopIteration):
        if default is _marker:
            raise ValueError('last() was called on an empty iterable, and no default was provided.')
        return 



def nth_or_last(iterable, n, default = (_marker,)):
    """Return the nth or the last item of *iterable*,
    or *default* if *iterable* is empty.

        >>> nth_or_last([0, 1, 2, 3], 2)
        2
        >>> nth_or_last([0, 1], 2)
        1
        >>> nth_or_last([], 0, 'some default')
        'some default'

    If *default* is not provided and there are no items in the iterable,
    raise ``ValueError``.
    """
    return last(islice(iterable, n + 1), default = default)


class peekable:
    '''Wrap an iterator to allow lookahead and prepending elements.

    Call :meth:`peek` on the result to get the value that will be returned
    by :func:`next`. This won\'t advance the iterator:

        >>> p = peekable([\'a\', \'b\'])
        >>> p.peek()
        \'a\'
        >>> next(p)
        \'a\'

    Pass :meth:`peek` a default value to return that instead of raising
    ``StopIteration`` when the iterator is exhausted.

        >>> p = peekable([])
        >>> p.peek(\'hi\')
        \'hi\'

    peekables also offer a :meth:`prepend` method, which "inserts" items
    at the head of the iterable:

        >>> p = peekable([1, 2, 3])
        >>> p.prepend(10, 11, 12)
        >>> next(p)
        10
        >>> p.peek()
        11
        >>> list(p)
        [11, 12, 1, 2, 3]

    peekables can be indexed. Index 0 is the item that will be returned by
    :func:`next`, index 1 is the item after that, and so on:
    The values up to the given index will be cached.

        >>> p = peekable([\'a\', \'b\', \'c\', \'d\'])
        >>> p[0]
        \'a\'
        >>> p[1]
        \'b\'
        >>> next(p)
        \'a\'

    Negative indexes are supported, but be aware that they will cache the
    remaining items in the source iterator, which may require significant
    storage.

    To check whether a peekable is exhausted, check its truth value:

        >>> p = peekable([\'a\', \'b\'])
        >>> if p:  # peekable has items
        ...     list(p)
        [\'a\', \'b\']
        >>> if not p:  # peekable is exhausted
        ...     list(p)
        []

    '''
    
    def __init__(self, iterable):
        self._it = iter(iterable)
        self._cache = deque()

    
    def __iter__(self):
        return self

    
    def __bool__(self):
        
        try:
            self.peek()
        except StopIteration:
            return False

        return True

    
    def peek(self, default = (_marker,)):
        '''Return the item that will be next returned from ``next()``.

        Return ``default`` if there are no items left. If ``default`` is not
        provided, raise ``StopIteration``.

        '''
        if not self._cache:
            
            try:
                self._cache.append(next(self._it))
            except StopIteration:
                if default is _marker:
                    raise 
                return 

            return self._cache[0]

    
    def prepend(self, *items):
        '''Stack up items to be the next ones returned from ``next()`` or
        ``self.peek()``. The items will be returned in
        first in, first out order::

            >>> p = peekable([1, 2, 3])
            >>> p.prepend(10, 11, 12)
            >>> next(p)
            10
            >>> list(p)
            [11, 12, 1, 2, 3]

        It is possible, by prepending items, to "resurrect" a peekable that
        previously raised ``StopIteration``.

            >>> p = peekable([])
            >>> next(p)
            Traceback (most recent call last):
              ...
            StopIteration
            >>> p.prepend(1)
            >>> next(p)
            1
            >>> next(p)
            Traceback (most recent call last):
              ...
            StopIteration

        '''
        self._cache.extendleft(reversed(items))

    
    def __next__(self):
        if self._cache:
            return self._cache.popleft()
        return None(self._it)

    
    def _get_slice(self, index):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._get_slice(index)
        cache_len = None(self._cache)
        if index < 0:
            self._cache.extend(self._it)
        elif index >= cache_len:
            self._cache.extend(islice(self._it, index + 1 - cache_len))
        return self._cache[index]



def collate(*iterables, **kwargs):
    """Return a sorted merge of the items from each of several already-sorted
    *iterables*.

        >>> list(collate('ACDZ', 'AZ', 'JKL'))
        ['A', 'A', 'C', 'D', 'J', 'K', 'L', 'Z', 'Z']

    Works lazily, keeping only the next value from each iterable in memory. Use
    :func:`collate` to, for example, perform a n-way mergesort of items that
    don't fit in memory.

    If a *key* function is specified, the iterables will be sorted according
    to its result:

        >>> key = lambda s: int(s)  # Sort by numeric value, not by string
        >>> list(collate(['1', '10'], ['2', '11'], key=key))
        ['1', '2', '10', '11']


    If the *iterables* are sorted in descending order, set *reverse* to
    ``True``:

        >>> list(collate([5, 3, 1], [4, 2, 0], reverse=True))
        [5, 4, 3, 2, 1, 0]

    If the elements of the passed-in iterables are out of order, you might get
    unexpected results.

    On Python 3.5+, this function is an alias for :func:`heapq.merge`.

    """
    warnings.warn('collate is no longer part of more_itertools, use heapq.merge', DeprecationWarning)
# WARNING: Decompyle incomplete


def consumer(func):
    '''Decorator that automatically advances a PEP-342-style "reverse iterator"
    to its first yield point so you don\'t have to call ``next()`` on it
    manually.

        >>> @consumer
        ... def tally():
        ...     i = 0
        ...     while True:
        ...         print(\'Thing number %s is %s.\' % (i, (yield)))
        ...         i += 1
        ...
        >>> t = tally()
        >>> t.send(\'red\')
        Thing number 0 is red.
        >>> t.send(\'fish\')
        Thing number 1 is fish.

    Without the decorator, you would have to call ``next(t)`` before
    ``t.send()`` could be used.

    '''
    pass
# WARNING: Decompyle incomplete


def ilen(iterable):
    '''Return the number of items in *iterable*.

        >>> ilen(x for x in range(1000000) if x % 3 == 0)
        333334

    This consumes the iterable, so handle with care.

    '''
    counter = count()
    deque(zip(iterable, counter), maxlen = 0)
    return next(counter)


def iterate(func, start):
    '''Return ``start``, ``func(start)``, ``func(func(start))``, ...

    >>> from itertools import islice
    >>> list(islice(iterate(lambda x: 2*x, 1), 10))
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    '''
    pass
# WARNING: Decompyle incomplete


def with_iter(context_manager):
    """Wrap an iterable in a ``with`` statement, so it closes once exhausted.

    For example, this will close the file when the iterator is exhausted::

        upper_lines = (line.upper() for line in with_iter(open('foo')))

    Any context manager which returns an iterable is a candidate for
    ``with_iter``.

    """
    pass
# WARNING: Decompyle incomplete


def one(iterable, too_short, too_long = (None, None)):
    """Return the first item from *iterable*, which is expected to contain only
    that item. Raise an exception if *iterable* is empty or has more than one
    item.

    :func:`one` is useful for ensuring that an iterable contains only one item.
    For example, it can be used to retrieve the result of a database query
    that is expected to return a single row.

    If *iterable* is empty, ``ValueError`` will be raised. You may specify a
    different exception with the *too_short* keyword:

        >>> it = []
        >>> one(it)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: too many items in iterable (expected 1)'
        >>> too_short = IndexError('too few items')
        >>> one(it, too_short=too_short)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        IndexError: too few items

    Similarly, if *iterable* contains more than one item, ``ValueError`` will
    be raised. You may specify a different exception with the *too_long*
    keyword:

        >>> it = ['too', 'many']
        >>> one(it)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: Expected exactly one item in iterable, but got 'too',
        'many', and perhaps more.
        >>> too_long = RuntimeError
        >>> one(it, too_long=too_long)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        RuntimeError

    Note that :func:`one` attempts to advance *iterable* twice to ensure there
    is only one item. See :func:`spy` or :func:`peekable` to check iterable
    contents less destructively.

    """
    it = iter(iterable)
    
    try:
        first_value = next(it)
    except StopIteration:
        e = None
        if not too_short:
            raise ValueError('too few items in iterable (expected 1)'), e
        e = None
        del e

    
    try:
        second_value = next(it)
        msg = 'Expected exactly one item in iterable, but got {!r}, {!r}, and perhaps more.'.format(first_value, second_value)
        if not too_long:
            raise ValueError(msg)
    except StopIteration:
        pass

    return first_value


def distinct_permutations(iterable, r = (None,)):
    '''Yield successive distinct permutations of the elements in *iterable*.

        >>> sorted(distinct_permutations([1, 0, 1]))
        [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

    Equivalent to ``set(permutations(iterable))``, except duplicates are not
    generated and thrown away. For larger input sequences this is much more
    efficient.

    Duplicate permutations arise when there are duplicated elements in the
    input iterable. The number of items returned is
    `n! / (x_1! * x_2! * ... * x_n!)`, where `n` is the total number of
    items input, and each `x_i` is the count of a distinct item in the input
    sequence.

    If *r* is given, only the *r*-length permutations are yielded.

        >>> sorted(distinct_permutations([1, 0, 1], r=2))
        [(0, 1), (1, 0), (1, 1)]
        >>> sorted(distinct_permutations(range(3), r=2))
        [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

    '''
    pass
# WARNING: Decompyle incomplete


def intersperse(e, iterable, n = (1,)):
    """Intersperse filler element *e* among the items in *iterable*, leaving
    *n* items between each filler element.

        >>> list(intersperse('!', [1, 2, 3, 4, 5]))
        [1, '!', 2, '!', 3, '!', 4, '!', 5]

        >>> list(intersperse(None, [1, 2, 3, 4, 5], n=2))
        [1, 2, None, 3, 4, None, 5]

    """
    if n == 0:
        raise ValueError('n must be > 0')
    if n == 1:
        return islice(interleave(repeat(e), iterable), 1, None)
    filler = None([
        e])
    chunks = chunked(iterable, n)
    return flatten(islice(interleave(filler, chunks), 1, None))


def unique_to_each(*iterables):
    '''Return the elements from each of the input iterables that aren\'t in the
    other input iterables.

    For example, suppose you have a set of packages, each with a set of
    dependencies::

        {\'pkg_1\': {\'A\', \'B\'}, \'pkg_2\': {\'B\', \'C\'}, \'pkg_3\': {\'B\', \'D\'}}

    If you remove one package, which dependencies can also be removed?

    If ``pkg_1`` is removed, then ``A`` is no longer necessary - it is not
    associated with ``pkg_2`` or ``pkg_3``. Similarly, ``C`` is only needed for
    ``pkg_2``, and ``D`` is only needed for ``pkg_3``::

        >>> unique_to_each({\'A\', \'B\'}, {\'B\', \'C\'}, {\'B\', \'D\'})
        [[\'A\'], [\'C\'], [\'D\']]

    If there are duplicates in one input iterable that aren\'t in the others
    they will be duplicated in the output. Input order is preserved::

        >>> unique_to_each("mississippi", "missouri")
        [[\'p\', \'p\'], [\'o\', \'u\', \'r\']]

    It is assumed that the elements of each iterable are hashable.

    '''
    pass
# WARNING: Decompyle incomplete


def windowed(seq, n, fillvalue, step = (None, 1)):
    """Return a sliding window of width *n* over the given iterable.

        >>> all_windows = windowed([1, 2, 3, 4, 5], 3)
        >>> list(all_windows)
        [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

    When the window is larger than the iterable, *fillvalue* is used in place
    of missing values:

        >>> list(windowed([1, 2, 3], 4))
        [(1, 2, 3, None)]

    Each window will advance in increments of *step*:

        >>> list(windowed([1, 2, 3, 4, 5, 6], 3, fillvalue='!', step=2))
        [(1, 2, 3), (3, 4, 5), (5, 6, '!')]

    To slide into the iterable's items, use :func:`chain` to add filler items
    to the left:

        >>> iterable = [1, 2, 3, 4]
        >>> n = 3
        >>> padding = [None] * (n - 1)
        >>> list(windowed(chain(padding, iterable), 3))
        [(None, None, 1), (None, 1, 2), (1, 2, 3), (2, 3, 4)]
    """
    pass
# WARNING: Decompyle incomplete


def substrings(iterable):
    """Yield all of the substrings of *iterable*.

        >>> [''.join(s) for s in substrings('more')]
        ['m', 'o', 'r', 'e', 'mo', 'or', 're', 'mor', 'ore', 'more']

    Note that non-string iterables can also be subdivided.

        >>> list(substrings([0, 1, 2]))
        [(0,), (1,), (2,), (0, 1), (1, 2), (0, 1, 2)]

    """
    pass
# WARNING: Decompyle incomplete


def substrings_indexes(seq, reverse = (False,)):
    """Yield all substrings and their positions in *seq*

    The items yielded will be a tuple of the form ``(substr, i, j)``, where
    ``substr == seq[i:j]``.

    This function only works for iterables that support slicing, such as
    ``str`` objects.

    >>> for item in substrings_indexes('more'):
    ...    print(item)
    ('m', 0, 1)
    ('o', 1, 2)
    ('r', 2, 3)
    ('e', 3, 4)
    ('mo', 0, 2)
    ('or', 1, 3)
    ('re', 2, 4)
    ('mor', 0, 3)
    ('ore', 1, 4)
    ('more', 0, 4)

    Set *reverse* to ``True`` to yield the same items in the opposite order.


    """
    pass
# WARNING: Decompyle incomplete


class bucket:
    """Wrap *iterable* and return an object that buckets it iterable into
    child iterables based on a *key* function.

        >>> iterable = ['a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'b3']
        >>> s = bucket(iterable, key=lambda x: x[0])  # Bucket by 1st character
        >>> sorted(list(s))  # Get the keys
        ['a', 'b', 'c']
        >>> a_iterable = s['a']
        >>> next(a_iterable)
        'a1'
        >>> next(a_iterable)
        'a2'
        >>> list(s['b'])
        ['b1', 'b2', 'b3']

    The original iterable will be advanced and its items will be cached until
    they are used by the child iterables. This may require significant storage.

    By default, attempting to select a bucket to which no items belong  will
    exhaust the iterable and cache all values.
    If you specify a *validator* function, selected buckets will instead be
    checked against it.

        >>> from itertools import count
        >>> it = count(1, 2)  # Infinite sequence of odd numbers
        >>> key = lambda x: x % 10  # Bucket by last digit
        >>> validator = lambda x: x in {1, 3, 5, 7, 9}  # Odd digits only
        >>> s = bucket(it, key=key, validator=validator)
        >>> 2 in s
        False
        >>> list(s[2])
        []

    """
    
    def __init__(self, iterable, key, validator = (None,)):
