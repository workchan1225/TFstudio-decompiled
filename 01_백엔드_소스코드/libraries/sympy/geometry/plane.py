# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: plane.pyc (Python 3.11)

'''Geometrical Planes.

Contains
========
Plane

'''
from sympy.core import Dummy, Rational, S, Symbol
from sympy.core.symbol import _symbol
from sympy.functions.elementary.trigonometric import cos, sin, acos, asin, sqrt
from entity import GeometryEntity
from line import Line, Ray, Segment, Line3D, LinearEntity, LinearEntity3D, Ray3D, Segment3D
from point import Point, Point3D
from sympy.matrices import Matrix
from sympy.polys.polytools import cancel
from sympy.solvers import solve, linsolve
from sympy.utilities.iterables import uniq, is_sequence
from sympy.utilities.misc import filldedent, func_name, Undecidable
from mpmath.libmp.libmpf import prec_to_dps
import random
(x, y, z, t) = range(4)()

class Plane(GeometryEntity):
    """
    A plane is a flat, two-dimensional surface. A plane is the two-dimensional
    analogue of a point (zero-dimensions), a line (one-dimension) and a solid
    (three-dimensions). A plane can generally be constructed by two types of
    inputs. They are:
    - three non-collinear points
    - a point and the plane's normal vector

    Attributes
    ==========

    p1
    normal_vector

    Examples
    ========

    >>> from sympy import Plane, Point3D
    >>> Plane(Point3D(1, 1, 1), Point3D(2, 3, 4), Point3D(2, 2, 2))
    Plane(Point3D(1, 1, 1), (-1, 2, -1))
    >>> Plane((1, 1, 1), (2, 3, 4), (2, 2, 2))
    Plane(Point3D(1, 1, 1), (-1, 2, -1))
    >>> Plane(Point3D(1, 1, 1), normal_vector=(1,4,7))
    Plane(Point3D(1, 1, 1), (1, 4, 7))

    """
    
    def __new__(cls, p1, a, b = (None, None), **kwargs):
        p1 = Point3D(p1, dim = 3)
    # WARNING: Decompyle incomplete

    
    def __contains__(self, o):
        k = self.equation(x, y, z)
        if isinstance(o, (LinearEntity, LinearEntity3D)):
            d = Point3D(o.arbitrary_point(t))
            e = k.subs([
                (x, d.x),
                (y, d.y),
                (z, d.z)])
            return e.equals(0)
        
        try:
            o = Point(o, dim = 3, strict = True)
            d = k.xreplace(dict(zip((x, y, z), o.args)))
            return d.equals(0)
        except TypeError:
            return False


    
    def _eval_evalf(self, prec = (15,), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def angle_between(self, o):
        """Angle between the plane and other geometric entity.

        Parameters
        ==========

        LinearEntity3D, Plane.

        Returns
        =======

        angle : angle in radians

        Notes
        =====

        This method accepts only 3D entities as it's parameter, but if you want
        to calculate the angle between a 2D entity and a plane you should
        first convert to a 3D entity by projecting onto a desired plane and
        then proceed to calculate the angle.

        Examples
        ========

        >>> from sympy import Point3D, Line3D, Plane
        >>> a = Plane(Point3D(1, 2, 2), normal_vector=(1, 2, 3))
        >>> b = Line3D(Point3D(1, 3, 4), Point3D(2, 2, 2))
        >>> a.angle_between(b)
        -asin(sqrt(21)/6)

        """
        if isinstance(o, LinearEntity3D):
            a = Matrix(self.normal_vector)
            b = Matrix(o.direction_ratio)
            c = a.dot(b)
            d = sum((lambda .0: pass# WARNING: Decompyle incomplete
)(self.normal_vector()))
            e = sum((lambda .0: pass# WARNING: Decompyle incomplete
)(o.direction_ratio()))
            return asin(c / (d * e))
        if None(o, Plane):
            a = Matrix(self.normal_vector)
            b = Matrix(o.normal_vector)
            c = a.dot(b)
            d = sum((lambda .0: pass# WARNING: Decompyle incomplete
)(self.normal_vector()))
            e = sum((lambda .0: pass# WARNING: Decompyle incomplete
)(o.normal_vector()))
            return acos(c / (d * e))

    
    def arbitrary_point(self, u, v = (None, None)):
        ''' Returns an arbitrary point on the Plane. If given two
        parameters, the point ranges over the entire plane. If given 1
        or no parameters, returns a point with one parameter which,
        when varying from 0 to 2*pi, moves the point in a circle of
        radius 1 about p1 of the Plane.

        Examples
        ========

        >>> from sympy import Plane, Ray
        >>> from sympy.abc import u, v, t, r
        >>> p = Plane((1, 1, 1), normal_vector=(1, 0, 0))
        >>> p.arbitrary_point(u, v)
        Point3D(1, u + 1, v + 1)
        >>> p.arbitrary_point(t)
        Point3D(1, cos(t) + 1, sin(t) + 1)

        While arbitrary values of u and v can move the point anywhere in
        the plane, the single-parameter point can be used to construct a
        ray whose arbitrary point can be located at angle t and radius
        r from p.p1:

        >>> Ray(p.p1, _).arbitrary_point(r)
        Point3D(1, r*cos(t) + 1, r*sin(t) + 1)

        Returns
        =======

        Point3D

        '''
        pass
    # WARNING: Decompyle incomplete

    are_concurrent = (lambda : planes = list(uniq(planes))for i in planes:
if not isinstance(i, Plane):
raise ValueError('All objects should be Planes but got %s' % i.func)if len(planes) < 2:
Falseplanes = None(planes)first = planes.pop(0)sol = first.intersection(planes[0])if sol == []:
Falseline = None[0]for i in planes[1:]:
l = first.intersection(i)if l or l[0] not in line:
FalseTrue)()
    
    def distance(self, o):
        """Distance between the plane and another geometric entity.

        Parameters
        ==========

        Point3D, LinearEntity3D, Plane.

        Returns
        =======

        distance

        Notes
        =====

        This method accepts only 3D entities as it's parameter, but if you want
        to calculate the distance between a 2D entity and a plane you should
        first convert to a 3D entity by projecting onto a desired plane and
        then proceed to calculate the distance.

        Examples
        ========

        >>> from sympy import Point3D, Line3D, Plane
        >>> a = Plane(Point3D(1, 1, 1), normal_vector=(1, 1, 1))
        >>> b = Point3D(1, 2, 3)
        >>> a.distance(b)
        sqrt(3)
        >>> c = Line3D(Point3D(2, 3, 1), Point3D(1, 2, 2))
        >>> a.distance(c)
        0

        """
        if self.intersection(o) != []:
            return S.Zero
    # WARNING: Decompyle incomplete

    
    def equals(self, o):
        '''
        Returns True if self and o are the same mathematical entities.

        Examples
        ========

        >>> from sympy import Plane, Point3D
        >>> a = Plane(Point3D(1, 2, 3), normal_vector=(1, 1, 1))
        >>> b = Plane(Point3D(1, 2, 3), normal_vector=(2, 2, 2))
        >>> c = Plane(Point3D(1, 2, 3), normal_vector=(-1, 4, 6))
        >>> a.equals(a)
        True
        >>> a.equals(b)
        True
        >>> a.equals(c)
        False
        '''
        if isinstance(o, Plane):
            a = self.equation()
            b = o.equation()
            return cancel(a / b).is_constant()

    
    def equation(self, x, y, z = (None, None, None)):
        '''The equation of the Plane.

        Examples
        ========

        >>> from sympy import Point3D, Plane
        >>> a = Plane(Point3D(1, 1, 2), Point3D(2, 4, 7), Point3D(3, 5, 1))
        >>> a.equation()
        -23*x + 11*y - 2*z + 16
        >>> a = Plane(Point3D(1, 4, 2), normal_vector=(6, 6, 6))
        >>> a.equation()
        6*x + 6*y + 6*z - 42

        '''
        (x, y, z) = zip((x, y, z), 'xyz')()
        a = Point3D(x, y, z)
        b = self.p1.direction_ratio(a)
        c = self.normal_vector
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(b, c)())

    
    def intersection(self, o):
