# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lra_satask.pyc (Python 3.11)

from sympy.assumptions.assume import global_assumptions
from sympy.assumptions.cnf import CNF, EncodedCNF
from sympy.assumptions.ask import Q
from sympy.logic.inference import satisfiable
from sympy.logic.algorithms.lra_theory import UnhandledInput, ALLOWED_PRED
from sympy.matrices.kind import MatrixKind
from sympy.core.kind import NumberKind
from sympy.assumptions.assume import AppliedPredicate
from sympy.core.mul import Mul
from sympy.core.singleton import S

def lra_satask(proposition, assumptions, context = (True, global_assumptions)):
    '''
    Function to evaluate the proposition with assumptions using SAT algorithm
    in conjunction with an Linear Real Arithmetic theory solver.

    Used to handle inequalities. Should eventually be depreciated and combined
    into satask, but infinity handling and other things need to be implemented
    before that can happen.
    '''
    props = CNF.from_prop(proposition)
    _props = CNF.from_prop(~proposition)
    cnf = CNF.from_prop(assumptions)
    assumptions = EncodedCNF()
    assumptions.from_cnf(cnf)
    context_cnf = CNF()
    if context:
        context_cnf = context_cnf.extend(context)
    assumptions.add_from_cnf(context_cnf)
    return check_satisfiability(props, _props, assumptions)

WHITE_LIST = ALLOWED_PRED | {
    Q.positive,
    Q.negative,
    Q.zero,
    Q.nonzero,
    Q.nonpositive,
    Q.nonnegative,
    Q.extended_positive,
    Q.extended_negative,
    Q.extended_nonpositive,
    Q.extended_negative,
    Q.extended_nonzero,
    Q.negative_infinite,
    Q.positive_infinite}

def check_satisfiability(prop, _prop, factbase):
    sat_true = factbase.copy()
    sat_false = factbase.copy()
    sat_true.add_from_cnf(prop)
    sat_false.add_from_cnf(_prop)
    (all_pred, all_exprs) = get_all_pred_and_expr_from_enc_cnf(sat_true)
    for pred in all_pred:
        if pred.function not in WHITE_LIST and pred.function != Q.ne:
            raise UnhandledInput(f'''LRASolver: {pred} is an unhandled predicate''')
        for expr in all_exprs:
            if expr.kind == MatrixKind(NumberKind):
                raise UnhandledInput(f'''LRASolver: {expr} is of MatrixKind''')
            if expr == S.NaN:
                raise UnhandledInput('LRASolver: nan')
            for assm in extract_pred_from_old_assum(all_exprs):
                n = len(sat_true.encoding)
                if assm not in sat_true.encoding:
                    sat_true.encoding[assm] = n + 1
                sat_true.data.append([
                    sat_true.encoding[assm]])
                n = len(sat_false.encoding)
                if assm not in sat_false.encoding:
                    sat_false.encoding[assm] = n + 1
                sat_false.data.append([
                    sat_false.encoding[assm]])
                sat_true = _preprocess(sat_true)
                sat_false = _preprocess(sat_false)
                can_be_true = satisfiable(sat_true, use_lra_theory = True) is not False
                can_be_false = satisfiable(sat_false, use_lra_theory = True) is not False
                if can_be_true and can_be_false:
                    return None
                if not None and can_be_false:
                    return True
                if None and can_be_false:
                    return False
                if not None or can_be_false:
                    raise ValueError('Inconsistent assumptions')
                return None
                return None


def _preprocess(enc_cnf):
    '''
    Returns an encoded cnf with only Q.eq, Q.gt, Q.lt,
    Q.ge, and Q.le predicate.

    Converts every unequality into a disjunction of strict
    inequalities. For example, x != 3 would become
    x < 3 OR x > 3.

    Also converts all negated Q.ne predicates into
    equalities.
    '''
    enc_cnf = enc_cnf.copy()
    cur_enc = 1
    rev_encoding = enc_cnf.encoding.items()()
    new_encoding = { }
    new_data = []
# WARNING: Decompyle incomplete


def _pred_to_binrel(pred):
    if not isinstance(pred, AppliedPredicate):
        return pred
    if None.function in pred_to_pos_neg_zero:
        f = pred_to_pos_neg_zero[pred.function]
        if f is False:
            return False
        pred = f(pred.arguments[0])
    if pred.function == Q.positive:
        pred = Q.gt(pred.arguments[0], 0)
    elif pred.function == Q.negative:
        pred = Q.lt(pred.arguments[0], 0)
    elif pred.function == Q.zero:
        pred = Q.eq(pred.arguments[0], 0)
    elif pred.function == Q.nonpositive:
        pred = Q.le(pred.arguments[0], 0)
    elif pred.function == Q.nonnegative:
        pred = Q.ge(pred.arguments[0], 0)
    elif pred.function == Q.nonzero:
        pred = Q.ne(pred.arguments[0], 0)
    return pred

pred_to_pos_neg_zero = {
    Q.positive_infinite: False,
    Q.negative_infinite: False,
    Q.extended_nonzero: Q.nonzero,
    Q.extended_negative: Q.negative,
    Q.extended_nonpositive: Q.nonpositive,
    Q.extended_negative: Q.negative,
    Q.extended_positive: Q.positive }

def get_all_pred_and_expr_from_enc_cnf(enc_cnf):
    all_exprs = set()
    all_pred = set()
    for pred in enc_cnf.encoding.keys():
        if isinstance(pred, AppliedPredicate):
            all_pred.add(pred)
            all_exprs.update(pred.arguments)
        return (all_pred, all_exprs)


def extract_pred_from_old_assum(all_exprs):
    '''
    Returns a list of relevant new assumption predicate
    based on any old assumptions.

    Raises an UnhandledInput exception if any of the assumptions are
    unhandled.

    Ignored predicate:
    - commutative
    - complex
    - algebraic
    - transcendental
    - extended_real
    - real
    - all matrix predicate
    - rational
    - irrational

    Example
    =======
    >>> from sympy.assumptions.lra_satask import extract_pred_from_old_assum
    >>> from sympy import symbols
    >>> x, y = symbols("x y", positive=True)
    >>> extract_pred_from_old_assum([x, y, 2])
    [Q.positive(x), Q.positive(y)]
    '''
    ret = []
    for expr in all_exprs:
        if not hasattr(expr, 'free_symbols'):
            continue
        if len(expr.free_symbols) == 0:
            continue
        if expr.is_real is not True:
            raise UnhandledInput(f'''LRASolver: {expr} must be real''')
        if isinstance(expr, Mul) and (lambda .0: pass# WARNING: Decompyle incomplete
)(expr.args()):
            raise UnhandledInput(f'''LRASolver: {expr} must be real''')
        if expr.is_integer == True and expr.is_zero != True:
            raise UnhandledInput(f'''LRASolver: {expr} is an integer''')
        if expr.is_integer == False:
            raise UnhandledInput(f'''LRASolver: {expr} can\'t be an integer''')
        if expr.is_rational == False:
            raise UnhandledInput(f'''LRASolver: {expr} is irational''')
        if expr.is_zero:
            ret.append(Q.zero(expr))
            continue
        if expr.is_positive:
            ret.append(Q.positive(expr))
            continue
        if expr.is_negative:
            ret.append(Q.negative(expr))
            continue
        if expr.is_nonzero:
            ret.append(Q.nonzero(expr))
            continue
        if expr.is_nonpositive:
            ret.append(Q.nonpositive(expr))
            continue
        if expr.is_nonnegative:
            ret.append(Q.nonnegative(expr))
        return ret
