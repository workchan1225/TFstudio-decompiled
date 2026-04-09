# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polygon.pyc (Python 3.11)

from sympy.core import Expr, S, oo, pi, sympify
from sympy.core.evalf import N
from sympy.core.sorting import default_sort_key, ordered
from sympy.core.symbol import _symbol, Dummy, Symbol
from sympy.functions.elementary.complexes import sign
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.elementary.trigonometric import cos, sin, tan
from ellipse import Circle
from entity import GeometryEntity, GeometrySet
from exceptions import GeometryError
from line import Line, Segment, Ray
from point import Point
from sympy.logic import And
from sympy.matrices import Matrix
from sympy.simplify.simplify import simplify
from sympy.solvers.solvers import solve
from sympy.utilities.iterables import has_dups, has_variety, uniq, rotate_left, least_rotation
from sympy.utilities.misc import as_int, func_name
from mpmath.libmp.libmpf import prec_to_dps
import warnings
(x, y, T) = range(3)()

class Polygon(GeometrySet):
    '''A two-dimensional polygon.

    A simple polygon in space. Can be constructed from a sequence of points
    or from a center, radius, number of sides and rotation angle.

    Parameters
    ==========

    vertices
        A sequence of points.

    n : int, optional
        If $> 0$, an n-sided RegularPolygon is created.
        Default value is $0$.

    Attributes
    ==========

    area
    angles
    perimeter
    vertices
    centroid
    sides

    Raises
    ======

    GeometryError
        If all parameters are not Points.

    See Also
    ========

    sympy.geometry.point.Point, sympy.geometry.line.Segment, Triangle

    Notes
    =====

    Polygons are treated as closed paths rather than 2D areas so
    some calculations can be be negative or positive (e.g., area)
    based on the orientation of the points.

    Any consecutive identical points are reduced to a single point
    and any points collinear and between two points will be removed
    unless they are needed to define an explicit intersection (see examples).

    A Triangle, Segment or Point will be returned when there are 3 or
    fewer points provided.

    Examples
    ========

    >>> from sympy import Polygon, pi
    >>> p1, p2, p3, p4, p5 = [(0, 0), (1, 0), (5, 1), (0, 1), (3, 0)]
    >>> Polygon(p1, p2, p3, p4)
    Polygon(Point2D(0, 0), Point2D(1, 0), Point2D(5, 1), Point2D(0, 1))
    >>> Polygon(p1, p2)
    Segment2D(Point2D(0, 0), Point2D(1, 0))
    >>> Polygon(p1, p2, p5)
    Segment2D(Point2D(0, 0), Point2D(3, 0))

    The area of a polygon is calculated as positive when vertices are
    traversed in a ccw direction. When the sides of a polygon cross the
    area will have positive and negative contributions. The following
    defines a Z shape where the bottom right connects back to the top
    left.

    >>> Polygon((0, 2), (2, 2), (0, 0), (2, 0)).area
    0

    When the keyword `n` is used to define the number of sides of the
    Polygon then a RegularPolygon is created and the other arguments are
    interpreted as center, radius and rotation. The unrotated RegularPolygon
    will always have a vertex at Point(r, 0) where `r` is the radius of the
    circle that circumscribes the RegularPolygon. Its method `spin` can be
    used to increment that angle.

    >>> p = Polygon((0,0), 1, n=3)
    >>> p
    RegularPolygon(Point2D(0, 0), 1, 3, 0)
    >>> p.vertices[0]
    Point2D(1, 0)
    >>> p.args[0]
    Point2D(0, 0)
    >>> p.spin(pi/2)
    >>> p.vertices[0]
    Point2D(0, 1)

    '''
    __slots__ = ()
    
    def __new__(cls = None, *, n, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    area = (lambda self: area = 0args = self.argsfor i in range(len(args)):
(x1, y1) = args[i - 1].args(x2, y2) = args[i].argsarea += x1 * y2 - x2 * y1simplify(area) / 2)()
    _is_clockwise = (lambda a, b, c: ba = b - aca = c - at_area = simplify(ba.x * ca.y - ca.x * ba.y)res = t_area.is_nonpositive# WARNING: Decompyle incomplete
)()
    angles = (lambda self: args = self.verticesn = len(args)ret = { }for i in range(n):
c = args[i]b = args[i - 1]a = args[i - 2]reflex_ang = Ray(b, a).angle_between(Ray(b, c))if self._is_clockwise(a, b, c):
ret[b] = 2 * S.Pi - reflex_angcontinueret[b] = reflex_angwrong = ((sum(ret.values()) / S.Pi - 1) / (n - 2) - 1).is_positiveif wrong:
two_pi = 2 * S.Pifor b in ret:
ret[b] = two_pi - ret[b]# WARNING: Decompyle incomplete
)()
    ambient_dimension = (lambda self: self.vertices[0].ambient_dimension)()
    perimeter = (lambda self: p = 0args = self.verticesfor i in range(len(args)):
p += args[i - 1].distance(args[i])simplify(p))()
    vertices = (lambda self: list(self.args))()
    centroid = (lambda self: A = 1 / (6 * self.area)(cx, cy) = (0, 0)args = self.argsfor i in range(len(args)):
(x1, y1) = args[i - 1].args(x2, y2) = args[i].argsv = x1 * y2 - x2 * y1cx += v * (x1 + x2)cy += v * (y1 + y2)Point(simplify(A * cx), simplify(A * cy)))()
    
    def second_moment_of_area(self, point = (None,)):
        '''Returns the second moment and product moment of area of a two dimensional polygon.

        Parameters
        ==========

        point : Point, two-tuple of sympifyable objects, or None(default=None)
            point is the point about which second moment of area is to be found.
            If "point=None" it will be calculated about the axis passing through the
            centroid of the polygon.

        Returns
        =======

        I_xx, I_yy, I_xy : number or SymPy expression
                           I_xx, I_yy are second moment of area of a two dimensional polygon.
                           I_xy is product moment of area of a two dimensional polygon.

        Examples
        ========

        >>> from sympy import Polygon, symbols
        >>> a, b = symbols(\'a, b\')
        >>> p1, p2, p3, p4, p5 = [(0, 0), (a, 0), (a, b), (0, b), (a/3, b/3)]
        >>> rectangle = Polygon(p1, p2, p3, p4)
        >>> rectangle.second_moment_of_area()
        (a*b**3/12, a**3*b/12, 0)
        >>> rectangle.second_moment_of_area(p5)
        (a*b**3/9, a**3*b/9, a**2*b**2/36)

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Second_moment_of_area

        '''
        (I_xx, I_yy, I_xy) = (0, 0, 0)
        args = self.vertices
    # WARNING: Decompyle incomplete

    
    def first_moment_of_area(self, point = (None,)):
        '''
        Returns the first moment of area of a two-dimensional polygon with
        respect to a certain point of interest.

        First moment of area is a measure of the distribution of the area
        of a polygon in relation to an axis. The first moment of area of
        the entire polygon about its own centroid is always zero. Therefore,
        here it is calculated for an area, above or below a certain point
        of interest, that makes up a smaller portion of the polygon. This
        area is bounded by the point of interest and the extreme end
        (top or bottom) of the polygon. The first moment for this area is
        is then determined about the centroidal axis of the initial polygon.

        References
        ==========

        .. [1] https://skyciv.com/docs/tutorials/section-tutorials/calculating-the-statical-or-first-moment-of-area-of-beam-sections/?cc=BMD
        .. [2] https://mechanicalc.com/reference/cross-sections

        Parameters
        ==========

        point: Point, two-tuple of sympifyable objects, or None (default=None)
            point is the point above or below which the area of interest lies
            If ``point=None`` then the centroid acts as the point of interest.

        Returns
        =======

        Q_x, Q_y: number or SymPy expressions
            Q_x is the first moment of area about the x-axis
            Q_y is the first moment of area about the y-axis
            A negative sign indicates that the section modulus is
            determined for a section below (or left of) the centroidal axis

        Examples
        ========

        >>> from sympy import Point, Polygon
        >>> a, b = 50, 10
        >>> p1, p2, p3, p4 = [(0, b), (0, 0), (a, 0), (a, b)]
        >>> p = Polygon(p1, p2, p3, p4)
        >>> p.first_moment_of_area()
        (625, 3125)
        >>> p.first_moment_of_area(point=Point(30, 7))
        (525, 3000)
        '''
        if point:
            (xc, yc) = self.centroid
        else:
            point = self.centroid
            (xc, yc) = point
        h_line = Line(point, slope = 0)
        v_line = Line(point, slope = S.Infinity)
        h_poly = self.cut_section(h_line)
        v_poly = self.cut_section(v_line)
        poly_1 = h_poly[0] if h_poly[0].area <= h_poly[1].area else h_poly[1]
        poly_2 = v_poly[0] if v_poly[0].area <= v_poly[1].area else v_poly[1]
        Q_x = (poly_1.centroid.y - yc) * poly_1.area
        Q_y = (poly_2.centroid.x - xc) * poly_2.area
        return (Q_x, Q_y)

    
    def polar_second_moment_of_area(self):
        """Returns the polar modulus of a two-dimensional polygon

        It is a constituent of the second moment of area, linked through
        the perpendicular axis theorem. While the planar second moment of
        area describes an object's resistance to deflection (bending) when
        subjected to a force applied to a plane parallel to the central
        axis, the polar second moment of area describes an object's
        resistance to deflection when subjected to a moment applied in a
        plane perpendicular to the object's central axis (i.e. parallel to
        the cross-section)

        Examples
        ========

        >>> from sympy import Polygon, symbols
        >>> a, b = symbols('a, b')
        >>> rectangle = Polygon((0, 0), (a, 0), (a, b), (0, b))
        >>> rectangle.polar_second_moment_of_area()
        a**3*b/12 + a*b**3/12

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Polar_moment_of_inertia

        """
        second_moment = self.second_moment_of_area()
        return second_moment[0] + second_moment[1]

    
    def section_modulus(self, point = (None,)):
        '''Returns a tuple with the section modulus of a two-dimensional
        polygon.

        Section modulus is a geometric property of a polygon defined as the
        ratio of second moment of area to the distance of the extreme end of
        the polygon from the centroidal axis.

        Parameters
        ==========

        point : Point, two-tuple of sympifyable objects, or None(default=None)
            point is the point at which section modulus is to be found.
            If "point=None" it will be calculated for the point farthest from the
            centroidal axis of the polygon.

        Returns
        =======

        S_x, S_y: numbers or SymPy expressions
                  S_x is the section modulus with respect to the x-axis
                  S_y is the section modulus with respect to the y-axis
                  A negative sign indicates that the section modulus is
                  determined for a point below the centroidal axis

        Examples
        ========

        >>> from sympy import symbols, Polygon, Point
        >>> a, b = symbols(\'a, b\', positive=True)
        >>> rectangle = Polygon((0, 0), (a, 0), (a, b), (0, b))
        >>> rectangle.section_modulus()
        (a*b**2/6, a**2*b/6)
        >>> rectangle.section_modulus(Point(a/4, b/4))
        (-a*b**2/3, -a**2*b/3)

        References
        ==========

        .. [1] https://en.wikipedia.org/wiki/Section_modulus

        '''
        (x_c, y_c) = self.centroid
    # WARNING: Decompyle incomplete

    sides = (lambda self: res = []args = self.verticesfor i in range(-len(args), 0):
res.append(Segment(args[i], args[i + 1]))res)()
    bounds = (lambda self: verts = self.verticesxs = verts()ys = verts()(min(xs), min(ys), max(xs), max(ys)))()
    
    def is_convex(self):
