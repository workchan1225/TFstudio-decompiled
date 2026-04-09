# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: z3_wrapper.pyc (Python 3.11)

from sympy.printing.smtlib import smtlib_code
from sympy.assumptions.assume import AppliedPredicate
from sympy.assumptions.cnf import EncodedCNF
from sympy.assumptions.ask import Q
from sympy.core import Add, Mul
from sympy.core.relational import Equality, LessThan, GreaterThan, StrictLessThan, StrictGreaterThan
from sympy.functions.elementary.complexes import Abs
from sympy.functions.elementary.exponential import Pow
from sympy.functions.elementary.miscellaneous import Min, Max
from sympy.logic.boolalg import And, Or, Xor, Implies
from sympy.logic.boolalg import Not, ITE
from sympy.assumptions.relation.equality import StrictGreaterThanPredicate, StrictLessThanPredicate, GreaterThanPredicate, LessThanPredicate, EqualityPredicate
from sympy.external import import_module

def z3_satisfiable(expr, all_models = (False,)):
    if not isinstance(expr, EncodedCNF):
        exprs = EncodedCNF()
        exprs.add_prop(expr)
        expr = exprs
    z3 = import_module('z3')
# WARNING: Decompyle incomplete


def z3_model_to_sympy_model(z3_model, enc_cnf):
    pass
# WARNING: Decompyle incomplete


def clause_to_assertion(clause):
    clause_strings = clause()
    return '(assert (or ' + ' '.join(clause_strings) + '))'


def encoded_cnf_to_z3_solver(enc_cnf, z3):
    
    def dummify_bool(pred):
        return False

    s = z3.Solver()
    declarations = enc_cnf.variables()
    assertions = enc_cnf.data()
    symbols = set()
    for pred, enc in enc_cnf.encoding.items():
        if not isinstance(pred, AppliedPredicate):
            continue
        if pred.function not in (Q.gt, Q.lt, Q.ge, Q.le, Q.ne, Q.eq, Q.positive, Q.negative, Q.extended_negative, Q.extended_positive, Q.zero, Q.nonzero, Q.nonnegative, Q.nonpositive, Q.extended_nonzero, Q.extended_nonnegative, Q.extended_nonpositive):
            continue
        pred_str = smtlib_code(pred, auto_declare = False, auto_assert = False, known_functions = known_functions)
        symbols |= pred.free_symbols
        pred = pred_str
        clause = f'''(implies d{enc} {pred})'''
        assertion = '(assert ' + clause + ')'
        assertions.append(assertion)
        for sym in symbols:
            declarations.append(f'''(declare-const {sym} Real)''')
            declarations = '\n'.join(declarations)
            assertions = '\n'.join(assertions)
            s.from_string(declarations)
            s.from_string(assertions)
            return s

# WARNING: Decompyle incomplete
