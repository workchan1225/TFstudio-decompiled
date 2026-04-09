# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpy_.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal, Self, cast
import numpy as np
from pandas._libs import lib
from pandas._libs.tslibs import is_supported_dtype
from pandas.compat.numpy import function as nv
from pandas.util._decorators import set_module
from pandas.core.dtypes.astype import astype_array, astype_is_view
from pandas.core.dtypes.cast import construct_1d_object_array_from_listlike, maybe_downcast_to_dtype
from pandas.core.dtypes.common import pandas_dtype
from pandas.core.dtypes.dtypes import NumpyEADtype
from pandas.core.dtypes.missing import isna
from pandas.core import arraylike, missing, nanops, ops
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
from pandas.core.construction import ensure_wrapped_if_datetimelike
from pandas.core.strings.object_array import ObjectStringArrayMixin
if TYPE_CHECKING:
    from collections.abc import Callable
    from pandas._typing import ArrayLike, AxisInt, Dtype, FillnaOptions, InterpolateOptions, NpDtype, Scalar, TakeIndexer, npt
    from pandas import Index
    from pandas.arrays import StringArray
NumpyExtensionArray = <NODE:12>()
