# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: string_arrow.pyc (Python 3.11)

from __future__ import annotations
import operator
import re
from typing import TYPE_CHECKING, Self
import numpy as np
from pandas._libs import lib, missing as libmissing
from pandas.compat import HAS_PYARROW, PYARROW_MIN_VERSION, pa_version_under16p0
from pandas.util._decorators import set_module
from pandas.util._validators import validate_na_arg
from pandas.core.dtypes.common import is_scalar, pandas_dtype
from pandas.core.dtypes.missing import isna
from pandas.core.arrays._arrow_string_mixins import ArrowStringArrayMixin
from pandas.core.arrays.arrow import ArrowExtensionArray
from pandas.core.arrays.boolean import BooleanDtype
from pandas.core.arrays.floating import Float64Dtype
from pandas.core.arrays.integer import Int64Dtype
from pandas.core.arrays.numeric import NumericDtype
from pandas.core.arrays.string_ import BaseStringArray, StringDtype
from pandas.core.strings.object_array import ObjectStringArrayMixin
if HAS_PYARROW:
    import pyarrow as pa
    from pyarrow.compute import compute as pc
if TYPE_CHECKING:
    from collections.abc import Callable, Sequence
    from pandas._typing import ArrayLike, Dtype, NpDtype, Scalar, npt
    from pandas.core.dtypes.dtypes import ExtensionDtype
    from pandas import Series

def _check_pyarrow_available():
    if not HAS_PYARROW:
        msg = f'''pyarrow>={PYARROW_MIN_VERSION} is required for PyArrow backed ArrowExtensionArray.'''
        raise ImportError(msg)


def _is_string_view(typ):
    if not pa_version_under16p0:
        pass
    return pa.types.is_string_view(typ)

ArrowStringArray = <NODE:12>()
