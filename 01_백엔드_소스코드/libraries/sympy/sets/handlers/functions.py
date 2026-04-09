# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

from sympy.core.singleton import S
from sympy.sets.sets import Set
from sympy.calculus.singularities import singularities
from sympy.core import Expr, Add
from sympy.core.function import Lambda, FunctionClass, diff, expand_mul
from sympy.core.numbers import Float, oo
from sympy.core.symbol import Dummy, symbols, Wild
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.miscellaneous import Min, Max
from sympy.logic.boolalg import true
from sympy.multipledispatch import Dispatcher
from sympy.sets import imageset, Interval, FiniteSet, Union, ImageSet, Intersection, Range, Complement
from sympy.sets.sets import EmptySet, is_function_invertible_in_set
from sympy.sets.fancysets import Integers, Naturals, Reals
from sympy.functions.elementary.exponential import match_real_imag
(_x, _y) = symbols('x y')
FunctionUnion = (FunctionClass, Lambda)
_set_function = Dispatcher('_set_function')
_ = (lambda f, x: pass)()
_ = (lambda f, x: pass# WARNING: Decompyle incomplete
)()
_ = (lambda f, x: pass# WARNING: Decompyle incomplete
)()
_ = (lambda f, x: if f == exp:
Interval(exp(x.start), exp(x.end), x.left_open, x.right_open)if None == log:
Interval(log(x.start), log(x.end), x.left_open, x.right_open)None(Lambda(_x, f(_x)), x))()
_ = (lambda f, x: pass# WARNING: Decompyle incomplete
)()
_ = (lambda f, x: pass# WARNING: Decompyle incomplete
)()
_ = (lambda f, x: x)()
_ = (lambda f, x: ImageSet(Lambda(_x, f(_x)), x))()
_ = (lambda f, self: if not self:
S.EmptySetif not None(f.expr, Expr):
Noneif None.size == 1:
FiniteSet(f(self[0]))if None is S.IdentityFunction:
selfx = None.variables[0]expr = f.exprif x not in expr.free_symbols or x in expr.diff(x).free_symbols:
Noneif None.start.is_finite:
F = f(self.step * x + self.start)else:
F = f(-(self.step) * x + self[-1])F = expand_mul(F)if F != expr:
imageset(x, F, Range(self.size)))()
_ = (lambda f, self: expr = f.exprif not isinstance(expr, Expr):
Nonen = None.variables[0]if expr == abs(n):
S.Naturals0c = f(0)fx = f(n) - cf_x = f(-n) - c
neg_count = lambda e: (lambda .0: pass# WARNING: Decompyle incomplete
)(Add.make_args(e)())
if neg_count(f_x) < neg_count(fx):
expr = f_x + ca = Wild('a', exclude = [
n])b = Wild('b', exclude = [
n])match = expr.match(a * n + b)# WARNING: Decompyle incomplete
)()
_ = (lambda f, self: expr = f.exprif not isinstance(expr, Expr):
Nonex = None.variables[0]if not expr.free_symbols - {
x}:
if expr == abs(x):
if self is S.Naturals:
selfNone.Naturals0step = None.coeff(x)c = expr.subs(x, 0)if c.is_Integer or step.is_Integer or expr == step * x + c:
if self is S.Naturals:
c += stepif step > 0:
if step == 1:
if c == 0:
S.Naturals0if None == 1:
S.NaturalsNone(c, oo, step)None(c, -oo, step)NoneNoneNone)()
_ = (lambda f, self: expr = f.exprif not isinstance(expr, Expr):
NoneNone(f, Interval(-oo, oo)))()
