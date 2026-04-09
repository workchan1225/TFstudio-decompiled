# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

from sympy.vector.coordsysrect import CoordSys3D
from sympy.vector.deloperator import Del
from sympy.vector.scalar import BaseScalar
from sympy.vector.vector import Vector, BaseVector
from sympy.vector.operators import gradient, curl, divergence
from sympy.core.function import diff
from sympy.core.singleton import S
from sympy.integrals.integrals import integrate
from sympy.simplify.simplify import simplify
from sympy.core import sympify
from sympy.vector.dyadic import Dyadic

def express(expr, system, system2, variables = (None, False)):
    """
    Global function for 'express' functionality.

    Re-expresses a Vector, Dyadic or scalar(sympyfiable) in the given
    coordinate system.

    If 'variables' is True, then the coordinate variables (base scalars)
    of other coordinate systems present in the vector/scalar field or
    dyadic are also substituted in terms of the base scalars of the
    given system.

    Parameters
    ==========

    expr : Vector/Dyadic/scalar(sympyfiable)
        The expression to re-express in CoordSys3D 'system'

    system: CoordSys3D
        The coordinate system the expr is to be expressed in

    system2: CoordSys3D
        The other coordinate system required for re-expression
        (only for a Dyadic Expr)

    variables : boolean
        Specifies whether to substitute the coordinate variables present
        in expr, in terms of those of parameter system

    Examples
    ========

    >>> from sympy.vector import CoordSys3D
    >>> from sympy import Symbol, cos, sin
    >>> N = CoordSys3D('N')
    >>> q = Symbol('q')
    >>> B = N.orient_new_axis('B', q, N.k)
    >>> from sympy.vector import express
    >>> express(B.i, N)
    (cos(q))*N.i + (sin(q))*N.j
    >>> express(N.x, B, variables=True)
    B.x*cos(q) - B.y*sin(q)
    >>> d = N.i.outer(N.i)
    >>> express(d, B, N) == (cos(q))*(B.i|N.i) + (-sin(q))*(B.j|N.i)
    True

    """
    if expr in (0, Vector.zero):
        return expr
    if not None(system, CoordSys3D):
        raise TypeError('system should be a CoordSys3D                         instance')
# WARNING: Decompyle incomplete


def directional_derivative(field, direction_vector):
    """
    Returns the directional derivative of a scalar or vector field computed
    along a given vector in coordinate system which parameters are expressed.

    Parameters
    ==========

    field : Vector or Scalar
        The scalar or vector field to compute the directional derivative of

    direction_vector : Vector
        The vector to calculated directional derivative along them.


    Examples
    ========

    >>> from sympy.vector import CoordSys3D, directional_derivative
    >>> R = CoordSys3D('R')
    >>> f1 = R.x*R.y*R.z
    >>> v1 = 3*R.i + 4*R.j + R.k
    >>> directional_derivative(f1, v1)
    R.x*R.y + 4*R.x*R.z + 3*R.y*R.z
    >>> f2 = 5*R.x**2*R.z
    >>> directional_derivative(f2, v1)
    5*R.x**2 + 30*R.x*R.z

    """
    _get_coord_systems = _get_coord_systems
    import sympy.vector.operators
    coord_sys = _get_coord_systems(field)
    if len(coord_sys) > 0:
        coord_sys = next(iter(coord_sys))
        field = express(field, coord_sys, variables = True)
        (i, j, k) = coord_sys.base_vectors()
        (x, y, z) = coord_sys.base_scalars()
        out = Vector.dot(direction_vector, i) * diff(field, x)
        out += Vector.dot(direction_vector, j) * diff(field, y)
        out += Vector.dot(direction_vector, k) * diff(field, z)
        if out == 0 and isinstance(field, Vector):
            out = Vector.zero
        return out
    if None(field, Vector):
        return Vector.zero
    return None.Zero


def laplacian(expr):
    """
    Return the laplacian of the given field computed in terms of
    the base scalars of the given coordinate system.

    Parameters
    ==========

    expr : SymPy Expr or Vector
        expr denotes a scalar or vector field.

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, laplacian
    >>> R = CoordSys3D('R')
    >>> f = R.x**2*R.y**5*R.z
    >>> laplacian(f)
    20*R.x**2*R.y**3*R.z + 2*R.y**5*R.z
    >>> f = R.x**2*R.i + R.y**3*R.j + R.z**4*R.k
    >>> laplacian(f)
    2*R.i + 6*R.y*R.j + 12*R.z**2*R.k

    """
    delop = Del()
    if expr.is_Vector:
        return (gradient(divergence(expr)) - curl(curl(expr))).doit()
    return None.dot(delop(expr)).doit()


def is_conservative(field):
    """
    Checks if a field is conservative.

    Parameters
    ==========

    field : Vector
        The field to check for conservative property

    Examples
    ========

    >>> from sympy.vector import CoordSys3D
    >>> from sympy.vector import is_conservative
    >>> R = CoordSys3D('R')
    >>> is_conservative(R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k)
    True
    >>> is_conservative(R.z*R.j)
    False

    """
    if not isinstance(field, Vector):
        raise TypeError('field should be a Vector')
    if field == Vector.zero:
        return True
    return None(field).simplify() == Vector.zero


def is_solenoidal(field):
    """
    Checks if a field is solenoidal.

    Parameters
    ==========

    field : Vector
        The field to check for solenoidal property

    Examples
    ========

    >>> from sympy.vector import CoordSys3D
    >>> from sympy.vector import is_solenoidal
    >>> R = CoordSys3D('R')
    >>> is_solenoidal(R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k)
    True
    >>> is_solenoidal(R.y * R.j)
    False

    """
    if not isinstance(field, Vector):
        raise TypeError('field should be a Vector')
    if field == Vector.zero:
        return True
    return None(field).simplify() is S.Zero


def scalar_potential(field, coord_sys):
    """
    Returns the scalar potential function of a field in a given
    coordinate system (without the added integration constant).

    Parameters
    ==========

    field : Vector
        The vector field whose scalar potential function is to be
        calculated

    coord_sys : CoordSys3D
        The coordinate system to do the calculation in

    Examples
    ========

    >>> from sympy.vector import CoordSys3D
    >>> from sympy.vector import scalar_potential, gradient
    >>> R = CoordSys3D('R')
    >>> scalar_potential(R.k, R) == R.z
    True
    >>> scalar_field = 2*R.x**2*R.y*R.z
    >>> grad_field = gradient(scalar_field)
    >>> scalar_potential(grad_field, R)
    2*R.x**2*R.y*R.z

    """
    if not is_conservative(field):
        raise ValueError('Field is not conservative')
    if field == Vector.zero:
        return S.Zero
    if not None(coord_sys, CoordSys3D):
        raise TypeError('coord_sys must be a CoordSys3D')
    field = express(field, coord_sys, variables = True)
    dimensions = coord_sys.base_vectors()
    scalars = coord_sys.base_scalars()
    temp_function = integrate(field.dot(dimensions[0]), scalars[0])
    for i, dim in enumerate(dimensions[1:]):
        partial_diff = diff(temp_function, scalars[i + 1])
        partial_diff = field.dot(dim) - partial_diff
        temp_function += integrate(partial_diff, scalars[i + 1])
        return temp_function


def scalar_potential_difference(field, coord_sys, point1, point2):
    """
    Returns the scalar potential difference between two points in a
    certain coordinate system, wrt a given field.

    If a scalar field is provided, its values at the two points are
    considered. If a conservative vector field is provided, the values
    of its scalar potential function at the two points are used.

    Returns (potential at point2) - (potential at point1)

    The position vectors of the two Points are calculated wrt the
    origin of the coordinate system provided.

    Parameters
    ==========

    field : Vector/Expr
        The field to calculate wrt

    coord_sys : CoordSys3D
        The coordinate system to do the calculations in

    point1 : Point
        The initial Point in given coordinate system

    position2 : Point
        The second Point in the given coordinate system

    Examples
    ========

    >>> from sympy.vector import CoordSys3D
    >>> from sympy.vector import scalar_potential_difference
    >>> R = CoordSys3D('R')
    >>> P = R.origin.locate_new('P', R.x*R.i + R.y*R.j + R.z*R.k)
    >>> vectfield = 4*R.x*R.y*R.i + 2*R.x**2*R.j
    >>> scalar_potential_difference(vectfield, R, R.origin, P)
    2*R.x**2*R.y
    >>> Q = R.origin.locate_new('O', 3*R.i + R.j + 2*R.k)
    >>> scalar_potential_difference(vectfield, R, P, Q)
    -2*R.x**2*R.y + 18

    """
    if not isinstance(coord_sys, CoordSys3D):
        raise TypeError('coord_sys must be a CoordSys3D')
    if isinstance(field, Vector):
        scalar_fn = scalar_potential(field, coord_sys)
    else:
        scalar_fn = field
    origin = coord_sys.origin
    position1 = express(point1.position_wrt(origin), coord_sys, variables = True)
    position2 = express(point2.position_wrt(origin), coord_sys, variables = True)
    subs_dict1 = { }
    subs_dict2 = { }
    scalars = coord_sys.base_scalars()
    for i, x in enumerate(coord_sys.base_vectors()):
        subs_dict1[scalars[i]] = x.dot(position1)
        subs_dict2[scalars[i]] = x.dot(position2)
        return scalar_fn.subs(subs_dict2) - scalar_fn.subs(subs_dict1)


def matrix_to_vector(matrix, system):
    """
    Converts a vector in matrix form to a Vector instance.

    It is assumed that the elements of the Matrix represent the
    measure numbers of the components of the vector along basis
    vectors of 'system'.

    Parameters
    ==========

    matrix : SymPy Matrix, Dimensions: (3, 1)
        The matrix to be converted to a vector

    system : CoordSys3D
        The coordinate system the vector is to be defined in

    Examples
    ========

    >>> from sympy import ImmutableMatrix as Matrix
    >>> m = Matrix([1, 2, 3])
    >>> from sympy.vector import CoordSys3D, matrix_to_vector
    >>> C = CoordSys3D('C')
    >>> v = matrix_to_vector(m, C)
    >>> v
    C.i + 2*C.j + 3*C.k
    >>> v.to_matrix(C) == m
    True

    """
    outvec = Vector.zero
    vects = system.base_vectors()
    for i, x in enumerate(matrix):
        outvec += x * vects[i]
        return outvec


def _path(from_object, to_object):
    """
    Calculates the 'path' of objects starting from 'from_object'
    to 'to_object', along with the index of the first common
    ancestor in the tree.

    Returns (index, list) tuple.
    """
    if from_object._root != to_object._root:
        raise ValueError('No connecting path found between ' + str(from_object) + ' and ' + str(to_object))
    other_path = []
    obj = to_object
# WARNING: Decompyle incomplete


def orthogonalize(*, orthonormal, *vlist):
    """
    Takes a sequence of independent vectors and orthogonalizes them
    using the Gram - Schmidt process. Returns a list of
    orthogonal or orthonormal vectors.

    Parameters
    ==========

    vlist : sequence of independent vectors to be made orthogonal.

    orthonormal : Optional parameter
                  Set to True if the vectors returned should be
                  orthonormal.
                  Default: False

    Examples
    ========

    >>> from sympy.vector.coordsysrect import CoordSys3D
    >>> from sympy.vector.functions import orthogonalize
    >>> C = CoordSys3D('C')
    >>> i, j, k = C.base_vectors()
    >>> v1 = i + 2*j
    >>> v2 = 2*i + 3*j
    >>> orthogonalize(v1, v2)
    [C.i + 2*C.j, 2/5*C.i + (-1/5)*C.j]

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Gram-Schmidt_process

    """
    if not (lambda .0: pass# WARNING: Decompyle incomplete
)(vlist()):
        raise TypeError('Each element must be of Type Vector')
    ortho_vlist = []
    for i, term in enumerate(vlist):
        for j in range(i):
            term -= ortho_vlist[j].projection(vlist[i])
            if simplify(term).equals(Vector.zero):
                raise ValueError('Vector set not linearly independent')
            ortho_vlist.append(term)
            if orthonormal:
                ortho_vlist = ortho_vlist()
    return ortho_vlist
