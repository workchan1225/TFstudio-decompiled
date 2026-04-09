# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: solveset.pyc (Python 3.11)

'''
This module contains functions to:

    - solve a single equation for a single variable, in any domain either real or complex.

    - solve a single transcendental equation for a single variable in any domain either real or complex.
      (currently supports solving in real domain only)

    - solve a system of linear equations with N variables and M equations.

    - solve a system of Non Linear Equations with N variables and M equations
'''
from sympy.core.sympify import sympify
from sympy.core import S, Pow, Dummy, pi, Expr, Wild, Mul, Add, Basic
from sympy.core.containers import Tuple
from sympy.core.function import Lambda, expand_complex, AppliedUndef, expand_log, _mexpand, expand_trig, nfloat
from sympy.core.mod import Mod
from sympy.core.numbers import I, Number, Rational, oo
from sympy.core.intfunc import integer_log
from sympy.core.relational import Eq, Ne, Relational
from sympy.core.sorting import default_sort_key, ordered
from sympy.core.symbol import Symbol, _uniquely_named_symbol
from sympy.core.sympify import _sympify
from sympy.core.traversal import preorder_traversal
from sympy.external.gmpy import gcd as number_gcd, lcm as number_lcm
from sympy.polys.matrices.linsolve import _linear_eq_to_dict
from sympy.polys.polyroots import UnsolvableFactorError
from sympy.simplify.simplify import simplify, fraction, trigsimp, nsimplify
from sympy.simplify import powdenest, logcombine
from sympy.functions import log, tan, cot, sin, cos, sec, csc, exp, acos, asin, atan, acot, acsc, asec, piecewise_fold, Piecewise
from sympy.functions.combinatorial.numbers import totient
from sympy.functions.elementary.complexes import Abs, arg, re, im
from sympy.functions.elementary.hyperbolic import HyperbolicFunction, sinh, cosh, tanh, coth, sech, csch, asinh, acosh, atanh, acoth, asech, acsch
from sympy.functions.elementary.miscellaneous import real_root
from sympy.functions.elementary.trigonometric import TrigonometricFunction
from sympy.logic.boolalg import And, BooleanTrue
from sympy.sets import FiniteSet, imageset, Interval, Intersection, Union, ConditionSet, ImageSet, Complement, Contains
from sympy.sets.sets import Set, ProductSet
from sympy.matrices import zeros, Matrix, MatrixBase
from sympy.ntheory.factor_ import divisors
from sympy.ntheory.residue_ntheory import discrete_log, nthroot_mod
from sympy.polys import roots, Poly, degree, together, PolynomialError, RootOf, factor, lcm, gcd
from sympy.polys.polyerrors import CoercionFailed
from sympy.polys.polytools import invert, groebner, poly
from sympy.polys.solvers import sympy_eqs_to_ring, solve_lin_sys, PolyNonlinearError
from sympy.polys.matrices.linsolve import _linsolve
from sympy.solvers.solvers import checksol, denoms, unrad, _simple_dens, recast_to_symbols
from sympy.solvers.polysys import solve_poly_system
from sympy.utilities import filldedent
from sympy.utilities.iterables import numbered_symbols, has_dups, is_sequence, iterable
from sympy.calculus.util import periodicity, continuous_domain, function_range
from types import GeneratorType

class NonlinearError(ValueError):
    '''Raised when unexpectedly encountering nonlinear equations'''
    pass


def _masked(f, *atoms):
    '''Return ``f``, with all objects given by ``atoms`` replaced with
    Dummy symbols, ``d``, and the list of replacements, ``(d, e)``,
    where ``e`` is an object of type given by ``atoms`` in which
    any other instances of atoms have been recursively replaced with
    Dummy symbols, too. The tuples are ordered so that if they are
    applied in sequence, the origin ``f`` will be restored.

    Examples
    ========

    >>> from sympy import cos
    >>> from sympy.abc import x
    >>> from sympy.solvers.solveset import _masked

    >>> f = cos(cos(x) + 1)
    >>> f, reps = _masked(cos(1 + cos(x)), cos)
    >>> f
    _a1
    >>> reps
    [(_a1, cos(_a0 + 1)), (_a0, cos(x))]
    >>> for d, e in reps:
    ...     f = f.xreplace({d: e})
    >>> f
    cos(cos(x) + 1)
    '''
    sym = numbered_symbols('a', cls = Dummy, real = True)
    mask = []
# WARNING: Decompyle incomplete


def _invert(f_x, y, x, domain = (S.Complexes,)):
    '''
    Reduce the complex valued equation $f(x) = y$ to a set of equations

    $$\\left\\{g(x) = h_1(y),\\  g(x) = h_2(y),\\ \\dots,\\  g(x) = h_n(y) \\right\\}$$

    where $g(x)$ is a simpler function than $f(x)$.  The return value is a tuple
    $(g(x), \\mathrm{set}_h)$, where $g(x)$ is a function of $x$ and $\\mathrm{set}_h$ is
    the set of function $\\left\\{h_1(y), h_2(y), \\dots, h_n(y)\\right\\}$.
    Here, $y$ is not necessarily a symbol.

    $\\mathrm{set}_h$ contains the functions, along with the information
    about the domain in which they are valid, through set
    operations. For instance, if :math:`y = |x| - n` is inverted
    in the real domain, then $\\mathrm{set}_h$ is not simply
    $\\{-n, n\\}$ as the nature of `n` is unknown; rather, it is:

    $$ \\left(\\left[0, \\infty\\right) \\cap \\left\\{n\\right\\}\\right) \\cup
                       \\left(\\left(-\\infty, 0\\right] \\cap \\left\\{- n\\right\\}\\right)$$

    By default, the complex domain is used which means that inverting even
    seemingly simple functions like $\\exp(x)$ will give very different
    results from those obtained in the real domain.
    (In the case of $\\exp(x)$, the inversion via $\\log$ is multi-valued
    in the complex domain, having infinitely many branches.)

    If you are working with real values only (or you are not sure which
    function to use) you should probably set the domain to
    ``S.Reals`` (or use ``invert_real`` which does that automatically).


    Examples
    ========

    >>> from sympy.solvers.solveset import invert_complex, invert_real
    >>> from sympy.abc import x, y
    >>> from sympy import exp

    When does exp(x) == y?

    >>> invert_complex(exp(x), y, x)
    (x, ImageSet(Lambda(_n, I*(2*_n*pi + arg(y)) + log(Abs(y))), Integers))
    >>> invert_real(exp(x), y, x)
    (x, Intersection({log(y)}, Reals))

    When does exp(x) == 1?

    >>> invert_complex(exp(x), 1, x)
    (x, ImageSet(Lambda(_n, 2*_n*I*pi), Integers))
    >>> invert_real(exp(x), 1, x)
    (x, {0})

    See Also
    ========
    invert_real, invert_complex
    '''
    x = sympify(x)
    if not x.is_Symbol:
        raise ValueError('x must be a symbol')
    f_x = sympify(f_x)
    if x not in f_x.free_symbols:
        raise ValueError("Inverse of constant function doesn't exist")
    y = sympify(y)
    if x in y.free_symbols:
        raise ValueError('y should be independent of x ')
    if domain.is_subset(S.Reals):
        (x1, s) = _invert_real(f_x, FiniteSet(y), x)
    else:
        (x1, s) = _invert_complex(f_x, FiniteSet(y), x)
    if x1 != x:
        return (x1, s)
    if None is S.Complexes:
        return (x1, s)
    if None(s, FiniteSet):
        return (x1, s.intersect(domain))
    if None is S.Reals:
        return (x1, s)
    return (None, s.intersect(domain))

invert_complex = _invert

def invert_real(f_x, y, x):
    '''
    Inverts a real-valued function. Same as :func:`invert_complex`, but sets
    the domain to ``S.Reals`` before inverting.
    '''
    return _invert(f_x, y, x, S.Reals)


def _invert_real(f, g_ys, symbol):
    '''Helper function for _invert.'''
    if f == symbol or g_ys is S.EmptySet:
        return (symbol, g_ys)
    n = None('n', real = True)
    if (isinstance(f, exp) or f.is_Pow) and f.base == S.Exp1:
        return _invert_real(f.exp, imageset(Lambda(n, log(n)), g_ys), symbol)
# WARNING: Decompyle incomplete

_trig_inverses = None
_hyp_inverses = None

def _invert_trig_hyp_real(f, g_ys, symbol):
    '''Helper function for inverting trigonometric and hyperbolic functions.

    This helper only handles inversion over the reals.

    For trigonometric functions only finite `g_ys` sets are implemented.

    For hyperbolic functions the set `g_ys` is checked against the domain of the
    respective inverse functions. Infinite `g_ys` sets are also supported.
    '''
    pass
# WARNING: Decompyle incomplete


def _invert_trig_hyp_complex(f, g_ys, symbol):
    '''Helper function for inverting trigonometric and hyperbolic functions.

    This helper only handles inversion over the complex numbers.
    Only finite `g_ys` sets are implemented.

    Handling of singularities is only implemented for hyperbolic equations.
    In case of a symbolic element g in g_ys a ConditionSet may be returned.
    '''
    pass
# WARNING: Decompyle incomplete


def _invert_complex(f, g_ys, symbol):
    '''Helper function for _invert.'''
    pass
# WARNING: Decompyle incomplete


def _invert_abs(f, g_ys, symbol):
    '''Helper function for inverting absolute value functions.

    Returns the complete result of inverting an absolute value
    function along with the conditions which must also be satisfied.

    If it is certain that all these conditions are met, a :class:`~.FiniteSet`
    of all possible solutions is returned. If any condition cannot be
    satisfied, an :class:`~.EmptySet` is returned. Otherwise, a
    :class:`~.ConditionSet` of the solutions, with all the required conditions
    specified, is returned.

    '''
    if not g_ys.is_FiniteSet:
        pos = Intersection(g_ys, Interval(0, S.Infinity))
        parg = _invert_real(f, pos, symbol)
        narg = _invert_real(-f, pos, symbol)
        if parg[0] != narg[0]:
            raise NotImplementedError
        return (parg[0], Union(narg[1], parg[1]))
    unknown = None
# WARNING: Decompyle incomplete


def domain_check(f, symbol, p):
    '''Returns False if point p is infinite or any subexpression of f
    is infinite or becomes so after replacing symbol with p. If none of
    these conditions is met then True will be returned.

    Examples
    ========

    >>> from sympy import Mul, oo
    >>> from sympy.abc import x
    >>> from sympy.solvers.solveset import domain_check
    >>> g = 1/(1 + (1/(x + 1))**2)
    >>> domain_check(g, x, -1)
    False
    >>> domain_check(x**2, x, 0)
    True
    >>> domain_check(1/x, x, oo)
    False

    * The function relies on the assumption that the original form
      of the equation has not been changed by automatic simplification.

    >>> domain_check(x/x, x, 0) # x/x is automatically simplified to 1
    True

    * To deal with automatic evaluations use evaluate=False:

    >>> domain_check(Mul(x, 1/x, evaluate=False), x, 0)
    False
    '''
    p = sympify(p)
    f = sympify(f)
    if p.is_infinite:
        return False
    return None(f, symbol, p)


def _domain_check(f, symbol, p):
    pass
# WARNING: Decompyle incomplete


def _is_finite_with_finite_vars(f, domain = (S.Complexes,)):
    '''
    Return True if the given expression is finite. For symbols that
    do not assign a value for `complex` and/or `real`, the domain will
    be used to assign a value; symbols that do not assign a value
    for `finite` will be made finite. All other assumptions are
    left unmodified.
    '''
    pass
# WARNING: Decompyle incomplete


def _is_function_class_equation(func_class, f, symbol):
    ''' Tests whether the equation is an equation of the given function class.

    The given equation belongs to the given function class if it is
    comprised of functions of the function class which are multiplied by
    or added to expressions independent of the symbol. In addition, the
    arguments of all such functions must be linear in the symbol as well.

    Examples
    ========

    >>> from sympy.solvers.solveset import _is_function_class_equation
    >>> from sympy import tan, sin, tanh, sinh, exp
    >>> from sympy.abc import x
    >>> from sympy.functions.elementary.trigonometric import TrigonometricFunction
    >>> from sympy.functions.elementary.hyperbolic import HyperbolicFunction
    >>> _is_function_class_equation(TrigonometricFunction, exp(x) + tan(x), x)
    False
    >>> _is_function_class_equation(TrigonometricFunction, tan(x) + sin(x), x)
    True
    >>> _is_function_class_equation(TrigonometricFunction, tan(x**2), x)
    False
    >>> _is_function_class_equation(TrigonometricFunction, tan(x + 2), x)
    True
    >>> _is_function_class_equation(HyperbolicFunction, tanh(x) + sinh(x), x)
    True
    '''
    pass
# WARNING: Decompyle incomplete


def _solve_as_rational(f, symbol, domain):
    ''' solve rational functions'''
    f = together(_mexpand(f, recursive = True), deep = True)
    (g, h) = fraction(f)
    if not h.has(symbol):
        
        try:
            return _solve_as_poly(g, symbol, domain)
        except NotImplementedError:
            return 
            except CoercionFailed:
                return 
            _solveset(h, symbol, domain) = _solveset(g, symbol, domain)
            return valid_solns - invalid_solns



class _SolveTrig1Error(Exception):
    '''Raised when _solve_trig1 heuristics do not apply'''
    pass


def _solve_trig(f, symbol, domain):
    '''Function to call other helpers to solve trigonometric equations '''
    pass
# WARNING: Decompyle incomplete


def _solve_trig1(f, symbol, domain):
    """Primary solver for trigonometric and hyperbolic equations

    Returns either the solution set as a ConditionSet (auto-evaluated to a
    union of ImageSets if no variables besides 'symbol' are involved) or
    raises _SolveTrig1Error if f == 0 cannot be solved.

    Notes
    =====
    Algorithm:
    1. Do a change of variable x -> mu*x in arguments to trigonometric and
    hyperbolic functions, in order to reduce them to small integers. (This
    step is crucial to keep the degrees of the polynomials of step 4 low.)
    2. Rewrite trigonometric/hyperbolic functions as exponentials.
    3. Proceed to a 2nd change of variable, replacing exp(I*x) or exp(x) by y.
    4. Solve the resulting rational equation.
    5. Use invert_complex or invert_real to return to the original variable.
    6. If the coefficients of 'symbol' were symbolic in nature, add the
    necessary consistency conditions in a ConditionSet.

    """
    pass
# WARNING: Decompyle incomplete


def _solve_trig2(f, symbol, domain):
    '''Secondary helper to solve trigonometric equations,
    called when first helper fails '''
    pass
# WARNING: Decompyle incomplete


def _solve_as_poly(f, symbol, domain = (S.Complexes,)):
    '''
    Solve the equation using polynomial techniques if it already is a
    polynomial equation or, with a change of variables, can be made so.
    '''
    pass
# WARNING: Decompyle incomplete


def _solve_radical(f, unradf, symbol, solveset_solver):
    ''' Helper function to solve equations with radicals '''
    pass
# WARNING: Decompyle incomplete


def _solve_abs(f, symbol, domain):
    ''' Helper function to solve equation involving absolute value function '''
    pass
# WARNING: Decompyle incomplete


def solve_decomposition(f, symbol, domain):
    '''
    Function to solve equations via the principle of "Decomposition
    and Rewriting".

    Examples
    ========
    >>> from sympy import exp, sin, Symbol, pprint, S
    >>> from sympy.solvers.solveset import solve_decomposition as sd
    >>> x = Symbol(\'x\')
    >>> f1 = exp(2*x) - 3*exp(x) + 2
    >>> sd(f1, x, S.Reals)
    {0, log(2)}
    >>> f2 = sin(x)**2 + 2*sin(x) + 1
    >>> pprint(sd(f2, x, S.Reals), use_unicode=False)
              3*pi
    {2*n*pi + ---- | n in Integers}
               2
    >>> f3 = sin(x + 2)
    >>> pprint(sd(f3, x, S.Reals), use_unicode=False)
    {2*n*pi - 2 | n in Integers} U {2*n*pi - 2 + pi | n in Integers}

    '''
    decompogen = decompogen
    import sympy.solvers.decompogen
    g_s = decompogen(f, symbol)
    y_s = FiniteSet(0)
    for g in g_s:
        frange = function_range(g, symbol, domain)
        y_s = Intersection(frange, y_s)
        result = S.EmptySet
        if isinstance(y_s, FiniteSet):
            for y in y_s:
                solutions = solveset(Eq(g, y), symbol, domain)
                if not isinstance(solutions, ConditionSet):
                    result += solutions
        if isinstance(y_s, ImageSet):
            iter_iset = (y_s,)
        elif isinstance(y_s, Union):
            iter_iset = y_s.args
        elif y_s is S.EmptySet:
            
            return None, S.EmptySet
        for solveset(Eq(iset.lamda.expr, g), symbol, domain) in iter_iset:
            dummy_var = tuple(iset.lamda.expr.free_symbols)[0]
            (base_set,) = iset.base_sets
            if isinstance(new_solutions, FiniteSet):
                new_exprs = new_solutions
            elif isinstance(new_solutions, Intersection) and isinstance(new_solutions.args[1], FiniteSet):
                new_exprs = new_solutions.args[1]
            for new_expr in new_exprs:
                result += ImageSet(Lambda(dummy_var, new_expr), base_set)
                if result is S.EmptySet:
                    
                    return None, ConditionSet(symbol, Eq(f, 0), domain)
                return y_s


def _solveset(f, symbol, domain, _check = (False,)):
    """Helper for solveset to return a result from an expression
    that has already been sympify'ed and is known to contain the
    given symbol."""
    pass
# WARNING: Decompyle incomplete


def _is_modular(f, symbol):
