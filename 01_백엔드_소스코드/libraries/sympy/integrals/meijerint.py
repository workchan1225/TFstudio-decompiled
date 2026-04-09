# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: meijerint.pyc (Python 3.11)

'''
Integrate functions by rewriting them as Meijer G-functions.

There are three user-visible functions that can be used by other parts of the
sympy library to solve various integration problems:

- meijerint_indefinite
- meijerint_definite
- meijerint_inversion

They can be used to compute, respectively, indefinite integrals, definite
integrals over intervals of the real line, and inverse laplace-type integrals
(from c-I*oo to c+I*oo). See the respective docstrings for details.

The main references for this are:

[L] Luke, Y. L. (1969), The Special Functions and Their Approximations,
    Volume 1

[R] Kelly B. Roach.  Meijer G Function Representations.
    In: Proceedings of the 1997 International Symposium on Symbolic and
    Algebraic Computation, pages 205-211, New York, 1997. ACM.

[P] A. P. Prudnikov, Yu. A. Brychkov and O. I. Marichev (1990).
    Integrals and Series: More Special Functions, Vol. 3,.
    Gordon and Breach Science Publisher
'''
from __future__ import annotations
import itertools
from sympy import SYMPY_DEBUG
from sympy.core import S, Expr
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.cache import cacheit
from sympy.core.containers import Tuple
from sympy.core.exprtools import factor_terms
from sympy.core.function import expand, expand_mul, expand_power_base, expand_trig, Function
from sympy.core.mul import Mul
from sympy.core.intfunc import ilcm
from sympy.core.numbers import Rational, pi
from sympy.core.relational import Eq, Ne, _canonical_coeff
from sympy.core.sorting import default_sort_key, ordered
from sympy.core.symbol import Dummy, symbols, Wild, Symbol
from sympy.core.sympify import sympify
from sympy.functions.combinatorial.factorials import factorial
from sympy.functions.elementary.complexes import re, im, arg, Abs, sign, unpolarify, polarify, polar_lift, principal_branch, unbranched_argument, periodic_argument
from sympy.functions.elementary.exponential import exp, exp_polar, log
from sympy.functions.elementary.integers import ceiling
from sympy.functions.elementary.hyperbolic import cosh, sinh, _rewrite_hyperbolics_as_exp, HyperbolicFunction
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.piecewise import Piecewise, piecewise_fold
from sympy.functions.elementary.trigonometric import cos, sin, sinc, TrigonometricFunction
from sympy.functions.special.bessel import besselj, bessely, besseli, besselk
from sympy.functions.special.delta_functions import DiracDelta, Heaviside
from sympy.functions.special.elliptic_integrals import elliptic_k, elliptic_e
from sympy.functions.special.error_functions import erf, erfc, erfi, Ei, expint, Si, Ci, Shi, Chi, fresnels, fresnelc
from sympy.functions.special.gamma_functions import gamma
from sympy.functions.special.hyper import hyper, meijerg
from sympy.functions.special.singularity_functions import SingularityFunction
from integrals import Integral
from sympy.logic.boolalg import And, Or, BooleanAtom, Not, BooleanFunction
from sympy.polys import cancel, factor
from sympy.utilities.iterables import multiset_partitions
from sympy.utilities.misc import debug as _debug
from sympy.utilities.misc import debugf as _debugf
z = Dummy('z')

def _has(res, *f):
    pass
# WARNING: Decompyle incomplete


def _create_lookup_table(table):
    ''' Add formulae for the function -> meijerg lookup table. '''
    pass
# WARNING: Decompyle incomplete

from sympy.utilities.timeutils import timethis
timeit = timethis('meijerg')

def _mytype(f = None, x = None):
    ''' Create a hashable entity describing the type of f. '''
    pass
# WARNING: Decompyle incomplete


class _CoeffExpValueError(ValueError):
    '''
    Exception raised by _get_coeff_exp, for internal use only.
    '''
    pass


def _get_coeff_exp(expr, x):
    '''
    When expr is known to be of the form c*x**b, with c and/or b possibly 1,
    return c, b.

    Examples
    ========

    >>> from sympy.abc import x, a, b
    >>> from sympy.integrals.meijerint import _get_coeff_exp
    >>> _get_coeff_exp(a*x**b, x)
    (a, b)
    >>> _get_coeff_exp(x, x)
    (1, 1)
    >>> _get_coeff_exp(2*x, x)
    (2, 1)
    >>> _get_coeff_exp(x**3, x)
    (1, 3)
    '''
    powsimp = powsimp
    import sympy.simplify
    (c, m) = expand_power_base(powsimp(expr)).as_coeff_mul(x)
    if not m:
        return (c, S.Zero)
    (m,) = None
    if m.is_Pow:
        if m.base != x:
            raise _CoeffExpValueError('expr not of form a*x**b')
        return (c, m.exp)
    if None == x:
        return (c, S.One)
    raise None('expr not of form a*x**b: %s' % expr)


def _exponents(expr, x):
    '''
    Find the exponents of ``x`` (not including zero) in ``expr``.

    Examples
    ========

    >>> from sympy.integrals.meijerint import _exponents
    >>> from sympy.abc import x, y
    >>> from sympy import sin
    >>> _exponents(x, x)
    {1}
    >>> _exponents(x**2, x)
    {2}
    >>> _exponents(x**2 + x, x)
    {1, 2}
    >>> _exponents(x**3*sin(x + x**y) + 1/x, x)
    {-1, 1, 3, y}
    '''
    pass
# WARNING: Decompyle incomplete


def _functions(expr, x):
    ''' Find the types of functions in expr, to estimate the complexity. '''
    pass
# WARNING: Decompyle incomplete


def _find_splitting_points(expr, x):
    '''
    Find numbers a such that a linear substitution x -> x + a would
    (hopefully) simplify expr.

    Examples
    ========

    >>> from sympy.integrals.meijerint import _find_splitting_points as fsp
    >>> from sympy import sin
    >>> from sympy.abc import x
    >>> fsp(x, x)
    {0}
    >>> fsp((x-1)**3, x)
    {1}
    >>> fsp(sin(x+3)*x, x)
    {-3, 0}
    '''
    pass
# WARNING: Decompyle incomplete


def _split_mul(f, x):
    '''
    Split expression ``f`` into fac, po, g, where fac is a constant factor,
    po = x**s for some s independent of s, and g is "the rest".

    Examples
    ========

    >>> from sympy.integrals.meijerint import _split_mul
    >>> from sympy import sin
    >>> from sympy.abc import s, x
    >>> _split_mul((3*x)**s*sin(x**2)*x, x)
    (3**s, x*x**s, sin(x**2))
    '''
    fac = S.One
    po = S.One
    g = S.One
    f = expand_power_base(f)
    args = Mul.make_args(f)
    for a in args:
        if a == x:
            po *= x
            continue
        if x not in a.free_symbols:
            fac *= a
            continue
        if a.is_Pow and x not in a.exp.free_symbols:
            (c, t) = a.base.as_coeff_mul(x)
            if t != (x,):
                (c, t) = expand_mul(a.base).as_coeff_mul(x)
            if t == (x,):
                po *= x ** a.exp
                fac *= unpolarify(polarify(c ** a.exp, subs = False))
                continue
        g *= a
        return (fac, po, g)


def _mul_args(f):
    '''
    Return a list ``L`` such that ``Mul(*L) == f``.

    If ``f`` is not a ``Mul`` or ``Pow``, ``L=[f]``.
    If ``f=g**n`` for an integer ``n``, ``L=[g]*n``.
    If ``f`` is a ``Mul``, ``L`` comes from applying ``_mul_args`` to all factors of ``f``.
    '''
    args = Mul.make_args(f)
    gs = []
    for g in args:
        if g.is_Pow and g.exp.is_Integer:
            n = g.exp
            base = g.base
            if n < 0:
                n = -n
                base = 1 / base
            gs += [
                base] * n
            continue
        gs.append(g)
        return gs


def _mul_as_two_parts(f):
