# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sathandlers.pyc (Python 3.11)

from collections import defaultdict
from sympy.assumptions.ask import Q
from sympy.core import Add, Mul, Pow, Number, NumberSymbol, Symbol
from sympy.core.numbers import ImaginaryUnit
from sympy.functions.elementary.complexes import Abs
from sympy.logic.boolalg import Equivalent, And, Or, Implies
from sympy.matrices.expressions import MatMul

def allargs(symbol, fact, expr):
    '''
    Apply all arguments of the expression to the fact structure.

    Parameters
    ==========

    symbol : Symbol
        A placeholder symbol.

    fact : Boolean
        Resulting ``Boolean`` expression.

    expr : Expr

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.sathandlers import allargs
    >>> from sympy.abc import x, y
    >>> allargs(x, Q.negative(x) | Q.positive(x), x*y)
    (Q.negative(x) | Q.positive(x)) & (Q.negative(y) | Q.positive(y))

    '''
    pass
# WARNING: Decompyle incomplete


def anyarg(symbol, fact, expr):
    '''
    Apply any argument of the expression to the fact structure.

    Parameters
    ==========

    symbol : Symbol
        A placeholder symbol.

    fact : Boolean
        Resulting ``Boolean`` expression.

    expr : Expr

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.sathandlers import anyarg
    >>> from sympy.abc import x, y
    >>> anyarg(x, Q.negative(x) & Q.positive(x), x*y)
    (Q.negative(x) & Q.positive(x)) | (Q.negative(y) & Q.positive(y))

    '''
    pass
# WARNING: Decompyle incomplete


def exactlyonearg(symbol, fact, expr):
    '''
    Apply exactly one argument of the expression to the fact structure.

    Parameters
    ==========

    symbol : Symbol
        A placeholder symbol.

    fact : Boolean
        Resulting ``Boolean`` expression.

    expr : Expr

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.sathandlers import exactlyonearg
    >>> from sympy.abc import x, y
    >>> exactlyonearg(x, Q.positive(x), x*y)
    (Q.positive(x) & ~Q.positive(y)) | (Q.positive(y) & ~Q.positive(x))

    '''
    pass
# WARNING: Decompyle incomplete


class ClassFactRegistry:
    '''
    Register handlers against classes.

    Explanation
    ===========

    ``register`` method registers the handler function for a class. Here,
    handler function should return a single fact. ``multiregister`` method
    registers the handler function for multiple classes. Here, handler function
    should return a container of multiple facts.

    ``registry(expr)`` returns a set of facts for *expr*.

    Examples
    ========

    Here, we register the facts for ``Abs``.

    >>> from sympy import Abs, Equivalent, Q
    >>> from sympy.assumptions.sathandlers import ClassFactRegistry
    >>> reg = ClassFactRegistry()
    >>> @reg.register(Abs)
    ... def f1(expr):
    ...     return Q.nonnegative(expr)
    >>> @reg.register(Abs)
    ... def f2(expr):
    ...     arg = expr.args[0]
    ...     return Equivalent(~Q.zero(arg), ~Q.zero(expr))

    Calling the registry with expression returns the defined facts for the
    expression.

    >>> from sympy.abc import x
    >>> reg(Abs(x))
    {Q.nonnegative(Abs(x)), Equivalent(~Q.zero(x), ~Q.zero(Abs(x)))}

    Multiple facts can be registered at once by ``multiregister`` method.

    >>> reg2 = ClassFactRegistry()
    >>> @reg2.multiregister(Abs)
    ... def _(expr):
    ...     arg = expr.args[0]
    ...     return [Q.even(arg) >> Q.even(expr), Q.odd(arg) >> Q.odd(expr)]
    >>> reg2(Abs(x))
    {Implies(Q.even(x), Q.even(Abs(x))), Implies(Q.odd(x), Q.odd(Abs(x)))}

    '''
    
    def __init__(self):
        self.singlefacts = defaultdict(frozenset)
        self.multifacts = defaultdict(frozenset)

    
    def register(self, cls):
        pass
    # WARNING: Decompyle incomplete

    
    def multiregister(self, *classes):
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, key):
        ret1 = self.singlefacts[key]
        for k in self.singlefacts:
            if issubclass(key, k):
                ret1 |= self.singlefacts[k]
            ret2 = self.multifacts[key]
            for k in self.multifacts:
                if issubclass(key, k):
                    ret2 |= self.multifacts[k]
                return (ret1, ret2)

    
    def __call__(self, expr):
        pass
    # WARNING: Decompyle incomplete


class_fact_registry = ClassFactRegistry()
x = Symbol('x')
_ = (lambda expr: arg = expr.args[0][
Q.nonnegative(expr),
Equivalent(~Q.zero(arg), ~Q.zero(expr)),
Q.even(arg) >> Q.even(expr),
Q.odd(arg) >> Q.odd(expr),
Q.integer(arg) >> Q.integer(expr)])()
_ = (lambda expr: [
allargs(x, Q.positive(x), expr) >> Q.positive(expr),
allargs(x, Q.negative(x), expr) >> Q.negative(expr),
allargs(x, Q.real(x), expr) >> Q.real(expr),
allargs(x, Q.rational(x), expr) >> Q.rational(expr),
allargs(x, Q.integer(x), expr) >> Q.integer(expr),
exactlyonearg(x, ~Q.integer(x), expr) >> ~Q.integer(expr)])()
_ = (lambda expr: allargs_real = allargs(x, Q.real(x), expr)onearg_irrational = exactlyonearg(x, Q.irrational(x), expr)Implies(allargs_real, Implies(onearg_irrational, Q.irrational(expr))))()
_ = (lambda expr: [
Equivalent(Q.zero(expr), anyarg(x, Q.zero(x), expr)),
allargs(x, Q.positive(x), expr) >> Q.positive(expr),
allargs(x, Q.real(x), expr) >> Q.real(expr),
allargs(x, Q.rational(x), expr) >> Q.rational(expr),
allargs(x, Q.integer(x), expr) >> Q.integer(expr),
exactlyonearg(x, ~Q.rational(x), expr) >> ~Q.integer(expr),
allargs(x, Q.commutative(x), expr) >> Q.commutative(expr)])()
_ = (lambda expr: allargs_prime = allargs(x, Q.prime(x), expr)Implies(allargs_prime, ~Q.prime(expr)))()
_ = (lambda expr: allargs_imag_or_real = allargs(x, Q.imaginary(x) | Q.real(x), expr)onearg_imaginary = exactlyonearg(x, Q.imaginary(x), expr)Implies(allargs_imag_or_real, Implies(onearg_imaginary, Q.imaginary(expr))))()
_ = (lambda expr: allargs_real = allargs(x, Q.real(x), expr)onearg_irrational = exactlyonearg(x, Q.irrational(x), expr)Implies(allargs_real, Implies(onearg_irrational, Q.irrational(expr))))()
_ = (lambda expr: allargs_integer = allargs(x, Q.integer(x), expr)anyarg_even = anyarg(x, Q.even(x), expr)Implies(allargs_integer, Equivalent(anyarg_even, Q.even(expr))))()
_ = (lambda expr: allargs_square = allargs(x, Q.square(x), expr)allargs_invertible = allargs(x, Q.invertible(x), expr)Implies(allargs_square, Equivalent(Q.invertible(expr), allargs_invertible)))()
_ = (lambda expr: exp = expr.expbase = expr.base[
(Q.real(base) & Q.even(exp) & Q.nonnegative(exp)) >> Q.nonnegative(expr),
(Q.nonnegative(base) & Q.odd(exp) & Q.nonnegative(exp)) >> Q.nonnegative(expr),
(Q.nonpositive(base) & Q.odd(exp) & Q.nonnegative(exp)) >> Q.nonpositive(expr),
Equivalent(Q.zero(expr), Q.zero(base) & Q.positive(exp))])()
_old_assump_getters = {
    Q.composite: (lambda o: o.is_composite),
    Q.prime: (lambda o: o.is_prime),
    Q.imaginary: (lambda o: o.is_imaginary),
    Q.odd: (lambda o: o.is_odd),
    Q.even: (lambda o: o.is_even),
    Q.irrational: (lambda o: o.is_irrational),
    Q.rational: (lambda o: o.is_rational),
    Q.negative: (lambda o: o.is_negative),
    Q.zero: (lambda o: o.is_zero),
    Q.positive: (lambda o: o.is_positive) }
_ = (lambda expr: ret = []# WARNING: Decompyle incomplete
)()
