# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector.pyc (Python 3.11)

from __future__ import annotations
from itertools import product
from sympy.core.add import Add
from sympy.core.assumptions import StdFactKB
from sympy.core.expr import AtomicExpr, Expr
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.core.sorting import default_sort_key
from sympy.core.sympify import sympify
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.matrices.immutable import ImmutableDenseMatrix as Matrix
from sympy.vector.basisdependent import BasisDependentZero, BasisDependent, BasisDependentMul, BasisDependentAdd
from sympy.vector.coordsysrect import CoordSys3D
from sympy.vector.dyadic import Dyadic, BaseDyadic, DyadicAdd

class Vector(BasisDependent):
    '''
    Super class for all Vector classes.
    Ideally, neither this class nor any of its subclasses should be
    instantiated by the user.
    '''
    is_scalar = False
    is_Vector = True
    zero: 'VectorZero' = 12
    components = (lambda self: self._components)()
    
    def magnitude(self):
        '''
        Returns the magnitude of this vector.
        '''
        return sqrt(self & self)

    
    def normalize(self):
        '''
        Returns the normalized version of this vector.
        '''
        return self / self.magnitude()

    
    def dot(self, other):
        """
        Returns the dot product of this Vector, either with another
        Vector, or a Dyadic, or a Del operator.
        If 'other' is a Vector, returns the dot product scalar (SymPy
        expression).
        If 'other' is a Dyadic, the dot product is returned as a Vector.
        If 'other' is an instance of Del, returns the directional
        derivative operator as a Python function. If this function is
        applied to a scalar expression, it returns the directional
        derivative of the scalar field wrt this Vector.

        Parameters
        ==========

        other: Vector/Dyadic/Del
            The Vector or Dyadic we are dotting with, or a Del operator .

        Examples
        ========

        >>> from sympy.vector import CoordSys3D, Del
        >>> C = CoordSys3D('C')
        >>> delop = Del()
        >>> C.i.dot(C.j)
        0
        >>> C.i & C.i
        1
        >>> v = 3*C.i + 4*C.j + 5*C.k
        >>> v.dot(C.k)
        5
        >>> (C.i & delop)(C.x*C.y*C.z)
        C.y*C.z
        >>> d = C.i.outer(C.i)
        >>> C.i.dot(d)
        C.i

        """
        pass
    # WARNING: Decompyle incomplete

    
    def __and__(self, other):
        return self.dot(other)

    __and__.__doc__ = dot.__doc__
    
    def cross(self, other):
        """
        Returns the cross product of this Vector with another Vector or
        Dyadic instance.
        The cross product is a Vector, if 'other' is a Vector. If 'other'
        is a Dyadic, this returns a Dyadic instance.

        Parameters
        ==========

        other: Vector/Dyadic
            The Vector or Dyadic we are crossing with.

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> C = CoordSys3D('C')
        >>> C.i.cross(C.j)
        C.k
        >>> C.i ^ C.i
        0
        >>> v = 3*C.i + 4*C.j + 5*C.k
        >>> v ^ C.i
        5*C.j + (-4)*C.k
        >>> d = C.i.outer(C.i)
        >>> C.j.cross(d)
        (-1)*(C.k|C.i)

        """
        if isinstance(other, Dyadic):
            if isinstance(self, VectorZero):
                return Dyadic.zero
            outdyad = None.zero
            for k, v in other.components.items():
                cross_product = self.cross(k.args[0])
                outer = cross_product.outer(k.args[1])
                outdyad += v * outer
                return outdyad
                return cross(self, other)

    
    def __xor__(self, other):
        return self.cross(other)

    __xor__.__doc__ = cross.__doc__
    
    def outer(self, other):
