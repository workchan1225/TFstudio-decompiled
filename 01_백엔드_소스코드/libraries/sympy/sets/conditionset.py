# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conditionset.pyc (Python 3.11)

from sympy.core.singleton import S
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.function import Lambda, BadSignatureError
from sympy.core.logic import fuzzy_bool
from sympy.core.relational import Eq
from sympy.core.symbol import Dummy
from sympy.core.sympify import _sympify
from sympy.logic.boolalg import And, as_Boolean
from sympy.utilities.iterables import sift, flatten, has_dups
from sympy.utilities.exceptions import sympy_deprecation_warning
from contains import Contains
from sets import Set, Union, FiniteSet, SetKind
adummy = Dummy('conditionset')

class ConditionSet(Set):
    """
    Set of elements which satisfies a given condition.

    .. math:: \\{x \\mid \\textrm{condition}(x) = \\texttt{True}, x \\in S\\}

    Examples
    ========

    >>> from sympy import Symbol, S, ConditionSet, pi, Eq, sin, Interval
    >>> from sympy.abc import x, y, z

    >>> sin_sols = ConditionSet(x, Eq(sin(x), 0), Interval(0, 2*pi))
    >>> 2*pi in sin_sols
    True
    >>> pi/2 in sin_sols
    False
    >>> 3*pi in sin_sols
    False
    >>> 5 in ConditionSet(x, x**2 > 4, S.Reals)
    True

    If the value is not in the base set, the result is false:

    >>> 5 in ConditionSet(x, x**2 > 4, Interval(2, 4))
    False

    Notes
    =====

    Symbols with assumptions should be avoided or else the
    condition may evaluate without consideration of the set:

    >>> n = Symbol('n', negative=True)
    >>> cond = (n > 0); cond
    False
    >>> ConditionSet(n, cond, S.Integers)
    EmptySet

    Only free symbols can be changed by using `subs`:

    >>> c = ConditionSet(x, x < 1, {x, z})
    >>> c.subs(x, y)
    ConditionSet(x, x < 1, {y, z})

    To check if ``pi`` is in ``c`` use:

    >>> pi in c
    False

    If no base set is specified, the universal set is implied:

    >>> ConditionSet(x, x < 1).base_set
    UniversalSet

    Only symbols or symbol-like expressions can be used:

    >>> ConditionSet(x + 1, x + 1 < 1, S.Integers)
    Traceback (most recent call last):
    ...
    ValueError: non-symbol dummy not recognized in condition

    When the base set is a ConditionSet, the symbols will be
    unified if possible with preference for the outermost symbols:

    >>> ConditionSet(x, x < y, ConditionSet(z, z + y < 2, S.Integers))
    ConditionSet(x, (x < y) & (x + y < 2), Integers)

    """
    
    def __new__(cls, sym, condition, base_set = (S.UniversalSet,)):
        pass
    # WARNING: Decompyle incomplete

    sym = property((lambda self: self.args[0]))
    condition = property((lambda self: self.args[1]))
    base_set = property((lambda self: self.args[2]))
    free_symbols = (lambda self: cond_syms = self.condition.free_symbols - self.sym.free_symbolscond_syms | self.base_set.free_symbols)()
    bound_symbols = (lambda self: flatten([
self.sym]))()
    
    def _contains(self, other):
        pass
    # WARNING: Decompyle incomplete

    
    def as_relational(self, other):
        f = Lambda(self.sym, self.condition)
    # WARNING: Decompyle incomplete

    
    def _eval_subs(self, old, new):
        (sym, cond, base) = self.args
        dsym = sym.subs(old, adummy)
        insym = dsym.has(adummy)
        newbase = base.subs(old, new)
        if newbase != base:
            if not insym:
                cond = cond.subs(old, new)
            return self.func(sym, cond, newbase)
        if None:
            pass
        elif getattr(new, '_diff_wrt', False):
            cond = cond.subs(old, new)
        
        return self.func(sym, cond, base)

    
    def _kind(self):
        return SetKind(self.sym.kind)
