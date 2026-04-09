# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: blockmatrix.pyc (Python 3.11)

from sympy.assumptions.ask import Q, ask
from sympy.core import Basic, Add, Mul, S
from sympy.core.sympify import _sympify
from sympy.functions import adjoint
from sympy.functions.elementary.complexes import re, im
from sympy.strategies import typed, exhaust, condition, do_one, unpack
from sympy.strategies.traverse import bottom_up
from sympy.utilities.iterables import is_sequence, sift
from sympy.utilities.misc import filldedent
from sympy.matrices import Matrix, ShapeError
from sympy.matrices.exceptions import NonInvertibleMatrixError
from sympy.matrices.expressions.determinant import det, Determinant
from sympy.matrices.expressions.inverse import Inverse
from sympy.matrices.expressions.matadd import MatAdd
from sympy.matrices.expressions.matexpr import MatrixExpr, MatrixElement
from sympy.matrices.expressions.matmul import MatMul
from sympy.matrices.expressions.matpow import MatPow
from sympy.matrices.expressions.slice import MatrixSlice
from sympy.matrices.expressions.special import ZeroMatrix, Identity
from sympy.matrices.expressions.trace import trace
from sympy.matrices.expressions.transpose import Transpose, transpose

class BlockMatrix(MatrixExpr):
    pass
# WARNING: Decompyle incomplete


class BlockDiagMatrix(BlockMatrix):
    """A sparse matrix with block matrices along its diagonals

    Examples
    ========

    >>> from sympy import MatrixSymbol, BlockDiagMatrix, symbols
    >>> n, m, l = symbols('n m l')
    >>> X = MatrixSymbol('X', n, n)
    >>> Y = MatrixSymbol('Y', m, m)
    >>> BlockDiagMatrix(X, Y)
    Matrix([
    [X, 0],
    [0, Y]])

    Notes
    =====

    If you want to get the individual diagonal blocks, use
    :meth:`get_diag_blocks`.

    See Also
    ========

    sympy.matrices.dense.diag
    """
    
    def __new__(cls, *mats):
