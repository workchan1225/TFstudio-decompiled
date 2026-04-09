# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ops.pyc (Python 3.11)

'''
Provide classes to perform the groupby aggregate operations.

These are not exposed to the user and provide implementations of the grouping
operations, primarily in cython. These classes (BaseGrouper and BinGrouper)
are contained *in* the SeriesGroupBy and DataFrameGroupBy objects.
'''
from __future__ import annotations
import collections
import functools
from typing import TYPE_CHECKING, Any, Generic, final
import numpy as np
from pandas._libs import NaT, lib

groupby
from pandas._typing import ArrayLike, AxisInt, NDFrameT, Shape, npt
AxisInt = AxisInt
NDFrameT = NDFrameT
Shape = Shape
npt = npt
import pandas._libs.groupby, _libs
from pandas.errors import AbstractMethodError
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.cast import maybe_downcast_to_dtype
from pandas.core.dtypes.common import ensure_float64, ensure_int64, ensure_platform_int, ensure_uint64, is_1d_only_ea_dtype
from pandas.core.dtypes.missing import isna, maybe_fill
from pandas.core.arrays import Categorical
from pandas.core.frame import DataFrame
from pandas.core.groupby import grouper
from pandas.core.indexes.api import CategoricalIndex, Index, MultiIndex, ensure_index
from pandas.core.series import Series
from pandas.core.sorting import compress_group_index, decons_obs_group_ids, get_group_index, get_group_index_sorter, get_indexer_dict
if TYPE_CHECKING:
    from collections.abc import Callable, Generator, Hashable, Iterator
    from pandas.core.generic import NDFrame

def check_result_array(obj = None, dtype = None):
    if isinstance(obj, np.ndarray) or dtype != object:
        raise ValueError('Must produce aggregated value')
    return None


def extract_result(res):
    '''
    Extract the result object, it might be a 0-dim ndarray
    or a len-1 0-dim, or a scalar
    '''
    if hasattr(res, '_values'):
        res = res._values
        if res.ndim == 1 and len(res) == 1:
            res = res[0]
    return res


class WrappedCythonOp:
    __module__ = __name__
    __qualname__ = 'WrappedCythonOp'
    __doc__ = '\n    Dispatch logic for functions defined in _libs.groupby\n\n    Parameters\n    ----------\n    kind: str\n        Whether the operation is an aggregate or transform.\n    how: str\n        Operation name, e.g. "mean".\n    has_dropped_na: bool\n        True precisely when dropna=True and the grouper contains a null value.\n    '
    cast_blocklist = frozenset([
        'any',
        'all',
        'rank',
        'count',
        'size',
        'idxmin',
        'idxmax'])
    
    def __init__(self = None, kind = None, how = None, has_dropped_na = ('kind', 'str', 'how', 'str', 'has_dropped_na', 'bool', 'return', 'None')):
        self.kind = kind
        self.how = how
        self.has_dropped_na = has_dropped_na

# WARNING: Decompyle incomplete


class BaseGrouper:
    axis: 'Index' = '\n    This is an internal Grouper class, which actually holds\n    the generated groups\n\n    Parameters\n    ----------\n    axis : Index\n    groupings : Sequence[Grouping]\n        all the grouping instances to handle in this grouper\n        for example for grouper list to groupby, need to pass the list\n    sort : bool, default True\n        whether this grouper will give sorted result or not\n\n    '
    
    def __init__(self = None, axis = None, groupings = None, sort = (True, True), dropna = ('axis', 'Index', 'groupings', 'list[grouper.Grouping]', 'sort', 'bool', 'dropna', 'bool', 'return', 'None')):
        pass
    # WARNING: Decompyle incomplete

    groupings = (lambda self = None: self._groupings)()
    
    def __iter__(self = None):
        return iter(self.indices)

    nkeys = (lambda self = None: len(self.groupings))()
    
    def get_iterator(self = None, data = None):
        '''
        Groupby iterator

        Returns
        -------
        Generator yielding sequence of (name, subsetted object)
        for each group
        '''
        pass
    # WARNING: Decompyle incomplete

    _get_splitter = (lambda self = None, data = None: if isinstance(data, Series):
klass = SeriesSplitterelse:
klass = FrameSplitterklass(data, self.ngroups, sorted_ids = self._sorted_ids, sort_idx = self.result_ilocs))()
    indices = (lambda self = None: if not self.dropna:
has_mi = isinstance(self.result_index, MultiIndex)if has_mi and self.result_index.hasnans:
result = result.items()()elif has_mi:
result = result.items()()result)()
    result_ilocs = (lambda self = None: ids = self.idsif self.has_dropped_na:
mask = np.where(ids >= 0)null_gaps = np.cumsum(ids == -1)[mask]ids = ids[mask]result = get_group_index_sorter(ids, self.ngroups)if self.has_dropped_na:
result += np.take(null_gaps, result)result)()()
    codes = (lambda self = None: self.groupings())()
    levels = (lambda self = None: if len(self.groupings) > 1:
list(self.result_index.levels)[
None.result_index])()
    names = (lambda self = None: self.groupings())()
    size = (lambda self = None: ids = self.idsngroups = self.ngroupsif ngroups:
out = np.bincount(ids[ids != -1], minlength = ngroups)else:
out = []Series(out, index = self.result_index, dtype = 'int64', copy = False))()
    groups = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    is_monotonic = (lambda self = None: Index(self.ids, copy = False).is_monotonic_increasing)()()
    has_dropped_na = (lambda self = None: bool((self.ids < 0).any()))()()
    codes_info = (lambda self = None: self.ids)()
    ngroups = (lambda self = None: len(self.result_index))()()
    result_index = (lambda self = None: self.result_index_and_ids[0])()
    ids = (lambda self = None: self.result_index_and_ids[1])()
    result_index_and_ids = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    observed_grouper = (lambda self = None: if (lambda .0: pass# WARNING: Decompyle incomplete
)(self.groupings()):
            return self
        return all._observed_grouper
)()
    _observed_grouper = (lambda self = None: groupings = self.groupings()grouper = BaseGrouper(self.axis, groupings, sort = self._sort, dropna = self.dropna)grouper)()
    
    def _ob_index_and_ids(self, levels = None, codes = None, names = None, sorts = ('levels', 'list[Index]', 'codes', 'list[npt.NDArray[np.intp]]', 'names', 'list[Hashable]', 'sorts', 'list[bool]', 'return', 'tuple[MultiIndex, npt.NDArray[np.intp]]')):
        pass
    # WARNING: Decompyle incomplete

    
    def _unob_index_and_ids(self = None, levels = None, codes = None, names = ('levels', 'list[Index]', 'codes', 'list[npt.NDArray[np.intp]]', 'names', 'list[Hashable]', 'return', 'tuple[MultiIndex, npt.NDArray[np.intp]]')):
        shape = (lambda .0: pass# WARNING: Decompyle incomplete
)(levels())
        unob_ids = get_group_index(codes, shape, sort = True, xnull = True)
        unob_index = MultiIndex.from_product(levels, names = names)
        unob_ids = ensure_platform_int(unob_ids)
        return (unob_index, unob_ids)

    get_group_levels = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _cython_operation = (lambda self, kind = None, values = None, how = final, axis = (-1,), min_count = ('kind', 'str', 'how', 'str', 'axis', 'AxisInt', 'min_count', 'int', 'return', 'ArrayLike'): pass# WARNING: Decompyle incomplete
)()
    agg_series = (lambda self = None, obj = None, func = final, preserve_dtype = (False,): result = self._aggregate_series_pure_python(obj, func)obj.array._cast_pointwise_result(result))()
    _aggregate_series_pure_python = (lambda self = None, obj = None, func = final: result = np.empty(self.ngroups, dtype = 'O')initialized = Falsesplitter = self._get_splitter(obj)for i, group in enumerate(splitter):
res = func(group)res = extract_result(res)if not initialized:
check_result_array(res, group.dtype)initialized = Trueresult[i] = resresult)()
    apply_groupwise = (lambda self = None, f = None, data = final: mutated = Falsesplitter = self._get_splitter(data)group_keys = self.result_indexresult_values = []zipped = zip(group_keys, splitter, strict = True)for key, group in zipped:
object.__setattr__(group, 'name', key)group_axes = group.axesres = f(group)if not mutated and _is_indexed_like(res, group_axes):
mutated = Trueresult_values.append(res)if len(group_keys) == 0 and getattr(f, '__name__', None) in ('skew', 'kurt', 'sum', 'prod'):
f(data.iloc[:0])(result_values, mutated))()
    _sorted_ids = (lambda self = None: result = self.ids.take(self.result_ilocs)if getattr(self, 'dropna', True):
result = result[result >= 0]result)()()


class BinGrouper(BaseGrouper):
    binlabels: 'Index' = "\n    This is an internal Grouper class\n\n    Parameters\n    ----------\n    bins : the split index of binlabels to group the item of axis\n    binlabels : the label list\n    indexer : np.ndarray[np.intp], optional\n        the indexer created by Grouper\n        some groupers (TimeGrouper) will sort its axis and its\n        group_info is also sorted, so need the indexer to reorder\n\n    Examples\n    --------\n    bins: [2, 4, 6, 8, 10]\n    binlabels: DatetimeIndex(['2005-01-01', '2005-01-03',\n        '2005-01-05', '2005-01-07', '2005-01-09'],\n        dtype='datetime64[ns]', freq='2D')\n\n    the group_info, which contains the label of each item in grouped\n    axis, the index of label in label list, group number, is\n\n    (array([0, 0, 1, 1, 2, 2, 3, 3, 4, 4]), array([0, 1, 2, 3, 4]), 5)\n\n    means that, the grouped axis has 10 items, can be grouped into 5\n    labels, the first and second items belong to the first label, the\n    third and forth items belong to the second label, and so on\n\n    "
    
    def __init__(self = None, bins = None, binlabels = None, indexer = (None,)):
        self.bins = ensure_int64(bins)
        self.binlabels = ensure_index(binlabels)
        self.indexer = indexer
    # WARNING: Decompyle incomplete

    groups = (lambda self: result = zip(self.binlabels, self.bins, strict = True)()result)()
    nkeys = (lambda self = None: 1)()
    codes_info = (lambda self = None: ids = self.ids# WARNING: Decompyle incomplete
)()
    
    def get_iterator(self = None, data = None):
        '''
        Groupby iterator

        Returns
        -------
        Generator yielding sequence of (name, subsetted object)
        for each group
        '''
        pass
    # WARNING: Decompyle incomplete

    indices = (lambda self: indices = collections.defaultdict(list)i = 0for label, bin in zip(self.binlabels, self.bins, strict = True):
if i < bin:
if label is not NaT:
indices[label] = list(range(i, bin))i = binindices)()
    codes = (lambda self = None: [
self.ids])()
    result_index_and_ids = (lambda self: result_index = self.binlabelsif len(self.binlabels) != 0 and isna(self.binlabels[0]):
result_index = result_index[1:]ngroups = len(result_index)rep = np.diff(np.r_[(0, self.bins)])rep = ensure_platform_int(rep)if ngroups == len(self.bins):
ids = np.repeat(np.arange(ngroups), rep)else:
ids = np.repeat(np.r_[(-1, np.arange(ngroups))], rep)ids = ensure_platform_int(ids)(result_index, ids))()
    levels = (lambda self = None: [
self.binlabels])()
    names = (lambda self = None: [
self.binlabels.name])()
    groupings = (lambda self = None: lev = self.binlabelscodes = self.idslabels = lev.take(codes)ping = grouper.Grouping(labels, labels, in_axis = False, level = None, uniques = lev._values)[
ping])()
    observed_grouper = (lambda self = None: self)()


def _is_indexed_like(obj = None, axes = None):
    if isinstance(obj, Series):
        if len(axes) > 1:
            return False
        return None.index.equals(axes[0])
    if None(obj, DataFrame):
        return obj.index.equals(axes[0])


def DataSplitter():
    '''DataSplitter'''
    
    def __init__(self = None, data = None, ngroups = None, *, sort_idx, sorted_ids):
        self.data = data
        self.ngroups = ngroups
        self._slabels = sorted_ids
        self._sort_idx = sort_idx

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    _sorted_data = (lambda self = None: self.data.take(self._sort_idx, axis = 0))()
    
    def _chop(self = None, sdata = None, slice_obj = None):
        raise AbstractMethodError(self)


DataSplitter = <NODE:27>(DataSplitter, 'DataSplitter', Generic[NDFrameT])

class SeriesSplitter(DataSplitter):
    
    def _chop(self = None, sdata = None, slice_obj = None):
        mgr = sdata._mgr.get_slice(slice_obj)
        ser = sdata._constructor_from_mgr(mgr, axes = mgr.axes)
        ser._name = sdata.name
        return ser.__finalize__(sdata, method = 'groupby')



class FrameSplitter(DataSplitter):
    
    def _chop(self = None, sdata = None, slice_obj = None):
        mgr = sdata._mgr.get_slice(slice_obj, axis = 1)
        df = sdata._constructor_from_mgr(mgr, axes = mgr.axes)
        return df.__finalize__(sdata, method = 'groupby')
