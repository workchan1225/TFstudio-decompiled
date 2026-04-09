# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: binrel.pyc (Python 3.11)

'''
General binary relations.
'''
from typing import Optional
from sympy.core.singleton import S
from sympy.assumptions import AppliedPredicate, ask, Predicate, Q
from sympy.core.kind import BooleanKind
from sympy.core.relational import Eq, Ne, Gt, Lt, Ge, Le
from sympy.logic.boolalg import conjuncts, Not
__all__ = [
    'BinaryRelation',
    'AppliedBinaryRelation']

class BinaryRelation(Predicate):
    '''
    Base class for all binary relational predicates.

    Explanation
    ===========

    Binary relation takes two arguments and returns ``AppliedBinaryRelation``
    instance. To evaluate it to boolean value, use :obj:`~.ask()` or
    :obj:`~.refine()` function.

    You can add support for new types by registering the handler to dispatcher.
    See :obj:`~.Predicate()` for more information about predicate dispatching.

    Examples
    ========

    Applying and evaluating to boolean value:

    >>> from sympy import Q, ask, sin, cos
    >>> from sympy.abc import x
    >>> Q.eq(sin(x)**2+cos(x)**2, 1)
    Q.eq(sin(x)**2 + cos(x)**2, 1)
    >>> ask(_)
    True

    You can define a new binary relation by subclassing and dispatching.
    Here, we define a relation $R$ such that $x R y$ returns true if
    $x = y + 1$.

    >>> from sympy import ask, Number, Q
    >>> from sympy.assumptions import BinaryRelation
    >>> class MyRel(BinaryRelation):
    ...     name = "R"
    ...     is_reflexive = False
    >>> Q.R = MyRel()
    >>> @Q.R.register(Number, Number)
    ... def _(n1, n2, assumptions):
    ...     return ask(Q.zero(n1 - n2 - 1), assumptions)
    >>> Q.R(2, 1)
    Q.R(2, 1)

    Now, we can use ``ask()`` to evaluate it to boolean value.

    >>> ask(Q.R(2, 1))
    True
    >>> ask(Q.R(1, 2))
    False

    ``Q.R`` returns ``False`` with minimum cost if two arguments have same
    structure because it is antireflexive relation [1] by
    ``is_reflexive = False``.

    >>> ask(Q.R(x, x))
    False

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Reflexive_relation
    '''
    is_reflexive: Optional[bool] = None
    is_symmetric: Optional[bool] = None
    
    def __call__(self, *args):
        if not len(args) == 2:
            raise ValueError('Binary relation takes two arguments, but got %s.' % len(args))
    # WARNING: Decompyle incomplete

    reversed = (lambda self: if self.is_symmetric:
self)()
    negated = (lambda self: pass)()
    
    def _compare_reflexive(self, lhs, rhs):
        if lhs is S.NaN or rhs is S.NaN:
            return None
        reflexive = None.is_reflexive
    # WARNING: Decompyle incomplete

    
    def eval(self, args, assumptions = (True,)):
        pass
    # WARNING: Decompyle incomplete



class AppliedBinaryRelation(AppliedPredicate):
    '''
    The class of expressions resulting from applying ``BinaryRelation``
    to the arguments.

    '''
    lhs = (lambda self: self.arguments[0])()
    rhs = (lambda self: self.arguments[1])()
    reversed = (lambda self: revfunc = self.function.reversed# WARNING: Decompyle incomplete
)()
    reversedsign = (lambda self: revfunc = self.function.reversed# WARNING: Decompyle incomplete
)()
    negated = (lambda self: neg_rel = self.function.negated# WARNING: Decompyle incomplete
)()
    
    def _eval_ask(self, assumptions):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self):
        ret = ask(self)
    # WARNING: Decompyle incomplete
