# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fancysets.pyc (Python 3.11)

from functools import reduce
from itertools import product
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.core.function import Lambda
from sympy.core.logic import fuzzy_not, fuzzy_or, fuzzy_and
from sympy.core.mod import Mod
from sympy.core.intfunc import igcd
from sympy.core.numbers import oo, Rational
from sympy.core.relational import Eq, is_eq
from sympy.core.kind import NumberKind
from sympy.core.singleton import Singleton, S
from sympy.core.symbol import Dummy, symbols, Symbol
from sympy.core.sympify import _sympify, sympify, _sympy_converter
from sympy.functions.elementary.integers import ceiling, floor
from sympy.functions.elementary.trigonometric import sin, cos
from sympy.logic.boolalg import And, Or
from sets import tfn, Set, Interval, Union, FiniteSet, ProductSet, SetKind
from sympy.utilities.misc import filldedent

def Rationals():
    '''Rationals'''
    __doc__ = '\n    Represents the rational numbers. This set is also available as\n    the singleton ``S.Rationals``.\n\n    Examples\n    ========\n\n    >>> from sympy import S\n    >>> S.Half in S.Rationals\n    True\n    >>> iterable = iter(S.Rationals)\n    >>> [next(iterable) for i in range(12)]\n    [0, 1, -1, 1/2, 2, -1/2, -2, 1/3, 3, -1/3, -3, 2/3]\n    '
    is_iterable = True
    _inf = S.NegativeInfinity
    _sup = S.Infinity
    is_empty = False
    is_finite_set = False
    
    def _contains(self, other):
        if not isinstance(other, Expr):
            return S.false
        return None[other.is_rational]

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    _boundary = (lambda self: S.Reals)()
    
    def _kind(self):
        return SetKind(NumberKind)


Rationals = <NODE:27>(Rationals, 'Rationals', Set, metaclass = Singleton)

def Naturals():
    '''Naturals'''
    __doc__ = '\n    Represents the natural numbers (or counting numbers) which are all\n    positive integers starting from 1. This set is also available as\n    the singleton ``S.Naturals``.\n\n    Examples\n    ========\n\n    >>> from sympy import S, Interval, pprint\n    >>> 5 in S.Naturals\n    True\n    >>> iterable = iter(S.Naturals)\n    >>> next(iterable)\n    1\n    >>> next(iterable)\n    2\n    >>> next(iterable)\n    3\n    >>> pprint(S.Naturals.intersect(Interval(0, 10)))\n    {1, 2, ..., 10}\n\n    See Also\n    ========\n\n    Naturals0 : non-negative integers (i.e. includes 0, too)\n    Integers : also includes negative integers\n    '
    is_iterable = True
    _inf = S.One
    _sup = S.Infinity
    is_empty = False
    is_finite_set = False
    
    def _contains(self, other):
        if not isinstance(other, Expr):
            return S.false
        if None.is_positive and other.is_integer:
            return S.true
        if None.is_integer is False or other.is_positive is False:
            return S.false

    
    def _eval_is_subset(self, other):
        return Range(1, oo).is_subset(other)

    
    def _eval_is_superset(self, other):
        return Range(1, oo).is_superset(other)

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    _boundary = (lambda self: self)()
    
    def as_relational(self, x):
        return And(Eq(floor(x), x), x >= self.inf, x < oo)

    
    def _kind(self):
        return SetKind(NumberKind)


Naturals = <NODE:27>(Naturals, 'Naturals', Set, metaclass = Singleton)

class Naturals0(Naturals):
    '''Represents the whole numbers which are all the non-negative integers,
    inclusive of zero.

    See Also
    ========

    Naturals : positive integers; does not include 0
    Integers : also includes the negative integers
    '''
    _inf = S.Zero
    
    def _contains(self, other):
        if not isinstance(other, Expr):
            return S.false
        if None.is_integer and other.is_nonnegative:
            return S.true
        if None.is_integer is False or other.is_nonnegative is False:
            return S.false

    
    def _eval_is_subset(self, other):
        return Range(oo).is_subset(other)

    
    def _eval_is_superset(self, other):
        return Range(oo).is_superset(other)



def Integers():
    '''Integers'''
    __doc__ = '\n    Represents all integers: positive, negative and zero. This set is also\n    available as the singleton ``S.Integers``.\n\n    Examples\n    ========\n\n    >>> from sympy import S, Interval, pprint\n    >>> 5 in S.Naturals\n    True\n    >>> iterable = iter(S.Integers)\n    >>> next(iterable)\n    0\n    >>> next(iterable)\n    1\n    >>> next(iterable)\n    -1\n    >>> next(iterable)\n    2\n\n    >>> pprint(S.Integers.intersect(Interval(-4, 4)))\n    {-4, -3, ..., 4}\n\n    See Also\n    ========\n\n    Naturals0 : non-negative integers\n    Integers : positive and negative integers and zero\n    '
    is_iterable = True
    is_empty = False
    is_finite_set = False
    
    def _contains(self, other):
        if not isinstance(other, Expr):
            return S.false
        return None[other.is_integer]

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    _inf = (lambda self: S.NegativeInfinity)()
    _sup = (lambda self: S.Infinity)()
    _boundary = (lambda self: self)()
    
    def _kind(self):
        return SetKind(NumberKind)

    
    def as_relational(self, x):
        return And(Eq(floor(x), x), -oo < x, x < oo)

    
    def _eval_is_subset(self, other):
        return Range(-oo, oo).is_subset(other)

    
    def _eval_is_superset(self, other):
        return Range(-oo, oo).is_superset(other)


Integers = <NODE:27>(Integers, 'Integers', Set, metaclass = Singleton)

def Reals():
    '''Reals'''
    __doc__ = '\n    Represents all real numbers\n    from negative infinity to positive infinity,\n    including all integer, rational and irrational numbers.\n    This set is also available as the singleton ``S.Reals``.\n\n\n    Examples\n    ========\n\n    >>> from sympy import S, Rational, pi, I\n    >>> 5 in S.Reals\n    True\n    >>> Rational(-1, 2) in S.Reals\n    True\n    >>> pi in S.Reals\n    True\n    >>> 3*I in S.Reals\n    False\n    >>> S.Reals.contains(pi)\n    True\n\n\n    See Also\n    ========\n\n    ComplexRegion\n    '
    start = (lambda self: S.NegativeInfinity)()
    end = (lambda self: S.Infinity)()
    left_open = (lambda self: True)()
    right_open = (lambda self: True)()
    
    def __eq__(self, other):
        return other == Interval(S.NegativeInfinity, S.Infinity)

    
    def __hash__(self):
        return hash(Interval(S.NegativeInfinity, S.Infinity))


Reals = <NODE:27>(Reals, 'Reals', Interval, metaclass = Singleton)

class ImageSet(Set):
    """
    Image of a set under a mathematical function. The transformation
    must be given as a Lambda function which has as many arguments
    as the elements of the set upon which it operates, e.g. 1 argument
    when acting on the set of integers or 2 arguments when acting on
    a complex region.

    This function is not normally called directly, but is called
    from ``imageset``.


    Examples
    ========

    >>> from sympy import Symbol, S, pi, Dummy, Lambda
    >>> from sympy import FiniteSet, ImageSet, Interval

    >>> x = Symbol('x')
    >>> N = S.Naturals
    >>> squares = ImageSet(Lambda(x, x**2), N) # {x**2 for x in N}
    >>> 4 in squares
    True
    >>> 5 in squares
    False

    >>> FiniteSet(0, 1, 2, 3, 4, 5, 6, 7, 9, 10).intersect(squares)
    {1, 4, 9}

    >>> square_iterable = iter(squares)
    >>> for i in range(4):
    ...     next(square_iterable)
    1
    4
    9
    16

    If you want to get value for `x` = 2, 1/2 etc. (Please check whether the
    `x` value is in ``base_set`` or not before passing it as args)

    >>> squares.lamda(2)
    4
    >>> squares.lamda(S(1)/2)
    1/4

    >>> n = Dummy('n')
    >>> solutions = ImageSet(Lambda(n, n*pi), S.Integers) # solutions of sin(x) = 0
    >>> dom = Interval(-1, 1)
    >>> dom.intersect(solutions)
    {0}

    See Also
    ========

    sympy.sets.sets.imageset
    """
    
    def __new__(cls, flambda, *sets):
        pass
    # WARNING: Decompyle incomplete

    lamda = property((lambda self: self.args[0]))
    base_sets = property((lambda self: self.args[1:]))
    base_set = (lambda self: sets = self.base_setsif len(sets) == 1:
sets[0]# WARNING: Decompyle incomplete
)()
    base_pset = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _check_sig = (lambda cls, sig_i, set_i: pass# WARNING: Decompyle incomplete
)()
    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _is_multivariate(self):
        return len(self.lamda.variables) > 1

    
    def _contains(self, other):
        pass
    # WARNING: Decompyle incomplete

    is_iterable = (lambda self: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.base_sets())
)()
    
    def doit(self, **hints):
        pass
    # WARNING: Decompyle incomplete

    
    def _kind(self):
        return SetKind(self.lamda.expr.kind)



class Range(Set):
    """
    Represents a range of integers. Can be called as ``Range(stop)``,
    ``Range(start, stop)``, or ``Range(start, stop, step)``; when ``step`` is
    not given it defaults to 1.

    ``Range(stop)`` is the same as ``Range(0, stop, 1)`` and the stop value
    (just as for Python ranges) is not included in the Range values.

        >>> from sympy import Range
        >>> list(Range(3))
        [0, 1, 2]

    The step can also be negative:

        >>> list(Range(10, 0, -2))
        [10, 8, 6, 4, 2]

    The stop value is made canonical so equivalent ranges always
    have the same args:

        >>> Range(0, 10, 3)
        Range(0, 12, 3)

    Infinite ranges are allowed. ``oo`` and ``-oo`` are never included in the
    set (``Range`` is always a subset of ``Integers``). If the starting point
    is infinite, then the final value is ``stop - step``. To iterate such a
    range, it needs to be reversed:

        >>> from sympy import oo
        >>> r = Range(-oo, 1)
        >>> r[-1]
        0
        >>> next(iter(r))
        Traceback (most recent call last):
        ...
        TypeError: Cannot iterate over Range with infinite start
        >>> next(iter(r.reversed))
        0

    Although ``Range`` is a :class:`Set` (and supports the normal set
    operations) it maintains the order of the elements and can
    be used in contexts where ``range`` would be used.

        >>> from sympy import Interval
        >>> Range(0, 10, 2).intersect(Interval(3, 7))
        Range(4, 8, 2)
        >>> list(_)
        [4, 6]

    Although slicing of a Range will always return a Range -- possibly
    empty -- an empty set will be returned from any intersection that
    is empty:

        >>> Range(3)[:0]
        Range(0, 0, 1)
        >>> Range(3).intersect(Interval(4, oo))
        EmptySet
        >>> Range(3).intersect(Range(4, oo))
        EmptySet

    Range will accept symbolic arguments but has very limited support
    for doing anything other than displaying the Range:

        >>> from sympy import Symbol, pprint
        >>> from sympy.abc import i, j, k
        >>> Range(i, j, k).start
        i
        >>> Range(i, j, k).inf
        Traceback (most recent call last):
        ...
        ValueError: invalid method for symbolic range

    Better success will be had when using integer symbols:

        >>> n = Symbol('n', integer=True)
        >>> r = Range(n, n + 20, 3)
        >>> r.inf
        n
        >>> pprint(r)
        {n, n + 3, ..., n + 18}
    """
    
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], range):
            raise TypeError('use sympify(%s) to convert range to Range' % args[0])
    # WARNING: Decompyle incomplete

    start = property((lambda self: self.args[0]))
    stop = property((lambda self: self.args[1]))
    step = property((lambda self: self.args[2]))
    reversed = (lambda self: if self.has(Symbol):
n = (self.stop - self.start) / self.stepif not n.is_extended_positive or (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
                raise ValueError('invalid method for symbolic range')
        if self.start == self.stop:
            return self
        return all.func(self.stop - self.step, self.start - self.step, -(self.step))
)()
    
    def _kind(self):
        return SetKind(NumberKind)

    
    def _contains(self, other):
        if self.start == self.stop:
            return S.false
        if None.is_infinite:
            return S.false
        if not None.is_integer:
            return tfn[other.is_integer]
        if None.has(Symbol):
            n = (self.stop - self.start) / self.step
            if not n.is_extended_positive or (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
                return None
        n = self.size
        if self.start.is_finite:
            ref = self.start
        elif self.stop.is_finite:
            ref = self.stop
        else:
            return S.true
        if all == 1:
            return Eq(other, self[0])
        res = (None - other) % self.step
        if res == S.Zero:
            if self.has(Symbol):
                d = Dummy('i')
                return self.as_relational(d).subs(d, other)
            return None(other >= self.inf, other <= self.sup)
        if None.is_Integer:
            return S.false

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    is_iterable = (lambda self: dif = self.stop - self.startn = dif / self.stepif not n.has(S.Infinity) and n.has(S.NegativeInfinity) and n.is_Integer:
Falseif None.start in (S.NegativeInfinity, S.Infinity):
Falseif not None.is_extended_nonnegative or (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return False
        return all
)()
    
    def __len__(self):
        rv = self.size
        if rv is S.Infinity:
            raise ValueError('Use .size to get the length of an infinite Range')
        return int(rv)

    size = (lambda self: if self.start == self.stop:
S.Zerodif = None.stop - self.startn = dif / self.stepif n.is_infinite:
S.Infinityif None.is_extended_nonnegative and (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
            return abs(floor(n))
        raise all('Invalid method for symbolic Range')
)()
    is_finite_set = (lambda self: if self.start.is_integer and self.stop.is_integer:
TrueNone.size.is_finite)()
    is_empty = (lambda self: try:
self.size.is_zeroexcept ValueError:
None)()
    
    def __bool__(self):
        b = is_eq(self.start, self.stop)
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, i):
        ooslice = 'cannot slice from the end with an infinite value'
        zerostep = 'slice step cannot be zero'
        infinite = 'slicing not possible on range with infinite start'
        ambiguous = 'cannot unambiguously re-stride from the end with an infinite value'
    # WARNING: Decompyle incomplete

    _inf = (lambda self: if not self:
S.EmptySet.infif None.has(Symbol):
if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
                dif = self.stop - self.start
                if self.step.is_positive and dif.is_positive:
                    return self.start
                if all.step.is_negative and dif.is_negative:
                    return self.stop - self.step
                raise None('invalid method for symbolic range')
        if self.step > 0:
            return self.start
        return all.stop - self.step
)()
    _sup = (lambda self: if not self:
S.EmptySet.supif None.has(Symbol):
if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.args()):
                dif = self.stop - self.start
                if self.step.is_positive and dif.is_positive:
                    return self.stop - self.step
                if all.step.is_negative and dif.is_negative:
                    return self.start
                raise None('invalid method for symbolic range')
        if self.step > 0:
            return self.stop - self.step
        return all.start
)()
    _boundary = (lambda self: self)()
    
    def as_relational(self, x):
        '''Rewrite a Range in terms of equalities and logic operators. '''
        pass
    # WARNING: Decompyle incomplete



_sympy_converter[range] = lambda r: Range(r.start, r.stop, r.step)

def normalize_theta_set(theta):
    '''
    Normalize a Real Set `theta` in the interval `[0, 2\\pi)`. It returns
    a normalized value of theta in the Set. For Interval, a maximum of
    one cycle $[0, 2\\pi]$, is returned i.e. for theta equal to $[0, 10\\pi]$,
    returned normalized value would be $[0, 2\\pi)$. As of now intervals
    with end points as non-multiples of ``pi`` is not supported.

    Raises
    ======

    NotImplementedError
        The algorithms for Normalizing theta Set are not yet
        implemented.
    ValueError
        The input is not valid, i.e. the input is not a real set.
    RuntimeError
        It is a bug, please report to the github issue tracker.

    Examples
    ========

    >>> from sympy.sets.fancysets import normalize_theta_set
    >>> from sympy import Interval, FiniteSet, pi
    >>> normalize_theta_set(Interval(9*pi/2, 5*pi))
    Interval(pi/2, pi)
    >>> normalize_theta_set(Interval(-3*pi/2, pi/2))
    Interval.Ropen(0, 2*pi)
    >>> normalize_theta_set(Interval(-pi/2, pi/2))
    Union(Interval(0, pi/2), Interval.Ropen(3*pi/2, 2*pi))
    >>> normalize_theta_set(Interval(-4*pi, 3*pi))
    Interval.Ropen(0, 2*pi)
    >>> normalize_theta_set(Interval(-3*pi/2, -pi/2))
    Interval(pi/2, 3*pi/2)
    >>> normalize_theta_set(FiniteSet(0, pi, 3*pi))
    {0, pi}

    '''
    _pi_coeff = _pi_coeff
    import sympy.functions.elementary.trigonometric
# WARNING: Decompyle incomplete


class ComplexRegion(Set):
    '''
    Represents the Set of all Complex Numbers. It can represent a
    region of Complex Plane in both the standard forms Polar and
    Rectangular coordinates.

    * Polar Form
      Input is in the form of the ProductSet or Union of ProductSets
      of the intervals of ``r`` and ``theta``, and use the flag ``polar=True``.

      .. math:: Z = \\{z \\in \\mathbb{C} \\mid z = r\\times (\\cos(\\theta) + I\\sin(\\theta)), r \\in [\\texttt{r}], \\theta \\in [\\texttt{theta}]\\}

    * Rectangular Form
      Input is in the form of the ProductSet or Union of ProductSets
      of interval of x and y, the real and imaginary parts of the Complex numbers in a plane.
      Default input type is in rectangular form.

    .. math:: Z = \\{z \\in \\mathbb{C} \\mid z = x + Iy, x \\in [\\operatorname{re}(z)], y \\in [\\operatorname{im}(z)]\\}

    Examples
    ========

    >>> from sympy import ComplexRegion, Interval, S, I, Union
    >>> a = Interval(2, 3)
    >>> b = Interval(4, 6)
    >>> c1 = ComplexRegion(a*b)  # Rectangular Form
    >>> c1
    CartesianComplexRegion(ProductSet(Interval(2, 3), Interval(4, 6)))

    * c1 represents the rectangular region in complex plane
      surrounded by the coordinates (2, 4), (3, 4), (3, 6) and
      (2, 6), of the four vertices.

    >>> c = Interval(1, 8)
    >>> c2 = ComplexRegion(Union(a*b, b*c))
    >>> c2
    CartesianComplexRegion(Union(ProductSet(Interval(2, 3), Interval(4, 6)), ProductSet(Interval(4, 6), Interval(1, 8))))

    * c2 represents the Union of two rectangular regions in complex
      plane. One of them surrounded by the coordinates of c1 and
      other surrounded by the coordinates (4, 1), (6, 1), (6, 8) and
      (4, 8).

    >>> 2.5 + 4.5*I in c1
    True
    >>> 2.5 + 6.5*I in c1
    False

    >>> r = Interval(0, 1)
    >>> theta = Interval(0, 2*S.Pi)
    >>> c2 = ComplexRegion(r*theta, polar=True)  # Polar Form
    >>> c2  # unit Disk
    PolarComplexRegion(ProductSet(Interval(0, 1), Interval.Ropen(0, 2*pi)))

    * c2 represents the region in complex plane inside the
      Unit Disk centered at the origin.

    >>> 0.5 + 0.5*I in c2
    True
    >>> 1 + 2*I in c2
    False

    >>> unit_disk = ComplexRegion(Interval(0, 1)*Interval(0, 2*S.Pi), polar=True)
    >>> upper_half_unit_disk = ComplexRegion(Interval(0, 1)*Interval(0, S.Pi), polar=True)
    >>> intersection = unit_disk.intersect(upper_half_unit_disk)
    >>> intersection
    PolarComplexRegion(ProductSet(Interval(0, 1), Interval(0, pi)))
    >>> intersection == upper_half_unit_disk
    True

    See Also
    ========

    CartesianComplexRegion
    PolarComplexRegion
    Complexes

    '''
    is_ComplexRegion = True
    
    def __new__(cls, sets, polar = (False,)):
        if polar is False:
            return CartesianComplexRegion(sets)
        if None is True:
            return PolarComplexRegion(sets)
        raise None('polar should be either True or False')

    sets = (lambda self: self.args[0])()
    psets = (lambda self: if self.sets.is_ProductSet:
psets = ()psets = psets + (self.sets,)else:
psets = self.sets.argspsets)()
    a_interval = (lambda self: a_interval = []# WARNING: Decompyle incomplete
)()
    b_interval = (lambda self: b_interval = []# WARNING: Decompyle incomplete
)()
    _measure = (lambda self: self.sets._measure)()
    
    def _kind(self):
        return self.args[0].kind

    from_real = (lambda cls, sets: if not sets.is_subset(S.Reals):
raise ValueError('sets must be a subset of the real line')CartesianComplexRegion(sets * FiniteSet(0)))()
    
    def _contains(self, other):
        pass
    # WARNING: Decompyle incomplete



class CartesianComplexRegion(ComplexRegion):
    '''
    Set representing a square region of the complex plane.

    .. math:: Z = \\{z \\in \\mathbb{C} \\mid z = x + Iy, x \\in [\\operatorname{re}(z)], y \\in [\\operatorname{im}(z)]\\}

    Examples
    ========

    >>> from sympy import ComplexRegion, I, Interval
    >>> region = ComplexRegion(Interval(1, 3) * Interval(4, 6))
    >>> 2 + 5*I in region
    True
    >>> 5*I in region
    False

    See also
    ========

    ComplexRegion
    PolarComplexRegion
    Complexes
    '''
    polar = False
    variables = symbols('x, y', cls = Dummy)
    
    def __new__(cls, sets):
        if sets == S.Reals * S.Reals:
            return S.Complexes
    # WARNING: Decompyle incomplete

    expr = (lambda self: (x, y) = self.variablesx + S.ImaginaryUnit * y)()


class PolarComplexRegion(ComplexRegion):
    '''
    Set representing a polar region of the complex plane.

    .. math:: Z = \\{z \\in \\mathbb{C} \\mid z = r\\times (\\cos(\\theta) + I\\sin(\\theta)), r \\in [\\texttt{r}], \\theta \\in [\\texttt{theta}]\\}

    Examples
    ========

    >>> from sympy import ComplexRegion, Interval, oo, pi, I
    >>> rset = Interval(0, oo)
    >>> thetaset = Interval(0, pi)
    >>> upper_half_plane = ComplexRegion(rset * thetaset, polar=True)
    >>> 1 + I in upper_half_plane
    True
    >>> 1 - I in upper_half_plane
    False

    See also
    ========

    ComplexRegion
    CartesianComplexRegion
    Complexes

    '''
    polar = True
    variables = symbols('r, theta', cls = Dummy)
    
    def __new__(cls, sets):
        new_sets = []
        if not sets.is_ProductSet:
            for k in sets.args:
                new_sets.append(k)
        new_sets.append(sets)
    # WARNING: Decompyle incomplete

    expr = (lambda self: (r, theta) = self.variablesr * (cos(theta) + S.ImaginaryUnit * sin(theta)))()


def Complexes():
    '''Complexes'''
    __doc__ = '\n    The :class:`Set` of all complex numbers\n\n    Examples\n    ========\n\n    >>> from sympy import S, I\n    >>> S.Complexes\n    Complexes\n    >>> 1 + I in S.Complexes\n    True\n\n    See also\n    ========\n\n    Reals\n    ComplexRegion\n\n    '
    is_empty = False
    is_finite_set = False
    sets = (lambda self: ProductSet(S.Reals, S.Reals))()
    
    def __new__(cls):
        return Set.__new__(cls)


Complexes = <NODE:27>(Complexes, 'Complexes', CartesianComplexRegion, metaclass = Singleton)
