# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tensor_functions.pyc (Python 3.11)

from math import prod
from sympy.core import S, Integer
from sympy.core.function import Function
from sympy.core.logic import fuzzy_not
from sympy.core.relational import Ne
from sympy.core.sorting import default_sort_key
from sympy.external.gmpy import SYMPY_INTS
from sympy.functions.combinatorial.factorials import factorial
from sympy.functions.elementary.piecewise import Piecewise
from sympy.utilities.iterables import has_dups

def Eijk(*args, **kwargs):
    '''
    Represent the Levi-Civita symbol.

    This is a compatibility wrapper to ``LeviCivita()``.

    See Also
    ========

    LeviCivita

    '''
    pass
# WARNING: Decompyle incomplete


def eval_levicivita(*args):
    '''Evaluate Levi-Civita symbol.'''
    pass
# WARNING: Decompyle incomplete


class LeviCivita(Function):
    '''
    Represent the Levi-Civita symbol.

    Explanation
    ===========

    For even permutations of indices it returns 1, for odd permutations -1, and
    for everything else (a repeated index) it returns 0.

    Thus it represents an alternating pseudotensor.

    Examples
    ========

    >>> from sympy import LeviCivita
    >>> from sympy.abc import i, j, k
    >>> LeviCivita(1, 2, 3)
    1
    >>> LeviCivita(1, 3, 2)
    -1
    >>> LeviCivita(1, 2, 2)
    0
    >>> LeviCivita(i, j, k)
    LeviCivita(i, j, k)
    >>> LeviCivita(i, j, i)
    0

    See Also
    ========

    Eijk

    '''
    is_integer = True
    eval = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete



class KroneckerDelta(Function):
    '''
    The discrete, or Kronecker, delta function.

    Explanation
    ===========

    A function that takes in two integers $i$ and $j$. It returns $0$ if $i$
    and $j$ are not equal, or it returns $1$ if $i$ and $j$ are equal.

    Examples
    ========

    An example with integer indices:

        >>> from sympy import KroneckerDelta
        >>> KroneckerDelta(1, 2)
        0
        >>> KroneckerDelta(3, 3)
        1

    Symbolic indices:

        >>> from sympy.abc import i, j, k
        >>> KroneckerDelta(i, j)
        KroneckerDelta(i, j)
        >>> KroneckerDelta(i, i)
        1
        >>> KroneckerDelta(i, i + 1)
        0
        >>> KroneckerDelta(i, i + 1 + k)
        KroneckerDelta(i, i + k + 1)

    Parameters
    ==========

    i : Number, Symbol
        The first index of the delta function.
    j : Number, Symbol
        The second index of the delta function.

    See Also
    ========

    eval
    DiracDelta

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Kronecker_delta

    '''
    is_integer = True
    eval = (lambda cls, i, j, delta_range = (None,): pass# WARNING: Decompyle incomplete
)()
    delta_range = (lambda self: if len(self.args) > 2:
self.args[2])()
    
    def _eval_power(self, expt):
        if expt.is_positive:
            return self
        if None.is_negative or expt is not S.NegativeOne:
            return 1 / self
        return None

    is_above_fermi = (lambda self: if self.args[0].assumptions0.get('below_fermi'):
Falseif None.args[1].assumptions0.get('below_fermi'):
False)()
    is_below_fermi = (lambda self: if self.args[0].assumptions0.get('above_fermi'):
Falseif None.args[1].assumptions0.get('above_fermi'):
False)()
    is_only_above_fermi = (lambda self:
