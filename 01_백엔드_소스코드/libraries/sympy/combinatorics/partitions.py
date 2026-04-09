# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: partitions.pyc (Python 3.11)

from sympy.core import Basic, Dict, sympify, Tuple
from sympy.core.numbers import Integer
from sympy.core.sorting import default_sort_key
from sympy.core.sympify import _sympify
from sympy.functions.combinatorial.numbers import bell
from sympy.matrices import zeros
from sympy.sets.sets import FiniteSet, Union
from sympy.utilities.iterables import flatten, group
from sympy.utilities.misc import as_int
from collections import defaultdict

class Partition(FiniteSet):
    '''
    This class represents an abstract partition.

    A partition is a set of disjoint sets whose union equals a given set.

    See Also
    ========

    sympy.utilities.iterables.partitions,
    sympy.utilities.iterables.multiset_partitions
    '''
    _rank = None
    _partition = None
    
    def __new__(cls, *partition):
        '''
        Generates a new partition object.

        This method also verifies if the arguments passed are
        valid and raises a ValueError if they are not.

        Examples
        ========

        Creating Partition from Python lists:

        >>> from sympy.combinatorics import Partition
        >>> a = Partition([1, 2], [3])
        >>> a
        Partition({3}, {1, 2})
        >>> a.partition
        [[1, 2], [3]]
        >>> len(a)
        2
        >>> a.members
        (1, 2, 3)

        Creating Partition from Python sets:

        >>> Partition({1, 2, 3}, {4, 5})
        Partition({4, 5}, {1, 2, 3})

        Creating Partition from SymPy finite sets:

        >>> from sympy import FiniteSet
        >>> a = FiniteSet(1, 2, 3)
        >>> b = FiniteSet(4, 5)
        >>> Partition(a, b)
        Partition({4, 5}, {1, 2, 3})
        '''
        args = []
        dups = False
    # WARNING: Decompyle incomplete

    
    def sort_key(self, order = (None,)):
        '''Return a canonical key that can be used for sorting.

        Ordering is based on the size and sorted elements of the partition
        and ties are broken with the rank.

        Examples
        ========

        >>> from sympy import default_sort_key
        >>> from sympy.combinatorics import Partition
        >>> from sympy.abc import x
        >>> a = Partition([1, 2])
        >>> b = Partition([3, 4])
        >>> c = Partition([1, x])
        >>> d = Partition(list(range(4)))
        >>> l = [d, b, a + 1, a, c]
        >>> l.sort(key=default_sort_key); l
        [Partition({1, 2}), Partition({1}, {2}), Partition({1, x}), Partition({3, 4}), Partition({0, 1, 2, 3})]
        '''
        pass
    # WARNING: Decompyle incomplete

    partition = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def __add__(self, other):
        '''
        Return permutation whose rank is ``other`` greater than current rank,
        (mod the maximum rank for the set).

        Examples
        ========

        >>> from sympy.combinatorics import Partition
        >>> a = Partition([1, 2], [3])
        >>> a.rank
        1
        >>> (a + 1).rank
        2
        >>> (a + 100).rank
        1
        '''
        other = as_int(other)
        offset = self.rank + other
        result = RGS_unrank(offset % RGS_enum(self.size), self.size)
        return Partition.from_rgs(result, self.members)

    
    def __sub__(self, other):
        '''
        Return permutation whose rank is ``other`` less than current rank,
        (mod the maximum rank for the set).

        Examples
        ========

        >>> from sympy.combinatorics import Partition
        >>> a = Partition([1, 2], [3])
        >>> a.rank
        1
        >>> (a - 1).rank
        0
        >>> (a - 100).rank
        1
        '''
        return self.__add__(-other)

    
    def __le__(self, other):
        '''
        Checks if a partition is less than or equal to
        the other based on rank.

        Examples
        ========

        >>> from sympy.combinatorics import Partition
        >>> a = Partition([1, 2], [3, 4, 5])
        >>> b = Partition([1], [2, 3], [4], [5])
        >>> a.rank, b.rank
        (9, 34)
        >>> a <= a
        True
        >>> a <= b
        True
        '''
        return self.sort_key() <= sympify(other).sort_key()

    
    def __lt__(self, other):
        '''
        Checks if a partition is less than the other.

        Examples
        ========

        >>> from sympy.combinatorics import Partition
        >>> a = Partition([1, 2], [3, 4, 5])
        >>> b = Partition([1], [2, 3], [4], [5])
        >>> a.rank, b.rank
        (9, 34)
        >>> a < b
        True
        '''
        return self.sort_key() < sympify(other).sort_key()

    rank = (lambda self: pass# WARNING: Decompyle incomplete
)()
    RGS = (lambda self: pass# WARNING: Decompyle incomplete
)()
    from_rgs = (lambda self, rgs, elements: if len(rgs) != len(elements):
raise ValueError('mismatch in rgs and element lengths')max_elem = max(rgs) + 1partition = range(max_elem)()j = 0# WARNING: Decompyle incomplete
)()


class IntegerPartition(Basic):
    '''
    This class represents an integer partition.

    Explanation
    ===========

    In number theory and combinatorics, a partition of a positive integer,
    ``n``, also called an integer partition, is a way of writing ``n`` as a
    list of positive integers that sum to n. Two partitions that differ only
    in the order of summands are considered to be the same partition; if order
    matters then the partitions are referred to as compositions. For example,
    4 has five partitions: [4], [3, 1], [2, 2], [2, 1, 1], and [1, 1, 1, 1];
    the compositions [1, 2, 1] and [1, 1, 2] are the same as partition
    [2, 1, 1].

    See Also
    ========

    sympy.utilities.iterables.partitions,
    sympy.utilities.iterables.multiset_partitions

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Partition_%28number_theory%29
    '''
    _dict = None
    _keys = None
    
    def __new__(cls, partition, integer = (None,)):
        '''
        Generates a new IntegerPartition object from a list or dictionary.

        Explanation
        ===========

        The partition can be given as a list of positive integers or a
        dictionary of (integer, multiplicity) items. If the partition is
        preceded by an integer an error will be raised if the partition
        does not sum to that given integer.

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> a = IntegerPartition([5, 4, 3, 1, 1])
        >>> a
        IntegerPartition(14, (5, 4, 3, 1, 1))
        >>> print(a)
        [5, 4, 3, 1, 1]
        >>> IntegerPartition({1:3, 2:1})
        IntegerPartition(5, (2, 1, 1, 1))

        If the value that the partition should sum to is given first, a check
        will be made to see n error will be raised if there is a discrepancy:

        >>> IntegerPartition(10, [5, 4, 3, 1])
        Traceback (most recent call last):
        ...
        ValueError: The partition is not valid

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def prev_lex(self):
        '''Return the previous partition of the integer, n, in lexical order,
        wrapping around to [1, ..., 1] if the partition is [n].

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> p = IntegerPartition([4])
        >>> print(p.prev_lex())
        [3, 1]
        >>> p.partition > p.prev_lex().partition
        True
        '''
        d = defaultdict(int)
        d.update(self.as_dict())
        keys = self._keys
        if keys == [
            1]:
            return IntegerPartition({
                self.integer: 1 })
        if None[-1] != 1:
            if keys[-1] == 2:
                2 = None
            else:
                d[keys[-1] - 1] = 1
                d[1] = 1
    # WARNING: Decompyle incomplete

    
    def next_lex(self):
        '''Return the next partition of the integer, n, in lexical order,
        wrapping around to [n] if the partition is [1, ..., 1].

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> p = IntegerPartition([3, 1])
        >>> print(p.next_lex())
        [4]
        >>> p.partition < p.next_lex().partition
        True
        '''
        d = defaultdict(int)
        d.update(self.as_dict())
        key = self._keys
        a = key[-1]
        if a == self.integer:
            d.clear()
            d[1] = self.integer
        elif a == 1:
            if d[a] > 1:
                pass
            else:
                key[-2] = None
                (d[b] - 1) * b = None
                d[b] = 0
        elif d[a] > 1:
            if len(key) == 1:
                d.clear()
                d[a + 1] = 1
                d[1] = self.integer - a - 1
            else:
                a1 = a + 1
                d[a] * a - a1 = None
                d[a] = 0
        else:
            b = key[-2]
            b1 = b + 1
            d[b] * b + d[a] * a - b1 = None
            d[a] = 0
            d[b] = 0
            d[1] = need
        return IntegerPartition(self.integer, d)

    
    def as_dict(self):
        '''Return the partition as a dictionary whose keys are the
        partition integers and the values are the multiplicity of that
        integer.

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> IntegerPartition([1]*3 + [2] + [3]*4).as_dict()
        {1: 3, 2: 1, 3: 4}
        '''
        pass
    # WARNING: Decompyle incomplete

    conjugate = (lambda self: j = 1temp_arr = list(self.partition) + [
0]k = temp_arr[0]b = [
0] * k# WARNING: Decompyle incomplete
)()
    
    def __lt__(self, other):
        '''Return True if self is less than other when the partition
        is listed from smallest to biggest.

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> a = IntegerPartition([3, 1])
        >>> a < a
        False
        >>> b = a.next_lex()
        >>> a < b
        True
        >>> a == b
        False
        '''
        return list(reversed(self.partition)) < list(reversed(other.partition))

    
    def __le__(self, other):
        '''Return True if self is less than other when the partition
        is listed from smallest to biggest.

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> a = IntegerPartition([4])
        >>> a <= a
        True
        '''
        return list(reversed(self.partition)) <= list(reversed(other.partition))

    
    def as_ferrers(self, char = ('#',)):
        '''
        Prints the ferrer diagram of a partition.

        Examples
        ========

        >>> from sympy.combinatorics.partitions import IntegerPartition
        >>> print(IntegerPartition([1, 1, 5]).as_ferrers())
        #####
        #
        #
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        return str(list(self.partition))



def random_integer_partition(n, seed = (None,)):
    '''
    Generates a random integer partition summing to ``n`` as a list
    of reverse-sorted integers.

    Examples
    ========

    >>> from sympy.combinatorics.partitions import random_integer_partition

    For the following, a seed is given so a known value can be shown; in
    practice, the seed would not be given.

    >>> random_integer_partition(100, seed=[1, 1, 12, 1, 2, 1, 85, 1])
    [85, 12, 2, 1]
    >>> random_integer_partition(10, seed=[1, 2, 3, 1, 5, 1])
    [5, 3, 1, 1]
    >>> random_integer_partition(1)
    [1]
    '''
    _randint = _randint
    import sympy.core.random
    n = as_int(n)
    if n < 1:
        raise ValueError('n must be a positive integer')
    randint = _randint(seed)
    partition = []
# WARNING: Decompyle incomplete


def RGS_generalized(m):
    '''
    Computes the m + 1 generalized unrestricted growth strings
    and returns them as rows in matrix.

    Examples
    ========

    >>> from sympy.combinatorics.partitions import RGS_generalized
    >>> RGS_generalized(6)
    Matrix([
    [  1,   1,   1,  1,  1, 1, 1],
    [  1,   2,   3,  4,  5, 6, 0],
    [  2,   5,  10, 17, 26, 0, 0],
    [  5,  15,  37, 77,  0, 0, 0],
    [ 15,  52, 151,  0,  0, 0, 0],
    [ 52, 203,   0,  0,  0, 0, 0],
    [203,   0,   0,  0,  0, 0, 0]])
    '''
    d = zeros(m + 1)
    for i in range(m + 1):
        d[(0, i)] = 1
        for i in range(1, m + 1):
            for j in range(m):
                if j <= m - i:
                    d[(i, j)] = j * d[(i - 1, j)] + d[(i - 1, j + 1)]
                    continue
                d[(i, j)] = 0
                return d


def RGS_enum(m):
    '''
    RGS_enum computes the total number of restricted growth strings
    possible for a superset of size m.

    Examples
    ========

    >>> from sympy.combinatorics.partitions import RGS_enum
    >>> from sympy.combinatorics import Partition
    >>> RGS_enum(4)
    15
    >>> RGS_enum(5)
    52
    >>> RGS_enum(6)
    203

    We can check that the enumeration is correct by actually generating
    the partitions. Here, the 15 partitions of 4 items are generated:

    >>> a = Partition(list(range(4)))
    >>> s = set()
    >>> for i in range(20):
    ...     s.add(a)
    ...     a += 1
    ...
    >>> assert len(s) == 15

    '''
    if m < 1:
        return 0
    if None == 1:
        return 1
    return None(m)


def RGS_unrank(rank, m):
    '''
    Gives the unranked restricted growth string for a given
    superset size.

    Examples
    ========

    >>> from sympy.combinatorics.partitions import RGS_unrank
    >>> RGS_unrank(14, 4)
    [0, 1, 2, 3]
    >>> RGS_unrank(0, 4)
    [0, 0, 0, 0]
    '''
    if m < 1:
        raise ValueError('The superset size must be >= 1')
    if rank < 0 or RGS_enum(m) <= rank:
        raise ValueError('Invalid arguments')
    L = [
        1] * (m + 1)
    j = 1
    D = RGS_generalized(m)
    for i in range(2, m + 1):
        v = D[(m - i, j)]
        cr = j * v
        if cr <= rank:
            L[i] = j + 1
            rank -= cr
            j += 1
            continue
        L[i] = int(rank / v + 1)
        rank %= v
        return L[1:]()


def RGS_rank(rgs):
    '''
    Computes the rank of a restricted growth string.

    Examples
    ========

    >>> from sympy.combinatorics.partitions import RGS_rank, RGS_unrank
    >>> RGS_rank([0, 1, 2, 1, 3])
    42
    >>> RGS_rank(RGS_unrank(4, 7))
    4
    '''
    rgs_size = len(rgs)
    rank = 0
    D = RGS_generalized(rgs_size)
    for i in range(1, rgs_size):
        n = len(rgs[i + 1:])
        m = max(rgs[0:i])
        rank += D[(n, m + 1)] * rgs[i]
        return rank
