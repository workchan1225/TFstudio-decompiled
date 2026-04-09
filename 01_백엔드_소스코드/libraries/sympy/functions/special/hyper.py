# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hyper.pyc (Python 3.11)

'''Hypergeometric and Meijer G-functions'''
from collections import Counter
from sympy.core import S, Mod
from sympy.core.add import Add
from sympy.core.expr import Expr
from sympy.core.function import Function, Derivative, ArgumentIndexError
from sympy.core.containers import Tuple
from sympy.core.mul import Mul
from sympy.core.numbers import I, pi, oo, zoo
from sympy.core.parameters import global_parameters
from sympy.core.relational import Ne
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Dummy
from sympy.external.gmpy import lcm
from sympy.functions import sqrt, exp, log, sin, cos, asin, atan, sinh, cosh, asinh, acosh, atanh, acoth
from sympy.functions import factorial, RisingFactorial
from sympy.functions.elementary.complexes import Abs, re, unpolarify
from sympy.functions.elementary.exponential import exp_polar
from sympy.functions.elementary.integers import ceiling
from sympy.functions.elementary.piecewise import Piecewise
from sympy.logic.boolalg import And, Or
from sympy import ordered

class TupleArg(Tuple):
    
    def as_leading_term(self = None, *, logx, cdir, *x):
        pass
    # WARNING: Decompyle incomplete

    
    def limit(self, x, xlim, dir = ('+',)):
        ''' Compute limit x->xlim.
        '''
        pass
    # WARNING: Decompyle incomplete



def _prep_tuple(v):
    '''
    Turn an iterable argument *v* into a tuple and unpolarify, since both
    hypergeometric and meijer g-functions are unbranched in their parameters.

    Examples
    ========

    >>> from sympy.functions.special.hyper import _prep_tuple
    >>> _prep_tuple([1, 2, 3])
    (1, 2, 3)
    >>> _prep_tuple((4, 5))
    (4, 5)
    >>> _prep_tuple((7, 8, 9))
    (7, 8, 9)

    '''
    pass
# WARNING: Decompyle incomplete


class TupleParametersBase(Function):
    ''' Base class that takes care of differentiation, when some of
        the arguments are actually tuples. '''
    is_commutative = True
    
    def _eval_derivative(self, s):
        
        try:
            res = 0
            if self.args[0].has(s) or self.args[1].has(s):
                for i, p in enumerate(self._diffargs):
                    m = self._diffargs[i].diff(s)
                    if m != 0:
                        res += self.fdiff((1, i)) * m
                    return res + self.fdiff(3) * self.args[2].diff(s)
                    except (ArgumentIndexError, NotImplementedError):
                        return 




class hyper(TupleParametersBase):
    pass
# WARNING: Decompyle incomplete


class meijerg(TupleParametersBase):
    '''
    The Meijer G-function is defined by a Mellin-Barnes type integral that
    resembles an inverse Mellin transform. It generalizes the hypergeometric
    functions.

    Explanation
    ===========

    The Meijer G-function depends on four sets of parameters. There are
    "*numerator parameters*"
    $a_1, \\ldots, a_n$ and $a_{n+1}, \\ldots, a_p$, and there are
    "*denominator parameters*"
    $b_1, \\ldots, b_m$ and $b_{m+1}, \\ldots, b_q$.
    Confusingly, it is traditionally denoted as follows (note the position
    of $m$, $n$, $p$, $q$, and how they relate to the lengths of the four
    parameter vectors):

    .. math ::
        G_{p,q}^{m,n} \\left(\\begin{matrix}a_1, \\cdots, a_n & a_{n+1}, \\cdots, a_p \\\\
                                        b_1, \\cdots, b_m & b_{m+1}, \\cdots, b_q
                          \\end{matrix} \\middle| z \\right).

    However, in SymPy the four parameter vectors are always available
    separately (see examples), so that there is no need to keep track of the
    decorating sub- and super-scripts on the G symbol.

    The G function is defined as the following integral:

    .. math ::
         \\frac{1}{2 \\pi i} \\int_L \\frac{\\prod_{j=1}^m \\Gamma(b_j - s)
         \\prod_{j=1}^n \\Gamma(1 - a_j + s)}{\\prod_{j=m+1}^q \\Gamma(1- b_j +s)
         \\prod_{j=n+1}^p \\Gamma(a_j - s)} z^s \\mathrm{d}s,

    where $\\Gamma(z)$ is the gamma function. There are three possible
    contours which we will not describe in detail here (see the references).
    If the integral converges along more than one of them, the definitions
    agree. The contours all separate the poles of $\\Gamma(1-a_j+s)$
    from the poles of $\\Gamma(b_k-s)$, so in particular the G function
    is undefined if $a_j - b_k \\in \\mathbb{Z}_{>0}$ for some
    $j \\le n$ and $k \\le m$.

    The conditions under which one of the contours yields a convergent integral
    are complicated and we do not state them here, see the references.

    Please note currently the Meijer G-function constructor does *not* check any
    convergence conditions.

    Examples
    ========

    You can pass the parameters either as four separate vectors:

    >>> from sympy import meijerg, Tuple, pprint
    >>> from sympy.abc import x, a
    >>> pprint(meijerg((1, 2), (a, 4), (5,), [], x), use_unicode=False)
     __1, 2 /1, 2  4, a |  \\
    /__     |           | x|
    \\_|4, 1 \\ 5         |  /

    Or as two nested vectors:

    >>> pprint(meijerg([(1, 2), (3, 4)], ([5], Tuple()), x), use_unicode=False)
     __1, 2 /1, 2  3, 4 |  \\
    /__     |           | x|
    \\_|4, 1 \\ 5         |  /

    As with the hypergeometric function, the parameters may be passed as
    arbitrary iterables. Vectors of length zero and one also have to be
    passed as iterables. The parameters need not be constants, but if they
    depend on the argument then not much implemented functionality should be
    expected.

    All the subvectors of parameters are available:

    >>> from sympy import pprint
    >>> g = meijerg([1], [2], [3], [4], x)
    >>> pprint(g, use_unicode=False)
     __1, 1 /1  2 |  \\
    /__     |     | x|
    \\_|2, 2 \\3  4 |  /
    >>> g.an
    (1,)
    >>> g.ap
    (1, 2)
    >>> g.aother
    (2,)
    >>> g.bm
    (3,)
    >>> g.bq
    (3, 4)
    >>> g.bother
    (4,)

    The Meijer G-function generalizes the hypergeometric functions.
    In some cases it can be expressed in terms of hypergeometric functions,
    using Slater\'s theorem. For example:

    >>> from sympy import hyperexpand
    >>> from sympy.abc import a, b, c
    >>> hyperexpand(meijerg([a], [], [c], [b], x), allow_hyper=True)
    x**c*gamma(-a + c + 1)*hyper((-a + c + 1,),
                                 (-b + c + 1,), -x)/gamma(-b + c + 1)

    Thus the Meijer G-function also subsumes many named functions as special
    cases. You can use ``expand_func()`` or ``hyperexpand()`` to (try to)
    rewrite a Meijer G-function in terms of named special functions. For
    example:

    >>> from sympy import expand_func, S
    >>> expand_func(meijerg([[],[]], [[0],[]], -x))
    exp(x)
    >>> hyperexpand(meijerg([[],[]], [[S(1)/2],[0]], (x/2)**2))
    sin(x)/sqrt(pi)

    See Also
    ========

    hyper
    sympy.simplify.hyperexpand

    References
    ==========

    .. [1] Luke, Y. L. (1969), The Special Functions and Their Approximations,
           Volume 1
    .. [2] https://en.wikipedia.org/wiki/Meijer_G-function

    '''
    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def fdiff(self, argindex = (3,)):
        if argindex != 3:
            return self._diff_wrt_parameter(argindex[1])
        if None(self.an) >= 1:
            a = list(self.an)
            meijerg(a, self.aother, self.bm, self.bother, self.argument) = None
            return (1 / self.argument) * ((self.an[0] - 1) * self + G)
        if None(self.bm) >= 1:
            b = list(self.bm)
            meijerg(self.an, self.aother, b, self.bother, self.argument) = None
            return (1 / self.argument) * (self.bm[0] * self - G)
        return None.Zero

    
    def _diff_wrt_parameter(self, idx):
        an = list(self.an)
        ap = list(self.aother)
        bm = list(self.bm)
        bq = list(self.bother)
        if idx < len(an):
            an.pop(idx)
        else:
            idx -= len(an)
            if idx < len(ap):
                ap.pop(idx)
            else:
                idx -= len(ap)
                if idx < len(bm):
                    bm.pop(idx)
                else:
                    bq.pop(idx - len(bm))
        pairs1 = []
        pairs2 = []
    # WARNING: Decompyle incomplete

    
    def get_period(self):
        '''
        Return a number $P$ such that $G(x*exp(I*P)) == G(x)$.

        Examples
        ========

        >>> from sympy import meijerg, pi, S
        >>> from sympy.abc import z

        >>> meijerg([1], [], [], [], z).get_period()
        2*pi
        >>> meijerg([pi], [], [], [], z).get_period()
        oo
        >>> meijerg([1, 2], [], [], [], z).get_period()
        oo
        >>> meijerg([1,1], [2], [1, S(1)/2, S(1)/3], [1], z).get_period()
        12*pi

        '''
        
        def compute(l):
            pass
        # WARNING: Decompyle incomplete

        beta = compute(self.bm)
        alpha = compute(self.an)
        q = len(self.bq)
        p = len(self.ap)
        if p == q:
            if oo in (alpha, beta):
                return oo
            return None * pi * lcm(alpha, beta)
        if None < q:
            return 2 * pi * beta
        return None * pi * alpha

    
    def _eval_expand_func(self, **hints):
        hyperexpand = hyperexpand
        import sympy.simplify.hyperexpand
        return hyperexpand(self)

    
    def _eval_evalf(self, prec):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_as_leading_term(self, x, logx, cdir = (None, 0)):
        hyperexpand = hyperexpand
        import sympy.simplify.hyperexpand
        return hyperexpand(self).as_leading_term(x, logx = logx, cdir = cdir)

    
    def integrand(self, s):
        ''' Get the defining integrand D(s). '''
        pass
    # WARNING: Decompyle incomplete

    argument = (lambda self: self.args[2])()
    an = (lambda self: pass# WARNING: Decompyle incomplete
)()
    ap = (lambda self: pass# WARNING: Decompyle incomplete
)()
    aother = (lambda self: pass# WARNING: Decompyle incomplete
)()
    bm = (lambda self: pass# WARNING: Decompyle incomplete
)()
    bq = (lambda self: pass# WARNING: Decompyle incomplete
)()
    bother = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _diffargs = (lambda self: self.ap + self.bq)()
    nu = (lambda self: sum(self.bq) - sum(self.ap))()
    delta = (lambda self: len(self.bm) + len(self.an) - S(len(self.ap) + len(self.bq)) / 2)()
    is_number = (lambda self: not (self.free_symbols))()


class HyperRep(Function):
    '''
    A base class for "hyper representation functions".

    This is used exclusively in ``hyperexpand()``, but fits more logically here.

    pFq is branched at 1 if p == q+1. For use with slater-expansion, we want
    define an "analytic continuation" to all polar numbers, which is
    continuous on circles and on the ray t*exp_polar(I*pi). Moreover, we want
    a "nice" expression for the various cases.

    This base class contains the core logic, concrete derived classes only
    supply the actual functions.

    '''
    eval = (lambda cls: newargs = tuple(map(unpolarify, args[:-1])) + args[-1:]# WARNING: Decompyle incomplete
)()
    _expr_small = (lambda cls, x: raise NotImplementedError)()
    _expr_small_minus = (lambda cls, x: raise NotImplementedError)()
    _expr_big = (lambda cls, x, n: raise NotImplementedError)()
    _expr_big_minus = (lambda cls, x, n: raise NotImplementedError)()
    
    def _eval_rewrite_as_nonrep(self, *args, **kwargs):
        (x, n) = self.args[-1].extract_branch_factor(allow_half = True)
        minus = False
        newargs = self.args[:-1] + (x,)
        if not n.is_Integer:
            minus = True
            n -= S.Half
        newerargs = newargs + (n,)
    # WARNING: Decompyle incomplete

    
    def _eval_rewrite_as_nonrepsmall(self, *args, **kwargs):
        (x, n) = self.args[-1].extract_branch_factor(allow_half = True)
        args = self.args[:-1] + (x,)
    # WARNING: Decompyle incomplete



class HyperRep_power1(HyperRep):
    ''' Return a representative for hyper([-a], [], z) == (1 - z)**a. '''
    _expr_small = (lambda cls, a, x: (1 - x) ** a)()
    _expr_small_minus = (lambda cls, a, x: (1 + x) ** a)()
    _expr_big = (lambda cls, a, x, n: if a.is_integer:
cls._expr_small(a, x)(None - 1) ** a * exp((2 * n - 1) * pi * I * a))()
    _expr_big_minus = (lambda cls, a, x, n: if a.is_integer:
cls._expr_small_minus(a, x)(None + x) ** a * exp(2 * n * pi * I * a))()


class HyperRep_power2(HyperRep):
    ''' Return a representative for hyper([a, a - 1/2], [2*a], z). '''
    _expr_small = (lambda cls, a, x: 2 ** (2 * a - 1) * (1 + sqrt(1 - x)) ** (1 - 2 * a))()
    _expr_small_minus = (lambda cls, a, x: 2 ** (2 * a - 1) * (1 + sqrt(1 + x)) ** (1 - 2 * a))()
    _expr_big = (lambda cls, a, x, n: sgn = -1if n.is_odd:
sgn = 1n -= 12 ** (2 * a - 1) * (1 + sgn * I * sqrt(x - 1)) ** (1 - 2 * a) * exp(-2 * n * pi * I * a))()
    _expr_big_minus = (lambda cls, a, x, n: sgn = 1if n.is_odd:
sgn = -1sgn * 2 ** (2 * a - 1) * (sqrt(1 + x) + sgn) ** (1 - 2 * a) * exp(-2 * pi * I * a * n))()


class HyperRep_log1(HyperRep):
    ''' Represent -z*hyper([1, 1], [2], z) == log(1 - z). '''
    _expr_small = (lambda cls, x: log(1 - x))()
    _expr_small_minus = (lambda cls, x: log(1 + x))()
    _expr_big = (lambda cls, x, n: log(x - 1) + (2 * n - 1) * pi * I)()
    _expr_big_minus = (lambda cls, x, n: log(1 + x) + 2 * n * pi * I)()


class HyperRep_atanh(HyperRep):
    ''' Represent hyper([1/2, 1], [3/2], z) == atanh(sqrt(z))/sqrt(z). '''
    _expr_small = (lambda cls, x: atanh(sqrt(x)) / sqrt(x))()
    
    def _expr_small_minus(cls, x):
        return atan(sqrt(x)) / sqrt(x)

    
    def _expr_big(cls, x, n):
        if n.is_even:
            return (acoth(sqrt(x)) + I * pi / 2) / sqrt(x)
        return (None(sqrt(x)) - I * pi / 2) / sqrt(x)

    
    def _expr_big_minus(cls, x, n):
        if n.is_even:
            return atan(sqrt(x)) / sqrt(x)
        return (None(sqrt(x)) - pi) / sqrt(x)



class HyperRep_asin1(HyperRep):
    ''' Represent hyper([1/2, 1/2], [3/2], z) == asin(sqrt(z))/sqrt(z). '''
    _expr_small = (lambda cls, z: asin(sqrt(z)) / sqrt(z))()
    _expr_small_minus = (lambda cls, z: asinh(sqrt(z)) / sqrt(z))()
    _expr_big = (lambda cls, z, n: S.NegativeOne ** n * ((S.Half - n) * pi / sqrt(z) + I * acosh(sqrt(z)) / sqrt(z)))()
    _expr_big_minus = (lambda cls, z, n: S.NegativeOne ** n * (asinh(sqrt(z)) / sqrt(z) + n * pi * I / sqrt(z)))()


class HyperRep_asin2(HyperRep):
    ''' Represent hyper([1, 1], [3/2], z) == asin(sqrt(z))/sqrt(z)/sqrt(1-z). '''
    _expr_small = (lambda cls, z: HyperRep_asin1._expr_small(z) / HyperRep_power1._expr_small(S.Half, z))()
    _expr_small_minus = (lambda cls, z: HyperRep_asin1._expr_small_minus(z) / HyperRep_power1._expr_small_minus(S.Half, z))()
    _expr_big = (lambda cls, z, n: HyperRep_asin1._expr_big(z, n) / HyperRep_power1._expr_big(S.Half, z, n))()
    _expr_big_minus = (lambda cls, z, n: HyperRep_asin1._expr_big_minus(z, n) / HyperRep_power1._expr_big_minus(S.Half, z, n))()


class HyperRep_sqrts1(HyperRep):
    ''' Return a representative for hyper([-a, 1/2 - a], [1/2], z). '''
    _expr_small = (lambda cls, a, z: ((1 - sqrt(z)) ** (2 * a) + (1 + sqrt(z)) ** (2 * a)) / 2)()
    _expr_small_minus = (lambda cls, a, z: (1 + z) ** a * cos(2 * a * atan(sqrt(z))))()
    _expr_big = (lambda cls, a, z, n: if n.is_even:
((sqrt(z) + 1) ** (2 * a) * exp(2 * pi * I * n * a) + (sqrt(z) - 1) ** (2 * a) * exp(2 * pi * I * (n - 1) * a)) / 2None -= 1((sqrt(z) - 1) ** (2 * a) * exp(2 * pi * I * a * (n + 1)) + (sqrt(z) + 1) ** (2 * a) * exp(2 * pi * I * a * n)) / 2)()
    _expr_big_minus = (lambda cls, a, z, n: if n.is_even:
(1 + z) ** a * exp(2 * pi * I * n * a) * cos(2 * a * atan(sqrt(z)))(None + z) ** a * exp(2 * pi * I * n * a) * cos(2 * a * atan(sqrt(z)) - 2 * pi * a))()


class HyperRep_sqrts2(HyperRep):
    ''' Return a representative for
          sqrt(z)/2*[(1-sqrt(z))**2a - (1 + sqrt(z))**2a]
          == -2*z/(2*a+1) d/dz hyper([-a - 1/2, -a], [1/2], z)'''
    _expr_small = (lambda cls, a, z: sqrt(z) * ((1 - sqrt(z)) ** (2 * a) - (1 + sqrt(z)) ** (2 * a)) / 2)()
    _expr_small_minus = (lambda cls, a, z: sqrt(z) * (1 + z) ** a * sin(2 * a * atan(sqrt(z))))()
    _expr_big = (lambda cls, a, z, n: if n.is_even:
(sqrt(z) / 2) * ((sqrt(z) - 1) ** (2 * a) * exp(2 * pi * I * a * (n - 1)) - (sqrt(z) + 1) ** (2 * a) * exp(2 * pi * I * a * n))None -= 1(sqrt(z) / 2) * ((sqrt(z) - 1) ** (2 * a) * exp(2 * pi * I * a * (n + 1)) - (sqrt(z) + 1) ** (2 * a) * exp(2 * pi * I * a * n)))()
    
    def _expr_big_minus(cls, a, z, n):
        if n.is_even:
            return (1 + z) ** a * exp(2 * pi * I * n * a) * sqrt(z) * sin(2 * a * atan(sqrt(z)))
        return (None + z) ** a * exp(2 * pi * I * n * a) * sqrt(z) * sin(2 * a * atan(sqrt(z)) - 2 * pi * a)



class HyperRep_log2(HyperRep):
    ''' Represent log(1/2 + sqrt(1 - z)/2) == -z/4*hyper([3/2, 1, 1], [2, 2], z) '''
    _expr_small = (lambda cls, z: log(S.Half + sqrt(1 - z) / 2))()
    _expr_small_minus = (lambda cls, z: log(S.Half + sqrt(1 + z) / 2))()
    _expr_big = (lambda cls, z, n: if n.is_even:
(n - S.Half) * pi * I + log(sqrt(z) / 2) + I * asin(1 / sqrt(z))(None - S.Half) * pi * I + log(sqrt(z) / 2) - I * asin(1 / sqrt(z)))()
    
    def _expr_big_minus(cls, z, n):
        if n.is_even:
            return pi * I * n + log(S.Half + sqrt(1 + z) / 2)
        return None * I * n + log(sqrt(1 + z) / 2 - S.Half)



class HyperRep_cosasin(HyperRep):
    ''' Represent hyper([a, -a], [1/2], z) == cos(2*a*asin(sqrt(z))). '''
    _expr_small = (lambda cls, a, z: cos(2 * a * asin(sqrt(z))))()
    _expr_small_minus = (lambda cls, a, z: cosh(2 * a * asinh(sqrt(z))))()
    _expr_big = (lambda cls, a, z, n: cosh(2 * a * acosh(sqrt(z)) + a * pi * I * (2 * n - 1)))()
    _expr_big_minus = (lambda cls, a, z, n: cosh(2 * a * asinh(sqrt(z)) + 2 * a * pi * I * n))()


class HyperRep_sinasin(HyperRep):
    ''' Represent 2*a*z*hyper([1 - a, 1 + a], [3/2], z)
        == sqrt(z)/sqrt(1-z)*sin(2*a*asin(sqrt(z))) '''
    _expr_small = (lambda cls, a, z: (sqrt(z) / sqrt(1 - z)) * sin(2 * a * asin(sqrt(z))))()
    _expr_small_minus = (lambda cls, a, z: (-sqrt(z) / sqrt(1 + z)) * sinh(2 * a * asinh(sqrt(z))))()
    _expr_big = (lambda cls, a, z, n: (-1 / sqrt(1 - 1 / z)) * sinh(2 * a * acosh(sqrt(z)) + a * pi * I * (2 * n - 1)))()
    _expr_big_minus = (lambda cls, a, z, n: (-1 / sqrt(1 + 1 / z)) * sinh(2 * a * asinh(sqrt(z)) + 2 * a * pi * I * n))()


class appellf1(Function):
    """
    This is the Appell hypergeometric function of two variables as:

    .. math ::
        F_1(a,b_1,b_2,c,x,y) = \\sum_{m=0}^{\\infty} \\sum_{n=0}^{\\infty}
        \\frac{(a)_{m+n} (b_1)_m (b_2)_n}{(c)_{m+n}}
        \\frac{x^m y^n}{m! n!}.

    Examples
    ========

    >>> from sympy import appellf1, symbols
    >>> x, y, a, b1, b2, c = symbols('x y a b1 b2 c')
    >>> appellf1(2., 1., 6., 4., 5., 6.)
    0.0063339426292673
    >>> appellf1(12., 12., 6., 4., 0.5, 0.12)
    172870711.659936
    >>> appellf1(40, 2, 6, 4, 15, 60)
    appellf1(40, 2, 6, 4, 15, 60)
    >>> appellf1(20., 12., 10., 3., 0.5, 0.12)
    15605338197184.4
    >>> appellf1(40, 2, 6, 4, x, y)
    appellf1(40, 2, 6, 4, x, y)
    >>> appellf1(a, b1, b2, c, x, y)
    appellf1(a, b1, b2, c, x, y)

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Appell_series
    .. [2] https://functions.wolfram.com/HypergeometricFunctions/AppellF1/

    """
    eval = (lambda cls, a, b1, b2, c, x, y: if default_sort_key(b1) > default_sort_key(b2):
b2 = b1b1 = b2y = xx = ycls(a, b1, b2, c, x, y)if None == b2 and default_sort_key(x) > default_sort_key(y):
y = xx = ycls(a, b1, b2, c, x, y)if None == 0 or y == 0:
S.OneNone)()
    
    def fdiff(self, argindex = (5,)):
        (a, b1, b2, c, x, y) = self.args
        if argindex == 5:
            return (a * b1 / c) * appellf1(a + 1, b1 + 1, b2, c + 1, x, y)
        if None == 6:
            return (a * b2 / c) * appellf1(a + 1, b1, b2 + 1, c + 1, x, y)
        if None in (1, 2, 3, 4):
            return Derivative(self, self.args[argindex - 1])
        raise None(self, argindex)
