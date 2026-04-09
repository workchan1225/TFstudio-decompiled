# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: expressiondomain.pyc (Python 3.11)

'''Implementation of :class:`ExpressionDomain` class. '''
from sympy.core import sympify, SympifyError
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.domains.characteristiczero import CharacteristicZero
from sympy.polys.domains.field import Field
from sympy.polys.domains.simpledomain import SimpleDomain
from sympy.polys.polyutils import PicklableWithSlots
from sympy.utilities import public
eflags = {
    'deep': False,
    'mul': True,
    'power_exp': False,
    'power_base': False,
    'basic': False,
    'multinomial': False,
    'log': False }
ExpressionDomain = <NODE:12>()
EX = ExpressionDomain()
