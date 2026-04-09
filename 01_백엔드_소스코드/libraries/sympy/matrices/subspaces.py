# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: subspaces.pyc (Python 3.11)

from utilities import _iszero

def _columnspace(M, simplify = (False,)):
    '''Returns a list of vectors (Matrix objects) that span columnspace of ``M``

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix(3, 3, [1, 3, 0, -2, -6, 0, 3, 9, 6])
    >>> M
    Matrix([
    [ 1,  3, 0],
    [-2, -6, 0],
    [ 3,  9, 6]])
    >>> M.columnspace()
    [Matrix([
    [ 1],
    [-2],
    [ 3]]), Matrix([
    [0],
    [0],
    [6]])]

    See Also
    ========

    nullspace
    rowspace
    '''
    pass
# WARNING: Decompyle incomplete


def _nullspace(M, simplify, iszerofunc = (False, _iszero)):
    '''Returns list of vectors (Matrix objects) that span nullspace of ``M``

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix(3, 3, [1, 3, 0, -2, -6, 0, 3, 9, 6])
    >>> M
    Matrix([
    [ 1,  3, 0],
    [-2, -6, 0],
    [ 3,  9, 6]])
    >>> M.nullspace()
    [Matrix([
    [-3],
    [ 1],
    [ 0]])]

    See Also
    ========

    columnspace
    rowspace
    '''
    pass
# WARNING: Decompyle incomplete


def _rowspace(M, simplify = (False,)):
    '''Returns a list of vectors that span the row space of ``M``.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix(3, 3, [1, 3, 0, -2, -6, 0, 3, 9, 6])
    >>> M
    Matrix([
    [ 1,  3, 0],
    [-2, -6, 0],
    [ 3,  9, 6]])
    >>> M.rowspace()
    [Matrix([[1, 3, 0]]), Matrix([[0, 0, 6]])]
    '''
    pass
# WARNING: Decompyle incomplete


def _orthogonalize(cls = None, *, normalize, rankcheck, *vecs):
    '''Apply the Gram-Schmidt orthogonalization procedure
    to vectors supplied in ``vecs``.

    Parameters
    ==========

    vecs
        vectors to be made orthogonal

    normalize : bool
        If ``True``, return an orthonormal basis.

    rankcheck : bool
        If ``True``, the computation does not stop when encountering
        linearly dependent vectors.

        If ``False``, it will raise ``ValueError`` when any zero
        or linearly dependent vectors are found.

    Returns
    =======

    list
        List of orthogonal (or orthonormal) basis vectors.

    Examples
    ========

    >>> from sympy import I, Matrix
    >>> v = [Matrix([1, I]), Matrix([1, -I])]
    >>> Matrix.orthogonalize(*v)
    [Matrix([
    [1],
    [I]]), Matrix([
    [ 1],
    [-I]])]

    See Also
    ========

    MatrixBase.QRdecomposition

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gram%E2%80%93Schmidt_process
    '''
    _QRdecomposition_optional = _QRdecomposition_optional
    import decompositions
    if not vecs:
        return []
    all_row_vecs = None[0].rows == 1
    vecs = vecs()
# WARNING: Decompyle incomplete
