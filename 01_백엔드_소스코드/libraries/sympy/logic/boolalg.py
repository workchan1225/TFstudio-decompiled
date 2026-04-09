# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: boolalg.pyc (Python 3.11)

'''
Boolean algebra module for SymPy
'''
from collections import defaultdict
from itertools import chain, combinations, product, permutations
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.containers import Tuple
from sympy.core.decorators import sympify_method_args, sympify_return
from sympy.core.function import Application, Derivative
from sympy.core.kind import BooleanKind, NumberKind
from sympy.core.numbers import Number
from sympy.core.operations import LatticeOp
from sympy.core.singleton import Singleton, S
from sympy.core.sorting import ordered
from sympy.core.sympify import _sympy_converter, _sympify, sympify
from sympy.utilities.iterables import sift, ibin
from sympy.utilities.misc import filldedent

def as_Boolean(e):
    '''Like ``bool``, return the Boolean value of an expression, e,
    which can be any instance of :py:class:`~.Boolean` or ``bool``.

    Examples
    ========

    >>> from sympy import true, false, nan
    >>> from sympy.logic.boolalg import as_Boolean
    >>> from sympy.abc import x
    >>> as_Boolean(0) is false
    True
    >>> as_Boolean(1) is true
    True
    >>> as_Boolean(x)
    x
    >>> as_Boolean(2)
    Traceback (most recent call last):
    ...
    TypeError: expecting bool or Boolean, not `2`.
    >>> as_Boolean(nan)
    Traceback (most recent call last):
    ...
    TypeError: expecting bool or Boolean, not `nan`.

    '''
    Symbol = Symbol
    import sympy.core.symbol
    if e == True:
        return true
    if None == False:
        return false
# WARNING: Decompyle incomplete

Boolean = <NODE:12>()

class BooleanAtom(Boolean):
    '''
    Base class of :py:class:`~.BooleanTrue` and :py:class:`~.BooleanFalse`.
    '''
    is_Boolean = True
    is_Atom = True
    _op_priority = 11
    
    def simplify(self, *a, **kw):
        return self

    
    def expand(self, *a, **kw):
        return self

    canonical = (lambda self: self)()
    
    def _noop(self, other = (None,)):
        raise TypeError('BooleanAtom not allowed in this context.')

    __add__ = _noop
    __radd__ = _noop
    __sub__ = _noop
    __rsub__ = _noop
    __mul__ = _noop
    __rmul__ = _noop
    __pow__ = _noop
    __rpow__ = _noop
    __truediv__ = _noop
    __rtruediv__ = _noop
    __mod__ = _noop
    __rmod__ = _noop
    _eval_power = _noop
    
    def __lt__(self, other):
        raise TypeError(filldedent('\n            A Boolean argument can only be used in\n            Eq and Ne; all other relationals expect\n            real expressions.\n        '))

    __le__ = __lt__
    __gt__ = __lt__
    __ge__ = __lt__
    
    def _eval_simplify(self, **kwargs):
        return self



def BooleanTrue():
    '''BooleanTrue'''
    pass
# WARNING: Decompyle incomplete

BooleanTrue = <NODE:27>(BooleanTrue, 'BooleanTrue', BooleanAtom, metaclass = Singleton)

def BooleanFalse():
    '''BooleanFalse'''
    pass
# WARNING: Decompyle incomplete

BooleanFalse = <NODE:27>(BooleanFalse, 'BooleanFalse', BooleanAtom, metaclass = Singleton)
true = BooleanTrue()
false = BooleanFalse()
S.true = true
S.false = false

_sympy_converter[bool] = lambda x: true if x else false

class BooleanFunction(Boolean, Application):
    '''Boolean function is a function that lives in a boolean space
    It is used as base class for :py:class:`~.And`, :py:class:`~.Or`,
    :py:class:`~.Not`, etc.
    '''
    is_Boolean = True
    
    def _eval_simplify(self, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def simplify(self, **kwargs):
        simplify = simplify
        import sympy.simplify.simplify
    # WARNING: Decompyle incomplete

    
    def __lt__(self, other):
        raise TypeError(filldedent('\n            A Boolean argument can only be used in\n            Eq and Ne; all other relationals expect\n            real expressions.\n        '))

    __le__ = __lt__
    __ge__ = __lt__
    __gt__ = __lt__
    binary_check_and_simplify = (lambda self: args())()
    
    def to_nnf(self, simplify = (True,)):
        pass
    # WARNING: Decompyle incomplete

    
    def to_anf(self, deep = (True,)):
        pass
    # WARNING: Decompyle incomplete

    _to_nnf = (lambda cls: simplify = kwargs.get('simplify', True)argset = set()# WARNING: Decompyle incomplete
)()
    _to_anf = (lambda cls: deep = kwargs.get('deep', True)new_args = []# WARNING: Decompyle incomplete
)()
    
    def diff(self, *symbols, **assumptions):
        assumptions.setdefault('evaluate', True)
    # WARNING: Decompyle incomplete

    
    def _eval_derivative(self, x):
        if x in self.binary_symbols:
            Eq = Eq
            import sympy.core.relational
            Piecewise = Piecewise
            import sympy.functions.elementary.piecewise
            return Piecewise((0, Eq(self.subs(x, 0), self.subs(x, 1))), (1, True))
        if None in self.free_symbols:
            return None
        return None.Zero



class And(BooleanFunction, LatticeOp):
    pass
# WARNING: Decompyle incomplete


class Or(BooleanFunction, LatticeOp):
    pass
# WARNING: Decompyle incomplete


class Not(BooleanFunction):
    '''
    Logical Not function (negation)


    Returns ``true`` if the statement is ``false`` or ``False``.
    Returns ``false`` if the statement is ``true`` or ``True``.

    Examples
    ========

    >>> from sympy import Not, And, Or
    >>> from sympy.abc import x, A, B
    >>> Not(True)
    False
    >>> Not(False)
    True
    >>> Not(And(True, False))
    True
    >>> Not(Or(True, False))
    False
    >>> Not(And(And(True, x), Or(x, False)))
    ~x
    >>> ~x
    ~x
    >>> Not(And(Or(A, B), Or(~A, ~B)))
    ~((A | B) & (~A | ~B))

    Notes
    =====

    - The ``~`` operator is provided as a convenience, but note that its use
      here is different from its normal use in Python, which is bitwise
      not. In particular, ``~a`` and ``Not(a)`` will be different if ``a`` is
      an integer. Furthermore, since bools in Python subclass from ``int``,
      ``~True`` is the same as ``~1`` which is ``-2``, which has a boolean
      value of True.  To avoid this issue, use the SymPy boolean types
      ``true`` and ``false``.

    - As of Python 3.12, the bitwise not operator ``~`` used on a
      Python ``bool`` is deprecated and will emit a warning.

    >>> from sympy import true
    >>> ~True  # doctest: +SKIP
    -2
    >>> ~true
    False

    '''
    is_Not = True
    eval = (lambda cls, arg: if isinstance(arg, Number) or arg in (True, False):
false if arg else trueif None.is_Not:
arg.args[0]if None.is_Relational:
arg.negated)()
    
    def _eval_as_set(self):
        """
        Rewrite logic operators and relationals in terms of real sets.

        Examples
        ========

        >>> from sympy import Not, Symbol
        >>> x = Symbol('x')
        >>> Not(x > 0).as_set()
        Interval(-oo, 0)
        """
        return self.args[0].as_set().complement(S.Reals)

    
    def to_nnf(self, simplify = (True,)):
        pass
    # WARNING: Decompyle incomplete

    
    def to_anf(self, deep = (True,)):
        return Xor._to_anf(true, self.args[0], deep = deep)



class Xor(BooleanFunction):
    pass
# WARNING: Decompyle incomplete


class Nand(BooleanFunction):
    """
    Logical NAND function.

    It evaluates its arguments in order, giving True immediately if any
    of them are False, and False if they are all True.

    Returns True if any of the arguments are False
    Returns False if all arguments are True

    Examples
    ========

    >>> from sympy.logic.boolalg import Nand
    >>> from sympy import symbols
    >>> x, y = symbols('x y')
    >>> Nand(False, True)
    True
    >>> Nand(True, True)
    False
    >>> Nand(x, y)
    ~(x & y)

    """
    eval = (lambda cls: pass# WARNING: Decompyle incomplete
)()


class Nor(BooleanFunction):
    """
    Logical NOR function.

    It evaluates its arguments in order, giving False immediately if any
    of them are True, and True if they are all False.

    Returns False if any argument is True
    Returns True if all arguments are False

    Examples
    ========

    >>> from sympy.logic.boolalg import Nor
    >>> from sympy import symbols
    >>> x, y = symbols('x y')

    >>> Nor(True, False)
    False
    >>> Nor(True, True)
    False
    >>> Nor(False, True)
    False
    >>> Nor(False, False)
    True
    >>> Nor(x, y)
    ~(x | y)

    """
    eval = (lambda cls: pass# WARNING: Decompyle incomplete
)()


class Xnor(BooleanFunction):
    """
    Logical XNOR function.

    Returns False if an odd number of the arguments are True and the rest are
    False.

    Returns True if an even number of the arguments are True and the rest are
    False.

    Examples
    ========

    >>> from sympy.logic.boolalg import Xnor
    >>> from sympy import symbols
    >>> x, y = symbols('x y')
    >>> Xnor(True, False)
    False
    >>> Xnor(True, True)
    True
    >>> Xnor(True, False, True, True, False)
    False
    >>> Xnor(True, False, True, False)
    True

    """
    eval = (lambda cls: pass# WARNING: Decompyle incomplete
)()


class Implies(BooleanFunction):
    """
    Logical implication.

    A implies B is equivalent to if A then B. Mathematically, it is written
    as `A \\Rightarrow B` and is equivalent to `\\neg A \\vee B` or ``~A | B``.

    Accepts two Boolean arguments; A and B.
    Returns False if A is True and B is False
    Returns True otherwise.

    Examples
    ========

    >>> from sympy.logic.boolalg import Implies
    >>> from sympy import symbols
    >>> x, y = symbols('x y')

    >>> Implies(True, False)
    False
    >>> Implies(False, False)
    True
    >>> Implies(True, True)
    True
    >>> Implies(False, True)
    True
    >>> x >> y
    Implies(x, y)
    >>> y << x
    Implies(x, y)

    Notes
    =====

    The ``>>`` and ``<<`` operators are provided as a convenience, but note
    that their use here is different from their normal use in Python, which is
    bit shifts. Hence, ``Implies(a, b)`` and ``a >> b`` will return different
    things if ``a`` and ``b`` are integers.  In particular, since Python
    considers ``True`` and ``False`` to be integers, ``True >> True`` will be
    the same as ``1 >> 1``, i.e., 0, which has a truth value of False.  To
    avoid this issue, use the SymPy objects ``true`` and ``false``.

    >>> from sympy import true, false
    >>> True >> False
    1
    >>> true >> false
    False

    """
    eval = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    
    def to_nnf(self, simplify = (True,)):
        (a, b) = self.args
        return Or._to_nnf(Not(a), b, simplify = simplify)

    
    def to_anf(self, deep = (True,)):
        (a, b) = self.args
        return Xor._to_anf(true, a, And(a, b), deep = deep)



class Equivalent(BooleanFunction):
    pass
# WARNING: Decompyle incomplete


class ITE(BooleanFunction):
    '''
    If-then-else clause.

    ``ITE(A, B, C)`` evaluates and returns the result of B if A is true
    else it returns the result of C. All args must be Booleans.

    From a logic gate perspective, ITE corresponds to a 2-to-1 multiplexer,
    where A is the select signal.

    Examples
    ========

    >>> from sympy.logic.boolalg import ITE, And, Xor, Or
    >>> from sympy.abc import x, y, z
    >>> ITE(True, False, True)
    False
    >>> ITE(Or(True, False), And(True, True), Xor(True, True))
    True
    >>> ITE(x, y, z)
    ITE(x, y, z)
    >>> ITE(True, x, y)
    x
    >>> ITE(False, x, y)
    y
    >>> ITE(x, y, y)
    y

    Trying to use non-Boolean args will generate a TypeError:

    >>> ITE(True, [], ())
    Traceback (most recent call last):
    ...
    TypeError: expecting bool, Boolean or ITE, not `[]`

    '''
    
    def __new__(cls, *args, **kwargs):
        Eq = Eq
        Ne = Ne
        import sympy.core.relational
        if len(args) != 3:
            raise ValueError('expecting exactly 3 args')
        (a, b, c) = args
    # WARNING: Decompyle incomplete

    eval = (lambda cls: Eq = EqNe = Neimport sympy.core.relational(a, b, c) = args# WARNING: Decompyle incomplete
)()
    
    def to_nnf(self, simplify = (True,)):
        (a, b, c) = self.args
        return And._to_nnf(Or(Not(a), b), Or(a, c), simplify = simplify)

    
    def _eval_as_set(self):
        return self.to_nnf().as_set()

    
    def _eval_rewrite_as_Piecewise(self, *args, **kwargs):
        Piecewise = Piecewise
        import sympy.functions.elementary.piecewise
        return Piecewise((args[1], args[0]), (args[2], True))



class Exclusive(BooleanFunction):
    '''
    True if only one or no argument is true.

    ``Exclusive(A, B, C)`` is equivalent to ``~(A & B) & ~(A & C) & ~(B & C)``.

    For two arguments, this is equivalent to :py:class:`~.Xor`.

    Examples
    ========

    >>> from sympy.logic.boolalg import Exclusive
    >>> Exclusive(False, False, False)
    True
    >>> Exclusive(False, True, False)
    True
    >>> Exclusive(False, True, True)
    False

    '''
    eval = (lambda cls: and_args = []# WARNING: Decompyle incomplete
)()


def conjuncts(expr):
    '''Return a list of the conjuncts in ``expr``.

    Examples
    ========

    >>> from sympy.logic.boolalg import conjuncts
    >>> from sympy.abc import A, B
    >>> conjuncts(A & B)
    frozenset({A, B})
    >>> conjuncts(A | B)
    frozenset({A | B})

    '''
    return And.make_args(expr)


def disjuncts(expr):
    '''Return a list of the disjuncts in ``expr``.

    Examples
    ========

    >>> from sympy.logic.boolalg import disjuncts
    >>> from sympy.abc import A, B
    >>> disjuncts(A | B)
    frozenset({A, B})
    >>> disjuncts(A & B)
    frozenset({A & B})

    '''
    return Or.make_args(expr)


def distribute_and_over_or(expr):
    '''
    Given a sentence ``expr`` consisting of conjunctions and disjunctions
    of literals, return an equivalent sentence in CNF.

    Examples
    ========

    >>> from sympy.logic.boolalg import distribute_and_over_or, And, Or, Not
    >>> from sympy.abc import A, B, C
    >>> distribute_and_over_or(Or(A, And(Not(B), Not(C))))
    (A | ~B) & (A | ~C)

    '''
    return _distribute((expr, And, Or))


def distribute_or_over_and(expr):
    '''
    Given a sentence ``expr`` consisting of conjunctions and disjunctions
    of literals, return an equivalent sentence in DNF.

    Note that the output is NOT simplified.

    Examples
    ========

    >>> from sympy.logic.boolalg import distribute_or_over_and, And, Or, Not
    >>> from sympy.abc import A, B, C
    >>> distribute_or_over_and(And(Or(Not(A), B), C))
    (B & C) | (C & ~A)

    '''
    return _distribute((expr, Or, And))


def distribute_xor_over_and(expr):
    '''
    Given a sentence ``expr`` consisting of conjunction and
    exclusive disjunctions of literals, return an
    equivalent exclusive disjunction.

    Note that the output is NOT simplified.

    Examples
    ========

    >>> from sympy.logic.boolalg import distribute_xor_over_and, And, Xor, Not
    >>> from sympy.abc import A, B, C
    >>> distribute_xor_over_and(And(Xor(Not(A), B), C))
    (B & C) ^ (C & ~A)
    '''
    return _distribute((expr, Xor, And))


def _distribute(info):
    '''
    Distributes ``info[1]`` over ``info[2]`` with respect to ``info[0]``.
    '''
    pass
# WARNING: Decompyle incomplete


def to_anf(expr, deep = (True,)):
    '''
    Converts expr to Algebraic Normal Form (ANF).

    ANF is a canonical normal form, which means that two
    equivalent formulas will convert to the same ANF.

    A logical expression is in ANF if it has the form

    .. math:: 1 \\oplus a \\oplus b \\oplus ab \\oplus abc

    i.e. it can be:
        - purely true,
        - purely false,
        - conjunction of variables,
        - exclusive disjunction.

    The exclusive disjunction can only contain true, variables
    or conjunction of variables. No negations are permitted.

    If ``deep`` is ``False``, arguments of the boolean
    expression are considered variables, i.e. only the
    top-level expression is converted to ANF.

    Examples
    ========
    >>> from sympy.logic.boolalg import And, Or, Not, Implies, Equivalent
    >>> from sympy.logic.boolalg import to_anf
    >>> from sympy.abc import A, B, C
    >>> to_anf(Not(A))
    A ^ True
    >>> to_anf(And(Or(A, B), Not(C)))
    A ^ B ^ (A & B) ^ (A & C) ^ (B & C) ^ (A & B & C)
    >>> to_anf(Implies(Not(A), Equivalent(B, C)), deep=False)
    True ^ ~A ^ (~A & (Equivalent(B, C)))

    '''
    expr = sympify(expr)
    if is_anf(expr):
        return expr
    return None.to_anf(deep = deep)


def to_nnf(expr, simplify = (True,)):
    '''
    Converts ``expr`` to Negation Normal Form (NNF).

    A logical expression is in NNF if it
    contains only :py:class:`~.And`, :py:class:`~.Or` and :py:class:`~.Not`,
    and :py:class:`~.Not` is applied only to literals.
    If ``simplify`` is ``True``, the result contains no redundant clauses.

    Examples
    ========

    >>> from sympy.abc import A, B, C, D
    >>> from sympy.logic.boolalg import Not, Equivalent, to_nnf
    >>> to_nnf(Not((~A & ~B) | (C & D)))
    (A | B) & (~C | ~D)
    >>> to_nnf(Equivalent(A >> B, B >> A))
    (A | ~B | (A & ~B)) & (B | ~A | (B & ~A))

    '''
    if is_nnf(expr, simplify):
        return expr
    return None.to_nnf(simplify)


def to_cnf(expr, simplify, force = (False, False)):
    '''
    Convert a propositional logical sentence ``expr`` to conjunctive normal
    form: ``((A | ~B | ...) & (B | C | ...) & ...)``.
    If ``simplify`` is ``True``, ``expr`` is evaluated to its simplest CNF
    form using the Quine-McCluskey algorithm; this may take a long
    time. If there are more than 8 variables the ``force`` flag must be set
    to ``True`` to simplify (default is ``False``).

    Examples
    ========

    >>> from sympy.logic.boolalg import to_cnf
    >>> from sympy.abc import A, B, D
    >>> to_cnf(~(A | B) | D)
    (D | ~A) & (D | ~B)
    >>> to_cnf((A | B) & (A | ~A), True)
    A | B

    '''
    expr = sympify(expr)
    if not isinstance(expr, BooleanFunction):
        return expr
    if None:
        if force and len(_find_predicates(expr)) > 8:
            raise ValueError(filldedent('\n            To simplify a logical expression with more\n            than 8 variables may take a long time and requires\n            the use of `force=True`.'))
        return simplify_logic(expr, 'cnf', True, force = force)
    if None(expr):
        return expr
    expr = None(expr)
    res = distribute_and_over_or(expr)
    return res


def to_dnf(expr, simplify, force = (False, False)):
    '''
    Convert a propositional logical sentence ``expr`` to disjunctive normal
    form: ``((A & ~B & ...) | (B & C & ...) | ...)``.
    If ``simplify`` is ``True``, ``expr`` is evaluated to its simplest DNF form using
    the Quine-McCluskey algorithm; this may take a long
    time. If there are more than 8 variables, the ``force`` flag must be set to
    ``True`` to simplify (default is ``False``).

    Examples
    ========

    >>> from sympy.logic.boolalg import to_dnf
    >>> from sympy.abc import A, B, C
    >>> to_dnf(B & (A | C))
    (A & B) | (B & C)
    >>> to_dnf((A & B) | (A & ~B) | (B & C) | (~B & C), True)
    A | C

    '''
    expr = sympify(expr)
    if not isinstance(expr, BooleanFunction):
        return expr
    if None:
        if force and len(_find_predicates(expr)) > 8:
            raise ValueError(filldedent('\n            To simplify a logical expression with more\n            than 8 variables may take a long time and requires\n            the use of `force=True`.'))
        return simplify_logic(expr, 'dnf', True, force = force)
    if None(expr):
        return expr
    expr = None(expr)
    return distribute_or_over_and(expr)


def is_anf(expr):
    '''
    Checks if ``expr``  is in Algebraic Normal Form (ANF).

    A logical expression is in ANF if it has the form

    .. math:: 1 \\oplus a \\oplus b \\oplus ab \\oplus abc

    i.e. it is purely true, purely false, conjunction of
    variables or exclusive disjunction. The exclusive
    disjunction can only contain true, variables or
    conjunction of variables. No negations are permitted.

    Examples
    ========

    >>> from sympy.logic.boolalg import And, Not, Xor, true, is_anf
    >>> from sympy.abc import A, B, C
    >>> is_anf(true)
    True
    >>> is_anf(A)
    True
    >>> is_anf(And(A, B, C))
    True
    >>> is_anf(Xor(A, Not(B)))
    False

    '''
    expr = sympify(expr)
    if not is_literal(expr) and isinstance(expr, Not):
        return True
    if None(expr, And):
        for arg in expr.args:
            if not arg.is_Symbol:
                return False
            return True
            if isinstance(expr, Xor):
                for arg in expr.args:
                    if isinstance(arg, And):
                        for a in arg.args:
                            if not a.is_Symbol:
                                return False
                            if is_literal(arg):
                                if isinstance(arg, Not):
                                    return False
                    return False
                    return True
                    return False


def is_nnf(expr, simplified = (True,)):
    '''
    Checks if ``expr`` is in Negation Normal Form (NNF).

    A logical expression is in NNF if it
    contains only :py:class:`~.And`, :py:class:`~.Or` and :py:class:`~.Not`,
    and :py:class:`~.Not` is applied only to literals.
    If ``simplified`` is ``True``, checks if result contains no redundant clauses.

    Examples
    ========

    >>> from sympy.abc import A, B, C
    >>> from sympy.logic.boolalg import Not, is_nnf
    >>> is_nnf(A & B | ~C)
    True
    >>> is_nnf((A | ~A) & (B | C))
    False
    >>> is_nnf((A | ~A) & (B | C), False)
    True
    >>> is_nnf(Not(A & B) | C)
    False
    >>> is_nnf((A >> B) & (B >> A))
    False

    '''
    expr = sympify(expr)
    if is_literal(expr):
        return True
    stack = [
        None]
# WARNING: Decompyle incomplete


def is_cnf(expr):
    '''
    Test whether or not an expression is in conjunctive normal form.

    Examples
    ========

    >>> from sympy.logic.boolalg import is_cnf
    >>> from sympy.abc import A, B, C
    >>> is_cnf(A | B | C)
    True
    >>> is_cnf(A & B & C)
    True
    >>> is_cnf((A & B) | C)
    False

    '''
    return _is_form(expr, And, Or)


def is_dnf(expr):
    '''
    Test whether or not an expression is in disjunctive normal form.

    Examples
    ========

    >>> from sympy.logic.boolalg import is_dnf
    >>> from sympy.abc import A, B, C
    >>> is_dnf(A | B | C)
    True
    >>> is_dnf(A & B & C)
    True
    >>> is_dnf((A & B) | C)
    True
    >>> is_dnf(A & (B | C))
    False

    '''
    return _is_form(expr, Or, And)


def _is_form(expr, function1, function2):
    '''
    Test whether or not an expression is of the required form.

    '''
    expr = sympify(expr)
    vals = function1.make_args(expr) if isinstance(expr, function1) else [
        expr]
    for lit in vals:
        if isinstance(lit, function2):
            vals2 = function2.make_args(lit) if isinstance(lit, function2) else [
                lit]
            for l in vals2:
                if is_literal(l) is False:
                    return False
                if is_literal(lit) is False:
                    return False
                return True


def eliminate_implications(expr):
    '''
    Change :py:class:`~.Implies` and :py:class:`~.Equivalent` into
    :py:class:`~.And`, :py:class:`~.Or`, and :py:class:`~.Not`.
    That is, return an expression that is equivalent to ``expr``, but has only
    ``&``, ``|``, and ``~`` as logical
    operators.

    Examples
    ========

    >>> from sympy.logic.boolalg import Implies, Equivalent,          eliminate_implications
    >>> from sympy.abc import A, B, C
    >>> eliminate_implications(Implies(A, B))
    B | ~A
    >>> eliminate_implications(Equivalent(A, B))
    (A | ~B) & (B | ~A)
    >>> eliminate_implications(Equivalent(A, B, C))
    (A | ~C) & (B | ~A) & (C | ~B)

    '''
    return to_nnf(expr, simplify = False)


def is_literal(expr):
    '''
    Returns True if expr is a literal, else False.

    Examples
    ========

    >>> from sympy import Or, Q
    >>> from sympy.abc import A, B
    >>> from sympy.logic.boolalg import is_literal
    >>> is_literal(A)
    True
    >>> is_literal(~A)
    True
    >>> is_literal(Q.zero(A))
    True
    >>> is_literal(A + B)
    True
    >>> is_literal(Or(A, B))
    False

    '''
    pass
# WARNING: Decompyle incomplete


def to_int_repr(clauses, symbols):
    '''
    Takes clauses in CNF format and puts them into an integer representation.

    Examples
    ========

    >>> from sympy.logic.boolalg import to_int_repr
    >>> from sympy.abc import x, y
    >>> to_int_repr([x | y, y], [x, y]) == [{1, 2}, {2}]
    True

    '''
    pass
# WARNING: Decompyle incomplete


def term_to_integer(term):
    """
    Return an integer corresponding to the base-2 digits given by *term*.

    Parameters
    ==========

    term : a string or list of ones and zeros

    Examples
    ========

    >>> from sympy.logic.boolalg import term_to_integer
    >>> term_to_integer([1, 0, 0])
    4
    >>> term_to_integer('100')
    4

    """
    return int(''.join(list(map(str, list(term)))), 2)

integer_to_term = ibin

def truth_table(expr, variables, input = (True,)):
    """
    Return a generator of all possible configurations of the input variables,
    and the result of the boolean expression for those values.

    Parameters
    ==========

    expr : Boolean expression

    variables : list of variables

    input : bool (default ``True``)
        Indicates whether to return the input combinations.

    Examples
    ========

    >>> from sympy.logic.boolalg import truth_table
    >>> from sympy.abc import x,y
    >>> table = truth_table(x >> y, [x, y])
    >>> for t in table:
    ...     print('{0} -> {1}'.format(*t))
    [0, 0] -> True
    [0, 1] -> True
    [1, 0] -> False
    [1, 1] -> True

    >>> table = truth_table(x | y, [x, y])
    >>> list(table)
    [([0, 0], False), ([0, 1], True), ([1, 0], True), ([1, 1], True)]

    If ``input`` is ``False``, ``truth_table`` returns only a list of truth values.
    In this case, the corresponding input values of variables can be
    deduced from the index of a given output.

    >>> from sympy.utilities.iterables import ibin
    >>> vars = [y, x]
    >>> values = truth_table(x >> y, vars, input=False)
    >>> values = list(values)
    >>> values
    [True, False, True, True]

    >>> for i, value in enumerate(values):
    ...     print('{0} -> {1}'.format(list(zip(
    ...     vars, ibin(i, len(vars)))), value))
    [(y, 0), (x, 0)] -> True
    [(y, 0), (x, 1)] -> False
    [(y, 1), (x, 0)] -> True
    [(y, 1), (x, 1)] -> True

    """
    pass
# WARNING: Decompyle incomplete


def _check_pair(minterm1, minterm2):
    '''
    Checks if a pair of minterms differs by only one bit. If yes, returns
    index, else returns `-1`.
    '''
    index = -1
    for x, i in enumerate(minterm1):
        if i != minterm2[x]:
            if index == -1:
                index = x
                continue
            return -1
        return index


def _convert_to_varsSOP(minterm, variables):
    '''
    Converts a term in the expansion of a function from binary to its
    variable form (for SOP).
    '''
    pass
# WARNING: Decompyle incomplete


def _convert_to_varsPOS(maxterm, variables):
    '''
    Converts a term in the expansion of a function from binary to its
    variable form (for POS).
    '''
    pass
# WARNING: Decompyle incomplete


def _convert_to_varsANF(term, variables):
    """
    Converts a term in the expansion of a function from binary to its
    variable form (for ANF).

    Parameters
    ==========

    term : list of 1's and 0's (complementation pattern)
    variables : list of variables

    """
    pass
# WARNING: Decompyle incomplete


def _get_odd_parity_terms(n):
    '''
    Returns a list of lists, with all possible combinations of n zeros and ones
    with an odd number of ones.
    '''
    pass
# WARNING: Decompyle incomplete


def _get_even_parity_terms(n):
    '''
    Returns a list of lists, with all possible combinations of n zeros and ones
    with an even number of ones.
    '''
    pass
# WARNING: Decompyle incomplete


def _simplified_pairs(terms):
    '''
    Reduces a set of minterms, if possible, to a simplified set of minterms
    with one less variable in the terms using QM method.
    '''
    pass
# WARNING: Decompyle incomplete


def _rem_redundancy(l1, terms):
    '''
    After the truth table has been sufficiently simplified, use the prime
    implicant table method to recognize and eliminate redundant pairs,
    and return the essential arguments.
    '''
    pass
# WARNING: Decompyle incomplete


def _input_to_binlist(inputlist, variables):
    pass
# WARNING: Decompyle incomplete


def SOPform(variables, minterms, dontcares = (None,)):
    '''
    The SOPform function uses simplified_pairs and a redundant group-
    eliminating algorithm to convert the list of all input combos that
    generate \'1\' (the minterms) into the smallest sum-of-products form.

    The variables must be given as the first argument.

    Return a logical :py:class:`~.Or` function (i.e., the "sum of products" or
    "SOP" form) that gives the desired outcome. If there are inputs that can
    be ignored, pass them as a list, too.

    The result will be one of the (perhaps many) functions that satisfy
    the conditions.

    Examples
    ========

    >>> from sympy.logic import SOPform
    >>> from sympy import symbols
    >>> w, x, y, z = symbols(\'w x y z\')
    >>> minterms = [[0, 0, 0, 1], [0, 0, 1, 1],
    ...             [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1]]
    >>> dontcares = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]]
    >>> SOPform([w, x, y, z], minterms, dontcares)
    (y & z) | (~w & ~x)

    The terms can also be represented as integers:

    >>> minterms = [1, 3, 7, 11, 15]
    >>> dontcares = [0, 2, 5]
    >>> SOPform([w, x, y, z], minterms, dontcares)
    (y & z) | (~w & ~x)

    They can also be specified using dicts, which does not have to be fully
    specified:

    >>> minterms = [{w: 0, x: 1}, {y: 1, z: 1, x: 0}]
    >>> SOPform([w, x, y, z], minterms)
    (x & ~w) | (y & z & ~x)

    Or a combination:

    >>> minterms = [4, 7, 11, [1, 1, 1, 1]]
    >>> dontcares = [{w : 0, x : 0, y: 0}, 5]
    >>> SOPform([w, x, y, z], minterms, dontcares)
    (w & y & z) | (~w & ~y) | (x & z & ~w)

    See also
    ========

    POSform

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Quine-McCluskey_algorithm
    .. [2] https://en.wikipedia.org/wiki/Don%27t-care_term

    '''
    if not minterms:
        return false
    variables = None(map(sympify, variables))
    minterms = _input_to_binlist(minterms, variables)
    if not dontcares:
        dontcares = _input_to_binlist([], variables)
        for d in dontcares:
            if d in minterms:
                raise ValueError('%s in minterms is also in dontcares' % d)
            return _sop_form(variables, minterms, dontcares)


def _sop_form(variables, minterms, dontcares):
    pass
# WARNING: Decompyle incomplete


def POSform(variables, minterms, dontcares = (None,)):
    '''
    The POSform function uses simplified_pairs and a redundant-group
    eliminating algorithm to convert the list of all input combinations
    that generate \'1\' (the minterms) into the smallest product-of-sums form.

    The variables must be given as the first argument.

    Return a logical :py:class:`~.And` function (i.e., the "product of sums"
    or "POS" form) that gives the desired outcome. If there are inputs that can
    be ignored, pass them as a list, too.

    The result will be one of the (perhaps many) functions that satisfy
    the conditions.

    Examples
    ========

    >>> from sympy.logic import POSform
    >>> from sympy import symbols
    >>> w, x, y, z = symbols(\'w x y z\')
    >>> minterms = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1],
    ...             [1, 0, 1, 1], [1, 1, 1, 1]]
    >>> dontcares = [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 1]]
    >>> POSform([w, x, y, z], minterms, dontcares)
    z & (y | ~w)

    The terms can also be represented as integers:

    >>> minterms = [1, 3, 7, 11, 15]
    >>> dontcares = [0, 2, 5]
    >>> POSform([w, x, y, z], minterms, dontcares)
    z & (y | ~w)

    They can also be specified using dicts, which does not have to be fully
    specified:

    >>> minterms = [{w: 0, x: 1}, {y: 1, z: 1, x: 0}]
    >>> POSform([w, x, y, z], minterms)
    (x | y) & (x | z) & (~w | ~x)

    Or a combination:

    >>> minterms = [4, 7, 11, [1, 1, 1, 1]]
    >>> dontcares = [{w : 0, x : 0, y: 0}, 5]
    >>> POSform([w, x, y, z], minterms, dontcares)
    (w | x) & (y | ~w) & (z | ~y)

    See also
    ========

    SOPform

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Quine-McCluskey_algorithm
    .. [2] https://en.wikipedia.org/wiki/Don%27t-care_term

    '''
    pass
# WARNING: Decompyle incomplete


def ANFform(variables, truthvalues):
    '''
    The ANFform function converts the list of truth values to
    Algebraic Normal Form (ANF).

    The variables must be given as the first argument.

    Return True, False, logical :py:class:`~.And` function (i.e., the
    "Zhegalkin monomial") or logical :py:class:`~.Xor` function (i.e.,
    the "Zhegalkin polynomial"). When True and False
    are represented by 1 and 0, respectively, then
    :py:class:`~.And` is multiplication and :py:class:`~.Xor` is addition.

    Formally a "Zhegalkin monomial" is the product (logical
    And) of a finite set of distinct variables, including
    the empty set whose product is denoted 1 (True).
    A "Zhegalkin polynomial" is the sum (logical Xor) of a
    set of Zhegalkin monomials, with the empty set denoted
    by 0 (False).

    Parameters
    ==========

    variables : list of variables
    truthvalues : list of 1\'s and 0\'s (result column of truth table)

    Examples
    ========
    >>> from sympy.logic.boolalg import ANFform
    >>> from sympy.abc import x, y
    >>> ANFform([x], [1, 0])
    x ^ True
    >>> ANFform([x, y], [0, 1, 1, 1])
    x ^ y ^ (x & y)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Zhegalkin_polynomial

    '''
    pass
# WARNING: Decompyle incomplete


def anf_coeffs(truthvalues):
    '''
    Convert a list of truth values of some boolean expression
    to the list of coefficients of the polynomial mod 2 (exclusive
    disjunction) representing the boolean expression in ANF
    (i.e., the "Zhegalkin polynomial").

    There are `2^n` possible Zhegalkin monomials in `n` variables, since
    each monomial is fully specified by the presence or absence of
    each variable.

    We can enumerate all the monomials. For example, boolean
    function with four variables ``(a, b, c, d)`` can contain
    up to `2^4 = 16` monomials. The 13-th monomial is the
    product ``a & b & d``, because 13 in binary is 1, 1, 0, 1.

    A given monomial\'s presence or absence in a polynomial corresponds
    to that monomial\'s coefficient being 1 or 0 respectively.

    Examples
    ========
    >>> from sympy.logic.boolalg import anf_coeffs, bool_monomial, Xor
    >>> from sympy.abc import a, b, c
    >>> truthvalues = [0, 1, 1, 0, 0, 1, 0, 1]
    >>> coeffs = anf_coeffs(truthvalues)
    >>> coeffs
    [0, 1, 1, 0, 0, 0, 1, 0]
    >>> polynomial = Xor(*[
    ...     bool_monomial(k, [a, b, c])
    ...     for k, coeff in enumerate(coeffs) if coeff == 1
    ... ])
    >>> polynomial
    b ^ c ^ (a & b)

    '''
    s = '{:b}'.format(len(truthvalues))
    n = len(s) - 1
    if len(truthvalues) != 2 ** n:
        raise ValueError('The number of truth values must be a power of two, got %d' % len(truthvalues))
    coeffs = truthvalues()
    for i in range(n):
        tmp = []
        for j in range(2 ** (n - i - 1)):
            tmp.append(coeffs[2 * j] + list(map((lambda x, y: x ^ y), coeffs[2 * j], coeffs[2 * j + 1])))
            coeffs = tmp
            return coeffs[0]


def bool_minterm(k, variables):
    """
    Return the k-th minterm.

    Minterms are numbered by a binary encoding of the complementation
    pattern of the variables. This convention assigns the value 1 to
    the direct form and 0 to the complemented form.

    Parameters
    ==========

    k : int or list of 1's and 0's (complementation pattern)
    variables : list of variables

    Examples
    ========

    >>> from sympy.logic.boolalg import bool_minterm
    >>> from sympy.abc import x, y, z
    >>> bool_minterm([1, 0, 1], [x, y, z])
    x & z & ~y
    >>> bool_minterm(6, [x, y, z])
    x & y & ~z

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Canonical_normal_form#Indexing_minterms

    """
    if isinstance(k, int):
        k = ibin(k, len(variables))
    variables = tuple(map(sympify, variables))
    return _convert_to_varsSOP(k, variables)


def bool_maxterm(k, variables):
    """
    Return the k-th maxterm.

    Each maxterm is assigned an index based on the opposite
    conventional binary encoding used for minterms. The maxterm
    convention assigns the value 0 to the direct form and 1 to
    the complemented form.

    Parameters
    ==========

    k : int or list of 1's and 0's (complementation pattern)
    variables : list of variables

    Examples
    ========
    >>> from sympy.logic.boolalg import bool_maxterm
    >>> from sympy.abc import x, y, z
    >>> bool_maxterm([1, 0, 1], [x, y, z])
    y | ~x | ~z
    >>> bool_maxterm(6, [x, y, z])
    z | ~x | ~y

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Canonical_normal_form#Indexing_maxterms

    """
    if isinstance(k, int):
        k = ibin(k, len(variables))
    variables = tuple(map(sympify, variables))
    return _convert_to_varsPOS(k, variables)


def bool_monomial(k, variables):
    """
    Return the k-th monomial.

    Monomials are numbered by a binary encoding of the presence and
    absences of the variables. This convention assigns the value
    1 to the presence of variable and 0 to the absence of variable.

    Each boolean function can be uniquely represented by a
    Zhegalkin Polynomial (Algebraic Normal Form). The Zhegalkin
    Polynomial of the boolean function with `n` variables can contain
    up to `2^n` monomials. We can enumerate all the monomials.
    Each monomial is fully specified by the presence or absence
    of each variable.

    For example, boolean function with four variables ``(a, b, c, d)``
    can contain up to `2^4 = 16` monomials. The 13-th monomial is the
    product ``a & b & d``, because 13 in binary is 1, 1, 0, 1.

    Parameters
    ==========

    k : int or list of 1's and 0's
    variables : list of variables

    Examples
    ========
    >>> from sympy.logic.boolalg import bool_monomial
    >>> from sympy.abc import x, y, z
    >>> bool_monomial([1, 0, 1], [x, y, z])
    x & z
    >>> bool_monomial(6, [x, y, z])
    x & y

    """
    if isinstance(k, int):
        k = ibin(k, len(variables))
    variables = tuple(map(sympify, variables))
    return _convert_to_varsANF(k, variables)


def _find_predicates(expr):
    '''Helper to find logical predicates in BooleanFunctions.

    A logical predicate is defined here as anything within a BooleanFunction
    that is not a BooleanFunction itself.

    '''
    if not isinstance(expr, BooleanFunction):
        return {
            expr}
# WARNING: Decompyle incomplete


def simplify_logic(expr, form, deep, force, dontcare = (None, True, False, None)):
    """
    This function simplifies a boolean function to its simplified version
    in SOP or POS form. The return type is an :py:class:`~.Or` or
    :py:class:`~.And` object in SymPy.

    Parameters
    ==========

    expr : Boolean

    form : string (``'cnf'`` or ``'dnf'``) or ``None`` (default).
        If ``'cnf'`` or ``'dnf'``, the simplest expression in the corresponding
        normal form is returned; if ``None``, the answer is returned
        according to the form with fewest args (in CNF by default).

    deep : bool (default ``True``)
        Indicates whether to recursively simplify any
        non-boolean functions contained within the input.

    force : bool (default ``False``)
        As the simplifications require exponential time in the number
        of variables, there is by default a limit on expressions with
        8 variables. When the expression has more than 8 variables
        only symbolical simplification (controlled by ``deep``) is
        made. By setting ``force`` to ``True``, this limit is removed. Be
        aware that this can lead to very long simplification times.

    dontcare : Boolean
        Optimize expression under the assumption that inputs where this
        expression is true are don't care. This is useful in e.g. Piecewise
        conditions, where later conditions do not need to consider inputs that
        are converted by previous conditions. For example, if a previous
        condition is ``And(A, B)``, the simplification of expr can be made
        with don't cares for ``And(A, B)``.

    Examples
    ========

    >>> from sympy.logic import simplify_logic
    >>> from sympy.abc import x, y, z
    >>> b = (~x & ~y & ~z) | ( ~x & ~y & z)
    >>> simplify_logic(b)
    ~x & ~y
    >>> simplify_logic(x | y, dontcare=y)
    x

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Don%27t-care_term

    """
    pass
# WARNING: Decompyle incomplete


def _get_truthtable(variables, expr, const):
    ''' Return a list of all combinations leading to a True result for ``expr``.
    '''
    pass
# WARNING: Decompyle incomplete


def _finger(eq):
    """
    Assign a 5-item fingerprint to each symbol in the equation:
    [
    # of times it appeared as a Symbol;
    # of times it appeared as a Not(symbol);
    # of times it appeared as a Symbol in an And or Or;
    # of times it appeared as a Not(Symbol) in an And or Or;
    a sorted tuple of tuples, (i, j, k), where i is the number of arguments
    in an And or Or with which it appeared as a Symbol, and j is
    the number of arguments that were Not(Symbol); k is the number
    of times that (i, j) was seen.
    ]

    Examples
    ========

    >>> from sympy.logic.boolalg import _finger as finger
    >>> from sympy import And, Or, Not, Xor, to_cnf, symbols
    >>> from sympy.abc import a, b, x, y
    >>> eq = Or(And(Not(y), a), And(Not(y), b), And(x, y))
    >>> dict(finger(eq))
    {(0, 0, 1, 0, ((2, 0, 1),)): [x],
    (0, 0, 1, 0, ((2, 1, 1),)): [a, b],
    (0, 0, 1, 2, ((2, 0, 1),)): [y]}
    >>> dict(finger(x & ~y))
    {(0, 1, 0, 0, ()): [y], (1, 0, 0, 0, ()): [x]}

    In the following, the (5, 2, 6) means that there were 6 Or
    functions in which a symbol appeared as itself amongst 5 arguments in
    which there were also 2 negated symbols, e.g. ``(a0 | a1 | a2 | ~a3 | ~a4)``
    is counted once for a0, a1 and a2.

    >>> dict(finger(to_cnf(Xor(*symbols('a:5')))))
    {(0, 0, 8, 8, ((5, 0, 1), (5, 2, 6), (5, 4, 1))): [a0, a1, a2, a3, a4]}

    The equation must not have more than one level of nesting:

    >>> dict(finger(And(Or(x, y), y)))
    {(0, 0, 1, 0, ((2, 0, 1),)): [x], (1, 0, 1, 0, ((2, 0, 1),)): [y]}
    >>> dict(finger(And(Or(x, And(a, x)), y)))
    Traceback (most recent call last):
    ...
    NotImplementedError: unexpected level of nesting

    So y and x have unique fingerprints, but a and b do not.
    """
    f = eq.free_symbols
    
    def <listcomp>(.0):
        return [ [
            0] * 4 + [
            defaultdict(int)] for fi in .0 ]

    d = list(zip(f(<listcomp>, f())))
    for a in eq.args:
        if a.is_Symbol:
            continue
        if a.is_Not:
            continue
        (sum, (lambda .0: pass# WARNING: Decompyle incomplete
)(a.args()), o) = None
        for ai in a.args:
            if ai.is_Symbol:
                continue
            if ai.is_Not:
                continue
            raise NotImplementedError('unexpected level of nesting')
            defaultdict(list) = len(a.args)
            for k, v in ordered(iter(d.items())):
                v[-1] = sorted((lambda .0: [ i + (j,) for i, j in .0 ])(v[-1].items()()))
                inv[tuple(v)].append(k)
                return inv


def bool_map(bool1, bool2):
    '''
    Return the simplified version of *bool1*, and the mapping of variables
    that makes the two expressions *bool1* and *bool2* represent the same
    logical behaviour for some correspondence between the variables
    of each.
    If more than one mappings of this sort exist, one of them
    is returned.

    For example, ``And(x, y)`` is logically equivalent to ``And(a, b)`` for
    the mapping ``{x: a, y: b}`` or ``{x: b, y: a}``.
    If no such mapping exists, return ``False``.

    Examples
    ========

    >>> from sympy import SOPform, bool_map, Or, And, Not, Xor
    >>> from sympy.abc import w, x, y, z, a, b, c, d
    >>> function1 = SOPform([x, z, y],[[1, 0, 1], [0, 0, 1]])
    >>> function2 = SOPform([a, b, c],[[1, 0, 1], [1, 0, 0]])
    >>> bool_map(function1, function2)
    (y & ~z, {y: a, z: b})

    The results are not necessarily unique, but they are canonical. Here,
    ``(w, z)`` could be ``(a, d)`` or ``(d, a)``:

    >>> eq =  Or(And(Not(y), w), And(Not(y), z), And(x, y))
    >>> eq2 = Or(And(Not(c), a), And(Not(c), d), And(b, c))
    >>> bool_map(eq, eq2)
    ((x & y) | (w & ~y) | (z & ~y), {w: a, x: b, y: c, z: d})
    >>> eq = And(Xor(a, b), c, And(c,d))
    >>> bool_map(eq, eq.subs(c, x))
    (c & d & (a | b) & (~a | ~b), {a: a, b: b, c: d, d: x})

    '''
    
    def match(function1, function2):
        '''Return the mapping that equates variables between two
        simplified boolean expressions if possible.

        By "simplified" we mean that a function has been denested
        and is either an And (or an Or) whose arguments are either
        symbols (x), negated symbols (Not(x)), or Or (or an And) whose
        arguments are only symbols or negated symbols. For example,
        ``And(x, Not(y), Or(w, Not(z)))``.

        Basic.match is not robust enough (see issue 4835) so this is
        a workaround that is valid for simplified boolean expressions
        '''
        if function1.__class__ != function2.__class__:
            return None
        if None(function1.args) != len(function2.args):
            return None
        if None.is_Symbol:
            return {
                function1: function2 }
        f1 = None(function1)
        f2 = _finger(function2)
        if len(f1) != len(f2):
            return False
        matchdict = None
        for k in f1.keys():
            if k not in f2:
                return False
            if None(f1[k]) != len(f2[k]):
                return False
            for i, x in None(f1[k]):
                matchdict[x] = f2[k][i]
                return matchdict

    a = simplify_logic(bool1)
    b = simplify_logic(bool2)
    m = match(a, b)
    if m:
        return (a, m)


def _apply_patternbased_simplification(rv, patterns, measure, dominatingvalue, replacementvalue, threeterm_patterns = (None, None)):
    '''
    Replace patterns of Relational

    Parameters
    ==========

    rv : Expr
        Boolean expression

    patterns : tuple
        Tuple of tuples, with (pattern to simplify, simplified pattern) with
        two terms.

    measure : function
        Simplification measure.

    dominatingvalue : Boolean or ``None``
        The dominating value for the function of consideration.
        For example, for :py:class:`~.And` ``S.false`` is dominating.
        As soon as one expression is ``S.false`` in :py:class:`~.And`,
        the whole expression is ``S.false``.

    replacementvalue : Boolean or ``None``, optional
        The resulting value for the whole expression if one argument
        evaluates to ``dominatingvalue``.
        For example, for :py:class:`~.Nand` ``S.false`` is dominating, but
        in this case the resulting value is ``S.true``. Default is ``None``.
        If ``replacementvalue`` is ``None`` and ``dominatingvalue`` is not
        ``None``, ``replacementvalue = dominatingvalue``.

    threeterm_patterns : tuple, optional
        Tuple of tuples, with (pattern to simplify, simplified pattern) with
        three terms.

    '''
    pass
# WARNING: Decompyle incomplete


def _apply_patternbased_twoterm_simplification(Rel, patterns, func, dominatingvalue, replacementvalue, measure):
    ''' Apply pattern-based two-term simplification.'''
    pass
# WARNING: Decompyle incomplete


def _apply_patternbased_threeterm_simplification(Rel, patterns, func, dominatingvalue, replacementvalue, measure):
    ''' Apply pattern-based three-term simplification.'''
    pass
# WARNING: Decompyle incomplete

_simplify_patterns_and = (lambda : Wild = Wildimport sympy.coreEq = EqNe = NeGe = GeGt = GtLe = LeLt = Ltimport sympy.core.relationalAbs = Absimport sympy.functions.elementary.complexesMin = MinMax = Maximport sympy.functions.elementary.miscellaneousa = Wild('a')b = Wild('b')c = Wild('c')_matchers_and = ((Tuple(Eq(a, b), Lt(a, b)), false), (Tuple(Lt(b, a), Lt(a, b)), false), (Tuple(Eq(a, b), Le(b, a)), Eq(a, b)), (Tuple(Le(b, a), Le(a, b)), Eq(a, b)), (Tuple(Le(a, b), Lt(a, b)), Lt(a, b)), (Tuple(Le(a, b), Ne(a, b)), Lt(a, b)), (Tuple(Lt(a, b), Ne(a, b)), Lt(a, b)), (Tuple(Eq(a, b), Eq(a, -b)), And(Eq(a, S.Zero), Eq(b, S.Zero))), (Tuple(Le(b, a), Le(c, a)), Ge(a, Max(b, c))), (Tuple(Le(b, a), Lt(c, a)), ITE(b > c, Ge(a, b), Gt(a, c))), (Tuple(Lt(b, a), Lt(c, a)), Gt(a, Max(b, c))), (Tuple(Le(a, b), Le(a, c)), Le(a, Min(b, c))), (Tuple(Le(a, b), Lt(a, c)), ITE(b < c, Le(a, b), Lt(a, c))), (Tuple(Lt(a, b), Lt(a, c)), Lt(a, Min(b, c))), (Tuple(Le(a, b), Le(c, a)), ITE(Eq(b, c), Eq(a, b), ITE(b < c, false, And(Le(a, b), Ge(a, c))))), (Tuple(Le(c, a), Le(a, b)), ITE(Eq(b, c), Eq(a, b), ITE(b < c, false, And(Le(a, b), Ge(a, c))))), (Tuple(Lt(a, b), Lt(c, a)), ITE(b < c, false, And(Lt(a, b), Gt(a, c)))), (Tuple(Lt(c, a), Lt(a, b)), ITE(b < c, false, And(Lt(a, b), Gt(a, c)))), (Tuple(Le(a, b), Lt(c, a)), ITE(b <= c, false, And(Le(a, b), Gt(a, c)))), (Tuple(Le(c, a), Lt(a, b)), ITE(b <= c, false, And(Lt(a, b), Ge(a, c)))), (Tuple(Eq(a, b), Eq(a, c)), ITE(Eq(b, c), Eq(a, b), false)), (Tuple(Lt(a, b), Lt(-b, a)), ITE(b > 0, Lt(Abs(a), b), false)), (Tuple(Le(a, b), Le(-b, a)), ITE(b >= 0, Le(Abs(a), b), false)))_matchers_and)()
_simplify_patterns_and3 = (lambda : Wild = Wildimport sympy.coreEq = EqGe = GeGt = Gtimport sympy.core.relationala = Wild('a')b = Wild('b')c = Wild('c')_matchers_and = ((Tuple(Ge(a, b), Ge(b, c), Gt(c, a)), false), (Tuple(Ge(a, b), Gt(b, c), Gt(c, a)), false), (Tuple(Gt(a, b), Gt(b, c), Gt(c, a)), false), (Tuple(Ge(a, b), Ge(a, c), Ge(b, c)), And(Ge(a, b), Ge(b, c))), (Tuple(Ge(a, b), Ge(a, c), Gt(b, c)), And(Ge(a, b), Gt(b, c))), (Tuple(Ge(a, b), Gt(a, c), Gt(b, c)), And(Ge(a, b), Gt(b, c))), (Tuple(Ge(a, c), Gt(a, b), Gt(b, c)), And(Gt(a, b), Gt(b, c))), (Tuple(Ge(b, c), Gt(a, b), Gt(a, c)), And(Gt(a, b), Ge(b, c))), (Tuple(Gt(a, b), Gt(a, c), Gt(b, c)), And(Gt(a, b), Gt(b, c))), (Tuple(Ge(b, a), Ge(c, a), Ge(b, c)), And(Ge(c, a), Ge(b, c))), (Tuple(Ge(b, a), Ge(c, a), Gt(b, c)), And(Ge(c, a), Gt(b, c))), (Tuple(Ge(b, a), Gt(c, a), Gt(b, c)), And(Gt(c, a), Gt(b, c))), (Tuple(Ge(c, a), Gt(b, a), Gt(b, c)), And(Ge(c, a), Gt(b, c))), (Tuple(Ge(b, c), Gt(b, a), Gt(c, a)), And(Gt(c, a), Ge(b, c))), (Tuple(Gt(b, a), Gt(c, a), Gt(b, c)), And(Gt(c, a), Gt(b, c))), (Tuple(Ge(a, b), Ge(b, c), Ge(c, a)), And(Eq(a, b), Eq(b, c))))_matchers_and)()
_simplify_patterns_or = (lambda : Wild = Wildimport sympy.coreEq = EqNe = NeGe = GeGt = GtLe = LeLt = Ltimport sympy.core.relationalAbs = Absimport sympy.functions.elementary.complexesMin = MinMax = Maximport sympy.functions.elementary.miscellaneousa = Wild('a')b = Wild('b')c = Wild('c')_matchers_or = ((Tuple(Le(b, a), Le(a, b)), true), (Tuple(Le(b, a), Ne(a, b)), true), (Tuple(Eq(a, b), Le(a, b)), Le(a, b)), (Tuple(Eq(a, b), Lt(a, b)), Le(a, b)), (Tuple(Lt(b, a), Lt(a, b)), Ne(a, b)), (Tuple(Lt(b, a), Ne(a, b)), Ne(a, b)), (Tuple(Le(a, b), Lt(a, b)), Le(a, b)), (Tuple(Eq(a, b), Ne(a, c)), ITE(Eq(b, c), true, Ne(a, c))), (Tuple(Ne(a, b), Ne(a, c)), ITE(Eq(b, c), Ne(a, b), true)), (Tuple(Le(b, a), Le(c, a)), Ge(a, Min(b, c))), (Tuple(Le(b, a), Lt(c, a)), ITE(b > c, Lt(c, a), Le(b, a))), (Tuple(Lt(b, a), Lt(c, a)), Gt(a, Min(b, c))), (Tuple(Le(a, b), Le(a, c)), Le(a, Max(b, c))), (Tuple(Le(a, b), Lt(a, c)), ITE(b >= c, Le(a, b), Lt(a, c))), (Tuple(Lt(a, b), Lt(a, c)), Lt(a, Max(b, c))), (Tuple(Le(a, b), Le(c, a)), ITE(b >= c, true, Or(Le(a, b), Ge(a, c)))), (Tuple(Le(c, a), Le(a, b)), ITE(b >= c, true, Or(Le(a, b), Ge(a, c)))), (Tuple(Lt(a, b), Lt(c, a)), ITE(b > c, true, Or(Lt(a, b), Gt(a, c)))), (Tuple(Lt(c, a), Lt(a, b)), ITE(b > c, true, Or(Lt(a, b), Gt(a, c)))), (Tuple(Le(a, b), Lt(c, a)), ITE(b >= c, true, Or(Le(a, b), Gt(a, c)))), (Tuple(Le(c, a), Lt(a, b)), ITE(b >= c, true, Or(Lt(a, b), Ge(a, c)))), (Tuple(Lt(b, a), Lt(a, -b)), ITE(b >= 0, Gt(Abs(a), b), true)), (Tuple(Le(b, a), Le(a, -b)), ITE(b > 0, Ge(Abs(a), b), true)))_matchers_or)()
_simplify_patterns_xor = (lambda : Min = MinMax = Maximport sympy.functions.elementary.miscellaneousWild = Wildimport sympy.coreEq = EqNe = NeGe = GeGt = GtLe = LeLt = Ltimport sympy.core.relationala = Wild('a')b = Wild('b')c = Wild('c')_matchers_xor = ((Tuple(Eq(a, b), Le(a, b)), Lt(a, b)), (Tuple(Eq(a, b), Lt(a, b)), Le(a, b)), (Tuple(Le(a, b), Lt(a, b)), Eq(a, b)), (Tuple(Le(a, b), Le(b, a)), Ne(a, b)), (Tuple(Le(b, a), Ne(a, b)), Le(a, b)), (Tuple(Lt(b, a), Ne(a, b)), Lt(a, b)), (Tuple(Le(b, a), Le(c, a)), And(Ge(a, Min(b, c)), Lt(a, Max(b, c)))), (Tuple(Le(b, a), Lt(c, a)), ITE(b > c, And(Gt(a, c), Lt(a, b)), And(Ge(a, b), Le(a, c)))), (Tuple(Lt(b, a), Lt(c, a)), And(Gt(a, Min(b, c)), Le(a, Max(b, c)))), (Tuple(Le(a, b), Le(a, c)), And(Le(a, Max(b, c)), Gt(a, Min(b, c)))), (Tuple(Le(a, b), Lt(a, c)), ITE(b < c, And(Lt(a, c), Gt(a, b)), And(Le(a, b), Ge(a, c)))), (Tuple(Lt(a, b), Lt(a, c)), And(Lt(a, Max(b, c)), Ge(a, Min(b, c)))))_matchers_xor)()

def simplify_univariate(expr):
    '''return a simplified version of univariate boolean expression, else ``expr``'''
    Piecewise = Piecewise
    import sympy.functions.elementary.piecewise
    Eq = Eq
    Ne = Ne
    import sympy.core.relational
    if not isinstance(expr, BooleanFunction):
        return expr
    if None.atoms(Eq, Ne):
        return expr
    c = None
    free = c.free_symbols
    if len(free) != 1:
        return c
    x = None.pop()
    (ok, i) = Piecewise((0, c), evaluate = False)._intervals(x, err_on_Eq = True)
    if not ok:
        return c
    if not None:
        return false
    args = None
# WARNING: Decompyle incomplete

BooleanGates = (And, Or, Xor, Nand, Nor, Not, Xnor, ITE)

def gateinputcount(expr):
    '''
    Return the total number of inputs for the logic gates realizing the
    Boolean expression.

    Returns
    =======

    int
        Number of gate inputs

    Note
    ====

    Not all Boolean functions count as gate here, only those that are
    considered to be standard gates. These are: :py:class:`~.And`,
    :py:class:`~.Or`, :py:class:`~.Xor`, :py:class:`~.Not`, and
    :py:class:`~.ITE` (multiplexer). :py:class:`~.Nand`, :py:class:`~.Nor`,
    and :py:class:`~.Xnor` will be evaluated to ``Not(And())`` etc.

    Examples
    ========

    >>> from sympy.logic import And, Or, Nand, Not, gateinputcount
    >>> from sympy.abc import x, y, z
    >>> expr = And(x, y)
    >>> gateinputcount(expr)
    2
    >>> gateinputcount(Or(expr, z))
    4

    Note that ``Nand`` is automatically evaluated to ``Not(And())`` so

    >>> gateinputcount(Nand(x, y, z))
    4
    >>> gateinputcount(Not(And(x, y, z)))
    4

    Although this can be avoided by using ``evaluate=False``

    >>> gateinputcount(Nand(x, y, z, evaluate=False))
    3

    Also note that a comparison will count as a Boolean variable:

    >>> gateinputcount(And(x > z, y >= 2))
    2

    As will a symbol:
    >>> gateinputcount(x)
    0

    '''
    if not isinstance(expr, Boolean):
        raise TypeError('Expression must be Boolean')
    if isinstance(expr, BooleanGates):
        return sum + (lambda .0: pass# WARNING: Decompyle incomplete
)(expr.args())
