# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: algebraicfield.pyc (Python 3.11)

'''Implementation of :class:`AlgebraicField` class. '''
from sympy.core.add import Add
from sympy.core.mul import Mul
from sympy.core.singleton import S
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.polyclasses import ANP
from sympy.polys.polyerrors import CoercionFailed, DomainError, NotAlgebraic, IsomorphismFailed
from sympy.utilities import public
AlgebraicField = <NODE:12>()

def _make_converter(K):
    '''Construct the converter to convert back to Expr'''
    pass
# WARNING: Decompyle incomplete
