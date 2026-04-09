# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: solvers.pyc (Python 3.11)

'''
This module contain solvers for all kinds of equations:

    - algebraic or transcendental, use solve()

    - recurrence, use rsolve()

    - differential, use dsolve()

    - nonlinear (numerically), use nsolve()
      (you will need a good starting point)

'''
from __future__ import annotations
from sympy.core import S, Add, Symbol, Dummy, Expr, Mul
from sympy.core.assumptions import check_assumptions
from sympy.core.exprtools import factor_terms
from sympy.core.function import expand_mul, expand_log, Derivative, AppliedUndef, UndefinedFunction, nfloat, Function, expand_power_exp, _mexpand, expand, expand_func
from sympy.core.logic import fuzzy_not
from sympy.core.numbers import Float, Rational, _illegal
from sympy.core.intfunc import integer_log, ilcm
from sympy.core.power import Pow
from sympy.core.relational import Eq, Ne
from sympy.core.sorting import ordered, default_sort_key
from sympy.core.sympify import sympify, _sympify
from sympy.core.traversal import preorder_traversal
from sympy.logic.boolalg import And, BooleanAtom
from sympy.functions import log, exp, LambertW, cos, sin, tan, acos, asin, atan, Abs, re, im, arg, sqrt, atan2
from sympy.functions.combinatorial.factorials import binomial
from sympy.functions.elementary.hyperbolic import HyperbolicFunction
from sympy.functions.elementary.piecewise import piecewise_fold, Piecewise
from sympy.functions.elementary.trigonometric import TrigonometricFunction
from sympy.integrals.integrals import Integral
from sympy.ntheory.factor_ import divisors
from sympy.simplify import simplify, collect, powsimp, posify, powdenest, nsimplify, denom, logcombine, sqrtdenest, fraction, separatevars
from sympy.simplify.sqrtdenest import sqrt_depth
from sympy.simplify.fu import TR1, TR2i, TR10, TR11
from sympy.strategies.rl import rebuild
from sympy.matrices.exceptions import NonInvertibleMatrixError
from sympy.matrices import Matrix, zeros
from sympy.polys import roots, cancel, factor, Poly
from sympy.polys.solvers import sympy_eqs_to_ring, solve_lin_sys
from sympy.polys.polyerrors import GeneratorsNeeded, PolynomialError
from sympy.polys.polytools import gcd
from sympy.utilities.lambdify import lambdify
from sympy.utilities.misc import filldedent, debugf
from sympy.utilities.iterables import connected_components, generate_bell, uniq, iterable, is_sequence, subsets, flatten, sift
from sympy.utilities.decorator import conserve_mpmath_dps
from mpmath import findroot
from sympy.solvers.polysys import solve_poly_system
from types import GeneratorType
from collections import defaultdict
from itertools import combinations, product
import warnings

def recast_to_symbols(eqs, symbols):
    """
    Return (e, s, d) where e and s are versions of *eqs* and
    *symbols* in which any non-Symbol objects in *symbols* have
    been replaced with generic Dummy symbols and d is a dictionary
    that can be used to restore the original expressions.

    Examples
    ========

    >>> from sympy.solvers.solvers import recast_to_symbols
    >>> from sympy import symbols, Function
    >>> x, y = symbols('x y')
    >>> fx = Function('f')(x)
    >>> eqs, syms = [fx + 1, x, y], [fx, y]
    >>> e, s, d = recast_to_symbols(eqs, syms); (e, s, d)
    ([_X0 + 1, x, y], [_X0, y], {_X0: f(x)})

    The original equations and symbols can be restored using d:

    >>> assert [i.xreplace(d) for i in eqs] == eqs
    >>> assert [d.get(i, i) for i in s] == syms

    """
    pass
# WARNING: Decompyle incomplete


def _ispow(e):
