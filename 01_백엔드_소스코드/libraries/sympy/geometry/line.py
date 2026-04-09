# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: line.pyc (Python 3.11)

'''Line-like geometrical entities.

Contains
========
LinearEntity
Line
Ray
Segment
LinearEntity2D
Line2D
Ray2D
Segment2D
LinearEntity3D
Line3D
Ray3D
Segment3D

'''
from sympy.core.containers import Tuple
from sympy.core.evalf import N
from sympy.core.expr import Expr
from sympy.core.numbers import Rational, oo, Float
from sympy.core.relational import Eq
from sympy.core.singleton import S
from sympy.core.sorting import ordered
from sympy.core.symbol import _symbol, Dummy, uniquely_named_symbol
from sympy.core.sympify import sympify
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.elementary.trigonometric import _pi_coeff, acos, tan, atan2
from entity import GeometryEntity, GeometrySet
from exceptions import GeometryError
from point import Point, Point3D
from util import find, intersection
from sympy.logic.boolalg import And
from sympy.matrices import Matrix
from sympy.sets.sets import Intersection
from sympy.simplify.simplify import simplify
from sympy.solvers.solvers import solve
from sympy.solvers.solveset import linear_coeffs
from sympy.utilities.misc import Undecidable, filldedent
import random
(t, u) = range(2)()

class LinearEntity(GeometrySet):
    '''A base class for all linear entities (Line, Ray and Segment)
    in n-dimensional Euclidean space.

    Attributes
    ==========

    ambient_dimension
    direction
    length
    p1
    p2
    points

    Notes
    =====

    This is an abstract class and is not meant to be instantiated.

    See Also
    ========

    sympy.geometry.entity.GeometryEntity

    '''
    
    def __new__(cls, p1, p2 = (None,), **kwargs):
        (p1, p2) = Point._normalize_dimension(p1, p2)
        if p1 == p2:
            raise ValueError('%s.__new__ requires two unique Points.' % cls.__name__)
        if len(p1) != len(p2):
            raise ValueError('%s.__new__ requires two Points of equal dimension.' % cls.__name__)
    # WARNING: Decompyle incomplete

    
    def __contains__(self, other):
        '''Return a definitive answer or else raise an error if it cannot
        be determined that other is on the boundaries of self.'''
        result = self.contains(other)
    # WARNING: Decompyle incomplete

    
    def _span_test(self, other):
        """Test whether the point `other` lies in the positive span of `self`.
        A point x is 'in front' of a point y if x.dot(y) >= 0.  Return
        -1 if `other` is behind `self.p1`, 0 if `other` is `self.p1` and
        and 1 if `other` is in front of `self.p1`."""
        if self.p1 == other:
            return 0
        rel_pos = None - self.p1
        d = self.direction
        if d.dot(rel_pos) > 0:
            return 1

    ambient_dimension = (lambda self: len(self.p1))()
    
    def angle_between(l1, l2):
        '''Return the non-reflex angle formed by rays emanating from
        the origin with directions the same as the direction vectors
        of the linear entities.

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        angle : angle in radians

        Notes
        =====

        From the dot product of vectors v1 and v2 it is known that:

            ``dot(v1, v2) = |v1|*|v2|*cos(A)``

        where A is the angle formed between the two vectors. We can
        get the directional vectors of the two lines and readily
        find the angle between the two using the above formula.

        See Also
        ========

        is_perpendicular, Ray2D.closing_angle

        Examples
        ========

        >>> from sympy import Line
        >>> e = Line((0, 0), (1, 0))
        >>> ne = Line((0, 0), (1, 1))
        >>> sw = Line((1, 1), (0, 0))
        >>> ne.angle_between(e)
        pi/4
        >>> sw.angle_between(e)
        3*pi/4

        To obtain the non-obtuse angle at the intersection of lines, use
        the ``smallest_angle_between`` method:

        >>> sw.smallest_angle_between(e)
        pi/4

        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(-1, 2, 0)
        >>> l1, l2 = Line3D(p1, p2), Line3D(p2, p3)
        >>> l1.angle_between(l2)
        acos(-sqrt(2)/3)
        >>> l1.smallest_angle_between(l2)
        acos(sqrt(2)/3)
        '''
        if not isinstance(l1, LinearEntity) and isinstance(l2, LinearEntity):
            raise TypeError('Must pass only LinearEntity objects')
        v2 = l2.direction
        v1 = l1.direction
        return acos(v1.dot(v2) / (abs(v1) * abs(v2)))

    
    def smallest_angle_between(l1, l2):
        '''Return the smallest angle formed at the intersection of the
        lines containing the linear entities.

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        angle : angle in radians

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(0, 4), Point(2, -2)
        >>> l1, l2 = Line(p1, p2), Line(p1, p3)
        >>> l1.smallest_angle_between(l2)
        pi/4

        See Also
        ========

        angle_between, is_perpendicular, Ray2D.closing_angle
        '''
        if not isinstance(l1, LinearEntity) and isinstance(l2, LinearEntity):
            raise TypeError('Must pass only LinearEntity objects')
        v2 = l2.direction
        v1 = l1.direction
        return acos(abs(v1.dot(v2)) / (abs(v1) * abs(v2)))

    
    def arbitrary_point(self, parameter = ('t',)):
        """A parameterized point on the Line.

        Parameters
        ==========

        parameter : str, optional
            The name of the parameter which will be used for the parametric
            point. The default value is 't'. When this parameter is 0, the
            first point used to define the line will be returned, and when
            it is 1 the second point will be returned.

        Returns
        =======

        point : Point

        Raises
        ======

        ValueError
            When ``parameter`` already appears in the Line's definition.

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(1, 0), Point(5, 3)
        >>> l1 = Line(p1, p2)
        >>> l1.arbitrary_point()
        Point2D(4*t + 1, 3*t)
        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(1, 0, 0), Point3D(5, 3, 1)
        >>> l1 = Line3D(p1, p2)
        >>> l1.arbitrary_point()
        Point3D(4*t + 1, 3*t, t)

        """
        t = _symbol(parameter, real = True)
        if (lambda .0: pass# WARNING: Decompyle incomplete
) in self.free_symbols():
            raise ValueError(filldedent('\n                Symbol %s already appears in object\n                and cannot be used as a parameter.\n                ' % t.name))
        return self.p1 + (self.p2 - self.p1) * t

    are_concurrent = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    def contains(self, other):
        '''Subclasses should implement this method and should return
            True if other is on the boundaries of self;
            False if not on the boundaries of self;
            None if a determination cannot be made.'''
        raise NotImplementedError()

    direction = (lambda self: self.p2 - self.p1)()
    
    def intersection(self, other):
        '''The intersection with another geometrical entity.

        Parameters
        ==========

        o : Point or LinearEntity

        Returns
        =======

        intersection : list of geometrical entities

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line, Segment
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(7, 7)
        >>> l1 = Line(p1, p2)
        >>> l1.intersection(p3)
        [Point2D(7, 7)]
        >>> p4, p5 = Point(5, 0), Point(0, 3)
        >>> l2 = Line(p4, p5)
        >>> l1.intersection(l2)
        [Point2D(15/8, 15/8)]
        >>> p6, p7 = Point(0, 5), Point(2, 6)
        >>> s1 = Segment(p6, p7)
        >>> l1.intersection(s1)
        []
        >>> from sympy import Point3D, Line3D, Segment3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(7, 7, 7)
        >>> l1 = Line3D(p1, p2)
        >>> l1.intersection(p3)
        [Point3D(7, 7, 7)]
        >>> l1 = Line3D(Point3D(4,19,12), Point3D(5,25,17))
        >>> l2 = Line3D(Point3D(-3, -15, -19), direction_ratio=[2,8,8])
        >>> l1.intersection(l2)
        [Point3D(1, 1, -3)]
        >>> p6, p7 = Point3D(0, 5, 2), Point3D(2, 6, 3)
        >>> s1 = Segment3D(p6, p7)
        >>> l1.intersection(s1)
        []

        '''
        
        def intersect_parallel_rays(ray1, ray2):
            if ray1.direction.dot(ray2.direction) > 0:
                return [
                    ray2] if ray1._span_test(ray2.p1) >= 0 else [
                    ray1]
            st = None._span_test(ray2.p1)
            if st < 0:
                return []
            if None == 0:
                return [
                    ray2.p1]
            return [
                None(ray1.p1, ray2.p1)]

        
        def intersect_parallel_ray_and_segment(ray, seg):
            st2 = ray._span_test(seg.p2)
            st1 = ray._span_test(seg.p1)
            if st1 < 0 and st2 < 0:
                return []
            if None >= 0 and st2 >= 0:
                return [
                    seg]
            if None >= 0:
                return [
                    Segment(ray.p1, seg.p1)]
            return [
                None(ray.p1, seg.p2)]

        
        def intersect_parallel_segments(seg1, seg2):
            if seg1.contains(seg2):
                return [
                    seg2]
            if None.contains(seg1):
                return [
                    seg1]
            if None.direction.dot(seg2.direction) < 0:
                seg2 = Segment(seg2.p2, seg2.p1)
            if seg1._span_test(seg2.p1) < 0:
                seg2 = seg1
                seg1 = seg2
            if seg2._span_test(seg1.p2) < 0:
                return []
            return [
                None(seg2.p1, seg1.p2)]

        if not isinstance(other, GeometryEntity):
            other = Point(other, dim = self.ambient_dimension)
        if other.is_Point:
            if self.contains(other):
                return [
                    other]
            return None
    # WARNING: Decompyle incomplete

    
    def is_parallel(l1, l2):
        '''Are two linear entities parallel?

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        True : if l1 and l2 are parallel,
        False : otherwise.

        See Also
        ========

        coefficients

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> p3, p4 = Point(3, 4), Point(6, 7)
        >>> l1, l2 = Line(p1, p2), Line(p3, p4)
        >>> Line.is_parallel(l1, l2)
        True
        >>> p5 = Point(6, 6)
        >>> l3 = Line(p3, p5)
        >>> Line.is_parallel(l1, l3)
        False
        >>> from sympy import Point3D, Line3D
        >>> p1, p2 = Point3D(0, 0, 0), Point3D(3, 4, 5)
        >>> p3, p4 = Point3D(2, 1, 1), Point3D(8, 9, 11)
        >>> l1, l2 = Line3D(p1, p2), Line3D(p3, p4)
        >>> Line3D.is_parallel(l1, l2)
        True
        >>> p5 = Point3D(6, 6, 6)
        >>> l3 = Line3D(p3, p5)
        >>> Line3D.is_parallel(l1, l3)
        False

        '''
        if not isinstance(l1, LinearEntity) and isinstance(l2, LinearEntity):
            raise TypeError('Must pass only LinearEntity objects')
        return l1.direction.is_scalar_multiple(l2.direction)

    
    def is_perpendicular(l1, l2):
        '''Are two linear entities perpendicular?

        Parameters
        ==========

        l1 : LinearEntity
        l2 : LinearEntity

        Returns
        =======

        True : if l1 and l2 are perpendicular,
        False : otherwise.

        See Also
        ========

        coefficients

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(-1, 1)
        >>> l1, l2 = Line(p1, p2), Line(p1, p3)
        >>> l1.is_perpendicular(l2)
        True
        >>> p4 = Point(5, 3)
        >>> l3 = Line(p1, p4)
        >>> l1.is_perpendicular(l3)
        False
        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(-1, 2, 0)
        >>> l1, l2 = Line3D(p1, p2), Line3D(p2, p3)
        >>> l1.is_perpendicular(l2)
        False
        >>> p4 = Point3D(5, 3, 7)
        >>> l3 = Line3D(p1, p4)
        >>> l1.is_perpendicular(l3)
        False

        '''
        if not isinstance(l1, LinearEntity) and isinstance(l2, LinearEntity):
            raise TypeError('Must pass only LinearEntity objects')
        return S.Zero.equals(l1.direction.dot(l2.direction))

    
    def is_similar(self, other):
        '''
        Return True if self and other are contained in the same line.

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 1), Point(3, 4), Point(2, 3)
        >>> l1 = Line(p1, p2)
        >>> l2 = Line(p1, p3)
        >>> l1.is_similar(l2)
        True
        '''
        l = Line(self.p1, self.p2)
        return l.contains(other)

    length = (lambda self: S.Infinity)()
    p1 = (lambda self: self.args[0])()
    p2 = (lambda self: self.args[1])()
    
    def parallel_line(self, p):
        '''Create a new Line parallel to this linear entity which passes
        through the point `p`.

        Parameters
        ==========

        p : Point

        Returns
        =======

        line : Line

        See Also
        ========

        is_parallel

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(2, 3), Point(-2, 2)
        >>> l1 = Line(p1, p2)
        >>> l2 = l1.parallel_line(p3)
        >>> p3 in l2
        True
        >>> l1.is_parallel(l2)
        True
        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(2, 3, 4), Point3D(-2, 2, 0)
        >>> l1 = Line3D(p1, p2)
        >>> l2 = l1.parallel_line(p3)
        >>> p3 in l2
        True
        >>> l1.is_parallel(l2)
        True

        '''
        p = Point(p, dim = self.ambient_dimension)
        return Line(p, p + self.direction)

    
    def perpendicular_line(self, p):
        '''Create a new Line perpendicular to this linear entity which passes
        through the point `p`.

        Parameters
        ==========

        p : Point

        Returns
        =======

        line : Line

        See Also
        ========

        sympy.geometry.line.LinearEntity.is_perpendicular, perpendicular_segment

        Examples
        ========

        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(2, 3, 4), Point3D(-2, 2, 0)
        >>> L = Line3D(p1, p2)
        >>> P = L.perpendicular_line(p3); P
        Line3D(Point3D(-2, 2, 0), Point3D(4/29, 6/29, 8/29))
        >>> L.is_perpendicular(P)
        True

        In 3D the, the first point used to define the line is the point
        through which the perpendicular was required to pass; the
        second point is (arbitrarily) contained in the given line:

        >>> P.p2 in L
        True
        '''
        p = Point(p, dim = self.ambient_dimension)
        if p in self:
            p = p + self.direction.orthogonal_direction
        return Line(p, self.projection(p))

    
    def perpendicular_segment(self, p):
        '''Create a perpendicular line segment from `p` to this line.

        The endpoints of the segment are ``p`` and the closest point in
        the line containing self. (If self is not a line, the point might
        not be in self.)

        Parameters
        ==========

        p : Point

        Returns
        =======

        segment : Segment

        Notes
        =====

        Returns `p` itself if `p` is on this linear entity.

        See Also
        ========

        perpendicular_line

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(0, 2)
        >>> l1 = Line(p1, p2)
        >>> s1 = l1.perpendicular_segment(p3)
        >>> l1.is_perpendicular(s1)
        True
        >>> p3 in s1
        True
        >>> l1.perpendicular_segment(Point(4, 0))
        Segment2D(Point2D(4, 0), Point2D(2, 2))
        >>> from sympy import Point3D, Line3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(0, 2, 0)
        >>> l1 = Line3D(p1, p2)
        >>> s1 = l1.perpendicular_segment(p3)
        >>> l1.is_perpendicular(s1)
        True
        >>> p3 in s1
        True
        >>> l1.perpendicular_segment(Point3D(4, 0, 0))
        Segment3D(Point3D(4, 0, 0), Point3D(4/3, 4/3, 4/3))

        '''
        p = Point(p, dim = self.ambient_dimension)
        if p in self:
            return p
        l = None.perpendicular_line(p)
        (p2,) = Intersection(Line(self.p1, self.p2), l)
        return Segment(p, p2)

    points = (lambda self: (self.p1, self.p2))()
    
    def projection(self, other):
        '''Project a point, line, ray, or segment onto this linear entity.

        Parameters
        ==========

        other : Point or LinearEntity (Line, Ray, Segment)

        Returns
        =======

        projection : Point or LinearEntity (Line, Ray, Segment)
            The return type matches the type of the parameter ``other``.

        Raises
        ======

        GeometryError
            When method is unable to perform projection.

        Notes
        =====

        A projection involves taking the two points that define
        the linear entity and projecting those points onto a
        Line and then reforming the linear entity using these
        projections.
        A point P is projected onto a line L by finding the point
        on L that is closest to P. This point is the intersection
        of L and the line perpendicular to L that passes through P.

        See Also
        ========

        sympy.geometry.point.Point, perpendicular_line

        Examples
        ========

        >>> from sympy import Point, Line, Segment, Rational
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(Rational(1, 2), 0)
        >>> l1 = Line(p1, p2)
        >>> l1.projection(p3)
        Point2D(1/4, 1/4)
        >>> p4, p5 = Point(10, 0), Point(12, 1)
        >>> s1 = Segment(p4, p5)
        >>> l1.projection(s1)
        Segment2D(Point2D(5, 5), Point2D(13/2, 13/2))
        >>> p1, p2, p3 = Point(0, 0, 1), Point(1, 1, 2), Point(2, 0, 1)
        >>> l1 = Line(p1, p2)
        >>> l1.projection(p3)
        Point3D(2/3, 2/3, 5/3)
        >>> p4, p5 = Point(10, 0, 1), Point(12, 1, 3)
        >>> s1 = Segment(p4, p5)
        >>> l1.projection(s1)
        Segment3D(Point3D(10/3, 10/3, 13/3), Point3D(5, 5, 6))

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def random_point(self, seed = (None,)):
        '''A random point on a LinearEntity.

        Returns
        =======

        point : Point

        See Also
        ========

        sympy.geometry.point.Point

        Examples
        ========

        >>> from sympy import Point, Line, Ray, Segment
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> line = Line(p1, p2)
        >>> r = line.random_point(seed=42)  # seed value is optional
        >>> r.n(3)
        Point2D(-0.72, -0.432)
        >>> r in line
        True
        >>> Ray(p1, p2).random_point(seed=42).n(3)
        Point2D(0.72, 0.432)
        >>> Segment(p1, p2).random_point(seed=42).n(3)
        Point2D(3.2, 1.92)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def bisectors(self, other):
        '''Returns the perpendicular lines which pass through the intersections
        of self and other that are in the same plane.

        Parameters
        ==========

        line : Line3D

        Returns
        =======

        list: two Line instances

        Examples
        ========

        >>> from sympy import Point3D, Line3D
        >>> r1 = Line3D(Point3D(0, 0, 0), Point3D(1, 0, 0))
        >>> r2 = Line3D(Point3D(0, 0, 0), Point3D(0, 1, 0))
        >>> r1.bisectors(r2)
        [Line3D(Point3D(0, 0, 0), Point3D(1, 1, 0)), Line3D(Point3D(0, 0, 0), Point3D(1, -1, 0))]

        '''
        if not isinstance(other, LinearEntity):
            raise GeometryError('Expecting LinearEntity, not %s' % other)
        l2 = other
        l1 = self
        if l1.p1.ambient_dimension != l2.p1.ambient_dimension:
            if isinstance(l1, Line2D):
                l2 = l1
                l1 = l2
            (_, p1) = Point._normalize_dimension(l1.p1, l2.p1, on_morph = 'ignore')
            (_, p2) = Point._normalize_dimension(l1.p2, l2.p2, on_morph = 'ignore')
            l2 = Line(p1, p2)
        point = intersection(l1, l2)
        if not point:
            raise GeometryError('The lines do not intersect')
        pt = point[0]
        if isinstance(pt, Line):
            return [
                self]
        d1 = None.direction.unit
        d2 = l2.direction.unit
        bis1 = Line(pt, pt + d1 + d2)
        bis2 = Line(pt, pt + d1 - d2)
        return [
            bis1,
            bis2]



class Line(LinearEntity):
    """An infinite line in space.

    A 2D line is declared with two distinct points, point and slope, or
    an equation. A 3D line may be defined with a point and a direction ratio.

    Parameters
    ==========

    p1 : Point
    p2 : Point
    slope : SymPy expression
    direction_ratio : list
    equation : equation of a line

    Notes
    =====

    `Line` will automatically subclass to `Line2D` or `Line3D` based
    on the dimension of `p1`.  The `slope` argument is only relevant
    for `Line2D` and the `direction_ratio` argument is only relevant
    for `Line3D`.

    The order of the points will define the direction of the line
    which is used when calculating the angle between lines.

    See Also
    ========

    sympy.geometry.point.Point
    sympy.geometry.line.Line2D
    sympy.geometry.line.Line3D

    Examples
    ========

    >>> from sympy import Line, Segment, Point, Eq
    >>> from sympy.abc import x, y, a, b

    >>> L = Line(Point(2,3), Point(3,5))
    >>> L
    Line2D(Point2D(2, 3), Point2D(3, 5))
    >>> L.points
    (Point2D(2, 3), Point2D(3, 5))
    >>> L.equation()
    -2*x + y + 1
    >>> L.coefficients
    (-2, 1, 1)

    Instantiate with keyword ``slope``:

    >>> Line(Point(0, 0), slope=0)
    Line2D(Point2D(0, 0), Point2D(1, 0))

    Instantiate with another linear object

    >>> s = Segment((0, 0), (0, 1))
    >>> Line(s).equation()
    x

    The line corresponding to an equation in the for `ax + by + c = 0`,
    can be entered:

    >>> Line(3*x + y + 18)
    Line2D(Point2D(0, -18), Point2D(1, -21))

    If `x` or `y` has a different name, then they can be specified, too,
    as a string (to match the name) or symbol:

    >>> Line(Eq(3*a + b, -18), x='a', y=b)
    Line2D(Point2D(0, -18), Point2D(1, -21))
    """
    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def contains(self, other):
        '''
        Return True if `other` is on this Line, or False otherwise.

        Examples
        ========

        >>> from sympy import Line,Point
        >>> p1, p2 = Point(0, 1), Point(3, 4)
        >>> l = Line(p1, p2)
        >>> l.contains(p1)
        True
        >>> l.contains((0, 1))
        True
        >>> l.contains((0, 0))
        False
        >>> a = (0, 0, 0)
        >>> b = (1, 1, 1)
        >>> c = (2, 2, 2)
        >>> l1 = Line(a, b)
        >>> l2 = Line(b, a)
        >>> l1 == l2
        False
        >>> l1 in l2
        True

        '''
        if not isinstance(other, GeometryEntity):
            other = Point(other, dim = self.ambient_dimension)
        if isinstance(other, Point):
            return Point.is_collinear(other, self.p1, self.p2)
        if None(other, LinearEntity):
            return Point.is_collinear(self.p1, self.p2, other.p1, other.p2)

    
    def distance(self, other):
        '''
        Finds the shortest distance between a line and a point.

        Raises
        ======

        NotImplementedError is raised if `other` is not a Point

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> s = Line(p1, p2)
        >>> s.distance(Point(-1, 1))
        sqrt(2)
        >>> s.distance((-1, 2))
        3*sqrt(2)/2
        >>> p1, p2 = Point(0, 0, 0), Point(1, 1, 1)
        >>> s = Line(p1, p2)
        >>> s.distance(Point(-1, 1, 1))
        2*sqrt(6)/3
        >>> s.distance((-1, 1, 1))
        2*sqrt(6)/3

        '''
        if not isinstance(other, GeometryEntity):
            other = Point(other, dim = self.ambient_dimension)
        if self.contains(other):
            return S.Zero
        return None.perpendicular_segment(other).length

    
    def equals(self, other):
        '''Returns True if self and other are the same mathematical entities'''
        if not isinstance(other, Line):
            return False
        return None.is_collinear(self.p1, other.p1, self.p2, other.p2)

    
    def plot_interval(self, parameter = ('t',)):
        """The plot interval for the default geometric plot of line. Gives
        values that will produce a line that is +/- 5 units long (where a
        unit is the distance between the two points that define the line).

        Parameters
        ==========

        parameter : str, optional
            Default value is 't'.

        Returns
        =======

        plot_interval : list (plot interval)
            [parameter, lower_bound, upper_bound]

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(0, 0), Point(5, 3)
        >>> l1 = Line(p1, p2)
        >>> l1.plot_interval()
        [t, -5, 5]

        """
        t = _symbol(parameter, real = True)
        return [
            t,
            -5,
            5]



class Ray(LinearEntity):
    '''A Ray is a semi-line in the space with a source point and a direction.

    Parameters
    ==========

    p1 : Point
        The source of the Ray
    p2 : Point or radian value
        This point determines the direction in which the Ray propagates.
        If given as an angle it is interpreted in radians with the positive
        direction being ccw.

    Attributes
    ==========

    source

    See Also
    ========

    sympy.geometry.line.Ray2D
    sympy.geometry.line.Ray3D
    sympy.geometry.point.Point
    sympy.geometry.line.Line

    Notes
    =====

    `Ray` will automatically subclass to `Ray2D` or `Ray3D` based on the
    dimension of `p1`.

    Examples
    ========

    >>> from sympy import Ray, Point, pi
    >>> r = Ray(Point(2, 3), Point(3, 5))
    >>> r
    Ray2D(Point2D(2, 3), Point2D(3, 5))
    >>> r.points
    (Point2D(2, 3), Point2D(3, 5))
    >>> r.source
    Point2D(2, 3)
    >>> r.xdirection
    oo
    >>> r.ydirection
    oo
    >>> r.slope
    2
    >>> Ray(Point(0, 0), angle=pi/4).slope
    1

    '''
    
    def __new__(cls, p1, p2 = (None,), **kwargs):
        p1 = Point(p1)
    # WARNING: Decompyle incomplete

    
    def _svg(self, scale_factor, fill_color = (1, '#66cc99')):
        '''Returns SVG path element for the LinearEntity.

        Parameters
        ==========

        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        fill_color : str, optional
            Hex string for fill color. Default is "#66cc99".
        '''
        verts = (N(self.p1), N(self.p2))
        coords = verts()
        path = 'M {} L {}'.format(coords[0], ' L '.join(coords[1:]))
        return '<path fill-rule="evenodd" fill="{2}" stroke="#555555" stroke-width="{0}" opacity="0.6" d="{1}" marker-start="url(#markerCircle)" marker-end="url(#markerArrow)"/>'.format(2 * scale_factor, path, fill_color)

    
    def contains(self, other):
