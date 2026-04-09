# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: integers.pyc (Python 3.11)

from typing import Tuple as tTuple
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core import Add, S
from sympy.core.evalf import get_integer_part, PrecisionExhausted
from sympy.core.function import Function
from sympy.core.logic import fuzzy_or
from sympy.core.numbers import Integer, int_valued
from sympy.core.relational import Gt, Lt, Ge, Le, Relational, is_eq
from sympy.core.sympify import _sympify
from sympy.functions.elementary.complexes import im, re
from sympy.multipledispatch import dispatch

class RoundFunction(Function):
    args: tTuple[Expr] = 'Abstract base class for rounding functions.'
    eval = (lambda cls, arg: v = cls._eval_number(arg)# WARNING: Decompyle incomplete
)()
    _eval_number = (lambda cls, arg: raise NotImplementedError())()
    
    def _eval_is_finite(self):
        return self.args[0].is_finite

    
    def _eval_is_real(self):
        return self.args[0].is_real

    
    def _eval_is_integer(self):
        return self.args[0].is_real



class floor(RoundFunction):
    '''
    Floor is a univariate function which returns the largest integer
    value not greater than its argument. This implementation
    generalizes floor to complex numbers by taking the floor of the
    real and imaginary parts separately.

    Examples
    ========

    >>> from sympy import floor, E, I, S, Float, Rational
    >>> floor(17)
    17
    >>> floor(Rational(23, 10))
    2
    >>> floor(2*E)
    5
    >>> floor(-Float(0.567))
    -1
    >>> floor(-I/2)
    -I
    >>> floor(S(5)/2 + 5*I/2)
    2 + 2*I

    See Also
    ========

    sympy.functions.elementary.integers.ceiling

    References
    ==========

    .. [1] "Concrete mathematics" by Graham, pp. 87
    .. [2] https://mathworld.wolfram.com/FloorFunction.html

    '''
    _dir = -1
    _eval_number = (lambda cls, arg: if arg.is_Number:
arg.floor()if (lambda .0: pass# WARNING: Decompyle incomplete
)((arg, -arg)()):
            return arg
        if None.is_NumberSymbol:
            return arg.approximation_interval(Integer)[0]
)()
    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        AccumBounds = AccumBounds
        import sympy.calculus.accumulationbounds
        arg = self.args[0]
        arg0 = arg.subs(x, 0)
        r = self.subs(x, 0)
        if arg0 is S.NaN or isinstance(arg0, AccumBounds):
            arg0 = arg.limit(x, 0, dir = '-' if re(cdir).is_negative else '+')
            r = floor(arg0)
        if arg0.is_finite:
            if arg0 == r:
                ndir = arg.dir(x, cdir = cdir if cdir != 0 else 1)
                if ndir.is_negative:
                    return r - 1
                if None.is_positive:
                    return r
                raise None('Not sure of sign of %s' % ndir)
            return r
        return None.as_leading_term(x, logx = logx, cdir = cdir)

    
    def _eval_nseries(self, x, n, logx, cdir = (0,)):
        arg = self.args[0]
        arg0 = arg.subs(x, 0)
        r = self.subs(x, 0)
        if arg0 is S.NaN:
            arg0 = arg.limit(x, 0, dir = '-' if re(cdir).is_negative else '+')
            r = floor(arg0)
        if arg0.is_infinite:
            AccumBounds = AccumBounds
            import sympy.calculus.accumulationbounds
            Order = Order
            import sympy.series.order
            s = arg._eval_nseries(x, n, logx, cdir)
            o = Order(1, (x, 0)) if n <= 0 else AccumBounds(-1, 0)
            return s + o
        if None == r:
            ndir = arg.dir(x, cdir = cdir if cdir != 0 else 1)
            if ndir.is_negative:
                return r - 1
            if None.is_positive:
                return r
            raise None('Not sure of sign of %s' % ndir)
        return r

    
    def _eval_is_negative(self):
        return self.args[0].is_negative

    
    def _eval_is_nonnegative(self):
        return self.args[0].is_nonnegative

    
    def _eval_rewrite_as_ceiling(self, arg, **kwargs):
        return -ceiling(-arg)

    
    def _eval_rewrite_as_frac(self, arg, **kwargs):
        return arg - frac(arg)

    
    def __le__(self, other):
