# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: domain.pyc (Python 3.11)

'''Implementation of :class:`Domain` class. '''
from __future__ import annotations
from typing import Any
from sympy.core.numbers import AlgebraicNumber
from sympy.core import Basic, sympify
from sympy.core.sorting import ordered
from sympy.external.gmpy import GROUND_TYPES
from sympy.polys.domains.domainelement import DomainElement
from sympy.polys.orderings import lex
from sympy.polys.polyerrors import UnificationFailed, CoercionFailed, DomainError
from sympy.polys.polyutils import _unify_gens, _not_a_coeff
from sympy.utilities import public
from sympy.utilities.iterables import is_sequence
Domain = <NODE:12>()
__all__ = [
    'Domain']
