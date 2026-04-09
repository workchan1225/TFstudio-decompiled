# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _shape.pyc (Python 3.11)

from sympy.core.relational import Eq
from sympy.core.expr import Expr
from sympy.core.numbers import Integer
from sympy.logic.boolalg import Boolean, And
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.exceptions import ShapeError
from typing import Union

def is_matadd_valid(*args):
    """Return the symbolic condition how ``MatAdd``, ``HadamardProduct``
    makes sense.

    Parameters
    ==========

    args
        The list of arguments of matrices to be tested for.

    Examples
    ========

    >>> from sympy import MatrixSymbol, symbols
    >>> from sympy.matrices.expressions._shape import is_matadd_valid

    >>> m, n, p, q = symbols('m n p q')
    >>> A = MatrixSymbol('A', m, n)
    >>> B = MatrixSymbol('B', p, q)
    >>> is_matadd_valid(A, B)
    Eq(m, p) & Eq(n, q)
    """
    pass
# WARNING: Decompyle incomplete


def is_matmul_valid(*args):
    """Return the symbolic condition how ``MatMul`` makes sense

    Parameters
    ==========

    args
        The list of arguments of matrices and scalar expressions to be tested
        for.

    Examples
    ========

    >>> from sympy import MatrixSymbol, symbols
    >>> from sympy.matrices.expressions._shape import is_matmul_valid

    >>> m, n, p, q = symbols('m n p q')
    >>> A = MatrixSymbol('A', m, n)
    >>> B = MatrixSymbol('B', p, q)
    >>> is_matmul_valid(A, B)
    Eq(n, p)
    """
    pass
# WARNING: Decompyle incomplete


def is_square(arg = None):
    """Return the symbolic condition how the matrix is assumed to be square

    Parameters
    ==========

    arg
        The matrix to be tested for.

    Examples
    ========

    >>> from sympy import MatrixSymbol, symbols
    >>> from sympy.matrices.expressions._shape import is_square

    >>> m, n = symbols('m n')
    >>> A = MatrixSymbol('A', m, n)
    >>> is_square(A)
    Eq(m, n)
    """
    return Eq(arg.rows, arg.cols)


def validate_matadd_integer(*args):
    '''Validate matrix shape for addition only for integer values'''
    pass
# WARNING: Decompyle incomplete


def validate_matmul_integer(*args):
    '''Validate matrix shape for multiplication only for integer values'''
    for A, B in zip(args[:-1], args[1:]):
        j = B.rows
        i = A.cols
        if isinstance(i, (int, Integer)) and isinstance(j, (int, Integer)) and i != j:
            raise ShapeError('Matrices are not aligned', i, j)
        return None
