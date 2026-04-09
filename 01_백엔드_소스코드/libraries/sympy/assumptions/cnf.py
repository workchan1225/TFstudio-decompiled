# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cnf.pyc (Python 3.11)

'''
The classes used here are for the internal use of assumptions system
only and should not be used anywhere else as these do not possess the
signatures common to SymPy objects. For general use of logic constructs
please refer to sympy.logic classes And, Or, Not, etc.
'''
from itertools import combinations, product, zip_longest
from sympy.assumptions.assume import AppliedPredicate, Predicate
from sympy.core.relational import Eq, Ne, Gt, Lt, Ge, Le
from sympy.core.singleton import S
from sympy.logic.boolalg import Or, And, Not, Xnor
from sympy.logic.boolalg import Equivalent, ITE, Implies, Nand, Nor, Xor

class Literal:
    pass
# WARNING: Decompyle incomplete


class OR:
    '''
    A low-level implementation for Or
    '''
    
    def __init__(self, *args):
        self._args = args

    args = (lambda self: sorted(self._args, key = str))()
    
    def rcall(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def __invert__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __hash__(self):
        return hash((type(self).__name__,) + tuple(self.args))

    
    def __eq__(self, other):
        return self.args == other.args

    
    def __str__(self):
        s = ' | '.join + (lambda .0: [ str(arg) for arg in .0 ])(self.args()) + ')'
        return s

    __repr__ = __str__


class AND:
    '''
    A low-level implementation for And
    '''
    
    def __init__(self, *args):
        self._args = args

    
    def __invert__(self):
        pass
    # WARNING: Decompyle incomplete

    args = (lambda self: sorted(self._args, key = str))()
    
    def rcall(self, expr):
        pass
    # WARNING: Decompyle incomplete

    
    def __hash__(self):
        return hash((type(self).__name__,) + tuple(self.args))

    
    def __eq__(self, other):
        return self.args == other.args

    
    def __str__(self):
        s = ' & '.join + (lambda .0: [ str(arg) for arg in .0 ])(self.args()) + ')'
        return s

    __repr__ = __str__


def to_NNF(expr, composite_map = (None,)):
    '''
    Generates the Negation Normal Form of any boolean expression in terms
    of AND, OR, and Literal objects.

    Examples
    ========

    >>> from sympy import Q, Eq
    >>> from sympy.assumptions.cnf import to_NNF
    >>> from sympy.abc import x, y
    >>> expr = Q.even(x) & ~Q.positive(x)
    >>> to_NNF(expr)
    (Literal(Q.even(x), False) & Literal(Q.positive(x), True))

    Supported boolean objects are converted to corresponding predicates.

    >>> to_NNF(Eq(x, y))
    Literal(Q.eq(x, y), False)

    If ``composite_map`` argument is given, ``to_NNF`` decomposes the
    specified predicate into a combination of primitive predicates.

    >>> cmap = {Q.nonpositive: Q.negative | Q.zero}
    >>> to_NNF(Q.nonpositive, cmap)
    (Literal(Q.negative, False) | Literal(Q.zero, False))
    >>> to_NNF(Q.nonpositive(x), cmap)
    (Literal(Q.negative(x), False) | Literal(Q.zero(x), False))
    '''
    pass
# WARNING: Decompyle incomplete


def distribute_AND_over_OR(expr):
    '''
    Distributes AND over OR in the NNF expression.
    Returns the result( Conjunctive Normal Form of expression)
    as a CNF object.
    '''
    if not isinstance(expr, (AND, OR)):
        tmp = set()
        tmp.add(frozenset((expr,)))
        return CNF(tmp)
# WARNING: Decompyle incomplete


class CNF:
    '''
    Class to represent CNF of a Boolean expression.
    Consists of set of clauses, which themselves are stored as
    frozenset of Literal objects.

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.abc import x
    >>> cnf = CNF.from_prop(Q.real(x) & ~Q.zero(x))
    >>> cnf.clauses
    {frozenset({Literal(Q.zero(x), True)}),
    frozenset({Literal(Q.negative(x), False),
    Literal(Q.positive(x), False), Literal(Q.zero(x), False)})}
    '''
    
    def __init__(self, clauses = (None,)):
        if not clauses:
            clauses = set()
        self.clauses = clauses

    
    def add(self, prop):
        clauses = CNF.to_CNF(prop).clauses
        self.add_clauses(clauses)

    
    def __str__(self):
        s = (lambda .0: [ ' | '.join + (lambda .0: [ str(lit) for lit in .0 ])(clause()) + ')' for clause in .0 ]
)(self.clauses())
        return s

    
    def extend(self, props):
        for p in props:
            self.add(p)
            return self

    
    def copy(self):
        return CNF(set(self.clauses))

    
    def add_clauses(self, clauses):
        pass

    from_prop = (lambda cls, prop: res = cls()res.add(prop)res)()
    
    def __iand__(self, other):
        self.add_clauses(other.clauses)
        return self

    
    def all_predicates(self):
        predicates = set()
        for c in self.clauses:
            (lambda .0: pass# WARNING: Decompyle incomplete
) |= c()
            return predicates

    
    def _or(self, cnf):
        clauses = set()
        for a, b in product(self.clauses, cnf.clauses):
            tmp = set(a)
            tmp.update(b)
            clauses.add(frozenset(tmp))
            return CNF(clauses)

    
    def _and(self, cnf):
        clauses = self.clauses.union(cnf.clauses)
        return CNF(clauses)

    
    def _not(self):
        clss = list(self.clauses)
        ll = clss[-1]()
        ll = CNF(ll)
        for rest in clss[:-1]:
            p = rest()
            ll = ll._or(CNF(p))
            return ll

    
    def rcall(self, expr):
        pass
    # WARNING: Decompyle incomplete

    all_or = (lambda cls: b = cnfs[0].copy()for rest in cnfs[1:]:
b = b._or(rest)b)()
    all_and = (lambda cls: b = cnfs[0].copy()for rest in cnfs[1:]:
b = b._and(rest)b)()
    to_CNF = (lambda cls, expr: get_composite_predicates = get_composite_predicatesimport sympy.assumptions.factsexpr = to_NNF(expr, get_composite_predicates())expr = distribute_AND_over_OR(expr)expr)()
    CNF_to_cnf = (lambda cls, cnf: pass# WARNING: Decompyle incomplete
)()


class EncodedCNF:
    '''
    Class for encoding the CNF expression.
    '''
    
    def __init__(self, data, encoding = (None, None)):
        if not data and encoding:
            data = []
            encoding = { }
        self.data = data
        self.encoding = encoding
        self._symbols = list(encoding.keys())

    
    def from_cnf(self, cnf):
        pass
    # WARNING: Decompyle incomplete

    symbols = (lambda self: self._symbols)()
    variables = (lambda self: range(1, len(self._symbols) + 1))()
    
    def copy(self):
        new_data = self.data()
        return EncodedCNF(new_data, dict(self.encoding))

    
    def add_prop(self, prop):
        cnf = CNF.from_prop(prop)
        self.add_from_cnf(cnf)

    
    def add_from_cnf(self, cnf):
        pass
    # WARNING: Decompyle incomplete

    
    def encode_arg(self, arg):
        literal = arg.lit
        value = self.encoding.get(literal, None)
    # WARNING: Decompyle incomplete

    
    def encode(self, clause):
        pass
    # WARNING: Decompyle incomplete
