# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: immutable.pyc (Python 3.11)

from mpmath.matrices.matrices import _matrix
from sympy.core import Basic, Dict, Tuple
from sympy.core.numbers import Integer
from sympy.core.cache import cacheit
from sympy.core.sympify import _sympy_converter as sympify_converter, _sympify
from sympy.matrices.dense import DenseMatrix
from sympy.matrices.expressions import MatrixExpr
from sympy.matrices.matrixbase import MatrixBase
from sympy.matrices.repmatrix import RepMatrix
from sympy.matrices.sparse import SparseRepMatrix
from sympy.multipledispatch import dispatch

def sympify_matrix(arg):
    return arg.as_immutable()

sympify_converter[MatrixBase] = sympify_matrix

def sympify_mpmath_matrix(arg):
    mat = arg()
    return ImmutableDenseMatrix(arg.rows, arg.cols, mat)

sympify_converter[_matrix] = sympify_mpmath_matrix

class ImmutableRepMatrix(MatrixExpr, RepMatrix):
    pass
# WARNING: Decompyle incomplete


class ImmutableDenseMatrix(ImmutableRepMatrix, DenseMatrix):
    '''Create an immutable version of a matrix.

    Examples
    ========

    >>> from sympy import eye, ImmutableMatrix
    >>> ImmutableMatrix(eye(3))
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> _[0, 0] = 42
    Traceback (most recent call last):
    ...
    TypeError: Cannot set values of ImmutableDenseMatrix
    '''
    _iterable = True
    _class_priority = 8
    _op_priority = 10.001
    _new = (lambda cls: if len(args) == 1 and isinstance(args[0], ImmutableDenseMatrix):
args[0]if None.get('copy', True) is False:
if len(args) != 3:
raise TypeError("'copy=False' requires a matrix be initialized as rows,cols,[list]")(rows, cols, flat_list) = args# WARNING: Decompyle incomplete
)()
    _fromrep = (lambda cls, rep: (rows, cols) = rep.shapeflat_list = rep.to_sympy().to_list_flat()# WARNING: Decompyle incomplete
)()

ImmutableMatrix = ImmutableDenseMatrix

class ImmutableSparseMatrix(ImmutableRepMatrix, SparseRepMatrix):
    '''Create an immutable version of a sparse matrix.

    Examples
    ========

    >>> from sympy import eye, ImmutableSparseMatrix
    >>> ImmutableSparseMatrix(1, 1, {})
    Matrix([[0]])
    >>> ImmutableSparseMatrix(eye(3))
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> _[0, 0] = 42
    Traceback (most recent call last):
    ...
    TypeError: Cannot set values of ImmutableSparseMatrix
    >>> _.shape
    (3, 3)
    '''
    is_Matrix = True
    _class_priority = 9
    _new = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    _fromrep = (lambda cls, rep: (rows, cols) = rep.shapesmat = rep.to_sympy().to_dok()obj = Basic.__new__(cls, Integer(rows), Integer(cols), Dict(smat))obj._rows = rowsobj._cols = colsobj._rep = repobj)()

_eval_is_eq = (lambda lhs, rhs: if lhs.shape != rhs.shape:
False(None - rhs).is_zero_matrix)()
