# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: putmask.pyc (Python 3.11)

'''
EA-compatible analogue to np.putmask
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas._libs import lib
from pandas.core.dtypes.cast import infer_dtype_from
from pandas.core.dtypes.common import is_list_like
from pandas.core.arrays import ExtensionArray
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, npt
    from pandas import MultiIndex

def putmask_inplace(values = None, mask = None, value = None):
