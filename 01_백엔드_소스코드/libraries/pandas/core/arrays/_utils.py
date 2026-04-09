# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas._config import is_nan_na
from pandas._libs import lib
from pandas._libs.missing import NA
from pandas.errors import LossySetitemError
from pandas.core.dtypes.cast import np_can_hold_element
from pandas.core.dtypes.common import is_numeric_dtype
if TYPE_CHECKING:
    from pandas._typing import npt
    from pandas.core.arrays.base import ExtensionArray

def to_numpy_dtype_inference(arr = None, dtype = None, na_value = None, hasna = ('arr', 'ExtensionArray', 'dtype', 'npt.DTypeLike | None', 'hasna', 'bool', 'return', 'tuple[np.dtype | None, Any]')):
    inferred_numeric_dtype = False
# WARNING: Decompyle incomplete
