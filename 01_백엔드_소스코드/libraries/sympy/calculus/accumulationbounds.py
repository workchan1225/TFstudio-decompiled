# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: accumulationbounds.pyc (Python 3.11)

from sympy.core import Add, Mul, Pow, S
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.numbers import _sympifyit, oo, zoo
from sympy.core.relational import is_le, is_lt, is_ge, is_gt
from sympy.core.sympify import _sympify
from sympy.functions.elementary.miscellaneous import Min, Max
from sympy.logic.boolalg import And
from sympy.multipledispatch import dispatch
from sympy.series.order import Order
from sympy.sets.sets import FiniteSet

class AccumulationBounds(Expr):
    '''An accumulation bounds.

    # Note AccumulationBounds has an alias: AccumBounds

    AccumulationBounds represent an interval `[a, b]`, which is always closed
    at the ends. Here `a` and `b` can be any value from extended real numbers.

    The intended meaning of AccummulationBounds is to give an approximate
    location of the accumulation points of a real function at a limit point.

    Let `a` and `b` be reals such that `a \\le b`.

    `\\left\\langle a, b\\right\\rangle = \\{x \\in \\mathbb{R} \\mid a \\le x \\le b\\}`

    `\\left\\langle -\\infty, b\\right\\rangle = \\{x \\in \\mathbb{R} \\mid x \\le b\\} \\cup \\{-\\infty, \\infty\\}`

    `\\left\\langle a, \\infty \\right\\rangle = \\{x \\in \\mathbb{R} \\mid a \\le x\\} \\cup \\{-\\infty, \\infty\\}`

    `\\left\\langle -\\infty, \\infty \\right\\rangle = \\mathbb{R} \\cup \\{-\\infty, \\infty\\}`

    ``oo`` and ``-oo`` are added to the second and third definition respectively,
    since if either ``-oo`` or ``oo`` is an argument, then the other one should
    be included (though not as an end point). This is forced, since we have,
    for example, ``1/AccumBounds(0, 1) = AccumBounds(1, oo)``, and the limit at
    `0` is not one-sided. As `x` tends to `0-`, then `1/x \\rightarrow -\\infty`, so `-\\infty`
    should be interpreted as belonging to ``AccumBounds(1, oo)`` though it need
    not appear explicitly.

    In many cases it suffices to know that the limit set is bounded.
    However, in some other cases more exact information could be useful.
    For example, all accumulation values of `\\cos(x) + 1` are non-negative.
    (``AccumBounds(-1, 1) + 1 = AccumBounds(0, 2)``)

    A AccumulationBounds object is defined to be real AccumulationBounds,
    if its end points are finite reals.

    Let `X`, `Y` be real AccumulationBounds, then their sum, difference,
    product are defined to be the following sets:

    `X + Y = \\{ x+y \\mid x \\in X \\cap y \\in Y\\}`

    `X - Y = \\{ x-y \\mid x \\in X \\cap y \\in Y\\}`

    `X \\times Y = \\{ x \\times y \\mid x \\in X \\cap y \\in Y\\}`

    When an AccumBounds is raised to a negative power, if 0 is contained
    between the bounds then an infinite range is returned, otherwise if an
    endpoint is 0 then a semi-infinite range with consistent sign will be returned.

    AccumBounds in expressions behave a lot like Intervals but the
    semantics are not necessarily the same. Division (or exponentiation
    to a negative integer power) could be handled with *intervals* by
    returning a union of the results obtained after splitting the
    bounds between negatives and positives, but that is not done with
    AccumBounds. In addition, bounds are assumed to be independent of
    each other; if the same bound is used in more than one place in an
    expression, the result may not be the supremum or infimum of the
    expression (see below). Finally, when a boundary is ``1``,
    exponentiation to the power of ``oo`` yields ``oo``, neither
    ``1`` nor ``nan``.

    Examples
    ========

    >>> from sympy import AccumBounds, sin, exp, log, pi, E, S, oo
    >>> from sympy.abc import x

    >>> AccumBounds(0, 1) + AccumBounds(1, 2)
    AccumBounds(1, 3)

    >>> AccumBounds(0, 1) - AccumBounds(0, 2)
    AccumBounds(-2, 1)

    >>> AccumBounds(-2, 3)*AccumBounds(-1, 1)
    AccumBounds(-3, 3)

    >>> AccumBounds(1, 2)*AccumBounds(3, 5)
    AccumBounds(3, 10)

    The exponentiation of AccumulationBounds is defined
    as follows:

    If 0 does not belong to `X` or `n > 0` then

    `X^n = \\{ x^n \\mid x \\in X\\}`

    >>> AccumBounds(1, 4)**(S(1)/2)
    AccumBounds(1, 2)

    otherwise, an infinite or semi-infinite result is obtained:

    >>> 1/AccumBounds(-1, 1)
    AccumBounds(-oo, oo)
    >>> 1/AccumBounds(0, 2)
    AccumBounds(1/2, oo)
    >>> 1/AccumBounds(-oo, 0)
    AccumBounds(-oo, 0)

    A boundary of 1 will always generate all nonnegatives:

    >>> AccumBounds(1, 2)**oo
    AccumBounds(0, oo)
    >>> AccumBounds(0, 1)**oo
    AccumBounds(0, oo)

    If the exponent is itself an AccumulationBounds or is not an
    integer then unevaluated results will be returned unless the base
    values are positive:

    >>> AccumBounds(2, 3)**AccumBounds(-1, 2)
    AccumBounds(1/3, 9)
    >>> AccumBounds(-2, 3)**AccumBounds(-1, 2)
    AccumBounds(-2, 3)**AccumBounds(-1, 2)

    >>> AccumBounds(-2, -1)**(S(1)/2)
    sqrt(AccumBounds(-2, -1))

    Note: `\\left\\langle a, b\\right\\rangle^2` is not same as `\\left\\langle a, b\\right\\rangle \\times \\left\\langle a, b\\right\\rangle`

    >>> AccumBounds(-1, 1)**2
    AccumBounds(0, 1)

    >>> AccumBounds(1, 3) < 4
    True

    >>> AccumBounds(1, 3) < -1
    False

    Some elementary functions can also take AccumulationBounds as input.
    A function `f` evaluated for some real AccumulationBounds `\\left\\langle a, b \\right\\rangle`
    is defined as `f(\\left\\langle a, b\\right\\rangle) = \\{ f(x) \\mid a \\le x \\le b \\}`

    >>> sin(AccumBounds(pi/6, pi/3))
    AccumBounds(1/2, sqrt(3)/2)

    >>> exp(AccumBounds(0, 1))
    AccumBounds(1, E)

    >>> log(AccumBounds(1, E))
    AccumBounds(0, 1)

    Some symbol in an expression can be substituted for a AccumulationBounds
    object. But it does not necessarily evaluate the AccumulationBounds for
    that expression.

    The same expression can be evaluated to different values depending upon
    the form it is used for substitution since each instance of an
    AccumulationBounds is considered independent. For example:

    >>> (x**2 + 2*x + 1).subs(x, AccumBounds(-1, 1))
    AccumBounds(-1, 4)

    >>> ((x + 1)**2).subs(x, AccumBounds(-1, 1))
    AccumBounds(0, 4)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Interval_arithmetic

    .. [2] https://fab.cba.mit.edu/classes/S62.12/docs/Hickey_interval.pdf

    Notes
    =====

    Do not use ``AccumulationBounds`` for floating point interval arithmetic
    calculations, use ``mpmath.iv`` instead.
    '''
    is_extended_real = True
    is_number = False
    
    def __new__(cls, min, max):
        min = _sympify(min)
        max = _sympify(max)
        if not min.is_extended_real or max.is_extended_real:
            raise ValueError('Only real AccumulationBounds are supported')
        if max == min:
            return max
        if None.is_number and min.is_number:
            if max.is_comparable:
                pass
        if bad:
            raise ValueError('Lower limit should be smaller than upper limit')
        return Basic.__new__(cls, min, max)

    _op_priority = 11
    
    def _eval_is_real(self):
        if self.min.is_real or self.max.is_real:
            return True
        return None

    min = (lambda self: self.args[0])()
    max = (lambda self: self.args[1])()
    delta = (lambda self: self.max - self.min)()
    mid = (lambda self: (self.min + self.max) / 2)()
    _eval_power = (lambda self, other: self.__pow__(other))()
    __add__ = (lambda self, other: if isinstance(other, Expr):
if isinstance(other, AccumBounds):
AccumBounds(Add(self.min, other.min), Add(self.max, other.max))if (None is S.Infinity or self.min is S.NegativeInfinity or other is S.NegativeInfinity) and self.max is S.Infinity:
AccumBounds(-oo, oo)if None.is_extended_real:
if self.min is S.NegativeInfinity and self.max is S.Infinity:
AccumBounds(-oo, oo)if None.min is S.NegativeInfinity:
AccumBounds(-oo, self.max + other)if None.max is S.Infinity:
AccumBounds(self.min + other, oo)None(Add(self.min, other), Add(self.max, other))None(self, other, evaluate = False))()
    __radd__ = __add__
    
    def __neg__(self):
        return AccumBounds(-(self.max), -(self.min))

    __sub__ = (lambda self, other: if isinstance(other, Expr):
if isinstance(other, AccumBounds):
AccumBounds(Add(self.min, -(other.max)), Add(self.max, -(other.min)))if (None is S.NegativeInfinity or self.min is S.NegativeInfinity or other is S.Infinity) and self.max is S.Infinity:
AccumBounds(-oo, oo)if None.is_extended_real:
if self.min is S.NegativeInfinity and self.max is S.Infinity:
AccumBounds(-oo, oo)if None.min is S.NegativeInfinity:
AccumBounds(-oo, self.max - other)if None.max is S.Infinity:
AccumBounds(self.min - other, oo)None(Add(self.min, -other), Add(self.max, -other))None(self, -other, evaluate = False))()
    __rsub__ = (lambda self, other: self.__neg__() + other)()
    __mul__ = (lambda self, other: if self.args == (-oo, oo):
self# WARNING: Decompyle incomplete
)()
    __rmul__ = __mul__
    __truediv__ = (lambda self, other:
