# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dimensions.pyc (Python 3.11)

'''
Definition of physical dimensions.

Unit systems will be constructed on top of these dimensions.

Most of the examples in the doc use MKS system and are presented from the
computer point of view: from a human point, adding length to time is not legal
in MKS but it is in natural system; for a computer in natural system there is
no time dimension (but a velocity dimension instead) - in the basis - so the
question of adding time to length has no meaning.
'''
from __future__ import annotations
import collections
from functools import reduce
from sympy.core.basic import Basic
from sympy.core.containers import Dict, Tuple
from sympy.core.singleton import S
from sympy.core.sorting import default_sort_key
from sympy.core.symbol import Symbol
from sympy.core.sympify import sympify
from sympy.matrices.dense import Matrix
from sympy.functions.elementary.trigonometric import TrigonometricFunction
from sympy.core.expr import Expr
from sympy.core.power import Pow

class _QuantityMapper:
    _quantity_scale_factors_global: 'dict[Expr, Expr]' = { }
    _quantity_dimensional_equivalence_map_global: 'dict[Expr, Expr]' = { }
    _quantity_dimension_global: 'dict[Expr, Expr]' = { }
    
    def __init__(self, *args, **kwargs):
        self._quantity_dimension_map = { }
        self._quantity_scale_factors = { }

    
    def set_quantity_dimension(self, quantity, dimension):
        '''
        Set the dimension for the quantity in a unit system.

        If this relation is valid in every unit system, use
        ``quantity.set_global_dimension(dimension)`` instead.
        '''
        Quantity = Quantity
        import sympy.physics.units
        dimension = sympify(dimension)
        if not isinstance(dimension, Dimension):
            if dimension == 1:
                dimension = Dimension(1)
            else:
                raise ValueError('expected dimension or 1')
        if isinstance(dimension, Quantity):
            dimension = self.get_quantity_dimension(dimension)
        self._quantity_dimension_map[quantity] = dimension

    
    def set_quantity_scale_factor(self, quantity, scale_factor):
        '''
        Set the scale factor of a quantity relative to another quantity.

        It should be used only once per quantity to just one other quantity,
        the algorithm will then be able to compute the scale factors to all
        other quantities.

        In case the scale factor is valid in every unit system, please use
        ``quantity.set_global_relative_scale_factor(scale_factor)`` instead.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_quantity_dimension(self, unit):
        Quantity = Quantity
        import sympy.physics.units
        if unit in self._quantity_dimension_map:
            return self._quantity_dimension_map[unit]
        if None in self._quantity_dimension_global:
            return self._quantity_dimension_global[unit]
        if None in self._quantity_dimensional_equivalence_map_global:
            dep_unit = self._quantity_dimensional_equivalence_map_global[unit]
            if isinstance(dep_unit, Quantity):
                return self.get_quantity_dimension(dep_unit)
            return None(self.get_dimensional_expr(dep_unit))
        if None(unit, Quantity):
            return Dimension(unit.name)
        return None(1)

    
    def get_quantity_scale_factor(self, unit):
        if unit in self._quantity_scale_factors:
            return self._quantity_scale_factors[unit]
        if None in self._quantity_scale_factors_global:
            (mul_factor, other_unit) = self._quantity_scale_factors_global[unit]
            return mul_factor * self.get_quantity_scale_factor(other_unit)
        return None.One



class Dimension(Expr):
    pass
# WARNING: Decompyle incomplete


class DimensionSystem(_QuantityMapper, Basic):
    '''
    DimensionSystem represents a coherent set of dimensions.

    The constructor takes three parameters:

    - base dimensions;
    - derived dimensions: these are defined in terms of the base dimensions
      (for example velocity is defined from the division of length by time);
    - dependency of dimensions: how the derived dimensions depend
      on the base dimensions.

    Optionally either the ``derived_dims`` or the ``dimensional_dependencies``
    may be omitted.
    '''
    
    def __new__(cls, base_dims, derived_dims, dimensional_dependencies = ((), { })):
        pass
    # WARNING: Decompyle incomplete

    base_dims = (lambda self: self.args[0])()
    derived_dims = (lambda self: self.args[1])()
    dimensional_dependencies = (lambda self: self.args[2])()
    
    def _get_dimensional_dependencies_for_name(self, dimension):
        pass
    # WARNING: Decompyle incomplete

    
    def get_dimensional_dependencies(self, name, mark_dimensionless = (False,)):
        dimdep = self._get_dimensional_dependencies_for_name(name)
        if mark_dimensionless and dimdep == { }:
            return {
                Dimension(1): 1 }
        return None(dimdep.items())

    
    def equivalent_dims(self, dim1, dim2):
        deps1 = self.get_dimensional_dependencies(dim1)
        deps2 = self.get_dimensional_dependencies(dim2)
        return deps1 == deps2

    
    def extend(self, new_base_dims, new_derived_dims, new_dim_deps = ((), None)):
        deps = dict(self.dimensional_dependencies)
        if new_dim_deps:
            deps.update(new_dim_deps)
        new_dim_sys = DimensionSystem(tuple(self.base_dims) + tuple(new_base_dims), tuple(self.derived_dims) + tuple(new_derived_dims), deps)
        new_dim_sys._quantity_dimension_map.update(self._quantity_dimension_map)
        new_dim_sys._quantity_scale_factors.update(self._quantity_scale_factors)
        return new_dim_sys

    
    def is_dimensionless(self, dimension):
        '''
        Check if the dimension object really has a dimension.

        A dimension should have at least one component with non-zero power.
        '''
        if dimension.name == 1:
            return True
        return None.get_dimensional_dependencies(dimension) == { }

    list_can_dims = (lambda self: dimset = set()for i in self.base_dims:
dimset.update(set(self.get_dimensional_dependencies(i).keys()))tuple(sorted(dimset, key = str)))()
    inv_can_transf_matrix = (lambda self: pass# WARNING: Decompyle incomplete
)()
    can_transf_matrix = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def dim_can_vector(self, dim):
        '''
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.

        Dimensional representation in terms of the canonical base dimensions.
        '''
        vec = []
        for d in self.list_can_dims:
            vec.append(self.get_dimensional_dependencies(dim).get(d, 0))
            return Matrix(vec)

    
    def dim_vector(self, dim):
        '''
        Useless method, kept for compatibility with previous versions.

        DO NOT USE.


        Vector representation in terms of the base dimensions.
        '''
        return self.can_transf_matrix * Matrix(self.dim_can_vector(dim))

    
    def print_dim_base(self, dim):
        '''
        Give the string expression of a dimension in term of the basis symbols.
        '''
        dims = self.dim_vector(dim)
        symbols = self.base_dims()
        res = S.One
        for s, p in zip(symbols, dims):
            res *= s ** p
            return res

    dim = (lambda self: len(self.base_dims))()
    is_consistent = (lambda self: self.inv_can_transf_matrix.is_square)()
