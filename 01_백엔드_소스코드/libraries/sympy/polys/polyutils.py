# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: polyutils.pyc (Python 3.11)

__doc__ = 'Useful utilities for higher level polynomial classes. '
from __future__ import annotations
from sympy.external.gmpy import GROUND_TYPES
from sympy.core import S, Add, Mul, Pow, Eq, Expr, expand_mul, expand_multinomial
from sympy.core.exprtools import decompose_power, decompose_power_rat
from sympy.core.numbers import _illegal
from sympy.polys.polyerrors import PolynomialError, GeneratorsError
from sympy.polys.polyoptions import build_options
import re
# WARNING: Decompyle incomplete
