# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: setexpr.pyc (Python 3.11)

from sympy.core import Expr
from sympy.core.decorators import call_highest_priority, _sympifyit
from fancysets import ImageSet
from sets import set_add, set_sub, set_mul, set_div, set_pow, set_function

class SetExpr(Expr):
    '''An expression that can take on values of a set.

    Examples
    ========

    >>> from sympy import Interval, FiniteSet
    >>> from sympy.sets.setexpr import SetExpr

    >>> a = SetExpr(Interval(0, 5))
    >>> b = SetExpr(FiniteSet(1, 10))
    >>> (a + b).set
    Union(Interval(1, 6), Interval(10, 15))
    >>> (2*a + b).set
    Interval(1, 20)
    '''
    _op_priority = 11
    
    def __new__(cls, setarg):
        return Expr.__new__(cls, setarg)

    set = property((lambda self: self.args[0]))
    
    def _latex(self, printer):
        return 'SetExpr\\left({}\\right)'.format(printer._print(self.set))

    __add__ = (lambda self, other: _setexpr_apply_operation(set_add, self, other))()()
    __radd__ = (lambda self, other: _setexpr_apply_operation(set_add, other, self))()()
    __mul__ = (lambda self, other: _setexpr_apply_operation(set_mul, self, other))()()
    __rmul__ = (lambda self, other: _setexpr_apply_operation(set_mul, other, self))()()
    __sub__ = (lambda self, other: _setexpr_apply_operation(set_sub, self, other))()()
    __rsub__ = (lambda self, other: _setexpr_apply_operation(set_sub, other, self))()()
    __pow__ = (lambda self, other: _setexpr_apply_operation(set_pow, self, other))()()
    __rpow__ = (lambda self, other: _setexpr_apply_operation(set_pow, other, self))()()
    __truediv__ = (lambda self, other: _setexpr_apply_operation(set_div, self, other))()()
    __rtruediv__ = (lambda self, other: _setexpr_apply_operation(set_div, other, self))()()
    
    def _eval_func(self, func):
        res = set_function(func, self.set)
    # WARNING: Decompyle incomplete



def _setexpr_apply_operation(op, x, y):
    if isinstance(x, SetExpr):
        x = x.set
    if isinstance(y, SetExpr):
        y = y.set
    out = op(x, y)
    return SetExpr(out)
