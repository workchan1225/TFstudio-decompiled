# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transforms.pyc (Python 3.11)

''' Integral Transforms '''
from functools import reduce, wraps
from itertools import repeat
from sympy.core import S, pi
from sympy.core.add import Add
from sympy.core.function import AppliedUndef, count_ops, expand, expand_mul, Function
from sympy.core.mul import Mul
from sympy.core.intfunc import igcd, ilcm
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Dummy
from sympy.core.traversal import postorder_traversal
from sympy.functions.combinatorial.factorials import factorial, rf
from sympy.functions.elementary.complexes import re, arg, Abs
from sympy.functions.elementary.exponential import exp, exp_polar
from sympy.functions.elementary.hyperbolic import cosh, coth, sinh, tanh
from sympy.functions.elementary.integers import ceiling
from sympy.functions.elementary.miscellaneous import Max, Min, sqrt
from sympy.functions.elementary.piecewise import piecewise_fold
from sympy.functions.elementary.trigonometric import cos, cot, sin, tan
from sympy.functions.special.bessel import besselj
from sympy.functions.special.delta_functions import Heaviside
from sympy.functions.special.gamma_functions import gamma
from sympy.functions.special.hyper import meijerg
from sympy.integrals import integrate, Integral
from sympy.integrals.meijerint import _dummy
from sympy.logic.boolalg import to_cnf, conjuncts, disjuncts, Or, And
from sympy.polys.polyroots import roots
from sympy.polys.polytools import factor, Poly
from sympy.polys.rootoftools import CRootOf
from sympy.utilities.iterables import iterable
from sympy.utilities.misc import debug

class IntegralTransformError(NotImplementedError):
    pass
# WARNING: Decompyle incomplete


class IntegralTransform(Function):
    """
    Base class for integral transforms.

    Explanation
    ===========

    This class represents unevaluated transforms.

    To implement a concrete transform, derive from this class and implement
    the ``_compute_transform(f, x, s, **hints)`` and ``_as_integral(f, x, s)``
    functions. If the transform cannot be computed, raise :obj:`IntegralTransformError`.

    Also set ``cls._name``. For instance,

    >>> from sympy import LaplaceTransform
    >>> LaplaceTransform._name
    'Laplace'

    Implement ``self._collapse_extra`` if your function returns more than just a
    number and possibly a convergence condition.
    """
    function = (lambda self: self.args[0])()
    function_variable = (lambda self: self.args[1])()
    transform_variable = (lambda self: self.args[2])()
    free_symbols = (lambda self: self.function.free_symbols.union({
self.transform_variable}) - {
self.function_variable})()
    
    def _compute_transform(self, f, x, s, **hints):
        raise NotImplementedError

    
    def _as_integral(self, f, x, s):
        raise NotImplementedError

    
    def _collapse_extra(self, extra):
        pass
    # WARNING: Decompyle incomplete

    
    def _try_directly(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def doit(self, **hints):
        '''
        Try to evaluate the transform in closed form.

        Explanation
        ===========

        This general function handles linearity, but apart from that leaves
        pretty much everything to _compute_transform.

        Standard hints are the following:

        - ``simplify``: whether or not to simplify the result
        - ``noconds``: if True, do not return convergence conditions
        - ``needeval``: if True, raise IntegralTransformError instead of
                        returning IntegralTransform objects

        The default values of these hints depend on the concrete transform,
        usually the default is
        ``(simplify, noconds, needeval) = (True, False, False)``.
        '''
        pass
    # WARNING: Decompyle incomplete

    as_integral = (lambda self: self._as_integral(self.function, self.function_variable, self.transform_variable))()
    
    def _eval_rewrite_as_Integral(self, *args, **kwargs):
        return self.as_integral



def _simplify(expr, doit):
    if doit:
        simplify = simplify
        import sympy.simplify
        powdenest = powdenest
        import sympy.simplify.powsimp
        return simplify(powdenest(piecewise_fold(expr), polar = True))


def _noconds_(default):
    '''
    This is a decorator generator for dropping convergence conditions.

    Explanation
    ===========

    Suppose you define a function ``transform(*args)`` which returns a tuple of
    the form ``(result, cond1, cond2, ...)``.

    Decorating it ``@_noconds_(default)`` will add a new keyword argument
    ``noconds`` to it. If ``noconds=True``, the return value will be altered to
    be only ``result``, whereas if ``noconds=False`` the return value will not
    be altered.

    The default value of the ``noconds`` keyword will be ``default`` (i.e. the
    argument of this function).
    '''
    pass
# WARNING: Decompyle incomplete

_noconds = _noconds_(False)

def _default_integrator(f, x):
    return integrate(f, (x, S.Zero, S.Infinity))

_mellin_transform = (lambda f, x, s_, integrator, simplify = (_default_integrator, True): pass# WARNING: Decompyle incomplete
)()

class MellinTransform(IntegralTransform):
    '''
    Class representing unevaluated Mellin transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Mellin transforms, see the :func:`mellin_transform`
    docstring.
    '''
    _name = 'Mellin'
    
    def _compute_transform(self, f, x, s, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _as_integral(self, f, x, s):
        return Integral(f * x ** (s - 1), (x, S.Zero, S.Infinity))

    
    def _collapse_extra(self, extra):
        a = []
        b = []
        cond = []
    # WARNING: Decompyle incomplete



def mellin_transform(f, x, s, **hints):
    '''
    Compute the Mellin transform `F(s)` of `f(x)`,

    .. math :: F(s) = \\int_0^\\infty x^{s-1} f(x) \\mathrm{d}x.

    For all "sensible" functions, this converges absolutely in a strip
      `a < \\operatorname{Re}(s) < b`.

    Explanation
    ===========

    The Mellin transform is related via change of variables to the Fourier
    transform, and also to the (bilateral) Laplace transform.

    This function returns ``(F, (a, b), cond)``
    where ``F`` is the Mellin transform of ``f``, ``(a, b)`` is the fundamental strip
    (as above), and ``cond`` are auxiliary convergence conditions.

    If the integral cannot be computed in closed form, this function returns
    an unevaluated :class:`MellinTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`. If ``noconds=False``,
    then only `F` will be returned (i.e. not ``cond``, and also not the strip
    ``(a, b)``).

    Examples
    ========

    >>> from sympy import mellin_transform, exp
    >>> from sympy.abc import x, s
    >>> mellin_transform(exp(-x), x, s)
    (gamma(s), (0, oo), True)

    See Also
    ========

    inverse_mellin_transform, laplace_transform, fourier_transform
    hankel_transform, inverse_hankel_transform
    '''
    pass
# WARNING: Decompyle incomplete


def _rewrite_sin(m_n, s, a, b):
    '''
    Re-write the sine function ``sin(m*s + n)`` as gamma functions, compatible
    with the strip (a, b).

    Return ``(gamma1, gamma2, fac)`` so that ``f == fac/(gamma1 * gamma2)``.

    Examples
    ========

    >>> from sympy.integrals.transforms import _rewrite_sin
    >>> from sympy import pi, S
    >>> from sympy.abc import s
    >>> _rewrite_sin((pi, 0), s, 0, 1)
    (gamma(s), gamma(1 - s), pi)
    >>> _rewrite_sin((pi, 0), s, 1, 0)
    (gamma(s - 1), gamma(2 - s), -pi)
    >>> _rewrite_sin((pi, 0), s, -1, 0)
    (gamma(s + 1), gamma(-s), -pi)
    >>> _rewrite_sin((pi, pi/2), s, S(1)/2, S(3)/2)
    (gamma(s - 1/2), gamma(3/2 - s), -pi)
    >>> _rewrite_sin((pi, pi), s, 0, 1)
    (gamma(s), gamma(1 - s), -pi)
    >>> _rewrite_sin((2*pi, 0), s, 0, S(1)/2)
    (gamma(2*s), gamma(1 - 2*s), pi)
    >>> _rewrite_sin((2*pi, 0), s, S(1)/2, 1)
    (gamma(2*s - 1), gamma(2 - 2*s), -pi)
    '''
    (m, n) = m_n
    m = expand_mul(m / pi)
    n = expand_mul(n / pi)
    r = ceiling(-m * a - n.as_real_imag()[0])
    return (gamma(m * s + n + r), gamma(1 - n - r - m * s), -1 ** r * pi)


class MellinTransformStripError(ValueError):
    '''
    Exception raised by _rewrite_gamma. Mainly for internal use.
    '''
    pass


def _rewrite_gamma(f, s, a, b):
    '''
    Try to rewrite the product f(s) as a product of gamma functions,
    so that the inverse Mellin transform of f can be expressed as a meijer
    G function.

    Explanation
    ===========

    Return (an, ap), (bm, bq), arg, exp, fac such that
    G((an, ap), (bm, bq), arg/z**exp)*fac is the inverse Mellin transform of f(s).

    Raises IntegralTransformError or MellinTransformStripError on failure.

    It is asserted that f has no poles in the fundamental strip designated by
    (a, b). One of a and b is allowed to be None. The fundamental strip is
    important, because it determines the inversion contour.

    This function can handle exponentials, linear factors, trigonometric
    functions.

    This is a helper function for inverse_mellin_transform that will not
    attempt any transformations on f.

    Examples
    ========

    >>> from sympy.integrals.transforms import _rewrite_gamma
    >>> from sympy.abc import s
    >>> from sympy import oo
    >>> _rewrite_gamma(s*(s+3)*(s-1), s, -oo, oo)
    (([], [-3, 0, 1]), ([-2, 1, 2], []), 1, 1, -1)
    >>> _rewrite_gamma((s-1)**2, s, -oo, oo)
    (([], [1, 1]), ([2, 2], []), 1, 1, 1)

    Importance of the fundamental strip:

    >>> _rewrite_gamma(1/s, s, 0, oo)
    (([1], []), ([], [0]), 1, 1, 1)
    >>> _rewrite_gamma(1/s, s, None, oo)
    (([1], []), ([], [0]), 1, 1, 1)
    >>> _rewrite_gamma(1/s, s, 0, None)
    (([1], []), ([], [0]), 1, 1, 1)
    >>> _rewrite_gamma(1/s, s, -oo, 0)
    (([], [1]), ([0], []), 1, 1, -1)
    >>> _rewrite_gamma(1/s, s, None, 0)
    (([], [1]), ([0], []), 1, 1, -1)
    >>> _rewrite_gamma(1/s, s, -oo, None)
    (([], [1]), ([0], []), 1, 1, -1)

    >>> _rewrite_gamma(2**(-s+3), s, -oo, oo)
    (([], []), ([], []), 1/2, 1, 8)
    '''
    pass
# WARNING: Decompyle incomplete

_inverse_mellin_transform = (lambda F, s, x_, strip, as_meijerg = (False,): pass# WARNING: Decompyle incomplete
)()
_allowed = None

class InverseMellinTransform(IntegralTransform):
    '''
    Class representing unevaluated inverse Mellin transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Mellin transforms, see the
    :func:`inverse_mellin_transform` docstring.
    '''
    _name = 'Inverse Mellin'
    _none_sentinel = Dummy('None')
    _c = Dummy('c')
    
    def __new__(cls, F, s, x, a, b, **opts):
        pass
    # WARNING: Decompyle incomplete

    fundamental_strip = (lambda self: b = self.args[4]a = self.args[3]if a is InverseMellinTransform._none_sentinel:
a = Noneif b is InverseMellinTransform._none_sentinel:
b = None(a, b))()
    
    def _compute_transform(self, F, s, x, **hints):
        hints.pop('simplify', True)
    # WARNING: Decompyle incomplete

    
    def _as_integral(self, F, s, x):
        c = self.__class__._c
        return Integral(F * x ** (-s), (s, c - S.ImaginaryUnit * S.Infinity, c + S.ImaginaryUnit * S.Infinity)) / (2 * S.Pi * S.ImaginaryUnit)



def inverse_mellin_transform(F, s, x, strip, **hints):
    '''
    Compute the inverse Mellin transform of `F(s)` over the fundamental
    strip given by ``strip=(a, b)``.

    Explanation
    ===========

    This can be defined as

    .. math:: f(x) = \\frac{1}{2\\pi i} \\int_{c - i\\infty}^{c + i\\infty} x^{-s} F(s) \\mathrm{d}s,

    for any `c` in the fundamental strip. Under certain regularity
    conditions on `F` and/or `f`,
    this recovers `f` from its Mellin transform `F`
    (and vice versa), for positive real `x`.

    One of `a` or `b` may be passed as ``None``; a suitable `c` will be
    inferred.

    If the integral cannot be computed in closed form, this function returns
    an unevaluated :class:`InverseMellinTransform` object.

    Note that this function will assume x to be positive and real, regardless
    of the SymPy assumptions!

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.

    Examples
    ========

    >>> from sympy import inverse_mellin_transform, oo, gamma
    >>> from sympy.abc import x, s
    >>> inverse_mellin_transform(gamma(s), s, x, (0, oo))
    exp(-x)

    The fundamental strip matters:

    >>> f = 1/(s**2 - 1)
    >>> inverse_mellin_transform(f, s, x, (-oo, -1))
    x*(1 - 1/x**2)*Heaviside(x - 1)/2
    >>> inverse_mellin_transform(f, s, x, (-1, 1))
    -x*Heaviside(1 - x)/2 - Heaviside(x - 1)/(2*x)
    >>> inverse_mellin_transform(f, s, x, (1, oo))
    (1/2 - x**2/2)*Heaviside(1 - x)/x

    See Also
    ========

    mellin_transform
    hankel_transform, inverse_hankel_transform
    '''
    pass
# WARNING: Decompyle incomplete

_fourier_transform = (lambda f, x, k, a, b, name, simplify = (True,): F = integrate(a * f * exp(b * S.ImaginaryUnit * x * k), (x, S.NegativeInfinity, S.Infinity))if not F.has(Integral):
(_simplify(F, simplify), S.true)integral_f = None(f, (x, S.NegativeInfinity, S.Infinity))if integral_f in (S.NegativeInfinity, S.Infinity, S.NaN) or integral_f.has(Integral):
raise IntegralTransformError(name, f, 'function not integrable on real axis')if not F.is_Piecewise:
raise IntegralTransformError(name, f, 'could not compute integral')(F, cond) = F.args[0]if F.has(Integral):
raise IntegralTransformError(name, f, 'integral in unexpected form')(_simplify(F, simplify), cond))()

class FourierTypeTransform(IntegralTransform):
    ''' Base class for Fourier transforms.'''
    
    def a(self):
        raise NotImplementedError('Class %s must implement a(self) but does not' % self.__class__)

    
    def b(self):
        raise NotImplementedError('Class %s must implement b(self) but does not' % self.__class__)

    
    def _compute_transform(self, f, x, k, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _as_integral(self, f, x, k):
        a = self.a()
        b = self.b()
        return Integral(a * f * exp(b * S.ImaginaryUnit * x * k), (x, S.NegativeInfinity, S.Infinity))



class FourierTransform(FourierTypeTransform):
    '''
    Class representing unevaluated Fourier transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Fourier transforms, see the :func:`fourier_transform`
    docstring.
    '''
    _name = 'Fourier'
    
    def a(self):
        return 1

    
    def b(self):
        return -2 * S.Pi



def fourier_transform(f, x, k, **hints):
    '''
    Compute the unitary, ordinary-frequency Fourier transform of ``f``, defined
    as

    .. math:: F(k) = \\int_{-\\infty}^\\infty f(x) e^{-2\\pi i x k} \\mathrm{d} x.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`FourierTransform` object.

    For other Fourier transform conventions, see the function
    :func:`sympy.integrals.transforms._fourier_transform`.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import fourier_transform, exp
    >>> from sympy.abc import x, k
    >>> fourier_transform(exp(-x**2), x, k)
    sqrt(pi)*exp(-pi**2*k**2)
    >>> fourier_transform(exp(-x**2), x, k, noconds=False)
    (sqrt(pi)*exp(-pi**2*k**2), True)

    See Also
    ========

    inverse_fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete


class InverseFourierTransform(FourierTypeTransform):
    '''
    Class representing unevaluated inverse Fourier transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Fourier transforms, see the
    :func:`inverse_fourier_transform` docstring.
    '''
    _name = 'Inverse Fourier'
    
    def a(self):
        return 1

    
    def b(self):
        return 2 * S.Pi



def inverse_fourier_transform(F, k, x, **hints):
    '''
    Compute the unitary, ordinary-frequency inverse Fourier transform of `F`,
    defined as

    .. math:: f(x) = \\int_{-\\infty}^\\infty F(k) e^{2\\pi i x k} \\mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseFourierTransform` object.

    For other Fourier transform conventions, see the function
    :func:`sympy.integrals.transforms._fourier_transform`.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import inverse_fourier_transform, exp, sqrt, pi
    >>> from sympy.abc import x, k
    >>> inverse_fourier_transform(sqrt(pi)*exp(-(pi*k)**2), k, x)
    exp(-x**2)
    >>> inverse_fourier_transform(sqrt(pi)*exp(-(pi*k)**2), k, x, noconds=False)
    (exp(-x**2), True)

    See Also
    ========

    fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete

_sine_cosine_transform = (lambda f, x, k, a, b, K, name, simplify = (True,): F = integrate(a * f * K(b * x * k), (x, S.Zero, S.Infinity))if not F.has(Integral):
(_simplify(F, simplify), S.true)if not None.is_Piecewise:
raise IntegralTransformError(name, f, 'could not compute integral')(F, cond) = F.args[0]if F.has(Integral):
raise IntegralTransformError(name, f, 'integral in unexpected form')(_simplify(F, simplify), cond))()

class SineCosineTypeTransform(IntegralTransform):
    '''
    Base class for sine and cosine transforms.
    Specify cls._kern.
    '''
    
    def a(self):
        raise NotImplementedError('Class %s must implement a(self) but does not' % self.__class__)

    
    def b(self):
        raise NotImplementedError('Class %s must implement b(self) but does not' % self.__class__)

    
    def _compute_transform(self, f, x, k, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _as_integral(self, f, x, k):
        a = self.a()
        b = self.b()
        K = self.__class__._kern
        return Integral(a * f * K(b * x * k), (x, S.Zero, S.Infinity))



class SineTransform(SineCosineTypeTransform):
    '''
    Class representing unevaluated sine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute sine transforms, see the :func:`sine_transform`
    docstring.
    '''
    _name = 'Sine'
    _kern = sin
    
    def a(self):
        return sqrt(2) / sqrt(pi)

    
    def b(self):
        return S.One



def sine_transform(f, x, k, **hints):
    '''
    Compute the unitary, ordinary-frequency sine transform of `f`, defined
    as

    .. math:: F(k) = \\sqrt{\\frac{2}{\\pi}} \\int_{0}^\\infty f(x) \\sin(2\\pi x k) \\mathrm{d} x.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`SineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import sine_transform, exp
    >>> from sympy.abc import x, k, a
    >>> sine_transform(x*exp(-a*x**2), x, k)
    sqrt(2)*k*exp(-k**2/(4*a))/(4*a**(3/2))
    >>> sine_transform(x**(-a), x, k)
    2**(1/2 - a)*k**(a - 1)*gamma(1 - a/2)/gamma(a/2 + 1/2)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete


class InverseSineTransform(SineCosineTypeTransform):
    '''
    Class representing unevaluated inverse sine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse sine transforms, see the
    :func:`inverse_sine_transform` docstring.
    '''
    _name = 'Inverse Sine'
    _kern = sin
    
    def a(self):
        return sqrt(2) / sqrt(pi)

    
    def b(self):
        return S.One



def inverse_sine_transform(F, k, x, **hints):
    '''
    Compute the unitary, ordinary-frequency inverse sine transform of `F`,
    defined as

    .. math:: f(x) = \\sqrt{\\frac{2}{\\pi}} \\int_{0}^\\infty F(k) \\sin(2\\pi x k) \\mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseSineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import inverse_sine_transform, exp, sqrt, gamma
    >>> from sympy.abc import x, k, a
    >>> inverse_sine_transform(2**((1-2*a)/2)*k**(a - 1)*
    ...     gamma(-a/2 + 1)/gamma((a+1)/2), k, x)
    x**(-a)
    >>> inverse_sine_transform(sqrt(2)*k*exp(-k**2/(4*a))/(4*sqrt(a)**3), k, x)
    x*exp(-a*x**2)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete


class CosineTransform(SineCosineTypeTransform):
    '''
    Class representing unevaluated cosine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute cosine transforms, see the :func:`cosine_transform`
    docstring.
    '''
    _name = 'Cosine'
    _kern = cos
    
    def a(self):
        return sqrt(2) / sqrt(pi)

    
    def b(self):
        return S.One



def cosine_transform(f, x, k, **hints):
    '''
    Compute the unitary, ordinary-frequency cosine transform of `f`, defined
    as

    .. math:: F(k) = \\sqrt{\\frac{2}{\\pi}} \\int_{0}^\\infty f(x) \\cos(2\\pi x k) \\mathrm{d} x.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`CosineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import cosine_transform, exp, sqrt, cos
    >>> from sympy.abc import x, k, a
    >>> cosine_transform(exp(-a*x), x, k)
    sqrt(2)*a/(sqrt(pi)*(a**2 + k**2))
    >>> cosine_transform(exp(-a*sqrt(x))*cos(a*sqrt(x)), x, k)
    a*exp(-a**2/(2*k))/(2*k**(3/2))

    See Also
    ========

    fourier_transform, inverse_fourier_transform,
    sine_transform, inverse_sine_transform
    inverse_cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete


class InverseCosineTransform(SineCosineTypeTransform):
    '''
    Class representing unevaluated inverse cosine transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse cosine transforms, see the
    :func:`inverse_cosine_transform` docstring.
    '''
    _name = 'Inverse Cosine'
    _kern = cos
    
    def a(self):
        return sqrt(2) / sqrt(pi)

    
    def b(self):
        return S.One



def inverse_cosine_transform(F, k, x, **hints):
    '''
    Compute the unitary, ordinary-frequency inverse cosine transform of `F`,
    defined as

    .. math:: f(x) = \\sqrt{\\frac{2}{\\pi}} \\int_{0}^\\infty F(k) \\cos(2\\pi x k) \\mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseCosineTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import inverse_cosine_transform, sqrt, pi
    >>> from sympy.abc import x, k, a
    >>> inverse_cosine_transform(sqrt(2)*a/(sqrt(pi)*(a**2 + k**2)), k, x)
    exp(-a*x)
    >>> inverse_cosine_transform(1/sqrt(k), k, x)
    1/sqrt(x)

    See Also
    ========

    fourier_transform, inverse_fourier_transform,
    sine_transform, inverse_sine_transform
    cosine_transform
    hankel_transform, inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete

_hankel_transform = (lambda f, r, k, nu, name, simplify = (True,): F = integrate(f * besselj(nu, k * r) * r, (r, S.Zero, S.Infinity))if not F.has(Integral):
(_simplify(F, simplify), S.true)if not None.is_Piecewise:
raise IntegralTransformError(name, f, 'could not compute integral')(F, cond) = F.args[0]if F.has(Integral):
raise IntegralTransformError(name, f, 'integral in unexpected form')(_simplify(F, simplify), cond))()

class HankelTypeTransform(IntegralTransform):
    '''
    Base class for Hankel transforms.
    '''
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _compute_transform(self, f, r, k, nu, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _as_integral(self, f, r, k, nu):
        return Integral(f * besselj(nu, k * r) * r, (r, S.Zero, S.Infinity))

    as_integral = (lambda self: self._as_integral(self.function, self.function_variable, self.transform_variable, self.args[3]))()


class HankelTransform(HankelTypeTransform):
    '''
    Class representing unevaluated Hankel transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute Hankel transforms, see the :func:`hankel_transform`
    docstring.
    '''
    _name = 'Hankel'


def hankel_transform(f, r, k, nu, **hints):
    '''
    Compute the Hankel transform of `f`, defined as

    .. math:: F_\\nu(k) = \\int_{0}^\\infty f(r) J_\\nu(k r) r \\mathrm{d} r.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`HankelTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import hankel_transform, inverse_hankel_transform
    >>> from sympy import exp
    >>> from sympy.abc import r, k, m, nu, a

    >>> ht = hankel_transform(1/r**m, r, k, nu)
    >>> ht
    2*k**(m - 2)*gamma(-m/2 + nu/2 + 1)/(2**m*gamma(m/2 + nu/2))

    >>> inverse_hankel_transform(ht, k, r, nu)
    r**(-m)

    >>> ht = hankel_transform(exp(-a*r), r, k, 0)
    >>> ht
    a/(k**3*(a**2/k**2 + 1)**(3/2))

    >>> inverse_hankel_transform(ht, k, r, 0)
    exp(-a*r)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    inverse_hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete


class InverseHankelTransform(HankelTypeTransform):
    '''
    Class representing unevaluated inverse Hankel transforms.

    For usage of this class, see the :class:`IntegralTransform` docstring.

    For how to compute inverse Hankel transforms, see the
    :func:`inverse_hankel_transform` docstring.
    '''
    _name = 'Inverse Hankel'


def inverse_hankel_transform(F, k, r, nu, **hints):
    '''
    Compute the inverse Hankel transform of `F` defined as

    .. math:: f(r) = \\int_{0}^\\infty F_\\nu(k) J_\\nu(k r) k \\mathrm{d} k.

    Explanation
    ===========

    If the transform cannot be computed in closed form, this
    function returns an unevaluated :class:`InverseHankelTransform` object.

    For a description of possible hints, refer to the docstring of
    :func:`sympy.integrals.transforms.IntegralTransform.doit`.
    Note that for this transform, by default ``noconds=True``.

    Examples
    ========

    >>> from sympy import hankel_transform, inverse_hankel_transform
    >>> from sympy import exp
    >>> from sympy.abc import r, k, m, nu, a

    >>> ht = hankel_transform(1/r**m, r, k, nu)
    >>> ht
    2*k**(m - 2)*gamma(-m/2 + nu/2 + 1)/(2**m*gamma(m/2 + nu/2))

    >>> inverse_hankel_transform(ht, k, r, nu)
    r**(-m)

    >>> ht = hankel_transform(exp(-a*r), r, k, 0)
    >>> ht
    a/(k**3*(a**2/k**2 + 1)**(3/2))

    >>> inverse_hankel_transform(ht, k, r, 0)
    exp(-a*r)

    See Also
    ========

    fourier_transform, inverse_fourier_transform
    sine_transform, inverse_sine_transform
    cosine_transform, inverse_cosine_transform
    hankel_transform
    mellin_transform, laplace_transform
    '''
    pass
# WARNING: Decompyle incomplete


laplace
_laplace.LaplaceTransform = import sympy.integrals.laplace, integrals
laplace_transform = _laplace.laplace_transform
laplace_correspondence = _laplace.laplace_correspondence
laplace_initial_conds = _laplace.laplace_initial_conds
InverseLaplaceTransform = _laplace.InverseLaplaceTransform
inverse_laplace_transform = _laplace.inverse_laplace_transform
