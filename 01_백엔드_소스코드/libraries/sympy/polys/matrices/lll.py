# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lll.pyc (Python 3.11)

from __future__ import annotations
from math import floor as mfloor
from sympy.polys.domains import ZZ, QQ
from sympy.polys.matrices.exceptions import DMRankError, DMShapeError, DMValueError, DMDomainError

def _ddm_lll(x, delta, return_transform = (QQ(3, 4), False)):
    pass
# WARNING: Decompyle incomplete


def ddm_lll(x, delta = (QQ(3, 4),)):
    return _ddm_lll(x, delta = delta, return_transform = False)[0]


def ddm_lll_transform(x, delta = (QQ(3, 4),)):
    return _ddm_lll(x, delta = delta, return_transform = True)
