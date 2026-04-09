# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: more.pyc (Python 3.11)

import math
import warnings
from collections import Counter, defaultdict, deque, abc
from collections.abc import Sequence
from contextlib import suppress
from functools import cached_property, partial, reduce, wraps
from heapq import heapify, heapreplace
from itertools import chain, combinations, compress, count, cycle, dropwhile, groupby, islice, permutations, repeat, starmap, takewhile, tee, zip_longest, product
from math import comb, e, exp, factorial, floor, fsum, log, log1p, perm, tau
from math import ceil
from queue import Empty, Queue
from random import random, randrange, shuffle, uniform
from operator import attrgetter, is_not, itemgetter, lt, mul, neg, sub, gt
from sys import hexversion, maxsize
from time import monotonic
from recipes import _marker, _zip_equal, UnequalIterablesError, consume, first_true, flatten, is_prime, nth, powerset, sieve, take, unique_everseen, all_equal, batched
__all__ = [
    'AbortThread',
    'SequenceView',
    'UnequalIterablesError',
    'adjacent',
    'all_unique',
    'always_iterable',
    'always_reversible',
    'argmax',
    'argmin',
    'bucket',
    'callback_iter',
    'chunked',
    'chunked_even',
    'circular_shifts',
    'collapse',
    'combination_index',
    'combination_with_replacement_index',
    'consecutive_groups',
    'constrained_batches',
    'consumer',
    'count_cycle',
    'countable',
    'derangements',
    'dft',
    'difference',
    'distinct_combinations',
    'distinct_permutations',
    'distribute',
    'divide',
    'doublestarmap',
    'duplicates_everseen',
    'duplicates_justseen',
    'classify_unique',
    'exactly_n',
    'extract',
    'filter_except',
    'filter_map',
    'first',
    'gray_product',
    'groupby_transform',
    'ichunked',
    'iequals',
    'idft',
    'ilen',
    'interleave',
    'interleave_evenly',
    'interleave_longest',
    'interleave_randomly',
    'intersperse',
    'is_sorted',
    'islice_extended',
    'iterate',
    'iter_suppress',
    'join_mappings',
    'last',
    'locate',
    'longest_common_prefix',
    'lstrip',
    'make_decorator',
    'map_except',
    'map_if',
    'map_reduce',
    'mark_ends',
    'minmax',
    'nth_or_last',
    'nth_permutation',
    'nth_prime',
    'nth_product',
    'nth_combination_with_replacement',
    'numeric_range',
    'one',
    'only',
    'outer_product',
    'padded',
    'partial_product',
    'partitions',
    'peekable',
    'permutation_index',
    'powerset_of_sets',
    'product_index',
    'raise_',
    'repeat_each',
    'repeat_last',
    'replace',
    'rlocate',
    'rstrip',
    'run_length',
    'sample',
    'seekable',
    'set_partitions',
    'side_effect',
    'sliced',
    'sort_together',
    'split_after',
    'split_at',
    'split_before',
    'split_into',
    'split_when',
    'spy',
    'stagger',
    'strip',
    'strictly_n',
    'substrings',
    'substrings_indexes',
    'takewhile_inclusive',
    'time_limited',
    'unique_in_window',
    'unique_to_each',
    'unzip',
    'value_chain',
    'windowed',
    'windowed_complete',
    'with_iter',
    'zip_broadcast',
    'zip_equal',
    'zip_offset']

try:
    from math import sumprod as _fsumprod
except ImportError:
    
    def dl_split(x = None):
        '''Split a float into two half-precision components.'''
        t = x * 1.34218e+08
        hi = t - t - x
        lo = x - hi
        return (hi, lo)

    
    def dl_mul(x, y):
        '''Lossless multiplication.'''
        (xx_hi, xx_lo) = dl_split(x)
        (yy_hi, yy_lo) = dl_split(y)
        p = xx_hi * yy_hi
        q = xx_hi * yy_lo + xx_lo * yy_hi
        z = p + q
        zz = (p - z) + q + xx_lo * yy_lo
        return (z, zz)

    
    def _fsumprod(p, q):
        return fsum(chain.from_iterable(map(dl_mul, p, q)))



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
    for item in iterable:
        
        return None, item
        if default is _marker:
            raise ValueError('first() was called on an empty iterable, and no default value was provided.')
        return default


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
        if None(iterable, '__reversed__', None):
            return next(reversed(iterable))
        return None(iterable, maxlen = 1)[-1]
    except (IndexError, TypeError, StopIteration):
        if default is _marker:
            raise ValueError('last() was called on an empty iterable, and no default value was provided.')
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

    For example, there are 168 prime numbers below 1,000:

        >>> ilen(sieve(1000))
        168

    Equivalent to, but faster than::

        def ilen(iterable):
            count = 0
            for _ in iterable:
                count += 1
            return count

    This fully consumes the iterable, so handle with care.

    '''
    return sum(compress(repeat(1), zip(iterable)))


def iterate(func, start):
    '''Return ``start``, ``func(start)``, ``func(func(start))``, ...

    Produces an infinite iterator. To add a stopping condition,
    use :func:`take`, ``takewhile``, or :func:`takewhile_inclusive`:.

    >>> take(10, iterate(lambda x: 2*x, 1))
    [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]

    >>> collatz = lambda x: 3*x + 1 if x%2==1 else x // 2
    >>> list(takewhile_inclusive(lambda x: x!=1, iterate(collatz, 10)))
    [10, 5, 16, 8, 4, 2, 1]

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
        ValueError: too few items in iterable (expected 1)'
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
    iterator = iter(iterable)
    for first in iterator:
        for second in iterator:
            msg = f'''Expected exactly one item in iterable, but got {first!r}, {second!r}, and perhaps more.'''
            if not too_long:
                raise ValueError(msg)
            
            return too_long, first
            if not too_short:
                raise ValueError('too few items in iterable (expected 1)')


def raise_(exception, *args):
    pass
# WARNING: Decompyle incomplete


def strictly_n(iterable, n, too_short, too_long = (None, None)):
    """Validate that *iterable* has exactly *n* items and return them if
    it does. If it has fewer than *n* items, call function *too_short*
    with the actual number of items. If it has more than *n* items, call function
    *too_long* with the number ``n + 1``.

        >>> iterable = ['a', 'b', 'c', 'd']
        >>> n = 4
        >>> list(strictly_n(iterable, n))
        ['a', 'b', 'c', 'd']

    Note that the returned iterable must be consumed in order for the check to
    be made.

    By default, *too_short* and *too_long* are functions that raise
    ``ValueError``.

        >>> list(strictly_n('ab', 3))  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: too few items in iterable (got 2)

        >>> list(strictly_n('abc', 2))  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        ValueError: too many items in iterable (got at least 3)

    You can instead supply functions that do something else.
    *too_short* will be called with the number of items in *iterable*.
    *too_long* will be called with `n + 1`.

        >>> def too_short(item_count):
        ...     raise RuntimeError
        >>> it = strictly_n('abcd', 6, too_short=too_short)
        >>> list(it)  # doctest: +IGNORE_EXCEPTION_DETAIL
        Traceback (most recent call last):
        ...
        RuntimeError

        >>> def too_long(item_count):
        ...     print('The boss is going to hear about this')
        >>> it = strictly_n('abcdef', 4, too_long=too_long)
        >>> list(it)
        The boss is going to hear about this
        ['a', 'b', 'c', 'd']

    """
    pass
# WARNING: Decompyle incomplete


def distinct_permutations(iterable, r = (None,)):
    """Yield successive distinct permutations of the elements in *iterable*.

        >>> sorted(distinct_permutations([1, 0, 1]))
        [(0, 1, 1), (1, 0, 1), (1, 1, 0)]

    Equivalent to yielding from ``set(permutations(iterable))``, except
    duplicates are not generated and thrown away. For larger input sequences
    this is much more efficient.

    Duplicate permutations arise when there are duplicated elements in the
    input iterable. The number of items returned is
    `n! / (x_1! * x_2! * ... * x_n!)`, where `n` is the total number of
    items input, and each `x_i` is the count of a distinct item in the input
    sequence. The function :func:`multinomial` computes this directly.

    If *r* is given, only the *r*-length permutations are yielded.

        >>> sorted(distinct_permutations([1, 0, 1], r=2))
        [(0, 1), (1, 0), (1, 1)]
        >>> sorted(distinct_permutations(range(3), r=2))
        [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]

    *iterable* need not be sortable, but note that using equal (``x == y``)
    but non-identical (``id(x) != id(y)``) elements may produce surprising
    behavior. For example, ``1`` and ``True`` are equal but non-identical:

        >>> list(distinct_permutations([1, True, '3']))  # doctest: +SKIP
        [
            (1, True, '3'),
            (1, '3', True),
            ('3', 1, True)
        ]
        >>> list(distinct_permutations([1, 2, '3']))  # doctest: +SKIP
        [
            (1, 2, '3'),
            (1, '3', 2),
            (2, 1, '3'),
            (2, '3', 1),
            ('3', 1, 2),
            ('3', 2, 1)
        ]
    """
    pass
# WARNING: Decompyle incomplete


def derangements(iterable, r = (None,)):
    '''Yield successive derangements of the elements in *iterable*.

    A derangement is a permutation in which no element appears at its original
    index. In other words, a derangement is a permutation that has no fixed points.

    Suppose Alice, Bob, Carol, and Dave are playing Secret Santa.
    The code below outputs all of the different ways to assign gift recipients
    such that nobody is assigned to himself or herself:

        >>> for d in derangements([\'Alice\', \'Bob\', \'Carol\', \'Dave\']):
        ...    print(\', \'.join(d))
        Bob, Alice, Dave, Carol
        Bob, Carol, Dave, Alice
        Bob, Dave, Alice, Carol
        Carol, Alice, Dave, Bob
        Carol, Dave, Alice, Bob
        Carol, Dave, Bob, Alice
        Dave, Alice, Bob, Carol
        Dave, Carol, Alice, Bob
        Dave, Carol, Bob, Alice

    If *r* is given, only the *r*-length derangements are yielded.

        >>> sorted(derangements(range(3), 2))
        [(1, 0), (1, 2), (2, 0)]
        >>> sorted(derangements([0, 2, 3], 2))
        [(2, 0), (2, 3), (3, 0)]

    Elements are treated as unique based on their position, not on their value.

    Consider the Secret Santa example with two *different* people who have
    the *same* name. Then there are two valid gift assignments even though
    it might appear that a person is assigned to themselves:

        >>> names = [\'Alice\', \'Bob\', \'Bob\']
        >>> list(derangements(names))
        [(\'Bob\', \'Bob\', \'Alice\'), (\'Bob\', \'Alice\', \'Bob\')]

    To avoid confusion, make the inputs distinct:

        >>> deduped = [f\'{name}{index}\' for index, name in enumerate(names)]
        >>> list(derangements(deduped))
        [(\'Bob1\', \'Bob2\', \'Alice0\'), (\'Bob2\', \'Alice0\', \'Bob1\')]

    The number of derangements of a set of size *n* is known as the
    "subfactorial of n".  For n > 0, the subfactorial is:
    ``round(math.factorial(n) / math.e)``.

    References:

    * Article:  https://www.numberanalytics.com/blog/ultimate-guide-to-derangements-in-combinatorics
    * Sizes:    https://oeis.org/A000166
    '''
    xs = tuple(iterable)
    ys = tuple(range(len(xs)))
    return compress(permutations(xs, r = r), map(all, map(map, repeat(is_not), repeat(ys), permutations(ys, r = r))))


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
    """Wrap *iterable* and return an object that buckets the iterable into
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
