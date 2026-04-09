# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: concat.pyc (Python 3.11)

'''
Utility functions related to concat.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, cast
import numpy as np
from pandas._libs import lib
from pandas.util._decorators import set_module
from pandas.core.dtypes.astype import astype_array
from pandas.core.dtypes.cast import common_dtype_categorical_compat, find_common_type, np_find_common_type
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.generic import ABCCategoricalIndex, ABCSeries
if TYPE_CHECKING:
    from collections.abc import Sequence
    from pandas._typing import ArrayLike, AxisInt, DtypeObj
    from pandas.core.arrays import Categorical, ExtensionArray

def _is_nonempty(x = None, axis = None):
    if x.ndim <= axis:
        return True
    return None.shape[axis] > 0


def concat_compat(to_concat = None, axis = None, ea_compat_axis = None):
    """
    provide concatenation of an array of arrays each of which is a single
    'normalized' dtypes (in that for example, if it's object, then it is a
    non-datetimelike and provide a combined dtype for the resulting array that
    preserves the overall dtype if possible)

    Parameters
    ----------
    to_concat : sequence of arrays
    axis : axis to provide concatenation
    ea_compat_axis : bool, default False
        For ExtensionArray compat, behave as if axis == 1 when determining
        whether to drop empty arrays.

    Returns
    -------
    a single array, preserving the combined dtypes
    """
    pass
# WARNING: Decompyle incomplete


def _get_result_dtype(to_concat = None, non_empties = None):
    target_dtype = None
    dtypes = to_concat()
    kinds = to_concat()
    any_ea = (lambda .0: pass# WARNING: Decompyle incomplete
)(to_concat())
# WARNING: Decompyle incomplete

union_categoricals = (lambda to_union = None, sort_categories = None, ignore_order = set_module('pandas.api.types'): pass# WARNING: Decompyle incomplete
)()
