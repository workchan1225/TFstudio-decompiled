# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: astype.pyc (Python 3.11)

"""
Functions for implementing 'astype' methods according to pandas conventions,
particularly ones that differ from numpy.
"""
from __future__ import annotations
import inspect
from typing import TYPE_CHECKING, overload
import warnings
import numpy as np
from pandas._libs import lib
from pandas._libs.tslibs.timedeltas import array_to_timedelta64
from pandas.errors import IntCastingNaNError
from pandas.core.dtypes.common import is_object_dtype, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, IntervalDtype, NumpyEADtype, PeriodDtype
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, DtypeObj, IgnoreRaise
    from pandas.core.arrays import ExtensionArray
_astype_nansafe = (lambda arr = None, dtype = None, copy = overload, skipna = (..., ...): pass)()
_astype_nansafe = (lambda arr = None, dtype = None, copy = overload, skipna = (..., ...): pass)()

def _astype_nansafe(arr = None, dtype = None, copy = None, skipna = (True, False)):
