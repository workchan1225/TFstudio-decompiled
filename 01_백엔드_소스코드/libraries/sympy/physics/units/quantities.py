# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quantities.pyc (Python 3.11)

'''
Physical quantities.
'''
from sympy.core.expr import AtomicExpr
from sympy.core.symbol import Symbol
from sympy.core.sympify import sympify
from sympy.physics.units.dimensions import _QuantityMapper
from sympy.physics.units.prefixes import Prefix

class Quantity(AtomicExpr):
    '''
    Physical quantity: can be a unit of measure, a constant or a generic quantity.
    '''
    is_commutative = True
    is_real = True
    is_number = False
    is_nonzero = True
    is_physical_constant = False
    _diff_wrt = True
    
    def __new__(cls, name, abbrev, latex_repr, pretty_unicode_repr, pretty_ascii_repr, mathml_presentation_repr, is_prefixed = (None, None, None, None, None, False), **assumptions):
        if not isinstance(name, Symbol):
            name = Symbol(name)
    # WARNING: Decompyle incomplete

    
    def set_global_dimension(self, dimension):
        _QuantityMapper._quantity_dimension_global[self] = dimension

    
    def set_global_relative_scale_factor(self, scale_factor, reference_quantity):
        '''
        Setting a scale factor that is valid across all unit system.
        '''
        UnitSystem = UnitSystem
        import sympy.physics.units
        scale_factor = sympify(scale_factor)
        if isinstance(scale_factor, Prefix):
            self._is_prefixed = True
        scale_factor = scale_factor.replace((lambda x: isinstance(x, Prefix)), (lambda x: x.scale_factor))
        scale_factor = sympify(scale_factor)
        UnitSystem._quantity_scale_factors_global[self] = (scale_factor, reference_quantity)
        UnitSystem._quantity_dimensional_equivalence_map_global[self] = reference_quantity

    name = (lambda self: self._name)()
    dimension = (lambda self: UnitSystem = UnitSystemimport sympy.physics.unitsunit_system = UnitSystem.get_default_unit_system()unit_system.get_quantity_dimension(self))()
    abbrev = (lambda self: self._abbrev)()
    scale_factor = (lambda self: UnitSystem = UnitSystemimport sympy.physics.unitsunit_system = UnitSystem.get_default_unit_system()unit_system.get_quantity_scale_factor(self))()
    
    def _eval_is_positive(self):
        return True

    
    def _eval_is_constant(self):
        return True

    
    def _eval_Abs(self):
        return self

    
    def _eval_subs(self, old, new):
        if isinstance(new, Quantity) or self != old:
            return self
        return None

    
    def _latex(self, printer):
        if self._latex_repr:
            return self._latex_repr
        return None.format(self.args[1] if len(self.args) >= 2 else self.args[0])

    
    def convert_to(self, other, unit_system = ('SI',)):
        '''
        Convert the quantity to another quantity of same dimensions.

        Examples
        ========

        >>> from sympy.physics.units import speed_of_light, meter, second
        >>> speed_of_light
        speed_of_light
        >>> speed_of_light.convert_to(meter/second)
        299792458*meter/second

        >>> from sympy.physics.units import liter
        >>> liter.convert_to(meter**3)
        meter**3/1000
        '''
        convert_to = convert_to
        import util
        return convert_to(self, other, unit_system)

    free_symbols = (lambda self: set())()
    is_prefixed = (lambda self: self._is_prefixed)()


class PhysicalConstant(Quantity):
    '''Represents a physical constant, eg. `speed_of_light` or `avogadro_constant`.'''
    is_physical_constant = True
