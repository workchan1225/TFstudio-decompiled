# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cfunctions.pyc (Python 3.11)

'''
This module contains SymPy functions mathcin corresponding to special math functions in the
C standard library (since C99, also available in C++11).

The functions defined in this module allows the user to express functions such as ``expm1``
as a SymPy function for symbolic manipulation.

'''
from sympy.core.function import ArgumentIndexError, Function
from sympy.core.numbers import Rational
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.miscellaneous import sqrt

def _expm1(x):
    return exp(x) - S.One


class expm1(Function):
    """
    Represents the exponential function minus one.

    Explanation
    ===========

    The benefit of using ``expm1(x)`` over ``exp(x) - 1``
    is that the latter is prone to cancellation under finite precision
    arithmetic when x is close to zero.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import expm1
    >>> '%.0e' % expm1(1e-99).evalf()
    '1e-99'
    >>> from math import exp
    >>> exp(1e-99) - 1
    0.0
    >>> expm1(x).diff(x)
    exp(x)

    See Also
    ========

    log1p
    """
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_exp(self, arg, **kwargs):
        return exp(arg) - S.One

    _eval_rewrite_as_tractable = _eval_rewrite_as_exp
    eval = (lambda cls, arg: exp_arg = exp.eval(arg)# WARNING: Decompyle incomplete
)()
    
    def _eval_is_real(self):
        return self.args[0].is_real

    
    def _eval_is_finite(self):
        return self.args[0].is_finite



def _log1p(x):
    return log(x + S.One)


class log1p(Function):
    """
    Represents the natural logarithm of a number plus one.

    Explanation
    ===========

    The benefit of using ``log1p(x)`` over ``log(x + 1)``
    is that the latter is prone to cancellation under finite precision
    arithmetic when x is close to zero.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import log1p
    >>> from sympy import expand_log
    >>> '%.0e' % expand_log(log1p(1e-99)).evalf()
    '1e-99'
    >>> from math import log
    >>> log(1 + 1e-99)
    0.0
    >>> log1p(x).diff(x)
    1/(x + 1)

    See Also
    ========

    expm1
    """
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return S.One / (self.args[0] + S.One)
        raise None(self, argindex)

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_log(self, arg, **kwargs):
        return _log1p(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_log
    eval = (lambda cls, arg: if arg.is_Rational:
log(arg + S.One)if not None.is_Float:
log.eval(arg + S.One)if None.is_number:
log(Rational(arg) + S.One))()
    
    def _eval_is_real(self):
        return (self.args[0] + S.One).is_nonnegative

    
    def _eval_is_finite(self):
        if (self.args[0] + S.One).is_zero:
            return False
        return None.args[0].is_finite

    
    def _eval_is_positive(self):
        return self.args[0].is_positive

    
    def _eval_is_zero(self):
        return self.args[0].is_zero

    
    def _eval_is_nonnegative(self):
        return self.args[0].is_nonnegative


_Two = S(2)

def _exp2(x):
    return Pow(_Two, x)


class exp2(Function):
    '''
    Represents the exponential function with base two.

    Explanation
    ===========

    The benefit of using ``exp2(x)`` over ``2**x``
    is that the latter is not as efficient under finite precision
    arithmetic.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import exp2
    >>> exp2(2).evalf() == 4.0
    True
    >>> exp2(x).diff(x)
    log(2)*exp2(x)

    See Also
    ========

    log2
    '''
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return self * log(_Two)
        raise None(self, argindex)

    
    def _eval_rewrite_as_Pow(self, arg, **kwargs):
        return _exp2(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_Pow
    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    eval = (lambda cls, arg: if arg.is_number:
_exp2(arg))()


def _log2(x):
    return log(x) / log(_Two)


class log2(Function):
    '''
    Represents the logarithm function with base two.

    Explanation
    ===========

    The benefit of using ``log2(x)`` over ``log(x)/log(2)``
    is that the latter is not as efficient under finite precision
    arithmetic.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import log2
    >>> log2(4).evalf() == 2.0
    True
    >>> log2(x).diff(x)
    1/(x*log(2))

    See Also
    ========

    exp2
    log10
    '''
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return S.One / (log(_Two) * self.args[0])
        raise None(self, argindex)

    eval = (lambda cls, arg: if arg.is_number:
result = log.eval(arg, base = _Two)if result.is_Atom:
resultNoneif None.is_Pow or arg.base == _Two:
arg.expNone)()
    
    def _eval_evalf(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_log(self, arg, **kwargs):
        return _log2(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_log


def _fma(x, y, z):
    return x * y + z


class fma(Function):
    '''
    Represents "fused multiply add".

    Explanation
    ===========

    The benefit of using ``fma(x, y, z)`` over ``x*y + z``
    is that, under finite precision arithmetic, the former is
    supported by special instructions on some CPUs.

    Examples
    ========

    >>> from sympy.abc import x, y, z
    >>> from sympy.codegen.cfunctions import fma
    >>> fma(x, y, z).diff(x)
    y

    '''
    nargs = 3
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex in (1, 2):
            return self.args[2 - argindex]
        if None == 3:
            return S.One
        raise None(self, argindex)

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_tractable(self, arg, limitvar = (None,), **kwargs):
        return _fma(arg)


_Ten = S(10)

def _log10(x):
    return log(x) / log(_Ten)


class log10(Function):
    '''
    Represents the logarithm function with base ten.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import log10
    >>> log10(100).evalf() == 2.0
    True
    >>> log10(x).diff(x)
    1/(x*log(10))

    See Also
    ========

    log2
    '''
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return S.One / (log(_Ten) * self.args[0])
        raise None(self, argindex)

    eval = (lambda cls, arg: if arg.is_number:
result = log.eval(arg, base = _Ten)if result.is_Atom:
resultNoneif None.is_Pow or arg.base == _Ten:
arg.expNone)()
    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_log(self, arg, **kwargs):
        return _log10(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_log


def _Sqrt(x):
    return Pow(x, S.Half)


class Sqrt(Function):
    '''
    Represents the square root function.

    Explanation
    ===========

    The reason why one would use ``Sqrt(x)`` over ``sqrt(x)``
    is that the latter is internally represented as ``Pow(x, S.Half)`` which
    may not be what one wants when doing code-generation.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import Sqrt
    >>> Sqrt(x)
    Sqrt(x)
    >>> Sqrt(x).diff(x)
    1/(2*sqrt(x))

    See Also
    ========

    Cbrt
    '''
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return Pow(self.args[0], Rational(-1, 2)) / _Two
        raise None(self, argindex)

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Pow(self, arg, **kwargs):
        return _Sqrt(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_Pow


def _Cbrt(x):
    return Pow(x, Rational(1, 3))


class Cbrt(Function):
    '''
    Represents the cube root function.

    Explanation
    ===========

    The reason why one would use ``Cbrt(x)`` over ``cbrt(x)``
    is that the latter is internally represented as ``Pow(x, Rational(1, 3))`` which
    may not be what one wants when doing code-generation.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy.codegen.cfunctions import Cbrt
    >>> Cbrt(x)
    Cbrt(x)
    >>> Cbrt(x).diff(x)
    1/(3*x**(2/3))

    See Also
    ========

    Sqrt
    '''
    nargs = 1
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        if argindex == 1:
            return Pow(self.args[0], Rational(-_Two / 3)) / 3
        raise None(self, argindex)

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Pow(self, arg, **kwargs):
        return _Cbrt(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_Pow


def _hypot(x, y):
    return sqrt(Pow(x, 2) + Pow(y, 2))


class hypot(Function):
    '''
    Represents the hypotenuse function.

    Explanation
    ===========

    The hypotenuse function is provided by e.g. the math library
    in the C99 standard, hence one may want to represent the function
    symbolically when doing code-generation.

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> from sympy.codegen.cfunctions import hypot
    >>> hypot(3, 4).evalf() == 5.0
    True
    >>> hypot(x, y)
    hypot(x, y)
    >>> hypot(x, y).diff(x)
    x/hypot(x, y)

    '''
    nargs = 2
    
    def fdiff(self, argindex = (1,)):
        '''
        Returns the first derivative of this function.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_func(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_Pow(self, arg, **kwargs):
        return _hypot(arg)

    _eval_rewrite_as_tractable = _eval_rewrite_as_Pow


class isnan(Function):
    nargs = 1
