# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hyperbolic.pyc (Python 3.11)

from sympy.core import S, sympify, cacheit
from sympy.core.add import Add
from sympy.core.function import Function, ArgumentIndexError
from sympy.core.logic import fuzzy_or, fuzzy_and, fuzzy_not, FuzzyBool
from sympy.core.numbers import I, pi, Rational
from sympy.core.symbol import Dummy
from sympy.functions.combinatorial.factorials import binomial, factorial, RisingFactorial
from sympy.functions.combinatorial.numbers import bernoulli, euler, nC
from sympy.functions.elementary.complexes import Abs, im, re
from sympy.functions.elementary.exponential import exp, log, match_real_imag
from sympy.functions.elementary.integers import floor
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.trigonometric import acos, acot, asin, atan, cos, cot, csc, sec, sin, tan, _imaginary_unit_as_coefficient
from sympy.polys.specialpolys import symmetric_poly

def _rewrite_hyperbolics_as_exp(expr):
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(expr.atoms(HyperbolicFunction)())

_acosh_table = (lambda : pass# WARNING: Decompyle incomplete
)()
_acsch_table = (lambda : {
S(2): -I * log((1 + sqrt(5)) / 2),
I * (sqrt(6) - sqrt(2)): -5 * pi / 12,
I * sqrt(2 - 2 / sqrt(5)): -2 * pi / 5,
I * 2 / sqrt(2 + sqrt(2)): -3 * pi / 8,
I * 2 / sqrt(3): -pi / 3,
I * (sqrt(5) - 1): -3 * pi / 10,
I * sqrt(2): -pi / 4,
I * sqrt(2 + 2 / sqrt(5)): -pi / 5,
I * 2: -pi / 6,
I * 2 / sqrt(2 - sqrt(2)): -pi / 8,
I * (1 + sqrt(5)): -pi / 10,
I * (sqrt(2) + sqrt(6)): -pi / 12,
I: -pi / 2 })()
_asech_table = (lambda : pass# WARNING: Decompyle incomplete
)()

class HyperbolicFunction(Function):
    '''
    Base class for hyperbolic functions.

    See Also
    ========

    sinh, cosh, tanh, coth
    '''
    unbranched = True


def _peeloff_ipi(arg):
    '''
    Split ARG into two parts, a "rest" and a multiple of $I\\pi$.
    This assumes ARG to be an ``Add``.
    The multiple of $I\\pi$ returned in the second position is always a ``Rational``.

    Examples
    ========

    >>> from sympy.functions.elementary.hyperbolic import _peeloff_ipi as peel
    >>> from sympy import pi, I
    >>> from sympy.abc import x, y
    >>> peel(x + I*pi/2)
    (x, 1/2)
    >>> peel(x + I*2*pi/3 + I*pi*y)
    (x + I*pi*y + I*pi/6, 1/2)
    '''
    ipi = pi * I
    for a in Add.make_args(arg):
        if a == ipi:
            K = S.One
        elif a.is_Mul:
            (K, p) = a.as_two_terms()
            if p == ipi and K.is_Rational:
                pass
            
            return (arg, S.Zero)
            m1 = K % S.Half
            m2 = K - m1
            return (arg - m2 * ipi, m2)


class sinh(HyperbolicFunction):
    '''
    ``sinh(x)`` is the hyperbolic sine of ``x``.

    The hyperbolic sine function is $\\frac{e^x - e^{-x}}{2}$.

    Examples
    ========

    >>> from sympy import sinh
    >>> from sympy.abc import x
    >>> sinh(x)
    sinh(x)

    See Also
    ========

    cosh, tanh, asinh
    '''
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return cosh(self.args[0])
        raise None(self, argindex)

    
    def inverse(self, argindex = (1,)):
        '''
        Returns the inverse of this function.
        '''
        return asinh

    eval = (lambda cls, arg: if arg.is_Number:
if arg is S.NaN:
S.NaNif None is S.Infinity:
S.Infinityif None is S.NegativeInfinity:
S.NegativeInfinityif None.is_zero:
S.Zeroif None.is_negative:
-cls(-arg)Noneif None is S.ComplexInfinity:
S.NaNi_coeff = None(arg)# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n < 0 or n % 2 == 0:
S.Zerox = None(x)if len(previous_terms) > 2:
p = previous_terms[-2]p * x ** 2 / (n * (n - 1))None ** n / factorial(n))()()
    
    def _eval_conjugate(self):
        return self.func(self.args[0].conjugate())

    
    def as_real_imag(self, deep = (True,), **hints):
        '''
        Returns this function as a complex coordinate.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_complex(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_trig(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_tractable(self, arg, limitvar = (None,), **kwargs):
        return (exp(arg) - exp(-arg)) / 2

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        return (exp(arg) - exp(-arg)) / 2

    
    def _eval_rewrite_as_sin(self, arg, **kwargs):
        return -I * sin(I * arg)

    
    def _eval_rewrite_as_csc(self, arg, **kwargs):
        return -I / csc(I * arg)

    
    def _eval_rewrite_as_cosh(self, arg, **kwargs):
        return -I * cosh(arg + pi * I / 2)

    
    def _eval_rewrite_as_tanh(self, arg, **kwargs):
        tanh_half = tanh(S.Half * arg)
        return 2 * tanh_half / (1 - tanh_half ** 2)

    
    def _eval_rewrite_as_coth(self, arg, **kwargs):
        coth_half = coth(S.Half * arg)
        return 2 * coth_half / (coth_half ** 2 - 1)

    
    def _eval_rewrite_as_csch(self, arg, **kwargs):
        return 1 / csch(arg)

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        arg = self.args[0].as_leading_term(x, logx = logx, cdir = cdir)
        arg0 = arg.subs(x, 0)
        if arg0 is S.NaN:
            arg0 = arg.limit(x, 0, dir = '-' if cdir.is_negative else '+')
        if arg0.is_zero:
            return arg
        if None.is_finite:
            return self.func(arg0)

    
    def _eval_is_real(self):
        arg = self.args[0]
        if arg.is_real:
            return True
        (re, im) = None.as_real_imag()
        return (im % pi).is_zero

    
    def _eval_is_extended_real(self):
        if self.args[0].is_extended_real:
            return True

    
    def _eval_is_positive(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_positive

    
    def _eval_is_negative(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_negative

    
    def _eval_is_finite(self):
        arg = self.args[0]
        return arg.is_finite

    
    def _eval_is_zero(self):
        (rest, ipi_mult) = _peeloff_ipi(self.args[0])
        if rest.is_zero:
            return ipi_mult.is_integer



class cosh(HyperbolicFunction):
    '''
    ``cosh(x)`` is the hyperbolic cosine of ``x``.

    The hyperbolic cosine function is $\\frac{e^x + e^{-x}}{2}$.

    Examples
    ========

    >>> from sympy import cosh
    >>> from sympy.abc import x
    >>> cosh(x)
    cosh(x)

    See Also
    ========

    sinh, tanh, acosh
    '''
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return sinh(self.args[0])
        raise None(self, argindex)

    eval = (lambda cls, arg: cos = cosimport sympy.functions.elementary.trigonometricif arg.is_Number:
if arg is S.NaN:
S.NaNif None is S.Infinity:
S.Infinityif None is S.NegativeInfinity:
S.Infinityif None.is_zero:
S.Oneif None.is_negative:
cls(-arg)Noneif None is S.ComplexInfinity:
S.NaNi_coeff = None(arg)# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n < 0 or n % 2 == 1:
S.Zerox = None(x)if len(previous_terms) > 2:
p = previous_terms[-2]p * x ** 2 / (n * (n - 1))None ** n / factorial(n))()()
    
    def _eval_conjugate(self):
        return self.func(self.args[0].conjugate())

    
    def as_real_imag(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_complex(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_trig(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_tractable(self, arg, limitvar = (None,), **kwargs):
        return (exp(arg) + exp(-arg)) / 2

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        return (exp(arg) + exp(-arg)) / 2

    
    def _eval_rewrite_as_cos(self, arg, **kwargs):
        return cos(I * arg, evaluate = False)

    
    def _eval_rewrite_as_sec(self, arg, **kwargs):
        return 1 / sec(I * arg, evaluate = False)

    
    def _eval_rewrite_as_sinh(self, arg, **kwargs):
        return -I * sinh(arg + pi * I / 2, evaluate = False)

    
    def _eval_rewrite_as_tanh(self, arg, **kwargs):
        tanh_half = tanh(S.Half * arg) ** 2
        return (1 + tanh_half) / (1 - tanh_half)

    
    def _eval_rewrite_as_coth(self, arg, **kwargs):
        coth_half = coth(S.Half * arg) ** 2
        return (coth_half + 1) / (coth_half - 1)

    
    def _eval_rewrite_as_sech(self, arg, **kwargs):
        return 1 / sech(arg)

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        arg = self.args[0].as_leading_term(x, logx = logx, cdir = cdir)
        arg0 = arg.subs(x, 0)
        if arg0 is S.NaN:
            arg0 = arg.limit(x, 0, dir = '-' if cdir.is_negative else '+')
        if arg0.is_zero:
            return S.One
        if None.is_finite:
            return self.func(arg0)

    
    def _eval_is_real(self):
        arg = self.args[0]
        if arg.is_real or arg.is_imaginary:
            return True
        (re, im) = None.as_real_imag()
        return (im % pi).is_zero

    
    def _eval_is_positive(self):
        z = self.args[0]
        (x, y) = z.as_real_imag()
        ymod = y % 2 * pi
        yzero = ymod.is_zero
        if yzero:
            return True
        xzero = None.is_zero
        if xzero is False:
            return yzero
        return None([
            yzero,
            fuzzy_and([
                xzero,
                fuzzy_or([
                    ymod < pi / 2,
                    ymod > 3 * pi / 2])])])

    
    def _eval_is_nonnegative(self):
        z = self.args[0]
        (x, y) = z.as_real_imag()
        ymod = y % 2 * pi
        yzero = ymod.is_zero
        if yzero:
            return True
        xzero = None.is_zero
        if xzero is False:
            return yzero
        return None([
            yzero,
            fuzzy_and([
                xzero,
                fuzzy_or([
                    ymod <= pi / 2,
                    ymod >= 3 * pi / 2])])])

    
    def _eval_is_finite(self):
        arg = self.args[0]
        return arg.is_finite

    
    def _eval_is_zero(self):
        (rest, ipi_mult) = _peeloff_ipi(self.args[0])
        if ipi_mult or rest.is_zero:
            return (ipi_mult - S.Half).is_integer
        return None



class tanh(HyperbolicFunction):
    '''
    ``tanh(x)`` is the hyperbolic tangent of ``x``.

    The hyperbolic tangent function is $\\frac{\\sinh(x)}{\\cosh(x)}$.

    Examples
    ========

    >>> from sympy import tanh
    >>> from sympy.abc import x
    >>> tanh(x)
    tanh(x)

    See Also
    ========

    sinh, cosh, atanh
    '''
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return S.One - tanh(self.args[0]) ** 2
        raise None(self, argindex)

    
    def inverse(self, argindex = (1,)):
        '''
        Returns the inverse of this function.
        '''
        return atanh

    eval = (lambda cls, arg: if arg.is_Number:
if arg is S.NaN:
S.NaNif None is S.Infinity:
S.Oneif None is S.NegativeInfinity:
S.NegativeOneif None.is_zero:
S.Zeroif None.is_negative:
-cls(-arg)Noneif None is S.ComplexInfinity:
S.NaNi_coeff = None(arg)# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n < 0 or n % 2 == 0:
S.Zerox = None(x)a = 2 ** (n + 1)B = bernoulli(n + 1)F = factorial(n + 1)(a * (a - 1) * B / F) * x ** n)()()
    
    def _eval_conjugate(self):
        return self.func(self.args[0].conjugate())

    
    def as_real_imag(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_trig(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_tractable(self, arg, limitvar = (None,), **kwargs):
        pos_exp = exp(arg)
        neg_exp = exp(-arg)
        return (pos_exp - neg_exp) / (pos_exp + neg_exp)

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        pos_exp = exp(arg)
        neg_exp = exp(-arg)
        return (pos_exp - neg_exp) / (pos_exp + neg_exp)

    
    def _eval_rewrite_as_tan(self, arg, **kwargs):
        return -I * tan(I * arg, evaluate = False)

    
    def _eval_rewrite_as_cot(self, arg, **kwargs):
        return -I / cot(I * arg, evaluate = False)

    
    def _eval_rewrite_as_sinh(self, arg, **kwargs):
        return I * sinh(arg) / sinh(pi * I / 2 - arg, evaluate = False)

    
    def _eval_rewrite_as_cosh(self, arg, **kwargs):
        return I * cosh(pi * I / 2 - arg, evaluate = False) / cosh(arg)

    
    def _eval_rewrite_as_coth(self, arg, **kwargs):
        return 1 / coth(arg)

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        Order = Order
        import sympy.series.order
        arg = self.args[0].as_leading_term(x)
        if x in arg.free_symbols and Order(1, x).contains(arg):
            return arg
        return None.func(arg)

    
    def _eval_is_real(self):
        arg = self.args[0]
        if arg.is_real:
            return True
        (re, im) = None.as_real_imag()
        if re == 0 and im % pi == pi / 2:
            return None
        return (None % pi / 2).is_zero

    
    def _eval_is_extended_real(self):
        if self.args[0].is_extended_real:
            return True

    
    def _eval_is_positive(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_positive

    
    def _eval_is_negative(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_negative

    
    def _eval_is_finite(self):
        arg = self.args[0]
        (re, im) = arg.as_real_imag()
        denom = cos(im) ** 2 + sinh(re) ** 2
        if denom == 0:
            return False
        if None.is_number:
            return True
        if None.is_extended_real:
            return True

    
    def _eval_is_zero(self):
        arg = self.args[0]
        if arg.is_zero:
            return True



class coth(HyperbolicFunction):
    '''
    ``coth(x)`` is the hyperbolic cotangent of ``x``.

    The hyperbolic cotangent function is $\\frac{\\cosh(x)}{\\sinh(x)}$.

    Examples
    ========

    >>> from sympy import coth
    >>> from sympy.abc import x
    >>> coth(x)
    coth(x)

    See Also
    ========

    sinh, cosh, acoth
    '''
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return -1 / sinh(self.args[0]) ** 2
        raise None(self, argindex)

    
    def inverse(self, argindex = (1,)):
        '''
        Returns the inverse of this function.
        '''
        return acoth

    eval = (lambda cls, arg: if arg.is_Number:
if arg is S.NaN:
S.NaNif None is S.Infinity:
S.Oneif None is S.NegativeInfinity:
S.NegativeOneif None.is_zero:
S.ComplexInfinityif None.is_negative:
-cls(-arg)Noneif None is S.ComplexInfinity:
S.NaNi_coeff = None(arg)# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n == 0:
1 / sympify(x)if None < 0 or n % 2 == 0:
S.Zerox = None(x)B = bernoulli(n + 1)F = factorial(n + 1)(2 ** (n + 1) * B / F) * x ** n)()()
    
    def _eval_conjugate(self):
        return self.func(self.args[0].conjugate())

    
    def as_real_imag(self, deep = (True,), **hints):
        cos = cos
        sin = sin
        import sympy.functions.elementary.trigonometric
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_tractable(self, arg, limitvar = (None,), **kwargs):
        pos_exp = exp(arg)
        neg_exp = exp(-arg)
        return (pos_exp + neg_exp) / (pos_exp - neg_exp)

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        pos_exp = exp(arg)
        neg_exp = exp(-arg)
        return (pos_exp + neg_exp) / (pos_exp - neg_exp)

    
    def _eval_rewrite_as_sinh(self, arg, **kwargs):
        return -I * sinh(pi * I / 2 - arg, evaluate = False) / sinh(arg)

    
    def _eval_rewrite_as_cosh(self, arg, **kwargs):
        return -I * cosh(arg) / cosh(pi * I / 2 - arg, evaluate = False)

    
    def _eval_rewrite_as_tanh(self, arg, **kwargs):
        return 1 / tanh(arg)

    
    def _eval_is_positive(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_positive

    
    def _eval_is_negative(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_negative

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        Order = Order
        import sympy.series.order
        arg = self.args[0].as_leading_term(x)
        if x in arg.free_symbols and Order(1, x).contains(arg):
            return 1 / arg
        return None.func(arg)

    
    def _eval_expand_trig(self, **hints):
        arg = self.args[0]
    # WARNING: Decompyle incomplete



class ReciprocalHyperbolicFunction(HyperbolicFunction):
    '''Base class for reciprocal functions of hyperbolic functions. '''
    _reciprocal_of = None
    _is_even: FuzzyBool = None
    _is_odd: FuzzyBool = None
    eval = (lambda cls, arg: pass# WARNING: Decompyle incomplete
)()
    
    def _call_reciprocal(self, method_name, *args, **kwargs):
        o = self._reciprocal_of(self.args[0])
    # WARNING: Decompyle incomplete

    
    def _calculate_reciprocal(self, method_name, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _rewrite_reciprocal(self, method_name, arg):
        t = self._call_reciprocal(method_name, arg)
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        return self._rewrite_reciprocal('_eval_rewrite_as_exp', arg)

    
    def _eval_rewrite_as_tractable(self, arg, limitvar = (None,), **kwargs):
        return self._rewrite_reciprocal('_eval_rewrite_as_tractable', arg)

    
    def _eval_rewrite_as_tanh(self, arg, **kwargs):
        return self._rewrite_reciprocal('_eval_rewrite_as_tanh', arg)

    
    def _eval_rewrite_as_coth(self, arg, **kwargs):
        return self._rewrite_reciprocal('_eval_rewrite_as_coth', arg)

    
    def as_real_imag(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_conjugate(self):
        return self.func(self.args[0].conjugate())

    
    def _eval_expand_complex(self, deep = (True,), **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_trig(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        return (1 / self._reciprocal_of(self.args[0]))._eval_as_leading_term(x)

    
    def _eval_is_extended_real(self):
        return self._reciprocal_of(self.args[0]).is_extended_real

    
    def _eval_is_finite(self):
        return (1 / self._reciprocal_of(self.args[0])).is_finite



class csch(ReciprocalHyperbolicFunction):
    '''
    ``csch(x)`` is the hyperbolic cosecant of ``x``.

    The hyperbolic cosecant function is $\\frac{2}{e^x - e^{-x}}$

    Examples
    ========

    >>> from sympy import csch
    >>> from sympy.abc import x
    >>> csch(x)
    csch(x)

    See Also
    ========

    sinh, cosh, tanh, sech, asinh, acosh
    '''
    _reciprocal_of = sinh
    _is_odd = True
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function
        '''
        if argindex == 1:
            return -coth(self.args[0]) * csch(self.args[0])
        raise None(self, argindex)

    taylor_term = (lambda n, x: if n == 0:
1 / sympify(x)if None < 0 or n % 2 == 0:
S.Zerox = None(x)B = bernoulli(n + 1)F = factorial(n + 1)(2 * (1 - 2 ** n) * B / F) * x ** n)()()
    
    def _eval_rewrite_as_sin(self, arg, **kwargs):
        return I / sin(I * arg, evaluate = False)

    
    def _eval_rewrite_as_csc(self, arg, **kwargs):
        return I * csc(I * arg, evaluate = False)

    
    def _eval_rewrite_as_cosh(self, arg, **kwargs):
        return I / cosh(arg + I * pi / 2, evaluate = False)

    
    def _eval_rewrite_as_sinh(self, arg, **kwargs):
        return 1 / sinh(arg)

    
    def _eval_is_positive(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_positive

    
    def _eval_is_negative(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_negative



class sech(ReciprocalHyperbolicFunction):
    '''
    ``sech(x)`` is the hyperbolic secant of ``x``.

    The hyperbolic secant function is $\\frac{2}{e^x + e^{-x}}$

    Examples
    ========

    >>> from sympy import sech
    >>> from sympy.abc import x
    >>> sech(x)
    sech(x)

    See Also
    ========

    sinh, cosh, tanh, coth, csch, asinh, acosh
    '''
    _reciprocal_of = cosh
    _is_even = True
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return -tanh(self.args[0]) * sech(self.args[0])
        raise None(self, argindex)

    taylor_term = (lambda n, x: if n < 0 or n % 2 == 1:
S.Zerox = None(x)(euler(n) / factorial(n)) * x ** n)()()
    
    def _eval_rewrite_as_cos(self, arg, **kwargs):
        return 1 / cos(I * arg, evaluate = False)

    
    def _eval_rewrite_as_sec(self, arg, **kwargs):
        return sec(I * arg, evaluate = False)

    
    def _eval_rewrite_as_sinh(self, arg, **kwargs):
        return I / sinh(arg + I * pi / 2, evaluate = False)

    
    def _eval_rewrite_as_cosh(self, arg, **kwargs):
        return 1 / cosh(arg)

    
    def _eval_is_positive(self):
        if self.args[0].is_extended_real:
            return True



class InverseHyperbolicFunction(Function):
    '''Base class for inverse hyperbolic functions.'''
    pass


class asinh(InverseHyperbolicFunction):
    '''
    ``asinh(x)`` is the inverse hyperbolic sine of ``x``.

    The inverse hyperbolic sine function.

    Examples
    ========

    >>> from sympy import asinh
    >>> from sympy.abc import x
    >>> asinh(x).diff(x)
    1/sqrt(x**2 + 1)
    >>> asinh(1)
    log(1 + sqrt(2))

    See Also
    ========

    acosh, atanh, sinh
    '''
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            return 1 / sqrt(self.args[0] ** 2 + 1)
        raise None(self, argindex)

    eval = (lambda cls, arg: if arg.is_Number:
if arg is S.NaN:
S.NaNif None is S.Infinity:
S.Infinityif None is S.NegativeInfinity:
S.NegativeInfinityif None.is_zero:
S.Zeroif None is S.One:
log(sqrt(2) + 1)if None is S.NegativeOne:
log(sqrt(2) - 1)if None.is_negative:
-cls(-arg)if arg is S.ComplexInfinity:
S.ComplexInfinityif None.is_zero:
S.Zeroi_coeff = None(arg)# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n < 0 or n % 2 == 0:
S.Zerox = None(x)if len(previous_terms) >= 2 and n > 2:
p = previous_terms[-2](-p * (n - 2) ** 2 / (n * (n - 1))) * x ** 2k = (None - 1) // 2R = RisingFactorial(S.Half, k)F = factorial(k)(S.NegativeOne ** k * R / F) * x ** n / n)()()
    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        arg = self.args[0]
        x0 = arg.subs(x, 0).cancel()
        if x0.is_zero:
            return arg.as_leading_term(x)
        if None is S.NaN:
            expr = self.func(arg.as_leading_term(x))
            if expr.is_finite:
                return expr
            return None
        if None in (-I, I, S.ComplexInfinity):
            return self.rewrite(log)._eval_as_leading_term(x, logx = logx, cdir = cdir)
        if (None + x0 ** 2).is_negative:
            ndir = arg.dir(x, cdir if cdir else 1)
            if re(ndir).is_positive:
                if im(x0).is_negative:
                    return -self.func(x0) - I * pi
            if re(ndir).is_negative:
                if im(x0).is_positive:
                    return -self.func(x0) + I * pi
            return self.rewrite(log)._eval_as_leading_term(x, logx = logx, cdir = cdir)
        return None.func(x0)

    
    def _eval_nseries(self, x, n, logx, cdir = (0,)):
        arg = self.args[0]
        arg0 = arg.subs(x, 0)
        if arg0 in (I, -I):
            return self.rewrite(log)._eval_nseries(x, n, logx = logx, cdir = cdir)
        res = None._eval_nseries(self, x, n = n, logx = logx)
        if arg0 is S.ComplexInfinity:
            return res
        if (None + arg0 ** 2).is_negative:
            ndir = arg.dir(x, cdir if cdir else 1)
            if re(ndir).is_positive:
                if im(arg0).is_negative:
                    return -res - I * pi
            if re(ndir).is_negative:
                if im(arg0).is_positive:
                    return -res + I * pi
            return self.rewrite(log)._eval_nseries(x, n, logx = logx, cdir = cdir)

    
    def _eval_rewrite_as_log(self, x, **kwargs):
        return log(x + sqrt(x ** 2 + 1))

    _eval_rewrite_as_tractable = _eval_rewrite_as_log
    
    def _eval_rewrite_as_atanh(self, x, **kwargs):
        return atanh(x / sqrt(1 + x ** 2))

    
    def _eval_rewrite_as_acosh(self, x, **kwargs):
        ix = I * x
        return I * ((sqrt(1 - ix) / sqrt(ix - 1)) * acosh(ix) - pi / 2)

    
    def _eval_rewrite_as_asin(self, x, **kwargs):
        return -I * asin(I * x, evaluate = False)

    
    def _eval_rewrite_as_acos(self, x, **kwargs):
        return I * acos(I * x, evaluate = False) - I * pi / 2

    
    def inverse(self, argindex = (1,)):
        '''
        Returns the inverse of this function.
        '''
        return sinh

    
    def _eval_is_zero(self):
        return self.args[0].is_zero

    
    def _eval_is_extended_real(self):
        return self.args[0].is_extended_real

    
    def _eval_is_finite(self):
        return self.args[0].is_finite



class acosh(InverseHyperbolicFunction):
    '''
    ``acosh(x)`` is the inverse hyperbolic cosine of ``x``.

    The inverse hyperbolic cosine function.

    Examples
    ========

    >>> from sympy import acosh
    >>> from sympy.abc import x
    >>> acosh(x).diff(x)
    1/(sqrt(x - 1)*sqrt(x + 1))
    >>> acosh(1)
    0

    See Also
    ========

    asinh, atanh, cosh
    '''
    
    def fdiff(self, argindex = (1,)):
        if argindex == 1:
            arg = self.args[0]
            return 1 / (sqrt(arg - 1) * sqrt(arg + 1))
        raise None(self, argindex)

    eval = (lambda cls, arg: pass# WARNING: Decompyle incomplete
)()
    taylor_term = (lambda n, x: if n == 0:
I * pi / 2if None < 0 or n % 2 == 0:
S.Zerox = None(x)if len(previous_terms) >= 2 and n > 2:
p = previous_terms[-2](p * (n - 2) ** 2 / (n * (n - 1))) * x ** 2k = (None - 1) // 2R = RisingFactorial(S.Half, k)F = factorial(k)(-R / F) * I * x ** n / n)()()
    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
