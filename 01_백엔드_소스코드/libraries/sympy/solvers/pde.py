# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pde.pyc (Python 3.11)

"""
This module contains pdsolve() and different helper functions that it
uses. It is heavily inspired by the ode module and hence the basic
infrastructure remains the same.

**Functions in this module**

    These are the user functions in this module:

    - pdsolve()     - Solves PDE's
    - classify_pde() - Classifies PDEs into possible hints for dsolve().
    - pde_separate() - Separate variables in partial differential equation either by
                       additive or multiplicative separation approach.

    These are the helper functions in this module:

    - pde_separate_add() - Helper function for searching additive separable solutions.
    - pde_separate_mul() - Helper function for searching multiplicative
                           separable solutions.

**Currently implemented solver methods**

The following methods are implemented for solving partial differential
equations.  See the docstrings of the various pde_hint() functions for
more information on each (run help(pde)):

  - 1st order linear homogeneous partial differential equations
    with constant coefficients.
  - 1st order linear general partial differential equations
    with constant coefficients.
  - 1st order linear partial differential equations with
    variable coefficients.

"""
from functools import reduce
from itertools import combinations_with_replacement
from sympy.simplify import simplify
from sympy.core import Add, S
from sympy.core.function import Function, expand, AppliedUndef, Subs
from sympy.core.relational import Equality, Eq
from sympy.core.symbol import Symbol, Wild, symbols
from sympy.functions import exp
from sympy.integrals.integrals import Integral, integrate
from sympy.utilities.iterables import has_dups, is_sequence
from sympy.utilities.misc import filldedent
from sympy.solvers.deutils import _preprocess, ode_order, _desolve
from sympy.solvers.solvers import solve
from sympy.simplify.radsimp import collect
import operator
allhints = ('1st_linear_constant_coeff_homogeneous', '1st_linear_constant_coeff', '1st_linear_constant_coeff_Integral', '1st_linear_variable_coeff')

def pdsolve(eq, func, hint, dict, solvefun = (None, 'default', False, None), **kwargs):
    '''
    Solves any (supported) kind of partial differential equation.

    **Usage**

        pdsolve(eq, f(x,y), hint) -> Solve partial differential equation
        eq for function f(x,y), using method hint.

    **Details**

        ``eq`` can be any supported partial differential equation (see
            the pde docstring for supported methods).  This can either
            be an Equality, or an expression, which is assumed to be
            equal to 0.

        ``f(x,y)`` is a function of two variables whose derivatives in that
            variable make up the partial differential equation. In many
            cases it is not necessary to provide this; it will be autodetected
            (and an error raised if it could not be detected).

        ``hint`` is the solving method that you want pdsolve to use.  Use
            classify_pde(eq, f(x,y)) to get all of the possible hints for
            a PDE.  The default hint, \'default\', will use whatever hint
            is returned first by classify_pde().  See Hints below for
            more options that you can use for hint.

        ``solvefun`` is the convention used for arbitrary functions returned
            by the PDE solver. If not set by the user, it is set by default
            to be F.

    **Hints**

        Aside from the various solving methods, there are also some
        meta-hints that you can pass to pdsolve():

        "default":
                This uses whatever hint is returned first by
                classify_pde(). This is the default argument to
                pdsolve().

        "all":
                To make pdsolve apply all relevant classification hints,
                use pdsolve(PDE, func, hint="all").  This will return a
                dictionary of hint:solution terms.  If a hint causes
                pdsolve to raise the NotImplementedError, value of that
                hint\'s key will be the exception object raised.  The
                dictionary will also include some special keys:

                - order: The order of the PDE.  See also ode_order() in
                  deutils.py
                - default: The solution that would be returned by
                  default.  This is the one produced by the hint that
                  appears first in the tuple returned by classify_pde().

        "all_Integral":
                This is the same as "all", except if a hint also has a
                corresponding "_Integral" hint, it only returns the
                "_Integral" hint.  This is useful if "all" causes
                pdsolve() to hang because of a difficult or impossible
                integral.  This meta-hint will also be much faster than
                "all", because integrate() is an expensive routine.

        See also the classify_pde() docstring for more info on hints,
        and the pde docstring for a list of all supported hints.

    **Tips**
        - You can declare the derivative of an unknown function this way:

            >>> from sympy import Function, Derivative
            >>> from sympy.abc import x, y # x and y are the independent variables
            >>> f = Function("f")(x, y) # f is a function of x and y
            >>> # fx will be the partial derivative of f with respect to x
            >>> fx = Derivative(f, x)
            >>> # fy will be the partial derivative of f with respect to y
            >>> fy = Derivative(f, y)

        - See test_pde.py for many tests, which serves also as a set of
          examples for how to use pdsolve().
        - pdsolve always returns an Equality class (except for the case
          when the hint is "all" or "all_Integral"). Note that it is not possible
          to get an explicit solution for f(x, y) as in the case of ODE\'s
        - Do help(pde.pde_hintname) to get help more information on a
          specific hint


    Examples
    ========

    >>> from sympy.solvers.pde import pdsolve
    >>> from sympy import Function, Eq
    >>> from sympy.abc import x, y
    >>> f = Function(\'f\')
    >>> u = f(x, y)
    >>> ux = u.diff(x)
    >>> uy = u.diff(y)
    >>> eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)
    >>> pdsolve(eq)
    Eq(f(x, y), F(3*x - 2*y)*exp(-2*x/13 - 3*y/13))

    '''
    if not solvefun:
        solvefun = Function('F')
# WARNING: Decompyle incomplete


def _helper_simplify(eq, hint, func, order, match, solvefun):
    '''Helper function of pdsolve that calls the respective
    pde functions to solve for the partial differential
    equations. This minimizes the computation in
    calling _desolve multiple times.
    '''
    if hint.endswith('_Integral'):
        solvefunc = globals()['pde_' + hint[:-len('_Integral')]]
    else:
        solvefunc = globals()['pde_' + hint]
    return _handle_Integral(solvefunc(eq, func, order, match, solvefun), func, order, hint)


def _handle_Integral(expr, func, order, hint):
    '''
    Converts a solution with integrals in it into an actual solution.

    Simplifies the integral mainly using doit()
    '''
    if hint.endswith('_Integral'):
        return expr
    if None == '1st_linear_constant_coeff':
        return simplify(expr.doit())


def classify_pde(eq = None, func = (None, False), dict = {
    'prep': True }, *, prep, **kwargs):
    '''
    Returns a tuple of possible pdsolve() classifications for a PDE.

    The tuple is ordered so that first item is the classification that
    pdsolve() uses to solve the PDE by default.  In general,
    classifications near the beginning of the list will produce
    better solutions faster than those near the end, though there are
    always exceptions.  To make pdsolve use a different classification,
    use pdsolve(PDE, func, hint=<classification>).  See also the pdsolve()
    docstring for different meta-hints you can use.

    If ``dict`` is true, classify_pde() will return a dictionary of
    hint:match expression terms. This is intended for internal use by
    pdsolve().  Note that because dictionaries are ordered arbitrarily,
    this will most likely not be in the same order as the tuple.

    You can get help on different hints by doing help(pde.pde_hintname),
    where hintname is the name of the hint without "_Integral".

    See sympy.pde.allhints or the sympy.pde docstring for a list of all
    supported hints that can be returned from classify_pde.


    Examples
    ========

    >>> from sympy.solvers.pde import classify_pde
    >>> from sympy import Function, Eq
    >>> from sympy.abc import x, y
    >>> f = Function(\'f\')
    >>> u = f(x, y)
    >>> ux = u.diff(x)
    >>> uy = u.diff(y)
    >>> eq = Eq(1 + (2*(ux/u)) + (3*(uy/u)), 0)
    >>> classify_pde(eq)
    (\'1st_linear_constant_coeff_homogeneous\',)
    '''
    pass
# WARNING: Decompyle incomplete


def checkpdesol(pde, sol, func, solve_for_func = (None, True)):
    """
    Checks if the given solution satisfies the partial differential
    equation.

    pde is the partial differential equation which can be given in the
    form of an equation or an expression. sol is the solution for which
    the pde is to be checked. This can also be given in an equation or
    an expression form. If the function is not provided, the helper
    function _preprocess from deutils is used to identify the function.

    If a sequence of solutions is passed, the same sort of container will be
    used to return the result for each solution.

    The following methods are currently being implemented to check if the
    solution satisfies the PDE:

        1. Directly substitute the solution in the PDE and check. If the
           solution has not been solved for f, then it will solve for f
           provided solve_for_func has not been set to False.

    If the solution satisfies the PDE, then a tuple (True, 0) is returned.
    Otherwise a tuple (False, expr) where expr is the value obtained
    after substituting the solution in the PDE. However if a known solution
    returns False, it may be due to the inability of doit() to simplify it to zero.

    Examples
    ========

    >>> from sympy import Function, symbols
    >>> from sympy.solvers.pde import checkpdesol, pdsolve
    >>> x, y = symbols('x y')
    >>> f = Function('f')
    >>> eq = 2*f(x,y) + 3*f(x,y).diff(x) + 4*f(x,y).diff(y)
    >>> sol = pdsolve(eq)
    >>> assert checkpdesol(eq, sol)[0]
    >>> eq = x*f(x,y) + f(x,y).diff(x)
    >>> checkpdesol(eq, sol)
    (False, (x*F(4*x - 3*y) - 6*F(4*x - 3*y)/25 + 4*Subs(Derivative(F(_xi_1), _xi_1), _xi_1, 4*x - 3*y))*exp(-6*x/25 - 8*y/25))
    """
    pass
# WARNING: Decompyle incomplete


def pde_1st_linear_constant_coeff_homogeneous(eq, func, order, match, solvefun):
    '''
    Solves a first order linear homogeneous
    partial differential equation with constant coefficients.

    The general form of this partial differential equation is

    .. math:: a \\frac{\\partial f(x,y)}{\\partial x}
              + b \\frac{\\partial f(x,y)}{\\partial y} + c f(x,y) = 0

    where `a`, `b` and `c` are constants.

    The general solution is of the form:

    .. math::
        f(x, y) = F(- a y + b x ) e^{- \\frac{c (a x + b y)}{a^2 + b^2}}

    and can be found in SymPy with ``pdsolve``::

        >>> from sympy.solvers import pdsolve
        >>> from sympy.abc import x, y, a, b, c
        >>> from sympy import Function, pprint
        >>> f = Function(\'f\')
        >>> u = f(x,y)
        >>> ux = u.diff(x)
        >>> uy = u.diff(y)
        >>> genform = a*ux + b*uy + c*u
        >>> pprint(genform)
          d               d
        a*--(f(x, y)) + b*--(f(x, y)) + c*f(x, y)
          dx              dy

        >>> pprint(pdsolve(genform))
                                 -c*(a*x + b*y)
                                 ---------------
                                      2    2
                                     a  + b
        f(x, y) = F(-a*y + b*x)*e

    Examples
    ========

    >>> from sympy import pdsolve
    >>> from sympy import Function, pprint
    >>> from sympy.abc import x,y
    >>> f = Function(\'f\')
    >>> pdsolve(f(x,y) + f(x,y).diff(x) + f(x,y).diff(y))
    Eq(f(x, y), F(x - y)*exp(-x/2 - y/2))
    >>> pprint(pdsolve(f(x,y) + f(x,y).diff(x) + f(x,y).diff(y)))
                          x   y
                        - - - -
                          2   2
    f(x, y) = F(x - y)*e

    References
    ==========

    - Viktor Grigoryan, "Partial Differential Equations"
      Math 124A - Fall 2010, pp.7

    '''
    f = func.func
    x = func.args[0]
    y = func.args[1]
    b = match[match['b']]
    c = match[match['c']]
    d = match[match['d']]
    return Eq(f(x, y), exp((-S(d) / (b ** 2 + c ** 2)) * (b * x + c * y)) * solvefun(c * x - b * y))


def pde_1st_linear_constant_coeff(eq, func, order, match, solvefun):
    '''
    Solves a first order linear partial differential equation
    with constant coefficients.

    The general form of this partial differential equation is

    .. math:: a \\frac{\\partial f(x,y)}{\\partial x}
              + b \\frac{\\partial f(x,y)}{\\partial y}
              + c f(x,y) = G(x,y)

    where `a`, `b` and `c` are constants and `G(x, y)` can be an arbitrary
    function in `x` and `y`.

    The general solution of the PDE is:

    .. math::
        f(x, y) = \\left. \\left[F(\\eta) + \\frac{1}{a^2 + b^2}
        \\int\\limits^{a x + b y} G\\left(\\frac{a \\xi + b \\eta}{a^2 + b^2},
        \\frac{- a \\eta + b \\xi}{a^2 + b^2} \\right)
        e^{\\frac{c \\xi}{a^2 + b^2}}\\, d\\xi\\right]
        e^{- \\frac{c \\xi}{a^2 + b^2}}
        \\right|_{\\substack{\\eta=- a y + b x\\\\ \\xi=a x + b y }}\\, ,

    where `F(\\eta)` is an arbitrary single-valued function. The solution
    can be found in SymPy with ``pdsolve``::

        >>> from sympy.solvers import pdsolve
        >>> from sympy.abc import x, y, a, b, c
        >>> from sympy import Function, pprint
        >>> f = Function(\'f\')
        >>> G = Function(\'G\')
        >>> u = f(x, y)
        >>> ux = u.diff(x)
        >>> uy = u.diff(y)
        >>> genform = a*ux + b*uy + c*u - G(x,y)
        >>> pprint(genform)
          d               d
        a*--(f(x, y)) + b*--(f(x, y)) + c*f(x, y) - G(x, y)
          dx              dy
        >>> pprint(pdsolve(genform, hint=\'1st_linear_constant_coeff_Integral\'))
                  //          a*x + b*y                                             \\         \\|
                  ||              /                                                 |         ||
                  ||             |                                                  |         ||
                  ||             |                                      c*xi        |         ||
                  ||             |                                     -------      |         ||
                  ||             |                                      2    2      |         ||
                  ||             |      /a*xi + b*eta  -a*eta + b*xi\\  a  + b       |         ||
                  ||             |     G|------------, -------------|*e        d(xi)|         ||
                  ||             |      |   2    2         2    2   |               |         ||
                  ||             |      \\  a  + b         a  + b    /               |  -c*xi  ||
                  ||             |                                                  |  -------||
                  ||            /                                                   |   2    2||
                  ||                                                                |  a  + b ||
        f(x, y) = ||F(eta) + -------------------------------------------------------|*e       ||
                  ||                                  2    2                        |         ||
                  \\\\                                 a  + b                         /         /|eta=-a*y + b*x, xi=a*x + b*y

    Examples
    ========

    >>> from sympy.solvers.pde import pdsolve
    >>> from sympy import Function, pprint, exp
    >>> from sympy.abc import x,y
    >>> f = Function(\'f\')
    >>> eq = -2*f(x,y).diff(x) + 4*f(x,y).diff(y) + 5*f(x,y) - exp(x + 3*y)
    >>> pdsolve(eq)
    Eq(f(x, y), (F(4*x + 2*y)*exp(x/2) + exp(x + 4*y)/15)*exp(-y))

    References
    ==========

    - Viktor Grigoryan, "Partial Differential Equations"
      Math 124A - Fall 2010, pp.7

    '''
    (xi, eta) = symbols('xi eta')
    f = func.func
    x = func.args[0]
    y = func.args[1]
    b = match[match['b']]
    c = match[match['c']]
    d = match[match['d']]
    e = -match[match['e']]
    expterm = exp((-S(d) / (b ** 2 + c ** 2)) * xi)
    functerm = solvefun(eta)
    solvedict = solve((b * x + c * y - xi, c * x - b * y - eta), x, y)
    genterm = (1 / S(b ** 2 + c ** 2)) * Integral(((1 / expterm) * e).subs(solvedict), (xi, b * x + c * y))
    return Eq(f(x, y), Subs(expterm * (functerm + genterm), (eta, xi), (c * x - b * y, b * x + c * y)))


def pde_1st_linear_variable_coeff(eq, func, order, match, solvefun):
    '''
    Solves a first order linear partial differential equation
    with variable coefficients. The general form of this partial
    differential equation is

    .. math:: a(x, y) \\frac{\\partial f(x, y)}{\\partial x}
                + b(x, y) \\frac{\\partial f(x, y)}{\\partial y}
                + c(x, y) f(x, y) = G(x, y)

    where `a(x, y)`, `b(x, y)`, `c(x, y)` and `G(x, y)` are arbitrary
    functions in `x` and `y`. This PDE is converted into an ODE by
    making the following transformation:

    1. `\\xi` as `x`

    2. `\\eta` as the constant in the solution to the differential
       equation `\\frac{dy}{dx} = -\\frac{b}{a}`

    Making the previous substitutions reduces it to the linear ODE

    .. math:: a(\\xi, \\eta)\\frac{du}{d\\xi} + c(\\xi, \\eta)u - G(\\xi, \\eta) = 0

    which can be solved using ``dsolve``.

    >>> from sympy.abc import x, y
    >>> from sympy import Function, pprint
    >>> a, b, c, G, f= [Function(i) for i in [\'a\', \'b\', \'c\', \'G\', \'f\']]
    >>> u = f(x,y)
    >>> ux = u.diff(x)
    >>> uy = u.diff(y)
    >>> genform = a(x, y)*u + b(x, y)*ux + c(x, y)*uy - G(x,y)
    >>> pprint(genform)
                                         d                     d
    -G(x, y) + a(x, y)*f(x, y) + b(x, y)*--(f(x, y)) + c(x, y)*--(f(x, y))
                                         dx                    dy


    Examples
    ========

    >>> from sympy.solvers.pde import pdsolve
    >>> from sympy import Function, pprint
    >>> from sympy.abc import x,y
    >>> f = Function(\'f\')
    >>> eq =  x*(u.diff(x)) - y*(u.diff(y)) + y**2*u - y**2
    >>> pdsolve(eq)
    Eq(f(x, y), F(x*y)*exp(y**2/2) + 1)

    References
    ==========

    - Viktor Grigoryan, "Partial Differential Equations"
      Math 124A - Fall 2010, pp.7

    '''
    dsolve = dsolve
    import sympy.solvers.ode
    (xi, eta) = symbols('xi eta')
    f = func.func
    x = func.args[0]
    y = func.args[1]
    b = match[match['b']]
    c = match[match['c']]
    d = match[match['d']]
    e = -match[match['e']]
    if not d:
        if not b or c:
            if c:
                
                try:
                    tsol = integrate(e / c, y)
                    return Eq(f(x, y), solvefun(x) + tsol)
                except NotImplementedError:
                    raise NotImplementedError('Unable to find a solution due to inability of integrate')
                    if b:
                        
                        try:
                            tsol = integrate(e / b, x)
                            return Eq(f(x, y), solvefun(y) + tsol)
                        except NotImplementedError:
                            raise NotImplementedError('Unable to find a solution due to inability of integrate')
                            if not c:
                                plode = f(x).diff(x) * b + d * f(x) - e
                                sol = dsolve(plode, f(x))
                                syms = sol.free_symbols - plode.free_symbols - {
                                    x,
                                    y}
                                rhs = _simplify_variable_coeff(sol.rhs, syms, solvefun, y)
                                return Eq(f(x, y), rhs)
                            if not None:
                                plode = f(y).diff(y) * c + d * f(y) - e
                                sol = dsolve(plode, f(y))
                                syms = sol.free_symbols - plode.free_symbols - {
                                    x,
                                    y}
                                rhs = _simplify_variable_coeff(sol.rhs, syms, solvefun, x)
                                return Eq(f(x, y), rhs)
                            dummy = None('d')
                            h = (c / b).subs(y, dummy(x))
                            sol = dsolve(dummy(x).diff(x) - h, dummy(x))
                            if isinstance(sol, list):
                                sol = sol[0]
                            solsym = sol.free_symbols - h.free_symbols - {
                                x,
                                y}
                            if len(solsym) == 1:
                                solsym = solsym.pop()
                                etat = solve(sol, solsym)[0].subs(dummy(x), y)
                                ysub = solve(eta - etat, y)[0]
                                deq = (b * f(x).diff(x) + d * f(x) - e).subs(y, ysub)
                                final = dsolve(deq, f(x), hint = '1st_linear').rhs
                                if isinstance(final, list):
                                    final = final[0]
                                finsyms = final.free_symbols - deq.free_symbols - {
                                    x,
                                    y}
                                rhs = _simplify_variable_coeff(final, finsyms, solvefun, etat)
                                return Eq(f(x, y), rhs)
                            raise None('Cannot solve the partial differential equation due to inability of constantsimp')




def _simplify_variable_coeff(sol, syms, func, funcarg):
    '''
    Helper function to replace constants by functions in 1st_linear_variable_coeff
    '''
    eta = Symbol('eta')
    if len(syms) == 1:
        sym = syms.pop()
        final = sol.subs(sym, func(funcarg))
    else:
        for sym in syms:
            final = sol.subs(sym, func(funcarg))
            return simplify(final.subs(eta, funcarg))


def pde_separate(eq, fun, sep, strategy = ('mul',)):
    """Separate variables in partial differential equation either by additive
    or multiplicative separation approach. It tries to rewrite an equation so
    that one of the specified variables occurs on a different side of the
    equation than the others.

    :param eq: Partial differential equation

    :param fun: Original function F(x, y, z)

    :param sep: List of separated functions [X(x), u(y, z)]

    :param strategy: Separation strategy. You can choose between additive
        separation ('add') and multiplicative separation ('mul') which is
        default.

    Examples
    ========

    >>> from sympy import E, Eq, Function, pde_separate, Derivative as D
    >>> from sympy.abc import x, t
    >>> u, X, T = map(Function, 'uXT')

    >>> eq = Eq(D(u(x, t), x), E**(u(x, t))*D(u(x, t), t))
    >>> pde_separate(eq, u(x, t), [X(x), T(t)], strategy='add')
    [exp(-X(x))*Derivative(X(x), x), exp(T(t))*Derivative(T(t), t)]

    >>> eq = Eq(D(u(x, t), x, 2), D(u(x, t), t, 2))
    >>> pde_separate(eq, u(x, t), [X(x), T(t)], strategy='mul')
    [Derivative(X(x), (x, 2))/X(x), Derivative(T(t), (t, 2))/T(t)]

    See Also
    ========
    pde_separate_add, pde_separate_mul
    """
    do_add = False
    if strategy == 'add':
        do_add = True
    elif strategy == 'mul':
        do_add = False
    else:
        raise ValueError('Unknown strategy: %s' % strategy)
    if isinstance(eq, Equality):
        if eq.rhs != 0:
            return pde_separate(Eq(eq.lhs - eq.rhs, 0), fun, sep, strategy)
    return pde_separate(Eq(eq, 0), fun, sep, strategy)
    if eq.rhs != 0:
        raise ValueError('Value should be 0')
    orig_args = list(fun.args)
    subs_args = sep()
    if len(subs_args) != len(orig_args):
        raise ValueError('Variable counts do not match')
    if has_dups(subs_args):
        raise ValueError('Duplicate substitution arguments detected')
    if set(orig_args) != set(subs_args):
        raise ValueError('Arguments do not match')
    result = eq.lhs.subs(fun, functions).doit()
    if not do_add:
        eq = 0
        for i in result.args:
            eq += i / functions
            result = eq
            svar = subs_args[0]
            dvar = subs_args[1:]
            return _separate(result, svar, dvar)


def pde_separate_add(eq, fun, sep):
    """
    Helper function for searching additive separable solutions.

    Consider an equation of two independent variables x, y and a dependent
    variable w, we look for the product of two functions depending on different
    arguments:

    `w(x, y, z) = X(x) + y(y, z)`

    Examples
    ========

    >>> from sympy import E, Eq, Function, pde_separate_add, Derivative as D
    >>> from sympy.abc import x, t
    >>> u, X, T = map(Function, 'uXT')

    >>> eq = Eq(D(u(x, t), x), E**(u(x, t))*D(u(x, t), t))
    >>> pde_separate_add(eq, u(x, t), [X(x), T(t)])
    [exp(-X(x))*Derivative(X(x), x), exp(T(t))*Derivative(T(t), t)]

    """
    return pde_separate(eq, fun, sep, strategy = 'add')


def pde_separate_mul(eq, fun, sep):
    """
    Helper function for searching multiplicative separable solutions.

    Consider an equation of two independent variables x, y and a dependent
    variable w, we look for the product of two functions depending on different
    arguments:

    `w(x, y, z) = X(x)*u(y, z)`

    Examples
    ========

    >>> from sympy import Function, Eq, pde_separate_mul, Derivative as D
    >>> from sympy.abc import x, y
    >>> u, X, Y = map(Function, 'uXY')

    >>> eq = Eq(D(u(x, y), x, 2), D(u(x, y), y, 2))
    >>> pde_separate_mul(eq, u(x, y), [X(x), Y(y)])
    [Derivative(X(x), (x, 2))/X(x), Derivative(Y(y), (y, 2))/Y(y)]

    """
    return pde_separate(eq, fun, sep, strategy = 'mul')


def _separate(eq, dep, others):
    '''Separate expression into two parts based on dependencies of variables.'''
    pass
# WARNING: Decompyle incomplete
