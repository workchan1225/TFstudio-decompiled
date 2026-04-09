# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parabola.pyc (Python 3.11)

'''Parabolic geometrical entity.

Contains
* Parabola

'''
from sympy.core import S
from sympy.core.sorting import ordered
from sympy.core.symbol import _symbol, symbols
from sympy.geometry.entity import GeometryEntity, GeometrySet
from sympy.geometry.point import Point, Point2D
from sympy.geometry.line import Line, Line2D, Ray2D, Segment2D, LinearEntity3D
from sympy.geometry.ellipse import Ellipse
from sympy.functions import sign
from sympy.simplify import simplify
from sympy.solvers.solvers import solve

class Parabola(GeometrySet):
    """A parabolic GeometryEntity.

    A parabola is declared with a point, that is called 'focus', and
    a line, that is called 'directrix'.
    Only vertical or horizontal parabolas are currently supported.

    Parameters
    ==========

    focus : Point
        Default value is Point(0, 0)
    directrix : Line

    Attributes
    ==========

    focus
    directrix
    axis of symmetry
    focal length
    p parameter
    vertex
    eccentricity

    Raises
    ======
    ValueError
        When `focus` is not a two dimensional point.
        When `focus` is a point of directrix.
    NotImplementedError
        When `directrix` is neither horizontal nor vertical.

    Examples
    ========

    >>> from sympy import Parabola, Point, Line
    >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7,8)))
    >>> p1.focus
    Point2D(0, 0)
    >>> p1.directrix
    Line2D(Point2D(5, 8), Point2D(7, 8))

    """
    
    def __new__(cls, focus, directrix = (None, None), **kwargs):
        if focus:
            focus = Point(focus, dim = 2)
        else:
            focus = Point(0, 0)
        directrix = Line(directrix)
        if directrix.contains(focus):
            raise ValueError('The focus must not be a point of directrix')
    # WARNING: Decompyle incomplete

    ambient_dimension = (lambda self: 2)()
    axis_of_symmetry = (lambda self: self.directrix.perpendicular_line(self.focus))()
    directrix = (lambda self: self.args[1])()
    eccentricity = (lambda self: S.One)()
    
    def equation(self, x, y = ('x', 'y')):
        """The equation of the parabola.

        Parameters
        ==========
        x : str, optional
            Label for the x-axis. Default value is 'x'.
        y : str, optional
            Label for the y-axis. Default value is 'y'.

        Returns
        =======
        equation : SymPy expression

        Examples
        ========

        >>> from sympy import Parabola, Point, Line
        >>> p1 = Parabola(Point(0, 0), Line(Point(5, 8), Point(7, 8)))
        >>> p1.equation()
        -x**2 - 16*y + 64
        >>> p1.equation('f')
        -f**2 - 16*y + 64
        >>> p1.equation(y='z')
        -x**2 - 16*z + 64

        """
        x = _symbol(x, real = True)
        y = _symbol(y, real = True)
        m = self.directrix.slope
        if m is S.Infinity:
            t1 = 4 * self.p_parameter * (x - self.vertex.x)
            t2 = (y - self.vertex.y) ** 2
        elif m == 0:
            t1 = 4 * self.p_parameter * (y - self.vertex.y)
            t2 = (x - self.vertex.x) ** 2
        else:
            (a, b) = self.focus
            (c, d) = self.directrix.coefficients[:2]
            t1 = (x - a) ** 2 + (y - b) ** 2
            t2 = self.directrix.equation(x, y) ** 2 / (c ** 2 + d ** 2)
        return t1 - t2

    focal_length = (lambda self: distance = self.directrix.distance(self.focus)focal_length = distance / 2focal_length)()
    focus = (lambda self: self.args[0])()
    
    def intersection(self, o):
        '''The intersection of the parabola and another geometrical entity `o`.

        Parameters
        ==========

        o : GeometryEntity, LinearEntity

        Returns
        =======

        intersection : list of GeometryEntity objects

        Examples
        ========

        >>> from sympy import Parabola, Point, Ellipse, Line, Segment
        >>> p1 = Point(0,0)
        >>> l1 = Line(Point(1, -2), Point(-1,-2))
        >>> parabola1 = Parabola(p1, l1)
        >>> parabola1.intersection(Ellipse(Point(0, 0), 2, 5))
        [Point2D(-2, 0), Point2D(2, 0)]
        >>> parabola1.intersection(Line(Point(-7, 3), Point(12, 3)))
        [Point2D(-4, 3), Point2D(4, 3)]
        >>> parabola1.intersection(Segment((-12, -65), (14, -68)))
        []

        '''
        pass
    # WARNING: Decompyle incomplete

    p_parameter = (lambda self: m = self.directrix.slopeif m is S.Infinity:
x = self.directrix.coefficients[2]p = sign(self.focus.args[0] + x)elif m == 0:
y = self.directrix.coefficients[2]p = sign(self.focus.args[1] + y)else:
d = self.directrix.projection(self.focus)p = sign(self.focus.x - d.x)p * self.focal_length)()
    vertex = (lambda self: focus = self.focusm = self.directrix.slopeif m is S.Infinity:
vertex = Point(focus.args[0] - self.p_parameter, focus.args[1])elif m == 0:
vertex = Point(focus.args[0], focus.args[1] - self.p_parameter)else:
vertex = self.axis_of_symmetry.intersection(self)[0]vertex)()
