# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reshape.pyc (Python 3.11)

from __future__ import annotations
import itertools
from typing import TYPE_CHECKING, cast, overload
import warnings
import numpy as np
from pandas._config.config import get_option

reshape
from pandas.errors import Pandas4Warning, PerformanceWarning
PerformanceWarning = PerformanceWarning
import pandas._libs.reshape, _libs
from pandas.util._decorators import cache_readonly
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import find_common_type, maybe_promote
from pandas.core.dtypes.common import ensure_platform_int, is_1d_only_ea_dtype, is_integer, needs_i8_conversion
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.missing import isna, notna

algorithms
from pandas.core.algorithms import factorize, unique
unique = unique
import pandas.core.algorithms, core
from pandas.core.arrays._mixins import NDArrayBackedExtensionArray
from pandas.core.arrays.categorical import factorize_from_iterable
from pandas.core.construction import ensure_wrapped_if_datetimelike
from pandas.core.frame import DataFrame
from pandas.core.indexes.api import Index, MultiIndex, default_index
from pandas.core.reshape.concat import concat
from pandas.core.series import Series
from pandas.core.sorting import compress_group_index, decons_obs_group_ids, get_compressed_ids, get_group_index, get_group_index_sorter
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, Level, npt
    from pandas.core.arrays import ExtensionArray
    from pandas.core.indexes.frozen import FrozenList

class _Unstacker:
    '''
    Helper class to unstack data / pivot with multi-level index

    Parameters
    ----------
    index : MultiIndex
    level : int or str, default last level
        Level to "unstack". Accepts a name for the level.
    fill_value : scalar, optional
        Default value to fill in missing values if subgroups do not have the
        same set of labels. By default, missing values will be replaced with
        the default fill value for that data type, NaN for float, NaT for
        datetimelike, etc. For integer types, by default data will converted to
        float and missing values will be set to NaN.
    constructor : object
        Pandas ``DataFrame`` or subclass used to create unstacked
        response.  If None, DataFrame will be used.

    Examples
    --------
    >>> index = pd.MultiIndex.from_tuples(
    ...     [("one", "a"), ("one", "b"), ("two", "a"), ("two", "b")]
    ... )
    >>> s = pd.Series(np.arange(1, 5, dtype=np.int64), index=index)
    >>> s
    one  a    1
         b    2
    two  a    3
         b    4
    dtype: int64

    >>> s.unstack(level=-1)
         a  b
    one  1  2
    two  3  4

    >>> s.unstack(level=0)
       one  two
    a    1    3
    b    2    4

    Returns
    -------
    unstacked : DataFrame
    '''
    
    def __init__(self = None, index = None, level = None, constructor = (True,), sort = ('index', 'MultiIndex', 'level', 'Level', 'sort', 'bool', 'return', 'None')):
        self.constructor = constructor
        self.sort = sort
        self.index = index.remove_unused_levels()
        self.level = self.index._get_level_number(level)
        self.has_nan = -1 in self.index.codes[self.level]
        if self.has_nan:
            should_lift = self.sort
        self.lift = 1 if should_lift else 0
        self.new_index_levels = list(self.index.levels)
        self.new_index_names = list(self.index.names)
        self.removed_name = self.new_index_names.pop(self.level)
        self.removed_level = self.new_index_levels.pop(self.level)
        self.removed_level_full = index.levels[self.level]
        self.unique_nan_index = -1
        if not self.sort:
            unique_codes = unique(self.index.codes[self.level])
            if self.has_nan:
                nan_mask = unique_codes == -1
                unique_codes = unique_codes[~nan_mask]
                self.unique_nan_index = np.flatnonzero(nan_mask)[0]
            self.removed_level = self.removed_level.take(unique_codes)
            self.removed_level_full = self.removed_level_full.take(unique_codes)
        if get_option('performance_warnings'):
            num_rows = (lambda .0: pass# WARNING: Decompyle incomplete
)(self.new_index_levels())
            num_columns = self.removed_level.size
            num_cells = num_rows * num_columns
            if num_cells > np.iinfo(np.int32).max:
                warnings.warn(f'''The following operation may generate {num_cells} cells in the resulting pandas object.''', PerformanceWarning, stacklevel = find_stack_level())
        self._make_selectors()

    _indexer_and_to_sort = (lambda self = None: v = self.levelcodes = list(self.index.codes)if not self.sort:
codes = codes()levs = list(self.index.levels)to_sort = codes[:v] + codes[v + 1:] + [
codes[v]]sizes = (lambda .0: pass# WARNING: Decompyle incomplete
)(levs[:v] + levs[v + 1:] + [
            levs[v]]())
        (comp_index, obs_ids) = get_compressed_ids(to_sort, sizes)
        ngroups = len(obs_ids)
        indexer = get_group_index_sorter(comp_index, ngroups)
        return (indexer, to_sort)
)()
    sorted_labels = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _make_sorted_values(self = None, values = None):
        (indexer, _) = self._indexer_and_to_sort
        sorted_values = algos.take_nd(values, indexer, axis = 0)
        return sorted_values

    
    def _make_selectors(self = None):
        new_levels = self.new_index_levels
        remaining_labels = self.sorted_labels[:-1]
        level_sizes = (lambda .0: pass# WARNING: Decompyle incomplete
)(new_levels())
        (comp_index, obs_ids) = get_compressed_ids(remaining_labels, level_sizes)
        ngroups = len(obs_ids)
        comp_index = ensure_platform_int(comp_index)
        stride = self.index.levshape[self.level] + self.has_nan
        self.full_shape = (ngroups, stride)
        selector = self.sorted_labels[-1] + stride * comp_index + self.lift
        mask = np.zeros(np.prod(self.full_shape), dtype = bool)
        mask.put(selector, True)
        if mask.sum() < len(self.index):
            raise ValueError('Index contains duplicate entries, cannot reshape')
        self.group_index = comp_index
        self.mask = mask
        if self.sort:
            self.compressor = comp_index.searchsorted(np.arange(ngroups))
            return None
        self.compressor = tuple.sort(np.unique(comp_index, return_index = True)[1])

    mask_all = (lambda self = None: bool(self.mask.all()))()
    arange_result = (lambda self = None: dummy_arr = np.arange(len(self.index), dtype = np.intp)(new_values, mask) = self.get_new_values(dummy_arr, fill_value = -1)(new_values, mask.any(0)))()
    
    def get_result(self = None, obj = None, value_columns = None, fill_value = ('return', 'DataFrame')):
        values = obj._values
        if values.ndim == 1:
            values = values[(:, np.newaxis)]
    # WARNING: Decompyle incomplete

    
    def get_new_values(self, values, fill_value = (None,)):
        if values.ndim == 1:
            values = values[(:, np.newaxis)]
        sorted_values = self._make_sorted_values(values)
        (length, width) = self.full_shape
        stride = values.shape[1]
        result_width = width * stride
        result_shape = (length, result_width)
        mask = self.mask
        mask_all = self.mask_all
        if mask_all and len(values):
            new_values = sorted_values.reshape(length, width, stride).swapaxes(1, 2).reshape(result_shape)
            new_mask = np.ones(result_shape, dtype = bool)
            return (new_values, new_mask)
        dtype = None.dtype
        if isinstance(dtype, ExtensionDtype):
            cls = dtype.construct_array_type()
            new_values = cls._empty(result_shape, dtype = dtype)
            if not mask_all:
                new_values[:] = fill_value
            elif not mask_all:
                old_dtype = dtype
                (dtype, fill_value) = maybe_promote(dtype, fill_value)
                if old_dtype != dtype:
                    if old_dtype.kind not in 'iub':
                        warnings.warn('Using a fill_value that cannot be held in the existing dtype is deprecated and will raise in a future version.', Pandas4Warning, stacklevel = find_stack_level())
                    elif not isna(fill_value):
                        warnings.warn('Using a fill_value that cannot be held in the existing dtype is deprecated and will raise in a future version.', Pandas4Warning, stacklevel = find_stack_level())
        new_values = np.empty(result_shape, dtype = dtype)
        if not mask_all:
            new_values.fill(fill_value)
        name = dtype.name
        new_mask = np.zeros(result_shape, dtype = bool)
        if needs_i8_conversion(values.dtype):
            sorted_values = sorted_values.view('i8')
            new_values = new_values.view('i8')
        else:
            sorted_values = sorted_values.astype(name, copy = False)
        libreshape.unstack(sorted_values, mask.view('u1'), stride, length, width, new_values, new_mask.view('u1'))
        if needs_i8_conversion(values.dtype):
            new_values = new_values.view('M8[ns]')
            new_values = ensure_wrapped_if_datetimelike(new_values)
            new_values = new_values.view(values.dtype)
        return (new_values, new_mask)

    
    def get_new_columns(self = None, value_columns = None):
        pass
    # WARNING: Decompyle incomplete

    _repeater = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    new_index = (lambda self = None: pass# WARNING: Decompyle incomplete
)()


def _unstack_multiple(data = None, clocs = None, fill_value = None, sort = (None, True)):
    pass
# WARNING: Decompyle incomplete

unstack = (lambda obj = None, level = None, fill_value = overload, sort = (..., ...): pass)()
unstack = (lambda obj = None, level = None, fill_value = overload, sort = (..., ...): pass)()

def unstack(obj = None, level = None, fill_value = None, sort = (None, True)):
    if isinstance(level, (tuple, list)):
        if len(level) != 1:
            return _unstack_multiple(obj, level, fill_value = fill_value, sort = sort)
        level = None[0]
    if not is_integer(level) and level == '__placeholder__':
        obj.index._get_level_number(level)
    if isinstance(obj, DataFrame):
        if isinstance(obj.index, MultiIndex):
            return _unstack_frame(obj, level, fill_value = fill_value, sort = sort)
        return None.T.stack()
    if not None(obj.index, MultiIndex):
        raise ValueError(f'''index must be a MultiIndex to unstack, {type(obj.index)} was passed''')
    if is_1d_only_ea_dtype(obj.dtype):
        return _unstack_extension_series(obj, level, fill_value, sort = sort)
    unstacker = None(obj.index, level = level, constructor = obj._constructor_expanddim, sort = sort)
    return unstacker.get_result(obj, value_columns = None, fill_value = fill_value)


def _unstack_frame(obj = None, level = None, fill_value = None, sort = (None, True)):
    pass
# WARNING: Decompyle incomplete


def _unstack_extension_series(series = None, level = None, fill_value = None, sort = ('series', 'Series', 'sort', 'bool', 'return', 'DataFrame')):
    '''
    Unstack an ExtensionArray-backed Series.

    The ExtensionDtype is preserved.

    Parameters
    ----------
    series : Series
        A Series with an ExtensionArray for values
    level : Any
        The level name or number.
    fill_value : Any
        The user-level (not physical storage) fill value to use for
        missing values introduced by the reshape. Passed to
        ``series.values.take``.
    sort : bool
        Whether to sort the resulting MuliIndex levels

    Returns
    -------
    DataFrame
        Each column of the DataFrame will have the same dtype as
        the input Series.
    '''
    df = series.to_frame()
    result = df.unstack(level = level, fill_value = fill_value, sort = sort)
    result.columns = result.columns._drop_level_numbers([
        0])
    return result


def stack(frame = None, level = None, dropna = None, sort = (-1, True, True)):
    '''
    Convert DataFrame to Series with multi-level Index. Columns become the
    second level of the resulting hierarchical index

    Returns
    -------
    stacked : Series or DataFrame
    '''
    pass
# WARNING: Decompyle incomplete


def stack_multiple(frame = None, level = None, dropna = None, sort = (True, True)):
    pass
# WARNING: Decompyle incomplete


def _stack_multi_column_index(columns = None):
