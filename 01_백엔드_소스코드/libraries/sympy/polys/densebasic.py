# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: densebasic.pyc (Python 3.11)

'''Basic tools for dense recursive polynomials in ``K[x]`` or ``K[X]``. '''
from sympy.core import igcd
from sympy.polys.monomials import monomial_min, monomial_div
from sympy.polys.orderings import monomial_key
import random
ninf = float('-inf')

def poly_LC(f, K):
    '''
    Return leading coefficient of ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import poly_LC

    >>> poly_LC([], ZZ)
    0
    >>> poly_LC([ZZ(1), ZZ(2), ZZ(3)], ZZ)
    1

    '''
    if not f:
        return K.zero
    return None[0]


def poly_TC(f, K):
    '''
    Return trailing coefficient of ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import poly_TC

    >>> poly_TC([], ZZ)
    0
    >>> poly_TC([ZZ(1), ZZ(2), ZZ(3)], ZZ)
    3

    '''
    if not f:
        return K.zero
    return None[-1]

dup_LC = poly_LC
dmp_LC = poly_LC
dup_TC = poly_TC
dmp_TC = poly_TC

def dmp_ground_LC(f, u, K):
    '''
    Return the ground leading coefficient.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_ground_LC

    >>> f = ZZ.map([[[1], [2, 3]]])

    >>> dmp_ground_LC(f, 2, ZZ)
    1

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_ground_TC(f, u, K):
    '''
    Return the ground trailing coefficient.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_ground_TC

    >>> f = ZZ.map([[[1], [2, 3]]])

    >>> dmp_ground_TC(f, 2, ZZ)
    3

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_true_LT(f, u, K):
    '''
    Return the leading term ``c * x_1**n_1 ... x_k**n_k``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_true_LT

    >>> f = ZZ.map([[4], [2, 0], [3, 0, 0]])

    >>> dmp_true_LT(f, 1, ZZ)
    ((2, 0), 4)

    '''
    monom = []
# WARNING: Decompyle incomplete


def dup_degree(f):
    """
    Return the leading degree of ``f`` in ``K[x]``.

    Note that the degree of 0 is negative infinity (``float('-inf')``).

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_degree

    >>> f = ZZ.map([1, 2, 0, 3])

    >>> dup_degree(f)
    3

    """
    if not f:
        return ninf
    return None(f) - 1


def dmp_degree(f, u):
    """
    Return the leading degree of ``f`` in ``x_0`` in ``K[X]``.

    Note that the degree of 0 is negative infinity (``float('-inf')``).

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_degree

    >>> dmp_degree([[[]]], 2)
    -inf

    >>> f = ZZ.map([[2], [1, 2, 3]])

    >>> dmp_degree(f, 1)
    1

    """
    if dmp_zero_p(f, u):
        return ninf
    return None(f) - 1


def _rec_degree_in(g, v, i, j):
    '''Recursive helper function for :func:`dmp_degree_in`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_degree_in(f, j, u):
    '''
    Return the leading degree of ``f`` in ``x_j`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_degree_in

    >>> f = ZZ.map([[2], [1, 2, 3]])

    >>> dmp_degree_in(f, 0, 1)
    1
    >>> dmp_degree_in(f, 1, 1)
    2

    '''
    if not j:
        return dmp_degree(f, u)
    if None < 0 or j > u:
        raise IndexError(f'''0 <= j <= {u!s} expected, got {j!s}''')
    return _rec_degree_in(f, u, 0, j)


def _rec_degree_list(g, v, i, degs):
    '''Recursive helper for :func:`dmp_degree_list`.'''
    degs[i] = max(degs[i], dmp_degree(g, v))
    if v > 0:
        i = i + 1
        v = v - 1
        for c in g:
            _rec_degree_list(c, v, i, degs)
            return None
            return None


def dmp_degree_list(f, u):
    '''
    Return a list of degrees of ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_degree_list

    >>> f = ZZ.map([[1], [1, 2, 3]])

    >>> dmp_degree_list(f, 1)
    (1, 2)

    '''
    degs = [
        ninf] * (u + 1)
    _rec_degree_list(f, u, 0, degs)
    return tuple(degs)


def dup_strip(f):
    '''
    Remove leading zeros from ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.densebasic import dup_strip

    >>> dup_strip([0, 0, 1, 2, 3, 0])
    [1, 2, 3, 0]

    '''
    if f or f[0]:
        return f
    i = None
    for cf in f:
        if cf:
            pass
        else:
            i += 1
        return f[i:]


def dmp_strip(f, u):
    '''
    Remove leading zeros from ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_strip

    >>> dmp_strip([[], [0, 1, 2], [1]], 1)
    [[0, 1, 2], [1]]

    '''
    if not u:
        return dup_strip(f)
    if None(f, u):
        return f
    v = u - 1
    i = None
    for c in f:
        if not dmp_zero_p(c, v):
            pass
        else:
            i += 1
        if i == len(f):
            return dmp_zero(u)
        return None[i:]


def _rec_validate(f, g, i, K):
    '''Recursive helper for :func:`dmp_validate`.'''
    pass
# WARNING: Decompyle incomplete


def _rec_strip(g, v):
    '''Recursive helper for :func:`_rec_strip`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_validate(f, K = (None,)):
    '''
    Return the number of levels in ``f`` and recursively strip it.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_validate

    >>> dmp_validate([[], [0, 1, 2], [1]])
    ([[1, 2], [1]], 1)

    >>> dmp_validate([[1], 1])
    Traceback (most recent call last):
    ...
    ValueError: invalid data structure for a multivariate polynomial

    '''
    levels = _rec_validate(f, f, 0, K)
    u = levels.pop()
    if not levels:
        return (_rec_strip(f, u), u)
    raise None('invalid data structure for a multivariate polynomial')


def dup_reverse(f):
    '''
    Compute ``x**n * f(1/x)``, i.e.: reverse ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_reverse

    >>> f = ZZ.map([1, 2, 3, 0])

    >>> dup_reverse(f)
    [3, 2, 1]

    '''
    return dup_strip(list(reversed(f)))


def dup_copy(f):
    '''
    Create a new copy of a polynomial ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_copy

    >>> f = ZZ.map([1, 2, 3, 0])

    >>> dup_copy([1, 2, 3, 0])
    [1, 2, 3, 0]

    '''
    return list(f)


def dmp_copy(f, u):
    '''
    Create a new copy of a polynomial ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_copy

    >>> f = ZZ.map([[1], [1, 2]])

    >>> dmp_copy(f, 1)
    [[1], [1, 2]]

    '''
    pass
# WARNING: Decompyle incomplete


def dup_to_tuple(f):
    '''
    Convert `f` into a tuple.

    This is needed for hashing. This is similar to dup_copy().

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_copy

    >>> f = ZZ.map([1, 2, 3, 0])

    >>> dup_copy([1, 2, 3, 0])
    [1, 2, 3, 0]

    '''
    return tuple(f)


def dmp_to_tuple(f, u):
    '''
    Convert `f` into a nested tuple of tuples.

    This is needed for hashing.  This is similar to dmp_copy().

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_to_tuple

    >>> f = ZZ.map([[1], [1, 2]])

    >>> dmp_to_tuple(f, 1)
    ((1,), (1, 2))

    '''
    pass
# WARNING: Decompyle incomplete


def dup_normal(f, K):
    '''
    Normalize univariate polynomial in the given domain.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_normal

    >>> dup_normal([0, 1, 2, 3], ZZ)
    [1, 2, 3]

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_normal(f, u, K):
    '''
    Normalize a multivariate polynomial in the given domain.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_normal

    >>> dmp_normal([[], [0, 1, 2]], 1, ZZ)
    [[1, 2]]

    '''
    pass
# WARNING: Decompyle incomplete


def dup_convert(f, K0, K1):
    '''
    Convert the ground domain of ``f`` from ``K0`` to ``K1``.

    Examples
    ========

    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_convert

    >>> R, x = ring("x", ZZ)

    >>> dup_convert([R(1), R(2)], R.to_domain(), ZZ)
    [1, 2]
    >>> dup_convert([ZZ(1), ZZ(2)], ZZ, R.to_domain())
    [1, 2]

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_convert(f, u, K0, K1):
    '''
    Convert the ground domain of ``f`` from ``K0`` to ``K1``.

    Examples
    ========

    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_convert

    >>> R, x = ring("x", ZZ)

    >>> dmp_convert([[R(1)], [R(2)]], 1, R.to_domain(), ZZ)
    [[1], [2]]
    >>> dmp_convert([[ZZ(1)], [ZZ(2)]], 1, ZZ, R.to_domain())
    [[1], [2]]

    '''
    pass
# WARNING: Decompyle incomplete


def dup_from_sympy(f, K):
    '''
    Convert the ground domain of ``f`` from SymPy to ``K``.

    Examples
    ========

    >>> from sympy import S
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_from_sympy

    >>> dup_from_sympy([S(1), S(2)], ZZ) == [ZZ(1), ZZ(2)]
    True

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_from_sympy(f, u, K):
    '''
    Convert the ground domain of ``f`` from SymPy to ``K``.

    Examples
    ========

    >>> from sympy import S
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_from_sympy

    >>> dmp_from_sympy([[S(1)], [S(2)]], 1, ZZ) == [[ZZ(1)], [ZZ(2)]]
    True

    '''
    pass
# WARNING: Decompyle incomplete


def dup_nth(f, n, K):
    '''
    Return the ``n``-th coefficient of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_nth

    >>> f = ZZ.map([1, 2, 3])

    >>> dup_nth(f, 0, ZZ)
    3
    >>> dup_nth(f, 4, ZZ)
    0

    '''
    if n < 0:
        raise IndexError("'n' must be non-negative, got %i" % n)
    if n >= len(f):
        return K.zero
    return None[dup_degree(f) - n]


def dmp_nth(f, n, u, K):
    '''
    Return the ``n``-th coefficient of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_nth

    >>> f = ZZ.map([[1], [2], [3]])

    >>> dmp_nth(f, 0, 1, ZZ)
    [3]
    >>> dmp_nth(f, 4, 1, ZZ)
    []

    '''
    if n < 0:
        raise IndexError("'n' must be non-negative, got %i" % n)
    if n >= len(f):
        return dmp_zero(u - 1)
    return None[dmp_degree(f, u) - n]


def dmp_ground_nth(f, N, u, K):
    '''
    Return the ground ``n``-th coefficient of ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_ground_nth

    >>> f = ZZ.map([[1], [2, 3]])

    >>> dmp_ground_nth(f, (0, 1), 1, ZZ)
    2

    '''
    v = u
    for n in N:
        if n < 0:
            raise IndexError('`n` must be non-negative, got %i' % n)
        if n >= len(f):
            
            return None, K.zero
        if d == ninf:
            -1 = None(f, v)
        v = v - 1
        f = f[d - n]
        return f


def dmp_zero_p(f, u):
    '''
    Return ``True`` if ``f`` is zero in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_zero_p

    >>> dmp_zero_p([[[[[]]]]], 4)
    True
    >>> dmp_zero_p([[[[[1]]]]], 4)
    False

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_zero(u):
    '''
    Return a multivariate zero.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_zero

    >>> dmp_zero(4)
    [[[[[]]]]]

    '''
    r = []
    for i in range(u):
        r = [
            r]
        return r


def dmp_one_p(f, u, K):
    '''
    Return ``True`` if ``f`` is one in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_one_p

    >>> dmp_one_p([[[ZZ(1)]]], 2, ZZ)
    True

    '''
    return dmp_ground_p(f, K.one, u)


def dmp_one(u, K):
    '''
    Return a multivariate one over ``K``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_one

    >>> dmp_one(2, ZZ)
    [[[1]]]

    '''
    return dmp_ground(K.one, u)


def dmp_ground_p(f, c, u):
    '''
    Return True if ``f`` is constant in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_ground_p

    >>> dmp_ground_p([[[3]]], 3, 2)
    True
    >>> dmp_ground_p([[[4]]], None, 2)
    True

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_ground(c, u):
    '''
    Return a multivariate constant.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_ground

    >>> dmp_ground(3, 5)
    [[[[[[3]]]]]]
    >>> dmp_ground(1, -1)
    1

    '''
    if not c:
        return dmp_zero(u)
    for i in None(u + 1):
        c = [
            c]
        return c


def dmp_zeros(n, u, K):
    '''
    Return a list of multivariate zeros.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_zeros

    >>> dmp_zeros(3, 2, ZZ)
    [[[[]]], [[[]]], [[[]]]]
    >>> dmp_zeros(3, -1, ZZ)
    [0, 0, 0]

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_grounds(c, n, u):
    '''
    Return a list of multivariate constants.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_grounds

    >>> dmp_grounds(ZZ(4), 3, 2)
    [[[[4]]], [[[4]]], [[[4]]]]
    >>> dmp_grounds(ZZ(4), 3, -1)
    [4, 4, 4]

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_negative_p(f, u, K):
    '''
    Return ``True`` if ``LC(f)`` is negative.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_negative_p

    >>> dmp_negative_p([[ZZ(1)], [-ZZ(1)]], 1, ZZ)
    False
    >>> dmp_negative_p([[-ZZ(1)], [ZZ(1)]], 1, ZZ)
    True

    '''
    return K.is_negative(dmp_ground_LC(f, u, K))


def dmp_positive_p(f, u, K):
    '''
    Return ``True`` if ``LC(f)`` is positive.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_positive_p

    >>> dmp_positive_p([[ZZ(1)], [-ZZ(1)]], 1, ZZ)
    True
    >>> dmp_positive_p([[-ZZ(1)], [ZZ(1)]], 1, ZZ)
    False

    '''
    return K.is_positive(dmp_ground_LC(f, u, K))


def dup_from_dict(f, K):
    '''
    Create a ``K[x]`` polynomial from a ``dict``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_from_dict

    >>> dup_from_dict({(0,): ZZ(7), (2,): ZZ(5), (4,): ZZ(1)}, ZZ)
    [1, 0, 5, 0, 7]
    >>> dup_from_dict({}, ZZ)
    []

    '''
    if not f:
        return []
    h = []
    n = None(f.keys())
    if isinstance(n, int):
        for k in range(n, -1, -1):
            h.append(f.get(k, K.zero))
    (n,) = n
    for k in range(n, -1, -1):
        h.append(f.get((k,), K.zero))
        return dup_strip(h)


def dup_from_raw_dict(f, K):
    '''
    Create a ``K[x]`` polynomial from a raw ``dict``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_from_raw_dict

    >>> dup_from_raw_dict({0: ZZ(7), 2: ZZ(5), 4: ZZ(1)}, ZZ)
    [1, 0, 5, 0, 7]

    '''
    if not f:
        return []
    h = []
    n = None(f.keys())
    for k in range(n, -1, -1):
        h.append(f.get(k, K.zero))
        return dup_strip(h)


def dmp_from_dict(f, u, K):
    '''
    Create a ``K[X]`` polynomial from a ``dict``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_from_dict

    >>> dmp_from_dict({(0, 0): ZZ(3), (0, 1): ZZ(2), (2, 1): ZZ(1)}, 1, ZZ)
    [[1, 0], [], [2, 3]]
    >>> dmp_from_dict({}, 0, ZZ)
    []

    '''
    if not u:
        return dup_from_dict(f, K)
    if not None:
        return dmp_zero(u)
    coeffs = None
# WARNING: Decompyle incomplete


def dup_to_dict(f, K, zero = (None, False)):
    '''
    Convert ``K[x]`` polynomial to a ``dict``.

    Examples
    ========

    >>> from sympy.polys.densebasic import dup_to_dict

    >>> dup_to_dict([1, 0, 5, 0, 7])
    {(0,): 7, (2,): 5, (4,): 1}
    >>> dup_to_dict([])
    {}

    '''
    if f and zero:
        return {
            (0,): K.zero }
    result = { }
    n = None(f) - 1
    for k in range(0, n + 1):
        if f[n - k]:
            result[(k,)] = f[n - k]
        return result


def dup_to_raw_dict(f, K, zero = (None, False)):
    '''
    Convert a ``K[x]`` polynomial to a raw ``dict``.

    Examples
    ========

    >>> from sympy.polys.densebasic import dup_to_raw_dict

    >>> dup_to_raw_dict([1, 0, 5, 0, 7])
    {0: 7, 2: 5, 4: 1}

    '''
    if f and zero:
        return {
            0: K.zero }
    result = { }
    n = None(f) - 1
    for k in range(0, n + 1):
        if f[n - k]:
            result[k] = f[n - k]
        return result


def dmp_to_dict(f, u, K, zero = (None, False)):
    '''
    Convert a ``K[X]`` polynomial to a ``dict````.

    Examples
    ========

    >>> from sympy.polys.densebasic import dmp_to_dict

    >>> dmp_to_dict([[1, 0], [], [2, 3]], 1)
    {(0, 0): 3, (0, 1): 2, (2, 1): 1}
    >>> dmp_to_dict([], 0)
    {}

    '''
    if not u:
        return dup_to_dict(f, K, zero = zero)
    if None(f, u) and zero:
        return {
            (0,) * (u + 1): K.zero }
    result = { }
    v = u - 1
    n = None(f, u)
    if n == ninf:
        n = -1
    for k in range(0, n + 1):
        h = dmp_to_dict(f[n - k], v)
        for exp, coeff in h.items():
            result[(k,) + exp] = coeff
            return result


def dmp_swap(f, i, j, u, K):
    '''
    Transform ``K[..x_i..x_j..]`` to ``K[..x_j..x_i..]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_swap

    >>> f = ZZ.map([[[2], [1, 0]], []])

    >>> dmp_swap(f, 0, 1, 2, ZZ)
    [[[2], []], [[1, 0], []]]
    >>> dmp_swap(f, 1, 2, 2, ZZ)
    [[[1], [2, 0]], [[]]]
    >>> dmp_swap(f, 0, 2, 2, ZZ)
    [[[1, 0]], [[2, 0], []]]

    '''
    if i < 0 and j < 0 and i > u or j > u:
        raise IndexError('0 <= i < j <= %s expected' % u)
    if i == j:
        return f
    H = { }
    F = None(f, u)
    for exp, coeff in F.items():
        H[exp[:i] + (exp[j],) + exp[i + 1:j] + (exp[i],) + exp[j + 1:]] = coeff
        return dmp_from_dict(H, u, K)


def dmp_permute(f, P, u, K):
    '''
    Return a polynomial in ``K[x_{P(1)},..,x_{P(n)}]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_permute

    >>> f = ZZ.map([[[2], [1, 0]], []])

    >>> dmp_permute(f, [1, 0, 2], 2, ZZ)
    [[[2], []], [[1, 0], []]]
    >>> dmp_permute(f, [1, 2, 0], 2, ZZ)
    [[[1], []], [[2, 0], []]]

    '''
    H = { }
    F = dmp_to_dict(f, u)
    for exp, coeff in F.items():
        new_exp = [
            0] * len(exp)
        for e, p in zip(exp, P):
            new_exp[p] = e
            H[tuple(new_exp)] = coeff
            return dmp_from_dict(H, u, K)


def dmp_nest(f, l, K):
    '''
    Return a multivariate value nested ``l``-levels.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_nest

    >>> dmp_nest([[ZZ(1)]], 2, ZZ)
    [[[[1]]]]

    '''
    if not isinstance(f, list):
        return dmp_ground(f, l)
    for i in None(l):
        f = [
            f]
        return f


def dmp_raise(f, l, u, K):
    '''
    Return a multivariate polynomial raised ``l``-levels.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_raise

    >>> f = ZZ.map([[], [1, 2]])

    >>> dmp_raise(f, 2, 1, ZZ)
    [[[[]]], [[[1]], [[2]]]]

    '''
    pass
# WARNING: Decompyle incomplete


def dup_deflate(f, K):
    '''
    Map ``x**m`` to ``y`` in a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_deflate

    >>> f = ZZ.map([1, 0, 0, 1, 0, 0, 1])

    >>> dup_deflate(f, ZZ)
    (3, [1, 1, 1])

    '''
    if dup_degree(f) <= 0:
        return (1, f)
    g = None
    for i in range(len(f)):
        if not f[-i - 1]:
            continue
        g = igcd(g, i)
        if g == 1:
            
            return None, (1, f)
        return (g, f[::g])


def dmp_deflate(f, u, K):
    '''
    Map ``x_i**m_i`` to ``y_i`` in a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_deflate

    >>> f = ZZ.map([[1, 0, 0, 2], [], [3, 0, 0, 4]])

    >>> dmp_deflate(f, 1, ZZ)
    ((2, 3), [[1, 2], [3, 4]])

    '''
    if dmp_zero_p(f, u):
        return ((1,) * (u + 1), f)
    F = None(f, u)
    B = [
        0] * (u + 1)
    for M in F.keys():
        for i, m in enumerate(M):
            B[i] = igcd(B[i], m)
            for i, b in enumerate(B):
                if not b:
                    B[i] = 1
                B = tuple(B)
                if (lambda .0: pass# WARNING: Decompyle incomplete
)(B()):
                    return (B, f)
                H = all
                for A, coeff in F.items():
                    N = zip(A, B)()
                    H[tuple(N)] = coeff
                    return (B, dmp_from_dict(H, u, K))


def dup_multi_deflate(polys, K):
    '''
    Map ``x**m`` to ``y`` in a set of polynomials in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_multi_deflate

    >>> f = ZZ.map([1, 0, 2, 0, 3])
    >>> g = ZZ.map([4, 0, 0])

    >>> dup_multi_deflate((f, g), ZZ)
    (2, ([1, 2, 3], [4, 0]))

    '''
    pass
# WARNING: Decompyle incomplete


def dmp_multi_deflate(polys, u, K):
    '''
    Map ``x_i**m_i`` to ``y_i`` in a set of polynomials in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_multi_deflate

    >>> f = ZZ.map([[1, 0, 0, 2], [], [3, 0, 0, 4]])
    >>> g = ZZ.map([[1, 0, 2], [], [3, 0, 4]])

    >>> dmp_multi_deflate((f, g), 1, ZZ)
    ((2, 1), ([[1, 0, 0, 2], [3, 0, 0, 4]], [[1, 0, 2], [3, 0, 4]]))

    '''
    if not u:
        (M, H) = dup_multi_deflate(polys, K)
        return ((M,), H)
    B = [
        0] * (u + 1)
    F = None
    for p in polys:
        f = dmp_to_dict(p, u)
        if not dmp_zero_p(p, u):
            for M in f.keys():
                for i, m in enumerate(M):
                    B[i] = igcd(B[i], m)
                    F.append(f)
                    for i, b in enumerate(B):
                        if not b:
                            B[i] = 1
                        B = tuple(B)
                        if (lambda .0: pass# WARNING: Decompyle incomplete
)(B()):
                            return (B, polys)
                        H = all
                        for f in F:
                            h = { }
                            for A, coeff in f.items():
                                N = zip(A, B)()
                                h[tuple(N)] = coeff
                                H.append(dmp_from_dict(h, u, K))
                                return (B, tuple(H))


def dup_inflate(f, m, K):
    '''
    Map ``y`` to ``x**m`` in a polynomial in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_inflate

    >>> f = ZZ.map([1, 1, 1])

    >>> dup_inflate(f, 3, ZZ)
    [1, 0, 0, 1, 0, 0, 1]

    '''
    if m <= 0:
        raise IndexError("'m' must be positive, got %s" % m)
    if not m == 1 or f:
        return f
    result = [
        None[0]]
    for coeff in f[1:]:
        result.extend([
            K.zero] * (m - 1))
        result.append(coeff)
        return result


def _rec_inflate(g, M, v, i, K):
    '''Recursive helper for :func:`dmp_inflate`.'''
    pass
# WARNING: Decompyle incomplete


def dmp_inflate(f, M, u, K):
    '''
    Map ``y_i`` to ``x_i**k_i`` in a polynomial in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_inflate

    >>> f = ZZ.map([[1, 2], [3, 4]])

    >>> dmp_inflate(f, (2, 3), 1, ZZ)
    [[1, 0, 0, 2], [], [3, 0, 0, 4]]

    '''
    if not u:
        return dup_inflate(f, M[0], K)
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(M()):
        return f
    return None(f, M, u, 0, K)


def dmp_exclude(f, u, K):
    '''
    Exclude useless levels from ``f``.

    Return the levels excluded, the new excluded ``f``, and the new ``u``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_exclude

    >>> f = ZZ.map([[[1]], [[1], [2]]])

    >>> dmp_exclude(f, 2, ZZ)
    ([2], [[1], [1, 2]], 1)

    '''
    if u or dmp_ground_p(f, None, u):
        return ([], f, u)
    F = dmp_to_dict(f, u)
    J = None
    for j in range(0, u + 1):
        for monom in F.keys():
            if monom[j]:
                pass
            
            J.append(j)
            if not J:
                return ([], f, u)
            f = None
            for monom, coeff in F.items():
                monom = list(monom)
                for j in reversed(J):
                    del monom[j]
                    f[tuple(monom)] = coeff
                    u -= len(J)
                    return (J, dmp_from_dict(f, u, K), u)


def dmp_include(f, J, u, K):
    '''
    Include useless levels in ``f``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_include

    >>> f = ZZ.map([[1], [1, 2]])

    >>> dmp_include(f, [2], 1, ZZ)
    [[[1]], [[1], [2]]]

    '''
    if not J:
        return f
    f = { }
    F = None(f, u)
    for monom, coeff in F.items():
        monom = list(monom)
        for j in J:
            monom.insert(j, 0)
            f[tuple(monom)] = coeff
            u += len(J)
            return dmp_from_dict(f, u, K)


def dmp_inject(f, u, K, front = (False,)):
    '''
    Convert ``f`` from ``K[X][Y]`` to ``K[X,Y]``.

    Examples
    ========

    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_inject

    >>> R, x,y = ring("x,y", ZZ)

    >>> dmp_inject([R(1), x + 2], 0, R.to_domain())
    ([[[1]], [[1], [2]]], 2)
    >>> dmp_inject([R(1), x + 2], 0, R.to_domain(), front=True)
    ([[[1]], [[1, 2]]], 2)

    '''
    h = { }
    f = dmp_to_dict(f, u)
    v = K.ngens - 1
    for f_monom, g in f.items():
        g = g.to_dict()
        for g_monom, c in g.items():
            if front:
                h[g_monom + f_monom] = c
                continue
            h[f_monom + g_monom] = c
            w = u + v + 1
            return (dmp_from_dict(h, w, K.dom), w)


def dmp_eject(f, u, K, front = (False,)):
    """
    Convert ``f`` from ``K[X,Y]`` to ``K[X][Y]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_eject

    >>> dmp_eject([[[1]], [[1], [2]]], 2, ZZ['x', 'y'])
    [1, x + 2]

    """
    h = { }
    f = dmp_to_dict(f, u)
    n = K.ngens
    v = (u - K.ngens) + 1
    for monom, c in f.items():
        if front:
            f_monom = monom[n:]
            g_monom = monom[:n]
        else:
            f_monom = monom[:-n]
            g_monom = monom[-n:]
        if f_monom in h:
            h[f_monom][g_monom] = c
            continue
        h[f_monom] = {
            g_monom: c }
        for monom, c in h.items():
            h[monom] = K(c)
            return dmp_from_dict(h, v - 1, K)


def dup_terms_gcd(f, K):
    '''
    Remove GCD of terms from ``f`` in ``K[x]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_terms_gcd

    >>> f = ZZ.map([1, 0, 1, 0, 0])

    >>> dup_terms_gcd(f, ZZ)
    (2, [1, 0, 1])

    '''
    if not dup_TC(f, K) or f:
        return (0, f)
    i = None
    for c in reversed(f):
        if not c:
            i += 1
            continue
        return (i, f[:-i])


def dmp_terms_gcd(f, u, K):
    '''
    Remove GCD of terms from ``f`` in ``K[X]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_terms_gcd

    >>> f = ZZ.map([[1, 0], [1, 0, 0], [], []])

    >>> dmp_terms_gcd(f, 1, ZZ)
    ((2, 1), [[1], [1, 0]])

    '''
    if dmp_ground_TC(f, u, K) or dmp_zero_p(f, u):
        return ((0,) * (u + 1), f)
    F = None(f, u)
# WARNING: Decompyle incomplete


def _rec_list_terms(g, v, monom):
    '''Recursive helper for :func:`dmp_list_terms`.'''
    terms = []
    d = dmp_degree(g, v)
    if not v:
        for i, c in enumerate(g):
            if not c:
                continue
            terms.append((monom + (d - i,), c))
    w = v - 1
    for i, c in enumerate(g):
        terms.extend(_rec_list_terms(c, w, monom + (d - i,)))
        return terms


def dmp_list_terms(f, u, K, order = (None,)):
    """
    List all non-zero terms from ``f`` in the given order ``order``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_list_terms

    >>> f = ZZ.map([[1, 1], [2, 3]])

    >>> dmp_list_terms(f, 1, ZZ)
    [((1, 1), 1), ((1, 0), 1), ((0, 1), 2), ((0, 0), 3)]
    >>> dmp_list_terms(f, 1, ZZ, order='grevlex')
    [((1, 1), 1), ((1, 0), 1), ((0, 1), 2), ((0, 0), 3)]

    """
    
    def sort(terms, O):
        pass
    # WARNING: Decompyle incomplete

    terms = _rec_list_terms(f, u, ())
    if not terms:
        return [
            ((0,) * (u + 1), K.zero)]
# WARNING: Decompyle incomplete


def dup_apply_pairs(f, g, h, args, K):
    '''
    Apply ``h`` to pairs of coefficients of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_apply_pairs

    >>> h = lambda x, y, z: 2*x + y - z

    >>> dup_apply_pairs([1, 2, 3], [3, 2, 1], h, (1,), ZZ)
    [4, 5, 6]

    '''
    m = len(g)
    n = len(f)
    if n != m:
        if n > m:
            g = [
                K.zero] * (n - m) + g
        else:
            f = [
                K.zero] * (m - n) + f
    result = []
# WARNING: Decompyle incomplete


def dmp_apply_pairs(f, g, h, args, u, K):
    '''
    Apply ``h`` to pairs of coefficients of ``f`` and ``g``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dmp_apply_pairs

    >>> h = lambda x, y, z: 2*x + y - z

    >>> dmp_apply_pairs([[1], [2, 3]], [[3], [2, 1]], h, (1,), 1, ZZ)
    [[4], [5, 6]]

    '''
    if not u:
        return dup_apply_pairs(f, g, h, args, K)
    v = u - 1
    m = len(g)
    n = None(f)
    if n != m:
        if n > m:
            g = dmp_zeros(n - m, v, K) + g
        else:
            f = dmp_zeros(m - n, v, K) + f
    result = []
    for a, b in zip(f, g):
        result.append(dmp_apply_pairs(a, b, h, args, v, K))
        return dmp_strip(result, u)


def dup_slice(f, m, n, K):
    '''Take a continuous subsequence of terms of ``f`` in ``K[x]``. '''
    k = len(f)
    if k >= m:
        M = k - m
    else:
        M = 0
    if k >= n:
        N = k - n
    else:
        N = 0
    f = f[N:M]
# WARNING: Decompyle incomplete


def dmp_slice(f, m, n, u, K):
    '''Take a continuous subsequence of terms of ``f`` in ``K[X]``. '''
    return dmp_slice_in(f, m, n, 0, u, K)


def dmp_slice_in(f, m, n, j, u, K):
    '''Take a continuous subsequence of terms of ``f`` in ``x_j`` in ``K[X]``. '''
    if j < 0 or j > u:
        raise IndexError(f'''-{u!s} <= j < {u!s} expected, got {j!s}''')
    if not u:
        return dup_slice(f, m, n, K)
    g = { }
    f = None(f, u)
    for monom, coeff in f.items():
        k = monom[j]
        if k < m or k >= n:
            monom = monom[:j] + (0,) + monom[j + 1:]
        if monom in g:
            continue
        coeff = None
        return dmp_from_dict(g, u, K)


def dup_random(n, a, b, K):
    '''
    Return a polynomial of degree ``n`` with coefficients in ``[a, b]``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.densebasic import dup_random

    >>> dup_random(3, -10, 10, ZZ) #doctest: +SKIP
    [-2, -8, 9, -4]

    '''
    pass
# WARNING: Decompyle incomplete
