# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error_functions.pyc (Python 3.11)

''' This module contains various functions that are special cases
    of incomplete gamma functions. It should probably be renamed. '''
from sympy.core import EulerGamma
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.function import Function, ArgumentIndexError, expand_mul
from sympy.core.numbers import I, pi, Rational
from sympy.core.relational import is_eq
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.core.symbol import Dummy, uniquely_named_symbol
from sympy.core.sympify import sympify
from sympy.functions.combinatorial.factorials import factorial, factorial2, RisingFactorial
from sympy.functions.elementary.complexes import polar_lift, re, unpolarify
from sympy.functions.elementary.integers import ceiling, floor
from sympy.functions.elementary.miscellaneous import sqrt, root
from sympy.functions.elementary.exponential import exp, log, exp_polar
from sympy.functions.elementary.hyperbolic import cosh, sinh
from sympy.functions.elementary.trigonometric import cos, sin, sinc
from sympy.functions.special.hyper import hyper, meijerg

def real_to_real_as_real_imag(self, deep = (True,), **hints):
    pass
# WARNING: Decompyle incomplete


class erf(Function):
    pass
# WARNING: Decompyle incomplete


class erfc(Function):
    '''
    Complementary Error Function.

    Explanation
    ===========

    The function is defined as:

    .. math ::
        \\mathrm{erfc}(x) = \\frac{2}{\\sqrt{\\pi}} \\int_x^\\infty e^{-t^2} \\mathrm{d}t

    Examples
    ========

    >>> from sympy import I, oo, erfc
    >>> from sympy.abc import z

    Several special values are known:

    >>> erfc(0)
    1
    >>> erfc(oo)
    0
    >>> erfc(-oo)
    2
    >>> erfc(I*oo)
    -oo*I
    >>> erfc(-I*oo)
    oo*I

    The error function obeys the mirror symmetry:

    >>> from sympy import conjugate
    >>> conjugate(erfc(z))
    erfc(conjugate(z))

    Differentiation with respect to $z$ is supported:

    >>> from sympy import diff
    >>> diff(erfc(z), z)
    -2*exp(-z**2)/sqrt(pi)

    It also follows

    >>> erfc(-z)
    2 - erfc(z)

    We can numerically evaluate the complementary error function to arbitrary
    precision on the whole complex plane:

    >>> erfc(4).evalf(30)
    0.0000000154172579002800188521596734869

    >>> erfc(4*I).evalf(30)
    1.0 - 1296959.73071763923152794095062*I

    See Also
    ========

    erf: Gaussian error function.
    erfi: Imaginary error function.
    erf2: Two-argument error function.
    erfinv: Inverse error function.
    erfcinv: Inverse Complementary error function.
    erf2inv: Inverse two-argument error function.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Error_function
    .. [2] https://dlmf.nist.gov/7
    .. [3] https://mathworld.wolfram.com/Erfc.html
    .. [4] https://functions.wolfram.com/GammaBetaErf/Erfc

    '''
    unbranched = True
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return -2 * exp(-self.args[0] ** 2) / sqrt(pi)
        raise None(self, argindex)

    
    def inverse(self, argindex = (1,)):
        '''
        Returns the inverse of this function.

        '''
        return erfcinv

    eval = (lambda cls, arg:
