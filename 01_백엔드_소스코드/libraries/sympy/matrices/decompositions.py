# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decompositions.pyc (Python 3.11)

import copy
from sympy.core import S
from sympy.core.function import expand_mul
from sympy.functions.elementary.miscellaneous import Min, sqrt
from sympy.functions.elementary.complexes import sign
from exceptions import NonSquareMatrixError, NonPositiveDefiniteMatrixError
from utilities import _get_intermediate_simp, _iszero
from determinant import _find_reasonable_pivot_naive

def _rank_decomposition(M, iszerofunc, simplify = (_iszero, False)):
    '''Returns a pair of matrices (`C`, `F`) with matching rank
    such that `A = C F`.

    Parameters
    ==========

    iszerofunc : Function, optional
        A function used for detecting whether an element can
        act as a pivot.  ``lambda x: x.is_zero`` is used by default.

    simplify : Bool or Function, optional
        A function used to simplify elements when looking for a
        pivot. By default SymPy\'s ``simplify`` is used.

    Returns
    =======

    (C, F) : Matrices
        `C` and `F` are full-rank matrices with rank as same as `A`,
        whose product gives `A`.

        See Notes for additional mathematical details.

    Examples
    ========

    >>> from sympy import Matrix
    >>> A = Matrix([
    ...     [1, 3, 1, 4],
    ...     [2, 7, 3, 9],
    ...     [1, 5, 3, 1],
    ...     [1, 2, 0, 8]
    ... ])
    >>> C, F = A.rank_decomposition()
    >>> C
    Matrix([
    [1, 3, 4],
    [2, 7, 9],
    [1, 5, 1],
    [1, 2, 8]])
    >>> F
    Matrix([
    [1, 0, -2, 0],
    [0, 1,  1, 0],
    [0, 0,  0, 1]])
    >>> C * F == A
    True

    Notes
    =====

    Obtaining `F`, an RREF of `A`, is equivalent to creating a
    product

    .. math::
        E_n E_{n-1} ... E_1 A = F

    where `E_n, E_{n-1}, \\dots, E_1` are the elimination matrices or
    permutation matrices equivalent to each row-reduction step.

    The inverse of the same product of elimination matrices gives
    `C`:

    .. math::
        C = \\left(E_n E_{n-1} \\dots E_1\\right)^{-1}

    It is not necessary, however, to actually compute the inverse:
    the columns of `C` are those from the original matrix with the
    same column indices as the indices of the pivot columns of `F`.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Rank_factorization

    .. [2] Piziak, R.; Odell, P. L. (1 June 1999).
        "Full Rank Factorization of Matrices".
        Mathematics Magazine. 72 (3): 193. doi:10.2307/2690882

    See Also
    ========

    sympy.matrices.matrixbase.MatrixBase.rref
    '''
    (F, pivot_cols) = M.rref(simplify = simplify, iszerofunc = iszerofunc, pivots = True)
    rank = len(pivot_cols)
    C = M.extract(range(M.rows), pivot_cols)
    F = F[(:rank, :)]
    return (C, F)


def _liupc(M):
    """Liu's algorithm, for pre-determination of the Elimination Tree of
    the given matrix, used in row-based symbolic Cholesky factorization.

    Examples
    ========

    >>> from sympy import SparseMatrix
    >>> S = SparseMatrix([
    ... [1, 0, 3, 2],
    ... [0, 0, 1, 0],
    ... [4, 0, 0, 5],
    ... [0, 6, 7, 0]])
    >>> S.liupc()
    ([[0], [], [0], [1, 2]], [4, 3, 4, 4])

    References
    ==========

    .. [1] Symbolic Sparse Cholesky Factorization using Elimination Trees,
           Jeroen Van Grondelle (1999)
           https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.39.7582
    """
    R = range(M.rows)()
# WARNING: Decompyle incomplete


def _row_structure_symbolic_cholesky(M):
    '''Symbolic cholesky factorization, for pre-determination of the
    non-zero structure of the Cholesky factororization.

    Examples
    ========

    >>> from sympy import SparseMatrix
    >>> S = SparseMatrix([
    ... [1, 0, 3, 2],
    ... [0, 0, 1, 0],
    ... [4, 0, 0, 5],
    ... [0, 6, 7, 0]])
    >>> S.row_structure_symbolic_cholesky()
    [[0], [], [0], [1, 2]]

    References
    ==========

    .. [1] Symbolic Sparse Cholesky Factorization using Elimination Trees,
           Jeroen Van Grondelle (1999)
           https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.39.7582
    '''
    (R, parent) = M.liupc()
    inf = len(R)
    Lrow = copy.deepcopy(R)
# WARNING: Decompyle incomplete


def _cholesky(M, hermitian = (True,)):
    '''Returns the Cholesky-type decomposition L of a matrix A
    such that L * L.H == A if hermitian flag is True,
    or L * L.T == A if hermitian is False.

    A must be a Hermitian positive-definite matrix if hermitian is True,
    or a symmetric matrix if it is False.

    Examples
    ========

    >>> from sympy import Matrix
    >>> A = Matrix(((25, 15, -5), (15, 18, 0), (-5, 0, 11)))
    >>> A.cholesky()
    Matrix([
    [ 5, 0, 0],
    [ 3, 3, 0],
    [-1, 1, 3]])
    >>> A.cholesky() * A.cholesky().T
    Matrix([
    [25, 15, -5],
    [15, 18,  0],
    [-5,  0, 11]])

    The matrix can have complex entries:

    >>> from sympy import I
    >>> A = Matrix(((9, 3*I), (-3*I, 5)))
    >>> A.cholesky()
    Matrix([
    [ 3, 0],
    [-I, 2]])
    >>> A.cholesky() * A.cholesky().H
    Matrix([
    [   9, 3*I],
    [-3*I,   5]])

    Non-hermitian Cholesky-type decomposition may be useful when the
    matrix is not positive-definite.

    >>> A = Matrix([[1, 2], [2, 1]])
    >>> L = A.cholesky(hermitian=False)
    >>> L
    Matrix([
    [1,         0],
    [2, sqrt(3)*I]])
    >>> L*L.T == A
    True

    See Also
    ========

    sympy.matrices.dense.DenseMatrix.LDLdecomposition
    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    QRdecomposition
    '''
    pass
# WARNING: Decompyle incomplete


def _cholesky_sparse(M, hermitian = (True,)):
    '''
    Returns the Cholesky decomposition L of a matrix A
    such that L * L.T = A

    A must be a square, symmetric, positive-definite
    and non-singular matrix

    Examples
    ========

    >>> from sympy import SparseMatrix
    >>> A = SparseMatrix(((25,15,-5),(15,18,0),(-5,0,11)))
    >>> A.cholesky()
    Matrix([
    [ 5, 0, 0],
    [ 3, 3, 0],
    [-1, 1, 3]])
    >>> A.cholesky() * A.cholesky().T == A
    True

    The matrix can have complex entries:

    >>> from sympy import I
    >>> A = SparseMatrix(((9, 3*I), (-3*I, 5)))
    >>> A.cholesky()
    Matrix([
    [ 3, 0],
    [-I, 2]])
    >>> A.cholesky() * A.cholesky().H
    Matrix([
    [   9, 3*I],
    [-3*I,   5]])

    Non-hermitian Cholesky-type decomposition may be useful when the
    matrix is not positive-definite.

    >>> A = SparseMatrix([[1, 2], [2, 1]])
    >>> L = A.cholesky(hermitian=False)
    >>> L
    Matrix([
    [1,         0],
    [2, sqrt(3)*I]])
    >>> L*L.T == A
    True

    See Also
    ========

    sympy.matrices.sparse.SparseMatrix.LDLdecomposition
    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    QRdecomposition
    '''
    MutableDenseMatrix = MutableDenseMatrix
    import dense
    if not M.is_square:
        raise NonSquareMatrixError('Matrix must be square.')
    if not hermitian and M.is_hermitian:
        raise ValueError('Matrix must be Hermitian.')
    if not hermitian and M.is_symmetric():
        raise ValueError('Matrix must be symmetric.')
    dps = _get_intermediate_simp(expand_mul, expand_mul)
    Crowstruc = M.row_structure_symbolic_cholesky()
    C = MutableDenseMatrix.zeros(M.rows)
    for i in range(len(Crowstruc)):
        for j in Crowstruc[i]:
            if i != j:
                C[(i, j)] = M[(i, j)]
                summ = 0
                for p1 in Crowstruc[i]:
                    if p1 < j:
                        for p2 in Crowstruc[j]:
                            if p2 < j:
                                if p1 == p2:
                                    if hermitian:
                                        summ += C[(i, p1)] * C[(j, p1)].conjugate()
                                        continue
                                    summ += C[(i, p1)] * C[(j, p1)]
                                continue
                    
                    C[(i, j)] = dps((C[(i, j)] - summ) / C[(j, j)])
                    C[(j, j)] = M[(j, j)]
                    summ = 0
                    for k in Crowstruc[j]:
                        if k < j:
                            if hermitian:
                                summ += C[(j, k)] * C[(j, k)].conjugate()
                                continue
                            summ += C[(j, k)] ** 2
                            continue
                        Cjj2 = dps(C[(j, j)] - summ)
                        if hermitian and Cjj2.is_positive is False:
                            raise NonPositiveDefiniteMatrixError('Matrix must be positive-definite')
                        C[(j, j)] = sqrt(Cjj2)
                        return M._new(C)


def _LDLdecomposition(M, hermitian = (True,)):
    '''Returns the LDL Decomposition (L, D) of matrix A,
    such that L * D * L.H == A if hermitian flag is True, or
    L * D * L.T == A if hermitian is False.
    This method eliminates the use of square root.
    Further this ensures that all the diagonal entries of L are 1.
    A must be a Hermitian positive-definite matrix if hermitian is True,
    or a symmetric matrix otherwise.

    Examples
    ========

    >>> from sympy import Matrix, eye
    >>> A = Matrix(((25, 15, -5), (15, 18, 0), (-5, 0, 11)))
    >>> L, D = A.LDLdecomposition()
    >>> L
    Matrix([
    [   1,   0, 0],
    [ 3/5,   1, 0],
    [-1/5, 1/3, 1]])
    >>> D
    Matrix([
    [25, 0, 0],
    [ 0, 9, 0],
    [ 0, 0, 9]])
    >>> L * D * L.T * A.inv() == eye(A.rows)
    True

    The matrix can have complex entries:

    >>> from sympy import I
    >>> A = Matrix(((9, 3*I), (-3*I, 5)))
    >>> L, D = A.LDLdecomposition()
    >>> L
    Matrix([
    [   1, 0],
    [-I/3, 1]])
    >>> D
    Matrix([
    [9, 0],
    [0, 4]])
    >>> L*D*L.H == A
    True

    See Also
    ========

    sympy.matrices.dense.DenseMatrix.cholesky
    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    QRdecomposition
    '''
    pass
# WARNING: Decompyle incomplete


def _LDLdecomposition_sparse(M, hermitian = (True,)):
    '''
    Returns the LDL Decomposition (matrices ``L`` and ``D``) of matrix
    ``A``, such that ``L * D * L.T == A``. ``A`` must be a square,
    symmetric, positive-definite and non-singular.

    This method eliminates the use of square root and ensures that all
    the diagonal entries of L are 1.

    Examples
    ========

    >>> from sympy import SparseMatrix
    >>> A = SparseMatrix(((25, 15, -5), (15, 18, 0), (-5, 0, 11)))
    >>> L, D = A.LDLdecomposition()
    >>> L
    Matrix([
    [   1,   0, 0],
    [ 3/5,   1, 0],
    [-1/5, 1/3, 1]])
    >>> D
    Matrix([
    [25, 0, 0],
    [ 0, 9, 0],
    [ 0, 0, 9]])
    >>> L * D * L.T == A
    True

    '''
    MutableDenseMatrix = MutableDenseMatrix
    import dense
    if not M.is_square:
        raise NonSquareMatrixError('Matrix must be square.')
    if not hermitian and M.is_hermitian:
        raise ValueError('Matrix must be Hermitian.')
    if not hermitian and M.is_symmetric():
        raise ValueError('Matrix must be symmetric.')
    dps = _get_intermediate_simp(expand_mul, expand_mul)
    Lrowstruc = M.row_structure_symbolic_cholesky()
    L = MutableDenseMatrix.eye(M.rows)
    D = MutableDenseMatrix.zeros(M.rows, M.cols)
    for i in range(len(Lrowstruc)):
        for j in Lrowstruc[i]:
            if i != j:
                L[(i, j)] = M[(i, j)]
                summ = 0
                for p1 in Lrowstruc[i]:
                    if p1 < j:
                        for p2 in Lrowstruc[j]:
                            if p2 < j:
                                if p1 == p2:
                                    if hermitian:
                                        summ += L[(i, p1)] * L[(j, p1)].conjugate() * D[(p1, p1)]
                                        continue
                                    summ += L[(i, p1)] * L[(j, p1)] * D[(p1, p1)]
                                continue
                            L[(i, j)] = dps((L[(i, j)] - summ) / D[(j, j)])
                            D[(i, i)] = M[(i, i)]
                            summ = 0
                            for k in Lrowstruc[i]:
                                if k < i:
                                    if hermitian:
                                        summ += L[(i, k)] * L[(i, k)].conjugate() * D[(k, k)]
                                        continue
                                    summ += L[(i, k)] ** 2 * D[(k, k)]
                                    continue
                                D[(i, i)] = dps(D[(i, i)] - summ)
                                if hermitian and D[(i, i)].is_positive is False:
                                    raise NonPositiveDefiniteMatrixError('Matrix must be positive-definite')
                                return (M._new(L), M._new(D))


def _LUdecomposition(M, iszerofunc, simpfunc, rankcheck = (_iszero, None, False)):
    '''Returns (L, U, perm) where L is a lower triangular matrix with unit
    diagonal, U is an upper triangular matrix, and perm is a list of row
    swap index pairs. If A is the original matrix, then
    ``A = (L*U).permuteBkwd(perm)``, and the row permutation matrix P such
    that $P A = L U$ can be computed by ``P = eye(A.rows).permuteFwd(perm)``.

    See documentation for LUCombined for details about the keyword argument
    rankcheck, iszerofunc, and simpfunc.

    Parameters
    ==========

    rankcheck : bool, optional
        Determines if this function should detect the rank
        deficiency of the matrixis and should raise a
        ``ValueError``.

    iszerofunc : function, optional
        A function which determines if a given expression is zero.

        The function should be a callable that takes a single
        SymPy expression and returns a 3-valued boolean value
        ``True``, ``False``, or ``None``.

        It is internally used by the pivot searching algorithm.
        See the notes section for a more information about the
        pivot searching algorithm.

    simpfunc : function or None, optional
        A function that simplifies the input.

        If this is specified as a function, this function should be
        a callable that takes a single SymPy expression and returns
        an another SymPy expression that is algebraically
        equivalent.

        If ``None``, it indicates that the pivot search algorithm
        should not attempt to simplify any candidate pivots.

        It is internally used by the pivot searching algorithm.
        See the notes section for a more information about the
        pivot searching algorithm.

    Examples
    ========

    >>> from sympy import Matrix
    >>> a = Matrix([[4, 3], [6, 3]])
    >>> L, U, _ = a.LUdecomposition()
    >>> L
    Matrix([
    [  1, 0],
    [3/2, 1]])
    >>> U
    Matrix([
    [4,    3],
    [0, -3/2]])

    See Also
    ========

    sympy.matrices.dense.DenseMatrix.cholesky
    sympy.matrices.dense.DenseMatrix.LDLdecomposition
    QRdecomposition
    LUdecomposition_Simple
    LUdecompositionFF
    LUsolve
    '''
    pass
# WARNING: Decompyle incomplete


def _LUdecomposition_Simple(M, iszerofunc, simpfunc, rankcheck = (_iszero, None, False)):
    '''Compute the PLU decomposition of the matrix.

    Parameters
    ==========

    rankcheck : bool, optional
        Determines if this function should detect the rank
        deficiency of the matrixis and should raise a
        ``ValueError``.

    iszerofunc : function, optional
        A function which determines if a given expression is zero.

        The function should be a callable that takes a single
        SymPy expression and returns a 3-valued boolean value
        ``True``, ``False``, or ``None``.

        It is internally used by the pivot searching algorithm.
        See the notes section for a more information about the
        pivot searching algorithm.

    simpfunc : function or None, optional
        A function that simplifies the input.

        If this is specified as a function, this function should be
        a callable that takes a single SymPy expression and returns
        an another SymPy expression that is algebraically
        equivalent.

        If ``None``, it indicates that the pivot search algorithm
        should not attempt to simplify any candidate pivots.

        It is internally used by the pivot searching algorithm.
        See the notes section for a more information about the
        pivot searching algorithm.

    Returns
    =======

    (lu, row_swaps) : (Matrix, list)
        If the original matrix is a $m, n$ matrix:

        *lu* is a $m, n$ matrix, which contains result of the
        decomposition in a compressed form. See the notes section
        to see how the matrix is compressed.

        *row_swaps* is a $m$-element list where each element is a
        pair of row exchange indices.

        ``A = (L*U).permute_backward(perm)``, and the row
        permutation matrix $P$ from the formula $P A = L U$ can be
        computed by ``P=eye(A.row).permute_forward(perm)``.

    Raises
    ======

    ValueError
        Raised if ``rankcheck=True`` and the matrix is found to
        be rank deficient during the computation.

    Notes
    =====

    About the PLU decomposition:

    PLU decomposition is a generalization of a LU decomposition
    which can be extended for rank-deficient matrices.

    It can further be generalized for non-square matrices, and this
    is the notation that SymPy is using.

    PLU decomposition is a decomposition of a $m, n$ matrix $A$ in
    the form of $P A = L U$ where

    * $L$ is a $m, m$ lower triangular matrix with unit diagonal
        entries.
    * $U$ is a $m, n$ upper triangular matrix.
    * $P$ is a $m, m$ permutation matrix.

    So, for a square matrix, the decomposition would look like:

    .. math::
        L = \\begin{bmatrix}
        1 & 0 & 0 & \\cdots & 0 \\\\
        L_{1, 0} & 1 & 0 & \\cdots & 0 \\\\
        L_{2, 0} & L_{2, 1} & 1 & \\cdots & 0 \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        L_{n-1, 0} & L_{n-1, 1} & L_{n-1, 2} & \\cdots & 1
        \\end{bmatrix}

    .. math::
        U = \\begin{bmatrix}
        U_{0, 0} & U_{0, 1} & U_{0, 2} & \\cdots & U_{0, n-1} \\\\
        0 & U_{1, 1} & U_{1, 2} & \\cdots & U_{1, n-1} \\\\
        0 & 0 & U_{2, 2} & \\cdots & U_{2, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        0 & 0 & 0 & \\cdots & U_{n-1, n-1}
        \\end{bmatrix}

    And for a matrix with more rows than the columns,
    the decomposition would look like:

    .. math::
        L = \\begin{bmatrix}
        1 & 0 & 0 & \\cdots & 0 & 0 & \\cdots & 0 \\\\
        L_{1, 0} & 1 & 0 & \\cdots & 0 & 0 & \\cdots & 0 \\\\
        L_{2, 0} & L_{2, 1} & 1 & \\cdots & 0 & 0 & \\cdots & 0 \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots & \\ddots
        & \\vdots \\\\
        L_{n-1, 0} & L_{n-1, 1} & L_{n-1, 2} & \\cdots & 1 & 0
        & \\cdots & 0 \\\\
        L_{n, 0} & L_{n, 1} & L_{n, 2} & \\cdots & L_{n, n-1} & 1
        & \\cdots & 0 \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots & \\vdots
        & \\ddots & \\vdots \\\\
        L_{m-1, 0} & L_{m-1, 1} & L_{m-1, 2} & \\cdots & L_{m-1, n-1}
        & 0 & \\cdots & 1 \\\\
        \\end{bmatrix}

    .. math::
        U = \\begin{bmatrix}
        U_{0, 0} & U_{0, 1} & U_{0, 2} & \\cdots & U_{0, n-1} \\\\
        0 & U_{1, 1} & U_{1, 2} & \\cdots & U_{1, n-1} \\\\
        0 & 0 & U_{2, 2} & \\cdots & U_{2, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        0 & 0 & 0 & \\cdots & U_{n-1, n-1} \\\\
        0 & 0 & 0 & \\cdots & 0 \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        0 & 0 & 0 & \\cdots & 0
        \\end{bmatrix}

    Finally, for a matrix with more columns than the rows, the
    decomposition would look like:

    .. math::
        L = \\begin{bmatrix}
        1 & 0 & 0 & \\cdots & 0 \\\\
        L_{1, 0} & 1 & 0 & \\cdots & 0 \\\\
        L_{2, 0} & L_{2, 1} & 1 & \\cdots & 0 \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        L_{m-1, 0} & L_{m-1, 1} & L_{m-1, 2} & \\cdots & 1
        \\end{bmatrix}

    .. math::
        U = \\begin{bmatrix}
        U_{0, 0} & U_{0, 1} & U_{0, 2} & \\cdots & U_{0, m-1}
        & \\cdots & U_{0, n-1} \\\\
        0 & U_{1, 1} & U_{1, 2} & \\cdots & U_{1, m-1}
        & \\cdots & U_{1, n-1} \\\\
        0 & 0 & U_{2, 2} & \\cdots & U_{2, m-1}
        & \\cdots & U_{2, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots
        & \\cdots & \\vdots \\\\
        0 & 0 & 0 & \\cdots & U_{m-1, m-1}
        & \\cdots & U_{m-1, n-1} \\\\
        \\end{bmatrix}

    About the compressed LU storage:

    The results of the decomposition are often stored in compressed
    forms rather than returning $L$ and $U$ matrices individually.

    It may be less intiuitive, but it is commonly used for a lot of
    numeric libraries because of the efficiency.

    The storage matrix is defined as following for this specific
    method:

    * The subdiagonal elements of $L$ are stored in the subdiagonal
        portion of $LU$, that is $LU_{i, j} = L_{i, j}$ whenever
        $i > j$.
    * The elements on the diagonal of $L$ are all 1, and are not
        explicitly stored.
    * $U$ is stored in the upper triangular portion of $LU$, that is
        $LU_{i, j} = U_{i, j}$ whenever $i <= j$.
    * For a case of $m > n$, the right side of the $L$ matrix is
        trivial to store.
    * For a case of $m < n$, the below side of the $U$ matrix is
        trivial to store.

    So, for a square matrix, the compressed output matrix would be:

    .. math::
        LU = \\begin{bmatrix}
        U_{0, 0} & U_{0, 1} & U_{0, 2} & \\cdots & U_{0, n-1} \\\\
        L_{1, 0} & U_{1, 1} & U_{1, 2} & \\cdots & U_{1, n-1} \\\\
        L_{2, 0} & L_{2, 1} & U_{2, 2} & \\cdots & U_{2, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        L_{n-1, 0} & L_{n-1, 1} & L_{n-1, 2} & \\cdots & U_{n-1, n-1}
        \\end{bmatrix}

    For a matrix with more rows than the columns, the compressed
    output matrix would be:

    .. math::
        LU = \\begin{bmatrix}
        U_{0, 0} & U_{0, 1} & U_{0, 2} & \\cdots & U_{0, n-1} \\\\
        L_{1, 0} & U_{1, 1} & U_{1, 2} & \\cdots & U_{1, n-1} \\\\
        L_{2, 0} & L_{2, 1} & U_{2, 2} & \\cdots & U_{2, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        L_{n-1, 0} & L_{n-1, 1} & L_{n-1, 2} & \\cdots
        & U_{n-1, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots \\\\
        L_{m-1, 0} & L_{m-1, 1} & L_{m-1, 2} & \\cdots
        & L_{m-1, n-1} \\\\
        \\end{bmatrix}

    For a matrix with more columns than the rows, the compressed
    output matrix would be:

    .. math::
        LU = \\begin{bmatrix}
        U_{0, 0} & U_{0, 1} & U_{0, 2} & \\cdots & U_{0, m-1}
        & \\cdots & U_{0, n-1} \\\\
        L_{1, 0} & U_{1, 1} & U_{1, 2} & \\cdots & U_{1, m-1}
        & \\cdots & U_{1, n-1} \\\\
        L_{2, 0} & L_{2, 1} & U_{2, 2} & \\cdots & U_{2, m-1}
        & \\cdots & U_{2, n-1} \\\\
        \\vdots & \\vdots & \\vdots & \\ddots & \\vdots
        & \\cdots & \\vdots \\\\
        L_{m-1, 0} & L_{m-1, 1} & L_{m-1, 2} & \\cdots & U_{m-1, m-1}
        & \\cdots & U_{m-1, n-1} \\\\
        \\end{bmatrix}

    About the pivot searching algorithm:

    When a matrix contains symbolic entries, the pivot search algorithm
    differs from the case where every entry can be categorized as zero or
    nonzero.
    The algorithm searches column by column through the submatrix whose
    top left entry coincides with the pivot position.
    If it exists, the pivot is the first entry in the current search
    column that iszerofunc guarantees is nonzero.
    If no such candidate exists, then each candidate pivot is simplified
    if simpfunc is not None.
    The search is repeated, with the difference that a candidate may be
    the pivot if ``iszerofunc()`` cannot guarantee that it is nonzero.
    In the second search the pivot is the first candidate that
    iszerofunc can guarantee is nonzero.
    If no such candidate exists, then the pivot is the first candidate
    for which iszerofunc returns None.
    If no such candidate exists, then the search is repeated in the next
    column to the right.
    The pivot search algorithm differs from the one in ``rref()``, which
    relies on ``_find_reasonable_pivot()``.
    Future versions of ``LUdecomposition_simple()`` may use
    ``_find_reasonable_pivot()``.

    See Also
    ========

    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    LUdecompositionFF
    LUsolve
    '''
    pass
# WARNING: Decompyle incomplete


def _LUdecompositionFF(M):
    '''Compute a fraction-free LU decomposition.

    Returns 4 matrices P, L, D, U such that PA = L D**-1 U.
    If the elements of the matrix belong to some integral domain I, then all
    elements of L, D and U are guaranteed to belong to I.

    See Also
    ========

    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    LUdecomposition_Simple
    LUsolve

    References
    ==========

    .. [1] W. Zhou & D.J. Jeffrey, "Fraction-free matrix factors: new forms
        for LU and QR factors". Frontiers in Computer Science in China,
        Vol 2, no. 1, pp. 67-80, 2008.
    '''
    SparseMatrix = SparseMatrix
    import sympy.matrices
    zeros = SparseMatrix.zeros
    eye = SparseMatrix.eye
    m = M.cols
    n = M.rows
    P = eye(n)
    L = eye(n)
    U = M.as_mutable()
    DD = zeros(n, n)
    oldpivot = 1
    for k in range(n - 1):
        if U[(k, k)] == 0:
            for kpivot in range(k + 1, n):
                if U[(kpivot, k)]:
                    pass
                
                raise ValueError('Matrix is not full rank')
                U[(k, k:)], U[(kpivot, k:)] = U[(kpivot, k:)], U[(k, k:)]
                L[(k, :k)], L[(kpivot, :k)] = L[(kpivot, :k)], L[(k, :k)]
                P[(k, :)], P[(kpivot, :)] = P[(kpivot, :)], P[(k, :)]
                L[(k, k)] = U[(k, k)]
                Ukk = U[(k, k)]
                DD[(k, k)] = oldpivot * Ukk
                for i in range(k + 1, n):
                    L[(i, k)] = U[(i, k)]
                    Uik = U[(i, k)]
                    for j in range(k + 1, m):
                        U[(i, j)] = (Ukk * U[(i, j)] - U[(k, j)] * Uik) / oldpivot
                        U[(i, k)] = 0
                        oldpivot = Ukk
                        DD[(n - 1, n - 1)] = oldpivot
                        return (P, L, DD, U)


def _singular_value_decomposition(A):
    '''Returns a Condensed Singular Value decomposition.

    Explanation
    ===========

    A Singular Value decomposition is a decomposition in the form $A = U \\Sigma V^H$
    where

    - $U, V$ are column orthogonal matrix.
    - $\\Sigma$ is a diagonal matrix, where the main diagonal contains singular
      values of matrix A.

    A column orthogonal matrix satisfies
    $\\mathbb{I} = U^H U$ while a full orthogonal matrix satisfies
    relation $\\mathbb{I} = U U^H = U^H U$ where $\\mathbb{I}$ is an identity
    matrix with matching dimensions.

    For matrices which are not square or are rank-deficient, it is
    sufficient to return a column orthogonal matrix because augmenting
    them may introduce redundant computations.
    In condensed Singular Value Decomposition we only return column orthogonal
    matrices because of this reason

    If you want to augment the results to return a full orthogonal
    decomposition, you should use the following procedures.

    - Augment the $U, V$ matrices with columns that are orthogonal to every
      other columns and make it square.
    - Augment the $\\Sigma$ matrix with zero rows to make it have the same
      shape as the original matrix.

    The procedure will be illustrated in the examples section.

    Examples
    ========

    we take a full rank matrix first:

    >>> from sympy import Matrix
    >>> A = Matrix([[1, 2],[2,1]])
    >>> U, S, V = A.singular_value_decomposition()
    >>> U
    Matrix([
    [ sqrt(2)/2, sqrt(2)/2],
    [-sqrt(2)/2, sqrt(2)/2]])
    >>> S
    Matrix([
    [1, 0],
    [0, 3]])
    >>> V
    Matrix([
    [-sqrt(2)/2, sqrt(2)/2],
    [ sqrt(2)/2, sqrt(2)/2]])

    If a matrix if square and full rank both U, V
    are orthogonal in both directions

    >>> U * U.H
    Matrix([
    [1, 0],
    [0, 1]])
    >>> U.H * U
    Matrix([
    [1, 0],
    [0, 1]])

    >>> V * V.H
    Matrix([
    [1, 0],
    [0, 1]])
    >>> V.H * V
    Matrix([
    [1, 0],
    [0, 1]])
    >>> A == U * S * V.H
    True

    >>> C = Matrix([
    ...         [1, 0, 0, 0, 2],
    ...         [0, 0, 3, 0, 0],
    ...         [0, 0, 0, 0, 0],
    ...         [0, 2, 0, 0, 0],
    ...     ])
    >>> U, S, V = C.singular_value_decomposition()

    >>> V.H * V
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> V * V.H
    Matrix([
    [1/5, 0, 0, 0, 2/5],
    [  0, 1, 0, 0,   0],
    [  0, 0, 1, 0,   0],
    [  0, 0, 0, 0,   0],
    [2/5, 0, 0, 0, 4/5]])

    If you want to augment the results to be a full orthogonal
    decomposition, you should augment $V$ with an another orthogonal
    column.

    You are able to append an arbitrary standard basis that are linearly
    independent to every other columns and you can run the Gram-Schmidt
    process to make them augmented as orthogonal basis.

    >>> V_aug = V.row_join(Matrix([[0,0,0,0,1],
    ... [0,0,0,1,0]]).H)
    >>> V_aug = V_aug.QRdecomposition()[0]
    >>> V_aug
    Matrix([
    [0,   sqrt(5)/5, 0, -2*sqrt(5)/5, 0],
    [1,           0, 0,            0, 0],
    [0,           0, 1,            0, 0],
    [0,           0, 0,            0, 1],
    [0, 2*sqrt(5)/5, 0,    sqrt(5)/5, 0]])
    >>> V_aug.H * V_aug
    Matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]])
    >>> V_aug * V_aug.H
    Matrix([
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 1]])

    Similarly we augment U

    >>> U_aug = U.row_join(Matrix([0,0,1,0]))
    >>> U_aug = U_aug.QRdecomposition()[0]
    >>> U_aug
    Matrix([
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]])

    >>> U_aug.H * U_aug
    Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]])
    >>> U_aug * U_aug.H
    Matrix([
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]])

    We add 2 zero columns and one row to S

    >>> S_aug = S.col_join(Matrix([[0,0,0]]))
    >>> S_aug = S_aug.row_join(Matrix([[0,0,0,0],
    ... [0,0,0,0]]).H)
    >>> S_aug
    Matrix([
    [2,       0, 0, 0, 0],
    [0, sqrt(5), 0, 0, 0],
    [0,       0, 3, 0, 0],
    [0,       0, 0, 0, 0]])



    >>> U_aug * S_aug * V_aug.H == C
    True

    '''
    pass
# WARNING: Decompyle incomplete


def _QRdecomposition_optional(M, normalize = (True,)):
    
    def dot(u, v):
        return u.dot(v, hermitian = True)

    dps = _get_intermediate_simp(expand_mul, expand_mul)
    A = M.as_mutable()
    ranked = []
    Q = A
    R = A.zeros(A.cols)
    for j in range(A.cols):
        for i in range(j):
            if Q[(:, i)].is_zero_matrix:
                continue
            R[(i, j)] = dot(Q[(:, i)], Q[(:, j)]) / dot(Q[(:, i)], Q[(:, i)])
            R[(i, j)] = dps(R[(i, j)])
            dps(Q[(:, j)]) = None
            if Q[(:, j)].is_zero_matrix is not True:
                ranked.append(j)
                R[(j, j)] = M.one
        Q = Q.extract(range(Q.rows), ranked)
        R = R.extract(ranked, range(R.cols))
        if normalize:
            for i in range(Q.cols):
                norm = Q[(:, i)].norm()
                return (M.__class__(Q), M.__class__(R))


def _QRdecomposition(M):
    '''Returns a QR decomposition.

    Explanation
    ===========

    A QR decomposition is a decomposition in the form $A = Q R$
    where

    - $Q$ is a column orthogonal matrix.
    - $R$ is a upper triangular (trapezoidal) matrix.

    A column orthogonal matrix satisfies
    $\\mathbb{I} = Q^H Q$ while a full orthogonal matrix satisfies
    relation $\\mathbb{I} = Q Q^H = Q^H Q$ where $I$ is an identity
    matrix with matching dimensions.

    For matrices which are not square or are rank-deficient, it is
    sufficient to return a column orthogonal matrix because augmenting
    them may introduce redundant computations.
    And an another advantage of this is that you can easily inspect the
    matrix rank by counting the number of columns of $Q$.

    If you want to augment the results to return a full orthogonal
    decomposition, you should use the following procedures.

    - Augment the $Q$ matrix with columns that are orthogonal to every
      other columns and make it square.
    - Augment the $R$ matrix with zero rows to make it have the same
      shape as the original matrix.

    The procedure will be illustrated in the examples section.

    Examples
    ========

    A full rank matrix example:

    >>> from sympy import Matrix
    >>> A = Matrix([[12, -51, 4], [6, 167, -68], [-4, 24, -41]])
    >>> Q, R = A.QRdecomposition()
    >>> Q
    Matrix([
    [ 6/7, -69/175, -58/175],
    [ 3/7, 158/175,   6/175],
    [-2/7,    6/35,  -33/35]])
    >>> R
    Matrix([
    [14,  21, -14],
    [ 0, 175, -70],
    [ 0,   0,  35]])

    If the matrix is square and full rank, the $Q$ matrix becomes
    orthogonal in both directions, and needs no augmentation.

    >>> Q * Q.H
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> Q.H * Q
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])

    >>> A == Q*R
    True

    A rank deficient matrix example:

    >>> A = Matrix([[12, -51, 0], [6, 167, 0], [-4, 24, 0]])
    >>> Q, R = A.QRdecomposition()
    >>> Q
    Matrix([
    [ 6/7, -69/175],
    [ 3/7, 158/175],
    [-2/7,    6/35]])
    >>> R
    Matrix([
    [14,  21, 0],
    [ 0, 175, 0]])

    QRdecomposition might return a matrix Q that is rectangular.
    In this case the orthogonality condition might be satisfied as
    $\\mathbb{I} = Q.H*Q$ but not in the reversed product
    $\\mathbb{I} = Q * Q.H$.

    >>> Q.H * Q
    Matrix([
    [1, 0],
    [0, 1]])
    >>> Q * Q.H
    Matrix([
    [27261/30625,   348/30625, -1914/6125],
    [  348/30625, 30589/30625,   198/6125],
    [ -1914/6125,    198/6125,   136/1225]])

    If you want to augment the results to be a full orthogonal
    decomposition, you should augment $Q$ with an another orthogonal
    column.

    You are able to append an identity matrix,
    and you can run the Gram-Schmidt
    process to make them augmented as orthogonal basis.

    >>> Q_aug = Q.row_join(Matrix.eye(3))
    >>> Q_aug = Q_aug.QRdecomposition()[0]
    >>> Q_aug
    Matrix([
    [ 6/7, -69/175, 58/175],
    [ 3/7, 158/175, -6/175],
    [-2/7,    6/35,  33/35]])
    >>> Q_aug.H * Q_aug
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> Q_aug * Q_aug.H
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])

    Augmenting the $R$ matrix with zero row is straightforward.

    >>> R_aug = R.col_join(Matrix([[0, 0, 0]]))
    >>> R_aug
    Matrix([
    [14,  21, 0],
    [ 0, 175, 0],
    [ 0,   0, 0]])
    >>> Q_aug * R_aug == A
    True

    A zero matrix example:

    >>> from sympy import Matrix
    >>> A = Matrix.zeros(3, 4)
    >>> Q, R = A.QRdecomposition()

    They may return matrices with zero rows and columns.

    >>> Q
    Matrix(3, 0, [])
    >>> R
    Matrix(0, 4, [])
    >>> Q*R
    Matrix([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]])

    As the same augmentation rule described above, $Q$ can be augmented
    with columns of an identity matrix and $R$ can be augmented with
    rows of a zero matrix.

    >>> Q_aug = Q.row_join(Matrix.eye(3))
    >>> R_aug = R.col_join(Matrix.zeros(3, 4))
    >>> Q_aug * Q_aug.T
    Matrix([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]])
    >>> R_aug
    Matrix([
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]])
    >>> Q_aug * R_aug == A
    True

    See Also
    ========

    sympy.matrices.dense.DenseMatrix.cholesky
    sympy.matrices.dense.DenseMatrix.LDLdecomposition
    sympy.matrices.matrixbase.MatrixBase.LUdecomposition
    QRsolve
    '''
    return _QRdecomposition_optional(M, normalize = True)


def _upper_hessenberg_decomposition(A):
    '''Converts a matrix into Hessenberg matrix H.

    Returns 2 matrices H, P s.t.
    $P H P^{T} = A$, where H is an upper hessenberg matrix
    and P is an orthogonal matrix

    Examples
    ========

    >>> from sympy import Matrix
    >>> A = Matrix([
    ...     [1,2,3],
    ...     [-3,5,6],
    ...     [4,-8,9],
    ... ])
    >>> H, P = A.upper_hessenberg_decomposition()
    >>> H
    Matrix([
    [1,    6/5,    17/5],
    [5, 213/25, -134/25],
    [0, 216/25,  137/25]])
    >>> P
    Matrix([
    [1,    0,   0],
    [0, -3/5, 4/5],
    [0,  4/5, 3/5]])
    >>> P * H * P.H == A
    True


    References
    ==========

    .. [#] https://mathworld.wolfram.com/HessenbergDecomposition.html
    '''
    M = A.as_mutable()
    if not M.is_square:
        raise NonSquareMatrixError('Matrix must be square.')
    n = M.cols
    P = M.eye(n)
    H = M
    for j in range(n - 2):
        u = H[(j + 1:, j)]
        if u[(1:, :)].is_zero_matrix:
            continue
        if sign(u[0]) != 0:
            u[0] = u[0] + sign(u[0]) * u.norm()
        else:
            u[0] = u[0] + u.norm()
        v = u / u.norm()
        H[(j + 1:, :)] = H[(j + 1:, :)] - 2 * v * v.H * H[(j + 1:, :)]
        H[(:, j + 1:)] = H[(:, j + 1:)] - H[(:, j + 1:)] * 2 * v * v.H
        P[(:, j + 1:)] = P[(:, j + 1:)] - P[(:, j + 1:)] * 2 * v * v.H
        return (H, P)
