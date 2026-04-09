# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: recipes.pyc (Python 3.11)

'''Imported from the recipes section of the itertools documentation.

All functions taken from the recipes section of the itertools library docs
[1]_.
Some backward-compatible usability improvements have been made.

.. [1] http://docs.python.org/library/itertools.html#recipes

'''
import warnings
from collections import deque
from itertools import chain, combinations, count, cycle, groupby, islice, repeat, starmap, tee, zip_longest
import operator
from random import randrange, sample, choice
__all__ = [
    'all_equal',
    'before_and_after',
    'consume',
    'convolve',
    'dotproduct',
    'first_true',
    'flatten',
    'grouper',
    'iter_except',
    'ncycles',
    'nth',
    'nth_combination',
    'padnone',
    'pad_none',
    'pairwise',
    'partition',
    'powerset',
    'prepend',
    'quantify',
    'random_combination_with_replacement',
    'random_combination',
    'random_permutation',
    'random_product',
    'repeatfunc',
    'roundrobin',
    'sliding_window',
    'tabulate',
    'tail',
    'take',
    'triplewise',
    'unique_everseen',
    'unique_justseen']

def take(n, iterable):
    '''Return first *n* items of the iterable as a list.

        >>> take(3, range(10))
        [0, 1, 2]

    If there are fewer than *n* items in the iterable, all of them are
    returned.

        >>> take(10, range(3))
        [0, 1, 2]

    '''
    return list(islice(iterable, n))


def tabulate(function, start = (0,)):
    '''Return an iterator over the results of ``func(start)``,
    ``func(start + 1)``, ``func(start + 2)``...

    *func* should be a function that accepts one integer argument.

    If *start* is not specified it defaults to 0. It will be incremented each
    time the iterator is advanced.

        >>> square = lambda x: x ** 2
        >>> iterator = tabulate(square, -3)
        >>> take(4, iterator)
        [9, 4, 1, 0]

    '''
    return map(function, count(start))


def tail(n, iterable):
    """Return an iterator over the last *n* items of *iterable*.

    >>> t = tail(3, 'ABCDEFG')
    >>> list(t)
    ['E', 'F', 'G']

    """
    return iter(deque(iterable, maxlen = n))


def consume(iterator, n = (None,)):
    '''Advance *iterable* by *n* steps. If *n* is ``None``, consume it
    entirely.

    Efficiently exhausts an iterator without returning values. Defaults to
    consuming the whole iterator, but an optional second argument may be
    provided to limit consumption.

        >>> i = (x for x in range(10))
        >>> next(i)
        0
        >>> consume(i, 3)
        >>> next(i)
        4
        >>> consume(i)
        >>> next(i)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration

    If the iterator has fewer items remaining than the provided limit, the
    whole iterator will be consumed.

        >>> i = (x for x in range(3))
        >>> consume(i, 5)
        >>> next(i)
        Traceback (most recent call last):
          File "<stdin>", line 1, in <module>
        StopIteration

    '''
    pass
# WARNING: Decompyle incomplete


def nth(iterable, n, default = (None,)):
    '''Returns the nth item or a default value.

    >>> l = range(10)
    >>> nth(l, 3)
    3
    >>> nth(l, 20, "zebra")
    \'zebra\'

    '''
    return next(islice(iterable, n, None), default)


def all_equal(iterable):
