# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lie_group.pyc (Python 3.11)

'''
This module contains the implementation of the internal helper functions for the lie_group hint for
dsolve. These helper functions apply different heuristics on the given equation
and return the solution. These functions are used by :py:meth:`sympy.solvers.ode.single.LieGroup`

References
=========

- `abaco1_simple`, `function_sum` and `chi`  are referenced from E.S Cheb-Terrab, L.G.S Duarte
and L.A,C.P da Mota, Computer Algebra Solving of First Order ODEs Using
Symmetry Methods, pp. 7 - pp. 8

- `abaco1_product`, `abaco2_similar`, `abaco2_unique_unknown`, `linear`  and `abaco2_unique_general`
are referenced from E.S. Cheb-Terrab, A.D. Roche, Symmetries and First Order
ODE Patterns, pp. 7 - pp. 12

- `bivariate` from Lie Groups and Differential Equations pp. 327 - pp. 329

'''
from itertools import islice
from sympy.core import Add, S, Mul, Pow
from sympy.core.exprtools import factor_terms
from sympy.core.function import Function, AppliedUndef, expand
from sympy.core.relational import Equality, Eq
from sympy.core.symbol import Symbol, Wild, Dummy, symbols
from sympy.functions import exp, log
from sympy.integrals.integrals import integrate
from sympy.polys import Poly
from sympy.polys.polytools import cancel, div
from sympy.simplify import collect, powsimp, separatevars, simplify
from sympy.solvers import solve
from sympy.solvers.pde import pdsolve
from sympy.utilities import numbered_symbols
from sympy.solvers.deutils import _preprocess, ode_order
from ode import checkinfsol
lie_heuristics = ('abaco1_simple', 'abaco1_product', 'abaco2_similar', 'abaco2_unique_unknown', 'abaco2_unique_general', 'linear', 'function_sum', 'bivariate', 'chi')

def _ode_lie_group_try_heuristic(eq, heuristic, func, match, inf):
    pass
# WARNING: Decompyle incomplete


def _ode_lie_group(s, func, order, match):
    heuristics = lie_heuristics
    inf = { }
    f = func.func
    x = func.args[0]
    df = func.diff(x)
    xi = Function('xi')
    eta = Function('eta')
    xis = match['xi']
    etas = match['eta']
    y = match.pop('y', None)
    if y:
        h = -simplify(match[match['d']] / match[match['e']])
        y = y
    else:
        y = Dummy('y')
        h = s.subs(func, y)
# WARNING: Decompyle incomplete


def infinitesimals(eq, func, order, hint, match = (None, None, 'default', None)):
    """
    The infinitesimal functions of an ordinary differential equation, `\\xi(x,y)`
    and `\\eta(x,y)`, are the infinitesimals of the Lie group of point transformations
    for which the differential equation is invariant. So, the ODE `y'=f(x,y)`
    would admit a Lie group `x^*=X(x,y;\\varepsilon)=x+\\varepsilon\\xi(x,y)`,
    `y^*=Y(x,y;\\varepsilon)=y+\\varepsilon\\eta(x,y)` such that `(y^*)'=f(x^*, y^*)`.
    A change of coordinates, to `r(x,y)` and `s(x,y)`, can be performed so this Lie group
    becomes the translation group, `r^*=r` and `s^*=s+\\varepsilon`.
    They are tangents to the coordinate curves of the new system.

    Consider the transformation `(x, y) \\to (X, Y)` such that the
    differential equation remains invariant. `\\xi` and `\\eta` are the tangents to
    the transformed coordinates `X` and `Y`, at `\\varepsilon=0`.

    .. math:: \\left(\\frac{\\partial X(x,y;\\varepsilon)}{\\partial\\varepsilon
                }\\right)|_{\\varepsilon=0} = \\xi,
              \\left(\\frac{\\partial Y(x,y;\\varepsilon)}{\\partial\\varepsilon
                }\\right)|_{\\varepsilon=0} = \\eta,

    The infinitesimals can be found by solving the following PDE:

        >>> from sympy import Function, Eq, pprint
        >>> from sympy.abc import x, y
        >>> xi, eta, h = map(Function, ['xi', 'eta', 'h'])
        >>> h = h(x, y)  # dy/dx = h
        >>> eta = eta(x, y)
        >>> xi = xi(x, y)
        >>> genform = Eq(eta.diff(x) + (eta.diff(y) - xi.diff(x))*h
        ... - (xi.diff(y))*h**2 - xi*(h.diff(x)) - eta*(h.diff(y)), 0)
        >>> pprint(genform)
        /d               d           \\                     d              2       d                       d             d
        |--(eta(x, y)) - --(xi(x, y))|*h(x, y) - eta(x, y)*--(h(x, y)) - h (x, y)*--(xi(x, y)) - xi(x, y)*--(h(x, y)) + --(eta(x, y)) = 0
        \\dy              dx          /                     dy                     dy                      dx            dx

    Solving the above mentioned PDE is not trivial, and can be solved only by
    making intelligent assumptions for `\\xi` and `\\eta` (heuristics). Once an
    infinitesimal is found, the attempt to find more heuristics stops. This is done to
    optimise the speed of solving the differential equation. If a list of all the
    infinitesimals is needed, ``hint`` should be flagged as ``all``, which gives
    the complete list of infinitesimals. If the infinitesimals for a particular
    heuristic needs to be found, it can be passed as a flag to ``hint``.

    Examples
    ========

    >>> from sympy import Function
    >>> from sympy.solvers.ode.lie_group import infinitesimals
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = f(x).diff(x) - x**2*f(x)
    >>> infinitesimals(eq)
    [{eta(x, f(x)): exp(x**3/3), xi(x, f(x)): 0}]

    References
    ==========

    - Solving differential equations by Symmetry Groups,
      John Starrett, pp. 1 - pp. 14

    """
    pass
# WARNING: Decompyle incomplete


def lie_heuristic_abaco1_simple(match, comp = (False,)):
