# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: trigonometry.pyc (Python 3.11)

from sympy.core import cacheit, Dummy, Ne, Integer, Rational, S, Wild
from sympy.functions import binomial, sin, cos, Piecewise, Abs
from integrals import integrate

def _integer_instance(n):
    return isinstance(n, Integer)

_pat_sincos = (lambda x: pass# WARNING: Decompyle incomplete
)()
_u = Dummy('u')

def trigintegrate(f, x, conds = ('piecewise',)):
    '''
    Integrate f = Mul(trig) over x.

    Examples
    ========

    >>> from sympy import sin, cos, tan, sec
    >>> from sympy.integrals.trigonometry import trigintegrate
    >>> from sympy.abc import x

    >>> trigintegrate(sin(x)*cos(x), x)
    sin(x)**2/2

    >>> trigintegrate(sin(x)**2, x)
    x/2 - sin(x)*cos(x)/2

    >>> trigintegrate(tan(x)*sec(x), x)
    1/cos(x)

    >>> trigintegrate(sin(x)*tan(x), x)
    -log(sin(x) - 1)/2 + log(sin(x) + 1)/2 - sin(x)

    References
    ==========

    .. [1] https://en.wikibooks.org/wiki/Calculus/Integration_techniques

    See Also
    ========

    sympy.integrals.integrals.Integral.doit
    sympy.integrals.integrals.Integral
    '''
    (pat, a, n, m) = _pat_sincos(x)
    f = f.rewrite('sincos')
    M = f.match(pat)
# WARNING: Decompyle incomplete


def _sin_pow_integrate(n, x):
    if n > 0:
        if n == 1:
            return -cos(x)
        return None(-1, n) * cos(x) * sin(x) ** (n - 1) + Rational(n - 1, n) * _sin_pow_integrate(n - 2, x)
    if None < 0:
        if n == -1:
            return trigintegrate(1 / sin(x), x)
        return None(1, n + 1) * cos(x) * sin(x) ** (n + 1) + Rational(n + 2, n + 1) * _sin_pow_integrate(n + 2, x)


def _cos_pow_integrate(n, x):
    if n > 0:
        if n == 1:
            return sin(x)
        return None(1, n) * sin(x) * cos(x) ** (n - 1) + Rational(n - 1, n) * _cos_pow_integrate(n - 2, x)
    if None < 0:
        if n == -1:
            return trigintegrate(1 / cos(x), x)
        return None(-1, n + 1) * sin(x) * cos(x) ** (n + 1) + Rational(n + 2, n + 1) * _cos_pow_integrate(n + 2, x)
