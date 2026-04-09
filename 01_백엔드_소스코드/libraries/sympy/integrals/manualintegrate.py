# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: manualintegrate.pyc (Python 3.11)

'''Integration method that emulates by-hand techniques.

This module also provides functionality to get the steps used to evaluate a
particular integral, in the ``integral_steps`` function. This will return
nested ``Rule`` s representing the integration rules used.

Each ``Rule`` class represents a (maybe parametrized) integration rule, e.g.
``SinRule`` for integrating ``sin(x)`` and ``ReciprocalSqrtQuadraticRule``
for integrating ``1/sqrt(a+b*x+c*x**2)``. The ``eval`` method returns the
integration result.

The ``manualintegrate`` function computes the integral by calling ``eval``
on the rule returned by ``integral_steps``.

The integrator can be extended with new heuristics and evaluation
techniques. To do so, extend the ``Rule`` class, implement ``eval`` method,
then write a function that accepts an ``IntegralInfo`` object and returns
either a ``Rule`` instance or ``None``. If the new technique requires a new
match, add the key and call to the antiderivative function to integral_steps.
To enable simple substitutions, add the match to find_substitutions.

'''
from __future__ import annotations
from typing import NamedTuple, Type, Callable, Sequence
from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections import defaultdict
from collections.abc import Mapping
from sympy.core.add import Add
from sympy.core.cache import cacheit
from sympy.core.containers import Dict
from sympy.core.expr import Expr
from sympy.core.function import Derivative
from sympy.core.logic import fuzzy_not
from sympy.core.mul import Mul
from sympy.core.numbers import Integer, Number, E
from sympy.core.power import Pow
from sympy.core.relational import Eq, Ne, Boolean
from sympy.core.singleton import S
from sympy.core.symbol import Dummy, Symbol, Wild
from sympy.functions.elementary.complexes import Abs
from sympy.functions.elementary.exponential import exp, log
from sympy.functions.elementary.hyperbolic import HyperbolicFunction, csch, cosh, coth, sech, sinh, tanh, asinh
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.elementary.trigonometric import TrigonometricFunction, cos, sin, tan, cot, csc, sec, acos, asin, atan, acot, acsc, asec
from sympy.functions.special.delta_functions import Heaviside, DiracDelta
from sympy.functions.special.error_functions import erf, erfi, fresnelc, fresnels, Ci, Chi, Si, Shi, Ei, li
from sympy.functions.special.gamma_functions import uppergamma
from sympy.functions.special.elliptic_integrals import elliptic_e, elliptic_f
from sympy.functions.special.polynomials import chebyshevt, chebyshevu, legendre, hermite, laguerre, assoc_laguerre, gegenbauer, jacobi, OrthogonalPolynomial
from sympy.functions.special.zeta_functions import polylog
from integrals import Integral
from sympy.logic.boolalg import And
from sympy.ntheory.factor_ import primefactors
from sympy.polys.polytools import degree, lcm_list, gcd_list, Poly
from sympy.simplify.radsimp import fraction
from sympy.simplify.simplify import simplify
from sympy.solvers.solvers import solve
from sympy.strategies.core import switch, do_one, null_safe, condition
from sympy.utilities.iterables import iterable
from sympy.utilities.misc import debug
Rule = <NODE:12>()
AtomicRule = <NODE:12>()
ConstantRule = <NODE:12>()
ConstantTimesRule = <NODE:12>()
PowerRule = <NODE:12>()
NestedPowRule = <NODE:12>()
AddRule = <NODE:12>()
URule = <NODE:12>()
PartsRule = <NODE:12>()
CyclicPartsRule = <NODE:12>()
TrigRule = <NODE:12>()
SinRule = <NODE:12>()
CosRule = <NODE:12>()
SecTanRule = <NODE:12>()
CscCotRule = <NODE:12>()
Sec2Rule = <NODE:12>()
Csc2Rule = <NODE:12>()
HyperbolicRule = <NODE:12>()
SinhRule = <NODE:12>()
CoshRule = <NODE:12>()
ExpRule = <NODE:12>()
ReciprocalRule = <NODE:12>()
ArcsinRule = <NODE:12>()
ArcsinhRule = <NODE:12>()
ReciprocalSqrtQuadraticRule = <NODE:12>()
SqrtQuadraticDenomRule = <NODE:12>()
SqrtQuadraticRule = <NODE:12>()
AlternativeRule = <NODE:12>()
DontKnowRule = <NODE:12>()
DerivativeRule = <NODE:12>()
RewriteRule = <NODE:12>()
CompleteSquareRule = <NODE:12>()
PiecewiseRule = <NODE:12>()
HeavisideRule = <NODE:12>()
DiracDeltaRule = <NODE:12>()
TrigSubstitutionRule = <NODE:12>()
ArctanRule = <NODE:12>()
OrthogonalPolyRule = <NODE:12>()
JacobiRule = <NODE:12>()
GegenbauerRule = <NODE:12>()
ChebyshevTRule = <NODE:12>()
ChebyshevURule = <NODE:12>()
LegendreRule = <NODE:12>()
HermiteRule = <NODE:12>()
LaguerreRule = <NODE:12>()
AssocLaguerreRule = <NODE:12>()
IRule = <NODE:12>()
CiRule = <NODE:12>()
ChiRule = <NODE:12>()
EiRule = <NODE:12>()
SiRule = <NODE:12>()
ShiRule = <NODE:12>()
LiRule = <NODE:12>()
ErfRule = <NODE:12>()
FresnelCRule = <NODE:12>()
FresnelSRule = <NODE:12>()
PolylogRule = <NODE:12>()
UpperGammaRule = <NODE:12>()
EllipticFRule = <NODE:12>()
EllipticERule = <NODE:12>()

class IntegralInfo(NamedTuple):
    symbol: 'Symbol' = 'IntegralInfo'


def manual_diff(f, symbol):
    """Derivative of f in form expected by find_substitutions

    SymPy's derivatives for some trig functions (like cot) are not in a form
    that works well with finding substitutions; this replaces the
    derivatives for those particular forms with something that works better.

    """
    pass
# WARNING: Decompyle incomplete


def manual_subs(expr, *args):
    '''
    A wrapper for `expr.subs(*args)` with additional logic for substitution
    of invertible functions.
    '''
    pass
# WARNING: Decompyle incomplete

inverse_trig_functions = (atan, asin, acos, acot, acsc, asec)

def find_substitutions(integrand, symbol, u_var):
    pass
# WARNING: Decompyle incomplete


def rewriter(condition, rewrite):
    '''Strategy that rewrites an integrand.'''
    pass
# WARNING: Decompyle incomplete


def proxy_rewriter(condition, rewrite):
    '''Strategy that rewrites an integrand based on some other criteria.'''
    pass
# WARNING: Decompyle incomplete


def multiplexer(conditions):
    '''Apply the rule that matches the condition, else None'''
    pass
# WARNING: Decompyle incomplete


def alternatives(*rules):
    '''Strategy that makes an AlternativeRule out of multiple possible results.'''
    pass
# WARNING: Decompyle incomplete


def constant_rule(integral):
    pass
# WARNING: Decompyle incomplete


def power_rule(integral):
    (integrand, symbol) = integral
    (base, expt) = integrand.as_base_exp()
    if symbol not in expt.free_symbols and isinstance(base, Symbol):
        if simplify(expt + 1) == 0:
            return ReciprocalRule(integrand, symbol, base)
        return None(integrand, symbol, base, expt)
    if None not in base.free_symbols or isinstance(expt, Symbol):
        rule = ExpRule(integrand, symbol, base, expt)
        if fuzzy_not(log(base).is_zero):
            return rule
        if None(base).is_zero:
            return ConstantRule(1, symbol)
        return None(integrand, symbol, [
            (rule, Ne(log(base), 0)),
            (ConstantRule(1, symbol), True)])
    return None


def exp_rule(integral):
    (integrand, symbol) = integral
    if isinstance(integrand.args[0], Symbol):
        return ExpRule(integrand, symbol, E, integrand.args[0])


def orthogonal_poly_rule(integral):
    pass
# WARNING: Decompyle incomplete

_special_function_patterns: 'list[tuple[Type, Expr, Callable | None, tuple]]' = []
_wilds = []
_symbol = Dummy('x')

def special_function_rule(integral):
    pass
# WARNING: Decompyle incomplete


def _add_degenerate_step(generic_cond = dataclass, generic_step = dataclass, degenerate_step = None):
    pass
# WARNING: Decompyle incomplete


def nested_pow_rule(integral = dataclass):
    pass
# WARNING: Decompyle incomplete


def inverse_trig_rule(integral = dataclass, degenerate = dataclass):
    '''
    Set degenerate=False on recursive call where coefficient of quadratic term
    is assumed non-zero.
    '''
    pass
# WARNING: Decompyle incomplete


def add_rule(integral):
    pass
# WARNING: Decompyle incomplete


def mul_rule(integral = dataclass):
    (integrand, symbol) = integral
    (coeff, f) = integrand.as_independent(symbol)
# WARNING: Decompyle incomplete


def _parts_rule(integrand = dataclass, symbol = dataclass):
    pass
# WARNING: Decompyle incomplete


def parts_rule(integral):
    pass
# WARNING: Decompyle incomplete


def trig_rule(integral):
    (integrand, symbol) = integral
    if integrand == sin(symbol):
        return SinRule(integrand, symbol)
    if None == cos(symbol):
        return CosRule(integrand, symbol)
    if None == sec(symbol) ** 2:
        return Sec2Rule(integrand, symbol)
    if None == csc(symbol) ** 2:
        return Csc2Rule(integrand, symbol)
# WARNING: Decompyle incomplete


def trig_product_rule(integral = dataclass):
    (integrand, symbol) = integral
    if integrand == sec(symbol) * tan(symbol):
        return SecTanRule(integrand, symbol)
    if None == csc(symbol) * cot(symbol):
        return CscCotRule(integrand, symbol)


def quadratic_denom_rule(integral):
    (integrand, symbol) = integral
    a = Wild('a', exclude = [
        symbol])
    b = Wild('b', exclude = [
        symbol])
    c = Wild('c', exclude = [
        symbol])
    match = integrand.match(a / (b * symbol ** 2 + c))
    if match:
        c = match[c]
        b = match[b]
        a = match[a]
        general_rule = ArctanRule(integrand, symbol, a, b, c)
        if b.is_extended_real and c.is_extended_real:
            positive_cond = c / b > 0
            if positive_cond is S.true:
                return general_rule
            coeff = None / (2 * sqrt(-c) * sqrt(b))
            constant = sqrt(-c / b)
            r1 = 1 / (symbol - constant)
            r2 = 1 / (symbol + constant)
            log_steps = [
                ReciprocalRule(r1, symbol, symbol - constant),
                ConstantTimesRule(-r2, symbol, -1, r2, ReciprocalRule(r2, symbol, symbol + constant))]
            rewritten = r1 - r2
            sub = r1 - r2
            negative_step = AddRule(sub, symbol, log_steps)
            if coeff != 1:
                rewritten = Mul(coeff, sub, evaluate = False)
                negative_step = ConstantTimesRule(rewritten, symbol, coeff, sub, negative_step)
            negative_step = RewriteRule(integrand, symbol, rewritten, negative_step)
            if positive_cond is S.false:
                return negative_step
            return None(integrand, symbol, [
                (general_rule, positive_cond),
                (negative_step, S.true)])
        power = None(integrand, symbol, symbol, -2)
        if b != 1:
            power = ConstantTimesRule(integrand, symbol, 1 / b, symbol ** -2, power)
        return PiecewiseRule(integrand, symbol, [
            (general_rule, Ne(c, 0)),
            (power, True)])
    d = None('d', exclude = [
        symbol])
    match2 = integrand.match(a / (b * symbol ** 2 + c * symbol + d))
    if match2:
        c = match2[c]
        b = match2[b]
        if b.is_zero:
            return None
        u = None('u')
        u_func = symbol + c / (2 * b)
        integrand2 = integrand.subs(symbol, u - c / (2 * b))
        next_step = integral_steps(integrand2, u)
        if next_step:
            return URule(integrand2, symbol, u, u_func, next_step)
        return None
    e = None('e', exclude = [
        symbol])
    match3 = integrand.match((a * symbol + b) / (c * symbol ** 2 + d * symbol + e))
    if match3:
        (a, b, c, d, e) = (match3[a], match3[b], match3[c], match3[d], match3[e])
        if c.is_zero:
            return None
        denominator = None * symbol ** 2 + d * symbol + e
        const = a / (2 * c)
        numer1 = 2 * c * symbol + d
        numer2 = -const * d + b
        u = Dummy('u')
        step1 = URule(integrand, symbol, u, denominator, integral_steps(u ** -1, u))
        if const != 1:
            step1 = ConstantTimesRule(const * numer1 / denominator, symbol, const, numer1 / denominator, step1)
        if numer2.is_zero:
            return step1
        step2 = None(numer2 / denominator, symbol)
        substeps = AddRule(integrand, symbol, [
            step1,
            step2])
        rewriten = const * numer1 / denominator + numer2 / denominator
        return RewriteRule(integrand, symbol, rewriten, substeps)


def sqrt_linear_rule(integral = dataclass):
    '''
    Substitute common (a+b*x)**(1/n)
    '''
    pass
# WARNING: Decompyle incomplete


def sqrt_quadratic_rule(integral = dataclass, degenerate = dataclass):
    pass
# WARNING: Decompyle incomplete


def hyperbolic_rule(integral = dataclass):
    (integrand, symbol) = integral
    if isinstance(integrand, HyperbolicFunction) or integrand.args[0] == symbol:
        if integrand.func == sinh:
            return SinhRule(integrand, symbol)
        if None.func == cosh:
            return CoshRule(integrand, symbol)
        u = None('u')
        if integrand.func == tanh:
            rewritten = sinh(symbol) / cosh(symbol)
            return RewriteRule(integrand, symbol, rewritten, URule(rewritten, symbol, u, cosh(symbol), ReciprocalRule(1 / u, u, u)))
        if None.func == coth:
            rewritten = cosh(symbol) / sinh(symbol)
            return RewriteRule(integrand, symbol, rewritten, URule(rewritten, symbol, u, sinh(symbol), ReciprocalRule(1 / u, u, u)))
        rewritten = None.rewrite(tanh)
        if integrand.func == sech:
            return RewriteRule(integrand, symbol, rewritten, URule(rewritten, symbol, u, tanh(symbol / 2), ArctanRule(2 / (u ** 2 + 1), u, S(2), S.One, S.One)))
        if None.func == csch:
            return RewriteRule(integrand, symbol, rewritten, URule(rewritten, symbol, u, tanh(symbol / 2), ReciprocalRule(1 / u, u, u)))
        return None
    return None

make_wilds = (lambda symbol: a = Wild('a', exclude = [
symbol])b = Wild('b', exclude = [
symbol])m = Wild('m', exclude = [
symbol], properties = [
(lambda n: isinstance(n, Integer))])
    n = Wild('n', exclude = [
        symbol], properties = [
        (lambda n: isinstance(n, Integer))])
    return (a, b, m, n)
)()
sincos_pattern = (lambda symbol: (a, b, m, n) = make_wilds(symbol)pattern = sin(a * symbol) ** m * cos(b * symbol) ** n(pattern, a, b, m, n))()
tansec_pattern = (lambda symbol: (a, b, m, n) = make_wilds(symbol)pattern = tan(a * symbol) ** m * sec(b * symbol) ** n(pattern, a, b, m, n))()
cotcsc_pattern = (lambda symbol: (a, b, m, n) = make_wilds(symbol)pattern = cot(a * symbol) ** m * csc(b * symbol) ** n(pattern, a, b, m, n))()
heaviside_pattern = (lambda symbol: m = Wild('m', exclude = [
symbol])b = Wild('b', exclude = [
symbol])g = Wild('g')pattern = Heaviside(m * symbol + b) * g(pattern, m, b, g))()

def uncurry(func):
    pass
# WARNING: Decompyle incomplete


def trig_rewriter(rewrite):
    pass
# WARNING: Decompyle incomplete

sincos_botheven_condition = uncurry((lambda a, b, m, n, i, s:
