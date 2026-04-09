# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sets.pyc (Python 3.11)

'''
Handlers for predicates related to set membership: integer, rational, etc.
'''
from sympy.assumptions import Q, ask
from sympy.core import Add, Basic, Expr, Mul, Pow, S
from sympy.core.numbers import AlgebraicNumber, ComplexInfinity, Exp1, Float, GoldenRatio, ImaginaryUnit, Infinity, Integer, NaN, NegativeInfinity, Number, NumberSymbol, Pi, pi, Rational, TribonacciConstant, E
from sympy.core.logic import fuzzy_bool
from sympy.functions import Abs, acos, acot, asin, atan, cos, cot, exp, im, log, re, sin, tan
from sympy.core.numbers import I
from sympy.core.relational import Eq
from sympy.functions.elementary.complexes import conjugate
from sympy.matrices import Determinant, MatrixBase, Trace
from sympy.matrices.expressions.matexpr import MatrixElement
from sympy.multipledispatch import MDNotImplementedError
from common import test_closed_group
from predicates.sets import IntegerPredicate, RationalPredicate, IrrationalPredicate, RealPredicate, ExtendedRealPredicate, HermitianPredicate, ComplexPredicate, ImaginaryPredicate, AntihermitianPredicate, AlgebraicPredicate

def _IntegerPredicate_number(expr, assumptions):
    
    try:
        i = int(expr.round())
        if not (expr - i).equals(0):
            raise TypeError
        return True
    except TypeError:
        return False


_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: ret = expr.is_integer# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
_IntegerPredicate_number(expr, assumptions)None(expr, assumptions, Q.integer))()
_ = (lambda expr, assumptions: if expr.is_number:
_IntegerPredicate_number(expr, assumptions)_output = Nonefor arg in expr.args:
if not ask(Q.integer(arg), assumptions):
if arg.is_Rational:
if arg.q == 2:
None, ask(Q.even(2 * expr), assumptions)if ~(None.q & 1):
Noneif ask(Q.irrational(arg), assumptions):
if _output:
continueFalseNoneNone_output)()
_ = (lambda expr, assumptions: ask(Q.integer(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: ask(Q.integer_elements(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: pass)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: ret = expr.is_rational# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number and expr.as_real_imag()[1]:
FalseNone(expr, assumptions, Q.rational))()
_ = (lambda expr, assumptions: if expr.base == E:
x = expr.expif ask(Q.rational(x), assumptions):
ask(~Q.nonzero(x), assumptions)Noneif None(Q.integer(expr.exp), assumptions):
ask(Q.rational(expr.base), assumptions)if None(Q.rational(expr.exp), assumptions) or ask(Q.prime(expr.base), assumptions):
FalseNone)()
_ = (lambda expr, assumptions: x = expr.args[0]if ask(Q.rational(x), assumptions):
ask(~Q.nonzero(x), assumptions))()
_ = (lambda expr, assumptions: x = expr.expif ask(Q.rational(x), assumptions):
ask(~Q.nonzero(x), assumptions))()
_ = (lambda expr, assumptions: x = expr.args[0]if ask(Q.rational(x), assumptions):
False)()
_ = (lambda expr, assumptions: x = expr.args[0]if ask(Q.rational(x), assumptions):
ask(~Q.nonzero(x - 1), assumptions))()
_ = (lambda expr, assumptions: ret = expr.is_irrational# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: _real = ask(Q.real(expr), assumptions)# WARNING: Decompyle incomplete
)()

def _RealPredicate_number(expr, assumptions):
    i = expr.as_real_imag()[1].evalf(2)
    if i._prec != 1:
        return not i

_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: ret = expr.is_real# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
_RealPredicate_number(expr, assumptions)None(expr, assumptions, Q.real))()
_ = (lambda expr, assumptions: if expr.is_number:
_RealPredicate_number(expr, assumptions)result = Nonefor arg in expr.args:
if ask(Q.real(arg), assumptions):
continueif ask(Q.imaginary(arg), assumptions):
result = result ^ TruecontinueNoneresult)()
_ = (lambda expr, assumptions: if expr.is_number:
_RealPredicate_number(expr, assumptions)if None.base == E:
ask(Q.integer(expr.exp / I / pi) | Q.real(expr.exp), assumptions)if (None.base.func == exp or expr.base.is_Pow) and expr.base.base == E:
if ask(Q.imaginary(expr.base.exp), assumptions) and ask(Q.imaginary(expr.exp), assumptions):
Truei = None.base.exp / I / piif ask(Q.integer(2 * i), assumptions):
ask(Q.real(S.NegativeOne ** i ** expr.exp), assumptions)None# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if ask(Q.real(expr.args[0]), assumptions):
True)()
_ = (lambda expr, assumptions: ask(Q.integer(expr.exp / I / pi) | Q.real(expr.exp), assumptions))()
_ = (lambda expr, assumptions: ask(Q.positive(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: ask(Q.real_elements(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: ask(Q.negative_infinite(expr) | Q.negative(expr) | Q.zero(expr) | Q.positive(expr) | Q.positive_infinite(expr), assumptions))()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: test_closed_group(expr, assumptions, Q.extended_real))()
_ = (lambda expr, assumptions: if isinstance(expr, MatrixBase):
NoneNone(Q.real(expr), assumptions))()
_ = (lambda expr, assumptions: if expr.is_number:
raise MDNotImplementedErrortest_closed_group(expr, assumptions, Q.hermitian))()
_ = (lambda expr, assumptions:
