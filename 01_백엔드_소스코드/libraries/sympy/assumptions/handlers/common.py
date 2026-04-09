# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''
This module defines base class for handlers and some core handlers:
``Q.commutative`` and ``Q.is_true``.
'''
from sympy.assumptions import Q, ask, AppliedPredicate
from sympy.core import Basic, Symbol
from sympy.core.logic import _fuzzy_group
from sympy.core.numbers import NaN, Number
from sympy.logic.boolalg import And, BooleanTrue, BooleanFalse, conjuncts, Equivalent, Implies, Not, Or
from sympy.utilities.exceptions import sympy_deprecation_warning
from predicates.common import CommutativePredicate, IsTruePredicate

class AskHandler:
    pass
# WARNING: Decompyle incomplete


class CommonHandler(AskHandler):
    '''Defines some useful methods common to most Handlers. '''
    AlwaysTrue = (lambda expr, assumptions: True)()
    AlwaysFalse = (lambda expr, assumptions: False)()
    AlwaysNone = (lambda expr, assumptions: pass)()
    NaN = AlwaysFalse

_ = (lambda expr, assumptions: assumps = conjuncts(assumptions)# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: for arg in expr.args:
if not ask(Q.commutative(arg), assumptions):
FalseTrue)()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: expr)()
_ = (lambda expr, assumptions: True)()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: ask(expr, assumptions))()
_ = (lambda expr, assumptions: arg = expr.args[0]if arg.is_Symbol:
Nonevalue = None(arg, assumptions = assumptions)if value in (True, False):
not value)()
_ = (lambda expr, assumptions: result = False# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: result = True# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: (p, q) = expr.argsask(~p | q, assumptions = assumptions))()
_ = (lambda expr, assumptions: (p, q) = expr.argspt = ask(p, assumptions = assumptions)# WARNING: Decompyle incomplete
)()

def test_closed_group(expr, assumptions, key):
    '''
    Test for membership in a group with respect
    to the current operation.
    '''
    pass
# WARNING: Decompyle incomplete
