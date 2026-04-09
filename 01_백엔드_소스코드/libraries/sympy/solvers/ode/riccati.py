# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: riccati.pyc (Python 3.11)

'''
This module contains :py:meth:`~sympy.solvers.ode.riccati.solve_riccati`,
a function which gives all rational particular solutions to first order
Riccati ODEs. A general first order Riccati ODE is given by -

.. math:: y\' = b_0(x) + b_1(x)w + b_2(x)w^2

where `b_0, b_1` and `b_2` can be arbitrary rational functions of `x`
with `b_2 \\ne 0`. When `b_2 = 0`, the equation is not a Riccati ODE
anymore and becomes a Linear ODE. Similarly, when `b_0 = 0`, the equation
is a Bernoulli ODE. The algorithm presented below can find rational
solution(s) to all ODEs with `b_2 \\ne 0` that have a rational solution,
or prove that no rational solution exists for the equation.

Background
==========

A Riccati equation can be transformed to its normal form

.. math:: y\' + y^2 = a(x)

using the transformation

.. math:: y = -b_2(x) - \\frac{b\'_2(x)}{2 b_2(x)} - \\frac{b_1(x)}{2}

where `a(x)` is given by

.. math:: a(x) = \\frac{1}{4}\\left(\\frac{b_2\'}{b_2} + b_1\\right)^2 - \\frac{1}{2}\\left(\\frac{b_2\'}{b_2} + b_1\\right)\' - b_0 b_2

Thus, we can develop an algorithm to solve for the Riccati equation
in its normal form, which would in turn give us the solution for
the original Riccati equation.

Algorithm
=========

The algorithm implemented here is presented in the Ph.D thesis
"Rational and Algebraic Solutions of First-Order Algebraic ODEs"
by N. Thieu Vo. The entire thesis can be found here -
https://www3.risc.jku.at/publications/download/risc_5387/PhDThesisThieu.pdf

We have only implemented the Rational Riccati solver (Algorithm 11,
Pg 78-82 in Thesis). Before we proceed towards the implementation
of the algorithm, a few definitions to understand are -

1. Valuation of a Rational Function at `\\infty`:
    The valuation of a rational function `p(x)` at `\\infty` is equal
    to the difference between the degree of the denominator and the
    numerator of `p(x)`.

    NOTE: A general definition of valuation of a rational function
    at any value of `x` can be found in Pg 63 of the thesis, but
    is not of any interest for this algorithm.

2. Zeros and Poles of a Rational Function:
    Let `a(x) = \\frac{S(x)}{T(x)}, T \\ne 0` be a rational function
    of `x`. Then -

    a. The Zeros of `a(x)` are the roots of `S(x)`.
    b. The Poles of `a(x)` are the roots of `T(x)`. However, `\\infty`
    can also be a pole of a(x). We say that `a(x)` has a pole at
    `\\infty` if `a(\\frac{1}{x})` has a pole at 0.

Every pole is associated with an order that is equal to the multiplicity
of its appearance as a root of `T(x)`. A pole is called a simple pole if
it has an order 1. Similarly, a pole is called a multiple pole if it has
an order `\\ge` 2.

Necessary Conditions
====================

For a Riccati equation in its normal form,

.. math:: y\' + y^2 = a(x)

we can define

a. A pole is called a movable pole if it is a pole of `y(x)` and is not
a pole of `a(x)`.
b. Similarly, a pole is called a non-movable pole if it is a pole of both
`y(x)` and `a(x)`.

Then, the algorithm states that a rational solution exists only if -

a. Every pole of `a(x)` must be either a simple pole or a multiple pole
of even order.
b. The valuation of `a(x)` at `\\infty` must be even or be `\\ge` 2.

This algorithm finds all possible rational solutions for the Riccati ODE.
If no rational solutions are found, it means that no rational solutions
exist.

The algorithm works for Riccati ODEs where the coefficients are rational
functions in the independent variable `x` with rational number coefficients
i.e. in `Q(x)`. The coefficients in the rational function cannot be floats,
irrational numbers, symbols or any other kind of expression. The reasons
for this are -

1. When using symbols, different symbols could take the same value and this
would affect the multiplicity of poles if symbols are present here.

2. An integer degree bound is required to calculate a polynomial solution
to an auxiliary differential equation, which in turn gives the particular
solution for the original ODE. If symbols/floats/irrational numbers are
present, we cannot determine if the expression for the degree bound is an
integer or not.

Solution
========

With these definitions, we can state a general form for the solution of
the equation. `y(x)` must have the form -

.. math:: y(x) = \\sum_{i=1}^{n} \\sum_{j=1}^{r_i} \\frac{c_{ij}}{(x - x_i)^j} + \\sum_{i=1}^{m} \\frac{1}{x - \\chi_i} + \\sum_{i=0}^{N} d_i x^i

where `x_1, x_2, \\dots, x_n` are non-movable poles of `a(x)`,
`\\chi_1, \\chi_2, \\dots, \\chi_m` are movable poles of `a(x)`, and the values
of `N, n, r_1, r_2, \\dots, r_n` can be determined from `a(x)`. The
coefficient vectors `(d_0, d_1, \\dots, d_N)` and `(c_{i1}, c_{i2}, \\dots, c_{i r_i})`
can be determined from `a(x)`. We will have 2 choices each of these vectors
and part of the procedure is figuring out which of the 2 should be used
to get the solution correctly.

Implementation
==============

In this implementation, we use ``Poly`` to represent a rational function
rather than using ``Expr`` since ``Poly`` is much faster. Since we cannot
represent rational functions directly using ``Poly``, we instead represent
a rational function with 2 ``Poly`` objects - one for its numerator and
the other for its denominator.

The code is written to match the steps given in the thesis (Pg 82)

Step 0 : Match the equation -
Find `b_0, b_1` and `b_2`. If `b_2 = 0` or no such functions exist, raise
an error

Step 1 : Transform the equation to its normal form as explained in the
theory section.

Step 2 : Initialize an empty set of solutions, ``sol``.

Step 3 : If `a(x) = 0`, append `\\frac{1}/{(x - C1)}` to ``sol``.

Step 4 : If `a(x)` is a rational non-zero number, append `\\pm \\sqrt{a}`
to ``sol``.

Step 5 : Find the poles and their multiplicities of `a(x)`. Let
the number of poles be `n`. Also find the valuation of `a(x)` at
`\\infty` using ``val_at_inf``.

NOTE: Although the algorithm considers `\\infty` as a pole, it is
not mentioned if it a part of the set of finite poles. `\\infty`
is NOT a part of the set of finite poles. If a pole exists at
`\\infty`, we use its multiplicity to find the laurent series of
`a(x)` about `\\infty`.

Step 6 : Find `n` c-vectors (one for each pole) and 1 d-vector using
``construct_c`` and ``construct_d``. Now, determine all the ``2**(n + 1)``
combinations of choosing between 2 choices for each of the `n` c-vectors
and 1 d-vector.

NOTE: The equation for `d_{-1}` in Case 4 (Pg 80) has a printinig
mistake. The term `- d_N` must be replaced with `-N d_N`. The same
has been explained in the code as well.

For each of these above combinations, do

Step 8 : Compute `m` in ``compute_m_ybar``. `m` is the degree bound of
the polynomial solution we must find for the auxiliary equation.

Step 9 : In ``compute_m_ybar``, compute ybar as well where ``ybar`` is
one part of y(x) -

.. math:: \\overline{y}(x) = \\sum_{i=1}^{n} \\sum_{j=1}^{r_i} \\frac{c_{ij}}{(x - x_i)^j} + \\sum_{i=0}^{N} d_i x^i

Step 10 : If `m` is a non-negative integer -

Step 11: Find a polynomial solution of degree `m` for the auxiliary equation.

There are 2 cases possible -

    a. `m` is a non-negative integer: We can solve for the coefficients
    in `p(x)` using Undetermined Coefficients.

    b. `m` is not a non-negative integer: In this case, we cannot find
    a polynomial solution to the auxiliary equation, and hence, we ignore
    this value of `m`.

Step 12 : For each `p(x)` that exists, append `ybar + \\frac{p\'(x)}{p(x)}`
to ``sol``.

Step 13 : For each solution in ``sol``, apply an inverse transformation,
so that the solutions of the original equation are found using the
solutions of the equation in its normal form.
'''
from itertools import product
from sympy.core import S
from sympy.core.add import Add
from sympy.core.numbers import oo, Float
from sympy.core.function import count_ops
from sympy.core.relational import Eq
from sympy.core.symbol import symbols, Symbol, Dummy
from sympy.functions import sqrt, exp
from sympy.functions.elementary.complexes import sign
from sympy.integrals.integrals import Integral
from sympy.polys.domains import ZZ
from sympy.polys.polytools import Poly
from sympy.polys.polyroots import roots
from sympy.solvers.solveset import linsolve

def riccati_normal(w, x, b1, b2):
    """
    Given a solution `w(x)` to the equation

    .. math:: w'(x) = b_0(x) + b_1(x)*w(x) + b_2(x)*w(x)^2

    and rational function coefficients `b_1(x)` and
    `b_2(x)`, this function transforms the solution to
    give a solution `y(x)` for its corresponding normal
    Riccati ODE

    .. math:: y'(x) + y(x)^2 = a(x)

    using the transformation

    .. math:: y(x) = -b_2(x)*w(x) - b'_2(x)/(2*b_2(x)) - b_1(x)/2
    """
    return -b2 * w - b2.diff(x) / (2 * b2) - b1 / 2


def riccati_inverse_normal(y, x, b1, b2, bp = (None,)):
    '''
    Inverse transforming the solution to the normal
    Riccati ODE to get the solution to the Riccati ODE.
    '''
    pass
# WARNING: Decompyle incomplete


def riccati_reduced(eq, f, x):
    '''
    Convert a Riccati ODE into its corresponding
    normal Riccati ODE.
    '''
    (match, funcs) = match_riccati(eq, f, x)
    if not match:
        return False
    (b0, b1, b2) = None
    a = (-b0 * b2 + b1 ** 2 / 4 - b1.diff(x) / 2) + 3 * b2.diff(x) ** 2 / (4 * b2 ** 2) + b1 * b2.diff(x) / (2 * b2) - b2.diff(x, 2) / (2 * b2)
    return f(x).diff(x) + f(x) ** 2 - a


def linsolve_dict(eq, syms):
    '''
    Get the output of linsolve as a dict
    '''
    sol = linsolve(eq, syms)
    if not sol:
        return { }
    return None(zip(syms, list(sol)[0]))


def match_riccati(eq, f, x):
    '''
    A function that matches and returns the coefficients
    if an equation is a Riccati ODE

    Parameters
    ==========

    eq: Equation to be matched
    f: Dependent variable
    x: Independent variable

    Returns
    =======

    match: True if equation is a Riccati ODE, False otherwise
    funcs: [b0, b1, b2] if match is True, [] otherwise. Here,
    b0, b1 and b2 are rational functions which match the equation.
    '''
    pass
# WARNING: Decompyle incomplete


def val_at_inf(num, den, x):
    return den.degree(x) - num.degree(x)


def check_necessary_conds(val_inf, muls):
    '''
    The necessary conditions for a rational solution
    to exist are as follows -

    i) Every pole of a(x) must be either a simple pole
    or a multiple pole of even order.

    ii) The valuation of a(x) at infinity must be even
    or be greater than or equal to 2.

    Here, a simple pole is a pole with multiplicity 1
    and a multiple pole is a pole with multiplicity
    greater than 1.
    '''
    if val_inf >= 2 or val_inf <= 0:
        if val_inf % 2 == 0:
            pass
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(muls())


def inverse_transform_poly(num, den, x):
    '''
    A function to make the substitution
    x -> 1/x in a rational function that
    is represented using Poly objects for
    numerator and denominator.
    '''
    one = Poly(1, x)
    xpoly = Poly(x, x)
    pwr = val_at_inf(num, den, x)
    if pwr >= 0:
        if num.expr != 0:
            num = num.transform(one, xpoly) * x ** pwr
            den = den.transform(one, xpoly)
        else:
            num = num.transform(one, xpoly)
            den = den.transform(one, xpoly) * x ** (-pwr)
    return num.cancel(den, include = True)


def limit_at_inf(num, den, x):
    '''
    Find the limit of a rational function
    at oo
    '''
    pwr = -val_at_inf(num, den, x)
    if pwr > 0:
        return oo * sign(num.LC() / den.LC())
    if None == 0:
        return num.LC() / den.LC()


def construct_c_case_1(num, den, x, pole):
    (num1, den1) = (num * Poly((x - pole) ** 2, x, extension = True)).cancel(den, include = True)
    r = num1.subs(x, pole) / den1.subs(x, pole)
    if r != -S(1) / 4:
        return [
            [
                (1 + sqrt(1 + 4 * r)) / 2],
            [
                (1 - sqrt(1 + 4 * r)) / 2]]
    return [
        [
            None.Half]]


def construct_c_case_2(num, den, x, pole, mul):
    ri = mul // 2
    ser = rational_laurent_series(num, den, x, pole, mul, 6)
    cplus = range(ri)()
    cplus[ri - 1] = sqrt(ser[2 * ri])
    s = ri - 1
    sm = 0
    for s in range(ri - 1, 0, -1):
        sm = 0
        for j in range(s + 1, ri):
            sm += cplus[j - 1] * cplus[ri + s - j - 1]
            if s != 1:
                cplus[s - 1] = (ser[ri + s] - sm) / (2 * cplus[ri - 1])
        cminus = cplus()
        cplus[0] = (ser[ri + s] - sm - ri * cplus[ri - 1]) / (2 * cplus[ri - 1])
        cminus[0] = (ser[ri + s] - sm - ri * cminus[ri - 1]) / (2 * cminus[ri - 1])
        if cplus != cminus:
            return [
                cplus,
                cminus]
        return (lambda .0: [ -x for x in .0 ])


def construct_c_case_3():
    return [
        [
            1]]


def construct_c(num, den, x, poles, muls):
    '''
    Helper function to calculate the coefficients
    in the c-vector for each pole.
    '''
    c = []
    for pole, mul in zip(poles, muls):
        c.append([])
        if mul == 1:
            c[-1].extend(construct_c_case_3())
            continue
        if mul == 2:
            c[-1].extend(construct_c_case_1(num, den, x, pole))
            continue
        c[-1].extend(construct_c_case_2(num, den, x, pole, mul))
        return c


def construct_d_case_4(ser, N):
    dplus = range(N + 2)()
    dplus[N] = sqrt(ser[2 * N])
    for s in range(N - 1, -2, -1):
        sm = 0
        for j in range(s + 1, N):
            sm += dplus[j] * dplus[N + s - j]
            if s != -1:
                dplus[s] = (ser[N + s] - sm) / (2 * dplus[N])
        dminus = dplus()
        dplus[-1] = (ser[N + s] - N * dplus[N] - sm) / (2 * dplus[N])
        dminus[-1] = (ser[N + s] - N * dminus[N] - sm) / (2 * dminus[N])
        if dplus != dminus:
            return [
                dplus,
                dminus]
        return (lambda .0: [ -x for x in .0 ])


def construct_d_case_5(ser):
    dplus = [
        0,
        0]
    dplus[0] = sqrt(ser[0])
    dplus[-1] = ser[-1] / (2 * dplus[0])
    dminus = dplus()
    if dplus != dminus:
        return [
            dplus,
            dminus]
    return (lambda .0: [ -x for x in .0 ])


def construct_d_case_6(num, den, x):
    s_inf = limit_at_inf(Poly(x ** 2, x) * num, den, x)
    if s_inf != -S(1) / 4:
        return [
            [
                (1 + sqrt(1 + 4 * s_inf)) / 2],
            [
                (1 - sqrt(1 + 4 * s_inf)) / 2]]
    return [
        [
            None.Half]]


def construct_d(num, den, x, val_inf):
    '''
    Helper function to calculate the coefficients
    in the d-vector based on the valuation of the
    function at oo.
    '''
    N = -val_inf // 2
    mul = -val_inf if val_inf < 0 else 0
    ser = rational_laurent_series(num, den, x, oo, mul, 1)
    if val_inf < 0:
        d = construct_d_case_4(ser, N)
    elif val_inf == 0:
        d = construct_d_case_5(ser)
    else:
        d = construct_d_case_6(num, den, x)
    return d


def rational_laurent_series(num, den, x, r, m, n):
    '''
    The function computes the Laurent series coefficients
    of a rational function.

    Parameters
    ==========

    num: A Poly object that is the numerator of `f(x)`.
    den: A Poly object that is the denominator of `f(x)`.
    x: The variable of expansion of the series.
    r: The point of expansion of the series.
    m: Multiplicity of r if r is a pole of `f(x)`. Should
    be zero otherwise.
    n: Order of the term upto which the series is expanded.

    Returns
    =======

    series: A dictionary that has power of the term as key
    and coefficient of that term as value.

    Below is a basic outline of how the Laurent series of a
    rational function `f(x)` about `x_0` is being calculated -

    1. Substitute `x + x_0` in place of `x`. If `x_0`
    is a pole of `f(x)`, multiply the expression by `x^m`
    where `m` is the multiplicity of `x_0`. Denote the
    the resulting expression as g(x). We do this substitution
    so that we can now find the Laurent series of g(x) about
    `x = 0`.

    2. We can then assume that the Laurent series of `g(x)`
    takes the following form -

    .. math:: g(x) = \\frac{num(x)}{den(x)} = \\sum_{m = 0}^{\\infty} a_m x^m

    where `a_m` denotes the Laurent series coefficients.

    3. Multiply the denominator to the RHS of the equation
    and form a recurrence relation for the coefficients `a_m`.
    '''
    pass
# WARNING: Decompyle incomplete


def compute_m_ybar(x, poles, choice, N):
    '''
    Helper function to calculate -

    1. m - The degree bound for the polynomial
    solution that must be found for the auxiliary
    differential equation.

    2. ybar - Part of the solution which can be
    computed using the poles, c and d vectors.
    '''
    ybar = 0
    m = Poly(choice[-1][-1], x, extension = True)
    dybar = []
# WARNING: Decompyle incomplete


def solve_aux_eq(numa, dena, numy, deny, x, m):
    '''
    Helper function to find a polynomial solution
    of degree m for the auxiliary differential
    equation.
    '''
    psyms = symbols(f'''C0:{m}''', cls = Dummy)
    K = ZZ[psyms]
    psol = Poly(K.gens, x, domain = K) + Poly(x ** m, x, domain = K)
    auxeq = (dena * ((numy.diff(x) * deny - numy * deny.diff(x)) + numy ** 2) - numa * deny ** 2) * psol
    if m >= 1:
        px = psol.diff(x)
        auxeq += px * 2 * numy * deny * dena
    if m >= 2:
        auxeq += px.diff(x) * deny ** 2 * dena
    if m != 0:
        return (psol, linsolve_dict(auxeq.all_coeffs(), psyms), True)
    return (None.One, auxeq, auxeq == 0)


def remove_redundant_sols(sol1, sol2, x):
    '''
    Helper function to remove redundant
    solutions to the differential equation.
    '''
    pass
# WARNING: Decompyle incomplete


def get_gen_sol_from_part_sol(part_sols, a, x):
    '''"
    Helper function which computes the general
    solution for a Riccati ODE from its particular
    solutions.

    There are 3 cases to find the general solution
    from the particular solutions for a Riccati ODE
    depending on the number of particular solution(s)
    we have - 1, 2 or 3.

    For more information, see Section 6 of
    "Methods of Solution of the Riccati Differential Equation"
    by D. R. Haaheim and F. M. Stein
    '''
    if len(part_sols) == 0:
        return []
    if None(part_sols) == 1:
        y1 = part_sols[0]
        i = exp(Integral(2 * y1, x))
        z = i * Integral(a / i, x)
        z = z.doit()
        if a == 0 or z == 0:
            return y1
        return None + 1 / z
    if None(part_sols) == 2:
        (y1, y2) = part_sols
        if len(y1.atoms(Dummy)) + len(y2.atoms(Dummy)) > 0:
            u = exp(Integral(y2 - y1, x)).doit()
        else:
            C1 = Dummy('C1')
            u = C1 * exp(Integral(y2 - y1, x)).doit()
        if u == 1:
            return y2
        return (None * u - y1) / (u - 1)
    (y1, y2, y3) = None[:3]
    C1 = Dummy('C1')
    return (C1 + 1) * y2 * (y1 - y3) / (C1 * y1 + y2 - (C1 + 1) * y3)


def solve_riccati(fx, x, b0, b1, b2, gensol = (False,)):
    '''
    The main function that gives particular/general
    solutions to Riccati ODEs that have atleast 1
    rational particular solution.
    '''
    pass
# WARNING: Decompyle incomplete
