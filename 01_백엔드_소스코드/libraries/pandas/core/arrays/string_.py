# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: string_.pyc (Python 3.11)

from __future__ import annotations
from functools import partial
import operator
from pathlib import Path
from typing import TYPE_CHECKING, Any, Literal, Self, cast
import warnings
import numpy as np
from pandas._config import get_option, using_string_dtype
from pandas._libs import lib, missing as libmissing
from pandas._libs.arrays import NDArrayBacked
from pandas._libs.lib import ensure_string_array
from pandas.compat import HAS_PYARROW, PYARROW_MIN_VERSION
from pandas.compat.numpy import function as nv
from pandas.errors import Pandas4Warning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.base import ExtensionDtype, StorageExtensionDtype, register_extension_dtype
from pandas.core.dtypes.common import is_array_like, is_bool_dtype, is_integer_dtype, is_object_dtype, is_string_dtype, pandas_dtype
from pandas.core import missing, nanops, ops, roperator
from pandas.core.algorithms import isin
from pandas.core.array_algos import masked_reductions
from pandas.core.arrays.base import ExtensionArray
from pandas.core.arrays.floating import FloatingArray, FloatingDtype
from pandas.core.arrays.integer import IntegerArray, IntegerDtype
from pandas.core.arrays.numpy_ import NumpyExtensionArray
from pandas.core.construction import extract_array
from pandas.core.indexers import check_array_indexer
from pandas.core.missing import isna
from pandas.io.formats import printing
if HAS_PYARROW:
    import pyarrow as pa
    from pyarrow.compute import compute as pc
if TYPE_CHECKING:
    from collections.abc import MutableMapping
    import pyarrow
    from pandas._typing import ArrayLike, AxisInt, Dtype, DtypeObj, NumpySorter, NumpyValueArrayLike, Scalar, npt, type_t
    from pandas import Series
StringDtype = <NODE:12>()()

class BaseStringArray(ExtensionArray):
    pass
# WARNING: Decompyle incomplete

StringArray = <NODE:12>()
