# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unitsystem.pyc (Python 3.11)

'''
Unit system for physical quantities; include definition of constants.
'''
from typing import Dict as tDict, Set as tSet
from sympy.core.add import Add
from sympy.core.function import Derivative, Function
from sympy.core.mul import Mul
from sympy.core.power import Pow
from sympy.core.singleton import S
from sympy.physics.units.dimensions import _QuantityMapper
from sympy.physics.units.quantities import Quantity
from dimensions import Dimension

class UnitSystem(_QuantityMapper):
    pass
# WARNING: Decompyle incomplete
