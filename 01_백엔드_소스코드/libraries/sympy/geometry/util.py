# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

'''Utility functions for geometrical entities.

Contains
========
intersection
convex_hull
closest_points
farthest_points
are_coplanar
are_similar

'''
from collections import deque
from math import sqrt as _sqrt
from sympy import nsimplify
from entity import GeometryEntity
from exceptions import GeometryError
from point import Point, Point2D, Point3D
from sympy.core.containers import OrderedSet
from sympy.core.exprtools import factor_terms
from sympy.core.function import Function, expand_mul
from sympy.core.numbers import Float
from sympy.core.sorting import ordered
from sympy.core.symbol import Symbol
from sympy.core.singleton import S
from sympy.polys.polytools import cancel
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.utilities.iterables import is_sequence
from mpmath.libmp.libmpf import prec_to_dps

def find(x, equation):
    """
    Checks whether a Symbol matching ``x`` is present in ``equation``
    or not. If present, the matching symbol is returned, else a
    ValueError is raised. If ``x`` is a string the matching symbol
    will have the same name; if ``x`` is a Symbol then it will be
    returned if found.

    Examples
    ========

    >>> from sympy.geometry.util import find
    >>> from sympy import Dummy
    >>> from sympy.abc import x
    >>> find('x', x)
    x
    >>> find('x', Dummy('x'))
    _x

    The dummy symbol is returned since it has a matching name:

    >>> _.name == 'x'
    True
    >>> find(x, Dummy('x'))
    Traceback (most recent call last):
    ...
    ValueError: could not find x
    """
    pass
# WARNING: Decompyle incomplete


def _ordered_points(p):
    '''Return the tuple of points sorted numerically according to args'''
    return tuple(sorted(p, key = (lambda x: x.args)))


def are_coplanar(*e):
    ''' Returns True if the given entities are coplanar otherwise False

    Parameters
    ==========

    e: entities to be checked for being coplanar

    Returns
    =======

    Boolean

    Examples
    ========

    >>> from sympy import Point3D, Line3D
    >>> from sympy.geometry.util import are_coplanar
    >>> a = Line3D(Point3D(5, 0, 0), Point3D(1, -1, 1))
    >>> b = Line3D(Point3D(0, -2, 0), Point3D(3, 1, 1))
    >>> c = Line3D(Point3D(0, -1, 0), Point3D(5, -1, 9))
    >>> are_coplanar(a, b, c)
    False

    '''
    pass
# WARNING: Decompyle incomplete


def are_similar(e1, e2):
    '''Are two geometrical entities similar.

    Can one geometrical entity be uniformly scaled to the other?

    Parameters
    ==========

    e1 : GeometryEntity
    e2 : GeometryEntity

    Returns
    =======

    are_similar : boolean

    Raises
    ======

    GeometryError
        When `e1` and `e2` cannot be compared.

    Notes
    =====

    If the two objects are equal then they are similar.

    See Also
    ========

    sympy.geometry.entity.GeometryEntity.is_similar

    Examples
    ========

    >>> from sympy import Point, Circle, Triangle, are_similar
    >>> c1, c2 = Circle(Point(0, 0), 4), Circle(Point(1, 4), 3)
    >>> t1 = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
    >>> t2 = Triangle(Point(0, 0), Point(2, 0), Point(0, 2))
    >>> t3 = Triangle(Point(0, 0), Point(3, 0), Point(0, 1))
    >>> are_similar(t1, t2)
    True
    >>> are_similar(t1, t3)
    False

    '''
    if e1 == e2:
        return True
    is_similar1 = None(e1, 'is_similar', None)
    if is_similar1:
        return is_similar1(e2)
    is_similar2 = None(e2, 'is_similar', None)
    if is_similar2:
        return is_similar2(e1)
    n1 = None.__class__.__name__
    n2 = e2.__class__.__name__
    raise GeometryError(f'''Cannot test similarity between {n1!s} and {n2!s}''')


def centroid(*args):
    '''Find the centroid (center of mass) of the collection containing only Points,
    Segments or Polygons. The centroid is the weighted average of the individual centroid
    where the weights are the lengths (of segments) or areas (of polygons).
    Overlapping regions will add to the weight of that region.

    If there are no objects (or a mixture of objects) then None is returned.

    See Also
    ========

    sympy.geometry.point.Point, sympy.geometry.line.Segment,
    sympy.geometry.polygon.Polygon

    Examples
    ========

    >>> from sympy import Point, Segment, Polygon
    >>> from sympy.geometry.util import centroid
    >>> p = Polygon((0, 0), (10, 0), (10, 10))
    >>> q = p.translate(0, 20)
    >>> p.centroid, q.centroid
    (Point2D(20/3, 10/3), Point2D(20/3, 70/3))
    >>> centroid(p, q)
    Point2D(20/3, 40/3)
    >>> p, q = Segment((0, 0), (2, 0)), Segment((0, 0), (2, 2))
    >>> centroid(p, q)
    Point2D(1, 2 - sqrt(2))
    >>> centroid(Point(0, 0), Point(2, 0))
    Point2D(1, 0)

    Stacking 3 polygons on top of each other effectively triples the
    weight of that polygon:

    >>> p = Polygon((0, 0), (1, 0), (1, 1), (0, 1))
    >>> q = Polygon((1, 0), (3, 0), (3, 1), (1, 1))
    >>> centroid(p, q)
    Point2D(3/2, 1/2)
    >>> centroid(p, p, p, q) # centroid x-coord shifts left
    Point2D(11/10, 1/2)

    Stacking the squares vertically above and below p has the same
    effect:

    >>> centroid(p, p.translate(0, 1), p.translate(0, -1), q)
    Point2D(11/10, 1/2)

    '''
    pass
# WARNING: Decompyle incomplete


def closest_points(*args):
    '''Return the subset of points from a set of points that were
    the closest to each other in the 2D plane.

    Parameters
    ==========

    args
        A collection of Points on 2D plane.

    Notes
    =====

    This can only be performed on a set of points whose coordinates can
    be ordered on the number line. If there are no ties then a single
    pair of Points will be in the set.

    Examples
    ========

    >>> from sympy import closest_points, Triangle
    >>> Triangle(sss=(3, 4, 5)).args
    (Point2D(0, 0), Point2D(3, 0), Point2D(3, 4))
    >>> closest_points(*_)
    {(Point2D(0, 0), Point2D(3, 0))}

    References
    ==========

    .. [1] https://www.cs.mcgill.ca/~cs251/ClosestPair/ClosestPairPS.html

    .. [2] Sweep line algorithm
        https://en.wikipedia.org/wiki/Sweep_line_algorithm

    '''
    pass
# WARNING: Decompyle incomplete


def convex_hull(*, polygon, *args):
