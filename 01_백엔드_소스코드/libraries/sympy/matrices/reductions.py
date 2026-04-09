# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reductions.pyc (Python 3.11)

from types import FunctionType
from sympy.polys.polyerrors import CoercionFailed
from sympy.polys.domains import ZZ, QQ
from utilities import _get_intermediate_simp, _iszero, _dotprodsimp, _simplify
from determinant import _find_reasonable_pivot

def _row_reduce_list(mat, rows, cols, one, iszerofunc, simpfunc, normalize_last, normalize, zero_above = (True, True, True)):
    '''Row reduce a flat list representation of a matrix and return a tuple
    (rref_matrix, pivot_cols, swaps) where ``rref_matrix`` is a flat list,
    ``pivot_cols`` are the pivot columns and ``swaps`` are any row swaps that
    were used in the process of row reduction.

    Parameters
    ==========

    mat : list
        list of matrix elements, must be ``rows`` * ``cols`` in length

    rows, cols : integer
        number of rows and columns in flat list representation

    one : SymPy object
        represents the value one, from ``Matrix.one``

    iszerofunc : determines if an entry can be used as a pivot

    simpfunc : used to simplify elements and test if they are
        zero if ``iszerofunc`` returns `None`

    normalize_last : indicates where all row reduction should
        happen in a fraction-free manner and then the rows are
        normalized (so that the pivots are 1), or whether
        rows should be normalized along the way (like the naive
        row reduction algorithm)

    normalize : whether pivot rows should be normalized so that
        the pivot value is 1

    zero_above : whether entries above the pivot should be zeroed.
        If ``zero_above=False``, an echelon matrix will be returned.
    '''
    pass
# WARNING: Decompyle incomplete


def _row_reduce(M, iszerofunc, simpfunc, normalize_last, normalize, zero_above = (True, True, True)):
    (mat, pivot_cols, swaps) = _row_reduce_list(list(M), M.rows, M.cols, M.one, iszerofunc, simpfunc, normalize_last = normalize_last, normalize = normalize, zero_above = zero_above)
    return (M._new(M.rows, M.cols, mat), pivot_cols, swaps)


def _is_echelon(M, iszerofunc = (_iszero,)):
    '''Returns `True` if the matrix is in echelon form. That is, all rows of
    zeros are at the bottom, and below each leading non-zero in a row are
    exclusively zeros.'''
    pass
# WARNING: Decompyle incomplete


def _echelon_form(M, iszerofunc, simplify, with_pivots = (_iszero, False, False)):
    '''Returns a matrix row-equivalent to ``M`` that is in echelon form. Note
    that echelon form of a matrix is *not* unique, however, properties like the
    row space and the null space are preserved.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> M.echelon_form()
    Matrix([
    [1,  2],
    [0, -2]])
    '''
    simpfunc = simplify if isinstance(simplify, FunctionType) else _simplify
    (mat, pivots, _) = _row_reduce(M, iszerofunc, simpfunc, normalize_last = True, normalize = False, zero_above = False)
    if with_pivots:
        return (mat, pivots)


def _rank(M, iszerofunc, simplify = (_iszero, False)):
    '''Returns the rank of a matrix.

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.abc import x
    >>> m = Matrix([[1, 2], [x, 1 - 1/x]])
    >>> m.rank()
    2
    >>> n = Matrix(3, 3, range(1, 10))
    >>> n.rank()
    2
    '''
    pass
# WARNING: Decompyle incomplete


def _to_DM_ZZ_QQ(M):
    if not hasattr(M, '_rep'):
        return None
    rep = None._rep
    K = rep.domain
    if K.is_ZZ:
        return rep
    if None.is_QQ:
        
        try:
            return rep.convert_to(ZZ)
        except CoercionFailed:
            return 
            if not (lambda .0: pass# WARNING: Decompyle incomplete
)(M()):
                return None
            
            try:
                return rep.convert_to(ZZ)
            except CoercionFailed:
                return 




def _rref_dm(dM):
    '''Compute the reduced row echelon form of a DomainMatrix.'''
    K = dM.domain
    if K.is_ZZ:
        (dM_rref, den, pivots) = dM.rref_den(keep_domain = False)
        dM_rref = dM_rref.to_field() / den
    elif K.is_QQ:
        (dM_rref, pivots) = dM.rref()
# WARNING: Decompyle incomplete


def _rref(M, iszerofunc, simplify, pivots, normalize_last = (_iszero, False, True, True)):
    """Return reduced row-echelon form of matrix and indices
    of pivot vars.

    Parameters
    ==========

    iszerofunc : Function
        A function used for detecting whether an element can
        act as a pivot.  ``lambda x: x.is_zero`` is used by default.

    simplify : Function
        A function used to simplify elements when looking for a pivot.
        By default SymPy's ``simplify`` is used.

    pivots : True or False
        If ``True``, a tuple containing the row-reduced matrix and a tuple
        of pivot columns is returned.  If ``False`` just the row-reduced
        matrix is returned.

    normalize_last : True or False
        If ``True``, no pivots are normalized to `1` until after all
        entries above and below each pivot are zeroed.  This means the row
        reduction algorithm is fraction free until the very last step.
        If ``False``, the naive row reduction procedure is used where
        each pivot is normalized to be `1` before row operations are
        used to zero above and below the pivot.

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.abc import x
    >>> m = Matrix([[1, 2], [x, 1 - 1/x]])
    >>> m.rref()
    (Matrix([
    [1, 0],
    [0, 1]]), (0, 1))
    >>> rref_matrix, rref_pivots = m.rref()
    >>> rref_matrix
    Matrix([
    [1, 0],
    [0, 1]])
    >>> rref_pivots
    (0, 1)

    ``iszerofunc`` can correct rounding errors in matrices with float
    values. In the following example, calling ``rref()`` leads to
    floating point errors, incorrectly row reducing the matrix.
    ``iszerofunc= lambda x: abs(x) < 1e-9`` sets sufficiently small numbers
    to zero, avoiding this error.

    >>> m = Matrix([[0.9, -0.1, -0.2, 0], [-0.8, 0.9, -0.4, 0], [-0.1, -0.8, 0.6, 0]])
    >>> m.rref()
    (Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0]]), (0, 1, 2))
    >>> m.rref(iszerofunc=lambda x:abs(x)<1e-9)
    (Matrix([
    [1, 0, -0.301369863013699, 0],
    [0, 1, -0.712328767123288, 0],
    [0, 0,         0,          0]]), (0, 1))

    Notes
    =====

    The default value of ``normalize_last=True`` can provide significant
    speedup to row reduction, especially on matrices with symbols.  However,
    if you depend on the form row reduction algorithm leaves entries
    of the matrix, set ``normalize_last=False``
    """
    dM = _to_DM_ZZ_QQ(M)
# WARNING: Decompyle incomplete
