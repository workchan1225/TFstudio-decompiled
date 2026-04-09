# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: groebnertools.pyc (Python 3.11)

'''Groebner bases algorithms. '''
from sympy.core.symbol import Dummy
from sympy.polys.monomials import monomial_mul, monomial_lcm, monomial_divides, term_div
from sympy.polys.orderings import lex
from sympy.polys.polyerrors import DomainError
from sympy.polys.polyconfig import query

def groebner(seq, ring, method = (None,)):
    '''
    Computes Groebner basis for a set of polynomials in `K[X]`.

    Wrapper around the (default) improved Buchberger and the other algorithms
    for computing Groebner bases. The choice of algorithm can be changed via
    ``method`` argument or :func:`sympy.polys.polyconfig.setup`, where
    ``method`` can be either ``buchberger`` or ``f5b``.

    '''
    pass
# WARNING: Decompyle incomplete


def _buchberger(f, ring):
    """
    Computes Groebner basis for a set of polynomials in `K[X]`.

    Given a set of multivariate polynomials `F`, finds another
    set `G`, such that Ideal `F = Ideal G` and `G` is a reduced
    Groebner basis.

    The resulting basis is unique and has monic generators if the
    ground domains is a field. Otherwise the result is non-unique
    but Groebner bases over e.g. integers can be computed (if the
    input polynomials are monic).

    Groebner bases can be used to choose specific generators for a
    polynomial ideal. Because these bases are unique you can check
    for ideal equality by comparing the Groebner bases.  To see if
    one polynomial lies in an ideal, divide by the elements in the
    base and see if the remainder vanishes.

    They can also be used to solve systems of polynomial equations
    as,  by choosing lexicographic ordering,  you can eliminate one
    variable at a time, provided that the ideal is zero-dimensional
    (finite number of solutions).

    Notes
    =====

    Algorithm used: an improved version of Buchberger's algorithm
    as presented in T. Becker, V. Weispfenning, Groebner Bases: A
    Computational Approach to Commutative Algebra, Springer, 1993,
    page 232.

    References
    ==========

    .. [1] [Bose03]_
    .. [2] [Giovini91]_
    .. [3] [Ajwa95]_
    .. [4] [Cox97]_

    """
    pass
# WARNING: Decompyle incomplete


def spoly(p1, p2, ring):
    '''
    Compute LCM(LM(p1), LM(p2))/LM(p1)*p1 - LCM(LM(p1), LM(p2))/LM(p2)*p2
    This is the S-poly provided p1 and p2 are monic
    '''
    LM1 = p1.LM
    LM2 = p2.LM
    LCM12 = ring.monomial_lcm(LM1, LM2)
    m1 = ring.monomial_div(LCM12, LM1)
    m2 = ring.monomial_div(LCM12, LM2)
    s1 = p1.mul_monom(m1)
    s2 = p2.mul_monom(m2)
    s = s1 - s2
    return s


def Sign(f):
    return f[0]


def Polyn(f):
    return f[1]


def Num(f):
    return f[2]


def sig(monomial, index):
    return (monomial, index)


def lbp(signature, polynomial, number):
    return (signature, polynomial, number)


def sig_cmp(u, v, order):
    '''
    Compare two signatures by extending the term order to K[X]^n.

    u < v iff
        - the index of v is greater than the index of u
    or
        - the index of v is equal to the index of u and u[0] < v[0] w.r.t. order

    u > v otherwise
    '''
    if u[1] > v[1]:
        return -1
    if None[1] == v[1] and order(u[0]) < order(v[0]):
        return -1


def sig_key(s, order):
    '''
    Key for comparing two signatures.

    s = (m, k), t = (n, l)

    s < t iff [k > l] or [k == l and m < n]
    s > t otherwise
    '''
    return (-s[1], order(s[0]))


def sig_mult(s, m):
    '''
    Multiply a signature by a monomial.

    The product of a signature (m, i) and a monomial n is defined as
    (m * t, i).
    '''
    return sig(monomial_mul(s[0], m), s[1])


def lbp_sub(f, g):
    '''
    Subtract labeled polynomial g from f.

    The signature and number of the difference of f and g are signature
    and number of the maximum of f and g, w.r.t. lbp_cmp.
    '''
    if sig_cmp(Sign(f), Sign(g), Polyn(f).ring.order) < 0:
        max_poly = g
    else:
        max_poly = f
    ret = Polyn(f) - Polyn(g)
    return lbp(Sign(max_poly), ret, Num(max_poly))


def lbp_mul_term(f, cx):
    '''
    Multiply a labeled polynomial with a term.

    The product of a labeled polynomial (s, p, k) by a monomial is
    defined as (m * s, m * p, k).
    '''
    return lbp(sig_mult(Sign(f), cx[0]), Polyn(f).mul_term(cx), Num(f))


def lbp_cmp(f, g):
    '''
    Compare two labeled polynomials.

    f < g iff
        - Sign(f) < Sign(g)
    or
        - Sign(f) == Sign(g) and Num(f) > Num(g)

    f > g otherwise
    '''
    if sig_cmp(Sign(f), Sign(g), Polyn(f).ring.order) == -1:
        return -1
    if None(f) == Sign(g) and Num(f) > Num(g):
        return -1


def lbp_key(f):
    '''
    Key for comparing two labeled polynomials.
    '''
    return (sig_key(Sign(f), Polyn(f).ring.order), -Num(f))


def critical_pair(f, g, ring):
    '''
    Compute the critical pair corresponding to two labeled polynomials.

    A critical pair is a tuple (um, f, vm, g), where um and vm are
    terms such that um * f - vm * g is the S-polynomial of f and g (so,
    wlog assume um * f > vm * g).
    For performance sake, a critical pair is represented as a tuple
    (Sign(um * f), um, f, Sign(vm * g), vm, g), since um * f creates
    a new, relatively expensive object in memory, whereas Sign(um *
    f) and um are lightweight and f (in the tuple) is a reference to
    an already existing object in memory.
    '''
    domain = ring.domain
    ltf = Polyn(f).LT
    ltg = Polyn(g).LT
    lt = (monomial_lcm(ltf[0], ltg[0]), domain.one)
    um = term_div(lt, ltf, domain)
    vm = term_div(lt, ltg, domain)
    fr = lbp_mul_term(lbp(Sign(f), Polyn(f).leading_term(), Num(f)), um)
    gr = lbp_mul_term(lbp(Sign(g), Polyn(g).leading_term(), Num(g)), vm)
    if lbp_cmp(fr, gr) == -1:
        return (Sign(gr), vm, g, Sign(fr), um, f)
    return (None(fr), um, f, Sign(gr), vm, g)


def cp_cmp(c, d):
