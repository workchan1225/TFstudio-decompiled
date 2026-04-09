# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expr_with_limits.pyc (Python 3.11)

from sympy.core.add import Add
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.core.function import AppliedUndef, UndefinedFunction
from sympy.core.mul import Mul
from sympy.core.relational import Equality, Relational
from sympy.core.singleton import S
from sympy.core.symbol import Symbol, Dummy
from sympy.core.sympify import sympify
from sympy.functions.elementary.piecewise import piecewise_fold, Piecewise
from sympy.logic.boolalg import BooleanFunction
from sympy.matrices.matrixbase import MatrixBase
from sympy.sets.sets import Interval, Set
from sympy.sets.fancysets import Range
from sympy.tensor.indexed import Idx
from sympy.utilities import flatten
from sympy.utilities.iterables import sift, is_sequence
from sympy.utilities.exceptions import sympy_deprecation_warning

def _common_new(cls, function, *, discrete, *symbols, **assumptions):
    '''Return either a special return value or the tuple,
    (function, limits, orientation). This code is common to
    both ExprWithLimits and AddWithLimits.'''
    function = sympify(function)
# WARNING: Decompyle incomplete


def _process_limits(*, discrete, *symbols):
    '''Process the list of symbols and convert them to canonical limits,
    storing them as Tuple(symbol, lower, upper). The orientation of
    the function is also returned when the upper limit is missing
    so (x, 1, None) becomes (x, None, 1) and the orientation is changed.
    In the case that a limit is specified as (symbol, Range), a list of
    length 4 may be returned if a change of variables is needed; the
    expression that should replace the symbol in the expression is
    the fourth element in the list.
    '''
    limits = []
    orientation = 1
# WARNING: Decompyle incomplete


class ExprWithLimits(Expr):
    __slots__ = ('is_commutative',)
    
    def __new__(cls, function, *symbols, **assumptions):
        Product = Product
        import sympy.concrete.products
    # WARNING: Decompyle incomplete

    function = (lambda self: self._args[0])()
    kind = (lambda self: self.function.kind)()
    limits = (lambda self: self._args[1:])()
    variables = (lambda self: self.limits())()
    bound_symbols = (lambda self: self.limits())()
    free_symbols = (lambda self: pass# WARNING: Decompyle incomplete
)()
    is_number = (lambda self: not (self.free_symbols))()
    
    def _eval_interval(self, x, a, b):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_subs(self, old, new):
        '''
        Perform substitutions over non-dummy variables
        of an expression with limits.  Also, can be used
        to specify point-evaluation of an abstract antiderivative.

        Examples
        ========

        >>> from sympy import Sum, oo
        >>> from sympy.abc import s, n
        >>> Sum(1/n**s, (n, 1, oo)).subs(s, 2)
        Sum(n**(-2), (n, 1, oo))

        >>> from sympy import Integral
        >>> from sympy.abc import x, a
        >>> Integral(a*x**2, x).subs(x, 4)
        Integral(a*x**2, (x, 4))

        See Also
        ========

        variables : Lists the integration variables
        transform : Perform mapping on the dummy variable for integrals
        change_index : Perform mapping on the sum and product dummy variables

        '''
        pass
    # WARNING: Decompyle incomplete

    has_finite_limits = (lambda self: ret_None = False# WARNING: Decompyle incomplete
)()
    has_reversed_limits = (lambda self: ret_None = Falsefor lim in self.limits:
if len(lim) == 3:
(var, a, b) = limdif = b - aif dif.is_extended_negative:
Trueif None.is_extended_nonnegative:
continueret_None = TruecontinueNoneif ret_None:
NoneNone)()


class AddWithLimits(ExprWithLimits):
    '''Represents unevaluated oriented additions.
        Parent class for Integral and Sum.
    '''
    __slots__ = ()
    
    def __new__(cls, function, *symbols, **assumptions):
        Sum = Sum
        import sympy.concrete.summations
    # WARNING: Decompyle incomplete

    
    def _eval_adjoint(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_conjugate(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_transpose(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_factor(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_expand_basic(self, **hints):
        pass
    # WARNING: Decompyle incomplete
