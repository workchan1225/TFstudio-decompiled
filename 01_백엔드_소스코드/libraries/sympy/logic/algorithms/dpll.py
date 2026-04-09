# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dpll.pyc (Python 3.11)

'''Implementation of DPLL algorithm

Further improvements: eliminate calls to pl_true, implement branching rules,
efficient unit propagation.

References:
  - https://en.wikipedia.org/wiki/DPLL_algorithm
  - https://www.researchgate.net/publication/242384772_Implementations_of_the_DPLL_Algorithm
'''
from sympy.core.sorting import default_sort_key
from sympy.logic.boolalg import Or, Not, conjuncts, disjuncts, to_cnf, to_int_repr, _find_predicates
from sympy.assumptions.cnf import CNF
from sympy.logic.inference import pl_true, literal_symbol

def dpll_satisfiable(expr):
    '''
    Check satisfiability of a propositional sentence.
    It returns a model rather than True when it succeeds

    >>> from sympy.abc import A, B
    >>> from sympy.logic.algorithms.dpll import dpll_satisfiable
    >>> dpll_satisfiable(A & ~B)
    {A: True, B: False}
    >>> dpll_satisfiable(A & ~A)
    False

    '''
    if not isinstance(expr, CNF):
        clauses = conjuncts(to_cnf(expr))
    else:
        clauses = expr.clauses
    if False in clauses:
        return False
    symbols = None(_find_predicates(expr), key = default_sort_key)
    symbols_int_repr = set(range(1, len(symbols) + 1))
    clauses_int_repr = to_int_repr(clauses, symbols)
    result = dpll_int_repr(clauses_int_repr, symbols_int_repr, { })
    if not result:
        return result
    output = None
    for key in result:
        output.update({
            symbols[key - 1]: result[key] })
        return output


def dpll(clauses, symbols, model):
    '''
    Compute satisfiability in a partial model.
    Clauses is an array of conjuncts.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import dpll
    >>> dpll([A, B, D], [A, B], {D: False})
    False

    '''
    (P, value) = find_unit_clause(clauses, model)
# WARNING: Decompyle incomplete


def dpll_int_repr(clauses, symbols, model):
    '''
    Compute satisfiability in a partial model.
    Arguments are expected to be in integer representation

    >>> from sympy.logic.algorithms.dpll import dpll_int_repr
    >>> dpll_int_repr([{1}, {2}, {3}], {1, 2}, {3: False})
    False

    '''
    (P, value) = find_unit_clause_int_repr(clauses, model)
# WARNING: Decompyle incomplete


def pl_true_int_repr(clause, model = ({ },)):
    '''
    Lightweight version of pl_true.
    Argument clause represents the set of args of an Or clause. This is used
    inside dpll_int_repr, it is not meant to be used directly.

    >>> from sympy.logic.algorithms.dpll import pl_true_int_repr
    >>> pl_true_int_repr({1, 2}, {1: False})
    >>> pl_true_int_repr({1, 2}, {1: False, 2: False})
    False

    '''
    result = False
# WARNING: Decompyle incomplete


def unit_propagate(clauses, symbol):
    '''
    Returns an equivalent set of clauses
    If a set of clauses contains the unit clause l, the other clauses are
    simplified by the application of the two following rules:

      1. every clause containing l is removed
      2. in every clause that contains ~l this literal is deleted

    Arguments are expected to be in CNF.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import unit_propagate
    >>> unit_propagate([A | B, D | ~B, B], B)
    [D, B]

    '''
    pass
# WARNING: Decompyle incomplete


def unit_propagate_int_repr(clauses, s):
    '''
    Same as unit_propagate, but arguments are expected to be in integer
    representation

    >>> from sympy.logic.algorithms.dpll import unit_propagate_int_repr
    >>> unit_propagate_int_repr([{1, 2}, {3, -2}, {2}], 2)
    [{3}]

    '''
    pass
# WARNING: Decompyle incomplete


def find_pure_symbol(symbols, unknown_clauses):
    '''
    Find a symbol and its value if it appears only as a positive literal
    (or only as a negative) in clauses.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import find_pure_symbol
    >>> find_pure_symbol([A, B, D], [A|~B,~B|~D,D|A])
    (A, True)

    '''
    for sym in symbols:
        (found_pos, found_neg) = (False, False)
        for c in unknown_clauses:
            if found_pos and sym in disjuncts(c):
                found_pos = True
            if found_neg and Not(sym) in disjuncts(c):
                found_neg = True
            if found_pos != found_neg:
                
                return None, (sym, found_pos)
            return (None, None)


def find_pure_symbol_int_repr(symbols, unknown_clauses):
    '''
    Same as find_pure_symbol, but arguments are expected
    to be in integer representation

    >>> from sympy.logic.algorithms.dpll import find_pure_symbol_int_repr
    >>> find_pure_symbol_int_repr({1,2,3},
    ...     [{1, -2}, {-2, -3}, {3, 1}])
    (1, True)

    '''
    pass
# WARNING: Decompyle incomplete


def find_unit_clause(clauses, model):
    '''
    A unit clause has only 1 variable that is not bound in the model.

    >>> from sympy.abc import A, B, D
    >>> from sympy.logic.algorithms.dpll import find_unit_clause
    >>> find_unit_clause([A | B | D, B | ~D, A | ~B], {A:True})
    (B, False)

    '''
    for clause in clauses:
        num_not_in_model = 0
        for literal in disjuncts(clause):
            sym = literal_symbol(literal)
            if sym not in model:
                num_not_in_model += 1
                value = not isinstance(literal, Not)
                P = sym
            if num_not_in_model == 1:
                
                return None, (P, value)
            return (None, None)


def find_unit_clause_int_repr(clauses, model):
    '''
    Same as find_unit_clause, but arguments are expected to be in
    integer representation.

    >>> from sympy.logic.algorithms.dpll import find_unit_clause_int_repr
    >>> find_unit_clause_int_repr([{1, 2, 3},
    ...     {2, -3}, {1, -2}], {1: True})
    (2, False)

    '''
    bound = (lambda .0: pass# WARNING: Decompyle incomplete
) | model()
    for clause in clauses:
        unbound = clause - bound
        if len(unbound) == 1:
            p = unbound.pop()
            if p < 0:
                
                return set(model), (-p, False)
            
            return None, (set(model), True)
        return (None, None)
