# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: operators.pyc (Python 3.11)

import collections
from sympy.core.expr import Expr
from sympy.core import sympify, S, preorder_traversal
from sympy.vector.coordsysrect import CoordSys3D
from sympy.vector.vector import Vector, VectorMul, VectorAdd, Cross, Dot
from sympy.core.function import Derivative
from sympy.core.add import Add
from sympy.core.mul import Mul

def _get_coord_systems(expr):
    g = preorder_traversal(expr)
    ret = set()
    for i in g:
        if isinstance(i, CoordSys3D):
            ret.add(i)
            g.skip()
        return frozenset(ret)


def _split_mul_args_wrt_coordsys(expr):
    d = collections.defaultdict((lambda : S.One))
    for i in expr.args:
        return list(d.values())


class Gradient(Expr):
    """
    Represents unevaluated Gradient.

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, Gradient
    >>> R = CoordSys3D('R')
    >>> s = R.x*R.y*R.z
    >>> Gradient(s)
    Gradient(R.x*R.y*R.z)

    """
    
    def __new__(cls, expr):
        expr = sympify(expr)
        obj = Expr.__new__(cls, expr)
        obj._expr = expr
        return obj

    
    def doit(self, **hints):
        return gradient(self._expr, doit = True)



class Divergence(Expr):
    """
    Represents unevaluated Divergence.

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, Divergence
    >>> R = CoordSys3D('R')
    >>> v = R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k
    >>> Divergence(v)
    Divergence(R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k)

    """
    
    def __new__(cls, expr):
        expr = sympify(expr)
        obj = Expr.__new__(cls, expr)
        obj._expr = expr
        return obj

    
    def doit(self, **hints):
        return divergence(self._expr, doit = True)



class Curl(Expr):
    """
    Represents unevaluated Curl.

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, Curl
    >>> R = CoordSys3D('R')
    >>> v = R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k
    >>> Curl(v)
    Curl(R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k)

    """
    
    def __new__(cls, expr):
        expr = sympify(expr)
        obj = Expr.__new__(cls, expr)
        obj._expr = expr
        return obj

    
    def doit(self, **hints):
        return curl(self._expr, doit = True)



def curl(vect, doit = (True,)):
    """
    Returns the curl of a vector field computed wrt the base scalars
    of the given coordinate system.

    Parameters
    ==========

    vect : Vector
        The vector operand

    doit : bool
        If True, the result is returned after calling .doit() on
        each component. Else, the returned expression contains
        Derivative instances

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, curl
    >>> R = CoordSys3D('R')
    >>> v1 = R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k
    >>> curl(v1)
    0
    >>> v2 = R.x*R.y*R.z*R.i
    >>> curl(v2)
    R.x*R.y*R.j + (-R.x*R.z)*R.k

    """
    pass
# WARNING: Decompyle incomplete


def divergence(vect, doit = (True,)):
    """
    Returns the divergence of a vector field computed wrt the base
    scalars of the given coordinate system.

    Parameters
    ==========

    vector : Vector
        The vector operand

    doit : bool
        If True, the result is returned after calling .doit() on
        each component. Else, the returned expression contains
        Derivative instances

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, divergence
    >>> R = CoordSys3D('R')
    >>> v1 = R.x*R.y*R.z * (R.i+R.j+R.k)

    >>> divergence(v1)
    R.x*R.y + R.x*R.z + R.y*R.z
    >>> v2 = 2*R.y*R.z*R.j
    >>> divergence(v2)
    2*R.z

    """
    pass
# WARNING: Decompyle incomplete


def gradient(scalar_field, doit = (True,)):
    """
    Returns the vector gradient of a scalar field computed wrt the
    base scalars of the given coordinate system.

    Parameters
    ==========

    scalar_field : SymPy Expr
        The scalar field to compute the gradient of

    doit : bool
        If True, the result is returned after calling .doit() on
        each component. Else, the returned expression contains
        Derivative instances

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, gradient
    >>> R = CoordSys3D('R')
    >>> s1 = R.x*R.y*R.z
    >>> gradient(s1)
    R.y*R.z*R.i + R.x*R.z*R.j + R.x*R.y*R.k
    >>> s2 = 5*R.x**2*R.z
    >>> gradient(s2)
    10*R.x*R.z*R.i + 5*R.x**2*R.k

    """
    pass
# WARNING: Decompyle incomplete


class Laplacian(Expr):
    """
    Represents unevaluated Laplacian.

    Examples
    ========

    >>> from sympy.vector import CoordSys3D, Laplacian
    >>> R = CoordSys3D('R')
    >>> v = 3*R.x**3*R.y**2*R.z**3
    >>> Laplacian(v)
    Laplacian(3*R.x**3*R.y**2*R.z**3)

    """
    
    def __new__(cls, expr):
        expr = sympify(expr)
        obj = Expr.__new__(cls, expr)
        obj._expr = expr
        return obj

    
    def doit(self, **hints):
        laplacian = laplacian
        import sympy.vector.functions
        return laplacian(self._expr)



def _diff_conditional(expr, base_scalar, coeff_1, coeff_2):
    '''
    First re-expresses expr in the system that base_scalar belongs to.
    If base_scalar appears in the re-expressed form, differentiates
    it wrt base_scalar.
    Else, returns 0
    '''
    express = express
    import sympy.vector.functions
    new_expr = express(expr, base_scalar.system, variables = True)
    arg = coeff_1 * coeff_2 * new_expr
    return Derivative(arg, base_scalar) if arg else S.Zero
