# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mod.pyc (Python 3.11)

from add import Add
from exprtools import gcd_terms
from function import Function
from kind import NumberKind
from logic import fuzzy_and, fuzzy_not
from mul import Mul
from numbers import equal_valued
from singleton import S

class Mod(Function):
    """Represents a modulo operation on symbolic expressions.

    Parameters
    ==========

    p : Expr
        Dividend.

    q : Expr
        Divisor.

    Notes
    =====

    The convention used is the same as Python's: the remainder always has the
    same sign as the divisor.

    Many objects can be evaluated modulo ``n`` much faster than they can be
    evaluated directly (or at all).  For this, ``evaluate=False`` is
    necessary to prevent eager evaluation:

    >>> from sympy import binomial, factorial, Mod, Pow
    >>> Mod(Pow(2, 10**16, evaluate=False), 97)
    61
    >>> Mod(factorial(10**9, evaluate=False), 10**9 + 9)
    712524808
    >>> Mod(binomial(10**18, 10**12, evaluate=False), (10**5 + 3)**2)
    3744312326

    Examples
    ========

    >>> from sympy.abc import x, y
    >>> x**2 % y
    Mod(x**2, y)
    >>> _.subs({x: 5, y: 6})
    1

    """
    kind = NumberKind
    eval = (lambda cls, p, q: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_is_integer(self):
        (p, q) = self.args
        if fuzzy_and([
            p.is_integer,
            q.is_integer,
            fuzzy_not(q.is_zero)]):
            return True

    
    def _eval_is_nonnegative(self):
        if self.args[1].is_positive:
            return True

    
    def _eval_is_nonpositive(self):
        if self.args[1].is_negative:
            return True

    
    def _eval_rewrite_as_floor(self, a, b, **kwargs):
        floor = floor
        import sympy.functions.elementary.integers
        return a - b * floor(a / b)

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        floor = floor
        import sympy.functions.elementary.integers
        return self.rewrite(floor)._eval_as_leading_term(x, logx = logx, cdir = cdir)

    
    def _eval_nseries(self, x, n, logx, cdir = (0,)):
        floor = floor
        import sympy.functions.elementary.integers
        return self.rewrite(floor)._eval_nseries(x, n, logx = logx, cdir = cdir)
