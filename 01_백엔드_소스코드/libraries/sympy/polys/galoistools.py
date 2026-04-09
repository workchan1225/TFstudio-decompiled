# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: galoistools.pyc (Python 3.11)

'''Dense univariate polynomials with coefficients in Galois fields. '''
from math import ceil as _ceil, sqrt as _sqrt, prod
from sympy.core.random import uniform, _randint
from sympy.external.gmpy import SYMPY_INTS, MPZ, invert
from sympy.polys.polyconfig import query
from sympy.polys.polyerrors import ExactQuotientFailed
from sympy.polys.polyutils import _sort_factors

def gf_crt(U, M, K = (None,)):
    '''
    Chinese Remainder Theorem.

    Given a set of integer residues ``u_0,...,u_n`` and a set of
    co-prime integer moduli ``m_0,...,m_n``, returns an integer
    ``u``, such that ``u = u_i mod m_i`` for ``i = ``0,...,n``.

    Examples
    ========

    Consider a set of residues ``U = [49, 76, 65]``
    and a set of moduli ``M = [99, 97, 95]``. Then we have::

       >>> from sympy.polys.domains import ZZ
       >>> from sympy.polys.galoistools import gf_crt

       >>> gf_crt([49, 76, 65], [99, 97, 95], ZZ)
       639985

    This is the correct result because::

       >>> [639985 % m for m in [99, 97, 95]]
       [49, 76, 65]

    Note: this is a low-level routine with no error checking.

    See Also
    ========

    sympy.ntheory.modular.crt : a higher level crt routine
    sympy.ntheory.modular.solve_congruence

    '''
    p = prod(M, start = K.one)
    v = K.zero
    for u, m in zip(U, M):
        e = p // m
        (s, _, _) = K.gcdex(e, m)
        v += e * (u * s % m)
        return v % p


def gf_crt1(M, K):
    '''
    First part of the Chinese Remainder Theorem.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_crt, gf_crt1, gf_crt2
    >>> U = [49, 76, 65]
    >>> M = [99, 97, 95]

    The following two codes have the same result.

    >>> gf_crt(U, M, ZZ)
    639985

    >>> p, E, S = gf_crt1(M, ZZ)
    >>> gf_crt2(U, M, p, E, S, ZZ)
    639985

    However, it is faster when we want to fix ``M`` and
    compute for multiple U, i.e. the following cases:

    >>> p, E, S = gf_crt1(M, ZZ)
    >>> Us = [[49, 76, 65], [23, 42, 67]]
    >>> for U in Us:
    ...     print(gf_crt2(U, M, p, E, S, ZZ))
    639985
    236237

    See Also
    ========

    sympy.ntheory.modular.crt1 : a higher level crt routine
    sympy.polys.galoistools.gf_crt
    sympy.polys.galoistools.gf_crt2

    '''
    S = []
    E = []
    p = prod(M, start = K.one)
    for m in M:
        E.append(p // m)
        S.append(K.gcdex(E[-1], m)[0] % m)
        return (p, E, S)


def gf_crt2(U, M, p, E, S, K):
    '''
    Second part of the Chinese Remainder Theorem.

    See ``gf_crt1`` for usage.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_crt2

    >>> U = [49, 76, 65]
    >>> M = [99, 97, 95]
    >>> p = 912285
    >>> E = [9215, 9405, 9603]
    >>> S = [62, 24, 12]

    >>> gf_crt2(U, M, p, E, S, ZZ)
    639985

    See Also
    ========

    sympy.ntheory.modular.crt2 : a higher level crt routine
    sympy.polys.galoistools.gf_crt
    sympy.polys.galoistools.gf_crt1

    '''
    v = K.zero
    for u, m, e, s in zip(U, M, E, S):
        v += e * (u * s % m)
        return v % p


def gf_int(a, p):
    '''
    Coerce ``a mod p`` to an integer in the range ``[-p/2, p/2]``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_int

    >>> gf_int(2, 7)
    2
    >>> gf_int(5, 7)
    -2

    '''
    if a <= p // 2:
        return a
    return None - p


def gf_degree(f):
    '''
    Return the leading degree of ``f``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_degree

    >>> gf_degree([1, 1, 2, 0])
    3
    >>> gf_degree([])
    -1

    '''
    return len(f) - 1


def gf_LC(f, K):
    '''
    Return the leading coefficient of ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_LC

    >>> gf_LC([3, 0, 1], ZZ)
    3

    '''
    if not f:
        return K.zero
    return None[0]


def gf_TC(f, K):
    '''
    Return the trailing coefficient of ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_TC

    >>> gf_TC([3, 0, 1], ZZ)
    1

    '''
    if not f:
        return K.zero
    return None[-1]


def gf_strip(f):
    '''
    Remove leading zeros from ``f``.


    Examples
    ========

    >>> from sympy.polys.galoistools import gf_strip

    >>> gf_strip([0, 0, 0, 3, 0, 1])
    [3, 0, 1]

    '''
    if f or f[0]:
        return f
    k = None
    for coeff in f:
        if coeff:
            pass
        else:
            k += 1
        return f[k:]


def gf_trunc(f, p):
    '''
    Reduce all coefficients modulo ``p``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_trunc

    >>> gf_trunc([7, -2, 3], 5)
    [2, 3, 3]

    '''
    pass
# WARNING: Decompyle incomplete


def gf_normal(f, p, K):
    '''
    Normalize all coefficients in ``K``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_normal

    >>> gf_normal([5, 10, 21, -3], 5, ZZ)
    [1, 2]

    '''
    return gf_trunc(list(map(K, f)), p)


def gf_from_dict(f, p, K):
    '''
    Create a ``GF(p)[x]`` polynomial from a dict.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_from_dict

    >>> gf_from_dict({10: ZZ(4), 4: ZZ(33), 0: ZZ(-1)}, 5, ZZ)
    [4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4]

    '''
    h = []
    n = max(f.keys())
    if isinstance(n, SYMPY_INTS):
        for k in range(n, -1, -1):
            h.append(f.get(k, K.zero) % p)
    (n,) = n
    for k in range(n, -1, -1):
        h.append(f.get((k,), K.zero) % p)
        return gf_trunc(h, p)


def gf_to_dict(f, p, symmetric = (True,)):
    '''
    Convert a ``GF(p)[x]`` polynomial to a dict.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_to_dict

    >>> gf_to_dict([4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4], 5)
    {0: -1, 4: -2, 10: -1}
    >>> gf_to_dict([4, 0, 0, 0, 0, 0, 3, 0, 0, 0, 4], 5, symmetric=False)
    {0: 4, 4: 3, 10: 4}

    '''
    result = { }
    n = gf_degree(f)
    for k in range(0, n + 1):
        if symmetric:
            a = gf_int(f[n - k], p)
        else:
            a = f[n - k]
        if a:
            result[k] = a
        return result


def gf_from_int_poly(f, p):
    '''
    Create a ``GF(p)[x]`` polynomial from ``Z[x]``.

    Examples
    ========

    >>> from sympy.polys.galoistools import gf_from_int_poly

    >>> gf_from_int_poly([7, -2, 3], 5)
    [2, 3, 3]

    '''
    return gf_trunc(f, p)


def gf_to_int_poly(f, p, symmetric = (True,)):
    '''
    Convert a ``GF(p)[x]`` polynomial to ``Z[x]``.


    Examples
    ========

    >>> from sympy.polys.galoistools import gf_to_int_poly

    >>> gf_to_int_poly([2, 3, 3], 5)
    [2, -2, -2]
    >>> gf_to_int_poly([2, 3, 3], 5, symmetric=False)
    [2, 3, 3]

    '''
    pass
# WARNING: Decompyle incomplete


def gf_neg(f, p, K):
    '''
    Negate a polynomial in ``GF(p)[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.galoistools import gf_neg

    >>> gf_neg([3, 2, 1, 0], 5, ZZ)
    [2, 3, 4, 0]

    '''
    pass
# WARNING: Decompyle incomplete


def gf_add_ground(f, a, p, K):
