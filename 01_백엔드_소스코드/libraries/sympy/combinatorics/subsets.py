# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subsets.pyc (Python 3.11)

from itertools import combinations
from sympy.combinatorics.graycode import GrayCode

class Subset:
    """
    Represents a basic subset object.

    Explanation
    ===========

    We generate subsets using essentially two techniques,
    binary enumeration and lexicographic enumeration.
    The Subset class takes two arguments, the first one
    describes the initial subset to consider and the second
    describes the superset.

    Examples
    ========

    >>> from sympy.combinatorics import Subset
    >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
    >>> a.next_binary().subset
    ['b']
    >>> a.prev_binary().subset
    ['c']
    """
    _rank_binary = None
    _rank_lex = None
    _rank_graycode = None
    _subset = None
    _superset = None
    
    def __new__(cls, subset, superset):
        """
        Default constructor.

        It takes the ``subset`` and its ``superset`` as its parameters.

        Examples
        ========

        >>> from sympy.combinatorics import Subset
        >>> a = Subset(['c', 'd'], ['a', 'b', 'c', 'd'])
        >>> a.subset
        ['c', 'd']
        >>> a.superset
        ['a', 'b', 'c', 'd']
        >>> a.size
        2
        """
        if len(subset) > len(superset):
            raise ValueError('Invalid arguments have been provided. The superset must be larger than the subset.')
        for elem in subset:
            if elem not in superset:
                raise ValueError('The superset provided is invalid as it does not contain the element {}'.format(elem))
            obj = object.__new__(cls)
            obj._subset = subset
            obj._superset = superset
            return obj

    
    def __eq__(self, other):
