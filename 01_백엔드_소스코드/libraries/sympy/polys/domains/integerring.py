# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: integerring.pyc (Python 3.11)

'''Implementation of :class:`IntegerRing` class. '''
from sympy.external.gmpy import MPZ, GROUND_TYPES
from sympy.core.numbers import int_valued
from sympy.polys.domains.groundtypes import SymPyInteger, factorial, gcdex, gcd, lcm, sqrt, is_square, sqrtrem
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.ring import Ring
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.polyerrors import CoercionFailed
from sympy.utilities import public
import math
IntegerRing = <NODE:12>()
ZZ = IntegerRing()
