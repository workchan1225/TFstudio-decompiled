# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: densearith.pyc (Python 3.11)

'''Arithmetics for dense recursive polynomials in ``K[x]`` or ``K[X]``. '''
from sympy.polys.densebasic import dup_slice, dup_LC, dmp_LC, dup_degree, dmp_degree, dup_strip, dmp_strip, dmp_zero_p, dmp_zero, dmp_one_p, dmp_one, dmp_ground, dmp_zeros
from sympy.polys.polyerrors import ExactQuotientFailed, PolynomialDivisionFailed

def dup_add_term(f, c, i, K):
    '''
    Add ``c*x**i`` to ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add_term(x**2 - 1, ZZ(2), 4)
    2*x**4 + x**2 - 1

    '''
    if not c:
        return f
    n = None(f)
    m = n - i - 1
    if i == n - 1:
        return dup_strip([
            f[0] + c] + f[1:])
    if None >= n:
        return [
            c] + [
            K.zero] * (i - n) + f
    return None[:m] + [
        f[m] + c] + f[m + 1:]


def dmp_add_term(f, c, i, u, K):
    '''
    Add ``c(x_2..x_u)*x_0**i`` to ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add_term(x*y + 1, 2, 2)
    2*x**2 + x*y + 1

    '''
    if not u:
        return dup_add_term(f, c, i, K)
    v = None - 1
    if dmp_zero_p(c, v):
        return f
    n = None(f)
    m = n - i - 1
    if i == n - 1:
        return dmp_strip([
            dmp_add(f[0], c, v, K)] + f[1:], u)
    if None >= n:
        return [
            c] + dmp_zeros(i - n, v, K) + f
    return None[:m] + [
        dmp_add(f[m], c, v, K)] + f[m + 1:]


def dup_sub_term(f, c, i, K):
    '''
    Subtract ``c*x**i`` from ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub_term(2*x**4 + x**2 - 1, ZZ(2), 4)
    x**2 - 1

    '''
    if not c:
        return f
    n = None(f)
    m = n - i - 1
    if i == n - 1:
        return dup_strip([
            f[0] - c] + f[1:])
    if None >= n:
        return [
            -c] + [
            K.zero] * (i - n) + f
    return None[:m] + [
        f[m] - c] + f[m + 1:]


def dmp_sub_term(f, c, i, u, K):
    '''
    Subtract ``c(x_2..x_u)*x_0**i`` from ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub_term(2*x**2 + x*y + 1, 2, 2)
    x*y + 1

    '''
    if not u:
        return dup_add_term(f, -c, i, K)
    v = None - 1
    if dmp_zero_p(c, v):
        return f
    n = None(f)
    m = n - i - 1
    if i == n - 1:
        return dmp_strip([
            dmp_sub(f[0], c, v, K)] + f[1:], u)
    if None >= n:
        return [
            dmp_neg(c, v, K)] + dmp_zeros(i - n, v, K) + f
    return None[:m] + [
        dmp_sub(f[m], c, v, K)] + f[m + 1:]


def dup_mul_term(f, c, i, K):
    '''
    Multiply ``f`` by ``c*x**i`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mul_term(x**2 - 1, ZZ(3), 2)
    3*x**4 - 3*x**2

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_mul_term(f, c, i, u, K):
    '''
    Multiply ``f`` by ``c(x_2..x_u)*x_0**i`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_mul_term(x**2*y + x, 3*y, 2)
    3*x**4*y**2 + 3*x**3*y

    '''
    pass
# WARNING: Decompyle incomplete


def dup_add_ground(f, c, K):
    '''
    Add an element of the ground domain to ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x + 8

    '''
    return dup_add_term(f, c, 0, K)


def dmp_add_ground(f, c, u, K):
    '''
    Add an element of the ground domain to ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x + 8

    '''
    return dmp_add_term(f, dmp_ground(c, u - 1), 0, u, K)


def dup_sub_ground(f, c, K):
    '''
    Subtract an element of the ground domain from ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x

    '''
    return dup_sub_term(f, c, 0, K)


def dmp_sub_ground(f, c, u, K):
    '''
    Subtract an element of the ground domain from ``f``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub_ground(x**3 + 2*x**2 + 3*x + 4, ZZ(4))
    x**3 + 2*x**2 + 3*x

    '''
    return dmp_sub_term(f, dmp_ground(c, u - 1), 0, u, K)


def dup_mul_ground(f, c, K):
    '''
    Multiply ``f`` by a constant value in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mul_ground(x**2 + 2*x - 1, ZZ(3))
    3*x**2 + 6*x - 3

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_mul_ground(f, c, u, K):
    '''
    Multiply ``f`` by a constant value in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_mul_ground(2*x + 2*y, ZZ(3))
    6*x + 6*y

    '''
    pass
# WARNING: Decompyle incomplete


def dup_quo_ground(f, c, K):
    '''
    Quotient by a constant in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x = ring("x", ZZ)
    >>> R.dup_quo_ground(3*x**2 + 2, ZZ(2))
    x**2 + 1

    >>> R, x = ring("x", QQ)
    >>> R.dup_quo_ground(3*x**2 + 2, QQ(2))
    3/2*x**2 + 1

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_quo_ground(f, c, u, K):
    '''
    Quotient by a constant in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ, QQ

    >>> R, x,y = ring("x,y", ZZ)
    >>> R.dmp_quo_ground(2*x**2*y + 3*x, ZZ(2))
    x**2*y + x

    >>> R, x,y = ring("x,y", QQ)
    >>> R.dmp_quo_ground(2*x**2*y + 3*x, QQ(2))
    x**2*y + 3/2*x

    '''
    pass
# WARNING: Decompyle incomplete


def dup_exquo_ground(f, c, K):
    '''
    Exact quotient by a constant in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_exquo_ground(x**2 + 2, QQ(2))
    1/2*x**2 + 1

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_exquo_ground(f, c, u, K):
    '''
    Exact quotient by a constant in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x,y = ring("x,y", QQ)

    >>> R.dmp_exquo_ground(x**2*y + 2*x, QQ(2))
    1/2*x**2*y + x

    '''
    pass
# WARNING: Decompyle incomplete


def dup_lshift(f, n, K):
    '''
    Efficiently multiply ``f`` by ``x**n`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_lshift(x**2 + 1, 2)
    x**4 + x**2

    '''
    if not f:
        return f
    return None + [
        K.zero] * n


def dup_rshift(f, n, K):
    '''
    Efficiently divide ``f`` by ``x**n`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_rshift(x**4 + x**2, 2)
    x**2 + 1
    >>> R.dup_rshift(x**4 + x**2 + 2, 2)
    x**2 + 1

    '''
    return f[:-n]


def dup_abs(f, K):
    '''
    Make all coefficients positive in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_abs(x**2 - 1)
    x**2 + 1

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_abs(f, u, K):
    '''
    Make all coefficients positive in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_abs(x**2*y - x)
    x**2*y + x

    '''
    pass
# WARNING: Decompyle incomplete


def dup_neg(f, K):
    '''
    Negate a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_neg(x**2 - 1)
    -x**2 + 1

    '''
    return f()


def dmp_neg(f, u, K):
    '''
    Negate a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_neg(x**2*y - x)
    -x**2*y + x

    '''
    pass
# WARNING: Decompyle incomplete


def dup_add(f, g, K):
    '''
    Add dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add(x**2 - 1, x - 2)
    x**2 + x - 3

    '''
    if not f:
        return g
    if not None:
        return f
    df = None(f)
    dg = dup_degree(g)
    if df == dg:
        return (lambda .0: [ a + b for a, b in .0 ])(zip(f, g)())
    k = None(df - dg)
    if df > dg:
        f = f[k:]
        h = f[:k]
    else:
        g = g[k:]
        h = g[:k]
    return (lambda .0: [ a + b for a, b in .0 ]) + zip(f, g)()


def dmp_add(f, g, u, K):
    '''
    Add dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add(x**2 + y, x**2*y + x)
    x**2*y + x**2 + x + y

    '''
    pass
# WARNING: Decompyle incomplete


def dup_sub(f, g, K):
    '''
    Subtract dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub(x**2 - 1, x - 2)
    x**2 - x + 1

    '''
    if not f:
        return dup_neg(g, K)
    if not None:
        return f
    df = None(f)
    dg = dup_degree(g)
    if df == dg:
        return (lambda .0: [ a - b for a, b in .0 ])(zip(f, g)())
    k = None(df - dg)
    if df > dg:
        f = f[k:]
        h = f[:k]
    else:
        g = g[k:]
        h = dup_neg(g[:k], K)
    return (lambda .0: [ a - b for a, b in .0 ]) + zip(f, g)()


def dmp_sub(f, g, u, K):
    '''
    Subtract dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub(x**2 + y, x**2*y + x)
    -x**2*y + x**2 - x + y

    '''
    pass
# WARNING: Decompyle incomplete


def dup_add_mul(f, g, h, K):
    '''
    Returns ``f + g*h`` where ``f, g, h`` are in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_add_mul(x**2 - 1, x - 2, x + 2)
    2*x**2 - 5

    '''
    return dup_add(f, dup_mul(g, h, K), K)


def dmp_add_mul(f, g, h, u, K):
    '''
    Returns ``f + g*h`` where ``f, g, h`` are in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_add_mul(x**2 + y, x, x + 2)
    2*x**2 + 2*x + y

    '''
    return dmp_add(f, dmp_mul(g, h, u, K), u, K)


def dup_sub_mul(f, g, h, K):
    '''
    Returns ``f - g*h`` where ``f, g, h`` are in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sub_mul(x**2 - 1, x - 2, x + 2)
    3

    '''
    return dup_sub(f, dup_mul(g, h, K), K)


def dmp_sub_mul(f, g, h, u, K):
    '''
    Returns ``f - g*h`` where ``f, g, h`` are in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sub_mul(x**2 + y, x, x + 2)
    -2*x + y

    '''
    return dmp_sub(f, dmp_mul(g, h, u, K), u, K)


def dup_mul(f, g, K):
    '''
    Multiply dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_mul(x - 2, x + 2)
    x**2 - 4

    '''
    if f == g:
        return dup_sqr(f, K)
    if not None or g:
        return []
    df = None(f)
    dg = dup_degree(g)
    n = max(df, dg) + 1
    if n < 100:
        h = []
        for i in range(0, df + dg + 1):
            coeff = K.zero
            for j in range(max(0, i - dg), min(df, i) + 1):
                coeff += f[j] * g[i - j]
                h.append(coeff)
                return dup_strip(h)
                n2 = n // 2
                gl = dup_slice(g, 0, n2, K)
                fl = dup_slice(f, 0, n2, K)
                fh = dup_rshift(dup_slice(f, n2, n, K), n2, K)
                gh = dup_rshift(dup_slice(g, n2, n, K), n2, K)
                hi = dup_mul(fh, gh, K)
                lo = dup_mul(fl, gl, K)
                mid = dup_mul(dup_add(fl, fh, K), dup_add(gl, gh, K), K)
                mid = dup_sub(mid, dup_add(lo, hi, K), K)
                return dup_add(dup_add(lo, dup_lshift(mid, n2, K), K), dup_lshift(hi, 2 * n2, K), K)


def dmp_mul(f, g, u, K):
    '''
    Multiply dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_mul(x*y + 1, x)
    x**2*y + x

    '''
    if not u:
        return dup_mul(f, g, K)
    if None == g:
        return dmp_sqr(f, u, K)
    df = None(f, u)
    if df < 0:
        return f
    dg = None(g, u)
    if dg < 0:
        return g
    v = u - 1
    h = None
    for i in range(0, df + dg + 1):
        coeff = dmp_zero(v)
        for j in range(max(0, i - dg), min(df, i) + 1):
            coeff = dmp_add(coeff, dmp_mul(f[j], g[i - j], v, K), v, K)
            h.append(coeff)
            return dmp_strip(h, u)


def dup_sqr(f, K):
    '''
    Square dense polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x = ring("x", ZZ)

    >>> R.dup_sqr(x**2 + 1)
    x**4 + 2*x**2 + 1

    '''
    h = []
    df = len(f) - 1
    for i in range(0, 2 * df + 1):
        c = K.zero
        jmin = max(0, i - df)
        jmax = min(i, df)
        n = (jmax - jmin) + 1
        jmax = jmin + n // 2 - 1
        for j in range(jmin, jmax + 1):
            c += f[j] * f[i - j]
            c += c
            if n & 1:
                elem = f[jmax + 1]
                c += elem ** 2
        h.append(c)
        return dup_strip(h)


def dmp_sqr(f, u, K):
    '''
    Square dense polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys import ring, ZZ
    >>> R, x,y = ring("x,y", ZZ)

    >>> R.dmp_sqr(x**2 + x*y + y**2)
    x**4 + 2*x**3*y + 3*x**2*y**2 + 2*x*y**3 + y**4

    '''
    if not u:
        return dup_sqr(f, K)
    df = None(f, u)
    if df < 0:
        return f
    v = u - 1
    h = None
    for i in range(0, 2 * df + 1):
        c = dmp_zero(v)
        jmin = max(0, i - df)
        jmax = min(i, df)
        n = (jmax - jmin) + 1
        jmax = jmin + n // 2 - 1
        for j in range(jmin, jmax + 1):
            c = dmp_add(c, dmp_mul(f[j], f[i - j], v, K), v, K)
            c = dmp_mul_ground(c, K(2), v, K)
            if n & 1:
                elem = dmp_sqr(f[jmax + 1], v, K)
                c = dmp_add(c, elem, v, K)
        h.append(c)
        return dmp_strip(h, u)


def dup_pow(f, n, K):
