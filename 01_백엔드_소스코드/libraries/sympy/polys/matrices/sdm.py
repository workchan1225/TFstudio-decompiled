# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sdm.pyc (Python 3.11)

'''

Module for the SDM class.

'''
from operator import add, neg, pos, sub, mul
from collections import defaultdict
from sympy.external.gmpy import GROUND_TYPES
from sympy.utilities.decorator import doctest_depends_on
from sympy.utilities.iterables import _strongly_connected_components
from exceptions import DMBadInputError, DMDomainError, DMShapeError
from sympy.polys.domains import QQ
from ddm import DDM
if GROUND_TYPES != 'flint':
    __doctest_skip__ = [
        'SDM.to_dfm',
        'SDM.to_dfm_or_ddm']

class SDM(dict):
    pass
# WARNING: Decompyle incomplete


def binop_dict(A, B, fab, fa, fb):
    Bnz = set(B)
    Anz = set(A)
    C = { }
    for i in Anz & Bnz:
        Bi = B[i]
        Ai = A[i]
        Ci = { }
        Bnzi = set(Bi)
        Anzi = set(Ai)
        for j in Anzi & Bnzi:
            Cij = fab(Ai[j], Bi[j])
            if Cij:
                Ci[j] = Cij
            for j in Anzi - Bnzi:
                Cij = fa(Ai[j])
                if Cij:
                    Ci[j] = Cij
                for j in Bnzi - Anzi:
                    Cij = fb(Bi[j])
                    if Cij:
                        Ci[j] = Cij
                    if Ci:
                        C[i] = Ci
        for i in Anz - Bnz:
            Ai = A[i]
            Ci = { }
            for j, Aij in Ai.items():
                Cij = fa(Aij)
                if Cij:
                    Ci[j] = Cij
                if Ci:
                    C[i] = Ci
            for i in Bnz - Anz:
                Bi = B[i]
                Ci = { }
                for j, Bij in Bi.items():
                    Cij = fb(Bij)
                    if Cij:
                        Ci[j] = Cij
                    if Ci:
                        C[i] = Ci
                return C


def unop_dict(A, f):
    B = { }
    for i, Ai in A.items():
        Bi = { }
        for j, Aij in Ai.items():
            Bij = f(Aij)
            if Bij:
                Bi[j] = Bij
            if Bi:
                B[i] = Bi
        return B


def sdm_transpose(M):
    MT = { }
    for i, Mi in M.items():
        for j, Mij in Mi.items():
            MT[j][i] = Mij
            except KeyError:
                MT[j] = {
                    i: Mij }
                continue
            return MT


def sdm_dotvec(A, B, K):
    pass
# WARNING: Decompyle incomplete


def sdm_matvecmul(A, B, K):
    C = { }
    for i, Ai in A.items():
        Ci = sdm_dotvec(Ai, B, K)
        if Ci:
            C[i] = Ci
        return C


def sdm_matmul(A, B, K, m, o):
    if K.is_EXRAW:
        return sdm_matmul_exraw(A, B, K, m, o)
    C = None
    B_knz = set(B)
# WARNING: Decompyle incomplete


def sdm_matmul_exraw(A, B, K, m, o):
    zero = K.zero
    C = { }
    B_knz = set(B)
    for i, Ai in A.items():
        Ci_list = defaultdict(list)
        Ai_knz = set(Ai)
        for k in Ai_knz & B_knz:
            Aik = Ai[k]
            if zero * Aik == zero:
                for j, Bkj in B[k].items():
                    Ci_list[j].append(Aik * Bkj)
                    for j in range(o):
                        Ci_list[j].append(Aik * B[k].get(j, zero))
                        for k in Ai_knz - B_knz:
                            zAik = zero * Ai[k]
                            if zAik != zero:
                                for j in range(o):
                                    Ci_list[j].append(zAik)
                                    Ci = { }
                                    for j, Cij_list in Ci_list.items():
                                        Cij = K.sum(Cij_list)
                                        if Cij:
                                            Ci[j] = Cij
                                        if Ci:
                                            C[i] = Ci
        for k, Bk in B.items():
            for j, Bkj in Bk.items():
                if zero * Bkj != zero:
                    for i in range(m):
                        Aik = A.get(i, { }).get(k, zero)
                        if Aik == zero:
                            Ci = C.get(i, { })
                            Cij = Ci.get(j, zero) + Aik * Bkj
                            if Cij != zero:
                                Ci[j] = Cij
                            else:
                                raise RuntimeError
                            C[i] = Ci
                        return C


def sdm_irref(A):
    '''RREF and pivots of a sparse matrix *A*.

    Compute the reduced row echelon form (RREF) of the matrix *A* and return a
    list of the pivot columns. This routine does not work in place and leaves
    the original matrix *A* unmodified.

    The domain of the matrix must be a field.

    Examples
    ========

    This routine works with a dict of dicts sparse representation of a matrix:

    >>> from sympy import QQ
    >>> from sympy.polys.matrices.sdm import sdm_irref
    >>> A = {0: {0: QQ(1), 1: QQ(2)}, 1: {0: QQ(3), 1: QQ(4)}}
    >>> Arref, pivots, _ = sdm_irref(A)
    >>> Arref
    {0: {0: 1}, 1: {1: 1}}
    >>> pivots
    [0, 1]

    The analogous calculation with :py:class:`~.MutableDenseMatrix` would be

    >>> from sympy import Matrix
    >>> M = Matrix([[1, 2], [3, 4]])
    >>> Mrref, pivots = M.rref()
    >>> Mrref
    Matrix([
    [1, 0],
    [0, 1]])
    >>> pivots
    (0, 1)

    Notes
    =====

    The cost of this algorithm is determined purely by the nonzero elements of
    the matrix. No part of the cost of any step in this algorithm depends on
    the number of rows or columns in the matrix. No step depends even on the
    number of nonzero rows apart from the primary loop over those rows. The
    implementation is much faster than ddm_rref for sparse matrices. In fact
    at the time of writing it is also (slightly) faster than the dense
    implementation even if the input is a fully dense matrix so it seems to be
    faster in all cases.

    The elements of the matrix should support exact division with ``/``. For
    example elements of any domain that is a field (e.g. ``QQ``) should be
    fine. No attempt is made to handle inexact arithmetic.

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.rref
        The higher-level function that would normally be used to call this
        routine.
    sympy.polys.matrices.dense.ddm_irref
        The dense equivalent of this routine.
    sdm_rref_den
        Fraction-free version of this routine.
    '''
    pass
# WARNING: Decompyle incomplete


def sdm_rref_den(A, K):
    '''
    Return the reduced row echelon form (RREF) of A with denominator.

    The RREF is computed using fraction-free Gauss-Jordan elimination.

    Explanation
    ===========

    The algorithm used is the fraction-free version of Gauss-Jordan elimination
    described as FFGJ in [1]_. Here it is modified to handle zero or missing
    pivots and to avoid redundant arithmetic. This implementation is also
    optimized for sparse matrices.

    The domain $K$ must support exact division (``K.exquo``) but does not need
    to be a field. This method is suitable for most exact rings and fields like
    :ref:`ZZ`, :ref:`QQ` and :ref:`QQ(a)`. In the case of :ref:`QQ` or
    :ref:`K(x)` it might be more efficient to clear denominators and use
    :ref:`ZZ` or :ref:`K[x]` instead.

    For inexact domains like :ref:`RR` and :ref:`CC` use ``ddm_irref`` instead.

    Examples
    ========

    >>> from sympy.polys.matrices.sdm import sdm_rref_den
    >>> from sympy.polys.domains import ZZ
    >>> A = {0: {0: ZZ(1), 1: ZZ(2)}, 1: {0: ZZ(3), 1: ZZ(4)}}
    >>> A_rref, den, pivots = sdm_rref_den(A, ZZ)
    >>> A_rref
    {0: {0: -2}, 1: {1: -2}}
    >>> den
    -2
    >>> pivots
    [0, 1]

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.rref_den
        Higher-level interface to ``sdm_rref_den`` that would usually be used
        instead of calling this function directly.
    sympy.polys.matrices.sdm.sdm_rref_den
        The ``SDM`` method that uses this function.
    sdm_irref
        Computes RREF using field division.
    ddm_irref_den
        The dense version of this algorithm.

    References
    ==========

    .. [1] Fraction-free algorithms for linear and polynomial equations.
        George C. Nakos , Peter R. Turner , Robert M. Williams.
        https://dl.acm.org/doi/10.1145/271130.271133
    '''
    pass
# WARNING: Decompyle incomplete


def sdm_nullspace_from_rref(A, one, ncols, pivots, nonzero_cols):
    '''Get nullspace from A which is in RREF'''
    nonpivots = sorted(set(range(ncols)) - set(pivots))
    K = []
    for j in nonpivots:
        Kj = {
            j: one }
        for i in nonzero_cols.get(j, ()):
            Kj[pivots[i]] = -A[i][j]
            K.append(Kj)
            return (K, nonpivots)


def sdm_particular_from_rref(A, ncols, pivots):
    '''Get a particular solution from A which is in RREF'''
    P = { }
# WARNING: Decompyle incomplete


def sdm_berk(M, n, K):
    """
    Berkowitz algorithm for computing the characteristic polynomial.

    Explanation
    ===========

    The Berkowitz algorithm is a division-free algorithm for computing the
    characteristic polynomial of a matrix over any commutative ring using only
    arithmetic in the coefficient ring. This implementation is for sparse
    matrices represented in a dict-of-dicts format (like :class:`SDM`).

    Examples
    ========

    >>> from sympy import Matrix
    >>> from sympy.polys.matrices.sdm import sdm_berk
    >>> from sympy.polys.domains import ZZ
    >>> M = {0: {0: ZZ(1), 1:ZZ(2)}, 1: {0:ZZ(3), 1:ZZ(4)}}
    >>> sdm_berk(M, 2, ZZ)
    {0: 1, 1: -5, 2: -2}
    >>> Matrix([[1, 2], [3, 4]]).charpoly()
    PurePoly(lambda**2 - 5*lambda - 2, lambda, domain='ZZ')

    See Also
    ========

    sympy.polys.matrices.domainmatrix.DomainMatrix.charpoly
        The high-level interface to this function.
    sympy.polys.matrices.dense.ddm_berk
        The dense version of this function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Samuelson%E2%80%93Berkowitz_algorithm
    """
    zero = K.zero
    one = K.one
    if n == 0:
        return {
            0: one }
    if None == 1:
        pdict = {
            0: one }
        M00 = M.get(0, { }).get(0, zero)
        if M.get(0, { }).get(0, zero):
            pdict[1] = -M00
    (a, R, C, A) = (K.zero, { }, { }, defaultdict(dict))
# WARNING: Decompyle incomplete
