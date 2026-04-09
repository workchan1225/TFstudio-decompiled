# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sets.pyc (Python 3.11)

from sympy.core.assumptions import check_assumptions
from sympy.core.logic import fuzzy_and
from sympy.core.sympify import _sympify
from sympy.matrices.kind import MatrixKind
from sympy.sets.sets import Set, SetKind
from sympy.core.kind import NumberKind
from matexpr import MatrixExpr

class MatrixSet(Set):
    '''
    MatrixSet represents the set of matrices with ``shape = (n, m)`` over the
    given set.

    Examples
    ========

    >>> from sympy.matrices import MatrixSet
    >>> from sympy import S, I, Matrix
    >>> M = MatrixSet(2, 2, set=S.Reals)
    >>> X = Matrix([[1, 2], [3, 4]])
    >>> X in M
    True
    >>> X = Matrix([[1, 2], [I, 4]])
    >>> X in M
    False

    '''
    is_empty = False
    
    def __new__(cls, n, m, set):
        set = _sympify(set)
        m = _sympify(m)
        n = _sympify(n)
        cls._check_dim(n)
        cls._check_dim(m)
        if not isinstance(set, Set):
            raise TypeError('{} should be an instance of Set.'.format(set))
        return Set.__new__(cls, n, m, set)

    shape = (lambda self: self.args[:2])()
    set = (lambda self: self.args[2])()
    
    def _contains(self, other):
        pass
    # WARNING: Decompyle incomplete

    _check_dim = (lambda cls, dim: if not (dim.is_Float):
passok = check_assumptions(dim, integer = True, nonnegative = True)if ok is False:
raise ValueError('The dimension specification {} should be a nonnegative integer.'.format(dim)))()
    
    def _kind(self):
        return SetKind(MatrixKind(NumberKind))
