# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rde.pyc (Python 3.11)

'''
Algorithms for solving the Risch differential equation.

Given a differential field K of characteristic 0 that is a simple
monomial extension of a base field k and f, g in K, the Risch
Differential Equation problem is to decide if there exist y in K such
that Dy + f*y == g and to find one if there are some.  If t is a
monomial over k and the coefficients of f and g are in k(t), then y is
in k(t), and the outline of the algorithm here is given as:

1. Compute the normal part n of the denominator of y.  The problem is
then reduced to finding y\' in k<t>, where y == y\'/n.
2. Compute the special part s of the denominator of y.   The problem is
then reduced to finding y\'\' in k[t], where y == y\'\'/(n*s)
3. Bound the degree of y\'\'.
4. Reduce the equation Dy + f*y == g to a similar equation with f, g in
k[t].
5. Find the solutions in k[t] of bounded degree of the reduced equation.

See Chapter 6 of "Symbolic Integration I: Transcendental Functions" by
Manuel Bronstein.  See also the docstring of risch.py.
'''
from operator import mul
from functools import reduce
from sympy.core import oo
from sympy.core.symbol import Dummy
from sympy.polys import Poly, gcd, ZZ, cancel
from sympy.functions.elementary.complexes import im, re
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.integrals.risch import gcdex_diophantine, frac_in, derivation, splitfactor, NonElementaryIntegralException, DecrementLevel, recognize_log_derivative

def order_at(a, p, t):
    '''
    Computes the order of a at p, with respect to t.

    Explanation
    ===========

    For a, p in k[t], the order of a at p is defined as nu_p(a) = max({n
    in Z+ such that p**n|a}), where a != 0.  If a == 0, nu_p(a) = +oo.

    To compute the order at a rational function, a/b, use the fact that
    nu_p(a/b) == nu_p(a) - nu_p(b).
    '''
    if a.is_zero:
        return oo
    if None == Poly(t, t):
        return a.as_poly(t).ET()[0][0]
    power_list = None
    p1 = p
    r = a.rem(p1)
    tracks_power = 1
# WARNING: Decompyle incomplete


def order_at_oo(a, d, t):
    '''
    Computes the order of a/d at oo (infinity), with respect to t.

    For f in k(t), the order or f at oo is defined as deg(d) - deg(a), where
    f == a/d.
    '''
    if a.is_zero:
        return oo
    return None.degree(t) - a.degree(t)


def weak_normalizer(a, d, DE, z = (None,)):
    '''
    Weak normalization.

    Explanation
    ===========

    Given a derivation D on k[t] and f == a/d in k(t), return q in k[t]
    such that f - Dq/q is weakly normalized with respect to t.

    f in k(t) is said to be "weakly normalized" with respect to t if
    residue_p(f) is not a positive integer for any normal irreducible p
    in k[t] such that f is in R_p (Definition 6.1.1).  If f has an
    elementary integral, this is equivalent to no logarithm of
    integral(f) whose argument depends on t has a positive integer
    coefficient, where the arguments of the logarithms not in k(t) are
    in k[t].

    Returns (q, f - Dq/q)
    '''
    pass
# WARNING: Decompyle incomplete


def normal_denom(fa, fd, ga, gd, DE):
    '''
    Normal part of the denominator.

    Explanation
    ===========

    Given a derivation D on k[t] and f, g in k(t) with f weakly
    normalized with respect to t, either raise NonElementaryIntegralException,
    in which case the equation Dy + f*y == g has no solution in k(t), or the
    quadruplet (a, b, c, h) such that a, h in k[t], b, c in k<t>, and for any
    solution y in k(t) of Dy + f*y == g, q = y*h in k<t> satisfies
    a*Dq + b*q == c.

    This constitutes step 1 in the outline given in the rde.py docstring.
    '''
    (dn, ds) = splitfactor(fd, DE)
    (en, es) = splitfactor(gd, DE)
    p = dn.gcd(en)
    h = en.gcd(en.diff(DE.t)).quo(p.gcd(p.diff(DE.t)))
    a = dn * h
    c = a * h
    if c.div(en)[1]:
        raise NonElementaryIntegralException
    ca = c * ga
    (ca, cd) = ca.cancel(gd, include = True)
    ba = a * fa - dn * derivation(h, DE) * fd
    (ba, bd) = ba.cancel(fd, include = True)
    return (a, (ba, bd), (ca, cd), h)


def special_denom(a, ba, bd, ca, cd, DE, case = ('auto',)):
    """
    Special part of the denominator.

    Explanation
    ===========

    case is one of {'exp', 'tan', 'primitive'} for the hyperexponential,
    hypertangent, and primitive cases, respectively.  For the
    hyperexponential (resp. hypertangent) case, given a derivation D on
    k[t] and a in k[t], b, c, in k<t> with Dt/t in k (resp. Dt/(t**2 + 1) in
    k, sqrt(-1) not in k), a != 0, and gcd(a, t) == 1 (resp.
    gcd(a, t**2 + 1) == 1), return the quadruplet (A, B, C, 1/h) such that
    A, B, C, h in k[t] and for any solution q in k<t> of a*Dq + b*q == c,
    r = qh in k[t] satisfies A*Dr + B*r == C.

    For ``case == 'primitive'``, k<t> == k[t], so it returns (a, b, c, 1) in
    this case.

    This constitutes step 2 of the outline given in the rde.py docstring.
    """
    if case == 'auto':
        case = DE.case
    if case == 'exp':
        p = Poly(DE.t, DE.t)
    elif case == 'tan':
        p = Poly(DE.t ** 2 + 1, DE.t)
    elif case in ('primitive', 'base'):
        B = ba.to_field().quo(bd)
        C = ca.to_field().quo(cd)
        return (a, B, C, Poly(1, DE.t))
    raise ValueError("case must be one of {'exp', 'tan', 'primitive', 'base'}, not %s." % case)
    nb = order_at(ba, p, DE.t) - order_at(bd, p, DE.t)
    nc = order_at(ca, p, DE.t) - order_at(cd, p, DE.t)
    n = min(0, nc - min(0, nb))
# WARNING: Decompyle incomplete


def bound_degree(a, b, cQ, DE, case, parametric = ('auto', False)):
    '''
    Bound on polynomial solutions.

    Explanation
    ===========

    Given a derivation D on k[t] and ``a``, ``b``, ``c`` in k[t] with ``a != 0``, return
    n in ZZ such that deg(q) <= n for any solution q in k[t] of
    a*Dq + b*q == c, when parametric=False, or deg(q) <= n for any solution
    c1, ..., cm in Const(k) and q in k[t] of a*Dq + b*q == Sum(ci*gi, (i, 1, m))
    when parametric=True.

    For ``parametric=False``, ``cQ`` is ``c``, a ``Poly``; for ``parametric=True``, ``cQ`` is Q ==
    [q1, ..., qm], a list of Polys.

    This constitutes step 3 of the outline given in the rde.py docstring.
    '''
    pass
# WARNING: Decompyle incomplete


def spde(a, b, c, n, DE):
    """
    Rothstein's Special Polynomial Differential Equation algorithm.

    Explanation
    ===========

    Given a derivation D on k[t], an integer n and ``a``,``b``,``c`` in k[t] with
    ``a != 0``, either raise NonElementaryIntegralException, in which case the
    equation a*Dq + b*q == c has no solution of degree at most ``n`` in
    k[t], or return the tuple (B, C, m, alpha, beta) such that B, C,
    alpha, beta in k[t], m in ZZ, and any solution q in k[t] of degree
    at most n of a*Dq + b*q == c must be of the form
    q == alpha*h + beta, where h in k[t], deg(h) <= m, and Dh + B*h == C.

    This constitutes step 4 of the outline given in the rde.py docstring.
    """
    zero = Poly(0, DE.t)
    alpha = Poly(1, DE.t)
    beta = Poly(0, DE.t)
    if c.is_zero:
        return (zero, zero, 0, zero, beta)
    if None < 0 is True:
        raise NonElementaryIntegralException
    g = a.gcd(b)
    if not c.rem(g).is_zero:
        raise NonElementaryIntegralException
    c = c.quo(g)
    b = b.quo(g)
    a = a.quo(g)
    if a.degree(DE.t) == 0:
        b = b.to_field().quo(a)
        c = c.to_field().quo(a)
        return (b, c, n, alpha, beta)
    (r, z) = None(b, a, c)
    b += derivation(a, DE)
    c = z - derivation(r, DE)
    n -= a.degree(DE.t)
    beta += alpha * r
    alpha *= a
    continue


def no_cancel_b_large(b, c, n, DE):
    '''
    Poly Risch Differential Equation - No cancellation: deg(b) large enough.

    Explanation
    ===========

    Given a derivation D on k[t], ``n`` either an integer or +oo, and ``b``,``c``
    in k[t] with ``b != 0`` and either D == d/dt or
    deg(b) > max(0, deg(D) - 1), either raise NonElementaryIntegralException, in
    which case the equation ``Dq + b*q == c`` has no solution of degree at
    most n in k[t], or a solution q in k[t] of this equation with
    ``deg(q) < n``.
    '''
    q = Poly(0, DE.t)
    if not c.is_zero:
        m = c.degree(DE.t) - b.degree(DE.t)
        if not  <= 0, m or 0, m <= n:
            pass
        
        raise NonElementaryIntegralException
    q + p = Poly((c.as_poly(DE.t).LC() / b.as_poly(DE.t).LC()) * DE.t ** m, DE.t, expand = False)
    n = m - 1
    c = c - derivation(p, DE) - b * p
# WARNING: Decompyle incomplete


def no_cancel_b_small(b, c, n, DE):
    '''
    Poly Risch Differential Equation - No cancellation: deg(b) small enough.

    Explanation
    ===========

    Given a derivation D on k[t], ``n`` either an integer or +oo, and ``b``,``c``
    in k[t] with deg(b) < deg(D) - 1 and either D == d/dt or
    deg(D) >= 2, either raise NonElementaryIntegralException, in which case the
    equation Dq + b*q == c has no solution of degree at most n in k[t],
    or a solution q in k[t] of this equation with deg(q) <= n, or the
    tuple (h, b0, c0) such that h in k[t], b0, c0, in k, and for any
    solution q in k[t] of degree at most n of Dq + bq == c, y == q - h
    is a solution in k of Dy + b0*y == c0.
    '''
    q = Poly(0, DE.t)
    if not c.is_zero:
        if n == 0:
            m = 0
        else:
            m = (c.degree(DE.t) - DE.d.degree(DE.t)) + 1
        if not  <= 0, m or 0, m <= n:
            pass
        
        raise NonElementaryIntegralException
    if m > 0:
        pass
    elif b.degree(DE.t) != c.degree(DE.t):
        raise NonElementaryIntegralException
    if b.degree(DE.t) == 0:
        return (q, b.as_poly(DE.T[DE.level - 1]), c.as_poly(DE.T[DE.level - 1]))
    Poly((c.as_poly(DE.t).LC() / (m * DE.d.as_poly(DE.t).LC())) * DE.t ** m, DE.t, expand = False)(c.as_poly(DE.t).LC() / b.as_poly(DE.t).LC(), DE.t, expand = False) = None
    q = q + p
    n = m - 1
    c = c - derivation(p, DE) - b * p
# WARNING: Decompyle incomplete


def no_cancel_equal(b, c, n, DE):
    '''
    Poly Risch Differential Equation - No cancellation: deg(b) == deg(D) - 1

    Explanation
    ===========

    Given a derivation D on k[t] with deg(D) >= 2, n either an integer
    or +oo, and b, c in k[t] with deg(b) == deg(D) - 1, either raise
    NonElementaryIntegralException, in which case the equation Dq + b*q == c has
    no solution of degree at most n in k[t], or a solution q in k[t] of
    this equation with deg(q) <= n, or the tuple (h, m, C) such that h
    in k[t], m in ZZ, and C in k[t], and for any solution q in k[t] of
    degree at most n of Dq + b*q == c, y == q - h is a solution in k[t]
    of degree at most m of Dy + b*y == C.
    '''
    q = Poly(0, DE.t)
    lc = cancel(-b.as_poly(DE.t).LC() / DE.d.as_poly(DE.t).LC())
    if lc.is_Integer and lc.is_positive:
        M = lc
    else:
        M = -1
    if not c.is_zero:
        m = max(M, (c.degree(DE.t) - DE.d.degree(DE.t)) + 1)
        if not  <= 0, m or 0, m <= n:
            pass
        
        raise NonElementaryIntegralException
    if u.is_zero:
        return (q, m, c)
    if cancel(m * DE.d.as_poly(DE.t).LC() + b.as_poly(DE.t).LC()) > 0:
        Poly((c.as_poly(DE.t).LC() / u) * DE.t ** m, DE.t, expand = False) = None
    elif c.degree(DE.t) != DE.d.degree(DE.t) - 1:
        raise NonElementaryIntegralException
    p = c.as_poly(DE.t).LC() / b.as_poly(DE.t).LC()
    q = q + p
    n = m - 1
    c = c - derivation(p, DE) - b * p
# WARNING: Decompyle incomplete


def cancel_primitive(b, c, n, DE):
    '''
    Poly Risch Differential Equation - Cancellation: Primitive case.

    Explanation
    ===========

    Given a derivation D on k[t], n either an integer or +oo, ``b`` in k, and
    ``c`` in k[t] with Dt in k and ``b != 0``, either raise
    NonElementaryIntegralException, in which case the equation Dq + b*q == c
    has no solution of degree at most n in k[t], or a solution q in k[t] of
    this equation with deg(q) <= n.
    '''
    is_log_deriv_k_t_radical_in_field = is_log_deriv_k_t_radical_in_field
    import prde
    DecrementLevel(DE)
    (ba, bd) = frac_in(b, DE.t)
    A = is_log_deriv_k_t_radical_in_field(ba, bd, DE)
# WARNING: Decompyle incomplete


def cancel_exp(b, c, n, DE):
    '''
    Poly Risch Differential Equation - Cancellation: Hyperexponential case.

    Explanation
    ===========

    Given a derivation D on k[t], n either an integer or +oo, ``b`` in k, and
    ``c`` in k[t] with Dt/t in k and ``b != 0``, either raise
    NonElementaryIntegralException, in which case the equation Dq + b*q == c
    has no solution of degree at most n in k[t], or a solution q in k[t] of
    this equation with deg(q) <= n.
    '''
    parametric_log_deriv = parametric_log_deriv
    import prde
    eta = DE.d.quo(Poly(DE.t, DE.t)).as_expr()
    DecrementLevel(DE)
    (etaa, etad) = frac_in(eta, DE.t)
    (ba, bd) = frac_in(b, DE.t)
    A = parametric_log_deriv(ba, bd, etaa, etad, DE)
# WARNING: Decompyle incomplete


def solve_poly_rde(b, cQ, n, DE, parametric = (False,)):
    '''
    Solve a Polynomial Risch Differential Equation with degree bound ``n``.

    This constitutes step 4 of the outline given in the rde.py docstring.

    For parametric=False, cQ is c, a Poly; for parametric=True, cQ is Q ==
    [q1, ..., qm], a list of Polys.
    '''
    pass
# WARNING: Decompyle incomplete


def rischDE(fa, fd, ga, gd, DE):
    '''
    Solve a Risch Differential Equation: Dy + f*y == g.

    Explanation
    ===========

    See the outline in the docstring of rde.py for more information
    about the procedure used.  Either raise NonElementaryIntegralException, in
    which case there is no solution y in the given differential field,
    or return y in k(t) satisfying Dy + f*y == g, or raise
    NotImplementedError, in which case, the algorithms necessary to
    solve the given Risch Differential Equation have not yet been
    implemented.
    '''
    (fa, fd) = (_,)
    (ba, bd) = (a,)
    (ca, cd) = normal_denom(fa, fd, ga, gd, DE)
    hn = weak_normalizer(fa, fd, DE)
    (A, B, C, hs) = special_denom(a, ba, bd, ca, cd, DE)
    
    try:
        n = bound_degree(A, B, C, DE)
    except NotImplementedError:
        n = oo

    (B, C, m, alpha, beta) = spde(A, B, C, n, DE)
    if C.is_zero:
        y = C
    else:
        y = solve_poly_rde(B, C, m, DE)
    return (alpha * y + beta, hn * hs)
