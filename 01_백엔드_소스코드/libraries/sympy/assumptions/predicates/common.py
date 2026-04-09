# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

from sympy.assumptions import Predicate, AppliedPredicate, Q
from sympy.core.relational import Eq, Ne, Gt, Lt, Ge, Le
from sympy.multipledispatch import Dispatcher

class CommutativePredicate(Predicate):
    '''
    Commutative predicate.

    Explanation
    ===========

    ``ask(Q.commutative(x))`` is true iff ``x`` commutes with any other
    object with respect to multiplication operation.

    '''
    name = 'commutative'
    handler = Dispatcher('CommutativeHandler', doc = "Handler for key 'commutative'.")

binrelpreds = {
    Le: Q.le,
    Ge: Q.ge,
    Lt: Q.lt,
    Gt: Q.gt,
    Ne: Q.ne,
    Eq: Q.eq }

class IsTruePredicate(Predicate):
    pass
# WARNING: Decompyle incomplete
