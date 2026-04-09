# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: complexes.pyc (Python 3.11)

from typing import Tuple as tTuple
from sympy.core import S, Add, Mul, sympify, Symbol, Dummy, Basic
from sympy.core.expr import Expr
from sympy.core.exprtools import factor_terms
from sympy.core.function import Function, Derivative, ArgumentIndexError, AppliedUndef, expand_mul
from sympy.core.logic import fuzzy_not, fuzzy_or
from sympy.core.numbers import pi, I, oo
from sympy.core.power import Pow
from sympy.core.relational import Eq
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.piecewise import Piecewise

class re(Function):
    args: tTuple[Expr] = "\n    Returns real part of expression. This function performs only\n    elementary analysis and so it will fail to decompose properly\n    more complicated expressions. If completely simplified result\n    is needed then use ``Basic.as_real_imag()`` or perform complex\n    expansion on instance of this function.\n\n    Examples\n    ========\n\n    >>> from sympy import re, im, I, E, symbols\n    >>> x, y = symbols('x y', real=True)\n    >>> re(2*E)\n    2*E\n    >>> re(2*I + 17)\n    17\n    >>> re(2*I)\n    0\n    >>> re(im(x) + x*I + 2)\n    2\n    >>> re(5 + I + 2)\n    7\n\n    Parameters\n    ==========\n\n    arg : Expr\n        Real or complex expression.\n\n    Returns\n    =======\n\n    expr : Expr\n        Real part of expression.\n\n    See Also\n    ========\n\n    im\n    "
    is_extended_real = True
    unbranched = True
    _singularities = True
    eval = (lambda cls, arg: if arg is S.NaN:
S.NaNif None is S.ComplexInfinity:
S.NaNif None.is_extended_real:
argif None.is_imaginary or (I * arg).is_extended_real:
S.Zeroif None.is_Matrix:
arg.as_real_imag()[0]if None.is_Function and isinstance(arg, conjugate):
re(arg.args[0])excluded = []reverted = []included = Noneargs = Add.make_args(arg)# WARNING: Decompyle incomplete
)()
    
    def as_real_imag(self, deep = (True,), **hints):
        '''
        Returns the real number with a zero imaginary part.

        '''
        return (self, S.Zero)

    
    def _eval_derivative(self, x):
        if x.is_extended_real or self.args[0].is_extended_real:
            return re(Derivative(self.args[0], x, evaluate = True))
        if None.is_imaginary or self.args[0].is_imaginary:
            return -I * im(Derivative(self.args[0], x, evaluate = True))

    
    def _eval_rewrite_as_im(self, arg, **kwargs):
        return self.args[0] - I * im(self.args[0])

    
    def _eval_is_algebraic(self):
        return self.args[0].is_algebraic

    
    def _eval_is_zero(self):
        return fuzzy_or([
            self.args[0].is_imaginary,
            self.args[0].is_zero])

    
    def _eval_is_finite(self):
        if self.args[0].is_finite:
            return True

    
    def _eval_is_complex(self):
        if self.args[0].is_finite:
            return True



class im(Function):
    args: tTuple[Expr] = '\n    Returns imaginary part of expression. This function performs only\n    elementary analysis and so it will fail to decompose properly more\n    complicated expressions. If completely simplified result is needed then\n    use ``Basic.as_real_imag()`` or perform complex expansion on instance of\n    this function.\n\n    Examples\n    ========\n\n    >>> from sympy import re, im, E, I\n    >>> from sympy.abc import x, y\n    >>> im(2*E)\n    0\n    >>> im(2*I + 17)\n    2\n    >>> im(x*I)\n    re(x)\n    >>> im(re(x) + y)\n    im(y)\n    >>> im(2 + 3*I)\n    3\n\n    Parameters\n    ==========\n\n    arg : Expr\n        Real or complex expression.\n\n    Returns\n    =======\n\n    expr : Expr\n        Imaginary part of expression.\n\n    See Also\n    ========\n\n    re\n    '
    is_extended_real = True
    unbranched = True
    _singularities = True
    eval = (lambda cls, arg: if arg is S.NaN:
S.NaNif None is S.ComplexInfinity:
S.NaNif None.is_extended_real:
S.Zeroif None.is_imaginary or (I * arg).is_extended_real:
-I * argif None.is_Matrix:
arg.as_real_imag()[1]if None.is_Function and isinstance(arg, conjugate):
-im(arg.args[0])excluded = []reverted = []included = Noneargs = Add.make_args(arg)# WARNING: Decompyle incomplete
)()
    
    def as_real_imag(self, deep = (True,), **hints):
        '''
        Return the imaginary part with a zero real part.

        '''
        return (self, S.Zero)

    
    def _eval_derivative(self, x):
        if x.is_extended_real or self.args[0].is_extended_real:
            return im(Derivative(self.args[0], x, evaluate = True))
        if None.is_imaginary or self.args[0].is_imaginary:
            return -I * re(Derivative(self.args[0], x, evaluate = True))

    
    def _eval_rewrite_as_re(self, arg, **kwargs):
        return -I * (self.args[0] - re(self.args[0]))

    
    def _eval_is_algebraic(self):
        return self.args[0].is_algebraic

    
    def _eval_is_zero(self):
        return self.args[0].is_extended_real

    
    def _eval_is_finite(self):
        if self.args[0].is_finite:
            return True

    
    def _eval_is_complex(self):
        if self.args[0].is_finite:
            return True



class sign(Function):
    pass
# WARNING: Decompyle incomplete


class Abs(Function):
    args: tTuple[Expr] = "\n    Return the absolute value of the argument.\n\n    Explanation\n    ===========\n\n    This is an extension of the built-in function ``abs()`` to accept symbolic\n    values.  If you pass a SymPy expression to the built-in ``abs()``, it will\n    pass it automatically to ``Abs()``.\n\n    Examples\n    ========\n\n    >>> from sympy import Abs, Symbol, S, I\n    >>> Abs(-1)\n    1\n    >>> x = Symbol('x', real=True)\n    >>> Abs(-x)\n    Abs(x)\n    >>> Abs(x**2)\n    x**2\n    >>> abs(-x) # The Python built-in\n    Abs(x)\n    >>> Abs(3*x + 2*I)\n    sqrt(9*x**2 + 4)\n    >>> Abs(8*I)\n    8\n\n    Note that the Python built-in will return either an Expr or int depending on\n    the argument::\n\n        >>> type(abs(-1))\n        <... 'int'>\n        >>> type(abs(S.NegativeOne))\n        <class 'sympy.core.numbers.One'>\n\n    Abs will always return a SymPy object.\n\n    Parameters\n    ==========\n\n    arg : Expr\n        Real or complex expression.\n\n    Returns\n    =======\n\n    expr : Expr\n        Absolute value returned can be an expression or integer depending on\n        input arg.\n\n    See Also\n    ========\n\n    sign, conjugate\n    "
    is_extended_real = True
    is_extended_negative = False
    is_extended_nonnegative = True
    unbranched = True
    _singularities = True
    
    def fdiff(self, argindex = (1,)):
        '''
        Get the first derivative of the argument to Abs().

        '''
        if argindex == 1:
            return sign(self.args[0])
        raise None(self, argindex)

    eval = (lambda cls, arg: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_is_real(self):
        if self.args[0].is_finite:
            return True

    
    def _eval_is_integer(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_integer

    
    def _eval_is_extended_nonzero(self):
        return fuzzy_not(self._args[0].is_zero)

    
    def _eval_is_zero(self):
        return self._args[0].is_zero

    
    def _eval_is_extended_positive(self):
        return fuzzy_not(self._args[0].is_zero)

    
    def _eval_is_rational(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_rational

    
    def _eval_is_even(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_even

    
    def _eval_is_odd(self):
        if self.args[0].is_extended_real:
            return self.args[0].is_odd

    
    def _eval_is_algebraic(self):
        return self.args[0].is_algebraic

    
    def _eval_power(self, exponent):
