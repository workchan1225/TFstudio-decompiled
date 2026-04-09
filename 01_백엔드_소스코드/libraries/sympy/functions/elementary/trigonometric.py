# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: trigonometric.pyc (Python 3.11)

from typing import Tuple as tTuple, Union as tUnion
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.expr import Expr
from sympy.core.function import Function, ArgumentIndexError, PoleError, expand_mul
from sympy.core.logic import fuzzy_not, fuzzy_or, FuzzyBool, fuzzy_and
from sympy.core.mod import Mod
from sympy.core.numbers import Rational, pi, Integer, Float, equal_valued
from sympy.core.relational import Ne, Eq
from sympy.core.singleton import S
from sympy.core.symbol import Symbol, Dummy
from sympy.core.sympify import sympify
from sympy.functions.combinatorial.factorials import factorial, RisingFactorial
from sympy.functions.combinatorial.numbers import bernoulli, euler
from sympy.functions.elementary.complexes import arg as arg_f, im, re
from sympy.functions.elementary.exponential import log, exp
from sympy.functions.elementary.integers import floor
from sympy.functions.elementary.miscellaneous import sqrt, Min, Max
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.elementary._trigonometric_special import cos_table, ipartfrac, fermat_coords
from sympy.logic.boolalg import And
from sympy.ntheory import factorint
from sympy.polys.specialpolys import symmetric_poly
from sympy.utilities.iterables import numbered_symbols

def _imaginary_unit_as_coefficient(arg):
    ''' Helper to extract symbolic coefficient for imaginary unit '''
    if isinstance(arg, Float):
        return None
    return None.as_coefficient(S.ImaginaryUnit)


class TrigonometricFunction(Function):
    '''Base class for trigonometric functions. '''
    unbranched = True
    _singularities = (S.ComplexInfinity,)
    
    def _eval_is_rational(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_is_algebraic(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_complex(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _as_real_imag(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _period(self, general_period, symbol = (None,)):
        f = expand_mul(self.args[0])
    # WARNING: Decompyle incomplete


_table2 = (lambda : {
12: (3, 4),
20: (4, 5),
30: (5, 6),
15: (6, 10),
24: (6, 8),
40: (8, 10),
60: (20, 30),
120: (40, 60) })()

def _peeloff_pi(arg):
    '''
    Split ARG into two parts, a "rest" and a multiple of $\\pi$.
    This assumes ARG to be an Add.
    The multiple of $\\pi$ returned in the second position is always a Rational.

    Examples
    ========

    >>> from sympy.functions.elementary.trigonometric import _peeloff_pi
    >>> from sympy import pi
    >>> from sympy.abc import x, y
    >>> _peeloff_pi(x + pi/2)
    (x, 1/2)
    >>> _peeloff_pi(x + 2*pi/3 + pi*y)
    (x + pi*y + pi/6, 1/2)

    '''
    pi_coeff = S.Zero
    rest_terms = []
# WARNING: Decompyle incomplete


def _pi_coeff(arg = None, cycles = None):
    '''
    When arg is a Number times $\\pi$ (e.g. $3\\pi/2$) then return the Number
    normalized to be in the range $[0, 2]$, else `None`.

    When an even multiple of $\\pi$ is encountered, if it is multiplying
    something with known parity then the multiple is returned as 0 otherwise
    as 2.

    Examples
    ========

    >>> from sympy.functions.elementary.trigonometric import _pi_coeff
    >>> from sympy import pi, Dummy
    >>> from sympy.abc import x
    >>> _pi_coeff(3*x*pi)
    3*x
    >>> _pi_coeff(11*pi/7)
    11/7
    >>> _pi_coeff(-11*pi/7)
    3/7
    >>> _pi_coeff(4*pi)
    0
    >>> _pi_coeff(5*pi)
    1
    >>> _pi_coeff(5.0*pi)
    1
    >>> _pi_coeff(5.5*pi)
    3/2
    >>> _pi_coeff(2 + pi)

    >>> _pi_coeff(2*Dummy(integer=True)*pi)
    2
    >>> _pi_coeff(2*Dummy(even=True)*pi)
    0

    '''
    if arg is pi:
        return S.One
    if not None:
        return S.Zero
# WARNING: Decompyle incomplete


class sin(TrigonometricFunction):
    '''
    The sine function.

    Returns the sine of x (measured in radians).

    Explanation
    ===========

    This function will evaluate automatically in the
    case $x/\\pi$ is some rational number [4]_.  For example,
    if $x$ is a multiple of $\\pi$, $\\pi/2$, $\\pi/3$, $\\pi/4$, and $\\pi/6$.

    Examples
    ========

    >>> from sympy import sin, pi
    >>> from sympy.abc import x
    >>> sin(x**2).diff(x)
    2*x*cos(x**2)
    >>> sin(1).diff(x)
    0
    >>> sin(pi)
    0
    >>> sin(pi/2)
    1
    >>> sin(pi/6)
    1/2
    >>> sin(pi/12)
    -sqrt(2)/4 + sqrt(6)/4


    See Also
    ========

    csc, cos, sec, tan, cot
    asin, acsc, acos, asec, atan, acot, atan2

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Trigonometric_functions
    .. [2] https://dlmf.nist.gov/4.14
    .. [3] https://functions.wolfram.com/ElementaryFunctions/Sin
    .. [4] https://mathworld.wolfram.com/TrigonometryAngles.html

    '''
    
    def period(self, symbol = (None,)):
        return self._period(2 * pi, symbol)

    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return cos(self.args[0])
        raise None(self, argindex)

    eval = (lambda cls, arg: AccumBounds = AccumBoundsimport sympy.calculus.accumulationboundsSetExpr = SetExprimport sympy.sets.setexpr# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n < 0 or n % 2 == 0:
S.Zerox = None(x)if len(previous_terms) > 2:
p = previous_terms[-2]-p * x ** 2 / (n * (n - 1))None.NegativeOne ** (n // 2) * x ** n / factorial(n))()()
    
    def _eval_nseries(self, x, n, logx, cdir = (0,)):
        arg = self.args[0]
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        HyperbolicFunction = HyperbolicFunction
        import sympy.functions.elementary.hyperbolic
        I = S.ImaginaryUnit
        if isinstance(arg, (TrigonometricFunction, HyperbolicFunction)):
            arg = arg.func(arg.args[0]).rewrite(exp)
        return (exp(arg * I) - exp(-arg * I)) / (2 * I)

    
    def _eval_rewrite_as_Pow(self, arg, **kwargs):
        if isinstance(arg, log):
            I = S.ImaginaryUnit
            x = arg.args[0]
            return I * x ** (-I) / 2 - I * x ** I / 2

    
    def _eval_rewrite_as_cos(self, arg, **kwargs):
        return cos(arg - pi / 2, evaluate = False)

    
    def _eval_rewrite_as_tan(self, arg, **kwargs):
        tan_half = tan(S.Half * arg)
        return 2 * tan_half / (1 + tan_half ** 2)

    
    def _eval_rewrite_as_sincos(self, arg, **kwargs):
        return sin(arg) * cos(arg) / cos(arg)

    
    def _eval_rewrite_as_cot(self, arg, **kwargs):
        cot_half = cot(S.Half * arg)
        return Piecewise((0, And(Eq(im(arg), 0), Eq(Mod(arg, pi), 0))), (2 * cot_half / (1 + cot_half ** 2), True))

    
    def _eval_rewrite_as_pow(self, arg, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_sqrt(self, arg, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_csc(self, arg, **kwargs):
        return 1 / csc(arg)

    
    def _eval_rewrite_as_sec(self, arg, **kwargs):
        return 1 / sec(arg - pi / 2, evaluate = False)

    
    def _eval_rewrite_as_sinc(self, arg, **kwargs):
        return arg * sinc(arg)

    
    def _eval_rewrite_as_besselj(self, arg, **kwargs):
        besselj = besselj
        import sympy.functions.special.bessel
        return sqrt(pi * arg / 2) * besselj(S.Half, arg)

    
    def _eval_conjugate(self):
        return self.func(self.args[0].conjugate())

    
    def as_real_imag(self, deep = (True,), **hints):
        cosh = cosh
        sinh = sinh
        import sympy.functions.elementary.hyperbolic
    # WARNING: Decompyle incomplete

    
    def _eval_expand_trig(self, **hints):
