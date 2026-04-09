# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: densetools.pyc (Python 3.11)

'''Advanced tools for dense recursive polynomials in ``K[x]`` or ``K[X]``. '''
from sympy.polys.densearith import dup_add_term, dmp_add_term, dup_lshift, dup_add, dmp_add, dup_sub, dmp_sub, dup_mul, dmp_mul, dup_sqr, dup_div, dup_rem, dmp_rem, dmp_expand, dup_mul_ground, dmp_mul_ground, dup_quo_ground, dmp_quo_ground, dup_exquo_ground, dmp_exquo_ground
from sympy.polys.densebasic import dup_strip, dmp_strip, dup_convert, dmp_convert, dup_degree, dmp_degree, dmp_to_dict, dmp_from_dict, dup_LC, dmp_LC, dmp_ground_LC, dup_TC, dmp_TC, dmp_zero, dmp_ground, dmp_zero_p, dup_to_raw_dict, dup_from_raw_dict, dmp_zeros
from sympy.polys.polyerrors import MultivariatePolynomialError, DomainError
from sympy.utilities import variations
from math import ceil as _ceil, log2 as _log2

def dup_integrate(f, m, K):
    '''
    Computes the indefinite integral of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_integrate(x**2 + 2*x, 1)
    1/3*x**3 + x**2
    >>> R.dup_integrate(x**2 + 2*x, 2)
    1/12*x**4 + 1/3*x**3

    '''
    if not m <= 0 or f:
        return f
    g = [
        None.zero] * m
    for i, c in enumerate(reversed(f)):
        n = i + 1
        for j in range(1, m):
            n *= i + j + 1
            g.insert(0, K.exquo(c, K(n)))
            return g


def dmp_integrate(f, m, u, K):
    '''
    Computes the indefinite integral of ``f`` in ``x_0`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> R.dmp_integrate(x + 2*y, 1)
    1/2*x**2 + 2*x*y
    >>> R.dmp_integrate(x + 2*y, 2)
    1/6*x**3 + x**2*y

    '''
    if not u:
        return dup_integrate(f, m, K)
    if None <= 0 or dmp_zero_p(f, u):
        return f
    v = u - 1
    g = None(m, u - 1, K)
    for i, c in enumerate(reversed(f)):
        n = i + 1
        for j in range(1, m):
            n *= i + j + 1
            g.insert(0, dmp_quo_ground(c, K(n), v, K))
            return g


def _rec_integrate_in(g, m, v, i, j, K):
    '''Recursive helper for :func:`dmp_integrate_in`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_integrate_in(f, m, j, u, K):
    '''
    Computes the indefinite integral of ``f`` in ``x_j`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> R.dmp_integrate_in(x + 2*y, 1, 0)
    1/2*x**2 + 2*x*y
    >>> R.dmp_integrate_in(x + 2*y, 1, 1)
    x*y + y**2

    '''
    if j < 0 or j > u:
        raise IndexError('0 <= j <= u expected, got u = %d, j = %d' % (u, j))
    return _rec_integrate_in(f, m, u, 0, j, K)


def dup_diff(f, m, K):
    '''
    ``m``-th order derivative of a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_diff(x**3 + 2*x**2 + 3*x + 4, 1)
    3*x**2 + 4*x + 3
    >>> R.dup_diff(x**3 + 2*x**2 + 3*x + 4, 2)
    6*x + 4

    '''
    if m <= 0:
        return f
    n = None(f)
    if n < m:
        return []
    deriv = None
    if m == 1:
        for coeff in f[:-m]:
            deriv.append(K(n) * coeff)
            n -= 1
    for coeff in f[:-m]:
        k = n
        for i in range(n - 1, n - m, -1):
            k *= i
            deriv.append(K(k) * coeff)
            n -= 1
            return dup_strip(deriv)


def dmp_diff(f, m, u, K):
    '''
    ``m``-th order derivative in ``x_0`` of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x*y**2 + 2*x*y + 3*x + 2*y**2 + 3*y + 1

    >>> R.dmp_diff(f, 1)
    y**2 + 2*y + 3
    >>> R.dmp_diff(f, 2)
    0

    '''
    if not u:
        return dup_diff(f, m, K)
    if None <= 0:
        return f
    n = None(f, u)
    if n < m:
        return dmp_zero(u)
    v = u - 1
    deriv = None
    if m == 1:
        for coeff in f[:-m]:
            deriv.append(dmp_mul_ground(coeff, K(n), v, K))
            n -= 1
    for coeff in f[:-m]:
        k = n
        for i in range(n - 1, n - m, -1):
            k *= i
            deriv.append(dmp_mul_ground(coeff, K(k), v, K))
            n -= 1
            return dmp_strip(deriv, u)


def _rec_diff_in(g, m, v, i, j, K):
    '''Recursive helper for :func:`dmp_diff_in`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_diff_in(f, m, j, u, K):
    '''
    ``m``-th order derivative in ``x_j`` of a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x*y**2 + 2*x*y + 3*x + 2*y**2 + 3*y + 1

    >>> R.dmp_diff_in(f, 1, 0)
    y**2 + 2*y + 3
    >>> R.dmp_diff_in(f, 1, 1)
    2*x*y + 2*x + 4*y + 3

    '''
    if j < 0 or j > u:
        raise IndexError(f'''0 <= j <= {u!s} expected, got {j!s}''')
    return _rec_diff_in(f, m, u, 0, j, K)


def dup_eval(f, a, K):
    '''
    Evaluate a polynomial at ``x = a`` in ``K[x]`` using Horner scheme.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_eval(x**2 + 2*x + 3, 2)
    11

    '''
    if not a:
        return K.convert(dup_TC(f, K))
    result = None.zero
    for c in f:
        result *= a
        result += c
        return result


def dmp_eval(f, a, u, K):
    '''
    Evaluate a polynomial at ``x_0 = a`` in ``K[X]`` using the Horner scheme.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_eval(2*x*y + 3*x + y + 2, 2)
    5*y + 8

    '''
    if not u:
        return dup_eval(f, a, K)
    if not None:
        return dmp_TC(f, K)
    v = u - 1
    result = None(f, K)
    for coeff in f[1:]:
        result = dmp_mul_ground(result, a, v, K)
        result = dmp_add(result, coeff, v, K)
        return result


def _rec_eval_in(g, a, v, i, j, K):
    '''Recursive helper for :func:`dmp_eval_in`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_eval_in(f, a, j, u, K):
    '''
    Evaluate a polynomial at ``x_j = a`` in ``K[X]`` using the Horner scheme.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 2*x*y + 3*x + y + 2

    >>> R.dmp_eval_in(f, 2, 0)
    5*y + 8
    >>> R.dmp_eval_in(f, 2, 1)
    7*x + 4

    '''
    if j < 0 or j > u:
        raise IndexError(f'''0 <= j <= {u!s} expected, got {j!s}''')
    return _rec_eval_in(f, a, u, 0, j, K)


def _rec_eval_tail(g, i, A, u, K):
    '''Recursive helper for :func:`dmp_eval_tail`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_eval_tail(f, A, u, K):
    '''
    Evaluate a polynomial at ``x_j = a_j, ...`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 2*x*y + 3*x + y + 2

    >>> R.dmp_eval_tail(f, [2])
    7*x + 4
    >>> R.dmp_eval_tail(f, [2, 2])
    18

    '''
    if not A:
        return f
    if None(f, u):
        return dmp_zero(u - len(A))
    e = None(f, 0, A, u, K)
    if u == len(A) - 1:
        return e
    return None(e, u - len(A))


def _rec_diff_eval(g, m, a, v, i, j, K):
    '''Recursive helper for :func:`dmp_diff_eval`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_diff_eval_in(f, m, a, j, u, K):
    '''
    Differentiate and evaluate a polynomial in ``x_j`` at ``a`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = x*y**2 + 2*x*y + 3*x + 2*y**2 + 3*y + 1

    >>> R.dmp_diff_eval_in(f, 1, 2, 0)
    y**2 + 2*y + 3
    >>> R.dmp_diff_eval_in(f, 1, 2, 1)
    6*x + 11

    '''
    if j > u:
        raise IndexError(f'''-{u!s} <= j < {u!s} expected, got {j!s}''')
    if not j:
        return dmp_eval(dmp_diff(f, m, u, K), a, u, K)
    return None(f, m, a, u, 0, j, K)


def dup_trunc(f, p, K):
    '''
    Reduce a ``K[x]`` polynomial modulo a constant ``p`` in ``K``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_trunc(2*x**3 + 3*x**2 + 5*x + 7, ZZ(3))
    -x**3 - x + 1

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_trunc(f, p, u, K):
    '''
    Reduce a ``K[X]`` polynomial modulo a polynomial ``p`` in ``K[Y]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y + 8*x**2 + 5*x*y + 6*x + 2*y + 3
    >>> g = (y - 1).drop(x)

    >>> R.dmp_trunc(f, g)
    11*x**2 + 11*x + 5

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_ground_trunc(f, p, u, K):
    '''
    Reduce a ``K[X]`` polynomial modulo a constant ``p`` in ``K``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> f = 3*x**2*y + 8*x**2 + 5*x*y + 6*x + 2*y + 3

    >>> R.dmp_ground_trunc(f, ZZ(3))
    -x**2 - x*y - y

    '''
    pass
# WARNING: Decompyle incomplete


def dup_monic(f, K):
    '''
    Divide all coefficients by ``LC(f)`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> R.dup_monic(3*x**2 + 6*x + 9)
    x**2 + 2*x + 3

    >>> R, x = ring("x", QQ)
    >>> R.dup_monic(3*x**2 + 4*x + 2)
    x**2 + 4/3*x + 2/3

    '''
    if not f:
        return f
    lc = None(f, K)
    if K.is_one(lc):
        return f
    return None(f, lc, K)


def dmp_ground_monic(f, u, K):
    '''
    Divide all coefficients by ``LC(f)`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> f = 3*x**2*y + 6*x**2 + 3*x*y + 9*y + 3

    >>> R.dmp_ground_monic(f)
    x**2*y + 2*x**2 + x*y + 3*y + 1

    >>> R, x,y = ring("x,y", QQ)
    >>> f = 3*x**2*y + 8*x**2 + 5*x*y + 6*x + 2*y + 3

    >>> R.dmp_ground_monic(f)
    x**2*y + 8/3*x**2 + 5/3*x*y + 2*x + 2/3*y + 1

    '''
    if not u:
        return dup_monic(f, K)
    if None(f, u):
        return f
    lc = None(f, u, K)
    if K.is_one(lc):
        return f
    return None(f, lc, u, K)


def dup_content(f, K):
    '''
    Compute the GCD of coefficients of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> f = 6*x**2 + 8*x + 12

    >>> R.dup_content(f)
    2

    >>> R, x = ring("x", QQ)
    >>> f = 6*x**2 + 8*x + 12

    >>> R.dup_content(f)
    2

    '''
    QQ = QQ
    import sympy.polys.domains
    if not f:
        return K.zero
    cont = None.zero
    if K == QQ:
        for c in f:
            cont = K.gcd(cont, c)
    for c in f:
        cont = K.gcd(cont, c)
        if K.is_one(cont):
            pass
        
        return cont


def dmp_ground_content(f, u, K):
    '''
    Compute the GCD of coefficients of ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> f = 2*x*y + 6*x + 4*y + 12

    >>> R.dmp_ground_content(f)
    2

    >>> R, x,y = ring("x,y", QQ)
    >>> f = 2*x*y + 6*x + 4*y + 12

    >>> R.dmp_ground_content(f)
    2

    '''
    QQ = QQ
    import sympy.polys.domains
    if not u:
        return dup_content(f, K)
    if None(f, u):
        return K.zero
    v = u - 1
    cont = None.zero
    if K == QQ:
        for c in f:
            cont = K.gcd(cont, dmp_ground_content(c, v, K))
    for c in f:
        cont = K.gcd(cont, dmp_ground_content(c, v, K))
        if K.is_one(cont):
            pass
        
        return cont


def dup_primitive(f, K):
    '''
    Compute content and the primitive form of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> f = 6*x**2 + 8*x + 12

    >>> R.dup_primitive(f)
    (2, 3*x**2 + 4*x + 6)

    >>> R, x = ring("x", QQ)
    >>> f = 6*x**2 + 8*x + 12

    >>> R.dup_primitive(f)
    (2, 3*x**2 + 4*x + 6)

    '''
    if not f:
        return (K.zero, f)
    cont = None(f, K)
    if K.is_one(cont):
        return (cont, f)
    return (None, dup_quo_ground(f, cont, K))


def dmp_ground_primitive(f, u, K):
    '''
    Compute content and the primitive form of ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> f = 2*x*y + 6*x + 4*y + 12

    >>> R.dmp_ground_primitive(f)
    (2, x*y + 3*x + 2*y + 6)

    >>> R, x,y = ring("x,y", QQ)
    >>> f = 2*x*y + 6*x + 4*y + 12

    >>> R.dmp_ground_primitive(f)
    (2, x*y + 3*x + 2*y + 6)

    '''
    if not u:
        return dup_primitive(f, K)
    if None(f, u):
        return (K.zero, f)
    cont = None(f, u, K)
    if K.is_one(cont):
        return (cont, f)
    return (None, dmp_quo_ground(f, cont, u, K))


def dup_extract(f, g, K):
    '''
    Extract common content from a pair of polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_extract(6*x**2 + 12*x + 18, 4*x**2 + 8*x + 12)
    (2, 3*x**2 + 6*x + 9, 2*x**2 + 4*x + 6)

    '''
    fc = dup_content(f, K)
    gc = dup_content(g, K)
    gcd = K.gcd(fc, gc)
    if not K.is_one(gcd):
        f = dup_quo_ground(f, gcd, K)
        g = dup_quo_ground(g, gcd, K)
    return (gcd, f, g)


def dmp_ground_extract(f, g, u, K):
    '''
    Extract common content from a pair of polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_ground_extract(6*x*y + 12*x + 18, 4*x*y + 8*x + 12)
    (2, 3*x*y + 6*x + 9, 2*x*y + 4*x + 6)

    '''
    fc = dmp_ground_content(f, u, K)
    gc = dmp_ground_content(g, u, K)
    gcd = K.gcd(fc, gc)
    if not K.is_one(gcd):
        f = dmp_quo_ground(f, gcd, u, K)
        g = dmp_quo_ground(g, gcd, u, K)
    return (gcd, f, g)


def dup_real_imag(f, K):
    '''
    Find ``f1`` and ``f2``, such that ``f(x+I*y) = f1(x,y) + f2(x,y)*I``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dup_real_imag(x**3 + x**2 + x + 1)
    (x**3 + x**2 - 3*x*y**2 + x - y**2 + 1, 3*x**2*y + 2*x*y - y**3 + y)

    >>> from sympy.abc import x, y, z
    >>> from sympy import I
    >>> (z**3 + z**2 + z + 1).subs(z, x+I*y).expand().collect(I)
    x**3 + x**2 - 3*x*y**2 + x - y**2 + I*(3*x**2*y + 2*x*y - y**3 + y) + 1

    '''
    if not K.is_ZZ and K.is_QQ:
        raise DomainError('computing real and imaginary parts is not supported over %s' % K)
    f1 = dmp_zero(1)
    f2 = dmp_zero(1)
    if not f:
        return (f1, f2)
    g = [
        [
            [
                None.one,
                K.zero]],
        [
            [
                K.one],
            []]]
    h = dmp_ground(f[0], 2)
    for c in f[1:]:
        h = dmp_mul(h, g, 2, K)
        h = dmp_add_term(h, dmp_ground(c, 1), 0, 2, K)
        H = dup_to_raw_dict(h)
        for k, h in H.items():
            m = k % 4
            if not m:
                f1 = dmp_add(f1, h, 1, K)
                continue
            if m == 1:
                f2 = dmp_add(f2, h, 1, K)
                continue
            if m == 2:
                f1 = dmp_sub(f1, h, 1, K)
                continue
            f2 = dmp_sub(f2, h, 1, K)
            return (f1, f2)


def dup_mirror(f, K):
    '''
    Evaluate efficiently the composition ``f(-x)`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mirror(x**3 + 2*x**2 - 4*x + 2)
    -x**3 + 2*x**2 + 4*x + 2

    '''
    f = list(f)
    for i in range(len(f) - 2, -1, -2):
        f[i] = -f[i]
        return f


def dup_scale(f, a, K):
    '''
    Evaluate efficiently composition ``f(a*x)`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_scale(x**2 - 2*x + 1, ZZ(2))
    4*x**2 - 4*x + 1

    '''
    b = a
    n = len(f) - 1
    f = list(f)
    for i in range(n - 1, -1, -1):
        f[i], b = b * f[i], b * a
        return f


def dup_shift(f, a, K):
    '''
    Evaluate efficiently Taylor shift ``f(x + a)`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_shift(x**2 - 2*x + 1, ZZ(2))
    x**2 + 2*x + 1

    '''
    n = len(f) - 1
    f = list(f)
    for i in range(n, 0, -1):
        for j in range(0, i):
            return f


def dmp_shift(f, a, u, K):
    """
    Evaluate efficiently Taylor shift ``f(X + A)`` in ``K[X]``.

    Examples
    ========

    >>> from sympy import symbols, ring, ZZ
    >>> x, y = symbols('x y')
    >>> R, _, _ = ring([x, y], ZZ)

    >>> p = x**2*y + 2*x*y + 3*x + 4*y + 5

    >>> R.dmp_shift(R(p), [ZZ(1), ZZ(2)])
    x**2*y + 2*x**2 + 4*x*y + 11*x + 7*y + 22

    >>> p.subs({x: x + 1, y: y + 2}).expand()
    x**2*y + 2*x**2 + 4*x*y + 11*x + 7*y + 22
    """
    pass
# WARNING: Decompyle incomplete


def dup_transform(f, p, q, K):
    '''
    Evaluate functional transformation ``q**n * f(p/q)`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_transform(x**2 - 2*x + 1, x**2 + 1, x - 1)
    x**4 - 2*x**3 + 5*x**2 - 4*x + 4

    '''
    if not f:
        return []
    n = None(f) - 1
    Q = [
        [
            K.one]]
    h = [
        f[0]]
    for i in range(0, n):
        Q.append(dup_mul(Q[-1], q, K))
        for c, q in zip(f[1:], Q[1:]):
            h = dup_mul(h, p, K)
            q = dup_mul_ground(q, c, K)
            h = dup_add(h, q, K)
            return h


def dup_compose(f, g, K):
    '''
    Evaluate functional composition ``f(g)`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_compose(x**2 + x, x - 1)
    x**2 - x

    '''
    if len(g) <= 1:
        return dup_strip([
            dup_eval(f, dup_LC(g, K), K)])
    if not None:
        return []
    h = [
        None[0]]
    for c in f[1:]:
        h = dup_mul(h, g, K)
        h = dup_add_term(h, c, 0, K)
        return h


def dmp_compose(f, g, u, K):
    '''
    Evaluate functional composition ``f(g)`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_compose(x*y + 2*x + y, y)
    y**2 + 3*y

    '''
    if not u:
        return dup_compose(f, g, K)
    if None(f, u):
        return f
    h = [
        None[0]]
    for c in f[1:]:
        h = dmp_mul(h, g, u, K)
        h = dmp_add_term(h, c, 0, u, K)
        return h


def _dup_right_decompose(f, s, K):
    '''Helper function for :func:`_dup_decompose`.'''
    n = len(f) - 1
    lc = dup_LC(f, K)
    f = dup_to_raw_dict(f)
    g = {
        s: K.one }
    r = n // s
    for i in range(1, s):
        coeff = K.zero
        for j in range(0, i):
            if n + j - i not in f:
                continue
            if s - j not in g:
                continue
            gc = g[s - j]
            fc = f[n + j - i]
            coeff += (i - r * j) * fc * gc
            g[s - i] = K.quo(coeff, i * r * lc)
            return dup_from_raw_dict(g, K)


def _dup_left_decompose(f, h, K):
    '''Helper function for :func:`_dup_decompose`.'''
    i = 0
    g = { }
# WARNING: Decompyle incomplete


def _dup_decompose(f, K):
    '''Helper function for :func:`dup_decompose`.'''
    df = len(f) - 1
# WARNING: Decompyle incomplete


def dup_decompose(f, K):
    '''
    Computes functional decomposition of ``f`` in ``K[x]``.

    Given a univariate polynomial ``f`` with coefficients in a field of
    characteristic zero, returns list ``[f_1, f_2, ..., f_n]``, where::

              f = f_1 o f_2 o ... f_n = f_1(f_2(... f_n))

    and ``f_2, ..., f_n`` are monic and homogeneous polynomials of at
    least second degree.

    Unlike factorization, complete functional decompositions of
    polynomials are not unique, consider examples:

    1. ``f o g = f(x + b) o (g - b)``
    2. ``x**n o x**m = x**m o x**n``
    3. ``T_n o T_m = T_m o T_n``

    where ``T_n`` and ``T_m`` are Chebyshev polynomials.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_decompose(x**4 - 2*x**3 + x**2)
    [x**2, x**2 - x]

    References
    ==========

    .. [1] [Kozen89]_

    '''
    F = []
    result = _dup_decompose(f, K)
# WARNING: Decompyle incomplete


def dmp_lift(f, u, K):
    '''
    Convert algebraic coefficients to integers in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> from sympy import I

    >>> K = QQ.algebraic_field(I)
    >>> R, x = ring("x", K)

    >>> f = x**2 + K([QQ(1), QQ(0)])*x + K([QQ(2), QQ(0)])

    >>> R.dmp_lift(f)
    x**8 + 2*x**6 + 9*x**4 - 8*x**2 + 16

    '''
    if K.is_GaussianField:
        K1 = K.as_AlgebraicField()
        f = dmp_convert(f, u, K, K1)
        K = K1
    if not K.is_Algebraic:
        raise DomainError('computation can be done only in an algebraic domain')
    polys = []
    monoms = []
    F = dmp_to_dict(f, u)
    for monom, coeff in F.items():
        if not coeff.is_ground:
            monoms.append(monom)
        perms = variations([
            -1,
            1], len(monoms), repetition = True)
        for perm in perms:
            G = dict(F)
            for sign, monom in zip(perm, monoms):
                if sign == -1:
                    G[monom] = -G[monom]
                polys.append(dmp_from_dict(G, u, K))
                return dmp_convert(dmp_expand(polys, u, K), u, K, K.dom)


def dup_sign_variations(f, K):
    '''
    Compute the number of sign variations of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sign_variations(x**4 - x**2 - x + 1)
    2

    '''
    k = 0
    prev = K.zero
    for coeff in f:
        if K.is_negative(coeff * prev):
            k += 1
        if coeff:
            prev = coeff
        return k


def dup_clear_denoms(f, K0, K1, convert = (None, False)):
    '''
    Clear denominators, i.e. transform ``K_0`` to ``K_1``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = QQ(1,2)*x + QQ(1,3)

    >>> R.dup_clear_denoms(f, convert=False)
    (6, 3*x + 2)
    >>> R.dup_clear_denoms(f, convert=True)
    (6, 3*x + 2)

    '''
    pass
# WARNING: Decompyle incomplete


def _rec_clear_denoms(g, v, K0, K1):
    '''Recursive helper for :func:`dmp_clear_denoms`.'''
    common = K1.one
    if not v:
        for c in g:
            common = K1.lcm(common, K0.denom(c))
    w = v - 1
    for c in g:
        common = K1.lcm(common, _rec_clear_denoms(c, w, K0, K1))
        return common


def dmp_clear_denoms(f, u, K0, K1, convert = (None, False)):
    '''
    Clear denominators, i.e. transform ``K_0`` to ``K_1``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> f = QQ(1,2)*x + QQ(1,3)*y + 1

    >>> R.dmp_clear_denoms(f, convert=False)
    (6, 3*x + 2*y + 6)
    >>> R.dmp_clear_denoms(f, convert=True)
    (6, 3*x + 2*y + 6)

    '''
    if not u:
        return dup_clear_denoms(f, K0, K1, convert = convert)
# WARNING: Decompyle incomplete


def dup_revert(f, n, K):
    '''
    Compute ``f**(-1)`` mod ``x**n`` using Newton iteration.

    This function computes first ``2**n`` terms of a polynomial that
    is a result of inversion of a polynomial modulo ``x**n``. This is
    useful to efficiently compute series expansion of ``1/f``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> f = -QQ(1,720)*x**6 + QQ(1,24)*x**4 - QQ(1,2)*x**2 + 1

    >>> R.dup_revert(f, 8)
    61/720*x**6 + 5/24*x**4 + 1/2*x**2 + 1

    '''
    g = [
        K.revert(dup_TC(f, K))]
    h = [
        K.one,
        K.zero,
        K.zero]
    N = int(_ceil(_log2(n)))
    for i in range(1, N + 1):
        a = dup_mul_ground(g, K(2), K)
        b = dup_mul(f, dup_sqr(g, K), K)
        g = dup_rem(dup_sub(a, b, K), h, K)
        h = dup_lshift(h, dup_degree(h), K)
        return g


def dmp_revert(f, g, u, K):
    '''
    Compute ``f**(-1)`` mod ``x**n`` using Newton iteration.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    '''
    if not u:
        return dup_revert(f, g, K)
    raise None(f, g)
