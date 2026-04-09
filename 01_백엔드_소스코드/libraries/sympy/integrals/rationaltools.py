# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rationaltools.pyc (Python 3.11)

'''This module implements tools for integrating rational functions. '''
from sympy.core.function import Lambda
from sympy.core.numbers import I
from sympy.core.singleton import S
from sympy.core.symbol import Dummy, Symbol, symbols
from sympy.functions.elementary.exponential import log
from sympy.functions.elementary.trigonometric import atan
from sympy.polys.polyroots import roots
from sympy.polys.polytools import cancel
from sympy.polys.rootoftools import RootSum
from sympy.polys import Poly, resultant, ZZ

def ratint(f, x, **flags):
    """
    Performs indefinite integration of rational functions.

    Explanation
    ===========

    Given a field :math:`K` and a rational function :math:`f = p/q`,
    where :math:`p` and :math:`q` are polynomials in :math:`K[x]`,
    returns a function :math:`g` such that :math:`f = g'`.

    Examples
    ========

    >>> from sympy.integrals.rationaltools import ratint
    >>> from sympy.abc import x

    >>> ratint(36/(x**5 - 2*x**4 - 2*x**3 + 4*x**2 + x - 2), x)
    (12*x + 6)/(x**2 - 1) + 4*log(x - 2) - 4*log(x + 1)

    References
    ==========

    .. [1] M. Bronstein, Symbolic Integration I: Transcendental
       Functions, Second Edition, Springer-Verlag, 2005, pp. 35-70

    See Also
    ========

    sympy.integrals.integrals.Integral.doit
    sympy.integrals.rationaltools.ratint_logpart
    sympy.integrals.rationaltools.ratint_ratpart

    """
    if isinstance(f, tuple):
        (p, q) = f
    else:
        (p, q) = f.as_numer_denom()
    q = Poly(q, x, composite = False, field = True)
    p = Poly(p, x, composite = False, field = True)
    (coeff, p, q) = p.cancel(q)
    (poly, p) = p.div(q)
    result = poly.integrate(x).as_expr()
    if p.is_zero:
        return coeff * result
    (g, h) = None(p, q, x)
    (P, Q) = h.as_numer_denom()
    P = Poly(P, x)
    Q = Poly(Q, x)
    (q, r) = P.div(Q)
    result += g + q.integrate(x).as_expr()
# WARNING: Decompyle incomplete


def ratint_ratpart(f, g, x):
    """
    Horowitz-Ostrogradsky algorithm.

    Explanation
    ===========

    Given a field K and polynomials f and g in K[x], such that f and g
    are coprime and deg(f) < deg(g), returns fractions A and B in K(x),
    such that f/g = A' + B and B has square-free denominator.

    Examples
    ========

        >>> from sympy.integrals.rationaltools import ratint_ratpart
        >>> from sympy.abc import x, y
        >>> from sympy import Poly
        >>> ratint_ratpart(Poly(1, x, domain='ZZ'),
        ... Poly(x + 1, x, domain='ZZ'), x)
        (0, 1/(x + 1))
        >>> ratint_ratpart(Poly(1, x, domain='EX'),
        ... Poly(x**2 + y**2, x, domain='EX'), x)
        (0, 1/(x**2 + y**2))
        >>> ratint_ratpart(Poly(36, x, domain='ZZ'),
        ... Poly(x**5 - 2*x**4 - 2*x**3 + 4*x**2 + x - 2, x, domain='ZZ'), x)
        ((12*x + 6)/(x**2 - 1), 12/(x**2 - x - 2))

    See Also
    ========

    ratint, ratint_logpart
    """
    pass
# WARNING: Decompyle incomplete


def ratint_logpart(f, g, x, t = (None,)):
    """
    Lazard-Rioboo-Trager algorithm.

    Explanation
    ===========

    Given a field K and polynomials f and g in K[x], such that f and g
    are coprime, deg(f) < deg(g) and g is square-free, returns a list
    of tuples (s_i, q_i) of polynomials, for i = 1..n, such that s_i
    in K[t, x] and q_i in K[t], and::

                           ___    ___
                 d  f   d  \\  `   \\  `
                 -- - = --  )      )   a log(s_i(a, x))
                 dx g   dx /__,   /__,
                          i=1..n a | q_i(a) = 0

    Examples
    ========

    >>> from sympy.integrals.rationaltools import ratint_logpart
    >>> from sympy.abc import x
    >>> from sympy import Poly
    >>> ratint_logpart(Poly(1, x, domain='ZZ'),
    ... Poly(x**2 + x + 1, x, domain='ZZ'), x)
    [(Poly(x + 3*_t/2 + 1/2, x, domain='QQ[_t]'),
    ...Poly(3*_t**2 + 1, _t, domain='ZZ'))]
    >>> ratint_logpart(Poly(12, x, domain='ZZ'),
    ... Poly(x**2 - x - 2, x, domain='ZZ'), x)
    [(Poly(x - 3*_t/8 - 1/2, x, domain='QQ[_t]'),
    ...Poly(-_t**2 + 16, _t, domain='ZZ'))]

    See Also
    ========

    ratint, ratint_ratpart
    """
    g = Poly(g, x)
    f = Poly(f, x)
# WARNING: Decompyle incomplete


def log_to_atan(f, g):
    """
    Convert complex logarithms to real arctangents.

    Explanation
    ===========

    Given a real field K and polynomials f and g in K[x], with g != 0,
    returns a sum h of arctangents of polynomials in K[x], such that:

                   dh   d         f + I g
                   -- = -- I log( ------- )
                   dx   dx        f - I g

    Examples
    ========

        >>> from sympy.integrals.rationaltools import log_to_atan
        >>> from sympy.abc import x
        >>> from sympy import Poly, sqrt, S
        >>> log_to_atan(Poly(x, x, domain='ZZ'), Poly(1, x, domain='ZZ'))
        2*atan(x)
        >>> log_to_atan(Poly(x + S(1)/2, x, domain='QQ'),
        ... Poly(sqrt(3)/2, x, domain='EX'))
        2*atan(2*sqrt(3)*x/3 + sqrt(3)/3)

    See Also
    ========

    log_to_real
    """
    if f.degree() < g.degree():
        g = f
        f = -g
    f = f.to_field()
    g = g.to_field()
    (p, q) = f.div(g)
    if q.is_zero:
        return 2 * atan(p.as_expr())
    (s, t, h) = None.gcdex(-f)
    u = (f * s + g * t).quo(h)
    A = 2 * atan(u.as_expr())
    return A + log_to_atan(s, t)


def log_to_real(h, q, x, t):
    """
    Convert complex logarithms to real functions.

    Explanation
    ===========

    Given real field K and polynomials h in K[t,x] and q in K[t],
    returns real function f such that:
                          ___
                  df   d  \\  `
                  -- = --  )  a log(h(a, x))
                  dx   dx /__,
                         a | q(a) = 0

    Examples
    ========

        >>> from sympy.integrals.rationaltools import log_to_real
        >>> from sympy.abc import x, y
        >>> from sympy import Poly, S
        >>> log_to_real(Poly(x + 3*y/2 + S(1)/2, x, domain='QQ[y]'),
        ... Poly(3*y**2 + 1, y, domain='ZZ'), x, y)
        2*sqrt(3)*atan(2*sqrt(3)*x/3 + sqrt(3)/3)/3
        >>> log_to_real(Poly(x**2 - 1, x, domain='ZZ'),
        ... Poly(-2*y + 1, y, domain='ZZ'), x, y)
        log(x**2 - 1)/2

    See Also
    ========

    log_to_atan
    """
    collect = collect
    import sympy.simplify.radsimp
    (u, v) = symbols('u,v', cls = Dummy)
    H = h.as_expr().xreplace({
        t: u + I * v }).expand()
    Q = q.as_expr().xreplace({
        t: u + I * v }).expand()
    H_map = collect(H, I, evaluate = False)
    Q_map = collect(Q, I, evaluate = False)
    b = H_map.get(I, S.Zero)
    a = H_map.get(S.One, S.Zero)
    d = Q_map.get(I, S.Zero)
    c = Q_map.get(S.One, S.Zero)
    R = Poly(resultant(c, d, v), u)
    R_u = roots(R, filter = 'R')
    if len(R_u) != R.count_roots():
        return None
    result = None.Zero
    for r_u in R_u.keys():
        C = Poly(c.xreplace({
            u: r_u }), v)
        if not C:
            C = Poly(d.xreplace({
                u: r_u }), v)
            d = S.Zero
        R_v = roots(C, filter = 'R')
        if len(R_v) != C.count_roots():
            return None
        R_v_paired = None
        for r_v in R_v:
            if r_v not in R_v_paired and -r_v not in R_v_paired:
                if r_v.is_negative or r_v.could_extract_minus_sign():
                    R_v_paired.append(-r_v)
                    continue
                if not r_v.is_zero:
                    R_v_paired.append(r_v)
            for r_v in R_v_paired:
                D = d.xreplace({
                    v: r_v,
                    u: r_u })
                if D.evalf(chop = True) != 0:
                    continue
                A = Poly(a.xreplace({
                    v: r_v,
                    u: r_u }), x)
                B = Poly(b.xreplace({
                    v: r_v,
                    u: r_u }), x)
                AB = (A ** 2 + B ** 2).as_expr()
                result += r_u * log(AB) + r_v * log_to_atan(A, B)
                R_q = roots(q, filter = 'R')
                if len(R_q) != q.count_roots():
                    return None
                for r in None.keys():
                    result += r * log(h.as_expr().subs(t, r))
                    return result
