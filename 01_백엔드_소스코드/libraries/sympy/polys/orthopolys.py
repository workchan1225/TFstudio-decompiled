# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: orthopolys.pyc (Python 3.11)

'''Efficient functions for generating orthogonal polynomials.'''
from sympy.core.symbol import Dummy
from sympy.polys.densearith import dup_mul, dup_mul_ground, dup_lshift, dup_sub, dup_add, dup_sub_term, dup_sub_ground, dup_sqr
from sympy.polys.domains import ZZ, QQ
from sympy.polys.polytools import named_poly
from sympy.utilities import public

def dup_jacobi(n, a, b, K):
    '''Low-level implementation of Jacobi polynomials.'''
    if n < 1:
        return [
            K.one]
    m1 = [
        (a + b) / K(2) + K.one,
        (a - b) / K(2)]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        den = K(i) * (a + b + i) * (a + b + K(2) * i - K(2))
        f0 = (a + b + K(2) * i - K.one) * (a * a - b * b) / (K(2) * den)
        f1 = (a + b + K(2) * i - K.one) * (a + b + K(2) * i - K(2)) * (a + b + K(2) * i) / (K(2) * den)
        f2 = (a + i - K.one) * (b + i - K.one) * (a + b + K(2) * i) / den
        p0 = dup_mul_ground(m1, f0, K)
        p1 = dup_mul_ground(dup_lshift(m1, 1, K), f1, K)
        p2 = dup_mul_ground(m2, f2, K)
        m1 = dup_sub(dup_add(p0, p1, K), p2, K)
        m2 = m1
        return m1

jacobi_poly = (lambda n, a, b, x, polys = (None, False): named_poly(n, dup_jacobi, None, 'Jacobi polynomial', (x, a, b), polys))()

def dup_gegenbauer(n, a, K):
    '''Low-level implementation of Gegenbauer polynomials.'''
    if n < 1:
        return [
            K.one]
    m1 = [
        K(2) * a,
        K.zero]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        p1 = dup_mul_ground(dup_lshift(m1, 1, K), K(2) * (a - K.one) / K(i) + K(2), K)
        p2 = dup_mul_ground(m2, K(2) * (a - K.one) / K(i) + K.one, K)
        m1 = dup_sub(p1, p2, K)
        m2 = m1
        return m1


def gegenbauer_poly(n, a, x, polys = (None, False)):
    '''Generates the Gegenbauer polynomial `C_n^{(a)}(x)`.

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    a
        Decides minimal domain for the list of coefficients.
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.
    '''
    return named_poly(n, dup_gegenbauer, None, 'Gegenbauer polynomial', (x, a), polys)


def dup_chebyshevt(n, K):
    '''Low-level implementation of Chebyshev polynomials of the first kind.'''
    if n < 1:
        return [
            K.one]
    if None < 64:
        return _dup_chebyshevt_rec(n, K)
    return None(n, K)


def _dup_chebyshevt_rec(n, K):
    ''' Chebyshev polynomials of the first kind using recurrence.

    Explanation
    ===========

    Chebyshev polynomials of the first kind are defined by the recurrence
    relation:

    .. math::
        T_0(x) &= 1\\\\
        T_1(x) &= x\\\\
        T_n(x) &= 2xT_{n-1}(x) - T_{n-2}(x)

    This function calculates the Chebyshev polynomial of the first kind using
    the above recurrence relation.

    Parameters
    ==========

    n : int
        n is a nonnegative integer.
    K : domain

    '''
    m1 = [
        K.one,
        K.zero]
    m2 = [
        K.one]
    for _ in range(n - 1):
        m1 = dup_sub(dup_mul_ground(dup_lshift(m1, 1, K), K(2), K), m2, K)
        m2 = m1
        return m1


def _dup_chebyshevt_prod(n, K):
    ''' Chebyshev polynomials of the first kind using recursive products.

    Explanation
    ===========

    Computes Chebyshev polynomials of the first kind using

    .. math::
        T_{2n}(x) &= 2T_n^2(x) - 1\\\\
        T_{2n+1}(x) &= 2T_{n+1}(x)T_n(x) - x

    This is faster than ``_dup_chebyshevt_rec`` for large ``n``.

    Parameters
    ==========

    n : int
        n is a nonnegative integer.
    K : domain

    '''
    m1 = [
        K(2),
        K.zero,
        -(K.one)]
    m2 = [
        K.one,
        K.zero]
    for i in bin(n)[3:]:
        c = dup_sub_term(dup_mul_ground(dup_mul(m1, m2, K), K(2), K), K.one, 1, K)
        if i == '1':
            m1 = dup_sub_ground(dup_mul_ground(dup_sqr(m1, K), K(2), K), K.one, K)
            m2 = c
            continue
        m1 = c
        m2 = dup_sub_ground(dup_mul_ground(dup_sqr(m2, K), K(2), K), K.one, K)
        return m2


def dup_chebyshevu(n, K):
    '''Low-level implementation of Chebyshev polynomials of the second kind.'''
    if n < 1:
        return [
            K.one]
    m1 = [
        K(2),
        K.zero]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        m1 = dup_sub(dup_mul_ground(dup_lshift(m1, 1, K), K(2), K), m2, K)
        m2 = m1
        return m1

chebyshevt_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_chebyshevt, ZZ, 'Chebyshev polynomial of the first kind', (x,), polys))()
chebyshevu_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_chebyshevu, ZZ, 'Chebyshev polynomial of the second kind', (x,), polys))()

def dup_hermite(n, K):
    '''Low-level implementation of Hermite polynomials.'''
    if n < 1:
        return [
            K.one]
    m1 = [
        K(2),
        K.zero]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        a = dup_lshift(m1, 1, K)
        b = dup_mul_ground(m2, K(i - 1), K)
        m1 = dup_mul_ground(dup_sub(a, b, K), K(2), K)
        m2 = m1
        return m1


def dup_hermite_prob(n, K):
    """Low-level implementation of probabilist's Hermite polynomials."""
    if n < 1:
        return [
            K.one]
    m1 = [
        K.one,
        K.zero]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        a = dup_lshift(m1, 1, K)
        b = dup_mul_ground(m2, K(i - 1), K)
        m1 = dup_sub(a, b, K)
        m2 = m1
        return m1

hermite_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_hermite, ZZ, 'Hermite polynomial', (x,), polys))()
hermite_prob_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_hermite_prob, ZZ, "probabilist's Hermite polynomial", (x,), polys))()

def dup_legendre(n, K):
    '''Low-level implementation of Legendre polynomials.'''
    if n < 1:
        return [
            K.one]
    m1 = [
        K.one,
        K.zero]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        a = dup_mul_ground(dup_lshift(m1, 1, K), K(2 * i - 1, i), K)
        b = dup_mul_ground(m2, K(i - 1, i), K)
        m1 = dup_sub(a, b, K)
        m2 = m1
        return m1

legendre_poly = (lambda n, x, polys = (None, False): named_poly(n, dup_legendre, QQ, 'Legendre polynomial', (x,), polys))()

def dup_laguerre(n, alpha, K):
    '''Low-level implementation of Laguerre polynomials.'''
    m1 = [
        K.one]
    m2 = [
        K.zero]
    for i in range(1, n + 1):
        a = dup_mul(m1, [
            -(K.one) / K(i),
            (alpha - K.one) / K(i) + K(2)], K)
        b = dup_mul_ground(m2, (alpha - K.one) / K(i) + K.one, K)
        m1 = dup_sub(a, b, K)
        m2 = m1
        return m1

laguerre_poly = (lambda n, x, alpha, polys = (None, 0, False): named_poly(n, dup_laguerre, None, 'Laguerre polynomial', (x, alpha), polys))()

def dup_spherical_bessel_fn(n, K):
    '''Low-level implementation of fn(n, x).'''
    if n < 1:
        return [
            K.one,
            K.zero]
    m1 = [
        K.one,
        K.zero]
    m2 = [
        None.one]
    for i in range(2, n + 1):
        m1 = dup_sub(dup_mul_ground(dup_lshift(m1, 1, K), K(2 * i - 1), K), m2, K)
        m2 = m1
        return dup_lshift(m1, 1, K)


def dup_spherical_bessel_fn_minus(n, K):
    '''Low-level implementation of fn(-n, x).'''
    m1 = [
        K.zero]
    m2 = [
        K.one,
        K.zero]
    for i in range(2, n + 1):
        m1 = dup_sub(dup_mul_ground(dup_lshift(m1, 1, K), K(3 - 2 * i), K), m2, K)
        m2 = m1
        return m1


def spherical_bessel_fn(n, x, polys = (None, False)):
    '''
    Coefficients for the spherical Bessel functions.

    These are only needed in the jn() function.

    The coefficients are calculated from:

    fn(0, z) = 1/z
    fn(1, z) = 1/z**2
    fn(n-1, z) + fn(n+1, z) == (2*n+1)/z * fn(n, z)

    Parameters
    ==========

    n : int
        Degree of the polynomial.
    x : optional
    polys : bool, optional
        If True, return a Poly, otherwise (default) return an expression.

    Examples
    ========

    >>> from sympy.polys.orthopolys import spherical_bessel_fn as fn
    >>> from sympy import Symbol
    >>> z = Symbol("z")
    >>> fn(1, z)
    z**(-2)
    >>> fn(2, z)
    -1/z + 3/z**3
    >>> fn(3, z)
    -6/z**2 + 15/z**4
    >>> fn(4, z)
    1/z - 45/z**3 + 105/z**5

    '''
    pass
# WARNING: Decompyle incomplete
