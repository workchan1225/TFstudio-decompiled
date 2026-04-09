# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: permutations.pyc (Python 3.11)

import random
from collections import defaultdict
from collections.abc import Iterable
from functools import reduce
from sympy.core.parameters import global_parameters
from sympy.core.basic import Atom
from sympy.core.expr import Expr
from sympy.core.numbers import int_valued
from sympy.core.numbers import Integer
from sympy.core.sympify import _sympify
from sympy.matrices import zeros
from sympy.polys.polytools import lcm
from sympy.printing.repr import srepr
from sympy.utilities.iterables import flatten, has_variety, minlex, has_dups, runs, is_sequence
from sympy.utilities.misc import as_int
from mpmath.libmp.libintmath import ifac
from sympy.multipledispatch import dispatch

def _af_rmul(a, b):
    '''
    Return the product b*a; input and output are array forms. The ith value
    is a[b[i]].

    Examples
    ========

    >>> from sympy.combinatorics.permutations import _af_rmul, Permutation

    >>> a, b = [1, 0, 2], [0, 2, 1]
    >>> _af_rmul(a, b)
    [1, 2, 0]
    >>> [a[b[i]] for i in range(3)]
    [1, 2, 0]

    This handles the operands in reverse order compared to the ``*`` operator:

    >>> a = Permutation(a)
    >>> b = Permutation(b)
    >>> list(a*b)
    [2, 0, 1]
    >>> [b(a(i)) for i in range(3)]
    [2, 0, 1]

    See Also
    ========

    rmul, _af_rmuln
    '''
    pass
# WARNING: Decompyle incomplete


def _af_rmuln(*abc):
    '''
    Given [a, b, c, ...] return the product of ...*c*b*a using array forms.
    The ith value is a[b[c[i]]].

    Examples
    ========

    >>> from sympy.combinatorics.permutations import _af_rmul, Permutation

    >>> a, b = [1, 0, 2], [0, 2, 1]
    >>> _af_rmul(a, b)
    [1, 2, 0]
    >>> [a[b[i]] for i in range(3)]
    [1, 2, 0]

    This handles the operands in reverse order compared to the ``*`` operator:

    >>> a = Permutation(a); b = Permutation(b)
    >>> list(a*b)
    [2, 0, 1]
    >>> [b(a(i)) for i in range(3)]
    [2, 0, 1]

    See Also
    ========

    rmul, _af_rmul
    '''
    pass
# WARNING: Decompyle incomplete


def _af_parity(pi):
    '''
    Computes the parity of a permutation in array form.

    Explanation
    ===========

    The parity of a permutation reflects the parity of the
    number of inversions in the permutation, i.e., the
    number of pairs of x and y such that x > y but p[x] < p[y].

    Examples
    ========

    >>> from sympy.combinatorics.permutations import _af_parity
    >>> _af_parity([0, 1, 2, 3])
    0
    >>> _af_parity([3, 2, 0, 1])
    1

    See Also
    ========

    Permutation
    '''
    n = len(pi)
    a = [
        0] * n
    c = 0
# WARNING: Decompyle incomplete


def _af_invert(a):
    '''
    Finds the inverse, ~A, of a permutation, A, given in array form.

    Examples
    ========

    >>> from sympy.combinatorics.permutations import _af_invert, _af_rmul
    >>> A = [1, 2, 0, 3]
    >>> _af_invert(A)
    [2, 0, 1, 3]
    >>> _af_rmul(_, A)
    [0, 1, 2, 3]

    See Also
    ========

    Permutation, __invert__
    '''
    inv_form = [
        0] * len(a)
    for i, ai in enumerate(a):
        inv_form[ai] = i
        return inv_form


def _af_pow(a, n):
    '''
    Routine for finding powers of a permutation.

    Examples
    ========

    >>> from sympy.combinatorics import Permutation
    >>> from sympy.combinatorics.permutations import _af_pow
    >>> p = Permutation([2, 0, 3, 1])
    >>> p.order()
    4
    >>> _af_pow(p._array_form, 4)
    [0, 1, 2, 3]
    '''
    pass
# WARNING: Decompyle incomplete


def _af_commutes_with(a, b):
    '''
    Checks if the two permutations with array forms
    given by ``a`` and ``b`` commute.

    Examples
    ========

    >>> from sympy.combinatorics.permutations import _af_commutes_with
    >>> _af_commutes_with([1, 2, 0], [0, 2, 1])
    False

    See Also
    ========

    Permutation, commutes_with
    '''
    pass
# WARNING: Decompyle incomplete


class Cycle(dict):
    '''
    Wrapper around dict which provides the functionality of a disjoint cycle.

    Explanation
    ===========

    A cycle shows the rule to use to move subsets of elements to obtain
    a permutation. The Cycle class is more flexible than Permutation in
    that 1) all elements need not be present in order to investigate how
    multiple cycles act in sequence and 2) it can contain singletons:

    >>> from sympy.combinatorics.permutations import Perm, Cycle

    A Cycle will automatically parse a cycle given as a tuple on the rhs:

    >>> Cycle(1, 2)(2, 3)
    (1 3 2)

    The identity cycle, Cycle(), can be used to start a product:

    >>> Cycle()(1, 2)(2, 3)
    (1 3 2)

    The array form of a Cycle can be obtained by calling the list
    method (or passing it to the list function) and all elements from
    0 will be shown:

    >>> a = Cycle(1, 2)
    >>> a.list()
    [0, 2, 1]
    >>> list(a)
    [0, 2, 1]

    If a larger (or smaller) range is desired use the list method and
    provide the desired size -- but the Cycle cannot be truncated to
    a size smaller than the largest element that is out of place:

    >>> b = Cycle(2, 4)(1, 2)(3, 1, 4)(1, 3)
    >>> b.list()
    [0, 2, 1, 3, 4]
    >>> b.list(b.size + 1)
    [0, 2, 1, 3, 4, 5]
    >>> b.list(-1)
    [0, 2, 1]

    Singletons are not shown when printing with one exception: the largest
    element is always shown -- as a singleton if necessary:

    >>> Cycle(1, 4, 10)(4, 5)
    (1 5 4 10)
    >>> Cycle(1, 2)(4)(5)(10)
    (1 2)(10)

    The array form can be used to instantiate a Permutation so other
    properties of the permutation can be investigated:

    >>> Perm(Cycle(1, 2)(3, 4).list()).transpositions()
    [(1, 2), (3, 4)]

    Notes
    =====

    The underlying structure of the Cycle is a dictionary and although
    the __iter__ method has been redefined to give the array form of the
    cycle, the underlying dictionary items are still available with the
    such methods as items():

    >>> list(Cycle(1, 2).items())
    [(1, 2), (2, 1)]

    See Also
    ========

    Permutation
    '''
    
    def __missing__(self, arg):
        '''Enter arg into dictionary and return arg.'''
        return as_int(arg)

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, *other):
        '''Return product of cycles processed from R to L.

        Examples
        ========

        >>> from sympy.combinatorics import Cycle
        >>> Cycle(1, 2)(2, 3)
        (1 3 2)

        An instance of a Cycle will automatically parse list-like
        objects and Permutations that are on the right. It is more
        flexible than the Permutation in that all elements need not
        be present:

        >>> a = Cycle(1, 2)
        >>> a(2, 3)
        (1 3 2)
        >>> a(2, 3)(4, 5)
        (1 3 2)(4 5)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def list(self, size = (None,)):
        '''Return the cycles as an explicit list starting from 0 up
        to the greater of the largest value in the cycles and size.

        Truncation of trailing unmoved items will occur when size
        is less than the maximum element in the cycle; if this is
        desired, setting ``size=-1`` will guarantee such trimming.

        Examples
        ========

        >>> from sympy.combinatorics import Cycle
        >>> p = Cycle(2, 3)(4, 5)
        >>> p.list()
        [0, 1, 3, 2, 5, 4]
        >>> p.list(10)
        [0, 1, 3, 2, 5, 4, 6, 7, 8, 9]

        Passing a length too small will trim trailing, unchanged elements
        in the permutation:

        >>> Cycle(2, 4)(1, 2, 4).list(-1)
        [0, 2, 1]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        '''We want it to print as a Cycle, not as a dict.

        Examples
        ========

        >>> from sympy.combinatorics import Cycle
        >>> Cycle(1, 2)
        (1 2)
        >>> print(_)
        (1 2)
        >>> list(Cycle(1, 2).items())
        [(1, 2), (2, 1)]
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self):
        '''We want it to be printed in a Cycle notation with no
        comma in-between.

        Examples
        ========

        >>> from sympy.combinatorics import Cycle
        >>> Cycle(1, 2)
        (1 2)
        >>> Cycle(1, 2, 4)(5, 6)
        (1 2 4)(5 6)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self, *args):
        '''Load up a Cycle instance with the values for the cycle.

        Examples
        ========

        >>> from sympy.combinatorics import Cycle
        >>> Cycle(1, 2, 6)
        (1 2 6)
        '''
        if not args:
            return None
    # WARNING: Decompyle incomplete

    size = (lambda self: if not self:
0None(self.keys()) + 1)()
    
    def copy(self):
        return Cycle(self)



class Permutation(Atom):
    pass
# WARNING: Decompyle incomplete


def _merge(arr, temp, left, mid, right):
    '''
    Merges two sorted arrays and calculates the inversion count.

    Helper function for calculating inversions. This method is
    for internal use only.
    '''
    i = left
    k = left
    j = mid
    inv_count = 0
# WARNING: Decompyle incomplete

Perm = Permutation
_af_new = Perm._af_new

class AppliedPermutation(Expr):
    pass
# WARNING: Decompyle incomplete

_eval_is_eq = (lambda lhs, rhs: if lhs._size != rhs._size:
NoneNone._array_form == rhs._array_form)()
