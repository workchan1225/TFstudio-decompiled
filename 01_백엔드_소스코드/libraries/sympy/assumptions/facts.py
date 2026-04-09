# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: facts.pyc (Python 3.11)

'''
Known facts in assumptions module.

This module defines the facts between unary predicates in ``get_known_facts()``,
and supports functions to generate the contents in
``sympy.assumptions.ask_generated`` file.
'''
from sympy.assumptions.ask import Q
from sympy.assumptions.assume import AppliedPredicate
from sympy.core.cache import cacheit
from sympy.core.symbol import Symbol
from sympy.logic.boolalg import to_cnf, And, Not, Implies, Equivalent, Exclusive
from sympy.logic.inference import satisfiable
get_composite_predicates = (lambda : {
Q.complex: Q.algebraic | Q.transcendental,
Q.extended_nonnegative: Q.zero | Q.positive | Q.positive_infinite,
Q.extended_nonpositive: Q.negative_infinite | Q.negative | Q.zero,
Q.extended_nonzero: Q.negative_infinite | Q.negative | Q.positive | Q.positive_infinite,
Q.extended_negative: Q.negative | Q.negative_infinite,
Q.extended_positive: Q.positive | Q.positive_infinite,
Q.extended_real: Q.negative_infinite | Q.negative | Q.zero | Q.positive | Q.positive_infinite,
Q.nonnegative: Q.zero | Q.positive,
Q.nonzero: Q.negative | Q.positive,
Q.nonpositive: Q.negative | Q.zero,
Q.integer: Q.even | Q.odd,
Q.real: Q.negative | Q.zero | Q.positive })()
get_known_facts = (lambda x = (None,): pass# WARNING: Decompyle incomplete
)()
get_number_facts = (lambda x = (None,): pass# WARNING: Decompyle incomplete
)()
get_matrix_facts = (lambda x = (None,): pass# WARNING: Decompyle incomplete
)()

def generate_known_facts_dict(keys, fact):
    '''
    Computes and returns a dictionary which contains the relations between
    unary predicates.

    Each key is a predicate, and item is two groups of predicates.
    First group contains the predicates which are implied by the key, and
    second group contains the predicates which are rejected by the key.

    All predicates in *keys* and *fact* must be unary and have same placeholder
    symbol.

    Parameters
    ==========

    keys : list of AppliedPredicate instances.

    fact : Fact between predicates in conjugated normal form.

    Examples
    ========

    >>> from sympy import Q, And, Implies
    >>> from sympy.assumptions.facts import generate_known_facts_dict
    >>> from sympy.abc import x
    >>> keys = [Q.even(x), Q.odd(x), Q.zero(x)]
    >>> fact = And(Implies(Q.even(x), ~Q.odd(x)),
    ...     Implies(Q.zero(x), Q.even(x)))
    >>> generate_known_facts_dict(keys, fact)
    {Q.even: ({Q.even}, {Q.odd}),
     Q.odd: ({Q.odd}, {Q.even, Q.zero}),
     Q.zero: ({Q.even, Q.zero}, {Q.odd})}
    '''
    fact_cnf = to_cnf(fact)
    mapping = single_fact_lookup(keys, fact_cnf)
    ret = { }
    for key, value in mapping.items():
        implied = set()
        rejected = set()
        for expr in value:
            if isinstance(expr, AppliedPredicate):
                implied.add(expr.function)
                continue
            if isinstance(expr, Not):
                pred = expr.args[0]
                rejected.add(pred.function)
            ret[key.function] = (implied, rejected)
            return ret

get_known_facts_keys = (lambda : exclude = {
Q.eq,
Q.ne,
Q.gt,
Q.lt,
Q.ge,
Q.le}result = []for attr in Q.__class__.__dict__:
if attr.startswith('__'):
continuepred = getattr(Q, attr)if pred in exclude:
continueresult.append(pred)result)()

def single_fact_lookup(known_facts_keys, known_facts_cnf):
    mapping = { }
    for key in known_facts_keys:
        mapping[key] = {
            key}
        for other_key in known_facts_keys:
            if other_key != key:
                if ask_full_inference(other_key, key, known_facts_cnf):
                    mapping[key].add(other_key)
                if ask_full_inference(~other_key, key, known_facts_cnf):
                    mapping[key].add(~other_key)
            return mapping


def ask_full_inference(proposition, assumptions, known_facts_cnf):
    '''
    Method for inferring properties about objects.

    '''
    if not satisfiable(And(known_facts_cnf, assumptions, proposition)):
        return False
    if not None(And(known_facts_cnf, assumptions, Not(proposition))):
        return True
