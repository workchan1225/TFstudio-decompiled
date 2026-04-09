# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: boolean.pyc (Python 3.11)

from __future__ import annotations
import numbers
from typing import TYPE_CHECKING, ClassVar, Self, cast
import numpy as np
from pandas._libs import lib, missing as libmissing
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_list_like
from pandas.core.dtypes.dtypes import register_extension_dtype
from pandas.core.dtypes.missing import isna
from pandas.core import ops
from pandas.core.array_algos import masked_accumulations
from pandas.core.arrays.masked import BaseMaskedArray, BaseMaskedDtype
if TYPE_CHECKING:
    import pyarrow
    from pandas._typing import DtypeObj, npt, type_t
    from pandas.core.dtypes.dtypes import ExtensionDtype
BooleanDtype = <NODE:12>()()

def coerce_to_array(values = None, mask = register_extension_dtype, copy = set_module('pandas')):
    '''
    Coerce the input values array to numpy arrays with a mask.

    Parameters
    ----------
    values : 1D list-like
    mask : bool 1D array, optional
    copy : bool, default False
        if True, copy the input

    Returns
    -------
    tuple of (values, mask)
    '''
    pass
# WARNING: Decompyle incomplete

BooleanArray = <NODE:12>()
