# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: entity.pyc (Python 3.11)

'''The definition of the base geometrical entity with attributes common to
all derived geometrical entities.

Contains
========

GeometryEntity
GeometricSet

Notes
=====

A GeometryEntity is any object that has special geometric properties.
A GeometrySet is a superclass of any GeometryEntity that can also
be viewed as a sympy.sets.Set.  In particular, points are the only
GeometryEntity not considered a Set.

Rn is a GeometrySet representing n-dimensional Euclidean space. R2 and
R3 are currently the only ambient spaces implemented.

'''
from __future__ import annotations
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.evalf import EvalfMixin, N
from sympy.core.numbers import oo
from sympy.core.symbol import Dummy
from sympy.core.sympify import sympify
from sympy.functions.elementary.trigonometric import cos, sin, atan
from sympy.matrices import eye
from sympy.multipledispatch import dispatch
from sympy.printing import sstr
from sympy.sets import Set, Union, FiniteSet
from sympy.sets.handlers.intersection import intersection_sets
from sympy.sets.handlers.union import union_sets
from sympy.solvers.solvers import solve
from sympy.utilities.misc import func_name
from sympy.utilities.iterables import is_sequence
ordering_of_classes = [
    'Point2D',
    'Point3D',
    'Point',
    'Segment2D',
    'Ray2D',
    'Line2D',
    'Segment3D',
    'Line3D',
    'Ray3D',
    'Segment',
    'Ray',
    'Line',
    'Plane',
    'Triangle',
    'RegularPolygon',
    'Polygon',
    'Circle',
    'Ellipse',
    'Curve',
    'Parabola']
(x, y) = range(2)()
T = Dummy('entity_dummy', real = True)

class GeometryEntity(EvalfMixin, Basic):
    '''The base class for all geometrical entities.

    This class does not represent any particular geometric entity, it only
    provides the implementation of some methods common to all subclasses.

    '''
    __slots__: 'tuple[str, ...]' = ()
    
    def __cmp__(self, other):
        '''Comparison of two GeometryEntities.'''
        n1 = self.__class__.__name__
        n2 = other.__class__.__name__
        c = (n1 > n2) - (n1 < n2)
        if not c:
            return 0
        i1 = None
        for cls in self.__class__.__mro__:
            i1 = ordering_of_classes.index(cls.__name__)
        except ValueError:
            i1 = -1
            continue
        if i1 == -1:
            return c
        i2 = None
        for cls in other.__class__.__mro__:
            i2 = ordering_of_classes.index(cls.__name__)
        except ValueError:
            i2 = -1
            continue
        if i2 == -1:
            return c
        return (None > i2) - (i1 < i2)

    
    def __contains__(self, other):
        '''Subclasses should implement this method for anything more complex than equality.'''
        if type(self) is type(other):
            return self == other
        raise None()

    
    def __getnewargs__(self):
        '''Returns a tuple that will be passed to __new__ on unpickling.'''
        return tuple(self.args)

    
    def __ne__(self, o):
        '''Test inequality of two geometrical entities.'''
        return not (self == o)

    
    def __new__(cls, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __radd__(self, a):
        '''Implementation of reverse add method.'''
        return a.__add__(self)

    
    def __rtruediv__(self, a):
        '''Implementation of reverse division method.'''
        return a.__truediv__(self)

    
    def __repr__(self):
        '''String representation of a GeometryEntity that can be evaluated
        by sympy.'''
        return type(self).__name__ + repr(self.args)

    
    def __rmul__(self, a):
        '''Implementation of reverse multiplication method.'''
        return a.__mul__(self)

    
    def __rsub__(self, a):
        '''Implementation of reverse subtraction method.'''
        return a.__sub__(self)

    
    def __str__(self):
        '''String representation of a GeometryEntity.'''
        return type(self).__name__ + sstr(self.args)

    
    def _eval_subs(self, old, new):
        Point = Point
        Point3D = Point3D
        import sympy.geometry.point
        if is_sequence(old) or is_sequence(new):
            if isinstance(self, Point3D):
                old = Point3D(old)
                new = Point3D(new)
            else:
                old = Point(old)
                new = Point(new)
            return self._subs(old, new)

    
    def _repr_svg_(self):
        '''SVG representation of a GeometryEntity suitable for IPython'''
        
        try:
            bounds = self.bounds
        except (NotImplementedError, TypeError):
            return None

        if not (lambda .0: pass# WARNING: Decompyle incomplete
)(bounds()):
            return None
        svg_top = all
        (xmin, ymin, xmax, ymax) = map(N, bounds)
        dx = xmax - xmin
        dy = ymax - ymin
        width = min([
            max([
                100,
                dx]),
            300])
        height = min([
            max([
                100,
                dy]),
            300])
        scale_factor = 1 if max(width, height) == 0 else max(dx, dy) / max(width, height)
        
        try:
            svg = self._svg(scale_factor)
        except (NotImplementedError, TypeError):
            return None

        view_box = '{} {} {} {}'.format(xmin, ymin, dx, dy)
        transform = 'matrix(1,0,0,-1,0,{})'.format(ymax + ymin)
        svg_top = svg_top.format(view_box, width, height)
        return svg_top + '<g transform="{}">{}</g></svg>'.format(transform, svg)

    
    def _svg(self, scale_factor, fill_color = (1, '#66cc99')):
        '''Returns SVG path element for the GeometryEntity.

        Parameters
        ==========

        scale_factor : float
            Multiplication factor for the SVG stroke-width.  Default is 1.
        fill_color : str, optional
            Hex string for fill color. Default is "#66cc99".
        '''
        raise NotImplementedError()

    
    def _sympy_(self):
        return self

    ambient_dimension = (lambda self: raise NotImplementedError())()
    bounds = (lambda self: raise NotImplementedError())()
    
    def encloses(self, o):
        '''
        Return True if o is inside (not on or outside) the boundaries of self.

        The object will be decomposed into Points and individual Entities need
        only define an encloses_point method for their class.

        See Also
        ========

        sympy.geometry.ellipse.Ellipse.encloses_point
        sympy.geometry.polygon.Polygon.encloses_point

        Examples
        ========

        >>> from sympy import RegularPolygon, Point, Polygon
        >>> t  = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t2 = Polygon(*RegularPolygon(Point(0, 0), 2, 3).vertices)
        >>> t2.encloses(t)
        True
        >>> t.encloses(t2)
        False

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def equals(self, o):
        return self == o

    
    def intersection(self, o):
        '''
        Returns a list of all of the intersections of self with o.

        Notes
        =====

        An entity is not required to implement this method.

        If two different types of entities can intersect, the item with
        higher index in ordering_of_classes should implement
        intersections with anything having a lower index.

        See Also
        ========

        sympy.geometry.util.intersection

        '''
        raise NotImplementedError()

    
    def is_similar(self, other):
        '''Is this geometrical entity similar to another geometrical entity?

        Two entities are similar if a uniform scaling (enlarging or
        shrinking) of one of the entities will allow one to obtain the other.

        Notes
        =====

        This method is not intended to be used directly but rather
        through the `are_similar` function found in util.py.
        An entity is not required to implement this method.
        If two different types of entities can be similar, it is only
        required that one of them be able to determine this.

        See Also
        ========

        scale

        '''
        raise NotImplementedError()

    
    def reflect(self, line):
        '''
        Reflects an object across a line.

        Parameters
        ==========

        line: Line

        Examples
        ========

        >>> from sympy import pi, sqrt, Line, RegularPolygon
        >>> l = Line((0, pi), slope=sqrt(2))
        >>> pent = RegularPolygon((1, 2), 1, 5)
        >>> rpent = pent.reflect(l)
        >>> rpent
        RegularPolygon(Point2D(-2*sqrt(2)*pi/3 - 1/3 + 4*sqrt(2)/3, 2/3 + 2*sqrt(2)/3 + 2*pi/3), -1, 5, -atan(2*sqrt(2)) + 3*pi/5)

        >>> from sympy import pi, Line, Circle, Point
        >>> l = Line((0, pi), slope=1)
        >>> circ = Circle(Point(0, 0), 5)
        >>> rcirc = circ.reflect(l)
        >>> rcirc
        Circle(Point2D(-pi, pi), -5)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def rotate(self, angle, pt = (None,)):
        '''Rotate ``angle`` radians counterclockwise about Point ``pt``.

        The default pt is the origin, Point(0, 0)

        See Also
        ========

        scale, translate

        Examples
        ========

        >>> from sympy import Point, RegularPolygon, Polygon, pi
        >>> t = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t # vertex on x axis
        Triangle(Point2D(1, 0), Point2D(-1/2, sqrt(3)/2), Point2D(-1/2, -sqrt(3)/2))
        >>> t.rotate(pi/2) # vertex on y axis now
        Triangle(Point2D(0, 1), Point2D(-sqrt(3)/2, -1/2), Point2D(sqrt(3)/2, -1/2))

        '''
        newargs = []
    # WARNING: Decompyle incomplete

    
    def scale(self, x, y, pt = (1, 1, None)):
        '''Scale the object by multiplying the x,y-coordinates by x and y.

        If pt is given, the scaling is done relative to that point; the
        object is shifted by -pt, scaled, and shifted by pt.

        See Also
        ========

        rotate, translate

        Examples
        ========

        >>> from sympy import RegularPolygon, Point, Polygon
        >>> t = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t
        Triangle(Point2D(1, 0), Point2D(-1/2, sqrt(3)/2), Point2D(-1/2, -sqrt(3)/2))
        >>> t.scale(2)
        Triangle(Point2D(2, 0), Point2D(-1, sqrt(3)/2), Point2D(-1, -sqrt(3)/2))
        >>> t.scale(2, 2)
        Triangle(Point2D(2, 0), Point2D(-1, sqrt(3)), Point2D(-1, -sqrt(3)))

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def translate(self, x, y = (0, 0)):
        '''Shift the object by adding to the x,y-coordinates the values x and y.

        See Also
        ========

        rotate, scale

        Examples
        ========

        >>> from sympy import RegularPolygon, Point, Polygon
        >>> t = Polygon(*RegularPolygon(Point(0, 0), 1, 3).vertices)
        >>> t
        Triangle(Point2D(1, 0), Point2D(-1/2, sqrt(3)/2), Point2D(-1/2, -sqrt(3)/2))
        >>> t.translate(2)
        Triangle(Point2D(3, 0), Point2D(3/2, sqrt(3)/2), Point2D(3/2, -sqrt(3)/2))
        >>> t.translate(2, 2)
        Triangle(Point2D(3, 2), Point2D(3/2, sqrt(3)/2 + 2), Point2D(3/2, 2 - sqrt(3)/2))

        '''
        newargs = []
    # WARNING: Decompyle incomplete

    
    def parameter_value(self, other, t):
        '''Return the parameter corresponding to the given point.
        Evaluating an arbitrary point of the entity at this parameter
        value will return the given point.

        Examples
        ========

        >>> from sympy import Line, Point
        >>> from sympy.abc import t
        >>> a = Point(0, 0)
        >>> b = Point(2, 2)
        >>> Line(a, b).parameter_value((1, 1), t)
        {t: 1/2}
        >>> Line(a, b).arbitrary_point(t).subs(_)
        Point2D(1, 1)
        '''
        Point = Point
        import sympy.geometry.point
        if not isinstance(other, GeometryEntity):
            other = Point(other, dim = self.ambient_dimension)
        if not isinstance(other, Point):
            raise ValueError('other must be a point')
        sol = solve(self.arbitrary_point(T) - other, T, dict = True)
        if not sol:
            raise ValueError('Given point is not on %s' % func_name(self))
        return {
            t: sol[0][T] }



class GeometrySet(Set, GeometryEntity):
    '''Parent class of all GeometryEntity that are also Sets
    (compatible with sympy.sets)
    '''
    __slots__ = ()
    
    def _contains(self, other):
        '''sympy.sets uses the _contains method, so include it for compatibility.'''
        pass
    # WARNING: Decompyle incomplete


union_sets = (lambda self, o: pass# WARNING: Decompyle incomplete
)()
intersection_sets = (lambda self, o: pass# WARNING: Decompyle incomplete
)()

def translate(x, y):
    '''Return the matrix to translate a 2-D point by x and y.'''
    rv = eye(3)
    rv[(2, 0)] = x
    rv[(2, 1)] = y
    return rv


def scale(x, y, pt = (None,)):
    """Return the matrix to multiply a 2-D point's coordinates by x and y.

    If pt is given, the scaling is done relative to that point."""
    rv = eye(3)
    rv[(0, 0)] = x
    rv[(1, 1)] = y
# WARNING: Decompyle incomplete


def rotate(th):
    '''Return the matrix to rotate a 2-D point about the origin by ``angle``.

    The angle is measured in radians. To Point a point about a point other
    then the origin, translate the Point, do the rotation, and
    translate it back:

    >>> from sympy.geometry.entity import rotate, translate
    >>> from sympy import Point, pi
    >>> rot_about_11 = translate(-1, -1)*rotate(pi/2)*translate(1, 1)
    >>> Point(1, 1).transform(rot_about_11)
    Point2D(1, 1)
    >>> Point(0, 0).transform(rot_about_11)
    Point2D(2, 0)
    '''
    s = sin(th)
    rv = eye(3) * cos(th)
    rv[(0, 1)] = s
    rv[(1, 0)] = -s
    rv[(2, 2)] = 1
    return rv
