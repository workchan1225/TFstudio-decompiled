# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eigen.pyc (Python 3.11)

from types import FunctionType
from collections import Counter
from mpmath import mp, workprec
from mpmath.libmp.libmpf import prec_to_dps
from sympy.core.sorting import default_sort_key
from sympy.core.evalf import DEFAULT_MAXPREC, PrecisionExhausted
from sympy.core.logic import fuzzy_and, fuzzy_or
from sympy.core.numbers import Float
from sympy.core.sympify import _sympify
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.polys import roots, CRootOf, ZZ, QQ, EX
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.eigen import dom_eigenvects, dom_eigenvects_to_sympy
from sympy.polys.polytools import gcd
from exceptions import MatrixError, NonSquareMatrixError
from determinant import _find_reasonable_pivot
from utilities import _iszero, _simplify
__doctest_requires__ = {
    ('_is_indefinite', '_is_negative_definite', '_is_negative_semidefinite', '_is_positive_definite', '_is_positive_semidefinite'): [
        'matplotlib'] }

def _eigenvals_eigenvects_mpmath(M):
    
    norm2 = lambda v: sum((lambda .0: pass# WARNING: Decompyle incomplete
)(v()))

    v1 = None
    prec = (lambda .0: pass# WARNING: Decompyle incomplete
)(M.atoms(Float)())
    eps = 2 ** (-prec)
# WARNING: Decompyle incomplete


def _eigenvals_mpmath(M, multiple = (False,)):
    '''Compute eigenvalues using mpmath'''
    (E, _) = _eigenvals_eigenvects_mpmath(M)
    result = E()
    if multiple:
        return result
    return (lambda .0: [ _sympify(x) for x in .0 ])(Counter(result))


def _eigenvects_mpmath(M):
    (E, ER) = _eigenvals_eigenvects_mpmath(M)
    result = []
    for i in range(M.rows):
        eigenval = _sympify(E[i])
        eigenvect = _sympify(ER[(:, i)])
        result.append((eigenval, 1, [
            eigenvect]))
        return result


def _eigenvals(M = None, error_when_incomplete = (True,), *, simplify, multiple, rational, **flags):
    """Compute eigenvalues of the matrix.

    Parameters
    ==========

    error_when_incomplete : bool, optional
        If it is set to ``True``, it will raise an error if not all
        eigenvalues are computed. This is caused by ``roots`` not returning
        a full list of eigenvalues.

    simplify : bool or function, optional
        If it is set to ``True``, it attempts to return the most
        simplified form of expressions returned by applying default
        simplification method in every routine.

        If it is set to ``False``, it will skip simplification in this
        particular routine to save computation resources.

        If a function is passed to, it will attempt to apply
        the particular function as simplification method.

    rational : bool, optional
        If it is set to ``True``, every floating point numbers would be
        replaced with rationals before computation. It can solve some
        issues of ``roots`` routine not working well with floats.

    multiple : bool, optional
        If it is set to ``True``, the result will be in the form of a
        list.

        If it is set to ``False``, the result will be in the form of a
        dictionary.

    Returns
    =======

    eigs : list or dict
        Eigenvalues of a matrix. The return format would be specified by
        the key ``multiple``.

    Raises
    ======

    MatrixError
        If not enough roots had got computed.

    NonSquareMatrixError
        If attempted to compute eigenvalues from a non-square matrix.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix(3, 3, [0, 1, 1, 1, 0, 0, 1, 1, 1])
    >>> M.eigenvals()
    {-1: 1, 0: 1, 2: 1}

    See Also
    ========

    MatrixBase.charpoly
    eigenvects

    Notes
    =====

    Eigenvalues of a matrix $A$ can be computed by solving a matrix
    equation $\\det(A - \\lambda I) = 0$

    It's not always possible to return radical solutions for
    eigenvalues for matrices larger than $4, 4$ shape due to
    Abel-Ruffini theorem.

    If there is no radical solution is found for the eigenvalue,
    it may return eigenvalues in the form of
    :class:`sympy.polys.rootoftools.ComplexRootOf`.
    """
    pass
# WARNING: Decompyle incomplete

eigenvals_error_message = 'It is not always possible to express the eigenvalues of a matrix of size 5x5 or higher in radicals. We have CRootOf, but domains other than the rationals are not currently supported. If there are no symbols in the matrix, it should still be possible to compute numeric approximations of the eigenvalues using M.evalf().eigenvals() or M.charpoly().nroots().'

def _eigenvals_list(M, error_when_incomplete, simplify = (True, False), **flags):
    pass
# WARNING: Decompyle incomplete


def _eigenvals_dict(M, error_when_incomplete, simplify = (True, False), **flags):
    pass
# WARNING: Decompyle incomplete


def _eigenspace(M, eigenval, iszerofunc, simplify = (_iszero, False)):
    '''Get a basis for the eigenspace for a particular eigenvalue'''
    m = M - M.eye(M.rows) * eigenval
    ret = m.nullspace(iszerofunc = iszerofunc)
    if len(ret) == 0 and simplify:
        ret = m.nullspace(iszerofunc = iszerofunc, simplify = True)
    if len(ret) == 0:
        raise NotImplementedError("Can't evaluate eigenvector for eigenvalue {}".format(eigenval))
    return ret


def _eigenvects_DOM(M, **kwargs):
    DOM = DomainMatrix.from_Matrix(M, field = True, extension = True)
    DOM = DOM.to_dense()
# WARNING: Decompyle incomplete


def _eigenvects_sympy(M, iszerofunc, simplify = (True,), **flags):
    pass
# WARNING: Decompyle incomplete


def _eigenvects(M = None, error_when_incomplete = (True, _iszero), iszerofunc = {
    'chop': False }, *, chop, **flags):
    """Compute eigenvectors of the matrix.

    Parameters
    ==========

    error_when_incomplete : bool, optional
        Raise an error when not all eigenvalues are computed. This is
        caused by ``roots`` not returning a full list of eigenvalues.

    iszerofunc : function, optional
        Specifies a zero testing function to be used in ``rref``.

        Default value is ``_iszero``, which uses SymPy's naive and fast
        default assumption handler.

        It can also accept any user-specified zero testing function, if it
        is formatted as a function which accepts a single symbolic argument
        and returns ``True`` if it is tested as zero and ``False`` if it
        is tested as non-zero, and ``None`` if it is undecidable.

    simplify : bool or function, optional
        If ``True``, ``as_content_primitive()`` will be used to tidy up
        normalization artifacts.

        It will also be used by the ``nullspace`` routine.

    chop : bool or positive number, optional
        If the matrix contains any Floats, they will be changed to Rationals
        for computation purposes, but the answers will be returned after
        being evaluated with evalf. The ``chop`` flag is passed to ``evalf``.
        When ``chop=True`` a default precision will be used; a number will
        be interpreted as the desired level of precision.

    Returns
    =======

    ret : [(eigenval, multiplicity, eigenspace), ...]
        A ragged list containing tuples of data obtained by ``eigenvals``
        and ``nullspace``.

        ``eigenspace`` is a list containing the ``eigenvector`` for each
        eigenvalue.

        ``eigenvector`` is a vector in the form of a ``Matrix``. e.g.
        a vector of length 3 is returned as ``Matrix([a_1, a_2, a_3])``.

    Raises
    ======

    NotImplementedError
        If failed to compute nullspace.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix(3, 3, [0, 1, 1, 1, 0, 0, 1, 1, 1])
    >>> M.eigenvects()
    [(-1, 1, [Matrix([
    [-1],
    [ 1],
    [ 0]])]), (0, 1, [Matrix([
    [ 0],
    [-1],
    [ 1]])]), (2, 1, [Matrix([
    [2/3],
    [1/3],
    [  1]])])]

    See Also
    ========

    eigenvals
    MatrixBase.nullspace
    """
    pass
# WARNING: Decompyle incomplete


def _is_diagonalizable_with_eigen(M, reals_only = (False,)):
    '''See _is_diagonalizable. This function returns the bool along with the
    eigenvectors to avoid calculating them again in functions like
    ``diagonalize``.'''
    if not M.is_square:
        return (False, [])
    eigenvecs = None.eigenvects(simplify = True)
    for val, mult, basis in eigenvecs:
        if not reals_only and val.is_real:
            
            return None, (False, eigenvecs)
        if None != len(basis):
            
            return None, (False, eigenvecs)
        return (True, eigenvecs)


def _is_diagonalizable(M, reals_only = (False,), **kwargs):
    '''Returns ``True`` if a matrix is diagonalizable.

    Parameters
    ==========

    reals_only : bool, optional
        If ``True``, it tests whether the matrix can be diagonalized
        to contain only real numbers on the diagonal.


        If ``False``, it tests whether the matrix can be diagonalized
        at all, even with numbers that may not be real.

    Examples
    ========

    Example of a diagonalizable matrix:

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2, 0], [0, 3, 0], [2, -4, 2]])
    >>> M.is_diagonalizable()
    True

    Example of a non-diagonalizable matrix:

    >>> M = Matrix([[0, 1], [0, 0]])
    >>> M.is_diagonalizable()
    False

    Example of a matrix that is diagonalized in terms of non-real entries:

    >>> M = Matrix([[0, 1], [-1, 0]])
    >>> M.is_diagonalizable(reals_only=False)
    True
    >>> M.is_diagonalizable(reals_only=True)
    False

    See Also
    ========

    sympy.matrices.matrixbase.MatrixBase.is_diagonal
    diagonalize
    '''
    if not M.is_square:
        return False
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(M()) and M.is_symmetric():
        return True
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(M()) and M.is_hermitian:
        return True
    return None(M, reals_only = reals_only)[0]


def _householder_vector(x):
    if not x.cols == 1:
        raise ValueError('Input must be a column matrix')
    v = x.copy()
    v_plus = x.copy()
    v_minus = x.copy()
    q = x[(0, 0)] / abs(x[(0, 0)])
    norm_x = x.norm()
    v_plus[(0, 0)] = x[(0, 0)] + q * norm_x
    v_minus[(0, 0)] = x[(0, 0)] - q * norm_x
    if x[(1:, 0)].norm() == 0:
        bet = 0
        v[(0, 0)] = 1
    elif v_plus.norm() <= v_minus.norm():
        v = v_plus
    else:
        v = v_minus
    v = v / v[0]
    bet = 2 / v.norm() ** 2
    return (v, bet)


def _bidiagonal_decmp_hholder(M):
    m = M.rows
    n = M.cols
    A = M.as_mutable()
    V = A.eye(n)
    U = A.eye(m)
    for i in range(min(m, n)):
        (v, bet) = _householder_vector(A[(i:, i)])
        hh_mat = A.eye(m - i) - bet * v * v.H
        A[(i:, i:)] = hh_mat * A[(i:, i:)]
        temp = A.eye(m)
        temp[(i:, i:)] = hh_mat
        U = U * temp
        if i + 1 <= n - 2:
            (v, bet) = _householder_vector(A[(i, i + 1:)].T)
            hh_mat = A.eye(n - i - 1) - bet * v * v.H
            A[(i:, i + 1:)] = A[(i:, i + 1:)] * hh_mat
            temp = A.eye(n)
            temp[(i + 1:, i + 1:)] = hh_mat
            V = temp * V
        return (U, A, V)


def _eval_bidiag_hholder(M):
    m = M.rows
    n = M.cols
    A = M.as_mutable()
    for i in range(min(m, n)):
        (v, bet) = _householder_vector(A[(i:, i)])
        hh_mat = A.eye(m - i) - bet * v * v.H
        A[(i:, i:)] = hh_mat * A[(i:, i:)]
        if i + 1 <= n - 2:
            (v, bet) = _householder_vector(A[(i, i + 1:)].T)
            hh_mat = A.eye(n - i - 1) - bet * v * v.H
            A[(i:, i + 1:)] = A[(i:, i + 1:)] * hh_mat
        return A


def _bidiagonal_decomposition(M, upper = (True,)):
    '''
    Returns $(U,B,V.H)$ for

    $$A = UBV^{H}$$

    where $A$ is the input matrix, and $B$ is its Bidiagonalized form

    Note: Bidiagonal Computation can hang for symbolic matrices.

    Parameters
    ==========

    upper : bool. Whether to do upper bidiagnalization or lower.
                True for upper and False for lower.

    References
    ==========

    .. [1] Algorithm 5.4.2, Matrix computations by Golub and Van Loan, 4th edition
    .. [2] Complex Matrix Bidiagonalization, https://github.com/vslobody/Householder-Bidiagonalization

    '''
    if not isinstance(upper, bool):
        raise ValueError('upper must be a boolean')
    if upper:
        return _bidiagonal_decmp_hholder(M)
    X = None(M.H)
    return (X[2].H, X[1].H, X[0].H)


def _bidiagonalize(M, upper = (True,)):
    '''
    Returns $B$, the Bidiagonalized form of the input matrix.

    Note: Bidiagonal Computation can hang for symbolic matrices.

    Parameters
    ==========

    upper : bool. Whether to do upper bidiagnalization or lower.
                True for upper and False for lower.

    References
    ==========

    .. [1] Algorithm 5.4.2, Matrix computations by Golub and Van Loan, 4th edition
    .. [2] Complex Matrix Bidiagonalization : https://github.com/vslobody/Householder-Bidiagonalization

    '''
    if not isinstance(upper, bool):
        raise ValueError('upper must be a boolean')
    if upper:
        return _eval_bidiag_hholder(M)
    return None(M.H).H


def _diagonalize(M, reals_only, sort, normalize = (False, False, False)):
    '''
    Return (P, D), where D is diagonal and

        D = P^-1 * M * P

    where M is current matrix.

    Parameters
    ==========

    reals_only : bool. Whether to throw an error if complex numbers are need
                    to diagonalize. (Default: False)

    sort : bool. Sort the eigenvalues along the diagonal. (Default: False)

    normalize : bool. If True, normalize the columns of P. (Default: False)

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix(3, 3, [1, 2, 0, 0, 3, 0, 2, -4, 2])
    >>> M
    Matrix([
    [1,  2, 0],
    [0,  3, 0],
    [2, -4, 2]])
    >>> (P, D) = M.diagonalize()
    >>> D
    Matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]])
    >>> P
    Matrix([
    [-1, 0, -1],
    [ 0, 0, -1],
    [ 2, 1,  2]])
    >>> P.inv() * M * P
    Matrix([
    [1, 0, 0],
    [0, 2, 0],
    [0, 0, 3]])

    See Also
    ========

    sympy.matrices.matrixbase.MatrixBase.is_diagonal
    is_diagonalizable
    '''
    if not M.is_square:
        raise NonSquareMatrixError()
    (is_diagonalizable, eigenvecs) = _is_diagonalizable_with_eigen(M, reals_only = reals_only)
    if not is_diagonalizable:
        raise MatrixError('Matrix is not diagonalizable')
    if sort:
        eigenvecs = sorted(eigenvecs, key = default_sort_key)
    diag = []
    p_cols = []
    for val, mult, basis in eigenvecs:
        diag += [
            val] * mult
        p_cols += basis
        if normalize:
            p_cols = p_cols()
# WARNING: Decompyle incomplete


def _fuzzy_positive_definite(M):
    positive_diagonals = M._has_positive_diagonals()
    if positive_diagonals is False:
        return False
    if None and M.is_strongly_diagonally_dominant:
        return True


def _fuzzy_positive_semidefinite(M):
    nonnegative_diagonals = M._has_nonnegative_diagonals()
    if nonnegative_diagonals is False:
        return False
    if None and M.is_weakly_diagonally_dominant:
        return True


def _is_positive_definite(M):
    if not M.is_hermitian:
        if not M.is_square:
            return False
        M = None + M.H
    fuzzy = _fuzzy_positive_definite(M)
# WARNING: Decompyle incomplete


def _is_positive_semidefinite(M):
    if not M.is_hermitian:
        if not M.is_square:
            return False
        M = None + M.H
    fuzzy = _fuzzy_positive_semidefinite(M)
# WARNING: Decompyle incomplete


def _is_negative_definite(M):
    return _is_positive_definite(-M)


def _is_negative_semidefinite(M):
    return _is_positive_semidefinite(-M)


def _is_indefinite(M):
    if M.is_hermitian:
        eigen = M.eigenvals()
        args1 = eigen.keys()()
        any_positive = fuzzy_or(args1)
        args2 = eigen.keys()()
        any_negative = fuzzy_or(args2)
        return fuzzy_and([
            any_positive,
            any_negative])
    if None.is_square:
        return (M + M.H).is_indefinite


def _is_positive_definite_GE(M):
    '''A division-free gaussian elimination method for testing
    positive-definiteness.'''
    M = M.as_mutable()
    size = M.rows
    for i in range(size):
        is_positive = M[(i, i)].is_positive
        if is_positive is not True:
            
            return None, is_positive
        for None in None(i + 1, size):
            M[(i, i)] * M[(j, i + 1:)] - M[(j, i)] * M[(i, i + 1:)] = None
            return True


def _is_positive_semidefinite_cholesky(M):
    '''Uses Cholesky factorization with complete pivoting

    References
    ==========

    .. [1] http://eprints.ma.man.ac.uk/1199/1/covered/MIMS_ep2008_116.pdf

    .. [2] https://www.value-at-risk.net/cholesky-factorization/
    '''
    pass
# WARNING: Decompyle incomplete

_doc_positive_definite = 'Finds out the definiteness of a matrix.\n\n    Explanation\n    ===========\n\n    A square real matrix $A$ is:\n\n    - A positive definite matrix if $x^T A x > 0$\n      for all non-zero real vectors $x$.\n    - A positive semidefinite matrix if $x^T A x \\geq 0$\n      for all non-zero real vectors $x$.\n    - A negative definite matrix if $x^T A x < 0$\n      for all non-zero real vectors $x$.\n    - A negative semidefinite matrix if $x^T A x \\leq 0$\n      for all non-zero real vectors $x$.\n    - An indefinite matrix if there exists non-zero real vectors\n      $x, y$ with $x^T A x > 0 > y^T A y$.\n\n    A square complex matrix $A$ is:\n\n    - A positive definite matrix if $\\text{re}(x^H A x) > 0$\n      for all non-zero complex vectors $x$.\n    - A positive semidefinite matrix if $\\text{re}(x^H A x) \\geq 0$\n      for all non-zero complex vectors $x$.\n    - A negative definite matrix if $\\text{re}(x^H A x) < 0$\n      for all non-zero complex vectors $x$.\n    - A negative semidefinite matrix if $\\text{re}(x^H A x) \\leq 0$\n      for all non-zero complex vectors $x$.\n    - An indefinite matrix if there exists non-zero complex vectors\n      $x, y$ with $\\text{re}(x^H A x) > 0 > \\text{re}(y^H A y)$.\n\n    A matrix need not be symmetric or hermitian to be positive definite.\n\n    - A real non-symmetric matrix is positive definite if and only if\n      $\\frac{A + A^T}{2}$ is positive definite.\n    - A complex non-hermitian matrix is positive definite if and only if\n      $\\frac{A + A^H}{2}$ is positive definite.\n\n    And this extension can apply for all the definitions above.\n\n    However, for complex cases, you can restrict the definition of\n    $\\text{re}(x^H A x) > 0$ to $x^H A x > 0$ and require the matrix\n    to be hermitian.\n    But we do not present this restriction for computation because you\n    can check ``M.is_hermitian`` independently with this and use\n    the same procedure.\n\n    Examples\n    ========\n\n    An example of symmetric positive definite matrix:\n\n    .. plot::\n        :context: reset\n        :format: doctest\n        :include-source: True\n\n        >>> from sympy import Matrix, symbols\n        >>> from sympy.plotting import plot3d\n        >>> a, b = symbols(\'a b\')\n        >>> x = Matrix([a, b])\n\n        >>> A = Matrix([[1, 0], [0, 1]])\n        >>> A.is_positive_definite\n        True\n        >>> A.is_positive_semidefinite\n        True\n\n        >>> p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))\n\n    An example of symmetric positive semidefinite matrix:\n\n    .. plot::\n        :context: close-figs\n        :format: doctest\n        :include-source: True\n\n        >>> A = Matrix([[1, -1], [-1, 1]])\n        >>> A.is_positive_definite\n        False\n        >>> A.is_positive_semidefinite\n        True\n\n        >>> p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))\n\n    An example of symmetric negative definite matrix:\n\n    .. plot::\n        :context: close-figs\n        :format: doctest\n        :include-source: True\n\n        >>> A = Matrix([[-1, 0], [0, -1]])\n        >>> A.is_negative_definite\n        True\n        >>> A.is_negative_semidefinite\n        True\n        >>> A.is_indefinite\n        False\n\n        >>> p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))\n\n    An example of symmetric indefinite matrix:\n\n    .. plot::\n        :context: close-figs\n        :format: doctest\n        :include-source: True\n\n        >>> A = Matrix([[1, 2], [2, -1]])\n        >>> A.is_indefinite\n        True\n\n        >>> p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))\n\n    An example of non-symmetric positive definite matrix.\n\n    .. plot::\n        :context: close-figs\n        :format: doctest\n        :include-source: True\n\n        >>> A = Matrix([[1, 2], [-2, 1]])\n        >>> A.is_positive_definite\n        True\n        >>> A.is_positive_semidefinite\n        True\n\n        >>> p = plot3d((x.T*A*x)[0, 0], (a, -1, 1), (b, -1, 1))\n\n    Notes\n    =====\n\n    Although some people trivialize the definition of positive definite\n    matrices only for symmetric or hermitian matrices, this restriction\n    is not correct because it does not classify all instances of\n    positive definite matrices from the definition $x^T A x > 0$ or\n    $\\text{re}(x^H A x) > 0$.\n\n    For instance, ``Matrix([[1, 2], [-2, 1]])`` presented in\n    the example above is an example of real positive definite matrix\n    that is not symmetric.\n\n    However, since the following formula holds true;\n\n    .. math::\n        \\text{re}(x^H A x) > 0 \\iff\n        \\text{re}(x^H \\frac{A + A^H}{2} x) > 0\n\n    We can classify all positive definite matrices that may or may not\n    be symmetric or hermitian by transforming the matrix to\n    $\\frac{A + A^T}{2}$ or $\\frac{A + A^H}{2}$\n    (which is guaranteed to be always real symmetric or complex\n    hermitian) and we can defer most of the studies to symmetric or\n    hermitian positive definite matrices.\n\n    But it is a different problem for the existence of Cholesky\n    decomposition. Because even though a non symmetric or a non\n    hermitian matrix can be positive definite, Cholesky or LDL\n    decomposition does not exist because the decompositions require the\n    matrix to be symmetric or hermitian.\n\n    References\n    ==========\n\n    .. [1] https://en.wikipedia.org/wiki/Definiteness_of_a_matrix#Eigenvalues\n\n    .. [2] https://mathworld.wolfram.com/PositiveDefiniteMatrix.html\n\n    .. [3] Johnson, C. R. "Positive Definite Matrices." Amer.\n        Math. Monthly 77, 259-264 1970.\n    '
_is_positive_definite.__doc__ = _doc_positive_definite
_is_positive_semidefinite.__doc__ = _doc_positive_definite
_is_negative_definite.__doc__ = _doc_positive_definite
_is_negative_semidefinite.__doc__ = _doc_positive_definite
_is_indefinite.__doc__ = _doc_positive_definite

def _jordan_form(M = None, calc_transform = (True,), *, chop):
    '''Return $(P, J)$ where $J$ is a Jordan block
    matrix and $P$ is a matrix such that $M = P J P^{-1}$

    Parameters
    ==========

    calc_transform : bool
        If ``False``, then only $J$ is returned.

    chop : bool
        All matrices are converted to exact types when computing
        eigenvalues and eigenvectors.  As a result, there may be
        approximation errors.  If ``chop==True``, these errors
        will be truncated.

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[ 6,  5, -2, -3], [-3, -1,  3,  3], [ 2,  1, -2, -3], [-1,  1,  5,  5]])
    >>> P, J = M.jordan_form()
    >>> J
    Matrix([
    [2, 1, 0, 0],
    [0, 2, 0, 0],
    [0, 0, 2, 1],
    [0, 0, 0, 2]])

    See Also
    ========

    jordan_block
    '''
    pass
# WARNING: Decompyle incomplete


def _left_eigenvects(M, **flags):
    '''Returns left eigenvectors and eigenvalues.

    This function returns the list of triples (eigenval, multiplicity,
    basis) for the left eigenvectors. Options are the same as for
    eigenvects(), i.e. the ``**flags`` arguments gets passed directly to
    eigenvects().

    Examples
    ========

    >>> from sympy import Matrix
    >>> M = Matrix([[0, 1, 1], [1, 0, 0], [1, 1, 1]])
    >>> M.eigenvects()
    [(-1, 1, [Matrix([
    [-1],
    [ 1],
    [ 0]])]), (0, 1, [Matrix([
    [ 0],
    [-1],
    [ 1]])]), (2, 1, [Matrix([
    [2/3],
    [1/3],
    [  1]])])]
    >>> M.left_eigenvects()
    [(-1, 1, [Matrix([[-2, 1, 1]])]), (0, 1, [Matrix([[-1, -1, 1]])]), (2,
    1, [Matrix([[1, 1, 1]])])]

    '''
    pass
# WARNING: Decompyle incomplete


def _singular_values(M):
    """Compute the singular values of a Matrix

    Examples
    ========

    >>> from sympy import Matrix, Symbol
    >>> x = Symbol('x', real=True)
    >>> M = Matrix([[0, 1, 0], [0, x, 0], [-1, 0, 0]])
    >>> M.singular_values()
    [sqrt(x**2 + 1), 1, 0]

    See Also
    ========

    condition_number
    """
    if M.rows >= M.cols:
        valmultpairs = M.H.multiply(M).eigenvals()
    else:
        valmultpairs = M.multiply(M.H).eigenvals()
    vals = []
    for k, v in valmultpairs.items():
        vals += [
            sqrt(k)] * v
        if len(vals) < M.cols:
            vals += [
                M.zero] * (M.cols - len(vals))
    vals.sort(reverse = True, key = default_sort_key)
    return vals
