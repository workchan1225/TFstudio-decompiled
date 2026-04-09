# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rationalfield.pyc (Python 3.11)

'''Implementation of :class:`RationalField` class. '''
from sympy.external.gmpy import MPQ
from sympy.polys.domains.groundtypes import SymPyRational, is_square, sqrtrem
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.polyerrors import CoercionFailed
from sympy.utilities import public
RationalField = <NODE:12>()
QQ = RationalField()
