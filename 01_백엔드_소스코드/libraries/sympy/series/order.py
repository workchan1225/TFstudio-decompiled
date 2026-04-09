# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: order.pyc (Python 3.11)

from sympy.core import S, sympify, Expr, Dummy, Add, Mul
from sympy.core.cache import cacheit
from sympy.core.containers import Tuple
from sympy.core.function import Function, PoleError, expand_power_base, expand_log
from sympy.core.sorting import default_sort_key
from sympy.functions.elementary.exponential import exp, log
from sympy.sets.sets import Complement
from sympy.utilities.iterables import uniq, is_sequence

class Order(Expr):
    """ Represents the limiting behavior of some function.

    Explanation
    ===========

    The order of a function characterizes the function based on the limiting
    behavior of the function as it goes to some limit. Only taking the limit
    point to be a number is currently supported. This is expressed in
    big O notation [1]_.

    The formal definition for the order of a function `g(x)` about a point `a`
    is such that `g(x) = O(f(x))` as `x \\rightarrow a` if and only if there
    exists a `\\delta > 0` and an `M > 0` such that `|g(x)| \\leq M|f(x)|` for
    `|x-a| < \\delta`.  This is equivalent to `\\limsup_{x \\rightarrow a}
    |g(x)/f(x)| < \\infty`.

    Let's illustrate it on the following example by taking the expansion of
    `\\sin(x)` about 0:

    .. math ::
        \\sin(x) = x - x^3/3! + O(x^5)

    where in this case `O(x^5) = x^5/5! - x^7/7! + \\cdots`. By the definition
    of `O`, there is a `\\delta > 0` and an `M` such that:

    .. math ::
        |x^5/5! - x^7/7! + ....| <= M|x^5| \\text{ for } |x| < \\delta

    or by the alternate definition:

    .. math ::
        \\lim_{x \\rightarrow 0} | (x^5/5! - x^7/7! + ....) / x^5| < \\infty

    which surely is true, because

    .. math ::
        \\lim_{x \\rightarrow 0} | (x^5/5! - x^7/7! + ....) / x^5| = 1/5!


    As it is usually used, the order of a function can be intuitively thought
    of representing all terms of powers greater than the one specified. For
    example, `O(x^3)` corresponds to any terms proportional to `x^3,
    x^4,\\ldots` and any higher power. For a polynomial, this leaves terms
    proportional to `x^2`, `x` and constants.

    Examples
    ========

    >>> from sympy import O, oo, cos, pi
    >>> from sympy.abc import x, y

    >>> O(x + x**2)
    O(x)
    >>> O(x + x**2, (x, 0))
    O(x)
    >>> O(x + x**2, (x, oo))
    O(x**2, (x, oo))

    >>> O(1 + x*y)
    O(1, x, y)
    >>> O(1 + x*y, (x, 0), (y, 0))
    O(1, x, y)
    >>> O(1 + x*y, (x, oo), (y, oo))
    O(x*y, (x, oo), (y, oo))

    >>> O(1) in O(1, x)
    True
    >>> O(1, x) in O(1)
    False
    >>> O(x) in O(1, x)
    True
    >>> O(x**2) in O(x)
    True

    >>> O(x)*x
    O(x**2)
    >>> O(x) - O(x)
    O(x)
    >>> O(cos(x))
    O(1)
    >>> O(cos(x), (x, pi/2))
    O(x - pi/2, (x, pi/2))

    References
    ==========

    .. [1] `Big O notation <https://en.wikipedia.org/wiki/Big_O_notation>`_

    Notes
    =====

    In ``O(f(x), x)`` the expression ``f(x)`` is assumed to have a leading
    term.  ``O(f(x), x)`` is automatically transformed to
    ``O(f(x).as_leading_term(x),x)``.

        ``O(expr*f(x), x)`` is ``O(f(x), x)``

        ``O(expr, x)`` is ``O(1)``

        ``O(0, x)`` is 0.

    Multivariate O is also supported:

        ``O(f(x, y), x, y)`` is transformed to
        ``O(f(x, y).as_leading_term(x,y).as_leading_term(y), x, y)``

    In the multivariate case, it is assumed the limits w.r.t. the various
    symbols commute.

    If no symbols are passed then all symbols in the expression are used
    and the limit point is assumed to be zero.

    """
    is_Order = True
    __slots__ = ()
    __new__ = (lambda cls, expr: pass# WARNING: Decompyle incomplete
)()
    
    def _eval_nseries(self, x, n, logx, cdir = (0,)):
        return self

    expr = (lambda self: self.args[0])()
    variables = (lambda self: if self.args[1:]:
(lambda .0: pass# WARNING: Decompyle incomplete
)(self.args[1:]())
)()
    point = (lambda self: if self.args[1:]:
(lambda .0: pass# WARNING: Decompyle incomplete
)(self.args[1:]())
)()
    free_symbols = (lambda self: self.expr.free_symbols | set(self.variables))()
    
    def _eval_power(b, e):
        pass
    # WARNING: Decompyle incomplete

    
    def as_expr_variables(self, order_symbols):
        pass
    # WARNING: Decompyle incomplete

    
    def removeO(self):
        return S.Zero

    
    def getO(self):
        return self

    contains = (lambda self, expr: pass# WARNING: Decompyle incomplete
)()
    
    def __contains__(self, other):
        result = self.contains(other)
    # WARNING: Decompyle incomplete

    
    def _eval_subs(self, old, new):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_conjugate(self):
        expr = self.expr._eval_conjugate()
    # WARNING: Decompyle incomplete

    
    def _eval_derivative(self, x):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_transpose(self):
        expr = self.expr._eval_transpose()
    # WARNING: Decompyle incomplete

    
    def __neg__(self):
        return self


O = Order
