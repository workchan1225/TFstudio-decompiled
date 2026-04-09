# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_parser.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
from copy import copy
import csv
from enum import Enum
import itertools
from typing import TYPE_CHECKING, Any, cast, final, overload
import warnings
import numpy as np
from pandas._libs import lib, parsers

ops
from pandas._libs.parsers import STR_NA_VALUES
import pandas._libs.ops, _libs
from pandas.compat._optional import import_optional_dependency
from pandas.errors import ParserError, ParserWarning
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import is_bool_dtype, is_dict_like, is_float_dtype, is_integer, is_integer_dtype, is_list_like, is_object_dtype, is_string_dtype
from pandas.core.dtypes.missing import isna
from pandas import DataFrame, DatetimeIndex, StringDtype
from pandas.core import algorithms
from pandas.core.arrays import ArrowExtensionArray, BaseMaskedArray, BooleanArray, FloatingArray, IntegerArray
from pandas.core.indexes.api import Index, MultiIndex, default_index, ensure_index_from_sequences
from pandas.core.series import Series
from pandas.core.tools import datetimes as tools
from pandas.io.common import is_potential_multi_index
if TYPE_CHECKING:
    from collections.abc import Callable, Iterable, Mapping, Sequence
    from pandas._typing import ArrayLike, DtypeArg, Hashable, HashableT, Scalar, SequenceT

class ParserBase:
    
    class usecols_dtype: 'str | None'(Enum):
        ERROR = 0
        WARN = 1
        SKIP = 2

    
    def __init__(self = None, kwds = None):
        self._implicit_index = False
        self.names = kwds.get('names')
        self.orig_names = None
        self.index_col = kwds.get('index_col', None)
        self.unnamed_cols = set()
        self.index_names = None
        self.col_names = None
        parse_dates = kwds.pop('parse_dates', False)
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        pass

    _should_parse_dates = (lambda self = None, i = None: if isinstance(self.parse_dates, bool):
self.parse_dates# WARNING: Decompyle incomplete
)()
    _extract_multi_indexer_columns = (lambda self = None, header = None, index_names = final, passed_names = (False,): pass# WARNING: Decompyle incomplete
)()
    _maybe_make_multi_index_columns = (lambda self = None, columns = None, col_names = final: if is_potential_multi_index(columns):
columns_mi = cast('Sequence[tuple[Hashable, ...]]', columns)MultiIndex.from_tuples(columns_mi, names = col_names))()
    _make_index = (lambda self = None, alldata = None, columns = final, indexnamerow = (None,): if isinstance(self.index_col, list) and len(self.index_col):
to_remove = []indexes = []for idx in self.index_col:
if isinstance(idx, str):
raise ValueError(f'''Index {idx} invalid''')to_remove.append(idx)indexes.append(alldata[idx])for i in sorted(to_remove, reverse = True):
alldata.pop(i)if not self._implicit_index:
columns.pop(i)index = self._agg_index(indexes)if indexnamerow:
coffset = len(indexnamerow) - len(columns)index = index.set_names(indexnamerow[:coffset])else:
index = Nonecolumns = self._maybe_make_multi_index_columns(columns, self.col_names)(index, columns))()
    _clean_mapping = (lambda self, mapping: pass# WARNING: Decompyle incomplete
)()
    _agg_index = (lambda self = None, index = final: arrays = []converters = self._clean_mapping(self.converters)clean_dtypes = self._clean_mapping(self.dtype)# WARNING: Decompyle incomplete
)()
    _set_noconvert_dtype_columns = (lambda self = None, col_indices = None, names = final: pass# WARNING: Decompyle incomplete
)()
    _infer_types = (lambda self = None, values = None, na_values = final, no_dtype_specified = (True,), try_num_bool = ('try_num_bool', 'bool', 'return', 'tuple[ArrayLike, int]'): na_count = 0if issubclass(values.dtype.type, (np.number, np.bool_)):
na_values = (lambda .0: pass# WARNING: Decompyle incomplete
)(na_values())
            mask = algorithms.isin(values, na_values)
            na_count = mask.astype('uint8', copy = False).sum()
            if na_count > 0:
                if is_integer_dtype(values):
                    values = values.astype(np.float64)
                np.putmask(values, mask, np.nan)
            return (values, na_count)
        dtype_backend = None.dtype_backend
    # WARNING: Decompyle incomplete
)()
    _do_date_conversions = (lambda self = None, names = None, data = overload: pass)()
    _do_date_conversions = (lambda self = None, names = None, data = overload: pass)()
    _do_date_conversions = (lambda self = None, names = None, data = final: if not isinstance(self.parse_dates, list):
datafor colspec in None.parse_dates:
if isinstance(colspec, int) and colspec not in data:
colspec = names[colspec]if (isinstance(self.index_col, list) or colspec in self.index_col or isinstance(self.index_names, list)) and colspec in self.index_names:
continueresult = date_converter(data[colspec], col = colspec, dayfirst = self.dayfirst, cache_dates = self.cache_dates, date_format = self.date_format)data[colspec] = resultdata)()
    _check_data_length = (lambda self = None, columns = None, data = final: if self.index_col or len(columns) != len(data) or columns:
if is_object_dtype(data[-1]):
empty_str = data[-1] == ''empty_str_or_na = empty_str | isna(data[-1])if len(columns) == len(data) - 1 and np.all(empty_str_or_na):
NoneNone.warn('Length of header or names does not match length of data. This leads to a loss of data with index_col=False.', ParserWarning, stacklevel = find_stack_level())Noneis_object_dtype(data[-1])None)()
    _validate_usecols_names = (lambda self = None, usecols = None, names = final: pass# WARNING: Decompyle incomplete
)()
    _clean_index_names = (lambda self = None, columns = None, index_col = final: if not is_index_col(index_col):
(None, columns, index_col)columns = None(columns)if not columns:
([
None] * len(index_col), columns, index_col)cp_cols = None(columns)index_names = []index_col = list(index_col)for i, c in enumerate(index_col):
if isinstance(c, str):
index_names.append(c)for j, name in enumerate(cp_cols):
if name == c:
index_col[i] = jcolumns.remove(name)name = cp_cols[c]columns.remove(name)index_names.append(name)for i, name in enumerate(index_names):
if isinstance(name, str) and name in self.unnamed_cols:
index_names[i] = None(index_names, columns, index_col))()
    _get_empty_meta = (lambda self = None, columns = None, dtype = final: pass# WARNING: Decompyle incomplete
)()


def date_converter(date_col = None, col = None, dayfirst = None, cache_dates = (False, True, None), date_format = ('col', 'Hashable', 'dayfirst', 'bool', 'cache_dates', 'bool', 'date_format', 'dict[Hashable, str] | str | None')):
    if date_col.dtype.kind in 'Mm':
        return date_col
    date_fmt = date_format.get(col) if None(date_format, dict) else date_format
    str_objs = lib.ensure_string_array(np.asarray(date_col))
    
    try:
        result = tools.to_datetime(str_objs, format = date_fmt, utc = False, dayfirst = dayfirst, cache = cache_dates)
    except (ValueError, TypeError):
        return 

    if isinstance(result, DatetimeIndex):
        True = result.to_numpy()
        return arr
    return None._values

# WARNING: Decompyle incomplete
