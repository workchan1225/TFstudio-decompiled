# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: iterables.pyc (Python 3.11)

from collections import Counter, defaultdict, OrderedDict
from itertools import chain, combinations, combinations_with_replacement, cycle, islice, permutations, product, groupby
from itertools import product as cartes
from operator import gt
from sympy.utilities.enumerative import multiset_partitions_taocp, list_visitor, MultisetPartitionTraverser
from sympy.utilities.misc import as_int
from sympy.utilities.decorator import deprecated

def is_palindromic(s, i, j = (0, None)):
    """
    Return True if the sequence is the same from left to right as it
    is from right to left in the whole sequence (default) or in the
    Python slice ``s[i: j]``; else False.

    Examples
    ========

    >>> from sympy.utilities.iterables import is_palindromic
    >>> is_palindromic([1, 0, 1])
    True
    >>> is_palindromic('abcbb')
    False
    >>> is_palindromic('abcbb', 1)
    False

    Normal Python slicing is performed in place so there is no need to
    create a slice of the sequence for testing:

    >>> is_palindromic('abcbb', 1, -1)
    True
    >>> is_palindromic('abcbb', -4, -1)
    True

    See Also
    ========

    sympy.ntheory.digits.is_palindromic: tests integers

    """
    pass
# WARNING: Decompyle incomplete


def flatten(iterable, levels, cls = (None, None)):
    '''
    Recursively denest iterable containers.

    >>> from sympy import flatten

    >>> flatten([1, 2, 3])
    [1, 2, 3]
    >>> flatten([1, 2, [3]])
    [1, 2, 3]
    >>> flatten([1, [2, 3], [4, 5]])
    [1, 2, 3, 4, 5]
    >>> flatten([1.0, 2, (1, None)])
    [1.0, 2, 1, None]

    If you want to denest only a specified number of levels of
    nested containers, then set ``levels`` flag to the desired
    number of levels::

    >>> ls = [[(-2, -1), (1, 2)], [(0, 0)]]

    >>> flatten(ls, levels=1)
    [(-2, -1), (1, 2), (0, 0)]

    If cls argument is specified, it will only flatten instances of that
    class, for example:

    >>> from sympy import Basic, S
    >>> class MyOp(Basic):
    ...     pass
    ...
    >>> flatten([MyOp(S(1), MyOp(S(2), S(3)))], cls=MyOp)
    [1, 2, 3]

    adapted from https://kogs-www.informatik.uni-hamburg.de/~meine/python_tricks
    '''
    pass
# WARNING: Decompyle incomplete


def unflatten(iter, n = (2,)):
    '''Group ``iter`` into tuples of length ``n``. Raise an error if
    the length of ``iter`` is not a multiple of ``n``.
    '''
    pass
# WARNING: Decompyle incomplete


def reshape(seq, how):
    '''Reshape the sequence according to the template in ``how``.

    Examples
    ========

    >>> from sympy.utilities import reshape
    >>> seq = list(range(1, 9))

    >>> reshape(seq, [4]) # lists of 4
    [[1, 2, 3, 4], [5, 6, 7, 8]]

    >>> reshape(seq, (4,)) # tuples of 4
    [(1, 2, 3, 4), (5, 6, 7, 8)]

    >>> reshape(seq, (2, 2)) # tuples of 4
    [(1, 2, 3, 4), (5, 6, 7, 8)]

    >>> reshape(seq, (2, [2])) # (i, i, [i, i])
    [(1, 2, [3, 4]), (5, 6, [7, 8])]

    >>> reshape(seq, ((2,), [2])) # etc....
    [((1, 2), [3, 4]), ((5, 6), [7, 8])]

    >>> reshape(seq, (1, [2], 1))
    [(1, [2, 3], 4), (5, [6, 7], 8)]

    >>> reshape(tuple(seq), ([[1], 1, (2,)],))
    (([[1], 2, (3, 4)],), ([[5], 6, (7, 8)],))

    >>> reshape(tuple(seq), ([1], 1, (2,)))
    (([1], 2, (3, 4)), ([5], 6, (7, 8)))

    >>> reshape(list(range(12)), [2, [3], {2}, (1, (3,), 1)])
    [[0, 1, [2, 3, 4], {5, 6}, (7, (8, 9, 10), 11)]]

    '''
    m = sum(flatten(how))
    (n, rem) = divmod(len(seq), m)
    if m < 0 or rem:
        raise ValueError('template must sum to positive number that divides the length of the sequence')
    i = 0
    container = type(how)
    rv = [
        None] * n
    for k in range(len(rv)):
        _rv = []
        for hi in how:
            if isinstance(hi, int):
                _rv.extend(seq[i:i + hi])
                i += hi
                continue
            n = sum(flatten(hi))
            hi_type = type(hi)
            _rv.append(hi_type(reshape(seq[i:i + n], hi)[0]))
            i += n
            rv[k] = container(_rv)
            return type(seq)(rv)


def group(seq, multiple = (True,)):
