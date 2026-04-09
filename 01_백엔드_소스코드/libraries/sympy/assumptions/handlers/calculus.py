# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: calculus.pyc (Python 3.11)

'''
This module contains query handlers responsible for calculus queries:
infinitesimal, finite, etc.
'''
from sympy.assumptions import Q, ask
from sympy.core import Add, Mul, Pow, Symbol
from sympy.core.numbers import NegativeInfinity, GoldenRatio, Infinity, Exp1, ComplexInfinity, ImaginaryUnit, NaN, Number, Pi, E, TribonacciConstant
from sympy.functions import cos, exp, log, sign, sin
from sympy.logic.boolalg import conjuncts
from predicates.calculus import FinitePredicate, InfinitePredicate, PositiveInfinitePredicate, NegativeInfinitePredicate
_ = (lambda expr, assumptions: pass# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: sign = -1result = True# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: result = True# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.base == E:
ask(Q.finite(expr.exp), assumptions)base_bounded = None(Q.finite(expr.base), assumptions)exp_bounded = ask(Q.finite(expr.exp), assumptions)# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: ask(Q.finite(expr.exp), assumptions))()
_ = (lambda expr, assumptions: if ask(Q.infinite(expr.args[0]), assumptions):
FalseNone(~Q.zero(expr.args[0]), assumptions))()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: pass)()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: False)()
