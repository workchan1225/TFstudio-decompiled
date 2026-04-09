# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: determinant.pyc (Python 3.11)

from types import FunctionType
from sympy.core.cache import cacheit
from sympy.core.numbers import Float, Integer
from sympy.core.singleton import S
from sympy.core.symbol import uniquely_named_symbol
from sympy.core.mul import Mul
from sympy.polys import PurePoly, cancel
from sympy.functions.combinatorial.numbers import nC
from sympy.polys.matrices.domainmatrix import DomainMatrix
from sympy.polys.matrices.ddm import DDM
from exceptions import NonSquareMatrixError
from utilities import _get_intermediate_simp, _get_intermediate_simp_bool, _iszero, _is_zero_after_expand_mul, _dotprodsimp, _simplify

def _find_reasonable_pivot(col, iszerofunc, simpfunc = (_iszero, _simplify)):
    ''' Find the lowest index of an item in ``col`` that is
    suitable for a pivot.  If ``col`` consists only of
    Floats, the pivot with the largest norm is returned.
    Otherwise, the first element where ``iszerofunc`` returns
    False is used.  If ``iszerofunc`` does not return false,
    items are simplified and retested until a suitable
    pivot is found.

    Returns a 4-tuple
        (pivot_offset, pivot_val, assumed_nonzero, newly_determined)
    where pivot_offset is the index of the pivot, pivot_val is
    the (possibly simplified) value of the pivot, assumed_nonzero
    is True if an assumption that the pivot was non-zero
    was made without being proved, and newly_determined are
    elements that were simplified during the process of pivot
    finding.'''
    newly_determined = []
    col = list(col)
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(col()) and (lambda .0: pass# WARNING: Decompyle incomplete
)(col()):
        col_abs = col()
        max_value = max(col_abs)
        if iszerofunc(max_value):
            if max_value != 0:
                newly_determined = enumerate(col)()
            return (None, None, False, newly_determined)
        index = (lambda .0: [ abs(x) for x in .0 ]).index(max_value)
        return (index, col[index], False, newly_determined)
    possible_zeros = any
# WARNING: Decompyle incomplete


def _find_reasonable_pivot_naive(col, iszerofunc, simpfunc = (_iszero, None)):
    '''
    Helper that computes the pivot value and location from a
    sequence of contiguous matrix column elements. As a side effect
    of the pivot search, this function may simplify some of the elements
    of the input column. A list of these simplified entries and their
    indices are also returned.
    This function mimics the behavior of _find_reasonable_pivot(),
    but does less work trying to determine if an indeterminate candidate
    pivot simplifies to zero. This more naive approach can be much faster,
    with the trade-off that it may erroneously return a pivot that is zero.

    ``col`` is a sequence of contiguous column entries to be searched for
    a suitable pivot.
    ``iszerofunc`` is a callable that returns a Boolean that indicates
    if its input is zero, or None if no such determination can be made.
    ``simpfunc`` is a callable that simplifies its input. It must return
    its input if it does not simplify its input. Passing in
    ``simpfunc=None`` indicates that the pivot search should not attempt
    to simplify any candidate pivots.

    Returns a 4-tuple:
    (pivot_offset, pivot_val, assumed_nonzero, newly_determined)
    ``pivot_offset`` is the sequence index of the pivot.
    ``pivot_val`` is the value of the pivot.
    pivot_val and col[pivot_index] are equivalent, but will be different
    when col[pivot_index] was simplified during the pivot search.
    ``assumed_nonzero`` is a boolean indicating if the pivot cannot be
    guaranteed to be zero. If assumed_nonzero is true, then the pivot
    may or may not be non-zero. If assumed_nonzero is false, then
    the pivot is non-zero.
    ``newly_determined`` is a list of index-value pairs of pivot candidates
    that were simplified during the pivot search.
    '''
    indeterminates = []
# WARNING: Decompyle incomplete


def _berkowitz_toeplitz_matrix(M):
    '''Return (A,T) where T the Toeplitz matrix used in the Berkowitz algorithm
    corresponding to ``M`` and A is the first principal submatrix.
    '''
    pass
# WARNING: Decompyle incomplete


def _berkowitz_vector(M):
    ''' Run the Berkowitz algorithm and return a vector whose entries
        are the coefficients of the characteristic polynomial of ``M``.

        Given N x N matrix, efficiently compute
        coefficients of characteristic polynomials of ``M``
        without division in the ground domain.

        This method is particularly useful for computing determinant,
        principal minors and characteristic polynomial when ``M``
        has complicated coefficients e.g. polynomials. Semi-direct
        usage of this algorithm is also important in computing
        efficiently sub-resultant PRS.

        Assuming that M is a square matrix of dimension N x N and
        I is N x N identity matrix, then the Berkowitz vector is
        an N x 1 vector whose entries are coefficients of the
        polynomial

                        charpoly(M) = det(t*I - M)

        As a consequence, all polynomials generated by Berkowitz
        algorithm are monic.

        For more information on the implemented algorithm refer to:

        [1] S.J. Berkowitz, On computing the determinant in small
            parallel time using a small number of processors, ACM,
            Information Processing Letters 18, 1984, pp. 147-150

        [2] M. Keber, Division-Free computation of sub-resultants
            using Bezout matrices, Tech. Report MPI-I-2006-1-006,
            Saarbrucken, 2006
    '''
    if M.rows == 0 and M.cols == 0:
        return M._new(1, 1, [
            M.one])
    if None.rows == 1 and M.cols == 1:
        return M._new(2, 1, [
            M.one,
            -M[(0, 0)]])
    (submat, toeplitz) = None(M)
    return toeplitz.multiply(_berkowitz_vector(submat), dotprodsimp = None)


def _adjugate(M, method = ('berkowitz',)):
    '''Returns the adjugate, or classical adjoint, of
    a matrix.  That is, the transpose of the matrix of cofactors.

    https://en.wikipedia.org/wiki/Adjugate

    Parameters
    ==========

    method : string, optional
        Method to use to find the cofactors, can be "bareiss", "berkowitz",
        "bird", "laplace" or "lu".

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> M.adjugate()
    Matrix([
    [ 4, -2],
    [-3,  1]])

    See Also
    ========

    cofactor_matrix
    sympy.matrices.matrixbase.MatrixBase.transpose
    '''
    return M.cofactor_matrix(method = method).transpose()


def _charpoly(M, x, simplify = ('lambda', _simplify)):
    '''Computes characteristic polynomial det(x*I - M) where I is
    the identity matrix.

    A PurePoly is returned, so using different variables for ``x`` does
    not affect the comparison or the polynomials:

    Parameters
    ==========

    x : string, optional
        Name for the "lambda" variable, defaults to "lambda".

    simplify : function, optional
        Simplification function to use on the characteristic polynomial
        calculated. Defaults to ``simplify``.

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.abc import x, y
    >>> M = Matrix([[1, 3], [2, 0]])
    >>> M.charpoly()
    PurePoly(lambda**2 - lambda - 6, lambda, domain=\'ZZ\')
    >>> M.charpoly(x) == M.charpoly(y)
    True
    >>> M.charpoly(x) == M.charpoly(y)
    True

    Specifying ``x`` is optional; a symbol named ``lambda`` is used by
    default (which looks good when pretty-printed in unicode):

    >>> M.charpoly().as_expr()
    lambda**2 - lambda - 6

    And if ``x`` clashes with an existing symbol, underscores will
    be prepended to the name to make it unique:

    >>> M = Matrix([[1, 2], [x, 0]])
    >>> M.charpoly(x).as_expr()
    _x**2 - _x - 2*x

    Whether you pass a symbol or not, the generator can be obtained
    with the gen attribute since it may not be the same as the symbol
    that was passed:

    >>> M.charpoly(x).gen
    _x
    >>> M.charpoly(x).gen == x
    False

    Notes
    =====

    The Samuelson-Berkowitz algorithm is used to compute
    the characteristic polynomial efficiently and without any
    division operations.  Thus the characteristic polynomial over any
    commutative ring without zero divisors can be computed.

    If the determinant det(x*I - M) can be found out easily as
    in the case of an upper or a lower triangular matrix, then
    instead of Samuelson-Berkowitz algorithm, eigenvalues are computed
    and the characteristic polynomial with their help.

    See Also
    ========

    det
    '''
    pass
# WARNING: Decompyle incomplete


def _cofactor(M, i, j, method = ('berkowitz',)):
    '''Calculate the cofactor of an element.

    Parameters
    ==========

    method : string, optional
        Method to use to find the cofactors, can be "bareiss", "berkowitz",
        "bird", "laplace" or "lu".

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> M.cofactor(0, 1)
    -3

    See Also
    ========

    cofactor_matrix
    minor
    minor_submatrix
    '''
    if M.is_square or M.rows < 1:
        raise NonSquareMatrixError()
    return S.NegativeOne ** ((i + j) % 2) * M.minor(i, j, method)


def _cofactor_matrix(M, method = ('berkowitz',)):
    '''Return a matrix containing the cofactor of each element.

    Parameters
    ==========

    method : string, optional
        Method to use to find the cofactors, can be "bareiss", "berkowitz",
        "bird", "laplace" or "lu".

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> M.cofactor_matrix()
    Matrix([
    [ 4, -3],
    [-2,  1]])

    See Also
    ========

    cofactor
    minor
    minor_submatrix
    '''
    pass
# WARNING: Decompyle incomplete


def _per(M):
    """Returns the permanent of a matrix. Unlike determinant,
    permanent is defined for both square and non-square matrices.

    For an m x n matrix, with m less than or equal to n,
    it is given as the sum over the permutations s of size
    less than or equal to m on [1, 2, . . . n] of the product
    from i = 1 to m of M[i, s[i]]. Taking the transpose will
    not affect the value of the permanent.

    In the case of a square matrix, this is the same as the permutation
    definition of the determinant, but it does not take the sign of the
    permutation into account. Computing the permanent with this definition
    is quite inefficient, so here the Ryser formula is used.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> M.per()
    450
    >>> M = Matrix([1, 5, 7])
    >>> M.per()
    13

    References
    ==========

    .. [1] Prof. Frank Ben's notes: https://math.berkeley.edu/~bernd/ban275.pdf
    .. [2] Wikipedia article on Permanent: https://en.wikipedia.org/wiki/Permanent_%28mathematics%29
    .. [3] https://reference.wolfram.com/language/ref/Permanent.html
    .. [4] Permanent of a rectangular matrix : https://arxiv.org/pdf/0904.3251.pdf
    """
    pass
# WARNING: Decompyle incomplete


def _det_DOM(M):
    DOM = DomainMatrix.from_Matrix(M, field = True, extension = True)
    K = DOM.domain
    return K.to_sympy(DOM.det())


def _det(M, method, iszerofunc = ('bareiss', None)):
    '''Computes the determinant of a matrix if ``M`` is a concrete matrix object
    otherwise return an expressions ``Determinant(M)`` if ``M`` is a
    ``MatrixSymbol`` or other expression.

    Parameters
    ==========

    method : string, optional
        Specifies the algorithm used for computing the matrix determinant.

        If the matrix is at most 3x3, a hard-coded formula is used and the
        specified method is ignored. Otherwise, it defaults to
        ``\'bareiss\'``.

        Also, if the matrix is an upper or a lower triangular matrix, determinant
        is computed by simple multiplication of diagonal elements, and the
        specified method is ignored.

        If it is set to ``\'domain-ge\'``, then Gaussian elimination method will
        be used via using DomainMatrix.

        If it is set to ``\'bareiss\'``, Bareiss\' fraction-free algorithm will
        be used.

        If it is set to ``\'berkowitz\'``, Berkowitz\' algorithm will be used.

        If it is set to ``\'bird\'``, Bird\'s algorithm will be used [1]_.

        If it is set to ``\'laplace\'``, Laplace\'s algorithm will be used.

        Otherwise, if it is set to ``\'lu\'``, LU decomposition will be used.

        .. note::
            For backward compatibility, legacy keys like "bareis" and
            "det_lu" can still be used to indicate the corresponding
            methods.
            And the keys are also case-insensitive for now. However, it is
            suggested to use the precise keys for specifying the method.

    iszerofunc : FunctionType or None, optional
        If it is set to ``None``, it will be defaulted to ``_iszero`` if the
        method is set to ``\'bareiss\'``, and ``_is_zero_after_expand_mul`` if
        the method is set to ``\'lu\'``.

        It can also accept any user-specified zero testing function, if it
        is formatted as a function which accepts a single symbolic argument
        and returns ``True`` if it is tested as zero and ``False`` if it
        tested as non-zero, and also ``None`` if it is undecidable.

    Returns
    =======

    det : Basic
        Result of determinant.

    Raises
    ======

    ValueError
        If unrecognized keys are given for ``method`` or ``iszerofunc``.

    NonSquareMatrixError
        If attempted to calculate determinant from a non-square matrix.

    Examples
    ========

    >>> from sympy import Matrix, eye, det
    >>> I3 = eye(3)
    >>> det(I3)
    1
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> det(M)
    -2
    >>> det(M) == M.det()
    True
    >>> M.det(method="domain-ge")
    -2

    References
    ==========

    .. [1] Bird, R. S. (2011). A simple division-free algorithm for computing
           determinants. Inf. Process. Lett., 111(21), 1072-1074. doi:
           10.1016/j.ipl.2011.08.006
    '''
    method = method.lower()
    if method == 'bareis':
        method = 'bareiss'
    elif method == 'det_lu':
        method = 'lu'
    if method not in ('bareiss', 'berkowitz', 'lu', 'domain-ge', 'bird', 'laplace'):
        raise ValueError("Determinant method '%s' unrecognized" % method)
# WARNING: Decompyle incomplete


def _det_bareiss(M, iszerofunc = (_is_zero_after_expand_mul,)):
    """Compute matrix determinant using Bareiss' fraction-free
    algorithm which is an extension of the well known Gaussian
    elimination method. This approach is best suited for dense
    symbolic matrices and will result in a determinant with
    minimal number of fractions. It means that less term
    rewriting is needed on resulting formulae.

    Parameters
    ==========

    iszerofunc : function, optional
        The function to use to determine zeros when doing an LU decomposition.
        Defaults to ``lambda x: x.is_zero``.

    TODO: Implement algorithm for sparse matrices (SFF),
    http://www.eecis.udel.edu/~saunders/papers/sffge/it5.ps.
    """
    pass
# WARNING: Decompyle incomplete


def _det_berkowitz(M):
    ''' Use the Berkowitz algorithm to compute the determinant.'''
    if not M.is_square:
        raise NonSquareMatrixError()
    if M.rows == 0:
        return M.one
    berk_vector = None(M)
    return -1 ** (len(berk_vector) - 1) * berk_vector[-1]


def _det_LU(M, iszerofunc, simpfunc = (_iszero, None)):
    ''' Computes the determinant of a matrix from its LU decomposition.
    This function uses the LU decomposition computed by
    LUDecomposition_Simple().

    The keyword arguments iszerofunc and simpfunc are passed to
    LUDecomposition_Simple().
    iszerofunc is a callable that returns a boolean indicating if its
    input is zero, or None if it cannot make the determination.
    simpfunc is a callable that simplifies its input.
    The default is simpfunc=None, which indicate that the pivot search
    algorithm should not attempt to simplify any candidate pivots.
    If simpfunc fails to simplify its input, then it must return its input
    instead of a copy.

    Parameters
    ==========

    iszerofunc : function, optional
        The function to use to determine zeros when doing an LU decomposition.
        Defaults to ``lambda x: x.is_zero``.

    simpfunc : function, optional
        The simplification function to use when looking for zeros for pivots.
    '''
    if not M.is_square:
        raise NonSquareMatrixError()
    if M.rows == 0:
        return M.one
    (lu, row_swaps) = None.LUdecomposition_Simple(iszerofunc = iszerofunc, simpfunc = simpfunc)
    if iszerofunc(lu[(lu.rows - 1, lu.rows - 1)]):
        return M.zero
    det = -(M.one) if None(row_swaps) % 2 else M.one
    for k in range(lu.rows):
        det *= lu[(k, k)]
        return det

__det_laplace = (lambda M: pass# WARNING: Decompyle incomplete
)()

def _det_laplace(M):
    '''Compute the determinant of a matrix using Laplace expansion.

    While Laplace expansion is not the most efficient method of computing
    a determinant, it is a simple one, and it has the advantage of
    being division free. To improve efficiency, this function uses
    caching to avoid recomputing determinants of submatrices.
    '''
    if not M.is_square:
        raise NonSquareMatrixError()
    if M.shape[0] == 0:
        return M.one
    return None(M.as_immutable())


def _det_bird(M):
    """Compute the determinant of a matrix using Bird's algorithm.

    Bird's algorithm is a simple division-free algorithm for computing, which
    is of lower order than the Laplace's algorithm. It is described in [1]_.

    References
    ==========

    .. [1] Bird, R. S. (2011). A simple division-free algorithm for computing
           determinants. Inf. Process. Lett., 111(21), 1072-1074. doi:
           10.1016/j.ipl.2011.08.006
    """
    
    def mu(X):
        pass
    # WARNING: Decompyle incomplete

    Mddm = M._rep.to_ddm()
    n = M.shape[0]
    if n == 0:
        return M.one
    Fn1 = None
    for _ in range(n - 1):
        Fn1 = mu(Fn1).matmul(Mddm)
        detA = Fn1[0][0]
        if n % 2 == 0:
            detA = -detA
    return Mddm.domain.to_sympy(detA)


def _minor(M, i, j, method = ('berkowitz',)):
    '''Return the (i,j) minor of ``M``.  That is,
    return the determinant of the matrix obtained by deleting
    the `i`th row and `j`th column from ``M``.

    Parameters
    ==========

    i, j : int
        The row and column to exclude to obtain the submatrix.

    method : string, optional
        Method to use to find the determinant of the submatrix, can be
        "bareiss", "berkowitz", "bird", "laplace" or "lu".

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> M.minor(1, 1)
    -12

    See Also
    ========

    minor_submatrix
    cofactor
    det
    '''
    if not M.is_square:
        raise NonSquareMatrixError()
    return M.minor_submatrix(i, j).det(method = method)


def _minor_submatrix(M, i, j):
    '''Return the submatrix obtained by removing the `i`th row
    and `j`th column from ``M`` (works with Pythonic negative indices).

    Parameters
    ==========

    i, j : int
        The row and column to exclude to obtain the submatrix.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    >>> M.minor_submatrix(1, 1)
    Matrix([
    [1, 3],
    [7, 9]])

    See Also
    ========

    minor
    cofactor
    '''
    pass
# WARNING: Decompyle incomplete
