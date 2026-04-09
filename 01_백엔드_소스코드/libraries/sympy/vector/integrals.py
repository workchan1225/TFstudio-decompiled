# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: integrals.pyc (Python 3.11)

from sympy.core import Basic, diff
from sympy.core.singleton import S
from sympy.core.sorting import default_sort_key
from sympy.matrices import Matrix
from sympy.integrals import Integral, integrate
from sympy.geometry.entity import GeometryEntity
from sympy.simplify.simplify import simplify
from sympy.utilities.iterables import topological_sort
from sympy.vector import CoordSys3D, Vector, ParametricRegion, parametric_region_list, ImplicitRegion
from sympy.vector.operators import _get_coord_systems

class ParametricIntegral(Basic):
    pass
# WARNING: Decompyle incomplete


def vector_integrate(field, *region):
    """
    Compute the integral of a vector/scalar field
    over a a region or a set of parameters.

    Examples
    ========
    >>> from sympy.vector import CoordSys3D, ParametricRegion, vector_integrate
    >>> from sympy.abc import x, y, t
    >>> C = CoordSys3D('C')

    >>> region = ParametricRegion((t, t**2), (t, 1, 5))
    >>> vector_integrate(C.x*C.i, region)
    12

    Integrals over some objects of geometry module can also be calculated.

    >>> from sympy.geometry import Point, Circle, Triangle
    >>> c = Circle(Point(0, 2), 5)
    >>> vector_integrate(C.x**2 + C.y**2, c)
    290*pi
    >>> triangle = Triangle(Point(-2, 3), Point(2, 3), Point(0, 5))
    >>> vector_integrate(3*C.x**2*C.y*C.i + C.j, triangle)
    -8

    Integrals over some simple implicit regions can be computed. But in most cases,
    it takes too long to compute over them. This is due to the expressions of parametric
    representation becoming large.

    >>> from sympy.vector import ImplicitRegion
    >>> c2 = ImplicitRegion((x, y), (x - 2)**2 + (y - 1)**2 - 9)
    >>> vector_integrate(1, c2)
    6*pi

    Integral of fields with respect to base scalars:

    >>> vector_integrate(12*C.y**3, (C.y, 1, 3))
    240
    >>> vector_integrate(C.x**2*C.z, C.x)
    C.x**3*C.z/3
    >>> vector_integrate(C.x*C.i - C.y*C.k, C.x)
    (Integral(C.x, C.x))*C.i + (Integral(-C.y, C.x))*C.k
    >>> _.doit()
    C.x**2/2*C.i + (-C.x*C.y)*C.k

    """
    pass
# WARNING: Decompyle incomplete
