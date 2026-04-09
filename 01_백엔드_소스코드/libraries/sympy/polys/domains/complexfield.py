# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: complexfield.pyc (Python 3.11)

'''Implementation of :class:`ComplexField` class. '''
from sympy.external.gmpy import SYMPY_INTS
from sympy.core.numbers import Float, I
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.gaussiandomains import QQ_I
from sympy.polys.domains.mpelements import MPContext
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.polyerrors import DomainError, CoercionFailed
from sympy.utilities import public
ComplexField = <NODE:12>()
CC = ComplexField()
