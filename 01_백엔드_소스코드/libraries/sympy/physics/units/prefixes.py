# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: prefixes.pyc (Python 3.11)

__doc__ = '\nModule defining unit prefixe class and some constants.\n\nConstant dict for SI and binary prefixes are defined as PREFIXES and\nBIN_PREFIXES.\n'
from sympy.core.expr import Expr
from sympy.core.sympify import sympify
from sympy.core.singleton import S

class Prefix(Expr):
    pass
# WARNING: Decompyle incomplete


def prefix_unit(unit, prefixes):
    '''
    Return a list of all units formed by unit and the given prefixes.

    You can use the predefined PREFIXES or BIN_PREFIXES, but you can also
    pass as argument a subdict of them if you do not want all prefixed units.

        >>> from sympy.physics.units.prefixes import (PREFIXES,
        ...                                                 prefix_unit)
        >>> from sympy.physics.units import m
        >>> pref = {"m": PREFIXES["m"], "c": PREFIXES["c"], "d": PREFIXES["d"]}
        >>> prefix_unit(m, pref)  # doctest: +SKIP
        [millimeter, centimeter, decimeter]
    '''
    Quantity = Quantity
    import sympy.physics.units.quantities
    UnitSystem = UnitSystem
    import sympy.physics.units
    prefixed_units = []
    for prefix in prefixes.values():
        quantity = Quantity(f'''{prefix.name!s}{unit.name!s}''', abbrev = f'''{prefix.abbrev!s}{unit.abbrev!s}''', is_prefixed = True)
        UnitSystem._quantity_dimensional_equivalence_map_global[quantity] = unit
        UnitSystem._quantity_scale_factors_global[quantity] = (prefix.scale_factor, unit)
        prefixed_units.append(quantity)
        return prefixed_units

yotta = Prefix('yotta', 'Y', 24)
zetta = Prefix('zetta', 'Z', 21)
exa = Prefix('exa', 'E', 18)
peta = Prefix('peta', 'P', 15)
tera = Prefix('tera', 'T', 12)
giga = Prefix('giga', 'G', 9)
mega = Prefix('mega', 'M', 6)
kilo = Prefix('kilo', 'k', 3)
hecto = Prefix('hecto', 'h', 2)
deca = Prefix('deca', 'da', 1)
deci = Prefix('deci', 'd', -1)
centi = Prefix('centi', 'c', -2)
milli = Prefix('milli', 'm', -3)
micro = Prefix('micro', 'mu', -6, latex_repr = '\\mu')
nano = Prefix('nano', 'n', -9)
pico = Prefix('pico', 'p', -12)
femto = Prefix('femto', 'f', -15)
atto = Prefix('atto', 'a', -18)
zepto = Prefix('zepto', 'z', -21)
yocto = Prefix('yocto', 'y', -24)
# WARNING: Decompyle incomplete
