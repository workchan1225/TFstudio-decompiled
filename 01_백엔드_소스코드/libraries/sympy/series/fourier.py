# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fourier.pyc (Python 3.11)

'''Fourier Series'''
from sympy.core.numbers import oo, pi
from sympy.core.symbol import Wild
from sympy.core.expr import Expr
from sympy.core.add import Add
from sympy.core.containers import Tuple
from sympy.core.singleton import S
from sympy.core.symbol import Dummy, Symbol
from sympy.core.sympify import sympify
from sympy.functions.elementary.trigonometric import sin, cos, sinc
from sympy.series.series_class import SeriesBase
from sympy.series.sequences import SeqFormula
from sympy.sets.sets import Interval
from sympy.utilities.iterables import is_sequence
__doctest_requires__ = {
    ('fourier_series',): [
        'matplotlib'] }

def fourier_cos_seq(func, limits, n):
    '''Returns the cos sequence in a Fourier series'''
    integrate = integrate
    import sympy.integrals
    L = limits[2] - limits[1]
    x = limits[0]
    cos_term = cos(2 * n * pi * x / L)
    formula = 2 * cos_term * integrate(func * cos_term, limits) / L
    a0 = formula.subs(n, S.Zero) / 2
    return (a0, SeqFormula(2 * cos_term * integrate(func * cos_term, limits) / L, (n, 1, oo)))


def fourier_sin_seq(func, limits, n):
    '''Returns the sin sequence in a Fourier series'''
    integrate = integrate
    import sympy.integrals
    L = limits[2] - limits[1]
    x = limits[0]
    sin_term = sin(2 * n * pi * x / L)
    return SeqFormula(2 * sin_term * integrate(func * sin_term, limits) / L, (n, 1, oo))


def _process_limits(func, limits):
    '''
    Limits should be of the form (x, start, stop).
    x should be a symbol. Both start and stop should be bounded.

    Explanation
    ===========

    * If x is not given, x is determined from func.
    * If limits is None. Limit of the form (x, -pi, pi) is returned.

    Examples
    ========

    >>> from sympy.series.fourier import _process_limits as pari
    >>> from sympy.abc import x
    >>> pari(x**2, (x, -2, 2))
    (x, -2, 2)
    >>> pari(x**2, (-2, 2))
    (x, -2, 2)
    >>> pari(x**2, None)
    (x, -pi, pi)
    '''
    
    def _find_x(func):
        free = func.free_symbols
        if len(free) == 1:
            return free.pop()
        if not None:
            return Dummy('k')
        raise None(' specify dummy variables for %s. If the function contains more than one free symbol, a dummy variable should be supplied explicitly e.g. FourierSeries(m*n**2, (n, -pi, pi))' % func)

    (x, start, stop) = (None, None, None)
# WARNING: Decompyle incomplete


def finite_check(f, x, L):
    pass
# WARNING: Decompyle incomplete


class FourierSeries(SeriesBase):
    '''Represents Fourier sine/cosine series.

    Explanation
    ===========

    This class only represents a fourier series.
    No computation is performed.

    For how to compute Fourier series, see the :func:`fourier_series`
    docstring.

    See Also
    ========

    sympy.series.fourier.fourier_series
    '''
    
    def __new__(cls, *args):
        args = map(sympify, args)
    # WARNING: Decompyle incomplete

    function = (lambda self: self.args[0])()
    x = (lambda self: self.args[1][0])()
    period = (lambda self: (self.args[1][1], self.args[1][2]))()
    a0 = (lambda self: self.args[2][0])()
    an = (lambda self: self.args[2][1])()
    bn = (lambda self: self.args[2][2])()
    interval = (lambda self: Interval(0, oo))()
    start = (lambda self: self.interval.inf)()
    stop = (lambda self: self.interval.sup)()
    length = (lambda self: oo)()
    L = (lambda self: abs(self.period[1] - self.period[0]) / 2)()
    
    def _eval_subs(self, old, new):
        x = self.x
        if old.has(x):
            return self

    
    def truncate(self, n = (3,)):
        '''
        Return the first n nonzero terms of the series.

        If ``n`` is None return an iterator.

        Parameters
        ==========

        n : int or None
            Amount of non-zero terms in approximation or None.

        Returns
        =======

        Expr or iterator :
            Approximation of function expanded into Fourier series.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x, (x, -pi, pi))
        >>> s.truncate(4)
        2*sin(x) - sin(2*x) + 2*sin(3*x)/3 - sin(4*x)/2

        See Also
        ========

        sympy.series.fourier.FourierSeries.sigma_approximation
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def sigma_approximation(self, n = (3,)):
        '''
        Return :math:`\\sigma`-approximation of Fourier series with respect
        to order n.

        Explanation
        ===========

        Sigma approximation adjusts a Fourier summation to eliminate the Gibbs
        phenomenon which would otherwise occur at discontinuities.
        A sigma-approximated summation for a Fourier series of a T-periodical
        function can be written as

        .. math::
            s(\\theta) = \\frac{1}{2} a_0 + \\sum _{k=1}^{m-1}
            \\operatorname{sinc} \\Bigl( \\frac{k}{m} \\Bigr) \\cdot
            \\left[ a_k \\cos \\Bigl( \\frac{2\\pi k}{T} \\theta \\Bigr)
            + b_k \\sin \\Bigl( \\frac{2\\pi k}{T} \\theta \\Bigr) \\right],

        where :math:`a_0, a_k, b_k, k=1,\\ldots,{m-1}` are standard Fourier
        series coefficients and
        :math:`\\operatorname{sinc} \\Bigl( \\frac{k}{m} \\Bigr)` is a Lanczos
        :math:`\\sigma` factor (expressed in terms of normalized
        :math:`\\operatorname{sinc}` function).

        Parameters
        ==========

        n : int
            Highest order of the terms taken into account in approximation.

        Returns
        =======

        Expr :
            Sigma approximation of function expanded into Fourier series.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x, (x, -pi, pi))
        >>> s.sigma_approximation(4)
        2*sin(x)*sinc(pi/4) - 2*sin(2*x)/pi + 2*sin(3*x)*sinc(3*pi/4)/3

        See Also
        ========

        sympy.series.fourier.FourierSeries.truncate

        Notes
        =====

        The behaviour of
        :meth:`~sympy.series.fourier.FourierSeries.sigma_approximation`
        is different from :meth:`~sympy.series.fourier.FourierSeries.truncate`
        - it takes all nonzero terms of degree smaller than n, rather than
        first n nonzero ones.

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Gibbs_phenomenon
        .. [2] https://en.wikipedia.org/wiki/Sigma_approximation
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def shift(self, s):
        '''
        Shift the function by a term independent of x.

        Explanation
        ===========

        f(x) -> f(x) + s

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.shift(1).truncate()
        -4*cos(x) + cos(2*x) + 1 + pi**2/3
        '''
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        a0 = self.a0 + s
        sfunc = self.function + s
        return self.func(sfunc, self.args[1], (a0, self.an, self.bn))

    
    def shiftx(self, s):
        '''
        Shift x by a term independent of x.

        Explanation
        ===========

        f(x) -> f(x + s)

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.shiftx(1).truncate()
        -4*cos(x + 1) + cos(2*x + 2) + pi**2/3
        '''
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        an = self.an.subs(x, x + s)
        bn = self.bn.subs(x, x + s)
        sfunc = self.function.subs(x, x + s)
        return self.func(sfunc, self.args[1], (self.a0, an, bn))

    
    def scale(self, s):
        '''
        Scale the function by a term independent of x.

        Explanation
        ===========

        f(x) -> s * f(x)

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.scale(2).truncate()
        -8*cos(x) + 2*cos(2*x) + 2*pi**2/3
        '''
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        an = self.an.coeff_mul(s)
        bn = self.bn.coeff_mul(s)
        a0 = self.a0 * s
        sfunc = self.args[0] * s
        return self.func(sfunc, self.args[1], (a0, an, bn))

    
    def scalex(self, s):
        '''
        Scale x by a term independent of x.

        Explanation
        ===========

        f(x) -> f(s*x)

        This is fast, if Fourier series of f(x) is already
        computed.

        Examples
        ========

        >>> from sympy import fourier_series, pi
        >>> from sympy.abc import x
        >>> s = fourier_series(x**2, (x, -pi, pi))
        >>> s.scalex(2).truncate()
        -4*cos(2*x) + cos(4*x) + pi**2/3
        '''
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        an = self.an.subs(x, x * s)
        bn = self.bn.subs(x, x * s)
        sfunc = self.function.subs(x, x * s)
        return self.func(sfunc, self.args[1], (self.a0, an, bn))

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        for t in self:
            if t is not S.Zero:
                
                return None, t
            return None

    
    def _eval_term(self, pt):
        if pt == 0:
            return self.a0
        return None.an.coeff(pt) + self.bn.coeff(pt)

    
    def __neg__(self):
        return self.scale(-1)

    
    def __add__(self, other):
        if isinstance(other, FourierSeries):
            if self.period != other.period:
                raise ValueError('Both the series should have same periods')
            y = other.x
            x = self.x
            function = self.function + other.function.subs(y, x)
            if self.x not in function.free_symbols:
                return function
            an = None.an + other.an
            bn = self.bn + other.bn
            a0 = self.a0 + other.a0
            return self.func(function, self.args[1], (a0, an, bn))
        return None(self, other)

    
    def __sub__(self, other):
        return self.__add__(-other)



class FiniteFourierSeries(FourierSeries):
    '''Represents Finite Fourier sine/cosine series.

    For how to compute Fourier series, see the :func:`fourier_series`
    docstring.

    Parameters
    ==========

    f : Expr
        Expression for finding fourier_series

    limits : ( x, start, stop)
        x is the independent variable for the expression f
        (start, stop) is the period of the fourier series

    exprs: (a0, an, bn) or Expr
        a0 is the constant term a0 of the fourier series
        an is a dictionary of coefficients of cos terms
         an[k] = coefficient of cos(pi*(k/L)*x)
        bn is a dictionary of coefficients of sin terms
         bn[k] = coefficient of sin(pi*(k/L)*x)

        or exprs can be an expression to be converted to fourier form

    Methods
    =======

    This class is an extension of FourierSeries class.
    Please refer to sympy.series.fourier.FourierSeries for
    further information.

    See Also
    ========

    sympy.series.fourier.FourierSeries
    sympy.series.fourier.fourier_series
    '''
    
    def __new__(cls, f, limits, exprs):
        pass
    # WARNING: Decompyle incomplete

    interval = (lambda self: _length = 1 if self.a0 else 0_length += max(set(self.an.keys()).union(set(self.bn.keys()))) + 1Interval(0, _length))()
    length = (lambda self: self.stop - self.start)()
    
    def shiftx(self, s):
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        _expr = self.truncate().subs(x, x + s)
        sfunc = self.function.subs(x, x + s)
        return self.func(sfunc, self.args[1], _expr)

    
    def scale(self, s):
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        _expr = self.truncate() * s
        sfunc = self.function * s
        return self.func(sfunc, self.args[1], _expr)

    
    def scalex(self, s):
        x = self.x
        s = sympify(s)
        if x in s.free_symbols:
            raise ValueError(f'''\'{s!s}\' should be independent of {x!s}''')
        _expr = self.truncate().subs(x, x * s)
        sfunc = self.function.subs(x, x * s)
        return self.func(sfunc, self.args[1], _expr)

    
    def _eval_term(self, pt):
        if pt == 0:
            return self.a0
        _term = None.an.get(pt, S.Zero) * cos(pt * (pi / self.L) * self.x) + self.bn.get(pt, S.Zero) * sin(pt * (pi / self.L) * self.x)
        return _term

    
    def __add__(self, other):
        if isinstance(other, FourierSeries):
            return other.__add__(fourier_series(self.function, self.args[1], finite = False))
        if None(other, FiniteFourierSeries):
            if self.period != other.period:
                raise ValueError('Both the series should have same periods')
            y = other.x
            x = self.x
            function = self.function + other.function.subs(y, x)
            if self.x not in function.free_symbols:
                return function
            return None(function, limits = self.args[1])



def fourier_series(f, limits, finite = (None, True)):
