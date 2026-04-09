# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: order.pyc (Python 3.11)

'''
Handlers related to order relations: positive, negative, etc.
'''
from sympy.assumptions import Q, ask
from sympy.core import Add, Basic, Expr, Mul, Pow
from sympy.core.logic import fuzzy_not, fuzzy_and, fuzzy_or
from sympy.core.numbers import E, ImaginaryUnit, NaN, I, pi
from sympy.functions import Abs, acos, acot, asin, atan, exp, factorial, log
from sympy.matrices import Determinant, Trace
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.multipledispatch import MDNotImplementedError
from predicates.order import NegativePredicate, NonNegativePredicate, NonZeroPredicate, ZeroPredicate, NonPositivePredicate, PositivePredicate, ExtendedNegativePredicate, ExtendedNonNegativePredicate, ExtendedNonPositivePredicate, ExtendedNonZeroPredicate, ExtendedPositivePredicate

def _NegativePredicate_number(expr, assumptions):
    (r, i) = expr.as_real_imag()
    if not i:
        r = r.evalf(2)
        if r._prec != 1:
            return r < 0
        return None
    i = None.evalf(2)
    if i._prec != 1:
        if i != 0:
            return False
        r = None.evalf(2)
        if r._prec != 1:
            return r < 0
        return None

_ = (lambda expr, assumptions: if expr.is_number:
_NegativePredicate_number(expr, assumptions))()
_ = (lambda expr, assumptions: ret = expr.is_negative# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
_NegativePredicate_number(expr, assumptions)r = None(Q.real(expr), assumptions)if r is not True:
rnonpos = Nonefor arg in expr.args:
if ask(Q.negative(arg), assumptions) is not True:
if ask(Q.positive(arg), assumptions) is False:
nonpos += 1continueNoneif nonpos < len(expr.args):
TrueNone)()
_ = (lambda expr, assumptions: if expr.is_number:
_NegativePredicate_number(expr, assumptions)result = None# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.base == E:
if ask(Q.real(expr.exp), assumptions):
FalseNoneif None.is_number:
_NegativePredicate_number(expr, assumptions)if None(Q.real(expr.base), assumptions):
if ask(Q.positive(expr.base), assumptions) and ask(Q.real(expr.exp), assumptions):
Falseif None(Q.even(expr.exp), assumptions):
Falseif None(Q.odd(expr.exp), assumptions):
ask(Q.negative(expr.base), assumptions)None)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: if ask(Q.real(expr.exp), assumptions):
Falseraise None)()
_ = (lambda expr, assumptions: if expr.is_number:
notnegative = fuzzy_not(_NegativePredicate_number(expr, assumptions))if notnegative:
ask(Q.real(expr), assumptions)None)()
_ = (lambda expr, assumptions: ret = expr.is_nonnegative# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: ret = expr.is_nonzero# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: for arg in expr.args:
result = ask(Q.nonzero(arg), assumptions)if result:
continueNone, resultTrue)()
_ = (lambda expr, assumptions: ask(Q.nonzero(expr.base), assumptions))()
_ = (lambda expr, assumptions: ask(Q.nonzero(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: pass)()
_ = (lambda expr, assumptions: ret = expr.is_zero# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: fuzzy_and([
fuzzy_not(ask(Q.nonzero(expr), assumptions)),
ask(Q.real(expr), assumptions)]))()
_ = (lambda expr, assumptions: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: ret = expr.is_nonpositive# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
notpositive = fuzzy_not(_PositivePredicate_number(expr, assumptions))if notpositive:
ask(Q.real(expr), assumptions)None)()

def _PositivePredicate_number(expr, assumptions):
    (r, i) = expr.as_real_imag()
    if not i:
        r = r.evalf(2)
        if r._prec != 1:
            return r > 0
        return None
    i = None.evalf(2)
    if i._prec != 1:
        if i != 0:
            return False
        r = None.evalf(2)
        if r._prec != 1:
            return r > 0
        return None

_ = (lambda expr, assumptions: ret = expr.is_positive# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
_PositivePredicate_number(expr, assumptions))()
_ = (lambda expr, assumptions: if expr.is_number:
_PositivePredicate_number(expr, assumptions)result = Nonefor arg in expr.args:
if ask(Q.positive(arg), assumptions):
continueif ask(Q.negative(arg), assumptions):
result = result ^ TruecontinueNoneresult)()
_ = (lambda expr, assumptions: if expr.is_number:
_PositivePredicate_number(expr, assumptions)r = None(Q.real(expr), assumptions)if r is not True:
rnonneg = Nonefor arg in expr.args:
if ask(Q.positive(arg), assumptions) is not True:
if ask(Q.negative(arg), assumptions) is False:
nonneg += 1continueNoneif nonneg < len(expr.args):
TrueNone)()
_ = (lambda expr, assumptions: if expr.base == E:
if ask(Q.real(expr.exp), assumptions):
Trueif None(Q.imaginary(expr.exp), assumptions):
ask(Q.even(expr.exp / (I * pi)), assumptions)Noneif None.is_number:
_PositivePredicate_number(expr, assumptions)if None(Q.positive(expr.base), assumptions) and ask(Q.real(expr.exp), assumptions):
Trueif None(Q.negative(expr.base), assumptions):
if ask(Q.even(expr.exp), assumptions):
Trueif None(Q.odd(expr.exp), assumptions):
FalseNone)()
_ = (lambda expr, assumptions: if ask(Q.real(expr.exp), assumptions):
Trueif None(Q.imaginary(expr.exp), assumptions):
ask(Q.even(expr.exp / (I * pi)), assumptions))()
_ = (lambda expr, assumptions: r = ask(Q.real(expr.args[0]), assumptions)if r is not True:
rif None(Q.positive(expr.args[0] - 1), assumptions):
Trueif None(Q.negative(expr.args[0] - 1), assumptions):
False)()
_ = (lambda expr, assumptions: x = expr.args[0]if ask(Q.integer(x) & Q.positive(x), assumptions):
True)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: ask(Q.nonzero(expr), assumptions))()
_ = (lambda expr, assumptions: if ask(Q.positive_definite(expr.arg), assumptions):
True)()
_ = (lambda expr, assumptions: if ask(Q.positive_definite(expr.arg), assumptions):
True)()
_ = (lambda expr, assumptions: if expr.i == expr.j or ask(Q.positive_definite(expr.parent), assumptions):
TrueNone)()
_ = (lambda expr, assumptions: ask(Q.positive(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: x = expr.args[0]if ask(Q.positive(x) & Q.nonpositive(x - 1), assumptions):
Trueif None(Q.negative(x) & Q.nonnegative(x + 1), assumptions):
False)()
_ = (lambda expr, assumptions: x = expr.args[0]if ask(Q.nonpositive(x - 1) & Q.nonnegative(x + 1), assumptions):
True)()
_ = (lambda expr, assumptions: ask(Q.real(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: pass)()
_ = (lambda expr, assumptions: ask(Q.negative(expr) | Q.negative_infinite(expr), assumptions))()
_ = (lambda expr, assumptions: ask(Q.positive(expr) | Q.positive_infinite(expr), assumptions))()
_ = (lambda expr, assumptions: ask(Q.negative_infinite(expr) | Q.negative(expr) | Q.positive(expr) | Q.positive_infinite(expr), assumptions))()
_ = (lambda expr, assumptions: ask(Q.negative_infinite(expr) | Q.negative(expr) | Q.zero(expr), assumptions))()
_ = (lambda expr, assumptions: ask(Q.zero(expr) | Q.positive(expr) | Q.positive_infinite(expr), assumptions))()
