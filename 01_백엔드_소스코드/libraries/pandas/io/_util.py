# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Literal
import numpy as np
from pandas._config import using_string_dtype
from pandas._libs import lib
from pandas.compat import pa_version_under18p0, pa_version_under19p0
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.common import pandas_dtype
import pandas as pd
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Sequence
    import pyarrow
    from pandas._typing import DtypeArg, DtypeBackend

def _arrow_dtype_mapping():
    pa = import_optional_dependency('pyarrow')
    return {
        pa.large_string(): pd.StringDtype(),
        pa.string(): pd.StringDtype(),
        pa.float64(): pd.Float64Dtype(),
        pa.float32(): pd.Float32Dtype(),
        pa.string(): pd.StringDtype(),
        pa.bool_(): pd.BooleanDtype(),
        pa.uint64(): pd.UInt64Dtype(),
        pa.uint32(): pd.UInt32Dtype(),
        pa.uint16(): pd.UInt16Dtype(),
        pa.uint8(): pd.UInt8Dtype(),
        pa.int64(): pd.Int64Dtype(),
        pa.int32(): pd.Int32Dtype(),
        pa.int16(): pd.Int16Dtype(),
        pa.int8(): pd.Int8Dtype() }


def _arrow_string_types_mapper():
    pa = import_optional_dependency('pyarrow')
    mapping = {
        pa.large_string(): pd.StringDtype(na_value = np.nan),
        pa.string(): pd.StringDtype(na_value = np.nan) }
    if not pa_version_under18p0:
        mapping[pa.string_view()] = pd.StringDtype(na_value = np.nan)
    return mapping.get


def arrow_table_to_pandas(table, dtype_backend = None, null_to_int64 = None, to_pandas_kwargs = None, dtype = (lib.no_default, False, None, None, None), names = ('table', 'pyarrow.Table', 'dtype_backend', "DtypeBackend | Literal['numpy'] | lib.NoDefault", 'null_to_int64', 'bool', 'to_pandas_kwargs', 'dict | None', 'dtype', 'DtypeArg | None', 'names', 'Sequence[Hashable] | None', 'return', 'pd.DataFrame')):
    pa = import_optional_dependency('pyarrow')
# WARNING: Decompyle incomplete


def _post_convert_dtypes(df = None, dtype_backend = None, dtype = None, names = ('df', 'pd.DataFrame', 'dtype_backend', "DtypeBackend | Literal['numpy'] | lib.NoDefault", 'dtype', 'DtypeArg | None', 'names', 'Sequence[Hashable] | None', 'return', 'pd.DataFrame')):
    pass
# WARNING: Decompyle incomplete
