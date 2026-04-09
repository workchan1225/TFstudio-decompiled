# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polytools.pyc (Python 3.11)

'''User-friendly public interface to polynomial functions. '''
from functools import wraps, reduce
from operator import mul
from typing import Optional
from sympy.core import S, Expr, Add, Tuple
from sympy.core.basic import Basic
from sympy.core.decorators import _sympifyit
from sympy.core.exprtools import Factors, factor_nc, factor_terms
from sympy.core.evalf import pure_complex, evalf, fastlog, _evalf_with_bounded_error, quad_to_mpmath
from sympy.core.function import Derivative
from sympy.core.mul import Mul, _keep_coeff
from sympy.core.intfunc import ilcm
from sympy.core.numbers import I, Integer, equal_valued
from sympy.core.relational import Relational, Equality
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy, Symbol
from sympy.core.sympify import sympify, _sympify
from sympy.core.traversal import preorder_traversal, bottom_up
from sympy.logic.boolalg import BooleanAtom
from sympy.polys import polyoptions as options
from sympy.polys.constructor import construct_domain
from sympy.polys.domains import FF, QQ, ZZ
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.fglmtools import matrix_fglm
from sympy.polys.groebnertools import groebner as _groebner
from sympy.polys.monomials import Monomial
from sympy.polys.orderings import monomial_key
from sympy.polys.polyclasses import DMP, DMF, ANP
from sympy.polys.polyerrors import OperationNotSupported, DomainError, CoercionFailed, UnificationFailed, GeneratorsNeeded, PolynomialError, MultivariatePolynomialError, ExactQuotientFailed, PolificationFailed, ComputationFailed, GeneratorsError
from sympy.polys.polyutils import basic_from_dict, _sort_gens, _unify_gens, _dict_reorder, _dict_from_expr, _parallel_dict_from_expr
from sympy.polys.rationaltools import together
from sympy.polys.rootisolation import dup_isolate_real_roots_list
from sympy.utilities import group, public, filldedent
from sympy.utilities.exceptions import sympy_deprecation_warning
from sympy.utilities.iterables import iterable, sift
import sympy.polys as sympy
import mpmath
from mpmath.libmp.libhyper import NoConvergence

def _polifyit(func):
    pass
# WARNING: Decompyle incomplete

Poly = <NODE:12>()
PurePoly = <NODE:12>()
poly_from_expr = (lambda expr: opt = options.build_options(gens, args)_poly_from_expr(expr, opt))()

def _poly_from_expr(expr, opt):
    '''Construct a polynomial from an expression. '''
    expr = sympify(expr)
    orig = expr
    if not isinstance(expr, Basic):
        raise PolificationFailed(opt, orig, expr)
# WARNING: Decompyle incomplete

parallel_poly_from_expr = (lambda exprs: opt = options.build_options(gens, args)_parallel_poly_from_expr(exprs, opt))()

def _parallel_poly_from_expr(exprs, opt):
    '''Construct polynomials from expressions. '''
    pass
# WARNING: Decompyle incomplete


def _update_args(args, key, value):
    '''Add a new ``(key, value)`` pair to arguments ``dict``. '''
    args = dict(args)
    if key not in args:
        args[key] = value
    return args

degree = (lambda f, gen = (0,): f = sympify(f, strict = True)gen_is_Num = sympify(gen, strict = True).is_Numberif f.is_Poly:
p = fisNum = p.as_expr().is_Numberelse:
isNum = f.is_Numberif not isNum:
if gen_is_Num:
(p, _) = poly_from_expr(f)else:
(p, _) = poly_from_expr(f, gen)if isNum:
S.Zero if f else S.NegativeInfinityif not None:
if f.is_Poly and gen not in p.gens:
(p, _) = poly_from_expr(f.as_expr())if gen not in p.gens:
S.Zeroif f.is_Poly and len(f.free_symbols) > 1:
raise TypeError(filldedent(f'''\n         A symbolic generator of interest is required for a multivariate\n         expression like func = {f!s}, e.g. degree(func, gen = {next(ordered(f.free_symbols))!s}) instead of\n         degree(func, gen = {gen!s}).\n        '''))result = p.degree(gen)Integer(result) if isinstance(result, int) else S.NegativeInfinity)()
total_degree = (lambda f:
