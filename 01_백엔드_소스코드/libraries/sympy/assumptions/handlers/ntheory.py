# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ntheory.pyc (Python 3.11)

'''
Handlers for keys related to number theory: prime, even, odd, etc.
'''
from sympy.assumptions import Q, ask
from sympy.core import Add, Basic, Expr, Float, Mul, Pow, S
from sympy.core.numbers import ImaginaryUnit, Infinity, Integer, NaN, NegativeInfinity, NumberSymbol, Rational, int_valued
from sympy.functions import Abs, im, re
from sympy.ntheory import isprime
from sympy.multipledispatch import MDNotImplementedError
from predicates.ntheory import PrimePredicate, CompositePredicate, EvenPredicate, OddPredicate

def _PrimePredicate_number(expr, assumptions):
    exact = not expr.atoms(Float)
    
    try:
        i = int(expr.round())
        if (expr - i).equals(0) is False:
            raise TypeError
    except TypeError:
        return False

    if exact:
        return isprime(i)

_ = (lambda expr, assumptions: ret = expr.is_prime# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
_PrimePredicate_number(expr, assumptions))()
_ = (lambda expr, assumptions: if expr.is_number:
_PrimePredicate_number(expr, assumptions)for arg in None.args:
if not ask(Q.integer(arg), assumptions):
Nonefor arg in expr.args:
if arg.is_number and arg.is_composite:
FalseNone)()
_ = (lambda expr, assumptions: if expr.is_number:
_PrimePredicate_number(expr, assumptions)if None(Q.integer(expr.exp), assumptions) or ask(Q.integer(expr.base), assumptions):
FalseNone)()
_ = (lambda expr, assumptions: isprime(expr))()
_ = (lambda expr, assumptions: False)()
_ = (lambda expr, assumptions: _PrimePredicate_number(expr, assumptions))()
_ = (lambda expr, assumptions: _PrimePredicate_number(expr, assumptions))()
_ = (lambda expr, assumptions: pass)()
_ = (lambda expr, assumptions: ret = expr.is_composite# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: _positive = ask(Q.positive(expr), assumptions)# WARNING: Decompyle incomplete
)()

def _EvenPredicate_number(expr, assumptions):
    if isinstance(expr, (float, Float)):
        if int_valued(expr):
            return None
        return None
    
    try:
        i = int(expr.round())
    except TypeError:
        return False

    if not (expr - i).equals(0):
        return False
    return None % 2 == 0

_ = (lambda expr, assumptions: ret = expr.is_even# WARNING: Decompyle incomplete
)()
_ = (lambda expr, assumptions: if expr.is_number:
_EvenPredicate_number(expr, assumptions))()
_ = (lambda expr, assumptions:
