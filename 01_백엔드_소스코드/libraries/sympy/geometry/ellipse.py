# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ellipse.pyc (Python 3.11)

'''Elliptical geometrical entities.

Contains
* Ellipse
* Circle

'''
from sympy.core.expr import Expr
from sympy.core.relational import Eq
from sympy.core import S, pi, sympify
from sympy.core.evalf import N
from sympy.core.parameters import global_parameters
from sympy.core.logic import fuzzy_bool
from sympy.core.numbers import Rational, oo
from sympy.core.sorting import ordered
from sympy.core.symbol import Dummy, uniquely_named_symbol, _symbol
from sympy.simplify import simplify, trigsimp
from sympy.functions.elementary.miscellaneous import sqrt, Max
from sympy.functions.elementary.trigonometric import cos, sin
from sympy.functions.special.elliptic_integrals import elliptic_e
from entity import GeometryEntity, GeometrySet
from exceptions import GeometryError
from line import Line, Segment, Ray2D, Segment2D, Line2D, LinearEntity3D
from point import Point, Point2D, Point3D
from util import idiff, find
from sympy.polys import DomainError, Poly, PolynomialError
from sympy.polys.polyutils import _not_a_coeff, _nsort
from sympy.solvers import solve
from sympy.solvers.solveset import linear_coeffs
from sympy.utilities.misc import filldedent, func_name
from mpmath.libmp.libmpf import prec_to_dps
import random
(x, y) = range(2)()

class Ellipse(GeometrySet):
    pass
# WARNING: Decompyle incomplete


class Circle(Ellipse):
    """A circle in space.

    Constructed simply from a center and a radius, from three
    non-collinear points, or the equation of a circle.

    Parameters
    ==========

    center : Point
    radius : number or SymPy expression
    points : sequence of three Points
    equation : equation of a circle

    Attributes
    ==========

    radius (synonymous with hradius, vradius, major and minor)
    circumference
    equation

    Raises
    ======

    GeometryError
        When the given equation is not that of a circle.
        When trying to construct circle from incorrect parameters.

    See Also
    ========

    Ellipse, sympy.geometry.point.Point

    Examples
    ========

    >>> from sympy import Point, Circle, Eq
    >>> from sympy.abc import x, y, a, b

    A circle constructed from a center and radius:

    >>> c1 = Circle(Point(0, 0), 5)
    >>> c1.hradius, c1.vradius, c1.radius
    (5, 5, 5)

    A circle constructed from three points:

    >>> c2 = Circle(Point(0, 0), Point(1, 1), Point(1, 0))
    >>> c2.hradius, c2.vradius, c2.radius, c2.center
    (sqrt(2)/2, sqrt(2)/2, sqrt(2)/2, Point2D(1/2, 1/2))

    A circle can be constructed from an equation in the form
    `a*x**2 + by**2 + gx + hy + c = 0`, too:

    >>> Circle(x**2 + y**2 - 25)
    Circle(Point2D(0, 0), 5)

    If the variables corresponding to x and y are named something
    else, their name or symbol can be supplied:

    >>> Circle(Eq(a**2 + b**2, 25), x='a', y=b)
    Circle(Point2D(0, 0), 5)
    """
    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _eval_evalf(self, prec = (15,), **options):
        (pt, r) = self.args
        dps = prec_to_dps(prec)
    # WARNING: Decompyle incomplete

    circumference = (lambda self: 2 * S.Pi * self.radius)()
    
    def equation(self, x, y = ('x', 'y')):
        """The equation of the circle.

        Parameters
        ==========

        x : str or Symbol, optional
            Default value is 'x'.
        y : str or Symbol, optional
            Default value is 'y'.

        Returns
        =======

        equation : SymPy expression

        Examples
        ========

        >>> from sympy import Point, Circle
        >>> c1 = Circle(Point(0, 0), 5)
        >>> c1.equation()
        x**2 + y**2 - 25

        """
        x = _symbol(x, real = True)
        y = _symbol(y, real = True)
        t1 = (x - self.center.x) ** 2
        t2 = (y - self.center.y) ** 2
        return t1 + t2 - self.major ** 2

    
    def intersection(self, o):
        '''The intersection of this circle with another geometrical entity.

        Parameters
        ==========

        o : GeometryEntity

        Returns
        =======

        intersection : list of GeometryEntities

        Examples
        ========

        >>> from sympy import Point, Circle, Line, Ray
        >>> p1, p2, p3 = Point(0, 0), Point(5, 5), Point(6, 0)
        >>> p4 = Point(5, 0)
        >>> c1 = Circle(p1, 5)
        >>> c1.intersection(p2)
        []
        >>> c1.intersection(p4)
        [Point2D(5, 0)]
        >>> c1.intersection(Ray(p1, p2))
        [Point2D(5*sqrt(2)/2, 5*sqrt(2)/2)]
        >>> c1.intersection(Line(p2, p3))
        []

        '''
        return Ellipse.intersection(self, o)

    radius = (lambda self: self.args[1])()
    
    def reflect(self, line):
        '''Override GeometryEntity.reflect since the radius
        is not a GeometryEntity.

        Examples
        ========

        >>> from sympy import Circle, Line
        >>> Circle((0, 1), 1).reflect(Line((0, 0), (1, 1)))
        Circle(Point2D(1, 0), -1)
        '''
        c = self.center
        c = c.reflect(line)
        return self.func(c, -(self.radius))

    
    def scale(self, x, y, pt = (1, 1, None)):
        '''Override GeometryEntity.scale since the radius
        is not a GeometryEntity.

        Examples
        ========

        >>> from sympy import Circle
        >>> Circle((0, 0), 1).scale(2, 2)
        Circle(Point2D(0, 0), 2)
        >>> Circle((0, 0), 1).scale(2, 4)
        Ellipse(Point2D(0, 0), 2, 4)
        '''
        c = self.center
    # WARNING: Decompyle incomplete

    vradius = (lambda self: abs(self.radius))()

from polygon import Polygon, Triangle
