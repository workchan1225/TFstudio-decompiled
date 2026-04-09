# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: heurisch.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
from functools import reduce
from itertools import permutations
from sympy.core.add import Add
from sympy.core.basic import Basic
from sympy.core.mul import Mul
from sympy.core.symbol import Wild, Dummy, Symbol
from sympy.core.basic import sympify
from sympy.core.numbers import Rational, pi, I
from sympy.core.relational import Eq, Ne
from sympy.core.singleton import S
from sympy.core.sorting import ordered
from sympy.core.traversal import iterfreeargs
from sympy.functions import exp, sin, cos, tan, cot, asin, atan
from sympy.functions import log, sinh, cosh, tanh, coth, asinh
from sympy.functions import sqrt, erf, erfi, li, Ei
from sympy.functions import besselj, bessely, besseli, besselk
from sympy.functions import hankel1, hankel2, jn, yn
from sympy.functions.elementary.complexes import Abs, re, im, sign, arg
from sympy.functions.elementary.exponential import LambertW
from sympy.functions.elementary.integers import floor, ceiling
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.special.delta_functions import Heaviside, DiracDelta
from sympy.simplify.radsimp import collect
from sympy.logic.boolalg import And, Or
from sympy.utilities.iterables import uniq
from sympy.polys import quo, gcd, lcm, factor_list, cancel, PolynomialError
from sympy.polys.monomials import itermonomials
from sympy.polys.polyroots import root_factors
from sympy.polys.rings import PolyRing
from sympy.polys.solvers import solve_lin_sys
from sympy.polys.constructor import construct_domain
from sympy.integrals.integrals import integrate

def components(f, x):
    '''
    Returns a set of all functional components of the given expression
    which includes symbols, function applications and compositions and
    non-integer powers. Fractional powers are collected with
    minimal, positive exponents.

    Examples
    ========

    >>> from sympy import cos, sin
    >>> from sympy.abc import x
    >>> from sympy.integrals.heurisch import components

    >>> components(sin(x)*cos(x)**2, x)
    {x, sin(x), cos(x)}

    See Also
    ========

    heurisch
    '''
    result = set()
    if f.has_free(x):
        if f.is_symbol and f.is_commutative:
            result.add(f)
        elif f.is_Function or f.is_Derivative:
            for g in f.args:
                result |= components(g, x)
                result.add(f)
        if f.is_Pow:
            result |= components(f.base, x)
            if not f.exp.is_Integer:
                if f.exp.is_Rational:
                    result.add(f.base ** Rational(1, f.exp.q))
                else:
                    result |= components(f.exp, x) | {
                        f}
            else:
                for g in f.args:
                    result |= components(g, x)
                    return result

_symbols_cache: 'dict[str, list[Dummy]]' = { }

def _symbols(name, n):
    '''get vector of symbols local to this module'''
    
    try:
        lsyms = _symbols_cache[name]
    except KeyError:
        lsyms = []
        _symbols_cache[name] = lsyms

# WARNING: Decompyle incomplete


def heurisch_wrapper(f, x, rewrite, hints, mappings, retries, degree_offset, unnecessary_permutations, _try_heurisch = (False, None, None, 3, 0, None, None)):
    """
    A wrapper around the heurisch integration algorithm.

    Explanation
    ===========

    This method takes the result from heurisch and checks for poles in the
    denominator. For each of these poles, the integral is reevaluated, and
    the final integration result is given in terms of a Piecewise.

    Examples
    ========

    >>> from sympy import cos, symbols
    >>> from sympy.integrals.heurisch import heurisch, heurisch_wrapper
    >>> n, x = symbols('n x')
    >>> heurisch(cos(n*x), x)
    sin(n*x)/n
    >>> heurisch_wrapper(cos(n*x), x)
    Piecewise((sin(n*x)/n, Ne(n, 0)), (x, True))

    See Also
    ========

    heurisch
    """
    pass
# WARNING: Decompyle incomplete


class BesselTable:
    '''
    Derivatives of Bessel functions of orders n and n-1
    in terms of each other.

    See the docstring of DiffCache.
    '''
    
    def __init__(self):
        self.table = { }
        self.n = Dummy('n')
        self.z = Dummy('z')
        self._create_table()

    
    def _create_table(t):
        z = t.z
        n = t.n
        table = t.table
        for f in (besselj, bessely, hankel1, hankel2):
            table[f] = (f(n - 1, z) - n * f(n, z) / z, (n - 1) * f(n - 1, z) / z - f(n, z))
            f = besseli
            table[f] = (f(n - 1, z) - n * f(n, z) / z, (n - 1) * f(n - 1, z) / z + f(n, z))
            f = besselk
            table[f] = (-f(n - 1, z) - n * f(n, z) / z, (n - 1) * f(n - 1, z) / z - f(n, z))
            for f in (jn, yn):
                table[f] = (f(n - 1, z) - (n + 1) * f(n, z) / z, (n - 1) * f(n - 1, z) / z - f(n, z))
                return None

    
    def diffs(t, f, n, z):
        if f in t.table:
            (diff0, diff1) = t.table[f]
            repl = [
                (t.n, n),
                (t.z, z)]
            return (diff0.subs(repl), diff1.subs(repl))

    
    def has(t, f):
        return f in t.table


_bessel_table = None

class DiffCache:
    '''
    Store for derivatives of expressions.

    Explanation
    ===========

    The standard form of the derivative of a Bessel function of order n
    contains two Bessel functions of orders n-1 and n+1, respectively.
    Such forms cannot be used in parallel Risch algorithm, because
    there is a linear recurrence relation between the three functions
    while the algorithm expects that functions and derivatives are
    represented in terms of algebraically independent transcendentals.

    The solution is to take two of the functions, e.g., those of orders
    n and n-1, and to express the derivatives in terms of the pair.
    To guarantee that the proper form is used the two derivatives are
    cached as soon as one is encountered.

    Derivatives of other functions are also cached at no extra cost.
    All derivatives are with respect to the same variable `x`.
    '''
    
    def __init__(self, x):
        global _bessel_table
        self.cache = { }
        self.x = x
        if not _bessel_table:
            _bessel_table = BesselTable()
            return None

    
    def get_diff(self, f):
        cache = self.cache
        if f in cache:
            pass
        elif not hasattr(f, 'func') or _bessel_table.has(f.func):
            cache[f] = cancel(f.diff(self.x))
        else:
            (n, z) = f.args
            (d0, d1) = _bessel_table.diffs(f.func, n, z)
            dz = self.get_diff(z)
            cache[f] = d0 * dz
            cache[f.func(n - 1, z)] = d1 * dz
        return cache[f]



def heurisch(f, x, rewrite, hints, mappings, retries, degree_offset, unnecessary_permutations, _try_heurisch = (False, None, None, 3, 0, None, None)):
    '''
    Compute indefinite integral using heuristic Risch algorithm.

    Explanation
    ===========

    This is a heuristic approach to indefinite integration in finite
    terms using the extended heuristic (parallel) Risch algorithm, based
    on Manuel Bronstein\'s "Poor Man\'s Integrator".

    The algorithm supports various classes of functions including
    transcendental elementary or special functions like Airy,
    Bessel, Whittaker and Lambert.

    Note that this algorithm is not a decision procedure. If it isn\'t
    able to compute the antiderivative for a given function, then this is
    not a proof that such a functions does not exist.  One should use
    recursive Risch algorithm in such case.  It\'s an open question if
    this algorithm can be made a full decision procedure.

    This is an internal integrator procedure. You should use top level
    \'integrate\' function in most cases, as this procedure needs some
    preprocessing steps and otherwise may fail.

    Specification
    =============

     heurisch(f, x, rewrite=False, hints=None)

       where
         f : expression
         x : symbol

         rewrite -> force rewrite \'f\' in terms of \'tan\' and \'tanh\'
         hints   -> a list of functions that may appear in anti-derivate

          - hints = None          --> no suggestions at all
          - hints = [ ]           --> try to figure out
          - hints = [f1, ..., fn] --> we know better

    Examples
    ========

    >>> from sympy import tan
    >>> from sympy.integrals.heurisch import heurisch
    >>> from sympy.abc import x, y

    >>> heurisch(y*tan(x), x)
    y*log(tan(x)**2 + 1)/2

    See Manuel Bronstein\'s "Poor Man\'s Integrator":

    References
    ==========

    .. [1] https://www-sop.inria.fr/cafe/Manuel.Bronstein/pmint/index.html

    For more information on the implemented algorithm refer to:

    .. [2] K. Geddes, L. Stefanus, On the Risch-Norman Integration
       Method and its Implementation in Maple, Proceedings of
       ISSAC\'89, ACM Press, 212-217.

    .. [3] J. H. Davenport, On the Parallel Risch Algorithm (I),
       Proceedings of EUROCAM\'82, LNCS 144, Springer, 144-157.

    .. [4] J. H. Davenport, On the Parallel Risch Algorithm (III):
       Use of Tangents, SIGSAM Bulletin 16 (1982), 3-6.

    .. [5] J. H. Davenport, B. M. Trager, On the Parallel Risch
       Algorithm (II), ACM Transactions on Mathematical
       Software 11 (1985), 356-362.

    See Also
    ========

    sympy.integrals.integrals.Integral.doit
    sympy.integrals.integrals.Integral
    sympy.integrals.heurisch.components
    '''
    pass
# WARNING: Decompyle incomplete
