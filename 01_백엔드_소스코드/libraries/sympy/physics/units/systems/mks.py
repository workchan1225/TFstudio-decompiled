# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mks.pyc (Python 3.11)

'''
MKS unit system.

MKS stands for "meter, kilogram, second".
'''
from sympy.physics.units import UnitSystem
from sympy.physics.units.definitions import gravitational_constant, hertz, joule, newton, pascal, watt, speed_of_light, gram, kilogram, meter, second
from sympy.physics.units.definitions.dimension_definitions import acceleration, action, energy, force, frequency, momentum, power, pressure, velocity, length, mass, time
from sympy.physics.units.prefixes import PREFIXES, prefix_unit
from sympy.physics.units.systems.length_weight_time import dimsys_length_weight_time
dims = (velocity, acceleration, momentum, force, energy, power, pressure, frequency, action)
units = [
    meter,
    gram,
    second,
    joule,
    newton,
    watt,
    pascal,
    hertz]
all_units = []
all_units.extend([
    gram,
    joule,
    newton,
    watt,
    pascal,
    hertz])
for u in units:
    all_units.extend(prefix_unit(u, PREFIXES))
    all_units.extend([
        gravitational_constant,
        speed_of_light])
    MKS = UnitSystem(base_units = (meter, kilogram, second), units = all_units, name = 'MKS', dimension_system = dimsys_length_weight_time, derived_units = {
        acceleration: meter / second ** 2,
        velocity: meter / second,
        energy: joule,
        force: newton,
        mass: kilogram,
        frequency: hertz,
        length: meter,
        pressure: pascal,
        time: second,
        power: watt })
    __all__ = [
        'MKS',
        'units',
        'all_units',
        'dims']
    return None
