# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: euclidtools.pyc (Python 3.11)

'''Euclidean algorithms, GCDs, LCMs and polynomial remainder sequences. '''
from sympy.polys.densearith import dup_sub_mul, dup_neg, dmp_neg, dmp_add, dmp_sub, dup_mul, dmp_mul, dmp_pow, dup_div, dmp_div, dup_rem, dup_quo, dmp_quo, dup_prem, dmp_prem, dup_mul_ground, dmp_mul_ground, dmp_mul_term, dup_quo_ground, dmp_quo_ground, dup_max_norm, dmp_max_norm
from sympy.polys.densebasic import dup_strip, dmp_raise, dmp_zero, dmp_one, dmp_ground, dmp_one_p, dmp_zero_p, dmp_zeros, dup_degree, dmp_degree, dmp_degree_in, dup_LC, dmp_LC, dmp_ground_LC, dmp_multi_deflate, dmp_inflate, dup_convert, dmp_convert, dmp_apply_pairs
from sympy.polys.densetools import dup_clear_denoms, dmp_clear_denoms, dup_diff, dmp_diff, dup_eval, dmp_eval, dmp_eval_in, dup_trunc, dmp_ground_trunc, dup_monic, dmp_ground_monic, dup_primitive, dmp_ground_primitive, dup_extract, dmp_ground_extract
from sympy.polys.galoistools import gf_int, gf_crt
from sympy.polys.polyconfig import query
from sympy.polys.polyerrors import MultivariatePolynomialError, HeuristicGCDFailed, HomomorphismFailed, NotInvertible, DomainError

def dup_half_gcdex(f, g, K):
    '''
    Half extended Euclidean algorithm in `F[x]`.

    Returns ``(s, h)`` such that ``h = gcd(f, g)`` and ``s*f = h (mod g)``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**4 - 2*x**3 - 6*x**2 + 12*x + 15
    >>> g = x**3 + x**2 - 4*x - 4

    >>> R.dup_half_gcdex(f, g)
    (-1/5*x + 3/5, x + 1)

    '''
    if not K.is_Field:
        raise DomainError('Cannot compute half extended GCD over %s' % K)
    b = []
    a = [
        K.one]
# WARNING: Decompyle incomplete


def dmp_half_gcdex(f, g, u, K):
    '''
    Half extended Euclidean algorithm in `F[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
    if not u:
        return dup_half_gcdex(f, g, K)
    raise None(f, g)


def dup_gcdex(f, g, K):
    '''
    Extended Euclidean algorithm in `F[x]`.

    Returns ``(s, t, h)`` such that ``h = gcd(f, g)`` and ``s*f + t*g = h``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**4 - 2*x**3 - 6*x**2 + 12*x + 15
    >>> g = x**3 + x**2 - 4*x - 4

    >>> R.dup_gcdex(f, g)
    (-1/5*x + 3/5, 1/5*x**2 - 6/5*x + 2, x + 1)

    '''
    (s, h) = dup_half_gcdex(f, g, K)
    F = dup_sub_mul(h, s, f, K)
    t = dup_quo(F, g, K)
    return (s, t, h)


def dmp_gcdex(f, g, u, K):
    '''
    Extended Euclidean algorithm in `F[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
    if not u:
        return dup_gcdex(f, g, K)
    raise None(f, g)


def dup_invert(f, g, K):
    '''
    Compute multiplicative inverse of `f` modulo `g` in `F[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**2 - 1
    >>> g = 2*x - 1
    >>> h = x - 1

    >>> R.dup_invert(f, g)
    -4/3

    >>> R.dup_invert(f, h)
    Traceback (most recent call last):
    ...
    NotInvertible: zero divisor

    '''
    (s, h) = dup_half_gcdex(f, g, K)
    if h == [
        K.one]:
        return dup_rem(s, g, K)
    raise None('zero divisor')


def dmp_invert(f, g, u, K):
    '''
    Compute multiplicative inverse of `f` modulo `g` in `F[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    '''
    if not u:
        return dup_invert(f, g, K)
    raise None(f, g)


def dup_euclidean_prs(f, g, K):
    '''
    Euclidean polynomial remainder sequence (PRS) in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> g = 3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21

    >>> prs = R.dup_euclidean_prs(f, g)

    >>> prs[0]
    x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> prs[1]
    3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21
    >>> prs[2]
    -5/9*x**4 + 1/9*x**2 - 1/3
    >>> prs[3]
    -117/25*x**2 - 9*x + 441/25
    >>> prs[4]
    233150/19773*x - 102500/6591
    >>> prs[5]
    -1288744821/543589225

    '''
    prs = [
        f,
        g]
    h = dup_rem(f, g, K)
# WARNING: Decompyle incomplete


def dmp_euclidean_prs(f, g, u, K):
    '''
    Euclidean polynomial remainder sequence (PRS) in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
    if not u:
        return dup_euclidean_prs(f, g, K)
    raise None(f, g)


def dup_primitive_prs(f, g, K):
    '''
    Primitive polynomial remainder sequence (PRS) in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> f = x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> g = 3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21

    >>> prs = R.dup_primitive_prs(f, g)

    >>> prs[0]
    x**8 + x**6 - 3*x**4 - 3*x**3 + 8*x**2 + 2*x - 5
    >>> prs[1]
    3*x**6 + 5*x**4 - 4*x**2 - 9*x + 21
    >>> prs[2]
    -5*x**4 + x**2 - 3
    >>> prs[3]
    13*x**2 + 25*x - 49
    >>> prs[4]
    4663*x - 6150
    >>> prs[5]
    1

    '''
    prs = [
        f,
        g]
    (_, h) = dup_primitive(dup_prem(f, g, K), K)
# WARNING: Decompyle incomplete


def dmp_primitive_prs(f, g, u, K):
    '''
    Primitive polynomial remainder sequence (PRS) in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    '''
    if not u:
        return dup_primitive_prs(f, g, K)
    raise None(f, g)


def dup_inner_subresultants(f, g, K):
    '''
    Subresultant PRS algorithm in `K[x]`.

    Computes the subresultant polynomial remainder sequence (PRS)
    and the non-zero scalar subresultants of `f` and `g`.
    By [1] Thm. 3, these are the constants \'-c\' (- to optimize
    computation of sign).
    The first subdeterminant is set to 1 by convention to match
    the polynomial and the scalar subdeterminants.
    If \'deg(f) < deg(g)\', the subresultants of \'(g,f)\' are computed.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_inner_subresultants(x**2 + 1, x**2 - 1)
    ([x**2 + 1, x**2 - 1, -2], [1, 1, 4])

    References
    ==========

    .. [1] W.S. Brown, The Subresultant PRS Algorithm.
           ACM Transaction of Mathematical Software 4 (1978) 237-249

    '''
    n = dup_degree(f)
    m = dup_degree(g)
    if n < m:
        g = f
        f = g
        m = n
        n = m
    if not f:
        return ([], [])
    if not None:
        return ([
            f], [
            K.one])
    R = [
        None,
        g]
    d = n - m
    b = (-(K.one)) ** (d + 1)
    h = dup_prem(f, g, K)
    h = dup_mul_ground(h, b, K)
    lc = dup_LC(g, K)
    c = lc ** d
    S = [
        K.one,
        c]
    c = -c
# WARNING: Decompyle incomplete


def dup_subresultants(f, g, K):
    '''
    Computes subresultant PRS of two polynomials in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_subresultants(x**2 + 1, x**2 - 1)
    [x**2 + 1, x**2 - 1, -2]

    '''
    return dup_inner_subresultants(f, g, K)[0]


def dup_prs_resultant(f, g, K):
    '''
    Resultant algorithm in `K[x]` using subresultant PRS.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_prs_resultant(x**2 + 1, x**2 - 1)
    (4, [x**2 + 1, x**2 - 1, -2])

    '''
    if not f or g:
        return (K.zero, [])
    (R, S) = None(f, g, K)
    if dup_degree(R[-1]) > 0:
        return (K.zero, R)
    return (None[-1], R)


def dup_resultant(f, g, K, includePRS = (False,)):
    '''
    Computes resultant of two polynomials in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_resultant(x**2 + 1, x**2 - 1)
    4

    '''
    if includePRS:
        return dup_prs_resultant(f, g, K)
    return None(f, g, K)[0]


def dmp_inner_subresultants(f, g, u, K):
    '''
    Subresultant PRS algorithm in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> a = 3*x*y**4 + y**3 - 27*y + 4
    >>> b = -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    >>> prs = [f, g, a, b]
    >>> sres = [[1], [1], [3, 0, 0, 0, 0], [-3, 0, 0, -12, 1, 0, -54, 8, 729, -216, 16]]

    >>> R.dmp_inner_subresultants(f, g) == (prs, sres)
    True

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_subresultants(f, g, u, K):
    '''
    Computes subresultant PRS of two polynomials in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> a = 3*x*y**4 + y**3 - 27*y + 4
    >>> b = -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    >>> R.dmp_subresultants(f, g) == [f, g, a, b]
    True

    '''
    return dmp_inner_subresultants(f, g, u, K)[0]


def dmp_prs_resultant(f, g, u, K):
    '''
    Resultant algorithm in `K[X]` using subresultant PRS.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> a = 3*x*y**4 + y**3 - 27*y + 4
    >>> b = -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    >>> res, prs = R.dmp_prs_resultant(f, g)

    >>> res == b             # resultant has n-1 variables
    False
    >>> res == b.drop(x)
    True
    >>> prs == [f, g, a, b]
    True

    '''
    if not u:
        return dup_prs_resultant(f, g, K)
    if None(f, u) or dmp_zero_p(g, u):
        return (dmp_zero(u - 1), [])
    (R, S) = None(f, g, u, K)
    if dmp_degree(R[-1], u) > 0:
        return (dmp_zero(u - 1), R)
    return (None[-1], R)


def dmp_zz_modular_resultant(f, g, p, u, K):
    '''
    Compute resultant of `f` and `g` modulo a prime `p`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x + y + 2
    >>> g = 2*x*y + x + 3

    >>> R.dmp_zz_modular_resultant(f, g, 5)
    -2*y**2 + 1

    '''
    if not u:
        return gf_int(dup_prs_resultant(f, g, K)[0] % p, p)
    v = None - 1
    n = dmp_degree(f, u)
    m = dmp_degree(g, u)
    N = dmp_degree_in(f, 1, u)
    M = dmp_degree_in(g, 1, u)
    B = n * M + m * N
    a = -(K.one)
    D = [
        K.one]
    r = dmp_zero(v)
# WARNING: Decompyle incomplete


def _collins_crt(r, R, P, p, K):
    """Wrapper of CRT for Collins's resultant algorithm. """
    return gf_int(gf_crt([
        r,
        R], [
        P,
        p], K), P * p)


def dmp_zz_collins_resultant(f, g, u, K):
    '''
    Collins\'s modular resultant algorithm in `Z[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x + y + 2
    >>> g = 2*x*y + x + 3

    >>> R.dmp_zz_collins_resultant(f, g)
    -2*y**2 - 5*y + 1

    '''
    n = dmp_degree(f, u)
    m = dmp_degree(g, u)
    if n < 0 or m < 0:
        return dmp_zero(u - 1)
    A = None(f, u, K)
    B = dmp_max_norm(g, u, K)
    a = dmp_ground_LC(f, u, K)
    b = dmp_ground_LC(g, u, K)
    v = u - 1
    B = K(2) * K.factorial(K(n + m)) * A ** m * B ** n
    P = K.one
    p = K.one
    r = dmp_zero(v)
    nextprime = nextprime
    import sympy.ntheory
# WARNING: Decompyle incomplete


def dmp_qq_collins_resultant(f, g, u, K0):
    '''
    Collins\'s modular resultant algorithm in `Q[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> f = QQ(1,2)*x + y + QQ(2,3)
    >>> g = 2*x*y + x + 3

    >>> R.dmp_qq_collins_resultant(f, g)
    -2*y**2 - 7/3*y + 5/6

    '''
    n = dmp_degree(f, u)
    m = dmp_degree(g, u)
    if n < 0 or m < 0:
        return dmp_zero(u - 1)
    K1 = None.get_ring()
    (cf, f) = dmp_clear_denoms(f, u, K0, K1)
    (cg, g) = dmp_clear_denoms(g, u, K0, K1)
    f = dmp_convert(f, u, K0, K1)
    g = dmp_convert(g, u, K0, K1)
    r = dmp_zz_collins_resultant(f, g, u, K1)
    r = dmp_convert(r, u - 1, K1, K0)
    c = K0.convert(cf ** m * cg ** n, K1)
    return dmp_quo_ground(r, c, u - 1, K0)


def dmp_resultant(f, g, u, K, includePRS = (False,)):
    '''
    Computes resultant of two polynomials in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y - y**3 - 4
    >>> g = x**2 + x*y**3 - 9

    >>> R.dmp_resultant(f, g)
    -3*y**10 - 12*y**7 + y**6 - 54*y**4 + 8*y**3 + 729*y**2 - 216*y + 16

    '''
    if not u:
        return dup_resultant(f, g, K, includePRS = includePRS)
    if None:
        return dmp_prs_resultant(f, g, u, K)
    if None.is_Field:
        if K.is_QQ and query('USE_COLLINS_RESULTANT'):
            return dmp_qq_collins_resultant(f, g, u, K)
    if K.is_ZZ and query('USE_COLLINS_RESULTANT'):
        return dmp_zz_collins_resultant(f, g, u, K)
    return None(f, g, u, K)[0]


def dup_discriminant(f, K):
    '''
    Computes discriminant of a polynomial in `K[x]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_discriminant(x**2 + 2*x + 3)
    -8

    '''
    d = dup_degree(f)
    if d <= 0:
        return K.zero
    s = None ** (d * (d - 1) // 2)
    c = dup_LC(f, K)
    r = dup_resultant(f, dup_diff(f, 1, K), K)
    return K.quo(r, c * K(s))


def dmp_discriminant(f, u, K):
    '''
    Computes discriminant of a polynomial in `K[X]`.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y,z,t = ring("x,y,z,t", ZZ)

    >>> R.dmp_discriminant(x**2*y + x*z + t)
    -4*y*t + z**2

    '''
    if not u:
        return dup_discriminant(f, K)
    v = u - 1
    d = None(f, u)
    if d <= 0:
        return dmp_zero(v)
    s = None ** (d * (d - 1) // 2)
    c = dmp_LC(f, K)
    r = dmp_resultant(f, dmp_diff(f, 1, u, K), u, K)
    c = dmp_mul_ground(c, K(s), v, K)
    return dmp_quo(r, c, v, K)


def _dup_rr_trivial_gcd(f, g, K):
    '''Handle trivial cases in GCD algorithm over a ring. '''
    if not f and g:
        return ([], [], [])
    if not None:
        if K.is_nonnegative(dup_LC(g, K)):
            return (g, [], [
                K.one])
        return (None(g, K), [], [
            -(K.one)])
    if not None:
        if K.is_nonnegative(dup_LC(f, K)):
            return (f, [
                K.one], [])
        return (None(f, K), [
            -(K.one)], [])


def _dup_ff_trivial_gcd(f, g, K):
    '''Handle trivial cases in GCD algorithm over a field. '''
    if not f and g:
        return ([], [], [])
    if not None:
        return (dup_monic(g, K), [], [
            dup_LC(g, K)])
    if not None:
        return (dup_monic(f, K), [
            dup_LC(f, K)], [])


def _dmp_rr_trivial_gcd(f, g, u, K):
