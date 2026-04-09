# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ring_series.pyc (Python 3.11)

'''Power series evaluation and manipulation using sparse Polynomials

Implementing a new function
---------------------------

There are a few things to be kept in mind when adding a new function here::

    - The implementation should work on all possible input domains/rings.
      Special cases include the ``EX`` ring and a constant term in the series
      to be expanded. There can be two types of constant terms in the series:

        + A constant value or symbol.
        + A term of a multivariate series not involving the generator, with
          respect to which the series is to expanded.

      Strictly speaking, a generator of a ring should not be considered a
      constant. However, for series expansion both the cases need similar
      treatment (as the user does not care about inner details), i.e, use an
      addition formula to separate the constant part and the variable part (see
      rs_sin for reference).

    - All the algorithms used here are primarily designed to work for Taylor
      series (number of iterations in the algo equals the required order).
      Hence, it becomes tricky to get the series of the right order if a
      Puiseux series is input. Use rs_puiseux? in your function if your
      algorithm is not designed to handle fractional powers.

Extending rs_series
-------------------

To make a function work with rs_series you need to do two things::

    - Many sure it works with a constant term (as explained above).
    - If the series contains constant terms, you might need to extend its ring.
      You do so by adding the new terms to the rings as generators.
      ``PolyRing.compose`` and ``PolyRing.add_gens`` are two functions that do
      so and need to be called every time you expand a series containing a
      constant term.

Look at rs_sin and rs_series for further reference.

'''
from sympy.polys.domains import QQ, EX
from sympy.polys.rings import PolyElement, ring, sring
from sympy.polys.polyerrors import DomainError
from sympy.polys.monomials import monomial_min, monomial_mul, monomial_div, monomial_ldiv
from mpmath.libmp.libintmath import ifac
from sympy.core import PoleError, Function, Expr
from sympy.core.numbers import Rational
from sympy.core.intfunc import igcd
from sympy.functions import sin, cos, tan, atan, exp, atanh, tanh, log, ceiling
from sympy.utilities.misc import as_int
from mpmath.libmp.libintmath import giant_steps
import math

def _invert_monoms(p1):
    """
    Compute ``x**n * p1(1/x)`` for a univariate polynomial ``p1`` in ``x``.

    Examples
    ========

    >>> from sympy.polys.domains import ZZ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import _invert_monoms
    >>> R, x = ring('x', ZZ)
    >>> p = x**2 + 2*x + 3
    >>> _invert_monoms(p)
    3*x**2 + 2*x + 1

    See Also
    ========

    sympy.polys.densebasic.dup_reverse
    """
    terms = list(p1.items())
    terms.sort()
    deg = p1.degree()
    R = p1.ring
    p = R.zero
    cv = p1.listcoeffs()
    mv = p1.listmonoms()
    for mvi, cvi in zip(mv, cv):
        p[(deg - mvi[0],)] = cvi
        return p


def _giant_steps(target):
    """Return a list of precision steps for the Newton's method"""
    res = giant_steps(2, target)
    if res[0] != 2:
        res = [
            2] + res
    return res


def rs_trunc(p1, x, prec):
    """
    Truncate the series in the ``x`` variable with precision ``prec``,
    that is, modulo ``O(x**prec)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_trunc
    >>> R, x = ring('x', QQ)
    >>> p = x**10 + x**5 + x + 1
    >>> rs_trunc(p, x, 12)
    x**10 + x**5 + x + 1
    >>> rs_trunc(p, x, 10)
    x**5 + x + 1
    """
    R = p1.ring
    p = R.zero
    i = R.gens.index(x)
    for exp1 in p1:
        if exp1[i] >= prec:
            continue
        p[exp1] = p1[exp1]
        return p


def rs_is_puiseux(p, x):
    """
    Test if ``p`` is Puiseux series in ``x``.

    Raise an exception if it has a negative power in ``x``.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_is_puiseux
    >>> R, x = ring('x', QQ)
    >>> p = x**QQ(2,5) + x**QQ(2,3) + x
    >>> rs_is_puiseux(p, x)
    True
    """
    index = p.ring.gens.index(x)
    for k in p:
        if k[index] != int(k[index]):
            return True
        if None[index] < 0:
            raise ValueError('The series is not regular in %s' % x)
        return False


def rs_puiseux(f, p, x, prec):
    """
    Return the puiseux series for `f(p, x, prec)`.

    To be used when function ``f`` is implemented only for regular series.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_puiseux, rs_exp
    >>> R, x = ring('x', QQ)
    >>> p = x**QQ(2,5) + x**QQ(2,3) + x
    >>> rs_puiseux(rs_exp,p, x, 1)
    1/2*x**(4/5) + x**(2/3) + x**(2/5) + 1
    """
    pass
# WARNING: Decompyle incomplete


def rs_puiseux2(f, p, q, x, prec):
    '''
    Return the puiseux series for `f(p, q, x, prec)`.

    To be used when function ``f`` is implemented only for regular series.
    '''
    index = p.ring.gens.index(x)
    n = 1
    for k in p:
        power = k[index]
        if isinstance(power, Rational):
            (num, den) = power.as_numer_denom()
            n = n * den // igcd(n, den)
            continue
        if power != int(power):
            den = power.denominator
            n = n * den // igcd(n, den)
        if n != 1:
            p1 = pow_xin(p, index, n)
            r = f(p1, q, x, prec * n)
            n1 = QQ(1, n)
            r = pow_xin(r, index, n1)
        else:
            r = f(p, q, x, prec)
    return r


def rs_mul(p1, p2, x, prec):
    """
    Return the product of the given two series, modulo ``O(x**prec)``.

    ``x`` is the series variable or its position in the generators.

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_mul
    >>> R, x = ring('x', QQ)
    >>> p1 = x**2 + 2*x + 1
    >>> p2 = x + 1
    >>> rs_mul(p1, p2, x, 3)
    3*x**2 + 3*x + 1
    """
    pass
# WARNING: Decompyle incomplete


def rs_square(p1, x, prec):
    """
    Square the series modulo ``O(x**prec)``

    Examples
    ========

    >>> from sympy.polys.domains import QQ
    >>> from sympy.polys.rings import ring
    >>> from sympy.polys.ring_series import rs_square
    >>> R, x = ring('x', QQ)
    >>> p = x**2 + 2*x + 1
    >>> rs_square(p, x, 3)
    6*x**2 + 4*x + 1
    """
    pass
# WARNING: Decompyle incomplete


def rs_pow(p1, n, x, prec):
