# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: curve.pyc (Python 3.11)

'''Curves in 2-dimensional Euclidean space.

Contains
========
Curve

'''
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.core import diff
from sympy.core.containers import Tuple
from sympy.core.symbol import _symbol
from sympy.geometry.entity import GeometryEntity, GeometrySet
from sympy.geometry.point import Point
from sympy.integrals import integrate
from sympy.matrices import Matrix, rot_axis3
from sympy.utilities.iterables import is_sequence
from mpmath.libmp.libmpf import prec_to_dps

class Curve(GeometrySet):
    '''A curve in space.

    A curve is defined by parametric functions for the coordinates, a
    parameter and the lower and upper bounds for the parameter value.

    Parameters
    ==========

    function : list of functions
    limits : 3-tuple
        Function parameter and lower and upper bounds.

    Attributes
    ==========

    functions
    parameter
    limits

    Raises
    ======

    ValueError
        When `functions` are specified incorrectly.
        When `limits` are specified incorrectly.

    Examples
    ========

    >>> from sympy import Curve, sin, cos, interpolate
    >>> from sympy.abc import t, a
    >>> C = Curve((sin(t), cos(t)), (t, 0, 2))
    >>> C.functions
    (sin(t), cos(t))
    >>> C.limits
    (t, 0, 2)
    >>> C.parameter
    t
    >>> C = Curve((t, interpolate([1, 4, 9, 16], t)), (t, 0, 1)); C
    Curve((t, t**2), (t, 0, 1))
    >>> C.subs(t, 4)
    Point2D(4, 16)
    >>> C.arbitrary_point(a)
    Point2D(a, a**2)

    See Also
    ========

    sympy.core.function.Function
    sympy.polys.polyfuncs.interpolate

    '''
    
    def __new__(cls, function, limits):
        if is_sequence(function) or len(function) != 2:
            raise ValueError('Function argument should be (x(t), y(t)) but got %s' % str(function))
        if is_sequence(limits) or len(limits) != 3:
            raise ValueError('Limit argument should be (t, tmin, tmax) but got %s' % str(limits))
    # WARNING: Decompyle incomplete

    
    def __call__(self, f):
        return self.subs(self.parameter, f)

    
    def _eval_subs(self, old, new):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_evalf(self, prec = (15,), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def arbitrary_point(self, parameter = ('t',)):
        """A parameterized point on the curve.

        Parameters
        ==========

        parameter : str or Symbol, optional
            Default value is 't'.
            The Curve's parameter is selected with None or self.parameter
            otherwise the provided symbol is used.

        Returns
        =======

        Point :
            Returns a point in parametric form.

        Raises
        ======

        ValueError
            When `parameter` already appears in the functions.

        Examples
        ========

        >>> from sympy import Curve, Symbol
        >>> from sympy.abc import s
        >>> C = Curve([2*s, s**2], (s, 0, 2))
        >>> C.arbitrary_point()
        Point2D(2*t, t**2)
        >>> C.arbitrary_point(C.parameter)
        Point2D(2*s, s**2)
        >>> C.arbitrary_point(None)
        Point2D(2*s, s**2)
        >>> C.arbitrary_point(Symbol('a'))
        Point2D(2*a, a**2)

        See Also
        ========

        sympy.geometry.point.Point

        """
        pass
    # WARNING: Decompyle incomplete

    free_symbols = (lambda self: free = set()for a in self.functions + self.limits[1:]:
free |= a.free_symbolsfree = free.difference({
self.parameter})free)()
    ambient_dimension = (lambda self: len(self.args[0]))()
    functions = (lambda self: self.args[0])()
    limits = (lambda self: self.args[1])()
    parameter = (lambda self: self.args[1][0])()
    length = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def plot_interval(self, parameter = ('t',)):
        """The plot interval for the default geometric plot of the curve.

        Parameters
        ==========

        parameter : str or Symbol, optional
            Default value is 't';
            otherwise the provided symbol is used.

        Returns
        =======

        List :
            the plot interval as below:
                [parameter, lower_bound, upper_bound]

        Examples
        ========

        >>> from sympy import Curve, sin
        >>> from sympy.abc import x, s
        >>> Curve((x, sin(x)), (x, 1, 2)).plot_interval()
        [t, 1, 2]
        >>> Curve((x, sin(x)), (x, 1, 2)).plot_interval(s)
        [s, 1, 2]

        See Also
        ========

        limits : Returns limits of the parameter interval

        """
        t = _symbol(parameter, self.parameter, real = True)
        return [
            t] + list(self.limits[1:])

    
    def rotate(self, angle, pt = (0, None)):
        '''This function is used to rotate a curve along given point ``pt`` at given angle(in radian).

        Parameters
        ==========

        angle :
            the angle at which the curve will be rotated(in radian) in counterclockwise direction.
            default value of angle is 0.

        pt : Point
            the point along which the curve will be rotated.
            If no point given, the curve will be rotated around origin.

        Returns
        =======

        Curve :
            returns a curve rotated at given angle along given point.

        Examples
        ========

        >>> from sympy import Curve, pi
        >>> from sympy.abc import x
        >>> Curve((x, x), (x, 0, 1)).rotate(pi/2)
        Curve((-x, x), (x, 0, 1))

        '''
        if pt:
            pt = -Point(pt, dim = 2)
        else:
            pt = Point(0, 0)
    # WARNING: Decompyle incomplete

    
    def scale(self, x, y, pt = (1, 1, None)):
        '''Override GeometryEntity.scale since Curve is not made up of Points.

        Returns
        =======

        Curve :
            returns scaled curve.

        Examples
        ========

        >>> from sympy import Curve
        >>> from sympy.abc import x
        >>> Curve((x, x), (x, 0, 1)).scale(2)
        Curve((2*x, x), (x, 0, 1))

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def translate(self, x, y = (0, 0)):
        '''Translate the Curve by (x, y).

        Returns
        =======

        Curve :
            returns a translated curve.

        Examples
        ========

        >>> from sympy import Curve
        >>> from sympy.abc import x
        >>> Curve((x, x), (x, 0, 1)).translate(1, 2)
        Curve((x + 1, x + 2), (x, 0, 1))

        '''
        (fx, fy) = self.functions
        return self.func((fx + x, fy + y), self.limits)
