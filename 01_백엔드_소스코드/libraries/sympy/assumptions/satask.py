# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: satask.pyc (Python 3.11)

'''
Module to evaluate the proposition with assumptions using SAT algorithm.
'''
from sympy.core.singleton import S
from sympy.core.symbol import Symbol
from sympy.core.kind import NumberKind, UndefinedKind
from sympy.assumptions.ask_generated import get_all_known_matrix_facts, get_all_known_number_facts
from sympy.assumptions.assume import global_assumptions, AppliedPredicate
from sympy.assumptions.sathandlers import class_fact_registry
from sympy.core import oo
from sympy.logic.inference import satisfiable
from sympy.assumptions.cnf import CNF, EncodedCNF
from sympy.matrices.kind import MatrixKind

def satask(proposition, assumptions, context, use_known_facts, iterations = (True, global_assumptions, True, oo)):
    '''
    Function to evaluate the proposition with assumptions using SAT algorithm.

    This function extracts every fact relevant to the expressions composing
    proposition and assumptions. For example, if a predicate containing
    ``Abs(x)`` is proposed, then ``Q.zero(Abs(x)) | Q.positive(Abs(x))``
    will be found and passed to SAT solver because ``Q.nonnegative`` is
    registered as a fact for ``Abs``.

    Proposition is evaluated to ``True`` or ``False`` if the truth value can be
    determined. If not, ``None`` is returned.

    Parameters
    ==========

    proposition : Any boolean expression.
        Proposition which will be evaluated to boolean value.

    assumptions : Any boolean expression, optional.
        Local assumptions to evaluate the *proposition*.

    context : AssumptionsContext, optional.
        Default assumptions to evaluate the *proposition*. By default,
        this is ``sympy.assumptions.global_assumptions`` variable.

    use_known_facts : bool, optional.
        If ``True``, facts from ``sympy.assumptions.ask_generated``
        module are passed to SAT solver as well.

    iterations : int, optional.
        Number of times that relevant facts are recursively extracted.
        Default is infinite times until no new fact is found.

    Returns
    =======

    ``True``, ``False``, or ``None``

    Examples
    ========

    >>> from sympy import Abs, Q
    >>> from sympy.assumptions.satask import satask
    >>> from sympy.abc import x
    >>> satask(Q.zero(Abs(x)), Q.zero(x))
    True

    '''
    props = CNF.from_prop(proposition)
    _props = CNF.from_prop(~proposition)
    assumptions = CNF.from_prop(assumptions)
    context_cnf = CNF()
    if context:
        context_cnf = context_cnf.extend(context)
    sat = get_all_relevant_facts(props, assumptions, context_cnf, use_known_facts = use_known_facts, iterations = iterations)
    sat.add_from_cnf(assumptions)
    if context:
        sat.add_from_cnf(context_cnf)
    return check_satisfiability(props, _props, sat)


def check_satisfiability(prop, _prop, factbase):
    sat_true = factbase.copy()
    sat_false = factbase.copy()
    sat_true.add_from_cnf(prop)
    sat_false.add_from_cnf(_prop)
    can_be_true = satisfiable(sat_true)
    can_be_false = satisfiable(sat_false)
    if can_be_true and can_be_false:
        return None
    if not None and can_be_false:
        return True
    if None and can_be_false:
        return False
    if not None or can_be_false:
        raise ValueError('Inconsistent assumptions')
    return None


def extract_predargs(proposition, assumptions, context = (None, None)):
    '''
    Extract every expression in the argument of predicates from *proposition*,
    *assumptions* and *context*.

    Parameters
    ==========

    proposition : sympy.assumptions.cnf.CNF

    assumptions : sympy.assumptions.cnf.CNF, optional.

    context : sympy.assumptions.cnf.CNF, optional.
        CNF generated from assumptions context.

    Examples
    ========

    >>> from sympy import Q, Abs
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.assumptions.satask import extract_predargs
    >>> from sympy.abc import x, y
    >>> props = CNF.from_prop(Q.zero(Abs(x*y)))
    >>> assump = CNF.from_prop(Q.zero(x) & Q.zero(y))
    >>> extract_predargs(props, assump)
    {x, y, Abs(x*y)}

    '''
    pass
# WARNING: Decompyle incomplete


def find_symbols(pred):
    '''
    Find every :obj:`~.Symbol` in *pred*.

    Parameters
    ==========

    pred : sympy.assumptions.cnf.CNF, or any Expr.

    '''
    if isinstance(pred, CNF):
        symbols = set()
        for a in pred.all_predicates():
            symbols |= find_symbols(a)
            return symbols
            return pred.atoms(Symbol)


def get_relevant_clsfacts(exprs, relevant_facts = (None,)):
    """
    Extract relevant facts from the items in *exprs*. Facts are defined in
    ``assumptions.sathandlers`` module.

    This function is recursively called by ``get_all_relevant_facts()``.

    Parameters
    ==========

    exprs : set
        Expressions whose relevant facts are searched.

    relevant_facts : sympy.assumptions.cnf.CNF, optional.
        Pre-discovered relevant facts.

    Returns
    =======

    exprs : set
        Candidates for next relevant fact searching.

    relevant_facts : sympy.assumptions.cnf.CNF
        Updated relevant facts.

    Examples
    ========

    Here, we will see how facts relevant to ``Abs(x*y)`` are recursively
    extracted. On the first run, set containing the expression is passed
    without pre-discovered relevant facts. The result is a set containing
    candidates for next run, and ``CNF()`` instance containing facts
    which are relevant to ``Abs`` and its argument.

    >>> from sympy import Abs
    >>> from sympy.assumptions.satask import get_relevant_clsfacts
    >>> from sympy.abc import x, y
    >>> exprs = {Abs(x*y)}
    >>> exprs, facts = get_relevant_clsfacts(exprs)
    >>> exprs
    {x*y}
    >>> facts.clauses #doctest: +SKIP
    {frozenset({Literal(Q.odd(Abs(x*y)), False), Literal(Q.odd(x*y), True)}),
    frozenset({Literal(Q.zero(Abs(x*y)), False), Literal(Q.zero(x*y), True)}),
    frozenset({Literal(Q.even(Abs(x*y)), False), Literal(Q.even(x*y), True)}),
    frozenset({Literal(Q.zero(Abs(x*y)), True), Literal(Q.zero(x*y), False)}),
    frozenset({Literal(Q.even(Abs(x*y)), False),
                Literal(Q.odd(Abs(x*y)), False),
                Literal(Q.odd(x*y), True)}),
    frozenset({Literal(Q.even(Abs(x*y)), False),
                Literal(Q.even(x*y), True),
                Literal(Q.odd(Abs(x*y)), False)}),
    frozenset({Literal(Q.positive(Abs(x*y)), False),
                Literal(Q.zero(Abs(x*y)), False)})}

    We pass the first run's results to the second run, and get the expressions
    for next run and updated facts.

    >>> exprs, facts = get_relevant_clsfacts(exprs, relevant_facts=facts)
    >>> exprs
    {x, y}

    On final run, no more candidate is returned thus we know that all
    relevant facts are successfully retrieved.

    >>> exprs, facts = get_relevant_clsfacts(exprs, relevant_facts=facts)
    >>> exprs
    set()

    """
    if not relevant_facts:
        relevant_facts = CNF()
    newexprs = set()
    for expr in exprs:
        for fact in class_fact_registry(expr):
            newfact = CNF.to_CNF(fact)
            relevant_facts = relevant_facts._and(newfact)
            for key in newfact.all_predicates():
                if isinstance(key, AppliedPredicate):
                    newexprs |= set(key.arguments)
                return (newexprs - exprs, relevant_facts)


def get_all_relevant_facts(proposition, assumptions, context, use_known_facts, iterations = (True, oo)):
    '''
    Extract all relevant facts from *proposition* and *assumptions*.

    This function extracts the facts by recursively calling
    ``get_relevant_clsfacts()``. Extracted facts are converted to
    ``EncodedCNF`` and returned.

    Parameters
    ==========

    proposition : sympy.assumptions.cnf.CNF
        CNF generated from proposition expression.

    assumptions : sympy.assumptions.cnf.CNF
        CNF generated from assumption expression.

    context : sympy.assumptions.cnf.CNF
        CNF generated from assumptions context.

    use_known_facts : bool, optional.
        If ``True``, facts from ``sympy.assumptions.ask_generated``
        module are encoded as well.

    iterations : int, optional.
        Number of times that relevant facts are recursively extracted.
        Default is infinite times until no new fact is found.

    Returns
    =======

    sympy.assumptions.cnf.EncodedCNF

    Examples
    ========

    >>> from sympy import Q
    >>> from sympy.assumptions.cnf import CNF
    >>> from sympy.assumptions.satask import get_all_relevant_facts
    >>> from sympy.abc import x, y
    >>> props = CNF.from_prop(Q.nonzero(x*y))
    >>> assump = CNF.from_prop(Q.nonzero(x))
    >>> context = CNF.from_prop(Q.nonzero(y))
    >>> get_all_relevant_facts(props, assump, context) #doctest: +SKIP
    <sympy.assumptions.cnf.EncodedCNF at 0x7f09faa6ccd0>

    '''
    pass
# WARNING: Decompyle incomplete
