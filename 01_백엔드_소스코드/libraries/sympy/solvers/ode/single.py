# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: single.pyc (Python 3.11)

from __future__ import annotations
from typing import ClassVar, Iterator
from riccati import match_riccati, solve_riccati
from sympy.core import Add, S, Pow, Rational
from sympy.core.cache import cached_property
from sympy.core.exprtools import factor_terms
from sympy.core.expr import Expr
from sympy.core.function import AppliedUndef, Derivative, diff, Function, expand, Subs, _mexpand
from sympy.core.numbers import zoo
from sympy.core.relational import Equality, Eq
from sympy.core.symbol import Symbol, Dummy, Wild
from sympy.core.mul import Mul
from sympy.functions import exp, tan, log, sqrt, besselj, bessely, cbrt, airyai, airybi
from sympy.integrals import Integral
from sympy.polys import Poly
from sympy.polys.polytools import cancel, factor, degree
from sympy.simplify import collect, simplify, separatevars, logcombine, posify
from sympy.simplify.radsimp import fraction
from sympy.utilities import numbered_symbols
from sympy.solvers.solvers import solve
from sympy.solvers.deutils import ode_order, _preprocess
from sympy.polys.matrices.linsolve import _lin_eq2dict
from sympy.polys.solvers import PolyNonlinearError
from hypergeometric import equivalence_hypergeometric, match_2nd_2F1_hypergeometric, get_sol_2F1_hypergeometric, match_2nd_hypergeometric
from nonhomogeneous import _get_euler_characteristic_eq_sols, _get_const_characteristic_eq_sols, _solve_undetermined_coefficients, _solve_variation_of_parameters, _test_term, _undetermined_coefficients_match, _get_simplified_sol
from lie_group import _ode_lie_group

class ODEMatchError(NotImplementedError):
    '''Raised if a SingleODESolver is asked to solve an ODE it does not match'''
    pass


class SingleODEProblem:
    """Represents an ordinary differential equation (ODE)

    This class is used internally in the by dsolve and related
    functions/classes so that properties of an ODE can be computed
    efficiently.

    Examples
    ========

    This class is used internally by dsolve. To instantiate an instance
    directly first define an ODE problem:

    >>> from sympy import Function, Symbol
    >>> x = Symbol('x')
    >>> f = Function('f')
    >>> eq = f(x).diff(x, 2)

    Now you can create a SingleODEProblem instance and query its properties:

    >>> from sympy.solvers.ode.single import SingleODEProblem
    >>> problem = SingleODEProblem(f(x).diff(x), f(x), x)
    >>> problem.eq
    Derivative(f(x), x)
    >>> problem.func
    f(x)
    >>> problem.sym
    x
    """
    eq = None
    func = None
    sym = None
    _order = None
    _eq_expanded = None
    _eq_preprocessed = None
    _eq_high_order_free = None
    
    def __init__(self, eq, func, sym, prep = (True,), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    order = (lambda self = None: ode_order(self.eq, self.func))()
    eq_preprocessed = (lambda self = None: self._get_eq_preprocessed())()
    eq_high_order_free = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    eq_expanded = (lambda self = None: expand(self.eq_preprocessed))()
    
    def _get_eq_preprocessed(self = None):
        if self.prep:
            (process_eq, process_func) = _preprocess(self.eq, self.func)
            if process_func != self.func:
                raise ValueError
        else:
            process_eq = self.eq
        return process_eq

    
    def get_numbered_constants(self = None, num = None, start = None, prefix = (1, 1, 'C')):
        '''
        Returns a list of constants that do not occur
        in eq already.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_numbered_constants(self = None, start = None, prefix = None):
        '''
        Returns an iterator of constants that do not occur
        in eq already.
        '''
        atom_set = self.eq.free_symbols
        func_set = self.eq.atoms(Function)
        if func_set:
            (lambda .0: pass# WARNING: Decompyle incomplete
) |= func_set()
        return numbered_symbols(start = start, prefix = prefix, exclude = atom_set)

    is_autonomous = (lambda self: u = Dummy('u')x = self.symsyms = self.eq.subs(self.func, u).free_symbolsx not in syms)()
    
    def get_linear_coefficients(self, eq, func, order):
        """
        Matches a differential equation to the linear form:

        .. math:: a_n(x) y^{(n)} + \\cdots + a_1(x)y' + a_0(x) y + B(x) = 0

        Returns a dict of order:coeff terms, where order is the order of the
        derivative on each term, and coeff is the coefficient of that derivative.
        The key ``-1`` holds the function `B(x)`. Returns ``None`` if the ODE is
        not linear.  This function assumes that ``func`` has already been checked
        to be good.

        Examples
        ========

        >>> from sympy import Function, cos, sin
        >>> from sympy.abc import x
        >>> from sympy.solvers.ode.single import SingleODEProblem
        >>> f = Function('f')
        >>> eq = f(x).diff(x, 3) + 2*f(x).diff(x) + \\
        ... x*f(x).diff(x, 2) + cos(x)*f(x).diff(x) + x - f(x) - \\
        ... sin(x)
        >>> obj = SingleODEProblem(eq, f(x), x)
        >>> obj.get_linear_coefficients(eq, f(x), 3)
        {-1: x - sin(x), 0: -1, 1: cos(x) + 2, 2: x, 3: 1}
        >>> eq = f(x).diff(x, 3) + 2*f(x).diff(x) + \\
        ... x*f(x).diff(x, 2) + cos(x)*f(x).diff(x) + x - f(x) - \\
        ... sin(f(x))
        >>> obj = SingleODEProblem(eq, f(x), x)
        >>> obj.get_linear_coefficients(eq, f(x), 3) == None
        True

        """
        pass
    # WARNING: Decompyle incomplete



class SingleODESolver:
    has_integral: 'ClassVar[bool]' = "\n    Base class for Single ODE solvers.\n\n    Subclasses should implement the _matches and _get_general_solution\n    methods. This class is not intended to be instantiated directly but its\n    subclasses are as part of dsolve.\n\n    Examples\n    ========\n\n    You can use a subclass of SingleODEProblem to solve a particular type of\n    ODE. We first define a particular ODE problem:\n\n    >>> from sympy import Function, Symbol\n    >>> x = Symbol('x')\n    >>> f = Function('f')\n    >>> eq = f(x).diff(x, 2)\n\n    Now we solve this problem using the NthAlgebraic solver which is a\n    subclass of SingleODESolver:\n\n    >>> from sympy.solvers.ode.single import NthAlgebraic, SingleODEProblem\n    >>> problem = SingleODEProblem(eq, f(x), x)\n    >>> solver = NthAlgebraic(problem)\n    >>> solver.get_general_solution()\n    [Eq(f(x), _C*x + _C)]\n\n    The normal way to solve an ODE is to use dsolve (which would use\n    NthAlgebraic and other solvers internally). When using dsolve a number of\n    other things are done such as evaluating integrals, simplifying the\n    solution and renumbering the constants:\n\n    >>> from sympy import dsolve\n    >>> dsolve(eq, hint='nth_algebraic')\n    Eq(f(x), C1 + C2*x)\n    "
    ode_problem = None
    _matched: 'bool | None' = None
    order: 'list | None' = None
    
    def __init__(self, ode_problem):
        self.ode_problem = ode_problem

    
    def matches(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_general_solution(self = None, *, simplify):
        if not self.matches():
            msg = '%s solver cannot solve:\n%s'
            raise ODEMatchError(msg % (self.hint, self.ode_problem.eq))
        return self._get_general_solution(simplify_flag = simplify)

    
    def _matches(self = None):
        msg = 'Subclasses of SingleODESolver should implement matches.'
        raise NotImplementedError(msg)

    
    def _get_general_solution(self = None, *, simplify_flag):
        msg = 'Subclasses of SingleODESolver should implement get_general_solution.'
        raise NotImplementedError(msg)



class SinglePatternODESolver(SingleODESolver):
    '''Superclass for ODE solvers based on pattern matching'''
    
    def wilds(self):
        prob = self.ode_problem
        f = prob.func.func
        x = prob.sym
        order = prob.order
        return self._wilds(f, x, order)

    
    def wilds_match(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _matches(self):
        eq = self.ode_problem.eq_expanded
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        order = self.ode_problem.order
        df = f(x).diff(x, order)
        if order not in (1, 2):
            return False
        pattern = None._equation(f(x), x, order)
        if not pattern.coeff(df).has(Wild):
            eq = expand(eq / eq.coeff(df))
        eq = eq.collect([
            f(x).diff(x),
            f(x)], func = cancel)
        self._wilds_match = eq.match(pattern)
        match = eq.match(pattern)
    # WARNING: Decompyle incomplete

    
    def _verify(self = None, fx = None):
        return True

    
    def _wilds(self, f, x, order):
        msg = 'Subclasses of SingleODESolver should implement _wilds'
        raise NotImplementedError(msg)

    
    def _equation(self, fx, x, order):
        msg = 'Subclasses of SingleODESolver should implement _equation'
        raise NotImplementedError(msg)



class NthAlgebraic(SingleODESolver):
    """
    Solves an `n`\\th order ordinary differential equation using algebra and
    integrals.

    There is no general form for the kind of equation that this can solve. The
    the equation is solved algebraically treating differentiation as an
    invertible algebraic function.

    Examples
    ========

    >>> from sympy import Function, dsolve, Eq
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = Eq(f(x) * (f(x).diff(x)**2 - 1), 0)
    >>> dsolve(eq, f(x), hint='nth_algebraic')
    [Eq(f(x), 0), Eq(f(x), C1 - x), Eq(f(x), C1 + x)]

    Note that this solver can return algebraic solutions that do not have any
    integration constants (f(x) = 0 in the above example).
    """
    hint = 'nth_algebraic'
    has_integral = True
    
    def _matches(self):
        '''
        Matches any differential equation that nth_algebraic can solve. Uses
        `sympy.solve` but teaches it how to integrate derivatives.

        This involves calling `sympy.solve` and does most of the work of finding a
        solution (apart from evaluating the integrals).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        return self.solutions

    _diffx_stored: 'dict[Symbol, type[Function]]' = { }
    _get_diffx = (lambda var: pass# WARNING: Decompyle incomplete
)()


class FirstExact(SinglePatternODESolver):
    '''
    Solves 1st order exact ordinary differential equations.

    A 1st order differential equation is called exact if it is the total
    differential of a function. That is, the differential equation

    .. math:: P(x, y) \\,\\partial{}x + Q(x, y) \\,\\partial{}y = 0

    is exact if there is some function `F(x, y)` such that `P(x, y) =
    \\partial{}F/\\partial{}x` and `Q(x, y) = \\partial{}F/\\partial{}y`.  It can
    be shown that a necessary and sufficient condition for a first order ODE
    to be exact is that `\\partial{}P/\\partial{}y = \\partial{}Q/\\partial{}x`.
    Then, the solution will be as given below::

        >>> from sympy import Function, Eq, Integral, symbols, pprint
        >>> x, y, t, x0, y0, C1= symbols(\'x,y,t,x0,y0,C1\')
        >>> P, Q, F= map(Function, [\'P\', \'Q\', \'F\'])
        >>> pprint(Eq(Eq(F(x, y), Integral(P(t, y), (t, x0, x)) +
        ... Integral(Q(x0, t), (t, y0, y))), C1))
                    x                y
                    /                /
                   |                |
        F(x, y) =  |  P(t, y) dt +  |  Q(x0, t) dt = C1
                   |                |
                  /                /
                  x0               y0

    Where the first partials of `P` and `Q` exist and are continuous in a
    simply connected region.

    A note: SymPy currently has no way to represent inert substitution on an
    expression, so the hint ``1st_exact_Integral`` will return an integral
    with `dy`.  This is supposed to represent the function that you are
    solving for.

    Examples
    ========

    >>> from sympy import Function, dsolve, cos, sin
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> dsolve(cos(f(x)) - (x*sin(f(x)) - f(x)**2)*f(x).diff(x),
    ... f(x), hint=\'1st_exact\')
    Eq(x*cos(f(x)) + f(x)**3/3, C1)

    References
    ==========

    - https://en.wikipedia.org/wiki/Exact_differential_equation
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 73

    # indirect doctest

    '''
    hint = '1st_exact'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        P = Wild('P', exclude = [
            f(x).diff(x)])
        Q = Wild('Q', exclude = [
            f(x).diff(x)])
        return (P, Q)

    
    def _equation(self, fx, x, order):
        (P, Q) = self.wilds()
        return P + Q * fx.diff(x)

    
    def _verify(self = None, fx = None):
        (P, Q) = self.wilds()
        x = self.ode_problem.sym
        y = Dummy('y')
        (m, n) = self.wilds_match()
        m = m.subs(fx, y)
        n = n.subs(fx, y)
        numerator = cancel(m.diff(y) - n.diff(x))
        if numerator.is_zero:
            return True
        factor_n = None(numerator / n)
        factor_m = cancel(-numerator / m)
        if y not in factor_n.free_symbols:
            factor = factor_n
            integration_variable = x
        elif x not in factor_m.free_symbols:
            factor = factor_m
            integration_variable = y
        else:
            return False
        factor = None(Integral(factor, integration_variable))
        m *= factor
        n *= factor
        self._wilds_match[P] = m.subs(y, fx)
        self._wilds_match[Q] = n.subs(y, fx)
        return True

    
    def _get_general_solution(self = None, *, simplify_flag):
        (m, n) = self.wilds_match()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        y = Dummy('y')
        m = m.subs(fx, y)
        n = n.subs(fx, y)
        gen_sol = Eq(Subs(Integral(m, x) + Integral(n - Integral(m, x).diff(y), y), y, fx), C1)
        return [
            gen_sol]



class FirstLinear(SinglePatternODESolver):
    '''
    Solves 1st order linear differential equations.

    These are differential equations of the form

    .. math:: dy/dx + P(x) y = Q(x)\\text{.}

    These kinds of differential equations can be solved in a general way.  The
    integrating factor `e^{\\int P(x) \\,dx}` will turn the equation into a
    separable equation.  The general solution is::

        >>> from sympy import Function, dsolve, Eq, pprint, diff, sin
        >>> from sympy.abc import x
        >>> f, P, Q = map(Function, [\'f\', \'P\', \'Q\'])
        >>> genform = Eq(f(x).diff(x) + P(x)*f(x), Q(x))
        >>> pprint(genform)
                    d
        P(x)*f(x) + --(f(x)) = Q(x)
                    dx
        >>> pprint(dsolve(genform, f(x), hint=\'1st_linear_Integral\'))
                /       /                   \\
                |      |                    |
                |      |         /          |     /
                |      |        |           |    |
                |      |        | P(x) dx   |  - | P(x) dx
                |      |        |           |    |
                |      |       /            |   /
        f(x) = |C1 +  | Q(x)*e           dx|*e
                |      |                    |
                \\     /                     /


    Examples
    ========

    >>> f = Function(\'f\')
    >>> pprint(dsolve(Eq(x*diff(f(x), x) - f(x), x**2*sin(x)),
    ... f(x), \'1st_linear\'))
    f(x) = x*(C1 - cos(x))

    References
    ==========

    - https://en.wikipedia.org/wiki/Linear_differential_equation#First-order_equation_with_variable_coefficients
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 92

    # indirect doctest

    '''
    hint = '1st_linear'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        P = Wild('P', exclude = [
            f(x)])
        Q = Wild('Q', exclude = [
            f(x),
            f(x).diff(x)])
        return (P, Q)

    
    def _equation(self, fx, x, order):
        (P, Q) = self.wilds()
        return fx.diff(x) + P * fx - Q

    
    def _get_general_solution(self = None, *, simplify_flag):
        (P, Q) = self.wilds_match()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        gensol = Eq(fx, (C1 + Integral(Q * exp(Integral(P, x)), x)) * exp(-Integral(P, x)))
        return [
            gensol]



class AlmostLinear(SinglePatternODESolver):
    '''
    Solves an almost-linear differential equation.

    The general form of an almost linear differential equation is

    .. math:: a(x) g\'(f(x)) f\'(x) + b(x) g(f(x)) + c(x)

    Here `f(x)` is the function to be solved for (the dependent variable).
    The substitution `g(f(x)) = u(x)` leads to a linear differential equation
    for `u(x)` of the form `a(x) u\' + b(x) u + c(x) = 0`. This can be solved
    for `u(x)` by the `first_linear` hint and then `f(x)` is found by solving
    `g(f(x)) = u(x)`.

    See Also
    ========
    :obj:`sympy.solvers.ode.single.FirstLinear`

    Examples
    ========

    >>> from sympy import dsolve, Function, pprint, sin, cos
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> d = f(x).diff(x)
    >>> eq = x*d + x*f(x) + 1
    >>> dsolve(eq, f(x), hint=\'almost_linear\')
    Eq(f(x), (C1 - Ei(x))*exp(-x))
    >>> pprint(dsolve(eq, f(x), hint=\'almost_linear\'))
                        -x
    f(x) = (C1 - Ei(x))*e
    >>> example = cos(f(x))*f(x).diff(x) + sin(f(x)) + 1
    >>> pprint(example)
                        d
    sin(f(x)) + cos(f(x))*--(f(x)) + 1
                        dx
    >>> pprint(dsolve(example, f(x), hint=\'almost_linear\'))
                    /    -x    \\             /    -x    \\
    [f(x) = pi - asin\\C1*e   - 1/, f(x) = asin\\C1*e   - 1/]


    References
    ==========

    - Joel Moses, "Symbolic Integration - The Stormy Decade", Communications
      of the ACM, Volume 14, Number 8, August 1971, pp. 558
    '''
    hint = 'almost_linear'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        P = Wild('P', exclude = [
            f(x).diff(x)])
        Q = Wild('Q', exclude = [
            f(x).diff(x)])
        return (P, Q)

    
    def _equation(self, fx, x, order):
        (P, Q) = self.wilds()
        return P * fx.diff(x) + Q

    
    def _verify(self, fx):
        (a, b) = self.wilds_match()
        (c, b) = b.as_independent(fx) if b.is_Add else (S.Zero, b)
        if not b.diff(fx) != 0 and simplify(b.diff(fx) / a).has(fx):
            self.ly = factor_terms(b).as_independent(fx, as_Add = False)[1]
            self.ax = a / self.ly.diff(fx)
            self.cx = -c
            self.bx = factor_terms(b) / self.ly
            return True

    
    def _get_general_solution(self = None, *, simplify_flag):
        x = self.ode_problem.sym
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        gensol = Eq(self.ly, (C1 + Integral((self.cx / self.ax) * exp(Integral(self.bx / self.ax, x)), x)) * exp(-Integral(self.bx / self.ax, x)))
        return [
            gensol]



class Bernoulli(SinglePatternODESolver):
    '''
    Solves Bernoulli differential equations.

    These are equations of the form

    .. math:: dy/dx + P(x) y = Q(x) y^n\\text{, }n \\ne 1`\\text{.}

    The substitution `w = 1/y^{1-n}` will transform an equation of this form
    into one that is linear (see the docstring of
    :obj:`~sympy.solvers.ode.single.FirstLinear`).  The general solution is::

        >>> from sympy import Function, dsolve, Eq, pprint
        >>> from sympy.abc import x, n
        >>> f, P, Q = map(Function, [\'f\', \'P\', \'Q\'])
        >>> genform = Eq(f(x).diff(x) + P(x)*f(x), Q(x)*f(x)**n)
        >>> pprint(genform)
                    d                n
        P(x)*f(x) + --(f(x)) = Q(x)*f (x)
                    dx
        >>> pprint(dsolve(genform, f(x), hint=\'Bernoulli_Integral\'), num_columns=110)
                                                                                                                -1
                                                                                                               -----
                                                                                                               n - 1
               //         /                                 /                            \\                    \\
               ||        |                                 |                             |                    |
               ||        |                  /              |                  /          |            /       |
               ||        |                 |               |                 |           |           |        |
               ||        |       -(n - 1)* | P(x) dx       |       -(n - 1)* | P(x) dx   |  (n - 1)* | P(x) dx|
               ||        |                 |               |                 |           |           |        |
               ||        |                /                |                /            |          /         |
        f(x) = ||C1 - n* | Q(x)*e                    dx +  | Q(x)*e                    dx|*e                  |
               ||        |                                 |                             |                    |
               \\\\       /                                 /                              /                    /


    Note that the equation is separable when `n = 1` (see the docstring of
    :obj:`~sympy.solvers.ode.single.Separable`).

    >>> pprint(dsolve(Eq(f(x).diff(x) + P(x)*f(x), Q(x)*f(x)), f(x),
    ... hint=\'separable_Integral\'))
    f(x)
        /
    |                /
    |  1            |
    |  - dy = C1 +  | (-P(x) + Q(x)) dx
    |  y            |
    |              /
    /


    Examples
    ========

    >>> from sympy import Function, dsolve, Eq, pprint, log
    >>> from sympy.abc import x
    >>> f = Function(\'f\')

    >>> pprint(dsolve(Eq(x*f(x).diff(x) + f(x), log(x)*f(x)**2),
    ... f(x), hint=\'Bernoulli\'))
                    1
    f(x) =  -----------------
            C1*x + log(x) + 1

    References
    ==========

    - https://en.wikipedia.org/wiki/Bernoulli_differential_equation

    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 95

    # indirect doctest

    '''
    hint = 'Bernoulli'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        P = Wild('P', exclude = [
            f(x)])
        Q = Wild('Q', exclude = [
            f(x)])
        n = Wild('n', exclude = [
            x,
            f(x),
            f(x).diff(x)])
        return (P, Q, n)

    
    def _equation(self, fx, x, order):
        (P, Q, n) = self.wilds()
        return fx.diff(x) + P * fx - Q * fx ** n

    
    def _get_general_solution(self = None, *, simplify_flag):
        (P, Q, n) = self.wilds_match()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        if n == 1:
            gensol = Eq(log(fx), C1 + Integral(-P + Q, x))
        else:
            gensol = Eq(fx ** (1 - n), (C1 - (n - 1) * Integral(Q * exp(-n * Integral(P, x)) * exp(Integral(P, x)), x)) * exp(-(1 - n) * Integral(P, x)))
        return [
            gensol]



class Factorable(SingleODESolver):
    """
        Solves equations having a solvable factor.

        This function is used to solve the equation having factors. Factors may be of type algebraic or ode. It
        will try to solve each factor independently. Factors will be solved by calling dsolve. We will return the
        list of solutions.

        Examples
        ========

        >>> from sympy import Function, dsolve, pprint
        >>> from sympy.abc import x
        >>> f = Function('f')
        >>> eq = (f(x)**2-4)*(f(x).diff(x)+f(x))
        >>> pprint(dsolve(eq, f(x)))
                                        -x
        [f(x) = 2, f(x) = -2, f(x) = C1*e  ]


        """
    hint = 'factorable'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        func = self.ode_problem.func.func
        x = self.ode_problem.sym
        eqns = self.eqs
        sols = []
        for eq in eqns:
            sol = dsolve(eq, func(x))
            if isinstance(sol, list):
                sols.extend(sol)
                continue
            sols.append(sol)
            except NotImplementedError:
                continue
            if sols == []:
                raise NotImplementedError('The given ODE ' + str(eq) + ' cannot be solved by' + ' the factorable group method')
            return sols



class RiccatiSpecial(SinglePatternODESolver):
    '''
    The general Riccati equation has the form

    .. math:: dy/dx = f(x) y^2 + g(x) y + h(x)\\text{.}

    While it does not have a general solution [1], the "special" form, `dy/dx
    = a y^2 - b x^c`, does have solutions in many cases [2].  This routine
    returns a solution for `a(dy/dx) = b y^2 + c y/x + d/x^2` that is obtained
    by using a suitable change of variables to reduce it to the special form
    and is valid when neither `a` nor `b` are zero and either `c` or `d` is
    zero.

    >>> from sympy.abc import x, a, b, c, d
    >>> from sympy import dsolve, checkodesol, pprint, Function
    >>> f = Function(\'f\')
    >>> y = f(x)
    >>> genform = a*y.diff(x) - (b*y**2 + c*y/x + d/x**2)
    >>> sol = dsolve(genform, y, hint="Riccati_special_minus2")
    >>> pprint(sol, wrap_line=False)
            /                                 /        __________________       \\\\
            |           __________________    |       /                2        ||
            |          /                2     |     \\/  4*b*d - (a + c)  *log(x)||
           -|a + c - \\/  4*b*d - (a + c)  *tan|C1 + ----------------------------||
            \\                                 \\                 2*a             //
    f(x) = ------------------------------------------------------------------------
                                            2*b*x

    >>> checkodesol(genform, sol, order=1)[0]
    True

    References
    ==========

    - https://www.maplesoft.com/support/help/Maple/view.aspx?path=odeadvisor/Riccati
    - https://eqworld.ipmnet.ru/en/solutions/ode/ode0106.pdf -
      https://eqworld.ipmnet.ru/en/solutions/ode/ode0123.pdf
    '''
    hint = 'Riccati_special_minus2'
    has_integral = False
    order = [
        1]
    
    def _wilds(self, f, x, order):
        a = Wild('a', exclude = [
            x,
            f(x),
            f(x).diff(x),
            0])
        b = Wild('b', exclude = [
            x,
            f(x),
            f(x).diff(x),
            0])
        c = Wild('c', exclude = [
            x,
            f(x),
            f(x).diff(x)])
        d = Wild('d', exclude = [
            x,
            f(x),
            f(x).diff(x)])
        return (a, b, c, d)

    
    def _equation(self, fx, x, order):
        (a, b, c, d) = self.wilds()
        return a * fx.diff(x) + b * fx ** 2 + c * fx / x + d / x ** 2

    
    def _get_general_solution(self = None, *, simplify_flag):
        (a, b, c, d) = self.wilds_match()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        mu = sqrt(4 * d * b - (a - c) ** 2)
        gensol = Eq(fx, (a - c - mu * tan((mu / (2 * a)) * log(x) + C1)) / (2 * b * x))
        return [
            gensol]



class RationalRiccati(SinglePatternODESolver):
    '''
    Gives general solutions to the first order Riccati differential
    equations that have atleast one rational particular solution.

    .. math :: y\' = b_0(x) + b_1(x) y + b_2(x) y^2

    where `b_0`, `b_1` and `b_2` are rational functions of `x`
    with `b_2 \\ne 0` (`b_2 = 0` would make it a Bernoulli equation).

    Examples
    ========

    >>> from sympy import Symbol, Function, dsolve, checkodesol
    >>> f = Function(\'f\')
    >>> x = Symbol(\'x\')

    >>> eq = -x**4*f(x)**2 + x**3*f(x).diff(x) + x**2*f(x) + 20
    >>> sol = dsolve(eq, hint="1st_rational_riccati")
    >>> sol
    Eq(f(x), (4*C1 - 5*x**9 - 4)/(x**2*(C1 + x**9 - 1)))
    >>> checkodesol(eq, sol)
    (True, 0)

    References
    ==========

    - Riccati ODE:  https://en.wikipedia.org/wiki/Riccati_equation
    - N. Thieu Vo - Rational and Algebraic Solutions of First-Order Algebraic ODEs:
      Algorithm 11, pp. 78 - https://www3.risc.jku.at/publications/download/risc_5387/PhDThesisThieu.pdf
    '''
    has_integral = False
    hint = '1st_rational_riccati'
    order = [
        1]
    
    def _wilds(self, f, x, order):
        b0 = Wild('b0', exclude = [
            f(x),
            f(x).diff(x)])
        b1 = Wild('b1', exclude = [
            f(x),
            f(x).diff(x)])
        b2 = Wild('b2', exclude = [
            f(x),
            f(x).diff(x)])
        return (b0, b1, b2)

    
    def _equation(self, fx, x, order):
        (b0, b1, b2) = self.wilds()
        return fx.diff(x) - b0 - b1 * fx - b2 * fx ** 2

    
    def _matches(self):
        eq = self.ode_problem.eq_expanded
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        order = self.ode_problem.order
        if order != 1:
            return False
        (match, funcs) = None(eq, f, x)
        if not match:
            return False
        (_b0, _b1, _b2) = None
        (b0, b1, b2) = self.wilds()
        self._wilds_match = {
            b2: _b2,
            b1: _b1,
            b0: _b0 }
        match = {
            b2: _b2,
            b1: _b1,
            b0: _b0 }
        return True

    
    def _get_general_solution(self = None, *, simplify_flag):
        (b0, b1, b2) = self.wilds_match()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        return solve_riccati(fx, x, b0, b1, b2, gensol = True)



class SecondNonlinearAutonomousConserved(SinglePatternODESolver):
    """
    Gives solution for the autonomous second order nonlinear
    differential equation of the form

    .. math :: f''(x) = g(f(x))

    The solution for this differential equation can be computed
    by multiplying by `f'(x)` and integrating on both sides,
    converting it into a first order differential equation.

    Examples
    ========

    >>> from sympy import Function, symbols, dsolve
    >>> f, g = symbols('f g', cls=Function)
    >>> x = symbols('x')

    >>> eq = f(x).diff(x, 2) - g(f(x))
    >>> dsolve(eq, simplify=False)
    [Eq(Integral(1/sqrt(C1 + 2*Integral(g(_u), _u)), (_u, f(x))), C2 + x),
    Eq(Integral(1/sqrt(C1 + 2*Integral(g(_u), _u)), (_u, f(x))), C2 - x)]

    >>> from sympy import exp, log
    >>> eq = f(x).diff(x, 2) - exp(f(x)) + log(f(x))
    >>> dsolve(eq, simplify=False)
    [Eq(Integral(1/sqrt(-2*_u*log(_u) + 2*_u + C1 + 2*exp(_u)), (_u, f(x))), C2 + x),
    Eq(Integral(1/sqrt(-2*_u*log(_u) + 2*_u + C1 + 2*exp(_u)), (_u, f(x))), C2 - x)]

    References
    ==========

    - https://eqworld.ipmnet.ru/en/solutions/ode/ode0301.pdf
    """
    hint = '2nd_nonlinear_autonomous_conserved'
    has_integral = True
    order = [
        2]
    
    def _wilds(self, f, x, order):
        fy = Wild('fy', exclude = [
            0,
            f(x).diff(x),
            f(x).diff(x, 2)])
        return (fy,)

    
    def _equation(self, fx, x, order):
        fy = self.wilds()[0]
        return fx.diff(x, 2) + fy

    
    def _verify(self, fx):
        return self.ode_problem.is_autonomous

    
    def _get_general_solution(self = None, *, simplify_flag):
        g = self.wilds_match()[0]
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        u = Dummy('u')
        g = g.subs(fx, u)
        (C1, C2) = self.ode_problem.get_numbered_constants(num = 2)
        inside = -2 * Integral(g, u) + C1
        lhs = Integral(1 / sqrt(inside), (u, fx))
        return [
            Eq(lhs, C2 + x),
            Eq(lhs, C2 - x)]



class Liouville(SinglePatternODESolver):
    '''
    Solves 2nd order Liouville differential equations.

    The general form of a Liouville ODE is

    .. math:: \\frac{d^2 y}{dx^2} + g(y) \\left(\\!
                \\frac{dy}{dx}\\!\\right)^2 + h(x)
                \\frac{dy}{dx}\\text{.}

    The general solution is:

        >>> from sympy import Function, dsolve, Eq, pprint, diff
        >>> from sympy.abc import x
        >>> f, g, h = map(Function, [\'f\', \'g\', \'h\'])
        >>> genform = Eq(diff(f(x),x,x) + g(f(x))*diff(f(x),x)**2 +
        ... h(x)*diff(f(x),x), 0)
        >>> pprint(genform)
                          2                    2
                /d       \\         d          d
        g(f(x))*|--(f(x))|  + h(x)*--(f(x)) + ---(f(x)) = 0
                \\dx      /         dx           2
                                              dx
        >>> pprint(dsolve(genform, f(x), hint=\'Liouville_Integral\'))
                                          f(x)
                  /                     /
                 |                     |
                 |     /               |     /
                 |    |                |    |
                 |  - | h(x) dx        |    | g(y) dy
                 |    |                |    |
                 |   /                 |   /
        C1 + C2* | e            dx +   |  e           dy = 0
                 |                     |
                /                     /

    Examples
    ========

    >>> from sympy import Function, dsolve, Eq, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(diff(f(x), x, x) + diff(f(x), x)**2/f(x) +
    ... diff(f(x), x)/x, f(x), hint=\'Liouville\'))
               ________________           ________________
    [f(x) = -\\/ C1 + C2*log(x) , f(x) = \\/ C1 + C2*log(x) ]

    References
    ==========

    - Goldstein and Braun, "Advanced Methods for the Solution of Differential
      Equations", pp. 98
    - https://www.maplesoft.com/support/help/Maple/view.aspx?path=odeadvisor/Liouville

    # indirect doctest

    '''
    hint = 'Liouville'
    has_integral = True
    order = [
        2]
    
    def _wilds(self, f, x, order):
        d = Wild('d', exclude = [
            f(x).diff(x),
            f(x).diff(x, 2)])
        e = Wild('e', exclude = [
            f(x).diff(x)])
        k = Wild('k', exclude = [
            f(x).diff(x)])
        return (d, e, k)

    
    def _equation(self, fx, x, order):
        (d, e, k) = self.wilds()
        return d * fx.diff(x, 2) + e * fx.diff(x) ** 2 + k * fx.diff(x)

    
    def _verify(self, fx):
        (d, e, k) = self.wilds_match()
        self.y = Dummy('y')
        x = self.ode_problem.sym
        self.g = simplify(e / d).subs(fx, self.y)
        self.h = simplify(k / d).subs(fx, self.y)
        if self.y in self.h.free_symbols or x in self.g.free_symbols:
            return False

    
    def _get_general_solution(self = None, *, simplify_flag):
        (d, e, k) = self.wilds_match()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        (C1, C2) = self.ode_problem.get_numbered_constants(num = 2)
        int = Integral(exp(Integral(self.g, self.y)), (self.y, None, fx))
        gen_sol = Eq(int + C1 * Integral(exp(-Integral(self.h, x)), x) + C2, 0)
        return [
            gen_sol]



class Separable(SinglePatternODESolver):
    '''
    Solves separable 1st order differential equations.

    This is any differential equation that can be written as `P(y)
    \\tfrac{dy}{dx} = Q(x)`.  The solution can then just be found by
    rearranging terms and integrating: `\\int P(y) \\,dy = \\int Q(x) \\,dx`.
    This hint uses :py:meth:`sympy.simplify.simplify.separatevars` as its back
    end, so if a separable equation is not caught by this solver, it is most
    likely the fault of that function.
    :py:meth:`~sympy.simplify.simplify.separatevars` is
    smart enough to do most expansion and factoring necessary to convert a
    separable equation `F(x, y)` into the proper form `P(x)\\cdot{}Q(y)`.  The
    general solution is::

        >>> from sympy import Function, dsolve, Eq, pprint
        >>> from sympy.abc import x
        >>> a, b, c, d, f = map(Function, [\'a\', \'b\', \'c\', \'d\', \'f\'])
        >>> genform = Eq(a(x)*b(f(x))*f(x).diff(x), c(x)*d(f(x)))
        >>> pprint(genform)
                     d
        a(x)*b(f(x))*--(f(x)) = c(x)*d(f(x))
                     dx
        >>> pprint(dsolve(genform, f(x), hint=\'separable_Integral\'))
             f(x)
           /                  /
          |                  |
          |  b(y)            | c(x)
          |  ---- dy = C1 +  | ---- dx
          |  d(y)            | a(x)
          |                  |
         /                  /

    Examples
    ========

    >>> from sympy import Function, dsolve, Eq
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(Eq(f(x)*f(x).diff(x) + x, 3*x*f(x)**2), f(x),
    ... hint=\'separable\', simplify=False))
       /   2       \\         2
    log\\3*f (x) - 1/        x
    ---------------- = C1 + --
           6                2

    References
    ==========

    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 52

    # indirect doctest

    '''
    hint = 'separable'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        d = Wild('d', exclude = [
            f(x).diff(x),
            f(x).diff(x, 2)])
        e = Wild('e', exclude = [
            f(x).diff(x)])
        return (d, e)

    
    def _equation(self, fx, x, order):
        (d, e) = self.wilds()
        return d + e * fx.diff(x)

    
    def _verify(self, fx):
        (d, e) = self.wilds_match()
        self.y = Dummy('y')
        x = self.ode_problem.sym
        d = separatevars(d.subs(fx, self.y))
        e = separatevars(e.subs(fx, self.y))
        self.m1 = separatevars(d, dict = True, symbols = (x, self.y))
        self.m2 = separatevars(e, dict = True, symbols = (x, self.y))
        if self.m1 and self.m2:
            return True

    
    def _get_match_object(self):
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        return (self.m1, self.m2, x, fx)

    
    def _get_general_solution(self = None, *, simplify_flag):
        (m1, m2, x, fx) = self._get_match_object()
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        int = Integral(m2['coeff'] * m2[self.y] / m1[self.y], (self.y, None, fx))
        gen_sol = Eq(int, Integral(-m1['coeff'] * m1[x] / m2[x], x) + C1)
        return [
            gen_sol]



class SeparableReduced(Separable):
    '''
    Solves a differential equation that can be reduced to the separable form.

    The general form of this equation is

    .. math:: y\' + (y/x) H(x^n y) = 0\\text{}.

    This can be solved by substituting `u(y) = x^n y`.  The equation then
    reduces to the separable form `\\frac{u\'}{u (\\mathrm{power} - H(u))} -
    \\frac{1}{x} = 0`.

    The general solution is:

        >>> from sympy import Function, dsolve, pprint
        >>> from sympy.abc import x, n
        >>> f, g = map(Function, [\'f\', \'g\'])
        >>> genform = f(x).diff(x) + (f(x)/x)*g(x**n*f(x))
        >>> pprint(genform)
                         / n     \\
        d          f(x)*g\\x *f(x)/
        --(f(x)) + ---------------
        dx                x
        >>> pprint(dsolve(genform, hint=\'separable_reduced\'))
         n
        x *f(x)
          /
         |
         |         1
         |    ------------ dy = C1 + log(x)
         |    y*(n - g(y))
         |
         /

    See Also
    ========
    :obj:`sympy.solvers.ode.single.Separable`

    Examples
    ========

    >>> from sympy import dsolve, Function, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> d = f(x).diff(x)
    >>> eq = (x - x**2*f(x))*d - f(x)
    >>> dsolve(eq, hint=\'separable_reduced\')
    [Eq(f(x), (1 - sqrt(C1*x**2 + 1))/x), Eq(f(x), (sqrt(C1*x**2 + 1) + 1)/x)]
    >>> pprint(dsolve(eq, hint=\'separable_reduced\'))
                   ___________            ___________
                  /     2                /     2
            1 - \\/  C1*x  + 1          \\/  C1*x  + 1  + 1
    [f(x) = ------------------, f(x) = ------------------]
                    x                          x

    References
    ==========

    - Joel Moses, "Symbolic Integration - The Stormy Decade", Communications
      of the ACM, Volume 14, Number 8, August 1971, pp. 558
    '''
    hint = 'separable_reduced'
    has_integral = True
    order = [
        1]
    
    def _degree(self, expr, x):
        for val in expr:
            if val.has(x):
                if isinstance(val, Pow) and val.as_base_exp()[0] == x:
                    
                    return None, val.as_base_exp()[1]
                if None == x:
                    
                    return None, val.as_base_exp()[1]
                
                return None, None._degree(val.args, x)
            return 0

    
    def _powers(self, expr):
        pows = set()
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        self.y = Dummy('y')
        if isinstance(expr, Add):
            exprs = expr.atoms(Add)
        elif isinstance(expr, Mul):
            exprs = expr.atoms(Mul)
        elif isinstance(expr, Pow):
            exprs = expr.atoms(Pow)
        else:
            exprs = {
                expr}
        for arg in exprs:
            if arg.has(x):
                (_, u) = arg.as_independent(x, fx)
                pow = self._degree((u.subs(fx, self.y),), x) / self._degree((u.subs(fx, self.y),), self.y)
                pows.add(pow)
            return pows

    
    def _verify(self, fx):
        (num, den) = self.wilds_match()
        x = self.ode_problem.sym
        factor = simplify((x / fx) * num / den)
        (num, dem) = factor.as_numer_denom()
        num = expand(num)
        dem = expand(dem)
        pows = self._powers(num)
        pows.update(self._powers(dem))
        pows = list(pows)
        if len(pows) == 1 and pows[0] != zoo:
            self.t = Dummy('t')
            self.r2 = {
                't': self.t }
            num = num.subs(x ** pows[0] * fx, self.t)
            dem = dem.subs(x ** pows[0] * fx, self.t)
            test = num / dem
            free = test.free_symbols
            if len(free) == 1 and free.pop() == self.t:
                self.r2.update({
                    'power': pows[0],
                    'u': test })
                return True
            return None

    
    def _get_match_object(self):
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        u = self.r2['u'].subs(self.r2['t'], self.y)
        ycoeff = 1 / (self.y * (self.r2['power'] - u))
        m1 = {
            'coeff': 1,
            x: -1 / x,
            self.y: 1 }
        m2 = {
            'coeff': 1,
            x: 1,
            self.y: ycoeff }
        return (m1, m2, x, x ** self.r2['power'] * fx)



class HomogeneousCoeffSubsDepDivIndep(SinglePatternODESolver):
    '''
    Solves a 1st order differential equation with homogeneous coefficients
    using the substitution `u_1 = \\frac{\\text{<dependent
    variable>}}{\\text{<independent variable>}}`.

    This is a differential equation

    .. math:: P(x, y) + Q(x, y) dy/dx = 0

    such that `P` and `Q` are homogeneous and of the same order.  A function
    `F(x, y)` is homogeneous of order `n` if `F(x t, y t) = t^n F(x, y)`.
    Equivalently, `F(x, y)` can be rewritten as `G(y/x)` or `H(x/y)`.  See
    also the docstring of :py:meth:`~sympy.solvers.ode.homogeneous_order`.

    If the coefficients `P` and `Q` in the differential equation above are
    homogeneous functions of the same order, then it can be shown that the
    substitution `y = u_1 x` (i.e. `u_1 = y/x`) will turn the differential
    equation into an equation separable in the variables `x` and `u`.  If
    `h(u_1)` is the function that results from making the substitution `u_1 =
    f(x)/x` on `P(x, f(x))` and `g(u_2)` is the function that results from the
    substitution on `Q(x, f(x))` in the differential equation `P(x, f(x)) +
    Q(x, f(x)) f\'(x) = 0`, then the general solution is::

        >>> from sympy import Function, dsolve, pprint
        >>> from sympy.abc import x
        >>> f, g, h = map(Function, [\'f\', \'g\', \'h\'])
        >>> genform = g(f(x)/x) + h(f(x)/x)*f(x).diff(x)
        >>> pprint(genform)
         /f(x)\\    /f(x)\\ d
        g|----| + h|----|*--(f(x))
         \\ x  /    \\ x  / dx
        >>> pprint(dsolve(genform, f(x),
        ... hint=\'1st_homogeneous_coeff_subs_dep_div_indep_Integral\'))
                       f(x)
                       ----
                        x
                         /
                        |
                        |       -h(u1)
        log(x) = C1 +   |  ---------------- d(u1)
                        |  u1*h(u1) + g(u1)
                        |
                       /

    Where `u_1 h(u_1) + g(u_1) \\ne 0` and `x \\ne 0`.

    See also the docstrings of
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffBest` and
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsIndepDivDep`.

    Examples
    ========

    >>> from sympy import Function, dsolve
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(2*x*f(x) + (x**2 + f(x)**2)*f(x).diff(x), f(x),
    ... hint=\'1st_homogeneous_coeff_subs_dep_div_indep\', simplify=False))
                          /          3   \\
                          |3*f(x)   f (x)|
                       log|------ + -----|
                          |  x         3 |
                          \\           x  /
    log(x) = log(C1) - -------------------
                                3

    References
    ==========

    - https://en.wikipedia.org/wiki/Homogeneous_differential_equation
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 59

    # indirect doctest

    '''
    hint = '1st_homogeneous_coeff_subs_dep_div_indep'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        d = Wild('d', exclude = [
            f(x).diff(x),
            f(x).diff(x, 2)])
        e = Wild('e', exclude = [
            f(x).diff(x)])
        return (d, e)

    
    def _equation(self, fx, x, order):
        (d, e) = self.wilds()
        return d + e * fx.diff(x)

    
    def _verify(self, fx):
        (self.d, self.e) = self.wilds_match()
        self.y = Dummy('y')
        x = self.ode_problem.sym
        self.d = separatevars(self.d.subs(fx, self.y))
        self.e = separatevars(self.e.subs(fx, self.y))
        ordera = homogeneous_order(self.d, x, self.y)
        orderb = homogeneous_order(self.e, x, self.y)
    # WARNING: Decompyle incomplete

    
    def _get_match_object(self):
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        self.u1 = Dummy('u1')
        xarg = 0
        yarg = 0
        return [
            self.d,
            self.e,
            fx,
            x,
            self.u,
            self.u1,
            self.y,
            xarg,
            yarg]

    
    def _get_general_solution(self = None, *, simplify_flag):
        (d, e, fx, x, u, u1, y, xarg, yarg) = self._get_match_object()
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        int = Integral((-e / (d + u1 * e)).subs({
            y: u1,
            x: 1 }), (u1, None, fx / x))
        sol = logcombine(Eq(log(x), int + log(C1)), force = True)
        gen_sol = sol.subs(fx, u).subs(((u, u - yarg), (x, x - xarg), (u, fx)))
        return [
            gen_sol]



class HomogeneousCoeffSubsIndepDivDep(SinglePatternODESolver):
    '''
    Solves a 1st order differential equation with homogeneous coefficients
    using the substitution `u_2 = \\frac{\\text{<independent
    variable>}}{\\text{<dependent variable>}}`.

    This is a differential equation

    .. math:: P(x, y) + Q(x, y) dy/dx = 0

    such that `P` and `Q` are homogeneous and of the same order.  A function
    `F(x, y)` is homogeneous of order `n` if `F(x t, y t) = t^n F(x, y)`.
    Equivalently, `F(x, y)` can be rewritten as `G(y/x)` or `H(x/y)`.  See
    also the docstring of :py:meth:`~sympy.solvers.ode.homogeneous_order`.

    If the coefficients `P` and `Q` in the differential equation above are
    homogeneous functions of the same order, then it can be shown that the
    substitution `x = u_2 y` (i.e. `u_2 = x/y`) will turn the differential
    equation into an equation separable in the variables `y` and `u_2`.  If
    `h(u_2)` is the function that results from making the substitution `u_2 =
    x/f(x)` on `P(x, f(x))` and `g(u_2)` is the function that results from the
    substitution on `Q(x, f(x))` in the differential equation `P(x, f(x)) +
    Q(x, f(x)) f\'(x) = 0`, then the general solution is:

    >>> from sympy import Function, dsolve, pprint
    >>> from sympy.abc import x
    >>> f, g, h = map(Function, [\'f\', \'g\', \'h\'])
    >>> genform = g(x/f(x)) + h(x/f(x))*f(x).diff(x)
    >>> pprint(genform)
     / x  \\    / x  \\ d
    g|----| + h|----|*--(f(x))
     \\f(x)/    \\f(x)/ dx
    >>> pprint(dsolve(genform, f(x),
    ... hint=\'1st_homogeneous_coeff_subs_indep_div_dep_Integral\'))
                 x
                ----
                f(x)
                  /
                 |
                 |       -g(u1)
                 |  ---------------- d(u1)
                 |  u1*g(u1) + h(u1)
                 |
                /
    <BLANKLINE>
    f(x) = C1*e

    Where `u_1 g(u_1) + h(u_1) \\ne 0` and `f(x) \\ne 0`.

    See also the docstrings of
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffBest` and
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsDepDivIndep`.

    Examples
    ========

    >>> from sympy import Function, pprint, dsolve
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(2*x*f(x) + (x**2 + f(x)**2)*f(x).diff(x), f(x),
    ... hint=\'1st_homogeneous_coeff_subs_indep_div_dep\',
    ... simplify=False))
                             /   2     \\
                             |3*x      |
                          log|----- + 1|
                             | 2       |
                             \\f (x)    /
    log(f(x)) = log(C1) - --------------
                                3

    References
    ==========

    - https://en.wikipedia.org/wiki/Homogeneous_differential_equation
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 59

    # indirect doctest

    '''
    hint = '1st_homogeneous_coeff_subs_indep_div_dep'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        d = Wild('d', exclude = [
            f(x).diff(x),
            f(x).diff(x, 2)])
        e = Wild('e', exclude = [
            f(x).diff(x)])
        return (d, e)

    
    def _equation(self, fx, x, order):
        (d, e) = self.wilds()
        return d + e * fx.diff(x)

    
    def _verify(self, fx):
        (self.d, self.e) = self.wilds_match()
        self.y = Dummy('y')
        x = self.ode_problem.sym
        self.d = separatevars(self.d.subs(fx, self.y))
        self.e = separatevars(self.e.subs(fx, self.y))
        ordera = homogeneous_order(self.d, x, self.y)
        orderb = homogeneous_order(self.e, x, self.y)
    # WARNING: Decompyle incomplete

    
    def _get_match_object(self):
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        self.u1 = Dummy('u1')
        xarg = 0
        yarg = 0
        return [
            self.d,
            self.e,
            fx,
            x,
            self.u,
            self.u1,
            self.y,
            xarg,
            yarg]

    
    def _get_general_solution(self = None, *, simplify_flag):
        (d, e, fx, x, u, u1, y, xarg, yarg) = self._get_match_object()
        (C1,) = self.ode_problem.get_numbered_constants(num = 1)
        int = Integral(simplify((-d / (e + u1 * d)).subs({
            y: 1,
            x: u1 })), (u1, None, x / fx))
        sol = logcombine(Eq(log(fx), int + log(C1)), force = True)
        gen_sol = sol.subs(fx, u).subs(((u, u - yarg), (x, x - xarg), (u, fx)))
        return [
            gen_sol]



class HomogeneousCoeffBest(HomogeneousCoeffSubsDepDivIndep, HomogeneousCoeffSubsIndepDivDep):
    '''
    Returns the best solution to an ODE from the two hints
    ``1st_homogeneous_coeff_subs_dep_div_indep`` and
    ``1st_homogeneous_coeff_subs_indep_div_dep``.

    This is as determined by :py:meth:`~sympy.solvers.ode.ode.ode_sol_simplicity`.

    See the
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsIndepDivDep`
    and
    :obj:`~sympy.solvers.ode.single.HomogeneousCoeffSubsDepDivIndep`
    docstrings for more information on these hints.  Note that there is no
    ``ode_1st_homogeneous_coeff_best_Integral`` hint.

    Examples
    ========

    >>> from sympy import Function, dsolve, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(2*x*f(x) + (x**2 + f(x)**2)*f(x).diff(x), f(x),
    ... hint=\'1st_homogeneous_coeff_best\', simplify=False))
                             /   2     \\
                             |3*x      |
                          log|----- + 1|
                             | 2       |
                             \\f (x)    /
    log(f(x)) = log(C1) - --------------
                                3

    References
    ==========

    - https://en.wikipedia.org/wiki/Homogeneous_differential_equation
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 59

    # indirect doctest

    '''
    hint = '1st_homogeneous_coeff_best'
    has_integral = False
    order = [
        1]
    
    def _verify(self, fx):
        if HomogeneousCoeffSubsIndepDivDep._verify(self, fx) and HomogeneousCoeffSubsDepDivIndep._verify(self, fx):
            return True

    
    def _get_general_solution(self = None, *, simplify_flag):
        pass
    # WARNING: Decompyle incomplete



class LinearCoefficients(HomogeneousCoeffBest):
    '''
    Solves a differential equation with linear coefficients.

    The general form of a differential equation with linear coefficients is

    .. math:: y\' + F\\left(\\!\\frac{a_1 x + b_1 y + c_1}{a_2 x + b_2 y +
                c_2}\\!\\right) = 0\\text{,}

    where `a_1`, `b_1`, `c_1`, `a_2`, `b_2`, `c_2` are constants and `a_1 b_2
    - a_2 b_1 \\ne 0`.

    This can be solved by substituting:

    .. math:: x = x\' + \\frac{b_2 c_1 - b_1 c_2}{a_2 b_1 - a_1 b_2}

              y = y\' + \\frac{a_1 c_2 - a_2 c_1}{a_2 b_1 - a_1
                  b_2}\\text{.}

    This substitution reduces the equation to a homogeneous differential
    equation.

    See Also
    ========
    :obj:`sympy.solvers.ode.single.HomogeneousCoeffBest`
    :obj:`sympy.solvers.ode.single.HomogeneousCoeffSubsIndepDivDep`
    :obj:`sympy.solvers.ode.single.HomogeneousCoeffSubsDepDivIndep`

    Examples
    ========

    >>> from sympy import dsolve, Function, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> df = f(x).diff(x)
    >>> eq = (x + f(x) + 1)*df + (f(x) - 6*x + 1)
    >>> dsolve(eq, hint=\'linear_coefficients\')
    [Eq(f(x), -x - sqrt(C1 + 7*x**2) - 1), Eq(f(x), -x + sqrt(C1 + 7*x**2) - 1)]
    >>> pprint(dsolve(eq, hint=\'linear_coefficients\'))
                      ___________                     ___________
                   /         2                     /         2
    [f(x) = -x - \\/  C1 + 7*x   - 1, f(x) = -x + \\/  C1 + 7*x   - 1]


    References
    ==========

    - Joel Moses, "Symbolic Integration - The Stormy Decade", Communications
      of the ACM, Volume 14, Number 8, August 1971, pp. 558
    '''
    hint = 'linear_coefficients'
    has_integral = True
    order = [
        1]
    
    def _wilds(self, f, x, order):
        d = Wild('d', exclude = [
            f(x).diff(x),
            f(x).diff(x, 2)])
        e = Wild('e', exclude = [
            f(x).diff(x)])
        return (d, e)

    
    def _equation(self, fx, x, order):
        (d, e) = self.wilds()
        return d + e * fx.diff(x)

    
    def _verify(self, fx):
        (self.d, self.e) = self.wilds_match()
        (a, b) = self.wilds()
        F = self.d / self.e
        x = self.ode_problem.sym
        params = self._linear_coeff_match(F, fx)
    # WARNING: Decompyle incomplete

    
    def _linear_coeff_match(self, expr, func):
        """
        Helper function to match hint ``linear_coefficients``.

        Matches the expression to the form `(a_1 x + b_1 f(x) + c_1)/(a_2 x + b_2
        f(x) + c_2)` where the following conditions hold:

        1. `a_1`, `b_1`, `c_1`, `a_2`, `b_2`, `c_2` are Rationals;
        2. `c_1` or `c_2` are not equal to zero;
        3. `a_2 b_1 - a_1 b_2` is not equal to zero.

        Return ``xarg``, ``yarg`` where

        1. ``xarg`` = `(b_2 c_1 - b_1 c_2)/(a_2 b_1 - a_1 b_2)`
        2. ``yarg`` = `(a_1 c_2 - a_2 c_1)/(a_2 b_1 - a_1 b_2)`


        Examples
        ========

        >>> from sympy import Function, sin
        >>> from sympy.abc import x
        >>> from sympy.solvers.ode.single import LinearCoefficients
        >>> f = Function('f')
        >>> eq = (-25*f(x) - 8*x + 62)/(4*f(x) + 11*x - 11)
        >>> obj = LinearCoefficients(eq)
        >>> obj._linear_coeff_match(eq, f(x))
        (1/9, 22/9)
        >>> eq = sin((-5*f(x) - 8*x + 6)/(4*f(x) + x - 1))
        >>> obj = LinearCoefficients(eq)
        >>> obj._linear_coeff_match(eq, f(x))
        (19/27, 2/27)
        >>> eq = sin(f(x)/x)
        >>> obj = LinearCoefficients(eq)
        >>> obj._linear_coeff_match(eq, f(x))

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _get_match_object(self):
        fx = self.ode_problem.func
        x = self.ode_problem.sym
        self.u1 = Dummy('u1')
        u = Dummy('u')
        return [
            self.d,
            self.e,
            fx,
            x,
            u,
            self.u1,
            self.y,
            self.xarg,
            self.yarg]



class NthOrderReducible(SingleODESolver):
    """
    Solves ODEs that only involve derivatives of the dependent variable using
    a substitution of the form `f^n(x) = g(x)`.

    For example any second order ODE of the form `f''(x) = h(f'(x), x)` can be
    transformed into a pair of 1st order ODEs `g'(x) = h(g(x), x)` and
    `f'(x) = g(x)`. Usually the 1st order ODE for `g` is easier to solve. If
    that gives an explicit solution for `g` then `f` is found simply by
    integration.


    Examples
    ========

    >>> from sympy import Function, dsolve, Eq
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = Eq(x*f(x).diff(x)**2 + f(x).diff(x, 2), 0)
    >>> dsolve(eq, f(x), hint='nth_order_reducible')
    ... # doctest: +NORMALIZE_WHITESPACE
    Eq(f(x), C1 - sqrt(-1/C2)*log(-C2*sqrt(-1/C2) + x) + sqrt(-1/C2)*log(C2*sqrt(-1/C2) + x))

    """
    hint = 'nth_order_reducible'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        eq = self.ode_problem.eq
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        n = self.smallest
        names = eq.atoms(AppliedUndef)()
        name = Dummy().name
        if name not in names:
            g = Function(name)
        
        w = f(x).diff(x, n)
        geq = eq.subs(w, g(x))
        gsol = dsolve(geq, g(x))
        if not isinstance(gsol, list):
            gsol = [
                gsol]
        fsol = []
        for gsoli in gsol:
            fsoli = dsolve(gsoli.subs(g(x), w), f(x))
            fsol.append(fsoli)
            return fsol



class SecondHypergeometric(SingleODESolver):
    '''
    Solves 2nd order linear differential equations.

    It computes special function solutions which can be expressed using the
    2F1, 1F1 or 0F1 hypergeometric functions.

    .. math:: y\'\' + A(x) y\' + B(x) y = 0\\text{,}

    where `A` and `B` are rational functions.

    These kinds of differential equations have solution of non-Liouvillian form.

    Given linear ODE can be obtained from 2F1 given by

    .. math:: (x^2 - x) y\'\' + ((a + b + 1) x - c) y\' + b a y = 0\\text{,}

    where {a, b, c} are arbitrary constants.

    Notes
    =====

    The algorithm should find any solution of the form

    .. math:: y = P(x) _pF_q(..; ..;\\frac{\\alpha x^k + \\beta}{\\gamma x^k + \\delta})\\text{,}

    where pFq is any of 2F1, 1F1 or 0F1 and `P` is an "arbitrary function".
    Currently only the 2F1 case is implemented in SymPy but the other cases are
    described in the paper and could be implemented in future (contributions
    welcome!).


    Examples
    ========

    >>> from sympy import Function, dsolve, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> eq = (x*x - x)*f(x).diff(x,2) + (5*x - 1)*f(x).diff(x) + 4*f(x)
    >>> pprint(dsolve(eq, f(x), \'2nd_hypergeometric\'))
                                        _
           /        /           4  \\\\  |_  /-1, -1 |  \\
           |C1 + C2*|log(x) + -----||* |   |       | x|
           \\        \\         x + 1// 2  1 \\  1    |  /
    f(x) = --------------------------------------------
                                    3
                             (x - 1)


    References
    ==========

    - "Non-Liouvillian solutions for second order linear ODEs" by L. Chan, E.S. Cheb-Terrab

    '''
    hint = '2nd_hypergeometric'
    has_integral = True
    
    def _matches(self):
        eq = self.ode_problem.eq_preprocessed
        func = self.ode_problem.func
        r = match_2nd_hypergeometric(eq, func)
        self.match_object = None
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        eq = self.ode_problem.eq
        func = self.ode_problem.func
    # WARNING: Decompyle incomplete



class NthLinearConstantCoeffHomogeneous(SingleODESolver):
    '''
    Solves an `n`\\th order linear homogeneous differential equation with
    constant coefficients.

    This is an equation of the form

    .. math:: a_n f^{(n)}(x) + a_{n-1} f^{(n-1)}(x) + \\cdots + a_1 f\'(x)
                + a_0 f(x) = 0\\text{.}

    These equations can be solved in a general manner, by taking the roots of
    the characteristic equation `a_n m^n + a_{n-1} m^{n-1} + \\cdots + a_1 m +
    a_0 = 0`.  The solution will then be the sum of `C_n x^i e^{r x}` terms,
    for each where `C_n` is an arbitrary constant, `r` is a root of the
    characteristic equation and `i` is one of each from 0 to the multiplicity
    of the root - 1 (for example, a root 3 of multiplicity 2 would create the
    terms `C_1 e^{3 x} + C_2 x e^{3 x}`).  The exponential is usually expanded
    for complex roots using Euler\'s equation `e^{I x} = \\cos(x) + I \\sin(x)`.
    Complex roots always come in conjugate pairs in polynomials with real
    coefficients, so the two roots will be represented (after simplifying the
    constants) as `e^{a x} \\left(C_1 \\cos(b x) + C_2 \\sin(b x)\\right)`.

    If SymPy cannot find exact roots to the characteristic equation, a
    :py:class:`~sympy.polys.rootoftools.ComplexRootOf` instance will be return
    instead.

    >>> from sympy import Function, dsolve
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> dsolve(f(x).diff(x, 5) + 10*f(x).diff(x) - 2*f(x), f(x),
    ... hint=\'nth_linear_constant_coeff_homogeneous\')
    ... # doctest: +NORMALIZE_WHITESPACE
    Eq(f(x), C5*exp(x*CRootOf(_x**5 + 10*_x - 2, 0))
    + (C1*sin(x*im(CRootOf(_x**5 + 10*_x - 2, 1)))
    + C2*cos(x*im(CRootOf(_x**5 + 10*_x - 2, 1))))*exp(x*re(CRootOf(_x**5 + 10*_x - 2, 1)))
    + (C3*sin(x*im(CRootOf(_x**5 + 10*_x - 2, 3)))
    + C4*cos(x*im(CRootOf(_x**5 + 10*_x - 2, 3))))*exp(x*re(CRootOf(_x**5 + 10*_x - 2, 3))))

    Note that because this method does not involve integration, there is no
    ``nth_linear_constant_coeff_homogeneous_Integral`` hint.

    Examples
    ========

    >>> from sympy import Function, dsolve, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(f(x).diff(x, 4) + 2*f(x).diff(x, 3) -
    ... 2*f(x).diff(x, 2) - 6*f(x).diff(x) + 5*f(x), f(x),
    ... hint=\'nth_linear_constant_coeff_homogeneous\'))
                        x                            -2*x
    f(x) = (C1 + C2*x)*e  + (C3*sin(x) + C4*cos(x))*e

    References
    ==========

    - https://en.wikipedia.org/wiki/Linear_differential_equation section:
      Nonhomogeneous_equation_with_constant_coefficients
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 211

    # indirect doctest

    '''
    hint = 'nth_linear_constant_coeff_homogeneous'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        fx = self.ode_problem.func
        order = self.ode_problem.order
        (roots, collectterms) = _get_const_characteristic_eq_sols(self.r, fx, order)
        constants = self.ode_problem.get_numbered_constants(num = len(roots))
    # WARNING: Decompyle incomplete



class NthLinearConstantCoeffVariationOfParameters(SingleODESolver):
    '''
    Solves an `n`\\th order linear differential equation with constant
    coefficients using the method of variation of parameters.

    This method works on any differential equations of the form

    .. math:: f^{(n)}(x) + a_{n-1} f^{(n-1)}(x) + \\cdots + a_1 f\'(x) + a_0
                f(x) = P(x)\\text{.}

    This method works by assuming that the particular solution takes the form

    .. math:: \\sum_{x=1}^{n} c_i(x) y_i(x)\\text{,}

    where `y_i` is the `i`\\th solution to the homogeneous equation.  The
    solution is then solved using Wronskian\'s and Cramer\'s Rule.  The
    particular solution is given by

    .. math:: \\sum_{x=1}^n \\left( \\int \\frac{W_i(x)}{W(x)} \\,dx
                \\right) y_i(x) \\text{,}

    where `W(x)` is the Wronskian of the fundamental system (the system of `n`
    linearly independent solutions to the homogeneous equation), and `W_i(x)`
    is the Wronskian of the fundamental system with the `i`\\th column replaced
    with `[0, 0, \\cdots, 0, P(x)]`.

    This method is general enough to solve any `n`\\th order inhomogeneous
    linear differential equation with constant coefficients, but sometimes
    SymPy cannot simplify the Wronskian well enough to integrate it.  If this
    method hangs, try using the
    ``nth_linear_constant_coeff_variation_of_parameters_Integral`` hint and
    simplifying the integrals manually.  Also, prefer using
    ``nth_linear_constant_coeff_undetermined_coefficients`` when it
    applies, because it does not use integration, making it faster and more
    reliable.

    Warning, using simplify=False with
    \'nth_linear_constant_coeff_variation_of_parameters\' in
    :py:meth:`~sympy.solvers.ode.dsolve` may cause it to hang, because it will
    not attempt to simplify the Wronskian before integrating.  It is
    recommended that you only use simplify=False with
    \'nth_linear_constant_coeff_variation_of_parameters_Integral\' for this
    method, especially if the solution to the homogeneous equation has
    trigonometric functions in it.

    Examples
    ========

    >>> from sympy import Function, dsolve, pprint, exp, log
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(f(x).diff(x, 3) - 3*f(x).diff(x, 2) +
    ... 3*f(x).diff(x) - f(x) - exp(x)*log(x), f(x),
    ... hint=\'nth_linear_constant_coeff_variation_of_parameters\'))
           /       /       /     x*log(x)   11*x\\\\\\  x
    f(x) = |C1 + x*|C2 + x*|C3 + -------- - ----|||*e
           \\       \\       \\        6        36 ///

    References
    ==========

    - https://en.wikipedia.org/wiki/Variation_of_parameters
    - https://planetmath.org/VariationOfParameters
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 233

    # indirect doctest

    '''
    hint = 'nth_linear_constant_coeff_variation_of_parameters'
    has_integral = True
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        eq = self.ode_problem.eq_high_order_free
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        order = self.ode_problem.order
        (roots, collectterms) = _get_const_characteristic_eq_sols(self.r, f(x), order)
        constants = self.ode_problem.get_numbered_constants(num = len(roots))
    # WARNING: Decompyle incomplete



class NthLinearConstantCoeffUndeterminedCoefficients(SingleODESolver):
    '''
    Solves an `n`\\th order linear differential equation with constant
    coefficients using the method of undetermined coefficients.

    This method works on differential equations of the form

    .. math:: a_n f^{(n)}(x) + a_{n-1} f^{(n-1)}(x) + \\cdots + a_1 f\'(x)
                + a_0 f(x) = P(x)\\text{,}

    where `P(x)` is a function that has a finite number of linearly
    independent derivatives.

    Functions that fit this requirement are finite sums functions of the form
    `a x^i e^{b x} \\sin(c x + d)` or `a x^i e^{b x} \\cos(c x + d)`, where `i`
    is a non-negative integer and `a`, `b`, `c`, and `d` are constants.  For
    example any polynomial in `x`, functions like `x^2 e^{2 x}`, `x \\sin(x)`,
    and `e^x \\cos(x)` can all be used.  Products of `\\sin`\'s and `\\cos`\'s have
    a finite number of derivatives, because they can be expanded into `\\sin(a
    x)` and `\\cos(b x)` terms.  However, SymPy currently cannot do that
    expansion, so you will need to manually rewrite the expression in terms of
    the above to use this method.  So, for example, you will need to manually
    convert `\\sin^2(x)` into `(1 + \\cos(2 x))/2` to properly apply the method
    of undetermined coefficients on it.

    This method works by creating a trial function from the expression and all
    of its linear independent derivatives and substituting them into the
    original ODE.  The coefficients for each term will be a system of linear
    equations, which are be solved for and substituted, giving the solution.
    If any of the trial functions are linearly dependent on the solution to
    the homogeneous equation, they are multiplied by sufficient `x` to make
    them linearly independent.

    Examples
    ========

    >>> from sympy import Function, dsolve, pprint, exp, cos
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> pprint(dsolve(f(x).diff(x, 2) + 2*f(x).diff(x) + f(x) -
    ... 4*exp(-x)*x**2 + cos(2*x), f(x),
    ... hint=\'nth_linear_constant_coeff_undetermined_coefficients\'))
           /       /      3\\\\
           |       |     x ||  -x   4*sin(2*x)   3*cos(2*x)
    f(x) = |C1 + x*|C2 + --||*e   - ---------- + ----------
           \\       \\     3 //           25           25

    References
    ==========

    - https://en.wikipedia.org/wiki/Method_of_undetermined_coefficients
    - M. Tenenbaum & H. Pollard, "Ordinary Differential Equations",
      Dover 1963, pp. 221

    # indirect doctest

    '''
    hint = 'nth_linear_constant_coeff_undetermined_coefficients'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        eq = self.ode_problem.eq
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        order = self.ode_problem.order
        (roots, collectterms) = _get_const_characteristic_eq_sols(self.r, f(x), order)
        constants = self.ode_problem.get_numbered_constants(num = len(roots))
    # WARNING: Decompyle incomplete



class NthLinearEulerEqHomogeneous(SingleODESolver):
    '''
    Solves an `n`\\th order linear homogeneous variable-coefficient
    Cauchy-Euler equidimensional ordinary differential equation.

    This is an equation with form `0 = a_0 f(x) + a_1 x f\'(x) + a_2 x^2 f\'\'(x)
    \\cdots`.

    These equations can be solved in a general manner, by substituting
    solutions of the form `f(x) = x^r`, and deriving a characteristic equation
    for `r`.  When there are repeated roots, we include extra terms of the
    form `C_{r k} \\ln^k(x) x^r`, where `C_{r k}` is an arbitrary integration
    constant, `r` is a root of the characteristic equation, and `k` ranges
    over the multiplicity of `r`.  In the cases where the roots are complex,
    solutions of the form `C_1 x^a \\sin(b \\log(x)) + C_2 x^a \\cos(b \\log(x))`
    are returned, based on expansions with Euler\'s formula.  The general
    solution is the sum of the terms found.  If SymPy cannot find exact roots
    to the characteristic equation, a
    :py:obj:`~.ComplexRootOf` instance will be returned
    instead.

    >>> from sympy import Function, dsolve
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> dsolve(4*x**2*f(x).diff(x, 2) + f(x), f(x),
    ... hint=\'nth_linear_euler_eq_homogeneous\')
    ... # doctest: +NORMALIZE_WHITESPACE
    Eq(f(x), sqrt(x)*(C1 + C2*log(x)))

    Note that because this method does not involve integration, there is no
    ``nth_linear_euler_eq_homogeneous_Integral`` hint.

    The following is for internal use:

    - ``returns = \'sol\'`` returns the solution to the ODE.
    - ``returns = \'list\'`` returns a list of linearly independent solutions,
      corresponding to the fundamental solution set, for use with non
      homogeneous solution methods like variation of parameters and
      undetermined coefficients.  Note that, though the solutions should be
      linearly independent, this function does not explicitly check that.  You
      can do ``assert simplify(wronskian(sollist)) != 0`` to check for linear
      independence.  Also, ``assert len(sollist) == order`` will need to pass.
    - ``returns = \'both\'``, return a dictionary ``{\'sol\': <solution to ODE>,
      \'list\': <list of linearly independent solutions>}``.

    Examples
    ========

    >>> from sympy import Function, dsolve, pprint
    >>> from sympy.abc import x
    >>> f = Function(\'f\')
    >>> eq = f(x).diff(x, 2)*x**2 - 4*f(x).diff(x)*x + 6*f(x)
    >>> pprint(dsolve(eq, f(x),
    ... hint=\'nth_linear_euler_eq_homogeneous\'))
            2
    f(x) = x *(C1 + C2*x)

    References
    ==========

    - https://en.wikipedia.org/wiki/Cauchy%E2%80%93Euler_equation
    - C. Bender & S. Orszag, "Advanced Mathematical Methods for Scientists and
      Engineers", Springer 1999, pp. 12

    # indirect doctest

    '''
    hint = 'nth_linear_euler_eq_homogeneous'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        fx = self.ode_problem.func
        eq = self.ode_problem.eq
        homogen_sol = _get_euler_characteristic_eq_sols(eq, fx, self.r)[0]
        return [
            homogen_sol]



class NthLinearEulerEqNonhomogeneousVariationOfParameters(SingleODESolver):
    """
    Solves an `n`\\th order linear non homogeneous Cauchy-Euler equidimensional
    ordinary differential equation using variation of parameters.

    This is an equation with form `g(x) = a_0 f(x) + a_1 x f'(x) + a_2 x^2 f''(x)
    \\cdots`.

    This method works by assuming that the particular solution takes the form

    .. math:: \\sum_{x=1}^{n} c_i(x) y_i(x) {a_n} {x^n} \\text{, }

    where `y_i` is the `i`\\th solution to the homogeneous equation.  The
    solution is then solved using Wronskian's and Cramer's Rule.  The
    particular solution is given by multiplying eq given below with `a_n x^{n}`

    .. math:: \\sum_{x=1}^n \\left( \\int \\frac{W_i(x)}{W(x)} \\, dx
                \\right) y_i(x) \\text{, }

    where `W(x)` is the Wronskian of the fundamental system (the system of `n`
    linearly independent solutions to the homogeneous equation), and `W_i(x)`
    is the Wronskian of the fundamental system with the `i`\\th column replaced
    with `[0, 0, \\cdots, 0, \\frac{x^{- n}}{a_n} g{\\left(x \\right)}]`.

    This method is general enough to solve any `n`\\th order inhomogeneous
    linear differential equation, but sometimes SymPy cannot simplify the
    Wronskian well enough to integrate it.  If this method hangs, try using the
    ``nth_linear_constant_coeff_variation_of_parameters_Integral`` hint and
    simplifying the integrals manually.  Also, prefer using
    ``nth_linear_constant_coeff_undetermined_coefficients`` when it
    applies, because it does not use integration, making it faster and more
    reliable.

    Warning, using simplify=False with
    'nth_linear_constant_coeff_variation_of_parameters' in
    :py:meth:`~sympy.solvers.ode.dsolve` may cause it to hang, because it will
    not attempt to simplify the Wronskian before integrating.  It is
    recommended that you only use simplify=False with
    'nth_linear_constant_coeff_variation_of_parameters_Integral' for this
    method, especially if the solution to the homogeneous equation has
    trigonometric functions in it.

    Examples
    ========

    >>> from sympy import Function, dsolve, Derivative
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = x**2*Derivative(f(x), x, x) - 2*x*Derivative(f(x), x) + 2*f(x) - x**4
    >>> dsolve(eq, f(x),
    ... hint='nth_linear_euler_eq_nonhomogeneous_variation_of_parameters').expand()
    Eq(f(x), C1*x + C2*x**2 + x**4/6)

    """
    hint = 'nth_linear_euler_eq_nonhomogeneous_variation_of_parameters'
    has_integral = True
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        eq = self.ode_problem.eq
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        order = self.ode_problem.order
        (homogen_sol, roots) = _get_euler_characteristic_eq_sols(eq, f(x), self.r)
        self.r[-1] = self.r[-1] / self.r[order]
        sol = _solve_variation_of_parameters(eq, f(x), roots, homogen_sol, order, self.r, simplify_flag)
        return [
            Eq(f(x), homogen_sol.rhs + (sol.rhs - homogen_sol.rhs) * self.r[order])]



class NthLinearEulerEqNonhomogeneousUndeterminedCoefficients(SingleODESolver):
    """
    Solves an `n`\\th order linear non homogeneous Cauchy-Euler equidimensional
    ordinary differential equation using undetermined coefficients.

    This is an equation with form `g(x) = a_0 f(x) + a_1 x f'(x) + a_2 x^2 f''(x)
    \\cdots`.

    These equations can be solved in a general manner, by substituting
    solutions of the form `x = exp(t)`, and deriving a characteristic equation
    of form `g(exp(t)) = b_0 f(t) + b_1 f'(t) + b_2 f''(t) \\cdots` which can
    be then solved by nth_linear_constant_coeff_undetermined_coefficients if
    g(exp(t)) has finite number of linearly independent derivatives.

    Functions that fit this requirement are finite sums functions of the form
    `a x^i e^{b x} \\sin(c x + d)` or `a x^i e^{b x} \\cos(c x + d)`, where `i`
    is a non-negative integer and `a`, `b`, `c`, and `d` are constants.  For
    example any polynomial in `x`, functions like `x^2 e^{2 x}`, `x \\sin(x)`,
    and `e^x \\cos(x)` can all be used.  Products of `\\sin`'s and `\\cos`'s have
    a finite number of derivatives, because they can be expanded into `\\sin(a
    x)` and `\\cos(b x)` terms.  However, SymPy currently cannot do that
    expansion, so you will need to manually rewrite the expression in terms of
    the above to use this method.  So, for example, you will need to manually
    convert `\\sin^2(x)` into `(1 + \\cos(2 x))/2` to properly apply the method
    of undetermined coefficients on it.

    After replacement of x by exp(t), this method works by creating a trial function
    from the expression and all of its linear independent derivatives and
    substituting them into the original ODE.  The coefficients for each term
    will be a system of linear equations, which are be solved for and
    substituted, giving the solution. If any of the trial functions are linearly
    dependent on the solution to the homogeneous equation, they are multiplied
    by sufficient `x` to make them linearly independent.

    Examples
    ========

    >>> from sympy import dsolve, Function, Derivative, log
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> eq = x**2*Derivative(f(x), x, x) - 2*x*Derivative(f(x), x) + 2*f(x) - log(x)
    >>> dsolve(eq, f(x),
    ... hint='nth_linear_euler_eq_nonhomogeneous_undetermined_coefficients').expand()
    Eq(f(x), C1*x + C2*x**2 + log(x)/2 + 3/4)

    """
    hint = 'nth_linear_euler_eq_nonhomogeneous_undetermined_coefficients'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        symbol = Dummy('x')
        eq = S.Zero
        chareq = S.Zero
        for i in self.r.keys():
            if i >= 0:
                chareq += (self.r[i] * diff(x ** symbol, x, i) * x ** (-symbol)).expand()
            for i in range(1, degree(Poly(chareq, symbol)) + 1):
                eq += chareq.coeff(symbol ** i) * diff(f(x), x, i)
                if chareq.as_coeff_add(symbol)[0]:
                    eq += chareq.as_coeff_add(symbol)[0] * f(x)
        (e, re) = posify(self.r[-1].subs(x, exp(x)))
        eq += e.subs(re)
        self.const_undet_instance = NthLinearConstantCoeffUndeterminedCoefficients(SingleODEProblem(eq, f(x), x))
        sol = self.const_undet_instance.get_general_solution(simplify = simplify_flag)[0]
        sol = sol.subs(x, log(x))
        sol = sol.subs(f(log(x)), f(x)).expand()
        return [
            sol]



class SecondLinearBessel(SingleODESolver):
    """
    Gives solution of the Bessel differential equation

    .. math :: x^2 \\frac{d^2y}{dx^2} + x \\frac{dy}{dx} y(x) + (x^2-n^2) y(x)

    if `n` is integer then the solution is of the form ``Eq(f(x), C0 besselj(n,x)
    + C1 bessely(n,x))`` as both the solutions are linearly independent else if
    `n` is a fraction then the solution is of the form ``Eq(f(x), C0 besselj(n,x)
    + C1 besselj(-n,x))`` which can also transform into ``Eq(f(x), C0 besselj(n,x)
    + C1 bessely(n,x))``.

    Examples
    ========

    >>> from sympy.abc import x
    >>> from sympy import Symbol
    >>> v = Symbol('v', positive=True)
    >>> from sympy import dsolve, Function
    >>> f = Function('f')
    >>> y = f(x)
    >>> genform = x**2*y.diff(x, 2) + x*y.diff(x) + (x**2 - v**2)*y
    >>> dsolve(genform)
    Eq(f(x), C1*besselj(v, x) + C2*bessely(v, x))

    References
    ==========

    https://math24.net/bessel-differential-equation.html

    """
    hint = '2nd_linear_bessel'
    has_integral = False
    
    def _matches(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_general_solution(self = None, *, simplify_flag):
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        n = self.rn['n']
        a4 = self.rn['a4']
        c4 = self.rn['c4']
        d4 = self.rn['d4']
        b4 = self.rn['b4']
        n = sqrt(n ** 2 + Rational(1, 4) * (c4 - 1) ** 2)
        (C1, C2) = self.ode_problem.get_numbered_constants(num = 2)
        return [
            Eq(f(x), (x ** Rational(1 - c4, 2) * (C1 * besselj(n / d4, a4 * x ** d4 / d4) + C2 * bessely(n / d4, a4 * x ** d4 / d4))).subs(x, x - b4))]



class SecondLinearAiry(SingleODESolver):
    '''
    Gives solution of the Airy differential equation

    .. math :: \\frac{d^2y}{dx^2} + (a + b x) y(x) = 0

    in terms of Airy special functions airyai and airybi.

    Examples
    ========

    >>> from sympy import dsolve, Function
    >>> from sympy.abc import x
    >>> f = Function("f")
    >>> eq = f(x).diff(x, 2) - x*f(x)
    >>> dsolve(eq)
    Eq(f(x), C1*airyai(x) + C2*airybi(x))
    '''
    hint = '2nd_linear_airy'
    has_integral = False
    
    def _matches(self):
        eq = self.ode_problem.eq_high_order_free
        f = self.ode_problem.func
        order = self.ode_problem.order
        x = self.ode_problem.sym
        df = f.diff(x)
        a4 = Wild('a4', exclude = [
            x,
            f,
            df])
        b4 = Wild('b4', exclude = [
            x,
            f,
            df])
        match = self.ode_problem.get_linear_coefficients(eq, f, order)
        does_match = False
        if order == 2 and match and match[2] != 0 and match[1].is_zero:
            self.rn = cancel(match[0] / match[2]).match(a4 + b4 * x)
            if self.rn and self.rn[b4] != 0:
                self.rn = {
                    'b': self.rn[a4],
                    'm': self.rn[b4] }
                does_match = True
        return does_match

    
    def _get_general_solution(self = None, *, simplify_flag):
        f = self.ode_problem.func.func
        x = self.ode_problem.sym
        (C1, C2) = self.ode_problem.get_numbered_constants(num = 2)
        b = self.rn['b']
        m = self.rn['m']
        if m.is_positive:
            arg = -b / cbrt(m) ** 2 - cbrt(m) * x
        elif m.is_negative:
            arg = -b / cbrt(-m) ** 2 + cbrt(-m) * x
        else:
            arg = -b / cbrt(-m) ** 2 + cbrt(-m) * x
        return [
            Eq(f(x), C1 * airyai(arg) + C2 * airybi(arg))]



class LieGroup(SingleODESolver):
    """
    This hint implements the Lie group method of solving first order differential
    equations. The aim is to convert the given differential equation from the
    given coordinate system into another coordinate system where it becomes
    invariant under the one-parameter Lie group of translations. The converted
    ODE can be easily solved by quadrature. It makes use of the
    :py:meth:`sympy.solvers.ode.infinitesimals` function which returns the
    infinitesimals of the transformation.

    The coordinates `r` and `s` can be found by solving the following Partial
    Differential Equations.

    .. math :: \\xi\\frac{\\partial r}{\\partial x} + \\eta\\frac{\\partial r}{\\partial y}
                  = 0

    .. math :: \\xi\\frac{\\partial s}{\\partial x} + \\eta\\frac{\\partial s}{\\partial y}
                  = 1

    The differential equation becomes separable in the new coordinate system

    .. math :: \\frac{ds}{dr} = \\frac{\\frac{\\partial s}{\\partial x} +
                 h(x, y)\\frac{\\partial s}{\\partial y}}{
                 \\frac{\\partial r}{\\partial x} + h(x, y)\\frac{\\partial r}{\\partial y}}

    After finding the solution by integration, it is then converted back to the original
    coordinate system by substituting `r` and `s` in terms of `x` and `y` again.

    Examples
    ========

    >>> from sympy import Function, dsolve, exp, pprint
    >>> from sympy.abc import x
    >>> f = Function('f')
    >>> pprint(dsolve(f(x).diff(x) + 2*x*f(x) - x*exp(-x**2), f(x),
    ... hint='lie_group'))
           /      2\\    2
           |     x |  -x
    f(x) = |C1 + --|*e
           \\     2 /


    References
    ==========

    - Solving differential equations by Symmetry Groups,
      John Starrett, pp. 1 - pp. 14

    """
    hint = 'lie_group'
    has_integral = False
    
    def _has_additional_params(self):
