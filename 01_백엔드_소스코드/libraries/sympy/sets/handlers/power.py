# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: power.pyc (Python 3.11)

from sympy.core import Basic, Expr
from sympy.core.function import Lambda
from sympy.core.numbers import oo, Infinity, NegativeInfinity, Zero, Integer
from sympy.core.singleton import S
from sympy.core.symbol import symbols
from sympy.functions.elementary.miscellaneous import Max, Min
from sympy.sets.fancysets import ImageSet
from sympy.sets.setexpr import set_div
from sympy.sets.sets import Set, Interval, FiniteSet, Union
from sympy.multipledispatch import Dispatcher
(_x, _y) = symbols('x y')
_set_pow = Dispatcher('_set_pow')
_ = (lambda x, y: pass)()
_ = (lambda x, y: ImageSet(Lambda((_x, _y), _x ** _y), x, y))()
_ = (lambda x, y: x ** y)()
_ = (lambda x, z: FiniteSet(S.One))()
_ = (lambda x, exponent: s1 = x.start ** exponents2 = x.end ** exponentif s2 > s1 if exponent > 0 else x.end > -(x.start) == True:
left_open = x.left_openright_open = x.right_opensleft = s2else:
left_open = x.right_openright_open = x.left_opensleft = s1if x.start.is_positive:
Interval(Min(s1, s2), Max(s1, s2), left_open, right_open)if None.end.is_negative:
Interval(Min(s1, s2), Max(s1, s2), left_open, right_open)if None.is_odd:
if exponent.is_negative:
if x.start.is_zero:
Interval(s2, oo, x.right_open)if None.end.is_zero:
Interval(-oo, s1, True, x.left_open)None(Interval(-oo, s1, True, x.left_open), Interval(s2, oo, x.right_open))None(s1, s2, x.left_open, x.right_open)if None.is_even:
if exponent.is_negative:
if x.start.is_zero:
Interval(s2, oo, x.right_open)if None.end.is_zero:
Interval(s1, oo, x.left_open)None(0, oo)None(S.Zero, sleft, S.Zero not in x, left_open))()
_ = (lambda b, e: if b.start.is_nonnegative:
if b.end < 1:
FiniteSet(S.Zero)if None.start > 1:
FiniteSet(S.Infinity)None(0, oo)if None.end.is_negative:
if b.start > -1:
FiniteSet(S.Zero)if None.end < -1:
FiniteSet(-oo, oo)None(-oo, oo)if None.start > -1:
if b.end < 1:
FiniteSet(S.Zero)None(0, oo)None(-oo, oo))()
_ = (lambda b, e: _set_pow(set_div(S.One, b), oo))()
