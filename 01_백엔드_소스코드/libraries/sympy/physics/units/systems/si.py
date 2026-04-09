# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: si.pyc (Python 3.11)

__doc__ = '\nSI unit system.\nBased on MKSA, which stands for "meter, kilogram, second, ampere".\nAdded kelvin, candela and mole.\n\n'
from __future__ import annotations
from sympy.physics.units import DimensionSystem, Dimension, dHg0
from sympy.physics.units.quantities import Quantity
from sympy.core.numbers import Rational, pi
from sympy.core.singleton import S
from sympy.functions.elementary.miscellaneous import sqrt
from sympy.physics.units.definitions.dimension_definitions import acceleration, action, current, impedance, length, mass, time, velocity, amount_of_substance, temperature, information, frequency, force, pressure, energy, power, charge, voltage, capacitance, conductance, magnetic_flux, magnetic_density, inductance, luminous_intensity
from sympy.physics.units.definitions import kilogram, newton, second, meter, gram, cd, K, joule, watt, pascal, hertz, coulomb, volt, ohm, siemens, farad, henry, tesla, weber, dioptre, lux, katal, gray, becquerel, inch, liter, julian_year, gravitational_constant, speed_of_light, elementary_charge, planck, hbar, electronvolt, avogadro_number, avogadro_constant, boltzmann_constant, electron_rest_mass, stefan_boltzmann_constant, Da, atomic_mass_constant, molar_gas_constant, faraday_constant, josephson_constant, von_klitzing_constant, acceleration_due_to_gravity, magnetic_constant, vacuum_permittivity, vacuum_impedance, coulomb_constant, atmosphere, bar, pound, psi, mmHg, milli_mass_unit, quart, lightyear, astronomical_unit, planck_mass, planck_time, planck_temperature, planck_length, planck_charge, planck_area, planck_volume, planck_momentum, planck_energy, planck_force, planck_power, planck_density, planck_energy_density, planck_intensity, planck_angular_frequency, planck_pressure, planck_current, planck_voltage, planck_impedance, planck_acceleration, bit, byte, kibibyte, mebibyte, gibibyte, tebibyte, pebibyte, exbibyte, curie, rutherford, radian, degree, steradian, angular_mil, atomic_mass_unit, gee, kPa, ampere, u0, c, kelvin, mol, mole, candela, m, kg, s, electric_constant, G, boltzmann
from sympy.physics.units.prefixes import PREFIXES, prefix_unit
from sympy.physics.units.systems.mksa import MKSA, dimsys_MKSA
derived_dims = (frequency, force, pressure, energy, power, charge, voltage, capacitance, conductance, magnetic_flux, magnetic_density, inductance, luminous_intensity)
base_dims = (amount_of_substance, luminous_intensity, temperature)
units = [
    mol,
    cd,
    K,
    lux,
    hertz,
    newton,
    pascal,
    joule,
    watt,
    coulomb,
    volt,
    farad,
    ohm,
    siemens,
    weber,
    tesla,
    henry,
    candela,
    lux,
    becquerel,
    gray,
    katal]
all_units: 'list[Quantity]' = []
# WARNING: Decompyle incomplete
