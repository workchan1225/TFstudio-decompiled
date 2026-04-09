# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dyadic.pyc (Python 3.11)

from __future__ import annotations
from sympy.vector.basisdependent import BasisDependent, BasisDependentAdd, BasisDependentMul, BasisDependentZero
from sympy.core import S, Pow
from sympy.core.expr import AtomicExpr
from sympy.matrices.immutable import ImmutableDenseMatrix as Matrix
import sympy.vector as sympy

class Dyadic(BasisDependent):
    '''
    Super class for all Dyadic-classes.

    References
    ==========

    .. [1] https://en.wikipedia.org/wiki/Dyadic_tensor
    .. [2] Kane, T., Levinson, D. Dynamics Theory and Applications. 1985
           McGraw-Hill

    '''
    zero: 'DyadicZero' = 13
    components = (lambda self: self._components)()
    
    def dot(self, other):
        """
        Returns the dot product(also called inner product) of this
        Dyadic, with another Dyadic or Vector.
        If 'other' is a Dyadic, this returns a Dyadic. Else, it returns
        a Vector (unless an error is encountered).

        Parameters
        ==========

        other : Dyadic/Vector
            The other Dyadic or Vector to take the inner product with

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> D1 = N.i.outer(N.j)
        >>> D2 = N.j.outer(N.j)
        >>> D1.dot(D2)
        (N.i|N.j)
        >>> D1.dot(N.j)
        N.i

        """
        Vector = sympy.vector.Vector
        if isinstance(other, BasisDependentZero):
            return Vector.zero
        if None(other, Vector):
            outvec = Vector.zero
            for k, v in self.components.items():
                vect_dot = k.args[1].dot(other)
                outvec += vect_dot * v * k.args[0]
                return outvec
                if isinstance(other, Dyadic):
                    outdyad = Dyadic.zero
                    for k1, v1 in self.components.items():
                        for k2, v2 in other.components.items():
                            vect_dot = k1.args[1].dot(k2.args[0])
                            outer_product = k1.args[0].outer(k2.args[1])
                            outdyad += vect_dot * v1 * v2 * outer_product
                            return outdyad
                            raise TypeError('Inner product is not defined for ' + str(type(other)) + ' and Dyadics.')

    
    def __and__(self, other):
        return self.dot(other)

    __and__.__doc__ = dot.__doc__
    
    def cross(self, other):
        """
        Returns the cross product between this Dyadic, and a Vector, as a
        Vector instance.

        Parameters
        ==========

        other : Vector
            The Vector that we are crossing this Dyadic with

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> d = N.i.outer(N.i)
        >>> d.cross(N.j)
        (N.i|N.k)

        """
        Vector = sympy.vector.Vector
        if other == Vector.zero:
            return Dyadic.zero
        if None(other, Vector):
            outdyad = Dyadic.zero
            for k, v in self.components.items():
                cross_product = k.args[1].cross(other)
                outer = k.args[0].outer(cross_product)
                outdyad += v * outer
                return outdyad
                raise TypeError(str(type(other)) + ' not supported for ' + 'cross with dyadics')

    
    def __xor__(self, other):
        return self.cross(other)

    __xor__.__doc__ = cross.__doc__
    
    def to_matrix(self, system, second_system = (None,)):
        """
        Returns the matrix form of the dyadic with respect to one or two
        coordinate systems.

        Parameters
        ==========

        system : CoordSys3D
            The coordinate system that the rows and columns of the matrix
            correspond to. If a second system is provided, this
            only corresponds to the rows of the matrix.
        second_system : CoordSys3D, optional, default=None
            The coordinate system that the columns of the matrix correspond
            to.

        Examples
        ========

        >>> from sympy.vector import CoordSys3D
        >>> N = CoordSys3D('N')
        >>> v = N.i + 2*N.j
        >>> d = v.outer(N.i)
        >>> d.to_matrix(N)
        Matrix([
        [1, 0, 0],
        [2, 0, 0],
        [0, 0, 0]])
        >>> from sympy import Symbol
        >>> q = Symbol('q')
        >>> P = N.orient_new_axis('P', q, N.k)
        >>> d.to_matrix(N, P)
        Matrix([
        [  cos(q),   -sin(q), 0],
        [2*cos(q), -2*sin(q), 0],
        [       0,         0, 0]])

        """
        pass
    # WARNING: Decompyle incomplete

    
    def _div_helper(one, other):
        ''' Helper for division involving dyadics '''
        if isinstance(one, Dyadic) and isinstance(other, Dyadic):
            raise TypeError('Cannot divide two dyadics')
        if isinstance(one, Dyadic):
            return DyadicMul(one, Pow(other, S.NegativeOne))
        raise None('Cannot divide by a dyadic')



class BaseDyadic(AtomicExpr, Dyadic):
    pass
# WARNING: Decompyle incomplete


class DyadicMul(Dyadic, BasisDependentMul):
    ''' Products of scalars and BaseDyadics '''
    
    def __new__(cls, *args, **options):
        pass
    # WARNING: Decompyle incomplete

    base_dyadic = (lambda self: self._base_instance)()
    measure_number = (lambda self: self._measure_number)()


class DyadicAdd(Dyadic, BasisDependentAdd):
    ''' Class to hold dyadic sums '''
    
    def __new__(cls, *args, **options):
        pass
    # WARNING: Decompyle incomplete

    
    def _sympystr(self, printer):
        pass
    # WARNING: Decompyle incomplete



class DyadicZero(Dyadic, BasisDependentZero):
    '''
    Class to denote a zero dyadic
    '''
    _op_priority = 13.1
    _pretty_form = '(0|0)'
    _latex_form = '(\\mathbf{\\hat{0}}|\\mathbf{\\hat{0}})'
    
    def __new__(cls):
        obj = BasisDependentZero.__new__(cls)
        return obj


Dyadic._expr_type = Dyadic
Dyadic._mul_func = DyadicMul
Dyadic._add_func = DyadicAdd
Dyadic._zero_func = DyadicZero
Dyadic._base_func = BaseDyadic
Dyadic.zero = DyadicZero()
