# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: nonhomogeneous.pyc (Python 3.11)

'''
This File contains helper functions for nth_linear_constant_coeff_undetermined_coefficients,
nth_linear_euler_eq_nonhomogeneous_undetermined_coefficients,
nth_linear_constant_coeff_variation_of_parameters,
and nth_linear_euler_eq_nonhomogeneous_variation_of_parameters.

All the functions in this file are used by more than one solvers so, instead of creating
instances in other classes for using them it is better to keep it here as separate helpers.

'''
from collections import defaultdict
from sympy.core import Add, S
from sympy.core.function import diff, expand, _mexpand, expand_mul
from sympy.core.relational import Eq
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Dummy, Wild
from sympy.functions import exp, cos, cosh, im, log, re, sin, sinh, atan2, conjugate
from sympy.integrals import Integral
from sympy.polys import Poly, RootOf, rootof, roots
from sympy.simplify import collect, simplify, separatevars, powsimp, trigsimp
from sympy.utilities import numbered_symbols
from sympy.solvers.solvers import solve
from sympy.matrices import wronskian
from subscheck import sub_func_doit
from sympy.solvers.ode.ode import get_numbered_constants

def _test_term(coeff, func, order):
    '''
    Linear Euler ODEs have the form  K*x**order*diff(y(x), x, order) = F(x),
    where K is independent of x and y(x), order>= 0.
    So we need to check that for each term, coeff == K*x**order from
    some K.  We have a few cases, since coeff may have several
    different types.
    '''
    x = func.args[0]
    f = func.func
    if order < 0:
        raise ValueError('order should be greater than 0')
    if coeff == 0:
        return True
    if None == 0:
        if x in coeff.free_symbols:
            return False
        return None
    if None.is_Mul:
        if coeff.has(f(x)):
            return False
        return None ** order in coeff.args
    if None.is_Pow:
        return coeff.as_base_exp() == (x, order)
    if None == 1:
        return x == coeff


def _get_euler_characteristic_eq_sols(eq, func, match_obj):
    '''
    Returns the solution of homogeneous part of the linear euler ODE and
    the list of roots of characteristic equation.

    The parameter ``match_obj`` is a dict of order:coeff terms, where order is the order
    of the derivative on each term, and coeff is the coefficient of that derivative.

    '''
    pass
# WARNING: Decompyle incomplete


def _solve_variation_of_parameters(eq, func, roots, homogen_sol, order, match_obj, simplify_flag = (True,)):
    '''
    Helper function for the method of variation of parameters and nonhomogeneous euler eq.

    See the
    :py:meth:`~sympy.solvers.ode.single.NthLinearConstantCoeffVariationOfParameters`
    docstring for more information on this method.

    The parameter are ``match_obj`` should be a dictionary that has the following
    keys:

    ``list``
    A list of solutions to the homogeneous equation.

    ``sol``
    The general solution.

    '''
    pass
# WARNING: Decompyle incomplete


def _get_const_characteristic_eq_sols(r, func, order):
    '''
    Returns the roots of characteristic equation of constant coefficient
    linear ODE and list of collectterms which is later on used by simplification
    to use collect on solution.

    The parameter `r` is a dict of order:coeff terms, where order is the order of the
    derivative on each term, and coeff is the coefficient of that derivative.

    '''
    pass
# WARNING: Decompyle incomplete


def _get_simplified_sol(sol, func, collectterms):
    '''
    Helper function which collects the solution on
    collectterms. Ideally this should be handled by odesimp.It is used
    only when the simplify is set to True in dsolve.

    The parameter ``collectterms`` is a list of tuple (i, reroot, imroot) where `i` is
    the multiplicity of the root, reroot is real part and imroot being the imaginary part.

    '''
    f = func.func
    x = func.args[0]
    collectterms.sort(key = default_sort_key)
    collectterms.reverse()
# WARNING: Decompyle incomplete


def _undetermined_coefficients_match(expr, x, func, eq_homogeneous = (None, S.Zero)):
    """
    Returns a trial function match if undetermined coefficients can be applied
    to ``expr``, and ``None`` otherwise.

    A trial expression can be found for an expression for use with the method
    of undetermined coefficients if the expression is an
    additive/multiplicative combination of constants, polynomials in `x` (the
    independent variable of expr), `\\sin(a x + b)`, `\\cos(a x + b)`, and
    `e^{a x}` terms (in other words, it has a finite number of linearly
    independent derivatives).

    Note that you may still need to multiply each term returned here by
    sufficient `x` to make it linearly independent with the solutions to the
    homogeneous equation.

    This is intended for internal use by ``undetermined_coefficients`` hints.

    SymPy currently has no way to convert `\\sin^n(x) \\cos^m(y)` into a sum of
    only `\\sin(a x)` and `\\cos(b x)` terms, so these are not implemented.  So,
    for example, you will need to manually convert `\\sin^2(x)` into `[1 +
    \\cos(2 x)]/2` to properly apply the method of undetermined coefficients on
    it.

    Examples
    ========

    >>> from sympy import log, exp
    >>> from sympy.solvers.ode.nonhomogeneous import _undetermined_coefficients_match
    >>> from sympy.abc import x
    >>> _undetermined_coefficients_match(9*x*exp(x) + exp(-x), x)
    {'test': True, 'trialset': {x*exp(x), exp(-x), exp(x)}}
    >>> _undetermined_coefficients_match(log(x), x)
    {'test': False}

    """
    pass
# WARNING: Decompyle incomplete


def _solve_undetermined_coefficients(eq, func, order, match, trialset):
    """
    Helper function for the method of undetermined coefficients.

    See the
    :py:meth:`~sympy.solvers.ode.single.NthLinearConstantCoeffUndeterminedCoefficients`
    docstring for more information on this method.

    The parameter ``trialset`` is the set of trial functions as returned by
    ``_undetermined_coefficients_match()['trialset']``.

    The parameter ``match`` should be a dictionary that has the following
    keys:

    ``list``
    A list of solutions to the homogeneous equation.

    ``sol``
    The general solution.

    """
    r = match
    coeffs = numbered_symbols('a', cls = Dummy)
    coefflist = []
    gensols = r['list']
    gsol = r['sol']
    f = func.func
    x = func.args[0]
    if len(gensols) != order:
        raise NotImplementedError('Cannot find ' + str(order) + ' solutions to the homogeneous equation necessary to apply' + ' undetermined coefficients to ' + str(eq) + ' (number of terms != order)')
    trialfunc = 0
    for i in trialset:
        c = next(coeffs)
        coefflist.append(c)
        trialfunc += c * i
        eqs = sub_func_doit(eq, f(x), trialfunc)
        coeffsdict = dict(list(zip(trialset, [
            0] * (len(trialset) + 1))))
        eqs = _mexpand(eqs)
        for i in Add.make_args(eqs):
            s = separatevars(i, dict = True, symbols = [
                x])
            if coeffsdict.get(s[x]):
                continue
            s['coeff'] = None
            coeffvals = solve(list(coeffsdict.values()), coefflist)
            if not coeffvals:
                raise NotImplementedError('Could not solve `%s` using the method of undetermined coefficients (unable to solve for coefficients).' % eq)
            psol = trialfunc.subs(coeffvals)
            return Eq(f(x), gsol.rhs + psol)
