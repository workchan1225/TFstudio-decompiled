# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rootisolation.pyc (Python 3.11)

__doc__ = 'Real and complex root isolation and refinement algorithms. '
from sympy.polys.densearith import dup_neg, dup_rshift, dup_rem, dup_l2_norm_squared
from sympy.polys.densebasic import dup_LC, dup_TC, dup_degree, dup_strip, dup_reverse, dup_convert, dup_terms_gcd
from sympy.polys.densetools import dup_clear_denoms, dup_mirror, dup_scale, dup_shift, dup_transform, dup_diff, dup_eval, dmp_eval_in, dup_sign_variations, dup_real_imag
from sympy.polys.euclidtools import dup_discriminant
from sympy.polys.factortools import dup_factor_list
from sympy.polys.polyerrors import RefinementFailed, DomainError, PolynomialError
from sympy.polys.sqfreetools import dup_sqf_part, dup_sqf_list

def dup_sturm(f, K):
    '''
    Computes the Sturm sequence of ``f`` in ``F[x]``.

    Given a univariate, square-free polynomial ``f(x)`` returns the
    associated Sturm sequence ``f_0(x), ..., f_n(x)`` defined by::

       f_0(x), f_1(x) = f(x), f\'(x)
       f_n = -rem(f_{n-2}(x), f_{n-1}(x))

    Examples
    ========

    >>> from sympy.polys import ring, QQ
    >>> R, x = ring("x", QQ)

    >>> R.dup_sturm(x**3 - 2*x**2 + x - 3)
    [x**3 - 2*x**2 + x - 3, 3*x**2 - 4*x + 1, 2/9*x + 25/9, -2079/4]

    References
    ==========

    .. [1] [Davenport88]_

    '''
    if not K.is_Field:
        raise DomainError('Cannot compute Sturm sequence over %s' % K)
    f = dup_sqf_part(f, K)
    sturm = [
        f,
        dup_diff(f, 1, K)]
# WARNING: Decompyle incomplete


def dup_root_upper_bound(f, K):
    '''Compute the LMQ upper bound for the positive roots of `f`;
       LMQ (Local Max Quadratic) was developed by Akritas-Strzebonski-Vigklas.

    References
    ==========
    .. [1] Alkiviadis G. Akritas: "Linear and Quadratic Complexity Bounds on the
        Values of the Positive Roots of Polynomials"
        Journal of Universal Computer Science, Vol. 15, No. 3, 523-537, 2009.
    '''
    P = []
    n = len(f)
    t = n * [
        K.one]
    if dup_LC(f, K) < 0:
        f = dup_neg(f, K)
    f = list(reversed(f))
    for i in range(0, n):
        if f[i] >= 0:
            continue
        QL = []
        a = K.log(-f[i], 2)
        for j in range(i + 1, n):
            if f[j] <= 0:
                continue
            q = t[j] + a - K.log(f[j], 2)
            QL.append([
                q // (j - i),
                j])
            if not QL:
                continue
        q = min(QL)
        t[q[1]] = t[q[1]] + 1
        P.append(q[0])
        if not P:
            return None
        return K.get_field()(2) ** (max(P) + 1)


def dup_root_lower_bound(f, K):
    '''Compute the LMQ lower bound for the positive roots of `f`;
       LMQ (Local Max Quadratic) was developed by Akritas-Strzebonski-Vigklas.

       References
       ==========
       .. [1] Alkiviadis G. Akritas: "Linear and Quadratic Complexity Bounds on the
              Values of the Positive Roots of Polynomials"
              Journal of Universal Computer Science, Vol. 15, No. 3, 523-537, 2009.
    '''
    bound = dup_root_upper_bound(dup_reverse(f), K)
# WARNING: Decompyle incomplete


def dup_cauchy_upper_bound(f, K):
    """
    Compute the Cauchy upper bound on the absolute value of all roots of f,
    real or complex.

    References
    ==========
    .. [1] https://en.wikipedia.org/wiki/Geometrical_properties_of_polynomial_roots#Lagrange's_and_Cauchy's_bounds
    """
    pass
# WARNING: Decompyle incomplete


def dup_cauchy_lower_bound(f, K):
    '''Compute the Cauchy lower bound on the absolute value of all non-zero
       roots of f, real or complex.'''
    g = dup_reverse(f)
    if len(g) < 2:
        raise PolynomialError('Polynomial has no non-zero roots.')
    if K.is_ZZ:
        K = K.get_field()
    b = dup_cauchy_upper_bound(g, K)
    return K.one / b


def dup_mignotte_sep_bound_squared(f, K):
    '''
    Return the square of the Mignotte lower bound on separation between
    distinct roots of f. The square is returned so that the bound lies in
    K or its quotient field.

    References
    ==========

    .. [1] Mignotte, Maurice. "Some useful bounds." Computer algebra.
        Springer, Vienna, 1982. 259-263.
        https://people.dm.unipi.it/gianni/AC-EAG/Mignotte.pdf
    '''
    n = dup_degree(f)
    if n < 2:
        raise PolynomialError('Polynomials of degree < 2 have no distinct roots.')
    if K.is_ZZ:
        L = K.get_field()
        K = L
        f = dup_convert(f, K, L)
    elif K.is_QQ and K.is_RR or K.is_CC:
        raise DomainError('Mignotte bound not supported over %s' % K)
    D = dup_discriminant(f, K)
    l2sq = dup_l2_norm_squared(f, K)
    return K(3) * K.abs(D) / (K(n) ** (n + 1) * l2sq ** (n - 1))


def _mobius_from_interval(I, field):
    '''Convert an open interval to a Mobius transform. '''
    (s, t) = I
    c = field.denom(s)
    a = field.numer(s)
    d = field.denom(t)
    b = field.numer(t)
    return (a, b, c, d)


def _mobius_to_interval(M, field):
    '''Convert a Mobius transform to an open interval. '''
    (a, b, c, d) = M
    t = field(b, d)
    s = field(a, c)
    if s <= t:
        return (s, t)
    return (None, s)


def dup_step_refine_real_root(f, M, K, fast = (False,)):
    '''One step of positive real root refinement algorithm. '''
    (a, b, c, d) = M
    if a == b and c == d:
        return (f, (a, b, c, d))
    A = None(f, K)
# WARNING: Decompyle incomplete


def dup_inner_refine_real_root(f, M, K, eps, steps, disjoint, fast, mobius = (None, None, None, False, False)):
    '''Refine a positive root of `f` given a Mobius transform or an interval. '''
    F = K.get_field()
    if len(M) == 2:
        (a, b, c, d) = _mobius_from_interval(M, F)
    else:
        (a, b, c, d) = M
# WARNING: Decompyle incomplete


def dup_outer_refine_real_root(f, s, t, K, eps, steps, disjoint, fast = (None, None, None, False)):
    '''Refine a positive root of `f` given an interval `(s, t)`. '''
    (a, b, c, d) = _mobius_from_interval((s, t), K.get_field())
    f = dup_transform(f, dup_strip([
        a,
        b]), dup_strip([
        c,
        d]), K)
    if dup_sign_variations(f, K) != 1:
        raise RefinementFailed(f'''there should be exactly one root in ({s!s}, {t!s}) interval''')
    return dup_inner_refine_real_root(f, (a, b, c, d), K, eps = eps, steps = steps, disjoint = disjoint, fast = fast)


def dup_refine_real_root(f, s, t, K, eps, steps, disjoint, fast = (None, None, None, False)):
    """Refine real root's approximating interval to the given precision. """
    if K.is_QQ:
        (_, f) = 
        K = dup_clear_denoms(f, K, convert = True), K.get_ring()
    elif not K.is_ZZ:
        raise DomainError('real root refinement not supported over %s' % K)
    if s == t:
        return (s, t)
    if None > t:
        t = s
        s = t
    negative = False
    if s < 0:
        if t <= 0:
            (f, s, t, negative) = (dup_mirror(f, K), -t, -s, True)
        else:
            raise ValueError(f'''Cannot refine a real root in ({s!s}, {t!s})''')
# WARNING: Decompyle incomplete


def dup_inner_isolate_real_roots(f, K, eps, fast = (None, False)):
    '''Internal function for isolation positive roots up to given precision.

       References
       ==========
           1. Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative Study of Two Real Root
           Isolation Methods . Nonlinear Analysis: Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
           2. Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S. Vigklas: Improving the
           Performance of the Continued Fractions Method Using new Bounds of Positive Roots. Nonlinear
           Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.
    '''
    (a, b, c, d) = (K.one, K.zero, K.zero, K.one)
    k = dup_sign_variations(f, K)
    if k == 0:
        return []
    if None == 1:
        roots = [
            dup_inner_refine_real_root(f, (a, b, c, d), K, eps = eps, fast = fast, mobius = True)]
# WARNING: Decompyle incomplete


def _discard_if_outside_interval(f, M, inf, sup, K, negative, fast, mobius):
    '''Discard an isolating interval if outside ``(inf, sup)``. '''
    F = K.get_field()
    (u, v) = _mobius_to_interval(M, F)
    if negative:
        v = -u
        u = -v
# WARNING: Decompyle incomplete


def dup_inner_isolate_positive_roots(f, K, eps, inf, sup, fast, mobius = (None, None, None, False, False)):
    '''Iteratively compute disjoint positive root isolation intervals. '''
    pass
# WARNING: Decompyle incomplete


def dup_inner_isolate_negative_roots(f, K, inf, sup, eps, fast, mobius = (None, None, None, False, False)):
    '''Iteratively compute disjoint negative root isolation intervals. '''
    pass
# WARNING: Decompyle incomplete


def _isolate_zero(f, K, inf, sup, basis, sqf = (False, False)):
    '''Handle special case of CF algorithm when ``f`` is homogeneous. '''
    (j, f) = dup_terms_gcd(f, K)
# WARNING: Decompyle incomplete


def dup_isolate_real_roots_sqf(f, K, eps, inf, sup, fast, blackbox = (None, None, None, False, False)):
    '''Isolate real roots of a square-free polynomial using the Vincent-Akritas-Strzebonski (VAS) CF approach.

       References
       ==========
       .. [1] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative
              Study of Two Real Root Isolation Methods. Nonlinear Analysis:
              Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
       .. [2] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S.
              Vigklas: Improving the Performance of the Continued Fractions
              Method Using New Bounds of Positive Roots. Nonlinear Analysis:
              Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

    '''
    pass
# WARNING: Decompyle incomplete


def dup_isolate_real_roots(f, K, eps, inf, sup, basis, fast = (None, None, None, False, False)):
    '''Isolate real roots using Vincent-Akritas-Strzebonski (VAS) continued fractions approach.

       References
       ==========

       .. [1] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative
              Study of Two Real Root Isolation Methods. Nonlinear Analysis:
              Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
       .. [2] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S.
              Vigklas: Improving the Performance of the Continued Fractions
              Method Using New Bounds of Positive Roots.
              Nonlinear Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

    '''
    pass
# WARNING: Decompyle incomplete


def dup_isolate_real_roots_list(polys, K, eps, inf, sup, strict, basis, fast = (None, None, None, False, False, False)):
    '''Isolate real roots of a list of square-free polynomial using Vincent-Akritas-Strzebonski (VAS) CF approach.

       References
       ==========

       .. [1] Alkiviadis G. Akritas and Adam W. Strzebonski: A Comparative
              Study of Two Real Root Isolation Methods. Nonlinear Analysis:
              Modelling and Control, Vol. 10, No. 4, 297-304, 2005.
       .. [2] Alkiviadis G. Akritas, Adam W. Strzebonski and Panagiotis S.
              Vigklas: Improving the Performance of the Continued Fractions
              Method Using New Bounds of Positive Roots.
              Nonlinear Analysis: Modelling and Control, Vol. 13, No. 3, 265-279, 2008.

    '''
    if K.is_QQ:
        polys = polys[:]
        F = K
        K = K.get_ring()
        for i, p in enumerate(polys):
            polys[i] = dup_clear_denoms(p, F, K, convert = True)[1]
    if not K.is_ZZ:
        raise DomainError('isolation of real roots not supported over %s' % K)
    factors_dict = { }
    zeros = False
# WARNING: Decompyle incomplete


def _disjoint_p(M, N, strict = (False,)):
