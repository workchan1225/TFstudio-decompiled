# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: diagonal.pyc (Python 3.11)

from sympy.core.sympify import _sympify
from sympy.matrices.expressions import MatrixExpr
from sympy.core import S, Eq, Ge
from sympy.core.mul import Mul
from sympy.functions.special.tensor_functions import KroneckerDelta

class DiagonalMatrix(MatrixExpr):
    """DiagonalMatrix(M) will create a matrix expression that
    behaves as though all off-diagonal elements,
    `M[i, j]` where `i != j`, are zero.

    Examples
    ========

    >>> from sympy import MatrixSymbol, DiagonalMatrix, Symbol
    >>> n = Symbol('n', integer=True)
    >>> m = Symbol('m', integer=True)
    >>> D = DiagonalMatrix(MatrixSymbol('x', 2, 3))
    >>> D[1, 2]
    0
    >>> D[1, 1]
    x[1, 1]

    The length of the diagonal -- the lesser of the two dimensions of `M` --
    is accessed through the `diagonal_length` property:

    >>> D.diagonal_length
    2
    >>> DiagonalMatrix(MatrixSymbol('x', n + 1, n)).diagonal_length
    n

    When one of the dimensions is symbolic the other will be treated as
    though it is smaller:

    >>> tall = DiagonalMatrix(MatrixSymbol('x', n, 3))
    >>> tall.diagonal_length
    3
    >>> tall[10, 1]
    0

    When the size of the diagonal is not known, a value of None will
    be returned:

    >>> DiagonalMatrix(MatrixSymbol('x', n, m)).diagonal_length is None
    True

    """
    arg = property((lambda self: self.args[0]))
    shape = property((lambda self: self.arg.shape))
    diagonal_length = (lambda self: (r, c) = self.shapeif r.is_Integer and c.is_Integer:
m = min(r, c)elif not r.is_Integer and c.is_Integer:
m = relif not c.is_Integer and r.is_Integer:
m = celif r == c:
m = relse:
try:
m = min(r, c)except TypeError:
m = Nonem)()
    
    def _entry(self, i, j, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class DiagonalOf(MatrixExpr):
    """DiagonalOf(M) will create a matrix expression that
    is equivalent to the diagonal of `M`, represented as
    a single column matrix.

    Examples
    ========

    >>> from sympy import MatrixSymbol, DiagonalOf, Symbol
    >>> n = Symbol('n', integer=True)
    >>> m = Symbol('m', integer=True)
    >>> x = MatrixSymbol('x', 2, 3)
    >>> diag = DiagonalOf(x)
    >>> diag.shape
    (2, 1)

    The diagonal can be addressed like a matrix or vector and will
    return the corresponding element of the original matrix:

    >>> diag[1, 0] == diag[1] == x[1, 1]
    True

    The length of the diagonal -- the lesser of the two dimensions of `M` --
    is accessed through the `diagonal_length` property:

    >>> diag.diagonal_length
    2
    >>> DiagonalOf(MatrixSymbol('x', n + 1, n)).diagonal_length
    n

    When only one of the dimensions is symbolic the other will be
    treated as though it is smaller:

    >>> dtall = DiagonalOf(MatrixSymbol('x', n, 3))
    >>> dtall.diagonal_length
    3

    When the size of the diagonal is not known, a value of None will
    be returned:

    >>> DiagonalOf(MatrixSymbol('x', n, m)).diagonal_length is None
    True

    """
    arg = property((lambda self: self.args[0]))
    shape = (lambda self: (r, c) = self.arg.shapeif r.is_Integer and c.is_Integer:
m = min(r, c)elif not r.is_Integer and c.is_Integer:
m = relif not c.is_Integer and r.is_Integer:
m = celif r == c:
m = relse:
try:
m = min(r, c)except TypeError:
m = None(m, S.One))()
    diagonal_length = (lambda self: self.shape[0])()
    
    def _entry(self, i, j, **kwargs):
        pass
    # WARNING: Decompyle incomplete



class DiagMatrix(MatrixExpr):
    '''
    Turn a vector into a diagonal matrix.
    '''
    
    def __new__(cls, vector):
        vector = _sympify(vector)
        obj = MatrixExpr.__new__(cls, vector)
        shape = vector.shape
        dim = shape[1] if shape[0] == 1 else shape[0]
        if vector.shape[0] != 1:
            obj._iscolumn = True
        else:
            obj._iscolumn = False
        obj._shape = (dim, dim)
        obj._vector = vector
        return obj

    shape = (lambda self: self._shape)()
    
    def _entry(self, i, j, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_transpose(self):
        return self

    
    def as_explicit(self):
        diag = diag
        import sympy.matrices.dense
    # WARNING: Decompyle incomplete

    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete



def diagonalize_vector(vector):
    return DiagMatrix(vector).doit()
