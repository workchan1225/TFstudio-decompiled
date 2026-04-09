# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyroots.pyc (Python 3.11)

'''Algorithms for computing symbolic roots of polynomials. '''
import math
from functools import reduce
from sympy.core import S, I, pi
from sympy.core.exprtools import factor_terms
from sympy.core.function import _mexpand
from sympy.core.logic import fuzzy_not
from sympy.core.mul import expand_2arg, Mul
from sympy.core.intfunc import igcd
from sympy.core.numbers import Rational, comp
from sympy.core.power import Pow
from sympy.core.relational import Eq
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy, Symbol, symbols
from sympy.core.sympify import sympify
from sympy.functions import exp, im, cos, acos, Piecewise
from sympy.functions.elementary.miscellaneous import root, sqrt
from sympy.ntheory import divisors, isprime, nextprime
from sympy.polys.domains import EX
from sympy.polys.polyerrors import PolynomialError, GeneratorsNeeded, DomainError, UnsolvableFactorError
from sympy.polys.polyquinticconst import PolyQuintic
from sympy.polys.polytools import Poly, cancel, factor, gcd_list, discriminant
from sympy.polys.rationaltools import together
from sympy.polys.specialpolys import cyclotomic_poly
from sympy.utilities import public
from sympy.utilities.misc import filldedent
z = Symbol('z')

def roots_linear(f):
    '''Returns a list of roots of a linear polynomial.'''
    r = -f.nth(0) / f.nth(1)
    dom = f.get_domain()
    if not dom.is_Numerical:
        if dom.is_Composite:
            r = factor(r)
        else:
            simplify = simplify
            import sympy.simplify.simplify
            r = simplify(r)
    return [
        r]


def roots_quadratic(f):
    '''Returns a list of roots of a quadratic polynomial. If the domain is ZZ
    then the roots will be sorted with negatives coming before positives.
    The ordering will be the same for any numerical coefficients as long as
    the assumptions tested are correct, otherwise the ordering will not be
    sorted (but will be canonical).
    '''
    pass
# WARNING: Decompyle incomplete


def roots_cubic(f, trig = (False,)):
    '''Returns a list of roots of a cubic polynomial.

    References
    ==========
    [1] https://en.wikipedia.org/wiki/Cubic_function, General formula for roots,
    (accessed November 17, 2014).
    '''
    pass
# WARNING: Decompyle incomplete


def _roots_quartic_euler(p, q, r, a):
    '''
    Descartes-Euler solution of the quartic equation

    Parameters
    ==========

    p, q, r: coefficients of ``x**4 + p*x**2 + q*x + r``
    a: shift of the roots

    Notes
    =====

    This is a helper function for ``roots_quartic``.

    Look for solutions of the form ::

      ``x1 = sqrt(R) - sqrt(A + B*sqrt(R))``
      ``x2 = -sqrt(R) - sqrt(A - B*sqrt(R))``
      ``x3 = -sqrt(R) + sqrt(A - B*sqrt(R))``
      ``x4 = sqrt(R) + sqrt(A + B*sqrt(R))``

    To satisfy the quartic equation one must have
    ``p = -2*(R + A); q = -4*B*R; r = (R - A)**2 - B**2*R``
    so that ``R`` must satisfy the Descartes-Euler resolvent equation
    ``64*R**3 + 32*p*R**2 + (4*p**2 - 16*r)*R - q**2 = 0``

    If the resolvent does not have a rational solution, return None;
    in that case it is likely that the Ferrari method gives a simpler
    solution.

    Examples
    ========

    >>> from sympy import S
    >>> from sympy.polys.polyroots import _roots_quartic_euler
    >>> p, q, r = -S(64)/5, -S(512)/125, -S(1024)/3125
    >>> _roots_quartic_euler(p, q, r, S(0))[0]
    -sqrt(32*sqrt(5)/125 + 16/5) + 4*sqrt(5)/5
    '''
    x = Dummy('x')
    eq = 64 * x ** 3 + 32 * p * x ** 2 + (4 * p ** 2 - 16 * r) * x - q ** 2
    xsols = list(roots(Poly(eq, x), cubics = False).keys())
    xsols = xsols()
    if not xsols:
        return None
    R = (lambda .0: pass# WARNING: Decompyle incomplete
)(xsols)
    c1 = sqrt(R)
    B = -q * c1 / (4 * R)
    A = -R - p / 2
    c2 = sqrt(A + B)
    c3 = sqrt(A - B)
    return [
        c1 - c2 - a,
        -c1 - c3 - a,
        -c1 + c3 - a,
        c1 + c2 - a]


def roots_quartic(f):
    """
    Returns a list of roots of a quartic polynomial.

    There are many references for solving quartic expressions available [1-5].
    This reviewer has found that many of them require one to select from among
    2 or more possible sets of solutions and that some solutions work when one
    is searching for real roots but do not work when searching for complex roots
    (though this is not always stated clearly). The following routine has been
    tested and found to be correct for 0, 2 or 4 complex roots.

    The quasisymmetric case solution [6] looks for quartics that have the form
    `x**4 + A*x**3 + B*x**2 + C*x + D = 0` where `(C/A)**2 = D`.

    Although no general solution that is always applicable for all
    coefficients is known to this reviewer, certain conditions are tested
    to determine the simplest 4 expressions that can be returned:

      1) `f = c + a*(a**2/8 - b/2) == 0`
      2) `g = d - a*(a*(3*a**2/256 - b/16) + c/4) = 0`
      3) if `f != 0` and `g != 0` and `p = -d + a*c/4 - b**2/12` then
        a) `p == 0`
        b) `p != 0`

    Examples
    ========

        >>> from sympy import Poly
        >>> from sympy.polys.polyroots import roots_quartic

        >>> r = roots_quartic(Poly('x**4-6*x**3+17*x**2-26*x+20'))

        >>> # 4 complex roots: 1+-I*sqrt(3), 2+-I
        >>> sorted(str(tmp.evalf(n=2)) for tmp in r)
        ['1.0 + 1.7*I', '1.0 - 1.7*I', '2.0 + 1.0*I', '2.0 - 1.0*I']

    References
    ==========

    1. http://mathforum.org/dr.math/faq/faq.cubic.equations.html
    2. https://en.wikipedia.org/wiki/Quartic_function#Summary_of_Ferrari.27s_method
    3. https://planetmath.org/encyclopedia/GaloisTheoreticDerivationOfTheQuarticFormula.html
    4. https://people.bath.ac.uk/masjhd/JHD-CA.pdf
    5. http://www.albmath.org/files/Math_5713.pdf
    6. https://web.archive.org/web/20171002081448/http://www.statemaster.com/encyclopedia/Quartic-equation
    7. https://eqworld.ipmnet.ru/en/solutions/ae/ae0108.pdf
    """
    pass
# WARNING: Decompyle incomplete


def roots_binomial(f):
    '''Returns a list of roots of a binomial polynomial. If the domain is ZZ
    then the roots will be sorted with negatives coming before positives.
    The ordering will be the same for any numerical coefficients as long as
    the assumptions tested are correct, otherwise the ordering will not be
    sorted (but will be canonical).
    '''
    n = f.degree()
    b = f.nth(0)
    a = f.nth(n)
    base = -cancel(b / a)
    alpha = root(base, n)
    if alpha.is_number:
        alpha = alpha.expand(complex = True)
    neg = base.is_negative
    even = n % 2 == 0
    if neg:
        if even == True and (base + 1).is_positive:
            big = True
        else:
            big = False
    ks = []
    imax = n // 2
    if even:
        ks.append(imax)
        imax -= 1
    if not neg:
        ks.append(0)
    for i in range(imax, 0, -1):
        if neg:
            ks.extend([
                i,
                -i])
            continue
        ks.extend([
            -i,
            i])
        if neg:
            ks.append(0)
            if big:
                for i in range(0, len(ks), 2):
                    pair = ks[i:i + 2]
                    pair = list(reversed(pair))
                    d = 2 * I * pi / n
                    roots = []
                    for k in ks:
                        zeta = exp(k * d).expand(complex = True)
                        roots.append((alpha * zeta).expand(power_base = False))
                        return roots


def _inv_totient_estimate(m):
    '''
    Find ``(L, U)`` such that ``L <= phi^-1(m) <= U``.

    Examples
    ========

    >>> from sympy.polys.polyroots import _inv_totient_estimate

    >>> _inv_totient_estimate(192)
    (192, 840)
    >>> _inv_totient_estimate(400)
    (400, 1750)

    '''
    primes = divisors(m)()
    (a, b) = (1, 1)
# WARNING: Decompyle incomplete


def roots_cyclotomic(f, factor = (False,)):
    '''Compute roots of cyclotomic polynomials. '''
    pass
# WARNING: Decompyle incomplete


def roots_quintic(f):
    '''
    Calculate exact roots of a solvable irreducible quintic with rational coefficients.
    Return an empty list if the quintic is reducible or not solvable.
    '''
    pass
# WARNING: Decompyle incomplete


def _quintic_simplify(expr):
    powsimp = powsimp
    import sympy.simplify.simplify
    expr = powsimp(expr)
    expr = cancel(expr)
    return together(expr)


def _integer_basis(poly):
    """Compute coefficient basis for a polynomial over integers.

    Returns the integer ``div`` such that substituting ``x = div*y``
    ``p(x) = m*q(y)`` where the coefficients of ``q`` are smaller
    than those of ``p``.

    For example ``x**5 + 512*x + 1024 = 0``
    with ``div = 4`` becomes ``y**5 + 2*y + 1 = 0``

    Returns the integer ``div`` or ``None`` if there is no possible scaling.

    Examples
    ========

    >>> from sympy.polys import Poly
    >>> from sympy.abc import x
    >>> from sympy.polys.polyroots import _integer_basis
    >>> p = Poly(x**5 + 512*x + 1024, x, domain='ZZ')
    >>> _integer_basis(p)
    4
    """
    pass
# WARNING: Decompyle incomplete


def preprocess_roots(poly):
    '''Try to get rid of symbolic coefficients from ``poly``. '''
    pass
# WARNING: Decompyle incomplete

roots = (lambda f = public, *, auto: pass# WARNING: Decompyle incomplete
)()

def root_factors(f = None, *, filter, *gens, **args):
    '''
    Returns all factors of a univariate polynomial.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.polys.polyroots import root_factors

    >>> root_factors(x**2 - y, x)
    [x - sqrt(y), x + sqrt(y)]

    '''
    args = dict(args)
# WARNING: Decompyle incomplete
