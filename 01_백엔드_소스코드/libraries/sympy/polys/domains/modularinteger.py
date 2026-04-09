# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: modularinteger.pyc (Python 3.11)

'''Implementation of :class:`ModularInteger` class. '''
from __future__ import annotations
from typing import Any
import operator
from sympy.polys.polyutils import PicklableWithSlots
from sympy.polys.polyerrors import CoercionFailed
from sympy.polys.domains.domainelement import DomainElement
from sympy.utilities import public
from sympy.utilities.exceptions import sympy_deprecation_warning
ModularInteger = <NODE:12>()
_modular_integer_cache: 'dict[tuple[Any, Any, Any], type[ModularInteger]]' = { }

def ModularIntegerFactory(_mod, _dom, _sym, parent):
    '''Create custom class for specific integer modulus.'''
    pass
# WARNING: Decompyle incomplete
