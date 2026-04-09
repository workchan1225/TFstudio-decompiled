# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: normalforms.pyc (Python 3.11)

'''Functions returning normal forms of matrices'''
from collections import defaultdict
from domainmatrix import DomainMatrix
from exceptions import DMDomainError, DMShapeError
from sympy.ntheory.modular import symmetric_residue
from sympy.polys.domains import QQ, ZZ

def smith_normal_form(m):
    '''
    Return the Smith Normal Form of a matrix `m` over the ring `domain`.
    This will only work if the ring is a principal ideal domain.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DomainMatrix
    >>> from sympy.polys.matrices.normalforms import smith_normal_form
    >>> m = DomainMatrix([[ZZ(12), ZZ(6), ZZ(4)],
    ...                   [ZZ(3), ZZ(9), ZZ(6)],
    ...                   [ZZ(2), ZZ(16), ZZ(14)]], (3, 3), ZZ)
    >>> print(smith_normal_form(m).to_Matrix())
    Matrix([[1, 0, 0], [0, 10, 0], [0, 0, -30]])

    '''
    invs = invariant_factors(m)
    smf = DomainMatrix.diag(invs, m.domain, m.shape)
    return smf


def add_columns(m, i, j, a, b, c, d):
    for k in range(len(m)):
        e = m[k][i]
        m[k][i] = a * e + b * m[k][j]
        m[k][j] = c * e + d * m[k][j]
        return None


def invariant_factors(m):
    '''
    Return the tuple of abelian invariants for a matrix `m`
    (as in the Smith-Normal form)

    References
    ==========

    [1] https://en.wikipedia.org/wiki/Smith_normal_form#Algorithm
    [2] https://web.archive.org/web/20200331143852/https://sierra.nmsu.edu/morandi/notes/SmithNormalForm.pdf

    '''
    pass
# WARNING: Decompyle incomplete


def _gcdex(a, b):
    '''
    This supports the functions that compute Hermite Normal Form.

    Explanation
    ===========

    Let x, y be the coefficients returned by the extended Euclidean
    Algorithm, so that x*a + y*b = g. In the algorithms for computing HNF,
    it is critical that x, y not only satisfy the condition of being small
    in magnitude -- namely that |x| <= |b|/g, |y| <- |a|/g -- but also that
    y == 0 when a | b.

    '''
    (x, y, g) = ZZ.gcdex(a, b)
    if a != 0 and b % a == 0:
        y = 0
        x = -1 if a < 0 else 1
    return (x, y, g)


def _hermite_normal_form(A):
    '''
    Compute the Hermite Normal Form of DomainMatrix *A* over :ref:`ZZ`.

    Parameters
    ==========

    A : :py:class:`~.DomainMatrix` over domain :ref:`ZZ`.

    Returns
    =======

    :py:class:`~.DomainMatrix`
        The HNF of matrix *A*.

    Raises
    ======

    DMDomainError
        If the domain of the matrix is not :ref:`ZZ`.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
       (See Algorithm 2.4.5.)

    '''
    if not A.domain.is_ZZ:
        raise DMDomainError('Matrix must be over domain ZZ.')
    (m, n) = A.shape
    A = A.to_dense().rep.to_ddm().copy()
    k = n
    for i in range(m - 1, -1, -1):
        if k == 0:
            pass
        else:
            k -= 1
            for j in range(k - 1, -1, -1):
                if A[i][j] != 0:
                    (u, v, d) = _gcdex(A[i][k], A[i][j])
                    s = A[i][j] // d
                    r = A[i][k] // d
                    add_columns(A, k, j, u, v, -s, r)
                b = A[i][k]
                if b < 0:
                    add_columns(A, k, k, -1, 0, -1, 0)
                    b = -b
            if b == 0:
                k += 1
                continue
            for j in range(k + 1, n):
                q = A[i][j] // b
                add_columns(A, j, k, 1, -q, 0, 1)
                return DomainMatrix.from_rep(A.to_dfm_or_ddm())[(:, k:)]


def _hermite_normal_form_modulo_D(A, D):
    '''
    Perform the mod *D* Hermite Normal Form reduction algorithm on
    :py:class:`~.DomainMatrix` *A*.

    Explanation
    ===========

    If *A* is an $m \\times n$ matrix of rank $m$, having Hermite Normal Form
    $W$, and if *D* is any positive integer known in advance to be a multiple
    of $\\det(W)$, then the HNF of *A* can be computed by an algorithm that
    works mod *D* in order to prevent coefficient explosion.

    Parameters
    ==========

    A : :py:class:`~.DomainMatrix` over :ref:`ZZ`
        $m \\times n$ matrix, having rank $m$.
    D : :ref:`ZZ`
        Positive integer, known to be a multiple of the determinant of the
        HNF of *A*.

    Returns
    =======

    :py:class:`~.DomainMatrix`
        The HNF of matrix *A*.

    Raises
    ======

    DMDomainError
        If the domain of the matrix is not :ref:`ZZ`, or
        if *D* is given but is not in :ref:`ZZ`.

    DMShapeError
        If the matrix has more rows than columns.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
       (See Algorithm 2.4.8.)

    '''
    if not A.domain.is_ZZ:
        raise DMDomainError('Matrix must be over domain ZZ.')
    if ZZ.of_type(D) or D < 1:
        raise DMDomainError('Modulus D must be positive element of domain ZZ.')
    
    def add_columns_mod_R(m, R, i, j, a, b, c, d):
        for k in range(len(m)):
            e = m[k][i]
            m[k][i] = symmetric_residue((a * e + b * m[k][j]) % R, R)
            m[k][j] = symmetric_residue((c * e + d * m[k][j]) % R, R)
            return None

    W = defaultdict(dict)
    (m, n) = A.shape
    if n < m:
        raise DMShapeError('Matrix must have at least as many columns as rows.')
    A = A.to_dense().rep.to_ddm().copy()
    k = n
    R = D
    for i in range(m - 1, -1, -1):
        k -= 1
        for j in range(k - 1, -1, -1):
            if A[i][j] != 0:
                (u, v, d) = _gcdex(A[i][k], A[i][j])
                s = A[i][j] // d
                r = A[i][k] // d
                add_columns_mod_R(A, R, k, j, u, v, -s, r)
            b = A[i][k]
            if b == 0:
                A[i][k] = R
                b = R
        (u, v, d) = _gcdex(b, R)
        for ii in range(m):
            W[ii][i] = u * A[ii][k] % R
            if W[i][i] == 0:
                W[i][i] = R
        for j in range(i + 1, m):
            q = W[i][j] // W[i][i]
            add_columns(W, j, i, 1, -q, 0, 1)
            R //= d
            return DomainMatrix(W, (m, m), ZZ).to_dense()


def hermite_normal_form(A = None, *, D, check_rank):
    '''
    Compute the Hermite Normal Form of :py:class:`~.DomainMatrix` *A* over
    :ref:`ZZ`.

    Examples
    ========

    >>> from sympy import ZZ
    >>> from sympy.polys.matrices import DomainMatrix
    >>> from sympy.polys.matrices.normalforms import hermite_normal_form
    >>> m = DomainMatrix([[ZZ(12), ZZ(6), ZZ(4)],
    ...                   [ZZ(3), ZZ(9), ZZ(6)],
    ...                   [ZZ(2), ZZ(16), ZZ(14)]], (3, 3), ZZ)
    >>> print(hermite_normal_form(m).to_Matrix())
    Matrix([[10, 0, 2], [0, 15, 3], [0, 0, 2]])

    Parameters
    ==========

    A : $m \\times n$ ``DomainMatrix`` over :ref:`ZZ`.

    D : :ref:`ZZ`, optional
        Let $W$ be the HNF of *A*. If known in advance, a positive integer *D*
        being any multiple of $\\det(W)$ may be provided. In this case, if *A*
        also has rank $m$, then we may use an alternative algorithm that works
        mod *D* in order to prevent coefficient explosion.

    check_rank : boolean, optional (default=False)
        The basic assumption is that, if you pass a value for *D*, then
        you already believe that *A* has rank $m$, so we do not waste time
        checking it for you. If you do want this to be checked (and the
        ordinary, non-modulo *D* algorithm to be used if the check fails), then
        set *check_rank* to ``True``.

    Returns
    =======

    :py:class:`~.DomainMatrix`
        The HNF of matrix *A*.

    Raises
    ======

    DMDomainError
        If the domain of the matrix is not :ref:`ZZ`, or
        if *D* is given but is not in :ref:`ZZ`.

    DMShapeError
        If the mod *D* algorithm is used but the matrix has more rows than
        columns.

    References
    ==========

    .. [1] Cohen, H. *A Course in Computational Algebraic Number Theory.*
       (See Algorithms 2.4.5 and 2.4.8.)

    '''
    if not A.domain.is_ZZ:
        raise DMDomainError('Matrix must be over domain ZZ.')
# WARNING: Decompyle incomplete
