# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: point.pyc (Python 3.11)

'''Geometrical Points.

Contains
========
Point
Point2D
Point3D

When methods of Point require 1 or more points as arguments, they
can be passed as a sequence of coordinates or Points:

>>> from sympy import Point
>>> Point(1, 1).is_collinear((2, 2), (3, 4))
False
>>> Point(1, 1).is_collinear(Point(2, 2), Point(3, 4))
False

'''
import warnings
from sympy.core import S, sympify, Expr
from sympy.core.add import Add
from sympy.core.containers import Tuple
from sympy.core.numbers import Float
from sympy.core.parameters import global_parameters
from sympy.simplify import nsimplify, simplify
from sympy.geometry.exceptions import GeometryError
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.functions.elementary.complexes import im
from sympy.functions.elementary.trigonometric import cos, sin
from sympy.matrices import Matrix
from sympy.matrices.expressions import Transpose
from sympy.utilities.iterables import uniq, is_sequence
from sympy.utilities.misc import filldedent, func_name, Undecidable
from entity import GeometryEntity
from mpmath.libmp.libmpf import prec_to_dps

class Point(GeometryEntity):
    """A point in a n-dimensional Euclidean space.

    Parameters
    ==========

    coords : sequence of n-coordinate values. In the special
        case where n=2 or 3, a Point2D or Point3D will be created
        as appropriate.
    evaluate : if `True` (default), all floats are turn into
        exact types.
    dim : number of coordinates the point should have.  If coordinates
        are unspecified, they are padded with zeros.
    on_morph : indicates what should happen when the number of
        coordinates of a point need to be changed by adding or
        removing zeros.  Possible values are `'warn'`, `'error'`, or
        `ignore` (default).  No warning or error is given when `*args`
        is empty and `dim` is given. An error is always raised when
        trying to remove nonzero coordinates.


    Attributes
    ==========

    length
    origin: A `Point` representing the origin of the
        appropriately-dimensioned space.

    Raises
    ======

    TypeError : When instantiating with anything but a Point or sequence
    ValueError : when instantiating with a sequence with length < 2 or
        when trying to reduce dimensions if keyword `on_morph='error'` is
        set.

    See Also
    ========

    sympy.geometry.line.Segment : Connects two Points

    Examples
    ========

    >>> from sympy import Point
    >>> from sympy.abc import x
    >>> Point(1, 2, 3)
    Point3D(1, 2, 3)
    >>> Point([1, 2])
    Point2D(1, 2)
    >>> Point(0, x)
    Point2D(0, x)
    >>> Point(dim=4)
    Point(0, 0, 0, 0)

    Floats are automatically converted to Rational unless the
    evaluate flag is False:

    >>> Point(0.5, 0.25)
    Point2D(1/2, 1/4)
    >>> Point(0.5, 0.25, evaluate=False)
    Point2D(0.5, 0.25)

    """
    is_Point = True
    
    def __new__(cls, *args, **kwargs):
        evaluate = kwargs.get('evaluate', global_parameters.evaluate)
        on_morph = kwargs.get('on_morph', 'ignore')
        coords = args[0] if len(args) == 1 else args
        if isinstance(coords, Point):
            evaluate = False
            if len(coords) == kwargs.get('dim', len(coords)):
                return coords
            if not None(coords):
                raise TypeError(filldedent('\n                Expecting sequence of coordinates, not `{}`'.format(func_name(coords))))
            if len(coords) == 0 and kwargs.get('dim', None):
                coords = (S.Zero,) * kwargs.get('dim')
    # WARNING: Decompyle incomplete

    
    def __abs__(self):
        '''Returns the distance between this point and the origin.'''
        origin = Point([
            0] * len(self))
        return Point.distance(origin, self)

    
    def __add__(self, other):
        """Add other to self by incrementing self's coordinates by
        those of other.

        Notes
        =====

        >>> from sympy import Point

        When sequences of coordinates are passed to Point methods, they
        are converted to a Point internally. This __add__ method does
        not do that so if floating point values are used, a floating
        point result (in terms of SymPy Floats) will be returned.

        >>> Point(1, 2) + (.1, .2)
        Point2D(1.1, 2.2)

        If this is not desired, the `translate` method can be used or
        another Point can be added:

        >>> Point(1, 2).translate(.1, .2)
        Point2D(11/10, 11/5)
        >>> Point(1, 2) + Point(.1, .2)
        Point2D(11/10, 11/5)

        See Also
        ========

        sympy.geometry.point.Point.translate

        """
        
        try:
            (s, o) = Point._normalize_dimension(self, Point(other, evaluate = False))
        except TypeError:
            raise GeometryError("Don't know how to add {} and a Point object".format(other))

        coords = zip(s, o)()
        return Point(coords, evaluate = False)

    
    def __contains__(self, item):
        return item in self.args

    
    def __truediv__(self, divisor):
        """Divide point's coordinates by a factor."""
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        if isinstance(other, Point) or len(self.args) != len(other.args):
            return False
        return None.args == other.args

    
    def __getitem__(self, key):
        return self.args[key]

    
    def __hash__(self):
        return hash(self.args)

    
    def __iter__(self):
        return self.args.__iter__()

    
    def __len__(self):
        return len(self.args)

    
    def __mul__(self, factor):
        """Multiply point's coordinates by a factor.

        Notes
        =====

        >>> from sympy import Point

        When multiplying a Point by a floating point number,
        the coordinates of the Point will be changed to Floats:

        >>> Point(1, 2)*0.1
        Point2D(0.1, 0.2)

        If this is not desired, the `scale` method can be used or
        else only multiply or divide by integers:

        >>> Point(1, 2).scale(1.1, 1.1)
        Point2D(11/10, 11/5)
        >>> Point(1, 2)*11/10
        Point2D(11/10, 11/5)

        See Also
        ========

        sympy.geometry.point.Point.scale
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __rmul__(self, factor):
        """Multiply a factor by point's coordinates."""
        return self.__mul__(factor)

    
    def __neg__(self):
        '''Negate the point.'''
        coords = self.args()
        return Point(coords, evaluate = False)

    
    def __sub__(self, other):
        """Subtract two points, or subtract a factor from this point's
        coordinates."""
        return (lambda .0: [ -x for x in .0 ]) + other()

    _normalize_dimension = (lambda cls: pass# WARNING: Decompyle incomplete
)()
    affine_rank = (lambda : pass# WARNING: Decompyle incomplete
)()
    ambient_dimension = (lambda self: getattr(self, '_ambient_dimension', len(self)))()
    are_coplanar = (lambda cls: if len(points) <= 1:
True# WARNING: Decompyle incomplete
)()
    
    def distance(self, other):
        '''The Euclidean distance between self and another GeometricEntity.

        Returns
        =======

        distance : number or symbolic expression.

        Raises
        ======

        TypeError : if other is not recognized as a GeometricEntity or is a
                    GeometricEntity for which distance is not defined.

        See Also
        ========

        sympy.geometry.line.Segment.length
        sympy.geometry.point.Point.taxicab_distance

        Examples
        ========

        >>> from sympy import Point, Line
        >>> p1, p2 = Point(1, 1), Point(4, 5)
        >>> l = Line((3, 1), (2, 2))
        >>> p1.distance(p2)
        5
        >>> p1.distance(l)
        sqrt(2)

        The computed distance may be symbolic, too:

        >>> from sympy.abc import x, y
        >>> p3 = Point(x, y)
        >>> p3.distance((0, 0))
        sqrt(x**2 + y**2)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def dot(self, p):
        '''Return dot product of self with another Point.'''
        if not is_sequence(p):
            p = Point(p)
    # WARNING: Decompyle incomplete

    
    def equals(self, other):
        '''Returns whether the coordinates of self and other agree.'''
        if isinstance(other, Point) or len(self) != len(other):
            return False
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(zip(self, other)())

    
    def _eval_evalf(self, prec = (15,), **options):
        '''Evaluate the coordinates of the point.

        This method will, where possible, create and return a new Point
        where the coordinates are evaluated as floating point numbers to
        the precision indicated (default=15).

        Parameters
        ==========

        prec : int

        Returns
        =======

        point : Point

        Examples
        ========

        >>> from sympy import Point, Rational
        >>> p1 = Point(Rational(1, 2), Rational(3, 2))
        >>> p1
        Point2D(1/2, 3/2)
        >>> p1.evalf()
        Point2D(0.5, 1.5)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def intersection(self, other):
        '''The intersection between this point and another GeometryEntity.

        Parameters
        ==========

        other : GeometryEntity or sequence of coordinates

        Returns
        =======

        intersection : list of Points

        Notes
        =====

        The return value will either be an empty list if there is no
        intersection, otherwise it will contain this point.

        Examples
        ========

        >>> from sympy import Point
        >>> p1, p2, p3 = Point(0, 0), Point(1, 1), Point(0, 0)
        >>> p1.intersection(p2)
        []
        >>> p1.intersection(p3)
        [Point2D(0, 0)]

        '''
        if not isinstance(other, GeometryEntity):
            other = Point(other)
        if isinstance(other, Point):
            if self == other:
                return [
                    self]
            (p1, p2) = None._normalize_dimension(self, other)
            if p1 == self and p1 == p2:
                return [
                    self]
            return None
        return None.intersection(self)

    
    def is_collinear(self, *args):
        '''Returns `True` if there exists a line
        that contains `self` and `points`.  Returns `False` otherwise.
        A trivially True value is returned if no points are given.

        Parameters
        ==========

        args : sequence of Points

        Returns
        =======

        is_collinear : boolean

        See Also
        ========

        sympy.geometry.line.Line

        Examples
        ========

        >>> from sympy import Point
        >>> from sympy.abc import x
        >>> p1, p2 = Point(0, 0), Point(1, 1)
        >>> p3, p4, p5 = Point(2, 2), Point(x, x), Point(1, 2)
        >>> Point.is_collinear(p1, p2, p3, p4)
        True
        >>> Point.is_collinear(p1, p2, p3, p5)
        False

        '''
        points = (self,) + args
    # WARNING: Decompyle incomplete

    
    def is_concyclic(self, *args):
        '''Do `self` and the given sequence of points lie in a circle?

        Returns True if the set of points are concyclic and
        False otherwise. A trivial value of True is returned
        if there are fewer than 2 other points.

        Parameters
        ==========

        args : sequence of Points

        Returns
        =======

        is_concyclic : boolean


        Examples
        ========

        >>> from sympy import Point

        Define 4 points that are on the unit circle:

        >>> p1, p2, p3, p4 = Point(1, 0), (0, 1), (-1, 0), (0, -1)

        >>> p1.is_concyclic() == p1.is_concyclic(p2, p3, p4) == True
        True

        Define a point not on that circle:

        >>> p = Point(1, 1)

        >>> p.is_concyclic(p1, p2, p3)
        False

        '''
        pass
    # WARNING: Decompyle incomplete

    is_nonzero = (lambda self: is_zero = self.is_zero# WARNING: Decompyle incomplete
)()
    
    def is_scalar_multiple(self, p):
        '''Returns whether each coordinate of `self` is a scalar
        multiple of the corresponding coordinate in point p.
        '''
        (s, o) = Point._normalize_dimension(self, Point(p))
    # WARNING: Decompyle incomplete

    is_zero = (lambda self: nonzero = self.args()if any(nonzero):
Falseif (lambda .0: pass# WARNING: Decompyle incomplete
)(nonzero()):
            return None
        return (lambda .0: [ x.is_nonzero for x in .0 ])
)()
    length = (lambda self: S.Zero)()
    
    def midpoint(self, p):
        '''The midpoint between self and point p.

        Parameters
        ==========

        p : Point

        Returns
        =======

        midpoint : Point

        See Also
        ========

        sympy.geometry.line.Segment.midpoint

        Examples
        ========

        >>> from sympy import Point
        >>> p1, p2 = Point(1, 1), Point(13, 5)
        >>> p1.midpoint(p2)
        Point2D(7, 3)

        '''
        (s, p) = Point._normalize_dimension(self, Point(p))
        return (lambda .0: [ simplify((a + b) * S.Half) for a, b in .0 ])(zip(s, p)())

    origin = (lambda self: Point([
0] * len(self), evaluate = False))()
    orthogonal_direction = (lambda self: dim = self.ambient_dimensionif self[0].is_zero:
Point([
1] + (dim - 1) * [
0])if None[1].is_zero:
Point([
0,
1] + (dim - 2) * [
0])None([
-self[1],
self[0]] + (dim - 2) * [
0]))()
    project = (lambda a, b: (a, b) = Point._normalize_dimension(Point(a), Point(b))if b.is_zero:
raise ValueError('Cannot project to the zero vector.')b * (a.dot(b) / b.dot(b)))()
    
    def taxicab_distance(self, p):
        '''The Taxicab Distance from self to point p.

        Returns the sum of the horizontal and vertical distances to point p.

        Parameters
        ==========

        p : Point

        Returns
        =======

        taxicab_distance : The sum of the horizontal
        and vertical distances to point p.

        See Also
        ========

        sympy.geometry.point.Point.distance

        Examples
        ========

        >>> from sympy import Point
        >>> p1, p2 = Point(1, 1), Point(4, 5)
        >>> p1.taxicab_distance(p2)
        7

        '''
        (s, p) = Point._normalize_dimension(self, Point(p))
    # WARNING: Decompyle incomplete

    
    def canberra_distance(self, p):
        '''The Canberra Distance from self to point p.

        Returns the weighted sum of horizontal and vertical distances to
        point p.

        Parameters
        ==========

        p : Point

        Returns
        =======

        canberra_distance : The weighted sum of horizontal and vertical
        distances to point p. The weight used is the sum of absolute values
        of the coordinates.

        Examples
        ========

        >>> from sympy import Point
        >>> p1, p2 = Point(1, 1), Point(3, 3)
        >>> p1.canberra_distance(p2)
        1
        >>> p1, p2 = Point(0, 0), Point(3, 3)
        >>> p1.canberra_distance(p2)
        2

        Raises
        ======

        ValueError when both vectors are zero.

        See Also
        ========

        sympy.geometry.point.Point.distance

        '''
        (s, p) = Point._normalize_dimension(self, Point(p))
        if self.is_zero and p.is_zero:
            raise ValueError('Cannot project to the zero vector.')
    # WARNING: Decompyle incomplete

    unit = (lambda self: self / abs(self))()


class Point2D(Point):
    '''A point in a 2-dimensional Euclidean space.

    Parameters
    ==========

    coords
        A sequence of 2 coordinate values.

    Attributes
    ==========

    x
    y
    length

    Raises
    ======

    TypeError
        When trying to add or subtract points with different dimensions.
        When trying to create a point with more than two dimensions.
        When `intersection` is called with object other than a Point.

    See Also
    ========

    sympy.geometry.line.Segment : Connects two Points

    Examples
    ========

    >>> from sympy import Point2D
    >>> from sympy.abc import x
    >>> Point2D(1, 2)
    Point2D(1, 2)
    >>> Point2D([1, 2])
    Point2D(1, 2)
    >>> Point2D(0, x)
    Point2D(0, x)

    Floats are automatically converted to Rational unless the
    evaluate flag is False:

    >>> Point2D(0.5, 0.25)
    Point2D(1/2, 1/4)
    >>> Point2D(0.5, 0.25, evaluate=False)
    Point2D(0.5, 0.25)

    '''
    _ambient_dimension = 2
    
    def __new__(cls = None, *, _nocheck, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self, item):
        return item == self

    bounds = (lambda self: (self.x, self.y, self.x, self.y))()
    
    def rotate(self, angle, pt = (None,)):
        '''Rotate ``angle`` radians counterclockwise about Point ``pt``.

        See Also
        ========

        translate, scale

        Examples
        ========

        >>> from sympy import Point2D, pi
        >>> t = Point2D(1, 0)
        >>> t.rotate(pi/2)
        Point2D(0, 1)
        >>> t.rotate(pi/2, (2, 0))
        Point2D(2, -1)

        '''
        c = cos(angle)
        s = sin(angle)
        rv = self
    # WARNING: Decompyle incomplete

    
    def scale(self, x, y, pt = (1, 1, None)):
        '''Scale the coordinates of the Point by multiplying by
        ``x`` and ``y`` after subtracting ``pt`` -- default is (0, 0) --
        and then adding ``pt`` back again (i.e. ``pt`` is the point of
        reference for the scaling).

        See Also
        ========

        rotate, translate

        Examples
        ========

        >>> from sympy import Point2D
        >>> t = Point2D(1, 1)
        >>> t.scale(2)
        Point2D(2, 1)
        >>> t.scale(2, 2)
        Point2D(2, 2)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def transform(self, matrix):
        '''Return the point after applying the transformation described
        by the 3x3 Matrix, ``matrix``.

        See Also
        ========
        sympy.geometry.point.Point2D.rotate
        sympy.geometry.point.Point2D.scale
        sympy.geometry.point.Point2D.translate
        '''
        if not matrix.is_Matrix or matrix.shape == (3, 3):
            raise ValueError('matrix must be a 3x3 matrix')
        (x, y) = self.args
    # WARNING: Decompyle incomplete

    
    def translate(self, x, y = (0, 0)):
        '''Shift the Point by adding x and y to the coordinates of the Point.

        See Also
        ========

        sympy.geometry.point.Point2D.rotate, scale

        Examples
        ========

        >>> from sympy import Point2D
        >>> t = Point2D(0, 1)
        >>> t.translate(2)
        Point2D(2, 1)
        >>> t.translate(2, 2)
        Point2D(2, 3)
        >>> t + Point2D(2, 2)
        Point2D(2, 3)

        '''
        return Point(self.x + x, self.y + y)

    coordinates = (lambda self: self.args)()
    x = (lambda self: self.args[0])()
    y = (lambda self: self.args[1])()


class Point3D(Point):
    '''A point in a 3-dimensional Euclidean space.

    Parameters
    ==========

    coords
        A sequence of 3 coordinate values.

    Attributes
    ==========

    x
    y
    z
    length

    Raises
    ======

    TypeError
        When trying to add or subtract points with different dimensions.
        When `intersection` is called with object other than a Point.

    Examples
    ========

    >>> from sympy import Point3D
    >>> from sympy.abc import x
    >>> Point3D(1, 2, 3)
    Point3D(1, 2, 3)
    >>> Point3D([1, 2, 3])
    Point3D(1, 2, 3)
    >>> Point3D(0, x, 3)
    Point3D(0, x, 3)

    Floats are automatically converted to Rational unless the
    evaluate flag is False:

    >>> Point3D(0.5, 0.25, 2)
    Point3D(1/2, 1/4, 2)
    >>> Point3D(0.5, 0.25, 3, evaluate=False)
    Point3D(0.5, 0.25, 3)

    '''
    _ambient_dimension = 3
    
    def __new__(cls = None, *, _nocheck, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self, item):
        return item == self

    are_collinear = (lambda : pass# WARNING: Decompyle incomplete
)()
    
    def direction_cosine(self, point):
        '''
        Gives the direction cosine between 2 points

        Parameters
        ==========

        p : Point3D

        Returns
        =======

        list

        Examples
        ========

        >>> from sympy import Point3D
        >>> p1 = Point3D(1, 2, 3)
        >>> p1.direction_cosine(Point3D(2, 3, 5))
        [sqrt(6)/6, sqrt(6)/6, sqrt(6)/3]
        '''
        a = self.direction_ratio(point)
    # WARNING: Decompyle incomplete

    
    def direction_ratio(self, point):
        '''
        Gives the direction ratio between 2 points

        Parameters
        ==========

        p : Point3D

        Returns
        =======

        list

        Examples
        ========

        >>> from sympy import Point3D
        >>> p1 = Point3D(1, 2, 3)
        >>> p1.direction_ratio(Point3D(2, 3, 5))
        [1, 1, 2]
        '''
        return [
            point.x - self.x,
            point.y - self.y,
            point.z - self.z]

    
    def intersection(self, other):
        '''The intersection between this point and another GeometryEntity.

        Parameters
        ==========

        other : GeometryEntity or sequence of coordinates

        Returns
        =======

        intersection : list of Points

        Notes
        =====

        The return value will either be an empty list if there is no
        intersection, otherwise it will contain this point.

        Examples
        ========

        >>> from sympy import Point3D
        >>> p1, p2, p3 = Point3D(0, 0, 0), Point3D(1, 1, 1), Point3D(0, 0, 0)
        >>> p1.intersection(p2)
        []
        >>> p1.intersection(p3)
        [Point3D(0, 0, 0)]

        '''
        if not isinstance(other, GeometryEntity):
            other = Point(other, dim = 3)
        if isinstance(other, Point3D):
            if self == other:
                return [
                    self]
            return None
        return None.intersection(self)

    
    def scale(self, x, y, z, pt = (1, 1, 1, None)):
        '''Scale the coordinates of the Point by multiplying by
        ``x`` and ``y`` after subtracting ``pt`` -- default is (0, 0) --
        and then adding ``pt`` back again (i.e. ``pt`` is the point of
        reference for the scaling).

        See Also
        ========

        translate

        Examples
        ========

        >>> from sympy import Point3D
        >>> t = Point3D(1, 1, 1)
        >>> t.scale(2)
        Point3D(2, 1, 1)
        >>> t.scale(2, 2)
        Point3D(2, 2, 1)

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def transform(self, matrix):
        '''Return the point after applying the transformation described
        by the 4x4 Matrix, ``matrix``.

        See Also
        ========
        sympy.geometry.point.Point3D.scale
        sympy.geometry.point.Point3D.translate
        '''
        if not matrix.is_Matrix or matrix.shape == (4, 4):
            raise ValueError('matrix must be a 4x4 matrix')
        (x, y, z) = self.args
        m = Transpose(matrix)
    # WARNING: Decompyle incomplete

    
    def translate(self, x, y, z = (0, 0, 0)):
        '''Shift the Point by adding x and y to the coordinates of the Point.

        See Also
        ========

        scale

        Examples
        ========

        >>> from sympy import Point3D
        >>> t = Point3D(0, 1, 1)
        >>> t.translate(2)
        Point3D(2, 1, 1)
        >>> t.translate(2, 2)
        Point3D(2, 3, 1)
        >>> t + Point3D(2, 2, 2)
        Point3D(2, 3, 3)

        '''
        return Point3D(self.x + x, self.y + y, self.z + z)

    coordinates = (lambda self: self.args)()
    x = (lambda self: self.args[0])()
    y = (lambda self: self.args[1])()
    z = (lambda self: self.args[2])()
