# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kronecker.pyc (Python 3.11)

__doc__ = 'Implementation of the Kronecker product'
from functools import reduce
from math import prod
from sympy.core import Mul, sympify
from sympy.functions import adjoint
from sympy.matrices.exceptions import ShapeError
from sympy.matrices.expressions.matexpr import MatrixExpr
from sympy.matrices.expressions.transpose import transpose
from sympy.matrices.expressions.special import Identity
from sympy.matrices.matrixbase import MatrixBase
from sympy.strategies import canon, condition, distribute, do_one, exhaust, flatten, typed, unpack
from sympy.strategies.traverse import bottom_up
from sympy.utilities import sift
from matadd import MatAdd
from matmul import MatMul
from matpow import MatPow

def kronecker_product(*matrices):
    """
    The Kronecker product of two or more arguments.

    This computes the explicit Kronecker product for subclasses of
    ``MatrixBase`` i.e. explicit matrices. Otherwise, a symbolic
    ``KroneckerProduct`` object is returned.


    Examples
    ========

    For ``MatrixSymbol`` arguments a ``KroneckerProduct`` object is returned.
    Elements of this matrix can be obtained by indexing, or for MatrixSymbols
    with known dimension the explicit matrix can be obtained with
    ``.as_explicit()``

    >>> from sympy import kronecker_product, MatrixSymbol
    >>> A = MatrixSymbol('A', 2, 2)
    >>> B = MatrixSymbol('B', 2, 2)
    >>> kronecker_product(A)
    A
    >>> kronecker_product(A, B)
    KroneckerProduct(A, B)
    >>> kronecker_product(A, B)[0, 1]
    A[0, 0]*B[0, 1]
    >>> kronecker_product(A, B).as_explicit()
    Matrix([
        [A[0, 0]*B[0, 0], A[0, 0]*B[0, 1], A[0, 1]*B[0, 0], A[0, 1]*B[0, 1]],
        [A[0, 0]*B[1, 0], A[0, 0]*B[1, 1], A[0, 1]*B[1, 0], A[0, 1]*B[1, 1]],
        [A[1, 0]*B[0, 0], A[1, 0]*B[0, 1], A[1, 1]*B[0, 0], A[1, 1]*B[0, 1]],
        [A[1, 0]*B[1, 0], A[1, 0]*B[1, 1], A[1, 1]*B[1, 0], A[1, 1]*B[1, 1]]])

    For explicit matrices the Kronecker product is returned as a Matrix

    >>> from sympy import Matrix, kronecker_product
    >>> sigma_x = Matrix([
    ... [0, 1],
    ... [1, 0]])
    ...
    >>> Isigma_y = Matrix([
    ... [0, 1],
    ... [-1, 0]])
    ...
    >>> kronecker_product(sigma_x, Isigma_y)
    Matrix([
    [ 0, 0,  0, 1],
    [ 0, 0, -1, 0],
    [ 0, 1,  0, 0],
    [-1, 0,  0, 0]])

    See Also
    ========
        KroneckerProduct

    """
    if not matrices:
        raise TypeError('Empty Kronecker product is undefined')
    if len(matrices) == 1:
        return matrices[0]
# WARNING: Decompyle incomplete


class KroneckerProduct(MatrixExpr):
    pass
# WARNING: Decompyle incomplete


def validate(*args):
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(args()):
        raise TypeError('Mix of Matrix and Scalar symbols')


def extract_commutative(kron):
    c_part = []
    nc_part = []
# WARNING: Decompyle incomplete


def matrix_kronecker_product(*matrices):
    '''Compute the Kronecker product of a sequence of SymPy Matrices.

    This is the standard Kronecker product of matrices [1].

    Parameters
    ==========

    matrices : tuple of MatrixBase instances
        The matrices to take the Kronecker product of.

    Returns
    =======

    matrix : MatrixBase
        The Kronecker product matrix.

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.matrices.expressions.kronecker import (
    ... matrix_kronecker_product)

    >>> m1 = Matrix([[1,2],[3,4]])
    >>> m2 = Matrix([[1,0],[0,1]])
    >>> matrix_kronecker_product(m1, m2)
    Matrix([
    [1, 0, 2, 0],
    [0, 1, 0, 2],
    [3, 0, 4, 0],
    [0, 3, 0, 4]])
    >>> matrix_kronecker_product(m2, m1)
    Matrix([
    [1, 2, 0, 0],
    [3, 4, 0, 0],
    [0, 0, 1, 2],
    [0, 0, 3, 4]])

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Kronecker_product
    '''
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(matrices()):
        raise TypeError('Sequence of Matrices expected, got: %s' % repr(matrices))
    matrix_expansion = matrices[-1]
    for mat in reversed(matrices[:-1]):
        rows = mat.rows
        cols = mat.cols
        for i in range(rows):
            start = matrix_expansion * mat[i * cols]
            for j in range(cols - 1):
                start = start.row_join(matrix_expansion * mat[i * cols + j + 1])
                if i == 0:
                    next = start
                    continue
            next = next.col_join(start)
            matrix_expansion = next
            MatrixClass = max(matrices, key = (lambda M: M._class_priority)).__class__
            if isinstance(matrix_expansion, MatrixClass):
                return matrix_expansion
            return MatrixClass(matrix_expansion)


def explicit_kronecker_product(kron):
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(kron.args()):
        return kron
# WARNING: Decompyle incomplete

rules = (unpack, explicit_kronecker_product, flatten, extract_commutative)
# WARNING: Decompyle incomplete
