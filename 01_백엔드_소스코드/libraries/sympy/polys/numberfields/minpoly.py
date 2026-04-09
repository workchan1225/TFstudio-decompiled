# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: minpoly.pyc (Python 3.11)

'''Minimal polynomials for algebraic numbers.'''
from functools import reduce
from sympy.core.add import Add
from sympy.core.exprtools import Factors
from sympy.core.function import expand_mul, expand_multinomial, _mexpand
from sympy.core.mul import Mul
from sympy.core.numbers import I, Rational, pi, _illegal
from sympy.core.singleton import S
from sympy.core.symbol import Dummy
from sympy.core.sympify import sympify
from sympy.core.traversal import preorder_traversal
from sympy.functions.elementary.exponential import exp
from sympy.functions.elementary.miscellaneous import sqrt, cbrt
from sympy.functions.elementary.trigonometric import cos, sin, tan
from sympy.ntheory.factor_ import divisors
from sympy.utilities.iterables import subsets
from sympy.polys.domains import ZZ, QQ, FractionField
from sympy.polys.orthopolys import dup_chebyshevt
from sympy.polys.polyerrors import NotAlgebraic, GeneratorsError
from sympy.polys.polytools import Poly, PurePoly, invert, factor_list, groebner, resultant, degree, poly_from_expr, parallel_poly_from_expr, lcm
from sympy.polys.polyutils import dict_from_expr, expr_from_dict
from sympy.polys.ring_series import rs_compose_add
from sympy.polys.rings import ring
from sympy.polys.rootoftools import CRootOf
from sympy.polys.specialpolys import cyclotomic_poly
from sympy.utilities import numbered_symbols, public, sift

def _choose_factor(factors, x, v, dom, prec, bound = (QQ, 200, 5)):
    '''
    Return a factor having root ``v``
    It is assumed that one of the factors has root ``v``.
    '''
    pass
# WARNING: Decompyle incomplete


def _is_sum_surds(p):
    args = p.args if p.is_Add else [
        p]
    for y in args:
        if not (y ** 2).is_Rational or y.is_extended_real:
            return False
        return True


def _separate_sq(p):
    '''
    helper function for ``_minimal_polynomial_sq``

    It selects a rational ``g`` such that the polynomial ``p``
    consists of a sum of terms whose surds squared have gcd equal to ``g``
    and a sum of terms with surds squared prime with ``g``;
    then it takes the field norm to eliminate ``sqrt(g)``

    See simplify.simplify.split_surds and polytools.sqf_norm.

    Examples
    ========

    >>> from sympy import sqrt
    >>> from sympy.abc import x
    >>> from sympy.polys.numberfields.minpoly import _separate_sq
    >>> p= -x + sqrt(2) + sqrt(3) + sqrt(7)
    >>> p = _separate_sq(p); p
    -x**2 + 2*sqrt(3)*x + 2*sqrt(7)*x - 2*sqrt(21) - 8
    >>> p = _separate_sq(p); p
    -x**4 + 4*sqrt(7)*x**3 - 32*x**2 + 8*sqrt(7)*x + 20
    >>> p = _separate_sq(p); p
    -x**8 + 48*x**6 - 536*x**4 + 1728*x**2 - 400

    '''
    
    def is_sqrt(expr):
        if expr.is_Pow:
            pass
        return expr.exp is S.Half

    a = []
# WARNING: Decompyle incomplete


def _minimal_polynomial_sq(p, n, x):
    '''
    Returns the minimal polynomial for the ``nth-root`` of a sum of surds
    or ``None`` if it fails.

    Parameters
    ==========

    p : sum of surds
    n : positive integer
    x : variable of the returned polynomial

    Examples
    ========

    >>> from sympy.polys.numberfields.minpoly import _minimal_polynomial_sq
    >>> from sympy import sqrt
    >>> from sympy.abc import x
    >>> q = 1 + sqrt(2) + sqrt(3)
    >>> _minimal_polynomial_sq(q, 3, x)
    x**12 - 4*x**9 - 4*x**6 + 16*x**3 - 8

    '''
    p = sympify(p)
    n = sympify(n)
    if not n.is_Integer and n > 0 or _is_sum_surds(p):
        return None
    pn = None ** Rational(1, n)
    p -= x
    p1 = _separate_sq(p)
    if p1 is p:
        p = p1.subs({
            x: x ** n })
    else:
        p = p1
    if n == 1:
        p1 = Poly(p)
        if p.coeff(x ** p1.degree(x)) < 0:
            p = -p
        p = p.primitive()[1]
        return p
    factors = None(p)[1]
    result = _choose_factor(factors, x, pn)
    return result


def _minpoly_op_algebraic_element(op, ex1, ex2, x, dom, mp1, mp2 = (None, None)):
    '''
    return the minimal polynomial for ``op(ex1, ex2)``

    Parameters
    ==========

    op : operation ``Add`` or ``Mul``
    ex1, ex2 : expressions for the algebraic elements
    x : indeterminate of the polynomials
    dom: ground domain
    mp1, mp2 : minimal polynomials for ``ex1`` and ``ex2`` or None

    Examples
    ========

    >>> from sympy import sqrt, Add, Mul, QQ
    >>> from sympy.polys.numberfields.minpoly import _minpoly_op_algebraic_element
    >>> from sympy.abc import x, y
    >>> p1 = sqrt(sqrt(2) + 1)
    >>> p2 = sqrt(sqrt(2) - 1)
    >>> _minpoly_op_algebraic_element(Mul, p1, p2, x, QQ)
    x - 1
    >>> q1 = sqrt(y)
    >>> q2 = 1 / y
    >>> _minpoly_op_algebraic_element(Add, q1, q2, x, QQ.frac_field(y))
    x**2*y**2 - 2*x*y - y**3 + 1

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Resultant
    .. [2] I.M. Isaacs, Proc. Amer. Math. Soc. 25 (1970), 638
           "Degrees of sums in a separable field extension".

    '''
    y = Dummy(str(x))
# WARNING: Decompyle incomplete


def _invertx(p, x):
    '''
    Returns ``expand_mul(x**degree(p, x)*p.subs(x, 1/x))``
    '''
    pass
# WARNING: Decompyle incomplete


def _muly(p, x, y):
    '''
    Returns ``_mexpand(y**deg*p.subs({x:x / y}))``
    '''
    pass
# WARNING: Decompyle incomplete


def _minpoly_pow(ex, pw, x, dom, mp = (None,)):
    '''
    Returns ``minpoly(ex**pw, x)``

    Parameters
    ==========

    ex : algebraic element
    pw : rational number
    x : indeterminate of the polynomial
    dom: ground domain
    mp : minimal polynomial of ``p``

    Examples
    ========

    >>> from sympy import sqrt, QQ, Rational
    >>> from sympy.polys.numberfields.minpoly import _minpoly_pow, minpoly
    >>> from sympy.abc import x, y
    >>> p = sqrt(1 + sqrt(2))
    >>> _minpoly_pow(p, 2, x, QQ)
    x**2 - 2*x - 1
    >>> minpoly(p**2, x)
    x**2 - 2*x - 1
    >>> _minpoly_pow(y, Rational(1, 3), x, QQ.frac_field(y))
    x**3 - y
    >>> minpoly(y**Rational(1, 3), x)
    x**3 - y

    '''
    pw = sympify(pw)
    if not mp:
        mp = _minpoly_compose(ex, x, dom)
    if not pw.is_rational:
        raise NotAlgebraic('%s does not seem to be an algebraic element' % ex)
    if pw < 0:
        if mp == x:
            raise ZeroDivisionError('%s is zero' % ex)
        mp = _invertx(mp, x)
        if pw == -1:
            return mp
        pw = -None
        ex = 1 / ex
    y = Dummy(str(x))
    mp = mp.subs({
        x: y })
    (n, d) = pw.as_numer_denom()
    res = Poly(resultant(mp, x ** d - y ** n, gens = [
        y]), x, domain = dom)
    (_, factors) = res.factor_list()
    res = _choose_factor(factors, x, ex ** pw, dom)
    return res.as_expr()


def _minpoly_add(x, dom, *a):
    '''
    returns ``minpoly(Add(*a), dom, x)``
    '''
    mp = _minpoly_op_algebraic_element(Add, a[0], a[1], x, dom)
    p = a[0] + a[1]
    for px in a[2:]:
        mp = _minpoly_op_algebraic_element(Add, p, px, x, dom, mp1 = mp)
        p = p + px
        return mp


def _minpoly_mul(x, dom, *a):
    '''
    returns ``minpoly(Mul(*a), dom, x)``
    '''
    mp = _minpoly_op_algebraic_element(Mul, a[0], a[1], x, dom)
    p = a[0] * a[1]
    for px in a[2:]:
        mp = _minpoly_op_algebraic_element(Mul, p, px, x, dom, mp1 = mp)
        p = p * px
        return mp


def _minpoly_sin(ex, x):
    '''
    Returns the minimal polynomial of ``sin(ex)``
    see https://mathworld.wolfram.com/TrigonometryAngles.html
    '''
    pass
# WARNING: Decompyle incomplete


def _minpoly_cos(ex, x):
    '''
    Returns the minimal polynomial of ``cos(ex)``
    see https://mathworld.wolfram.com/TrigonometryAngles.html
    '''
    pass
# WARNING: Decompyle incomplete


def _minpoly_tan(ex, x):
    '''
    Returns the minimal polynomial of ``tan(ex)``
    see https://github.com/sympy/sympy/issues/21430
    '''
    (c, a) = ex.args[0].as_coeff_Mul()
# WARNING: Decompyle incomplete


def _minpoly_exp(ex, x):
    '''
    Returns the minimal polynomial of ``exp(ex)``
    '''
    pass
# WARNING: Decompyle incomplete


def _minpoly_rootof(ex, x):
    '''
    Returns the minimal polynomial of a ``CRootOf`` object.
    '''
    p = ex.expr
    p = p.subs({
        ex.poly.gens[0]: x })
    (_, factors) = factor_list(p, x)
    result = _choose_factor(factors, x, ex)
    return result


def _minpoly_compose(ex, x, dom):
    '''
    Computes the minimal polynomial of an algebraic element
    using operations on minimal polynomials

    Examples
    ========

    >>> from sympy import minimal_polynomial, sqrt, Rational
    >>> from sympy.abc import x, y
    >>> minimal_polynomial(sqrt(2) + 3*Rational(1, 3), x, compose=True)
    x**2 - 2*x - 1
    >>> minimal_polynomial(sqrt(y) + 1/y, x, compose=True)
    x**2*y**2 - 2*x*y - y**3 + 1

    '''
    pass
# WARNING: Decompyle incomplete

minimal_polynomial = (lambda ex, x, compose, polys, domain = (None, True, False, None): ex = sympify(ex)if ex.is_number:
ex = _mexpand(ex, recursive = True)# WARNING: Decompyle incomplete
)()

def _minpoly_groebner(ex, x, cls):
    '''
    Computes the minimal polynomial of an algebraic number
    using Groebner bases

    Examples
    ========

    >>> from sympy import minimal_polynomial, sqrt, Rational
    >>> from sympy.abc import x
    >>> minimal_polynomial(sqrt(2) + 3*Rational(1, 3), x, compose=False)
    x**2 - 2*x - 1

    '''
    pass
# WARNING: Decompyle incomplete

minpoly = (lambda ex, x, compose, polys, domain = (None, True, False, None): minimal_polynomial(ex, x = x, compose = compose, polys = polys, domain = domain))()
