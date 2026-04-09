# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: inference.pyc (Python 3.11)

'''basic inference routines'''
from __future__ import annotations
from collections import abc
from numbers import Number
import re
from re import Pattern
from typing import TYPE_CHECKING, TypeGuard
import numpy as np
from pandas._libs import lib
from pandas.util._decorators import set_module
if TYPE_CHECKING:
    from collections.abc import Hashable
is_bool = lib.is_bool
is_integer = lib.is_integer
is_float = lib.is_float
is_complex = lib.is_complex
is_scalar = lib.is_scalar
is_decimal = lib.is_decimal
is_list_like = lib.is_list_like
is_iterator = lib.is_iterator
is_number = (lambda obj = None: isinstance(obj, (Number, np.number)))()

def iterable_not_string(obj = None):
