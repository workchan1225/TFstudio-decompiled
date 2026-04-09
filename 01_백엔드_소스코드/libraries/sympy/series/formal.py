# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: formal.pyc (Python 3.11)

'''Formal Power Series'''
from collections import defaultdict
from sympy.core.numbers import nan, oo, zoo
from sympy.core.add import Add
from sympy.core.expr import Expr
from sympy.core.function import Derivative, Function, expand
from sympy.core.mul import Mul
from sympy.core.numbers import Rational
from sympy.core.relational import Eq
from sympy.sets.sets import Interval
from sympy.core.singleton import S
from sympy.core.symbol import Wild, Dummy, symbols, Symbol
from sympy.core.sympify import sympify
from sympy.discrete.convolutions import convolution
from sympy.functions.combinatorial.factorials import binomial, factorial, rf
from sympy.functions.combinatorial.numbers import bell
from sympy.functions.elementary.integers import floor, frac, ceiling
from sympy.functions.elementary.miscellaneous import Min, Max
from sympy.functions.elementary.piecewise import Piecewise
from sympy.series.limits import Limit
from sympy.series.order import Order
from sympy.series.sequences import sequence
from sympy.series.series_class import SeriesBase
from sympy.utilities.iterables import iterable

def rational_algorithm(f, x, k, order, full = (4, False)):
    """
    Rational algorithm for computing
    formula of coefficients of Formal Power Series
    of a function.

    Explanation
    ===========

    Applicable when f(x) or some derivative of f(x)
    is a rational function in x.

    :func:`rational_algorithm` uses :func:`~.apart` function for partial fraction
    decomposition. :func:`~.apart` by default uses 'undetermined coefficients
    method'. By setting ``full=True``, 'Bronstein's algorithm' can be used
    instead.

    Looks for derivative of a function up to 4'th order (by default).
    This can be overridden using order option.

    Parameters
    ==========

    x : Symbol
    order : int, optional
        Order of the derivative of ``f``, Default is 4.
    full : bool

    Returns
    =======

    formula : Expr
    ind : Expr
        Independent terms.
    order : int
    full : bool

    Examples
    ========

    >>> from sympy import log, atan
    >>> from sympy.series.formal import rational_algorithm as ra
    >>> from sympy.abc import x, k

    >>> ra(1 / (1 - x), x, k)
    (1, 0, 0)
    >>> ra(log(1 + x), x, k)
    (-1/((-1)**k*k), 0, 1)

    >>> ra(atan(x), x, k, full=True)
    ((-I/(2*(-I)**k) + I/(2*I**k))/k, 0, 1)

    Notes
    =====

    By setting ``full=True``, range of admissible functions to be solved using
    ``rational_algorithm`` can be increased. This option should be used
    carefully as it can significantly slow down the computation as ``doit`` is
    performed on the :class:`~.RootSum` object returned by the :func:`~.apart`
    function. Use ``full=False`` whenever possible.

    See Also
    ========

    sympy.polys.partfrac.apart

    References
    ==========

    .. [1] Formal Power Series - Dominik Gruntz, Wolfram Koepf
    .. [2] Power Series in Computer Algebra - Wolfram Koepf

    """
    RootSum = RootSum
    apart = apart
    import sympy.polys
    integrate = integrate
    import sympy.integrals
    diff = f
    ds = []
    for i in range(order + 1):
        if i:
            diff = diff.diff(x)
        if diff.is_rational_function(x):
            sep = S.Zero
            coeff = S.Zero
            terms = apart(diff, x, full = full)
            if terms.has(RootSum):
                terms = terms.doit()
            for t in Add.make_args(terms):
                (num, den) = t.as_numer_denom()
                if not den.has(x):
                    sep += t
                    continue
                if isinstance(den, Mul):
                    ind = den.as_independent(x)
                    den = ind[1]
                    num /= ind[0]
                (den, j) = den.as_base_exp()
                (a, xterm) = den.as_coeff_add(x)
                if not a:
                    sep += t
                    continue
                xc = xterm[0].coeff(x)
                a /= -xc
                num /= xc ** j
                ak = -1 ** j * num * binomial(j + k - 1, k).rewrite(factorial) / a ** (j + k)
                coeff += ak
                if coeff.is_zero:
                    return None
                if None.has(x) and coeff.has(zoo) and coeff.has(oo) or coeff.has(nan):
                    return None
                for j in None(i):
                    coeff = coeff / (k + j + 1)
                    sep = integrate(sep, x)
                    sep += (ds.pop() - sep).limit(x, 0)
                    
                    return None, (coeff.subs(k, k - i), sep, i)
                    ds.append(diff)
                    return None


def rational_independent(terms, x):
    '''
    Returns a list of all the rationally independent terms.

    Examples
    ========

    >>> from sympy import sin, cos
    >>> from sympy.series.formal import rational_independent
    >>> from sympy.abc import x

    >>> rational_independent([cos(x), sin(x)], x)
    [cos(x), sin(x)]
    >>> rational_independent([x**2, sin(x), x*sin(x), x**3], x)
    [x**3 + x**2, x*sin(x) + sin(x)]
    '''
    if not terms:
        return []
    ind = None[0:1]
    for t in terms[1:]:
        n = t.as_independent(x)[1]
        for i, term in enumerate(ind):
            d = term.as_independent(x)[1]
            q = (n / d).cancel()
            if q.is_rational_function(x):
                pass
            
            ind.append(t)
            return ind


def simpleDE(f, x, g, order = (4,)):
    """
    Generates simple DE.

    Explanation
    ===========

    DE is of the form

    .. math::
        f^k(x) + \\sum\\limits_{j=0}^{k-1} A_j f^j(x) = 0

    where :math:`A_j` should be rational function in x.

    Generates DE's upto order 4 (default). DE's can also have free parameters.

    By increasing order, higher order DE's can be found.

    Yields a tuple of (DE, order).
    """
    pass
# WARNING: Decompyle incomplete


def exp_re(DE, r, k):
    """Converts a DE with constant coefficients (explike) into a RE.

    Explanation
    ===========

    Performs the substitution:

    .. math::
        f^j(x) \\to r(k + j)

    Normalises the terms so that lowest order of a term is always r(k).

    Examples
    ========

    >>> from sympy import Function, Derivative
    >>> from sympy.series.formal import exp_re
    >>> from sympy.abc import x, k
    >>> f, r = Function('f'), Function('r')

    >>> exp_re(-f(x) + Derivative(f(x)), r, k)
    -r(k) + r(k + 1)
    >>> exp_re(Derivative(f(x), x) + Derivative(f(x), (x, 2)), r, k)
    r(k) + r(k + 1)

    See Also
    ========

    sympy.series.formal.hyper_re
    """
    RE = S.Zero
    g = DE.atoms(Function).pop()
    mini = None
# WARNING: Decompyle incomplete


def hyper_re(DE, r, k):
    """
    Converts a DE into a RE.

    Explanation
    ===========

    Performs the substitution:

    .. math::
        x^l f^j(x) \\to (k + 1 - l)_j . a_{k + j - l}

    Normalises the terms so that lowest order of a term is always r(k).

    Examples
    ========

    >>> from sympy import Function, Derivative
    >>> from sympy.series.formal import hyper_re
    >>> from sympy.abc import x, k
    >>> f, r = Function('f'), Function('r')

    >>> hyper_re(-f(x) + Derivative(f(x)), r, k)
    (k + 1)*r(k + 1) - r(k)
    >>> hyper_re(-x*f(x) + Derivative(f(x), (x, 2)), r, k)
    (k + 2)*(k + 3)*r(k + 3) - r(k)

    See Also
    ========

    sympy.series.formal.exp_re
    """
    RE = S.Zero
    g = DE.atoms(Function).pop()
    x = g.atoms(Symbol).pop()
    mini = None
# WARNING: Decompyle incomplete


def _transformation_a(f, x, P, Q, k, m, shift):
    f *= x ** (-shift)
    P = P.subs(k, k + shift)
    Q = Q.subs(k, k + shift)
    return (f, P, Q, m)


def _transformation_c(f, x, P, Q, k, m, scale):
    f = f.subs(x, x ** scale)
    P = P.subs(k, k / scale)
    Q = Q.subs(k, k / scale)
    m *= scale
    return (f, P, Q, m)


def _transformation_e(f, x, P, Q, k, m):
    f = f.diff(x)
    P = P.subs(k, k + 1) * (k + m + 1)
    Q = Q.subs(k, k + 1) * (k + 1)
    return (f, P, Q, m)


def _apply_shift(sol, shift):
    pass
# WARNING: Decompyle incomplete


def _apply_scale(sol, scale):
    pass
# WARNING: Decompyle incomplete


def _apply_integrate(sol, x, k):
    pass
# WARNING: Decompyle incomplete


def _compute_formula(f, x, P, Q, k, m, k_max):
    '''Computes the formula for f.'''
    pass
# WARNING: Decompyle incomplete


def _rsolve_hypergeometric(f, x, P, Q, k, m):
    '''
    Recursive wrapper to rsolve_hypergeometric.

    Explanation
    ===========

    Returns a Tuple of (formula, series independent terms,
    maximum power of x in independent terms) if successful
    otherwise ``None``.

    See :func:`rsolve_hypergeometric` for details.
    '''
    lcm = lcm
    roots = roots
    import sympy.polys
    integrate = integrate
    import sympy.integrals
    qroots = roots(Q, k)
    proots = roots(P, k)
    all_roots = dict(proots)
    all_roots.update(qroots)
    scale = (lambda .0: pass# WARNING: Decompyle incomplete
)(all_roots.items()())
    (f, P, Q, m) = _transformation_c(f, x, P, Q, k, m, scale)
    qroots = roots(Q, k)
# WARNING: Decompyle incomplete


def rsolve_hypergeometric(f, x, P, Q, k, m):
    """
    Solves RE of hypergeometric type.

    Explanation
    ===========

    Attempts to solve RE of the form

    Q(k)*a(k + m) - P(k)*a(k)

    Transformations that preserve Hypergeometric type:

        a. x**n*f(x): b(k + m) = R(k - n)*b(k)
        b. f(A*x): b(k + m) = A**m*R(k)*b(k)
        c. f(x**n): b(k + n*m) = R(k/n)*b(k)
        d. f(x**(1/m)): b(k + 1) = R(k*m)*b(k)
        e. f'(x): b(k + m) = ((k + m + 1)/(k + 1))*R(k + 1)*b(k)

    Some of these transformations have been used to solve the RE.

    Returns
    =======

    formula : Expr
    ind : Expr
        Independent terms.
    order : int

    Examples
    ========

    >>> from sympy import exp, ln, S
    >>> from sympy.series.formal import rsolve_hypergeometric as rh
    >>> from sympy.abc import x, k

    >>> rh(exp(x), x, -S.One, (k + 1), k, 1)
    (Piecewise((1/factorial(k), Eq(Mod(k, 1), 0)), (0, True)), 1, 1)

    >>> rh(ln(1 + x), x, k**2, k*(k + 1), k, 1)
    (Piecewise(((-1)**(k - 1)*factorial(k - 1)/RisingFactorial(2, k - 1),
     Eq(Mod(k, 1), 0)), (0, True)), x, 2)

    References
    ==========

    .. [1] Formal Power Series - Dominik Gruntz, Wolfram Koepf
    .. [2] Power Series in Computer Algebra - Wolfram Koepf
    """
    result = _rsolve_hypergeometric(f, x, P, Q, k, m)
# WARNING: Decompyle incomplete


def _solve_hyper_RE(f, x, RE, g, k):
    '''See docstring of :func:`rsolve_hypergeometric` for details.'''
    terms = Add.make_args(RE)
    if len(terms) == 2:
        gs = list(RE.atoms(Function))
        (P, Q) = map(RE.coeff, gs)
        m = gs[1].args[0] - gs[0].args[0]
        if m < 0:
            Q = P
            P = Q
            m = abs(m)
        return rsolve_hypergeometric(f, x, P, Q, k, m)


def _solve_explike_DE(f, x, DE, g, k):
    '''Solves DE with constant coefficients.'''
    rsolve = rsolve
    import sympy.solvers
    for t in Add.make_args(DE):
        (coeff, d) = t.as_independent(g)
        if coeff.free_symbols:
            return None
        RE = exp_re(DE, g, k)
        init = { }
        for i in range(len(Add.make_args(RE))):
            if i:
                f = f.diff(x)
            init[g(k).subs(k, i)] = f.limit(x, 0)
            sol = rsolve(RE, g(k), init)
            if sol:
                return (sol / factorial(k), S.Zero, S.Zero)
            return None


def _solve_simple(f, x, DE, g, k):
    '''Converts DE into RE and solves using :func:`rsolve`.'''
    rsolve = rsolve
    import sympy.solvers
    RE = hyper_re(DE, g, k)
    init = { }
    for i in range(len(Add.make_args(RE))):
        if i:
            f = f.diff(x)
        init[g(k).subs(k, i)] = f.limit(x, 0) / factorial(i)
        sol = rsolve(RE, g(k), init)
        if sol:
            return (sol, S.Zero, S.Zero)
        return None


def _transform_explike_DE(DE, g, x, order, syms):
    '''Converts DE with free parameters into DE with constant coefficients.'''
    linsolve = linsolve
    import sympy.solvers.solveset
    eq = []
    highest_coeff = DE.coeff(Derivative(g(x), x, order))
    for i in range(order):
        coeff = DE.coeff(Derivative(g(x), x, i))
        coeff = (coeff / highest_coeff).expand().collect(x)
        for t in Add.make_args(coeff):
            eq.append(t)
            temp = []
            for e in eq:
                if e.has(x):
                    pass
                elif e.has(Symbol):
                    temp.append(e)
                eq = temp
                if eq:
                    
                    def <genexpr>(.0):
                        pass
                    # WARNING: Decompyle incomplete

                    sol = zip(syms(<genexpr>, linsolve(eq, list(syms))()))
                    if sol:
                        DE = DE.subs(sol)
                        DE = DE.factor().as_coeff_mul(Derivative)[1][0]
                        DE = DE.collect(Derivative(g(x)))
    return DE


def _transform_DE_RE(DE, g, k, order, syms):
    '''Converts DE with free parameters into RE of hypergeometric type.'''
    linsolve = linsolve
    import sympy.solvers.solveset
    RE = hyper_re(DE, g, k)
    eq = []
    for i in range(1, order):
        coeff = RE.coeff(g(k + i))
        eq.append(coeff)
        
        def <genexpr>(.0):
            pass
        # WARNING: Decompyle incomplete

        sol = zip(syms(<genexpr>, linsolve(eq, list(syms))()))
        if sol:
            m = Wild('m')
            RE = RE.subs(sol)
            RE = RE.factor().as_numer_denom()[0].collect(g(k + m))
            RE = RE.as_coeff_mul(g)[1][0]
            for i in range(order):
                if RE.coeff(g(k + i)) and i:
                    RE = RE.subs(k, k - i)
                    dict
                
                return RE


def solve_de(f, x, DE, order, g, k):
    """
    Solves the DE.

    Explanation
    ===========

    Tries to solve DE by either converting into a RE containing two terms or
    converting into a DE having constant coefficients.

    Returns
    =======

    formula : Expr
    ind : Expr
        Independent terms.
    order : int

    Examples
    ========

    >>> from sympy import Derivative as D, Function
    >>> from sympy import exp, ln
    >>> from sympy.series.formal import solve_de
    >>> from sympy.abc import x, k
    >>> f = Function('f')

    >>> solve_de(exp(x), x, D(f(x), x) - f(x), 1, f, k)
    (Piecewise((1/factorial(k), Eq(Mod(k, 1), 0)), (0, True)), 1, 1)

    >>> solve_de(ln(1 + x), x, (x + 1)*D(f(x), x, 2) + D(f(x)), 2, f, k)
    (Piecewise(((-1)**(k - 1)*factorial(k - 1)/RisingFactorial(2, k - 1),
     Eq(Mod(k, 1), 0)), (0, True)), x, 2)
    """
    sol = None
    syms = DE.free_symbols.difference({
        g,
        x})
    if syms:
        RE = _transform_DE_RE(DE, g, k, order, syms)
    else:
        RE = hyper_re(DE, g, k)
    if not RE.free_symbols.difference({
        k}):
        sol = _solve_hyper_RE(f, x, RE, g, k)
    if sol:
        return sol
    if None:
        DE = _transform_explike_DE(DE, g, x, order, syms)
    if not DE.free_symbols.difference({
        x}):
        sol = _solve_explike_DE(f, x, DE, g, k)
    if sol:
        return sol


def hyper_algorithm(f, x, k, order = (4,)):
    '''
    Hypergeometric algorithm for computing Formal Power Series.

    Explanation
    ===========

    Steps:
        * Generates DE
        * Convert the DE into RE
        * Solves the RE

    Examples
    ========

    >>> from sympy import exp, ln
    >>> from sympy.series.formal import hyper_algorithm

    >>> from sympy.abc import x, k

    >>> hyper_algorithm(exp(x), x, k)
    (Piecewise((1/factorial(k), Eq(Mod(k, 1), 0)), (0, True)), 1, 1)

    >>> hyper_algorithm(ln(1 + x), x, k)
    (Piecewise(((-1)**(k - 1)*factorial(k - 1)/RisingFactorial(2, k - 1),
     Eq(Mod(k, 1), 0)), (0, True)), x, 2)

    See Also
    ========

    sympy.series.formal.simpleDE
    sympy.series.formal.solve_de
    '''
    g = Function('g')
    des = []
    sol = None
# WARNING: Decompyle incomplete


def _compute_fps(f, x, x0, dir, hyper, order, rational, full):
    '''Recursive wrapper to compute fps.

    See :func:`compute_fps` for details.
    '''
    pass
# WARNING: Decompyle incomplete


def compute_fps(f, x, x0, dir, hyper, order, rational, full = (0, 1, True, 4, True, False)):
    """
    Computes the formula for Formal Power Series of a function.

    Explanation
    ===========

    Tries to compute the formula by applying the following techniques
    (in order):

    * rational_algorithm
    * Hypergeometric algorithm

    Parameters
    ==========

    x : Symbol
    x0 : number, optional
        Point to perform series expansion about. Default is 0.
    dir : {1, -1, '+', '-'}, optional
        If dir is 1 or '+' the series is calculated from the right and
        for -1 or '-' the series is calculated from the left. For smooth
        functions this flag will not alter the results. Default is 1.
    hyper : {True, False}, optional
        Set hyper to False to skip the hypergeometric algorithm.
        By default it is set to False.
    order : int, optional
        Order of the derivative of ``f``, Default is 4.
    rational : {True, False}, optional
        Set rational to False to skip rational algorithm. By default it is set
        to True.
    full : {True, False}, optional
        Set full to True to increase the range of rational algorithm.
        See :func:`rational_algorithm` for details. By default it is set to
        False.

    Returns
    =======

    ak : sequence
        Sequence of coefficients.
    xk : sequence
        Sequence of powers of x.
    ind : Expr
        Independent terms.
    mul : Pow
        Common terms.

    See Also
    ========

    sympy.series.formal.rational_algorithm
    sympy.series.formal.hyper_algorithm
    """
    f = sympify(f)
    x = sympify(x)
    if not f.has(x):
        return None
    x0 = None(x0)
    if dir == '+':
        dir = S.One
    elif dir == '-':
        dir = -(S.One)
    elif dir not in (S.One, -(S.One)):
        raise ValueError("Dir must be '+' or '-'")
    dir = sympify(dir)
    return _compute_fps(f, x, x0, dir, hyper, order, rational, full)


class Coeff(Function):
    '''
    Coeff(p, x, n) represents the nth coefficient of the polynomial p in x
    '''
    eval = (lambda cls, p, x, n: if p.is_polynomial(x) or n.is_integer:
p.coeff(x, n)None)()


class FormalPowerSeries(SeriesBase):
    '''
    Represents Formal Power Series of a function.

    Explanation
    ===========

    No computation is performed. This class should only to be used to represent
    a series. No checks are performed.

    For computing a series use :func:`fps`.

    See Also
    ========

    sympy.series.formal.fps
    '''
    
    def __new__(cls, *args):
        args = map(sympify, args)
    # WARNING: Decompyle incomplete

    
    def __init__(self, *args):
        ak = args[4][0]
        k = ak.variables[0]
        self.ak_seq = sequence(ak.formula, (k, 1, oo))
        self.fact_seq = sequence(factorial(k), (k, 1, oo))
        self.bell_coeff_seq = self.ak_seq * self.fact_seq
        self.sign_seq = sequence((-1, 1), (k, 1, oo))

    function = (lambda self: self.args[0])()
    x = (lambda self: self.args[1])()
    x0 = (lambda self: self.args[2])()
    dir = (lambda self: self.args[3])()
    ak = (lambda self: self.args[4][0])()
    xk = (lambda self: self.args[4][1])()
    ind = (lambda self: self.args[4][2])()
    interval = (lambda self: Interval(0, oo))()
    start = (lambda self: self.interval.inf)()
    stop = (lambda self: self.interval.sup)()
    length = (lambda self: oo)()
    infinite = (lambda self: Sum = Sumimport sympy.concretexk = self.xkak = self.akk = ak.variables[0]inf_sum = Sum(ak.formula * xk.formula, (k, ak.start, ak.stop))self.ind + inf_sum)()
    
    def _get_pow_x(self, term):
        '''Returns the power of x in a term.'''
        (xterm, pow_x) = term.as_independent(self.x)[1].as_base_exp()
        if not xterm.has(self.x):
            return S.Zero

    
    def polynomial(self, n = (6,)):
        '''
        Truncated series as polynomial.

        Explanation
        ===========

        Returns series expansion of ``f`` upto order ``O(x**n)``
        as a polynomial(without ``O`` term).
        '''
        terms = []
        sym = self.free_symbols
    # WARNING: Decompyle incomplete

    
    def truncate(self, n = (6,)):
        '''
        Truncated series.

        Explanation
        ===========

        Returns truncated series expansion of f upto
        order ``O(x**n)``.

        If n is ``None``, returns an infinite iterator.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def zero_coeff(self):
        return self._eval_term(0)

    
    def _eval_term(self, pt):
        
        try:
            pt_xk = self.xk.coeff(pt)
            pt_ak = self.ak.coeff(pt).simplify()
            term = pt_ak * pt_xk
        except IndexError:
            term = S.Zero

    # WARNING: Decompyle incomplete

    
    def _eval_subs(self, old, new):
        x = self.x
        if old.has(x):
            return self

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        for t in self:
            if t is not S.Zero:
                
                return None, t
            return None

    
    def _eval_derivative(self, x):
        f = self.function.diff(x)
        ind = self.ind.diff(x)
        pow_xk = self._get_pow_x(self.xk.formula)
        ak = self.ak
        k = ak.variables[0]
    # WARNING: Decompyle incomplete

    
    def integrate(self, x = (None,), **kwargs):
        '''
        Integrate Formal Power Series.

        Examples
        ========

        >>> from sympy import fps, sin, integrate
        >>> from sympy.abc import x
        >>> f = fps(sin(x))
        >>> f.integrate(x).truncate()
        -1 + x**2/2 - x**4/24 + O(x**6)
        >>> integrate(f, (x, 0, 1))
        1 - cos(1)
        '''
        integrate = integrate
        import sympy.integrals
    # WARNING: Decompyle incomplete

    
    def product(self, other, x, n = (None, 6)):
        '''
        Multiplies two Formal Power Series, using discrete convolution and
        return the truncated terms upto specified order.

        Parameters
        ==========

        n : Number, optional
            Specifies the order of the term up to which the polynomial should
            be truncated.

        Examples
        ========

        >>> from sympy import fps, sin, exp
        >>> from sympy.abc import x
        >>> f1 = fps(sin(x))
        >>> f2 = fps(exp(x))

        >>> f1.product(f2, x).truncate(4)
        x + x**2 + x**3/3 + O(x**4)

        See Also
        ========

        sympy.discrete.convolutions
        sympy.series.formal.FormalPowerSeriesProduct

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def coeff_bell(self, n):
        '''
        self.coeff_bell(n) returns a sequence of Bell polynomials of the second kind.
        Note that ``n`` should be a integer.

        The second kind of Bell polynomials (are sometimes called "partial" Bell
        polynomials or incomplete Bell polynomials) are defined as

        .. math::
            B_{n,k}(x_1, x_2,\\dotsc x_{n-k+1}) =
                \\sum_{j_1+j_2+j_2+\\dotsb=k \\atop j_1+2j_2+3j_2+\\dotsb=n}
                \\frac{n!}{j_1!j_2!\\dotsb j_{n-k+1}!}
                \\left(\\frac{x_1}{1!} \\right)^{j_1}
                \\left(\\frac{x_2}{2!} \\right)^{j_2} \\dotsb
                \\left(\\frac{x_{n-k+1}}{(n-k+1)!} \\right) ^{j_{n-k+1}}.

        * ``bell(n, k, (x1, x2, ...))`` gives Bell polynomials of the second kind,
          `B_{n,k}(x_1, x_2, \\dotsc, x_{n-k+1})`.

        See Also
        ========

        sympy.functions.combinatorial.numbers.bell

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def compose(self, other, x, n = (None, 6)):
        '''
        Returns the truncated terms of the formal power series of the composed function,
        up to specified ``n``.

        Explanation
        ===========

        If ``f`` and ``g`` are two formal power series of two different functions,
        then the coefficient sequence ``ak`` of the composed formal power series `fp`
        will be as follows.

        .. math::
            \\sum\\limits_{k=0}^{n} b_k B_{n,k}(x_1, x_2, \\dotsc, x_{n-k+1})

        Parameters
        ==========

        n : Number, optional
            Specifies the order of the term up to which the polynomial should
            be truncated.

        Examples
        ========

        >>> from sympy import fps, sin, exp
        >>> from sympy.abc import x
        >>> f1 = fps(exp(x))
        >>> f2 = fps(sin(x))

        >>> f1.compose(f2, x).truncate()
        1 + x + x**2/2 - x**4/8 - x**5/15 + O(x**6)

        >>> f1.compose(f2, x).truncate(8)
        1 + x + x**2/2 - x**4/8 - x**5/15 - x**6/240 + x**7/90 + O(x**8)

        See Also
        ========

        sympy.functions.combinatorial.numbers.bell
        sympy.series.formal.FormalPowerSeriesCompose

        References
        ==========

        .. [1] Comtet, Louis: Advanced combinatorics; the art of finite and infinite expansions. Reidel, 1974.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def inverse(self, x, n = (None, 6)):
        '''
        Returns the truncated terms of the inverse of the formal power series,
        up to specified ``n``.

        Explanation
        ===========

        If ``f`` and ``g`` are two formal power series of two different functions,
        then the coefficient sequence ``ak`` of the composed formal power series ``fp``
        will be as follows.

        .. math::
            \\sum\\limits_{k=0}^{n} (-1)^{k} x_0^{-k-1} B_{n,k}(x_1, x_2, \\dotsc, x_{n-k+1})

        Parameters
        ==========

        n : Number, optional
            Specifies the order of the term up to which the polynomial should
            be truncated.

        Examples
        ========

        >>> from sympy import fps, exp, cos
        >>> from sympy.abc import x
        >>> f1 = fps(exp(x))
        >>> f2 = fps(cos(x))

        >>> f1.inverse(x).truncate()
        1 - x + x**2/2 - x**3/6 + x**4/24 - x**5/120 + O(x**6)

        >>> f2.inverse(x).truncate(8)
        1 + x**2/2 + 5*x**4/24 + 61*x**6/720 + O(x**8)

        See Also
        ========

        sympy.functions.combinatorial.numbers.bell
        sympy.series.formal.FormalPowerSeriesInverse

        References
        ==========

        .. [1] Comtet, Louis: Advanced combinatorics; the art of finite and infinite expansions. Reidel, 1974.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __add__(self, other):
        other = sympify(other)
    # WARNING: Decompyle incomplete

    
    def __radd__(self, other):
        return self.__add__(other)

    
    def __neg__(self):
        return self.func(-(self.function), self.x, self.x0, self.dir, (-(self.ak), self.xk, -(self.ind)))

    
    def __sub__(self, other):
        return self.__add__(-other)

    
    def __rsub__(self, other):
        return -self.__add__(other)

    
    def __mul__(self, other):
        other = sympify(other)
        if other.has(self.x):
            return Mul(self, other)
        f = None.function * other
        ak = self.ak.coeff_mul(other)
        ind = self.ind * other
        return self.func(f, self.x, self.x0, self.dir, (ak, self.xk, ind))

    
    def __rmul__(self, other):
        return self.__mul__(other)



class FiniteFormalPowerSeries(FormalPowerSeries):
    '''Base Class for Product, Compose and Inverse classes'''
    
    def __init__(self, *args):
        pass

    ffps = (lambda self: self.args[0])()
    gfps = (lambda self: self.args[1])()
    f = (lambda self: self.ffps.function)()
    g = (lambda self: self.gfps.function)()
    infinite = (lambda self: raise NotImplementedError('No infinite version for an object of FiniteFormalPowerSeries class.'))()
    
    def _eval_terms(self, n):
        raise NotImplementedError('(%s)._eval_terms()' % self)

    
    def _eval_term(self, pt):
        raise NotImplementedError('By the current logic, one can get termsupto a certain order, instead of getting term by term.')

    
    def polynomial(self, n):
        return self._eval_terms(n)

    
    def truncate(self, n = (6,)):
        ffps = self.ffps
        pt_xk = ffps.xk.coeff(n)
        x0 = ffps.x0
        x = ffps.x
        return self.polynomial(n) + Order(pt_xk, (x, x0))

    
    def _eval_derivative(self, x):
        raise NotImplementedError

    
    def integrate(self, x):
        raise NotImplementedError



class FormalPowerSeriesProduct(FiniteFormalPowerSeries):
    '''Represents the product of two formal power series of two functions.

    Explanation
    ===========

    No computation is performed. Terms are calculated using a term by term logic,
    instead of a point by point logic.

    There are two differences between a :obj:`FormalPowerSeries` object and a
    :obj:`FormalPowerSeriesProduct` object. The first argument contains the two
    functions involved in the product. Also, the coefficient sequence contains
    both the coefficient sequence of the formal power series of the involved functions.

    See Also
    ========

    sympy.series.formal.FormalPowerSeries
    sympy.series.formal.FiniteFormalPowerSeries

    '''
    
    def __init__(self, *args):
        gfps = self.gfps
        ffps = self.ffps
        k = ffps.ak.variables[0]
        self.coeff1 = sequence(ffps.ak.formula, (k, 0, oo))
        k = gfps.ak.variables[0]
        self.coeff2 = sequence(gfps.ak.formula, (k, 0, oo))

    function = (lambda self: self.f * self.g)()
    
    def _eval_terms(self, n):
        '''
        Returns the first ``n`` terms of the product formal power series.
        Term by term logic is implemented here.

        Examples
        ========

        >>> from sympy import fps, sin, exp
        >>> from sympy.abc import x
        >>> f1 = fps(sin(x))
        >>> f2 = fps(exp(x))
        >>> fprod = f1.product(f2, x)

        >>> fprod._eval_terms(4)
        x**3/3 + x**2 + x

        See Also
        ========

        sympy.series.formal.FormalPowerSeries.product

        '''
        coeff2 = self.coeff2
        coeff1 = self.coeff1
        aks = convolution(coeff1[:n], coeff2[:n])
        terms = []
    # WARNING: Decompyle incomplete



class FormalPowerSeriesCompose(FiniteFormalPowerSeries):
    '''
    Represents the composed formal power series of two functions.

    Explanation
    ===========

    No computation is performed. Terms are calculated using a term by term logic,
    instead of a point by point logic.

    There are two differences between a :obj:`FormalPowerSeries` object and a
    :obj:`FormalPowerSeriesCompose` object. The first argument contains the outer
    function and the inner function involved in the omposition. Also, the
    coefficient sequence contains the generic sequence which is to be multiplied
    by a custom ``bell_seq`` finite sequence. The finite terms will then be added up to
    get the final terms.

    See Also
    ========

    sympy.series.formal.FormalPowerSeries
    sympy.series.formal.FiniteFormalPowerSeries

    '''
    function = (lambda self: x = self.ffps.xg = self.gf = self.ff.subs(x, g))()
    
    def _eval_terms(self, n):
        '''
        Returns the first `n` terms of the composed formal power series.
        Term by term logic is implemented here.

        Explanation
        ===========

        The coefficient sequence of the :obj:`FormalPowerSeriesCompose` object is the generic sequence.
        It is multiplied by ``bell_seq`` to get a sequence, whose terms are added up to get
        the final terms for the polynomial.

        Examples
        ========

        >>> from sympy import fps, sin, exp
        >>> from sympy.abc import x
        >>> f1 = fps(exp(x))
        >>> f2 = fps(sin(x))
        >>> fcomp = f1.compose(f2, x)

        >>> fcomp._eval_terms(6)
        -x**5/15 - x**4/8 + x**2/2 + x + 1

        >>> fcomp._eval_terms(8)
        x**7/90 - x**6/240 - x**5/15 - x**4/8 + x**2/2 + x + 1

        See Also
        ========

        sympy.series.formal.FormalPowerSeries.compose
        sympy.series.formal.FormalPowerSeries.coeff_bell

        '''
        gfps = self.gfps
        ffps = self.ffps
        terms = [
            ffps.zero_coeff()]
    # WARNING: Decompyle incomplete



class FormalPowerSeriesInverse(FiniteFormalPowerSeries):
    '''
    Represents the Inverse of a formal power series.

    Explanation
    ===========

    No computation is performed. Terms are calculated using a term by term logic,
    instead of a point by point logic.

    There is a single difference between a :obj:`FormalPowerSeries` object and a
    :obj:`FormalPowerSeriesInverse` object. The coefficient sequence contains the
    generic sequence which is to be multiplied by a custom ``bell_seq`` finite sequence.
    The finite terms will then be added up to get the final terms.

    See Also
    ========

    sympy.series.formal.FormalPowerSeries
    sympy.series.formal.FiniteFormalPowerSeries

    '''
    
    def __init__(self, *args):
        ffps = self.ffps
        k = ffps.xk.variables[0]
        inv = ffps.zero_coeff()
        inv_seq = sequence(inv ** (-(k + 1)), (k, 1, oo))
        self.aux_seq = ffps.sign_seq * ffps.fact_seq * inv_seq

    function = (lambda self: f = self.f1 / f)()
    g = (lambda self: raise ValueError('Only one function is considered while performinginverse of a formal power series.'))()
    gfps = (lambda self: raise ValueError('Only one function is considered while performinginverse of a formal power series.'))()
    
    def _eval_terms(self, n):
        '''
        Returns the first ``n`` terms of the composed formal power series.
        Term by term logic is implemented here.

        Explanation
        ===========

        The coefficient sequence of the `FormalPowerSeriesInverse` object is the generic sequence.
        It is multiplied by ``bell_seq`` to get a sequence, whose terms are added up to get
        the final terms for the polynomial.

        Examples
        ========

        >>> from sympy import fps, exp, cos
        >>> from sympy.abc import x
        >>> f1 = fps(exp(x))
        >>> f2 = fps(cos(x))
        >>> finv1, finv2 = f1.inverse(), f2.inverse()

        >>> finv1._eval_terms(6)
        -x**5/120 + x**4/24 - x**3/6 + x**2/2 - x + 1

        >>> finv2._eval_terms(8)
        61*x**6/720 + 5*x**4/24 + x**2/2 + 1

        See Also
        ========

        sympy.series.formal.FormalPowerSeries.inverse
        sympy.series.formal.FormalPowerSeries.coeff_bell

        '''
        ffps = self.ffps
        terms = [
            ffps.zero_coeff()]
    # WARNING: Decompyle incomplete



def fps(f, x, x0, dir, hyper, order, rational, full = (None, 0, 1, True, 4, True, False)):
    """
    Generates Formal Power Series of ``f``.

    Explanation
    ===========

    Returns the formal series expansion of ``f`` around ``x = x0``
    with respect to ``x`` in the form of a ``FormalPowerSeries`` object.

    Formal Power Series is represented using an explicit formula
    computed using different algorithms.

    See :func:`compute_fps` for the more details regarding the computation
    of formula.

    Parameters
    ==========

    x : Symbol, optional
        If x is None and ``f`` is univariate, the univariate symbols will be
        supplied, otherwise an error will be raised.
    x0 : number, optional
        Point to perform series expansion about. Default is 0.
    dir : {1, -1, '+', '-'}, optional
        If dir is 1 or '+' the series is calculated from the right and
        for -1 or '-' the series is calculated from the left. For smooth
        functions this flag will not alter the results. Default is 1.
    hyper : {True, False}, optional
        Set hyper to False to skip the hypergeometric algorithm.
        By default it is set to False.
    order : int, optional
        Order of the derivative of ``f``, Default is 4.
    rational : {True, False}, optional
        Set rational to False to skip rational algorithm. By default it is set
        to True.
    full : {True, False}, optional
        Set full to True to increase the range of rational algorithm.
        See :func:`rational_algorithm` for details. By default it is set to
        False.

    Examples
    ========

    >>> from sympy import fps, ln, atan, sin
    >>> from sympy.abc import x, n

    Rational Functions

    >>> fps(ln(1 + x)).truncate()
    x - x**2/2 + x**3/3 - x**4/4 + x**5/5 + O(x**6)

    >>> fps(atan(x), full=True).truncate()
    x - x**3/3 + x**5/5 + O(x**6)

    Symbolic Functions

    >>> fps(x**n*sin(x**2), x).truncate(8)
    -x**(n + 6)/6 + x**(n + 2) + O(x**(n + 8))

    See Also
    ========

    sympy.series.formal.FormalPowerSeries
    sympy.series.formal.compute_fps
    """
    f = sympify(f)
# WARNING: Decompyle incomplete
