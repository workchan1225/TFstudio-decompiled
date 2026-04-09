# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: groupby.pyc (Python 3.11)

'''
Provide the groupby split-apply-combine paradigm. Define the GroupBy
class providing the base-class of operations.

The SeriesGroupBy and DataFrameGroupBy sub-class
(defined in pandas.core.groupby.generic)
expose these user-facing objects to provide specific functionality.
'''
from __future__ import annotations
from collections.abc import Callable, Hashable, Iterable, Iterator, Mapping, Sequence
import datetime
from functools import partial, wraps
from typing import TYPE_CHECKING, Concatenate, Literal, Self, TypeAlias, TypeVar, Union, cast, final, overload
import warnings
import numpy as np
from pandas._libs import Timestamp, lib
from pandas._libs.algos import rank_1d

groupby
from pandas._libs.missing import NA
import pandas._libs.groupby, _libs
from pandas._typing import AnyArrayLike, ArrayLike, DtypeObj, IndexLabel, IntervalClosedType, NDFrameT, PositionalIndexer, RandomState, npt
from pandas.compat.numpy import function as nv
from pandas.errors import AbstractMethodError, DataError, Pandas4Warning
from pandas.util._decorators import cache_readonly
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import coerce_indexer_dtype, ensure_dtype_can_hold_na
from pandas.core.dtypes.common import is_bool, is_bool_dtype, is_float_dtype, is_hashable, is_integer, is_integer_dtype, is_list_like, is_numeric_dtype, is_object_dtype, is_scalar, is_string_dtype, needs_i8_conversion, pandas_dtype
from pandas.core.dtypes.missing import isna, na_value_for_dtype, notna
from pandas.core import algorithms, sample
from pandas.core._numba import executor
from pandas.core.arrays import ArrowExtensionArray, BaseMaskedArray, ExtensionArray, FloatingArray, IntegerArray, SparseArray
from pandas.core.arrays.string_ import StringDtype
from pandas.core.arrays.string_arrow import ArrowStringArray
from pandas.core.base import PandasObject, SelectionMixin

common
from pandas.core.frame import DataFrame
import pandas.core.common, core
from pandas.core.generic import NDFrame
from pandas.core.groupby import base, numba_, ops
from pandas.core.groupby.grouper import get_grouper
from pandas.core.groupby.indexing import GroupByIndexingMixin, GroupByNthSelector
from pandas.core.indexes.api import Index, MultiIndex, default_index
from pandas.core.internals.blocks import ensure_block_shape
from pandas.core.series import Series
from pandas.core.sorting import get_group_index_sorter
from pandas.core.util.numba_ import get_jit_arguments, maybe_use_numba, prepare_function_arguments
if TYPE_CHECKING:
    from pandas._libs.tslibs import BaseOffset
    from pandas._libs.tslibs.timedeltas import Timedelta
    from pandas._typing import Any, P, T
    from pandas.core.indexers.objects import BaseIndexer
    from pandas.core.resample import Resampler
    from pandas.core.window import ExpandingGroupby, ExponentialMovingWindowGroupby, RollingGroupby
_groupby_agg_method_engine_template = "\nCompute {fname} of group values.\n\nParameters\n----------\nnumeric_only : bool, default {no}\n    Include only float, int, boolean columns.\n\n    .. versionchanged:: 2.0.0\n\n        numeric_only no longer accepts ``None``.\n\nmin_count : int, default {mc}\n    The required number of valid values to perform the operation. If fewer\n    than ``min_count`` non-NA values are present the result will be NA.\n\nengine : str, default None {e}\n    * ``'cython'`` : Runs rolling apply through C-extensions from cython.\n    * ``'numba'`` : Runs rolling apply through JIT compiled code from numba.\n        Only available when ``raw`` is set to ``True``.\n    * ``None`` : Defaults to ``'cython'`` or globally setting\n        ``compute.use_numba``\n\nengine_kwargs : dict, default None {ek}\n    * For ``'cython'`` engine, there are no accepted ``engine_kwargs``\n    * For ``'numba'`` engine, the engine can accept ``nopython``, ``nogil``\n        and ``parallel`` dictionary keys. The values must either be ``True`` or\n        ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is\n        ``{{'nopython': True, 'nogil': False, 'parallel': False}}`` and will be\n        applied to both the ``func`` and the ``apply`` groupby aggregation.\n\nReturns\n-------\nSeries or DataFrame\n    Computed {fname} of values within each group.\n\nSee Also\n--------\nSeriesGroupBy.min : Return the min of the group values.\nDataFrameGroupBy.min : Return the min of the group values.\nSeriesGroupBy.max : Return the max of the group values.\nDataFrameGroupBy.max : Return the max of the group values.\nSeriesGroupBy.sum : Return the sum of the group values.\nDataFrameGroupBy.sum : Return the sum of the group values.\n\nExamples\n--------\n{example}\n"
_groupby_agg_method_skipna_engine_template = "\nCompute {fname} of group values.\n\nParameters\n----------\nnumeric_only : bool, default {no}\n    Include only float, int, boolean columns.\n\n    .. versionchanged:: 2.0.0\n\n        numeric_only no longer accepts ``None``.\n\nmin_count : int, default {mc}\n    The required number of valid values to perform the operation. If fewer\n    than ``min_count`` non-NA values are present the result will be NA.\n\nskipna : bool, default {s}\n    Exclude NA/null values. If the entire group is NA and ``skipna`` is\n    ``True``, the result will be NA.\n\n    .. versionchanged:: 3.0.0\n\nengine : str, default None {e}\n    * ``'cython'`` : Runs rolling apply through C-extensions from cython.\n    * ``'numba'`` : Runs rolling apply through JIT compiled code from numba.\n        Only available when ``raw`` is set to ``True``.\n    * ``None`` : Defaults to ``'cython'`` or globally setting\n        ``compute.use_numba``\n\nengine_kwargs : dict, default None {ek}\n    * For ``'cython'`` engine, there are no accepted ``engine_kwargs``\n    * For ``'numba'`` engine, the engine can accept ``nopython``, ``nogil``\n        and ``parallel`` dictionary keys. The values must either be ``True`` or\n        ``False``. The default ``engine_kwargs`` for the ``'numba'`` engine is\n        ``{{'nopython': True, 'nogil': False, 'parallel': False}}`` and will be\n        applied to both the ``func`` and the ``apply`` groupby aggregation.\n\nReturns\n-------\nSeries or DataFrame\n    Computed {fname} of values within each group.\n\nSee Also\n--------\nSeriesGroupBy.min : Return the min of the group values.\nDataFrameGroupBy.min : Return the min of the group values.\nSeriesGroupBy.max : Return the max of the group values.\nDataFrameGroupBy.max : Return the max of the group values.\nSeriesGroupBy.sum : Return the sum of the group values.\nDataFrameGroupBy.sum : Return the sum of the group values.\n\nExamples\n--------\n{example}\n"
_pipe_template = '\nApply a ``func`` with arguments to this %(klass)s object and return its result.\n\nUse `.pipe` when you want to improve readability by chaining together\nfunctions that expect Series, DataFrames, GroupBy or Resampler objects.\nInstead of writing\n\n>>> h = lambda x, arg2, arg3: x + 1 - arg2 * arg3\n>>> g = lambda x, arg1: x * 5 / arg1\n>>> f = lambda x: x ** 4\n>>> df = pd.DataFrame([["a", 4], ["b", 5]], columns=["group", "value"])\n>>> h(g(f(df.groupby(\'group\')), arg1=1), arg2=2, arg3=3)  # doctest: +SKIP\n\nYou can write\n\n>>> (df.groupby(\'group\')\n...    .pipe(f)\n...    .pipe(g, arg1=1)\n...    .pipe(h, arg2=2, arg3=3))  # doctest: +SKIP\n\nwhich is much more readable.\n\nParameters\n----------\nfunc : callable or tuple of (callable, str)\n    Function to apply to this %(klass)s object or, alternatively,\n    a `(callable, data_keyword)` tuple where `data_keyword` is a\n    string indicating the keyword of `callable` that expects the\n    %(klass)s object.\n*args : iterable, optional\n       Positional arguments passed into `func`.\n**kwargs : dict, optional\n         A dictionary of keyword arguments passed into `func`.\n\nReturns\n-------\n%(klass)s\n    The original object with the function `func` applied.\n\nSee Also\n--------\nSeries.pipe : Apply a function with arguments to a series.\nDataFrame.pipe: Apply a function with arguments to a dataframe.\napply : Apply function to each group instead of to the\n    full %(klass)s object.\n\nNotes\n-----\nSee more `here\n<https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#piping-function-calls>`_\n\nExamples\n--------\n%(examples)s\n'
_transform_template = '\nCall function producing a same-indexed %(klass)s on each group.\n\nReturns a %(klass)s having the same indexes as the original object\nfilled with the transformed values.\n\nParameters\n----------\nfunc : function, str\n    Function to apply to each group. See the Notes section below for requirements.\n\n    Accepted inputs are:\n\n    - String\n    - Python function\n    - Numba JIT function with ``engine=\'numba\'`` specified.\n\n    Only passing a single function is supported with this engine.\n    If the ``\'numba\'`` engine is chosen, the function must be\n    a user defined function with ``values`` and ``index`` as the\n    first and second arguments respectively in the function signature.\n    Each group\'s index will be passed to the user defined function\n    and optionally available for use.\n\n    If a string is chosen, then it needs to be the name\n    of the groupby method you want to use.\n*args\n    Positional arguments to pass to func.\nengine : str, default None\n    * ``\'cython\'`` : Runs the function through C-extensions from cython.\n    * ``\'numba\'`` : Runs the function through JIT compiled code from numba.\n    * ``None`` : Defaults to ``\'cython\'`` or the global setting ``compute.use_numba``\n\nengine_kwargs : dict, default None\n    * For ``\'cython\'`` engine, there are no accepted ``engine_kwargs``\n    * For ``\'numba\'`` engine, the engine can accept ``nopython``, ``nogil``\n      and ``parallel`` dictionary keys. The values must either be ``True`` or\n      ``False``. The default ``engine_kwargs`` for the ``\'numba\'`` engine is\n      ``{\'nopython\': True, \'nogil\': False, \'parallel\': False}`` and will be\n      applied to the function\n\n**kwargs\n    Keyword arguments to be passed into func.\n\nReturns\n-------\n%(klass)s\n    %(klass)s with the same indexes as the original object filled\n    with transformed values.\n\nSee Also\n--------\n%(klass)s.groupby.apply : Apply function ``func`` group-wise and combine\n    the results together.\n%(klass)s.groupby.aggregate : Aggregate using one or more operations.\n%(klass)s.transform : Call ``func`` on self producing a %(klass)s with the\n    same axis shape as self.\n\nNotes\n-----\nEach group is endowed the attribute \'name\' in case you need to know\nwhich group you are working on.\n\nThe current implementation imposes three requirements on f:\n\n* f must return a value that either has the same shape as the input\n  subframe or can be broadcast to the shape of the input subframe.\n  For example, if `f` returns a scalar it will be broadcast to have the\n  same shape as the input subframe.\n* if this is a DataFrame, f must support application column-by-column\n  in the subframe. If f also supports application to the entire subframe,\n  then a fast path is used starting from the second chunk.\n* f must not mutate groups. Mutation is not supported and may\n  produce unexpected results. See :ref:`gotchas.udf-mutation` for more details.\n\nWhen using ``engine=\'numba\'``, there will be no "fall back" behavior internally.\nThe group data and group index will be passed as numpy arrays to the JITed\nuser defined function, and no alternative execution attempts will be tried.\n\nThe resulting dtype will reflect the return value of the passed ``func``,\nsee the examples below.\n\n.. versionchanged:: 2.0.0\n\n    When using ``.transform`` on a grouped DataFrame and the transformation function\n    returns a DataFrame, pandas now aligns the result\'s index\n    with the input\'s index. You can call ``.to_numpy()`` on the\n    result of the transformation function to avoid alignment.\n\nExamples\n--------\n%(example)s'
GroupByPlot = <NODE:12>()
_KeysArgType: 'TypeAlias' = Hashable | list[Hashable] | Callable[([
    Hashable], Hashable)] | list[Callable[([
    Hashable], Hashable)]] | Mapping[(Hashable, Hashable)]

def BaseGroupBy():
    '''BaseGroupBy'''
    _grouper: 'ops.BaseGrouper' = PandasObject._hidden_attrs | {
        'obj',
        'keys',
        'sort',
        'level',
        'dropna',
        'grouper',
        'as_index',
        'observed',
        'exclusions',
        'group_keys'}
    keys: '_KeysArgType | None' = None
    group_keys: 'bool' = None
    __len__ = (lambda self = None: self._grouper.ngroups)()
    __repr__ = (lambda self = None: object.__repr__(self))()
    groups = (lambda self = None: if isinstance(self.keys, list) and len(self.keys) == 1:
warnings.warn(f'''In a future version, the keys of `groups` will be a tuple with a single element, e.g. ({self.keys[0]},) , instead of a scalar, e.g. {self.keys[0]}, when grouping by a list with a single element. Use ``df.groupby(by=\'a\').groups`` instead of ``df.groupby(by=[\'a\']).groups`` to avoid this warning''', Pandas4Warning, stacklevel = find_stack_level())self._grouper.groups)()()
    ngroups = (lambda self = None: self._grouper.ngroups)()()
    indices = (lambda self = None: self._grouper.indices)()()
    _get_index = (lambda self, name: pass# WARNING: Decompyle incomplete
)()
    _selected_obj = (lambda self: if isinstance(self.obj, Series):
self.obj# WARNING: Decompyle incomplete
)()()
    _dir_additions = (lambda self = final: self.obj._dir_additions())()
    pipe = (lambda self = None, func = final: pass)()
    pipe = (lambda self = None, func = None: pass)()
    
    def pipe(self = None, func = None, *args, **kwargs):
        '''
        Apply a ``func`` with arguments to this GroupBy object and return its result.

        Use `.pipe` when you want to improve readability by chaining together
        functions that expect Series, DataFrames, GroupBy or Resampler objects.
        Instead of writing

        >>> h = lambda x, arg2, arg3: x + 1 - arg2 * arg3
        >>> g = lambda x, arg1: x * 5 / arg1
        >>> f = lambda x: x**4
        >>> df = pd.DataFrame([["a", 4], ["b", 5]], columns=["group", "value"])
        >>> h(g(f(df.groupby("group")), arg1=1), arg2=2, arg3=3)  # doctest: +SKIP

        You can write

        >>> (
        ...     df.groupby("group").pipe(f).pipe(g, arg1=1).pipe(h, arg2=2, arg3=3)
        ... )  # doctest: +SKIP

        which is much more readable.

        Parameters
        ----------
        func : callable or tuple of (callable, str)
            Function to apply to this GroupBy object or, alternatively,
            a `(callable, data_keyword)` tuple where `data_keyword` is a
            string indicating the keyword of `callable` that expects the
            GroupBy object.
        *args : iterable, optional
            Positional arguments passed into `func`.
        **kwargs : dict, optional
            A dictionary of keyword arguments passed into `func`.

        Returns
        -------
        GroupBy
            The return type of `func`.

        See Also
        --------
        Series.pipe : Apply a function with arguments to a series.
        DataFrame.pipe : Apply a function with arguments to a dataframe.
        apply : Apply function to each group instead of to the
            full GroupBy object.

        Notes
        -----
        See more `here
        <https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html#piping-function-calls>`_

        Examples
        --------
        >>> df = pd.DataFrame({"A": "a b a b".split(), "B": [1, 2, 3, 4]})
        >>> df
           A  B
        0  a  1
        1  b  2
        2  a  3
        3  b  4

        To get the difference between each groups maximum and minimum value in one
        pass, you can do

        >>> df.groupby("A").pipe(lambda x: x.max() - x.min())
           B
        A
        a  2
        b  2
        '''
        pass
    # WARNING: Decompyle incomplete

    get_group = (lambda self = None, name = None: keys = self.keyslevel = self.levelif (is_list_like(level) or len(level) == 1 or is_list_like(keys)) and len(keys) == 1:
if isinstance(name, tuple) and len(name) == 1:
name = name[0]else:
raise KeyError(name)inds = self._get_index(name)if not len(inds):
raise KeyError(name)self._selected_obj.iloc[inds])()
    __iter__ = (lambda self = None: keys = self.keyslevel = self.levelresult = self._grouper.get_iterator(self._selected_obj)if (is_list_like(level) or len(level) == 1 or isinstance(keys, list)) and len(keys) == 1:
result = result()result)()

BaseGroupBy = <NODE:27>(BaseGroupBy, 'BaseGroupBy', PandasObject, SelectionMixin[NDFrameT], GroupByIndexingMixin)
OutputFrameOrSeries = TypeVar('OutputFrameOrSeries', bound = NDFrame)

def GroupBy():
    '''GroupBy'''
    as_index: 'bool' = '\n    Class for grouping and aggregating relational data.\n\n    See aggregate, transform, and apply functions on this object.\n\n    It\'s easiest to use obj.groupby(...) to use GroupBy, but you can also do:\n\n    ::\n\n        grouped = groupby(obj, ...)\n\n    Parameters\n    ----------\n    obj : pandas object\n    level : int, default None\n        Level of MultiIndex\n    groupings : list of Grouping objects\n        Most users should ignore this\n    exclusions : array-like, optional\n        List of columns to exclude\n    name : str\n        Most users should ignore this\n\n    Returns\n    -------\n    **Attributes**\n    groups : dict\n        {group name -> group labels}\n    len(grouped) : int\n        Number of groups\n\n    Notes\n    -----\n    After grouping, see aggregate, apply, and transform functions. Here are\n    some other brief notes about usage. When grouping by multiple groups, the\n    result index will be a MultiIndex (hierarchical) by default.\n\n    Iteration produces (key, group) tuples, i.e. chunking the data by group. So\n    you can write code like:\n\n    ::\n\n        grouped = obj.groupby(keys)\n        for key, group in grouped:\n            # do something with the data\n\n    Function calls on GroupBy, if not specially implemented, "dispatch" to the\n    grouped data. So if you group a DataFrame and wish to invoke the std()\n    method on each group, you can simply do:\n\n    ::\n\n        df.groupby(mapper).std()\n\n    rather than\n\n    ::\n\n        df.groupby(mapper).aggregate(np.std)\n\n    You can pass arguments to these "wrapped" functions, too.\n\n    See the online documentation for full exposition on these topics and much\n    more\n    '
    __init__ = (lambda self, obj, keys, level, grouper, exclusions, selection, as_index = None, sort = None, group_keys = final, observed = (None, None, None, None, None, True, True, True, False, True), dropna = ('obj', 'NDFrameT', 'keys', '_KeysArgType | None', 'level', 'IndexLabel | None', 'grouper', 'ops.BaseGrouper | None', 'exclusions', 'frozenset[Hashable] | None', 'selection', 'IndexLabel | None', 'as_index', 'bool', 'sort', 'bool', 'group_keys', 'bool', 'observed', 'bool', 'dropna', 'bool', 'return', 'None'): self._selection = selection# WARNING: Decompyle incomplete
)()
    
    def __getattr__(self = None, attr = None):
        if attr in self._internal_names_set:
            return object.__getattribute__(self, attr)
        if None in self.obj:
            return self[attr]
        raise None(f'''\'{type(self).__name__}\' object has no attribute \'{attr}\'''')

    _op_via_apply = (lambda self = None, name = None: pass# WARNING: Decompyle incomplete
)()
    _concat_objects = (lambda self = None, values = None, not_indexed_same = final, is_transform = (False, False): concat = concatimport pandas.core.reshape.concatif not self.group_keys and is_transform:
if self.as_index:
group_keys = self._grouper.result_indexgroup_levels = self._grouper.levelsgroup_names = self._grouper.namesresult = concat(values, axis = 0, keys = group_keys, levels = group_levels, names = group_names, sort = False)else:
result = concat(values, axis = 0)elif not not_indexed_same:
result = concat(values, axis = 0)ax = self._selected_obj.indexif self.dropna:
labels = self._grouper.idsmask = labels != -1ax = ax[mask]if not ax.has_duplicates and result.axes[0].equals(ax):
target = algorithms.unique1d(ax._values)(indexer, _) = result.index.get_indexer_non_unique(target)result = result.take(indexer, axis = 0)else:
result = result.reindex(ax, axis = 0)else:
result = concat(values, axis = 0)if self.obj.ndim == 1:
name = self.obj.nameelif is_hashable(self._selection):
name = self._selectionelse:
name = None# WARNING: Decompyle incomplete
)()
    _set_result_index_ordered = (lambda self = None, result = None: index = self.obj.indexif not self._grouper.is_monotonic and self._grouper.has_dropped_na:
result = result.set_axis(index, axis = 0)resultoriginal_positions = None(self._grouper.result_ilocs, copy = False)result = result.set_axis(original_positions, axis = 0)result = result.sort_index(axis = 0)if self._grouper.has_dropped_na:
result = result.reindex(default_index(len(index)), axis = 0)result = result.set_axis(index, axis = 0)result)()
    _insert_inaxis_grouper = (lambda self = None, result = None, qs = final: if isinstance(result, Series):
result = result.to_frame()n_groupings = len(self._grouper.groupings)# WARNING: Decompyle incomplete
)()
    _wrap_aggregated_output = (lambda self = None, result = None, qs = final: if not self.as_index:
result = self._insert_inaxis_grouper(result, qs = qs)result = result._consolidate()result.index = default_index(len(result))# WARNING: Decompyle incomplete
)()
    
    def _wrap_applied_output(self = None, data = None, values = None, not_indexed_same = (False, False), is_transform = ('values', 'list', 'not_indexed_same', 'bool', 'is_transform', 'bool')):
        raise AbstractMethodError(self)

    _numba_prep = (lambda self = None, data = None: ngroups = self._grouper.ngroupssorted_index = self._grouper.result_ilocssorted_ids = self._grouper._sorted_idssorted_data = data.take(sorted_index, axis = 0).to_numpy()index_data = data.indexif isinstance(index_data, MultiIndex):
if len(self._grouper.groupings) > 1:
raise NotImplementedError("Grouping with more than 1 grouping labels and a MultiIndex is not supported with engine='numba'")group_key = self._grouper.groupings[0].nameindex_data = index_data.get_level_values(group_key)sorted_index_data = index_data.take(sorted_index).to_numpy()(starts, ends) = lib.generate_slices(sorted_ids, ngroups)(starts, ends, sorted_index_data, sorted_data))()
    
    def _numba_agg_general(self = None, func = None, dtype_mapping = None, engine_kwargs = ('func', 'Callable', 'dtype_mapping', 'dict[np.dtype, Any]', 'engine_kwargs', 'dict[str, bool] | None'), **aggregator_kwargs):
        '''
        Perform groupby with a standard numerical aggregation function (e.g. mean)
        with Numba.
        '''
        if not self.as_index:
            raise NotImplementedError('as_index=False is not supported. Use .reset_index() instead.')
        data = self._obj_with_exclusions
        df = data if data.ndim == 2 else data.to_frame()
    # WARNING: Decompyle incomplete

    _transform_with_numba = (lambda self = final, func = {
        'engine_kwargs': None }, *, engine_kwargs, args = None: data = self._obj_with_exclusionsindex_sorting = self._grouper.result_ilocsdf = data if data.ndim == 2 else data.to_frame()(starts, ends, sorted_index, sorted_data) = self._numba_prep(df)numba_.validate_udf(func)(args, kwargs) = prepare_function_arguments(func, args, kwargs, num_required_args = 2)# WARNING: Decompyle incomplete
)()
    _aggregate_with_numba = (lambda self = final, func = {
        'engine_kwargs': None }, *, engine_kwargs, args = None: data = self._obj_with_exclusionsdf = data if data.ndim == 2 else data.to_frame()(starts, ends, sorted_index, sorted_data) = self._numba_prep(df)numba_.validate_udf(func)(args, kwargs) = prepare_function_arguments(func, args, kwargs, num_required_args = 2)# WARNING: Decompyle incomplete
)()
    
    def apply(self = None, func = None, *, include_groups, *args, **kwargs):
        '''
        Apply function ``func`` group-wise and combine the results together.

        The function passed to ``apply`` must take a dataframe as its first
        argument and return a DataFrame, Series or scalar. ``apply`` will
        then take care of combining the results back together into a single
        dataframe or series. ``apply`` is therefore a highly flexible
        grouping method.

        While ``apply`` is a very flexible method, its downside is that
        using it can be quite a bit slower than using more specific methods
        like ``agg`` or ``transform``. Pandas offers a wide range of method that will
        be much faster than using ``apply`` for their specific purposes, so try to
        use them before reaching for ``apply``.

        Parameters
        ----------
        func : callable
            A callable that takes a dataframe as its first argument, and
            returns a dataframe, a series or a scalar. In addition the
            callable may take positional and keyword arguments.

        *args : tuple
            Optional positional arguments to pass to ``func``.

        include_groups : bool, default False
            When True, will attempt to apply ``func`` to the groupings in
            the case that they are columns of the DataFrame. If this raises a
            TypeError, the result will be computed with the groupings excluded.
            When False, the groupings will be excluded when applying ``func``.

            .. versionadded:: 2.2.0

            .. versionchanged:: 3.0.0

            The default changed from True to False, and True is no longer allowed.

        **kwargs : dict
            Optional keyword arguments to pass to ``func``.

        Returns
        -------
        Series or DataFrame
            A pandas object with the result of applying ``func`` to each group.

        See Also
        --------
        pipe : Apply function to the full GroupBy object instead of to each
            group.
        aggregate : Apply aggregate function to the GroupBy object.
        transform : Apply function column-by-column to the GroupBy object.
        Series.apply : Apply a function to a Series.
        DataFrame.apply : Apply a function to each row or column of a DataFrame.

        Notes
        -----
        The resulting dtype will reflect the return value of the passed ``func``,
        see the examples below.

        Functions that mutate the passed object can produce unexpected
        behavior or errors and are not supported. See :ref:`gotchas.udf-mutation`
        for more details.

        Examples
        --------
        >>> df = pd.DataFrame({"A": "a a b".split(), "B": [1, 2, 3], "C": [4, 6, 5]})
        >>> g1 = df.groupby("A", group_keys=False)
        >>> g2 = df.groupby("A", group_keys=True)

        Notice that ``g1`` and ``g2`` have two groups, ``a`` and ``b``, and only
        differ in their ``group_keys`` argument. Calling `apply` in various ways,
        we can get different grouping results:

        Example 1: below the function passed to `apply` takes a DataFrame as
        its argument and returns a DataFrame. `apply` combines the result for
        each group together into a new DataFrame:

        >>> g1[["B", "C"]].apply(lambda x: x / x.sum())
                  B    C
        0  0.333333  0.4
        1  0.666667  0.6
        2  1.000000  1.0

        In the above, the groups are not part of the index. We can have them included
        by using ``g2`` where ``group_keys=True``:

        >>> g2[["B", "C"]].apply(lambda x: x / x.sum())
                    B    C
        A
        a 0  0.333333  0.4
          1  0.666667  0.6
        b 2  1.000000  1.0

        Example 2: The function passed to `apply` takes a DataFrame as
        its argument and returns a Series.  `apply` combines the result for
        each group together into a new DataFrame.

        The resulting dtype will reflect the return value of the passed ``func``.

        >>> g1[["B", "C"]].apply(lambda x: x.astype(float).max() - x.min())
             B    C
        A
        a  1.0  2.0
        b  0.0  0.0

        >>> g2[["B", "C"]].apply(lambda x: x.astype(float).max() - x.min())
             B    C
        A
        a  1.0  2.0
        b  0.0  0.0

        The ``group_keys`` argument has no effect here because the result is not
        like-indexed (i.e. :ref:`a transform <groupby.transform>`) when compared
        to the input.

        Example 3: The function passed to `apply` takes a DataFrame as
        its argument and returns a scalar. `apply` combines the result for
        each group together into a Series, including setting the index as
        appropriate:

        >>> g1.apply(lambda x: x.C.max() - x.B.min())
        A
        a    5
        b    2
        dtype: int64

        Example 4: The function passed to ``apply`` returns ``None`` for one of the
        group. This group is filtered from the result:

        >>> g1.apply(lambda x: None if x.iloc[0, 0] == 3 else x)
           B  C
        0  1  4
        1  2  6
        '''
        pass
    # WARNING: Decompyle incomplete

    _python_apply_general = (lambda self, f = None, data = None, not_indexed_same = final, is_transform = (None, False, False), is_agg = ('f', 'Callable', 'data', 'DataFrame | Series', 'not_indexed_same', 'bool | None', 'is_transform', 'bool', 'is_agg', 'bool', 'return', 'NDFrameT'): (values, mutated) = self._grouper.apply_groupwise(f, data)# WARNING: Decompyle incomplete
)()
    _agg_general = (lambda self = None, numeric_only = None, min_count = None, *, alias, npfunc, kwargs = None: pass# WARNING: Decompyle incomplete
)()
    
    def _agg_py_fallback(self, how = None, values = None, ndim = None, alt = ('how', 'str', 'values', 'ArrayLike', 'ndim', 'int', 'alt', 'Callable', 'return', 'ArrayLike')):
        '''
        Fallback to pure-python aggregation if _cython_operation raises
        NotImplementedError.
        '''
        pass
    # WARNING: Decompyle incomplete

    _cython_agg_general = (lambda self = None, how = None, alt = final, numeric_only = (None, False, -1), min_count = ('how', 'str', 'alt', 'Callable | None', 'numeric_only', 'bool', 'min_count', 'int'): pass# WARNING: Decompyle incomplete
)()
    
    def _cython_transform(self = None, how = None, numeric_only = None, **kwargs):
        raise AbstractMethodError(self)

    _transform = (lambda self = final, func = {
        'engine': None,
        'engine_kwargs': None }, *, engine, engine_kwargs: pass# WARNING: Decompyle incomplete
)()
    _reduction_kernel_transform = (lambda self = final, func = {
        'engine': None,
        'engine_kwargs': None }, *, engine, engine_kwargs: com.temp_setattr(self, 'as_index', True)# WARNING: Decompyle incomplete
)()
    _wrap_transform_fast_result = (lambda self = None, result = None: obj = self._obj_with_exclusionsids = self._grouper.idsresult = result.reindex(self._grouper.result_index, axis = 0)if self.obj.ndim == 1:
out = algorithms.take_nd(result._values, ids)output = obj._constructor(out, index = obj.index, name = obj.name)else:
new_ax = result.index.take(ids)output = result._reindex_with_indexers({
0: (new_ax, ids) }, allow_dups = True)output = output.set_axis(obj.index, axis = 0)output)()
    _apply_filter = (lambda self, indices, dropna: if len(indices) == 0:
indices = np.array([], dtype = 'int64')else:
indices = np.sort(np.concatenate(indices))if dropna:
filtered = self._selected_obj.take(indices, axis = 0)else:
mask = np.empty(len(self._selected_obj.index), dtype = bool)mask.fill(False)mask[indices.astype(int)] = Truemask = np.tile(mask, mask[1]).Tfiltered = self._selected_obj.where(mask)filtered)()
    _cumcount_array = (lambda self = None, ascending = final: ids = self._grouper.idsngroups = self._grouper.ngroupssorter = get_group_index_sorter(ids, ngroups)count = len(ids)ids = ids[sorter]if count == 0:
np.empty(0, dtype = np.int64)run = None.r_[(True, ids[:-1] != ids[1:])]rep = np.diff(np.r_[(np.nonzero(run)[0], count)])out = ~run.cumsum()if ascending:
out -= np.repeat(out[run], rep)else:
out = np.repeat(out[np.r_[(run[1:], True)]], rep) - outif self._grouper.has_dropped_na:
out = np.where(ids == -1, np.nan, out.astype(np.float64, copy = False))else:
out = out.astype(np.int64, copy = False)rev = np.empty(count, dtype = np.intp)rev[sorter] = np.arange(count, dtype = np.intp)out[rev])()
    _obj_1d_constructor = (lambda self = None: if isinstance(self.obj, DataFrame):
self.obj._constructor_sliced# WARNING: Decompyle incomplete
)()()
    any = (lambda self = None, skipna = None: pass# WARNING: Decompyle incomplete
)()
    all = (lambda self = None, skipna = None: pass# WARNING: Decompyle incomplete
)()
    count = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    mean = (lambda self = None, numeric_only = None, skipna = final, engine = (False, True, None, None), engine_kwargs = ('numeric_only', 'bool', 'skipna', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None'): pass# WARNING: Decompyle incomplete
)()
    median = (lambda self = None, numeric_only = None, skipna = final: pass# WARNING: Decompyle incomplete
)()
    std = (lambda self, ddof = None, engine = None, engine_kwargs = final, numeric_only = (1, None, None, False, True), skipna = ('ddof', 'int', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None', 'numeric_only', 'bool', 'skipna', 'bool'): pass# WARNING: Decompyle incomplete
)()
    var = (lambda self, ddof = None, engine = None, engine_kwargs = final, numeric_only = (1, None, None, False, True), skipna = ('ddof', 'int', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None', 'numeric_only', 'bool', 'skipna', 'bool'): pass# WARNING: Decompyle incomplete
)()
    _value_counts = (lambda self, subset = None, normalize = None, sort = final, ascending = (None, False, True, False, True), dropna = ('subset', 'Sequence[Hashable] | None', 'normalize', 'bool', 'sort', 'bool', 'ascending', 'bool', 'dropna', 'bool', 'return', 'DataFrame | Series'): pass# WARNING: Decompyle incomplete
)()
    sem = (lambda self = None, ddof = None, numeric_only = final, skipna = (1, False, True): pass# WARNING: Decompyle incomplete
)()
    size = (lambda self = None: result = self._grouper.size()dtype_backend = Noneif isinstance(self.obj, Series):
if isinstance(self.obj.array, ArrowExtensionArray):
if isinstance(self.obj.array, ArrowStringArray):
if self.obj.array.dtype.na_value is np.nan:
dtype_backend = Noneelse:
dtype_backend = 'numpy_nullable'else:
dtype_backend = 'pyarrow'elif isinstance(self.obj.array, BaseMaskedArray):
dtype_backend = 'numpy_nullable'if isinstance(self.obj, Series):
result = self._obj_1d_constructor(result, name = self.obj.name)else:
result = self._obj_1d_constructor(result)# WARNING: Decompyle incomplete
)()
    sum = (lambda self, numeric_only = None, min_count = None, skipna = final, engine = (False, 0, True, None, None), engine_kwargs = ('numeric_only', 'bool', 'min_count', 'int', 'skipna', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None'): if maybe_use_numba(engine):
grouped_sum = grouped_sumimport pandas.core._numba.kernelsself._numba_agg_general(grouped_sum, executor.default_dtype_mapping, engine_kwargs, min_periods = min_count, skipna = skipna)None.temp_setattr(self, 'observed', True)result = self._agg_general(numeric_only = numeric_only, min_count = min_count, alias = 'sum', npfunc = np.sum, skipna = skipna)None(None, None))()
    prod = (lambda self = None, numeric_only = None, min_count = final, skipna = (False, 0, True): self._agg_general(numeric_only = numeric_only, min_count = min_count, skipna = skipna, alias = 'prod', npfunc = np.prod))()
    min = (lambda self, numeric_only = None, min_count = None, skipna = final, engine = (False, -1, True, None, None), engine_kwargs = ('numeric_only', 'bool', 'min_count', 'int', 'skipna', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None'): if maybe_use_numba(engine):
grouped_min_max = grouped_min_maximport pandas.core._numba.kernelsself._numba_agg_general(grouped_min_max, executor.identity_dtype_mapping, engine_kwargs, min_periods = min_count, is_max = False, skipna = skipna)None._agg_general(numeric_only = numeric_only, min_count = min_count, skipna = skipna, alias = 'min', npfunc = np.min))()
    max = (lambda self, numeric_only = None, min_count = None, skipna = final, engine = (False, -1, True, None, None), engine_kwargs = ('numeric_only', 'bool', 'min_count', 'int', 'skipna', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None'): if maybe_use_numba(engine):
grouped_min_max = grouped_min_maximport pandas.core._numba.kernelsself._numba_agg_general(grouped_min_max, executor.identity_dtype_mapping, engine_kwargs, min_periods = min_count, is_max = True, skipna = skipna)None._agg_general(numeric_only = numeric_only, min_count = min_count, skipna = skipna, alias = 'max', npfunc = np.max))()
    first = (lambda self = None, numeric_only = None, min_count = final, skipna = (False, -1, True): 
def first_compat(obj = None):

def first(x = None):
"""Helper function for first item that isn't NA."""
arr = x.array[notna(x.array)]if not len(arr):
x.array.dtype.na_valueNone[0]if isinstance(obj, DataFrame):
obj.apply(first)if None(obj, Series):
first(obj)raise None(type(obj))self._agg_general(numeric_only = numeric_only, min_count = min_count, alias = 'first', npfunc = first_compat, skipna = skipna))()
    last = (lambda self = None, numeric_only = None, min_count = final, skipna = (False, -1, True): 
def last_compat(obj = None):

def last(x = None):
"""Helper function for last item that isn't NA."""
arr = x.array[notna(x.array)]if not len(arr):
x.array.dtype.na_valueNone[-1]if isinstance(obj, DataFrame):
obj.apply(last)if None(obj, Series):
last(obj)raise None(type(obj))self._agg_general(numeric_only = numeric_only, min_count = min_count, alias = 'last', npfunc = last_compat, skipna = skipna))()
    ohlc = (lambda self = None: if self.obj.ndim == 1:
obj = self._selected_objis_numeric = is_numeric_dtype(obj.dtype)if not is_numeric:
raise DataError('No numeric types to aggregate')res_values = self._grouper._cython_operation('aggregate', obj._values, 'ohlc', axis = 0, min_count = -1)agg_names = [
'open',
'high',
'low',
'close']result = self.obj._constructor_expanddim(res_values, index = self._grouper.result_index, columns = agg_names)resultresult = None._apply_to_column_groupbys((lambda sgb: sgb.ohlc()))
        return result
)()
    
    def describe(self = None, percentiles = None, include = None, exclude = (None, None, None)):
        '''
        Generate descriptive statistics.

        Descriptive statistics include those that summarize the central
        tendency, dispersion and shape of a
        dataset\'s distribution, excluding ``NaN`` values.

        Analyzes both numeric and object series, as well
        as ``DataFrame`` column sets of mixed data types. The output
        will vary depending on what is provided. Refer to the notes
        below for more detail.

        Parameters
        ----------
        percentiles : list-like of numbers, optional
            The percentiles to include in the output. All should
            fall between 0 and 1. The default, ``None``, will automatically
            return the 25th, 50th, and 75th percentiles.
        include : \'all\', list-like of dtypes or None (default), optional
            A white list of data types to include in the result. Ignored
            for ``Series``. Here are the options:

            - \'all\' : All columns of the input will be included in the output.
            - A list-like of dtypes : Limits the results to the
              provided data types.
              To limit the result to numeric types submit
              ``numpy.number``. To limit it instead to object columns submit
              the ``numpy.object`` data type. Strings
              can also be used in the style of
              ``select_dtypes`` (e.g. ``df.describe(include=[\'O\'])``). To
              select pandas categorical columns, use ``\'category\'``
            - None (default) : The result will include all numeric columns.
        exclude : list-like of dtypes or None (default), optional,
            A black list of data types to omit from the result. Ignored
            for ``Series``. Here are the options:

            - A list-like of dtypes : Excludes the provided data types
              from the result. To exclude numeric types submit
              ``numpy.number``. To exclude object columns submit the data
              type ``numpy.object``. Strings can also be used in the style of
              ``select_dtypes`` (e.g. ``df.describe(exclude=[\'O\'])``). To
              exclude pandas categorical columns, use ``\'category\'``
            - None (default) : The result will exclude nothing.

        Returns
        -------
        Series or DataFrame
            Summary statistics of the Series or Dataframe provided.

        See Also
        --------
        DataFrame.count: Count number of non-NA/null observations.
        DataFrame.max: Maximum of the values in the object.
        DataFrame.min: Minimum of the values in the object.
        DataFrame.mean: Mean of the values.
        DataFrame.std: Standard deviation of the observations.
        DataFrame.select_dtypes: Subset of a DataFrame including/excluding
            columns based on their dtype.

        Notes
        -----
        For numeric data, the result\'s index will include ``count``,
        ``mean``, ``std``, ``min``, ``max`` as well as lower, ``50`` and
        upper percentiles. By default the lower percentile is ``25`` and the
        upper percentile is ``75``. The ``50`` percentile is the
        same as the median.

        For object data (e.g. strings), the result\'s index
        will include ``count``, ``unique``, ``top``, and ``freq``. The ``top``
        is the most common value. The ``freq`` is the most common value\'s
        frequency.

        If multiple object values have the highest count, then the
        ``count`` and ``top`` results will be arbitrarily chosen from
        among those with the highest count.

        For mixed data types provided via a ``DataFrame``, the default is to
        return only an analysis of numeric columns. If the DataFrame consists
        only of object and categorical data without any numeric columns, the
        default is to return an analysis of both the object and categorical
        columns. If ``include=\'all\'`` is provided as an option, the result
        will include a union of attributes of each type.

        The `include` and `exclude` parameters can be used to limit
        which columns in a ``DataFrame`` are analyzed for the output.
        The parameters are ignored when analyzing a ``Series``.

        Examples
        --------
        Describing a numeric ``Series``.

        >>> s = pd.Series([1, 2, 3])
        >>> s.describe()
        count    3.0
        mean     2.0
        std      1.0
        min      1.0
        25%      1.5
        50%      2.0
        75%      2.5
        max      3.0
        dtype: float64

        Describing a categorical ``Series``.

        >>> s = pd.Series(["a", "a", "b", "c"])
        >>> s.describe()
        count     4
        unique    3
        top       a
        freq      2
        dtype: object

        Describing a timestamp ``Series``.

        >>> s = pd.Series(
        ...     [
        ...         np.datetime64("2000-01-01"),
        ...         np.datetime64("2010-01-01"),
        ...         np.datetime64("2010-01-01"),
        ...     ]
        ... )
        >>> s.describe()
        count                      3
        mean     2006-09-01 08:00:00
        min      2000-01-01 00:00:00
        25%      2004-12-31 12:00:00
        50%      2010-01-01 00:00:00
        75%      2010-01-01 00:00:00
        max      2010-01-01 00:00:00
        dtype: object

        Describing a ``DataFrame``. By default only numeric fields
        are returned.

        >>> df = pd.DataFrame(
        ...     {
        ...         "categorical": pd.Categorical(["d", "e", "f"]),
        ...         "numeric": [1, 2, 3],
        ...         "object": ["a", "b", "c"],
        ...     }
        ... )
        >>> df.describe()
               numeric
        count      3.0
        mean       2.0
        std        1.0
        min        1.0
        25%        1.5
        50%        2.0
        75%        2.5
        max        3.0

        Describing all columns of a ``DataFrame`` regardless of data type.

        >>> df.describe(include="all")  # doctest: +SKIP
               categorical  numeric object
        count            3      3.0      3
        unique           3      NaN      3
        top              f      NaN      a
        freq             1      NaN      1
        mean           NaN      2.0    NaN
        std            NaN      1.0    NaN
        min            NaN      1.0    NaN
        25%            NaN      1.5    NaN
        50%            NaN      2.0    NaN
        75%            NaN      2.5    NaN
        max            NaN      3.0    NaN

        Describing a column from a ``DataFrame`` by accessing it as
        an attribute.

        >>> df.numeric.describe()
        count    3.0
        mean     2.0
        std      1.0
        min      1.0
        25%      1.5
        50%      2.0
        75%      2.5
        max      3.0
        Name: numeric, dtype: float64

        Including only numeric columns in a ``DataFrame`` description.

        >>> df.describe(include=[np.number])
               numeric
        count      3.0
        mean       2.0
        std        1.0
        min        1.0
        25%        1.5
        50%        2.0
        75%        2.5
        max        3.0

        Including only string columns in a ``DataFrame`` description.

        >>> df.describe(include=[object])  # doctest: +SKIP
               object
        count       3
        unique      3
        top         a
        freq        1

        Including only categorical columns from a ``DataFrame`` description.

        >>> df.describe(include=["category"])
               categorical
        count            3
        unique           3
        top              d
        freq             1

        Excluding numeric columns from a ``DataFrame`` description.

        >>> df.describe(exclude=[np.number])  # doctest: +SKIP
               categorical object
        count            3      3
        unique           3      3
        top              f      a
        freq             1      1

        Excluding object columns from a ``DataFrame`` description.

        >>> df.describe(exclude=[object])  # doctest: +SKIP
               categorical  numeric
        count            3      3.0
        unique           3      NaN
        top              f      NaN
        freq             1      NaN
        mean           NaN      2.0
        std            NaN      1.0
        min            NaN      1.0
        25%            NaN      1.5
        50%            NaN      2.0
        75%            NaN      2.5
        max            NaN      3.0
        '''
        pass
    # WARNING: Decompyle incomplete

    resample = (lambda self = None, rule = None, *, include_groups, args = None: get_resampler_for_grouping = get_resampler_for_groupingimport pandas.core.resampleif include_groups:
raise ValueError('include_groups=True is no longer allowed.')# WARNING: Decompyle incomplete
)()
    rolling = (lambda self, window, min_periods, center = None, win_type = None, on = final, closed = (None, False, None, None, None, 'single'), method = ('window', 'int | datetime.timedelta | str | BaseOffset | BaseIndexer', 'min_periods', 'int | None', 'center', 'bool', 'win_type', 'str | None', 'on', 'str | None', 'closed', 'IntervalClosedType | None', 'method', 'str', 'return', 'RollingGroupby'): RollingGroupby = RollingGroupbyimport pandas.core.windowRollingGroupby(self._selected_obj, window = window, min_periods = min_periods, center = center, win_type = win_type, on = on, closed = closed, method = method, _grouper = self._grouper, _as_index = self.as_index))()
    expanding = (lambda self = None, min_periods = None, method = final: ExpandingGroupby = ExpandingGroupbyimport pandas.core.windowExpandingGroupby(self._selected_obj, min_periods = min_periods, method = method, _grouper = self._grouper))()
    ewm = (lambda self, com, span, halflife, alpha, min_periods = None, adjust = None, ignore_na = final, times = (None, None, None, None, 0, True, False, None, 'single'), method = ('com', 'float | None', 'span', 'float | None', 'halflife', 'float | str | Timedelta | None', 'alpha', 'float | None', 'min_periods', 'int | None', 'adjust', 'bool', 'ignore_na', 'bool', 'times', 'np.ndarray | Series | None', 'method', 'str', 'return', 'ExponentialMovingWindowGroupby'): ExponentialMovingWindowGroupby = ExponentialMovingWindowGroupbyimport pandas.core.windowExponentialMovingWindowGroupby(self._selected_obj, com = com, span = span, halflife = halflife, alpha = alpha, min_periods = min_periods, adjust = adjust, ignore_na = ignore_na, times = times, method = method, _grouper = self._grouper))()
    _fill = (lambda self = None, direction = None, limit = final: pass# WARNING: Decompyle incomplete
)()
    ffill = (lambda self = None, limit = None: self._fill('ffill', limit = limit))()
    bfill = (lambda self = None, limit = None: self._fill('bfill', limit = limit))()
    nth = (lambda self = None: GroupByNthSelector(self))()()
    
    def _nth(self = None, n = None, dropna = None):
        if not dropna:
            mask = self._make_mask_from_positional_indexer(n)
            ids = self._grouper.ids
            mask = mask & (ids != -1)
            out = self._mask_selected_obj(mask)
            return out
        if not None(n):
            raise ValueError('dropna option only supported for an integer argument')
        if dropna not in ('any', 'all'):
            raise ValueError(f'''For a DataFrame or Series groupby.nth, dropna must be either None, \'any\' or \'all\', (was passed {dropna}).''')
        n = cast(int, n)
        dropped = self._selected_obj.dropna(how = dropna, axis = 0)
        if len(dropped) == len(self._selected_obj):
            grouper = self._grouper
        else:
            axis = self._grouper.axis
            grouper = self._grouper.codes_info[axis.isin(dropped.index)]
            if self._grouper.has_dropped_na:
                nulls = grouper == -1
                values = np.where(nulls, NA, grouper)
                grouper = Index(values, dtype = 'Int64', copy = False)
        grb = dropped.groupby(grouper, as_index = self.as_index, sort = self.sort)
        return grb.nth(n)

    quantile = (lambda self = None, q = None, interpolation = final, numeric_only = (0.5, 'linear', False): pass# WARNING: Decompyle incomplete
)()
    ngroup = (lambda self = None, ascending = None: obj = self._obj_with_exclusionsindex = obj.indexcomp_ids = self._grouper.idsif self._grouper.has_dropped_na:
comp_ids = np.where(comp_ids == -1, np.nan, comp_ids)dtype = np.float64else:
dtype = np.int64if (lambda .0: pass# WARNING: Decompyle incomplete
)(self._grouper.groupings()):
            comp_ids = rank_1d(comp_ids, ties_method = 'dense') - 1
        result = self._obj_1d_constructor(comp_ids, index, dtype = dtype)
        if not ascending:
            result = self.ngroups - 1 - result
        return result
)()
    cumcount = (lambda self = None, ascending = None: index = self._obj_with_exclusions.indexcumcounts = self._cumcount_array(ascending = ascending)self._obj_1d_constructor(cumcounts, index))()
    rank = (lambda self = None, method = None, ascending = final, na_option = ('average', True, 'keep', False), pct = ('method', 'str', 'ascending', 'bool', 'na_option', 'str', 'pct', 'bool', 'return', 'NDFrameT'): if na_option not in frozenset({'top', 'keep', 'bottom'}):
msg = "na_option must be one of 'keep', 'top', or 'bottom'"raise ValueError(msg)kwargs = {
'ties_method': method,
'ascending': ascending,
'na_option': na_option,
'pct': pct }# WARNING: Decompyle incomplete
)()
    cumprod = (lambda self = None, numeric_only = None: nv.validate_groupby_func('cumprod', args, kwargs, [
'skipna'])# WARNING: Decompyle incomplete
)()
    cumsum = (lambda self = None, numeric_only = None: nv.validate_groupby_func('cumsum', args, kwargs, [
'skipna'])# WARNING: Decompyle incomplete
)()
    cummin = (lambda self = None, numeric_only = None: skipna = kwargs.get('skipna', True)self._cython_transform('cummin', numeric_only = numeric_only, skipna = skipna))()
    cummax = (lambda self = None, numeric_only = None: skipna = kwargs.get('skipna', True)self._cython_transform('cummax', numeric_only = numeric_only, skipna = skipna))()
    shift = (lambda self = None, periods = None, freq = final, fill_value = (1, None, lib.no_default, None), suffix = ('periods', 'int | Sequence[int]', 'suffix', 'str | None'): pass# WARNING: Decompyle incomplete
)()
    diff = (lambda self = None, periods = None: pass# WARNING: Decompyle incomplete
)()
    pct_change = (lambda self = None, periods = None, fill_method = final, freq = (1, None, None): pass# WARNING: Decompyle incomplete
)()
    head = (lambda self = None, n = None: mask = self._make_mask_from_positional_indexer(slice(None, n))self._mask_selected_obj(mask))()
    tail = (lambda self = None, n = None: if n:
mask = self._make_mask_from_positional_indexer(slice(-n, None))else:
mask = self._make_mask_from_positional_indexer([])self._mask_selected_obj(mask))()
    _mask_selected_obj = (lambda self = None, mask = None: ids = self._grouper.idsmask = mask & (ids != -1)self._selected_obj[mask])()
    sample = (lambda self, n = None, frac = None, replace = final, weights = (None, None, False, None, None), random_state = ('n', 'int | None', 'frac', 'float | None', 'replace', 'bool', 'weights', 'Sequence | Series | None', 'random_state', 'RandomState | None'): if self._selected_obj.empty:
self._selected_objsize = None.process_sampling_size(n, frac, replace)# WARNING: Decompyle incomplete
)()
    
    def _idxmax_idxmin(self = None, how = None, ignore_unobserved = None, skipna = (False, True, False), numeric_only = ('how', "Literal['idxmax', 'idxmin']", 'ignore_unobserved', 'bool', 'skipna', 'bool', 'numeric_only', 'bool', 'return', 'NDFrameT')):
        """Compute idxmax/idxmin.

        Parameters
        ----------
        how : {'idxmin', 'idxmax'}
            Whether to compute idxmin or idxmax.
        numeric_only : bool, default False
            Include only float, int, boolean columns.
        skipna : bool, default True
            Exclude NA/null values. If an entire group is NA, the result will be NA.
        ignore_unobserved : bool, default False
            When True and an unobserved group is encountered, do not raise. This used
            for transform where unobserved groups do not play an impact on the result.

        Returns
        -------
        Series or DataFrame
            idxmax or idxmin for the groupby operation.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def _wrap_idxmax_idxmin(self = None, res = None, how = None, skipna = ('res', 'NDFrameT', 'how', "Literal['idxmax', 'idxmin']", 'skipna', 'bool', 'return', 'NDFrameT')):
        index = self.obj.index
        if res.size == 0:
            result = res.astype(index.dtype)
        elif skipna and res.lt(0).any(axis = None):
            raise ValueError(f'''{how} with skipna=True encountered all NA values in a group.''')
        if isinstance(index, MultiIndex):
            index = index.to_flat_index()
        values = res._values
    # WARNING: Decompyle incomplete


GroupBy = <NODE:27>(GroupBy, 'GroupBy', BaseGroupBy[NDFrameT])

def get_groupby(obj = None, by = None, grouper = final, group_keys = (None, None, True)):
    '''
    Class for grouping and aggregating relational data.

    See aggregate, transform, and apply functions on this object.

    It\'s easiest to use obj.groupby(...) to use GroupBy, but you can also do:

    ::

        grouped = groupby(obj, ...)

    Parameters
    ----------
    obj : pandas object
    level : int, default None
        Level of MultiIndex
    groupings : list of Grouping objects
        Most users should ignore this
    exclusions : array-like, optional
        List of columns to exclude
    name : str
        Most users should ignore this

    Returns
    -------
    **Attributes**
    groups : dict
        {group name -> group labels}
    len(grouped) : int
        Number of groups

    Notes
    -----
    After grouping, see aggregate, apply, and transform functions. Here are
    some other brief notes about usage. When grouping by multiple groups, the
    result index will be a MultiIndex (hierarchical) by default.

    Iteration produces (key, group) tuples, i.e. chunking the data by group. So
    you can write code like:

    ::

        grouped = obj.groupby(keys)
        for key, group in grouped:
            # do something with the data

    Function calls on GroupBy, if not specially implemented, "dispatch" to the
    grouped data. So if you group a DataFrame and wish to invoke the std()
    method on each group, you can simply do:

    ::

        df.groupby(mapper).std()

    rather than

    ::

        df.groupby(mapper).aggregate(np.std)

    You can pass arguments to these "wrapped" functions, too.

    See the online documentation for full exposition on these topics and much
    more
    '''
    if isinstance(obj, Series):
        SeriesGroupBy = SeriesGroupBy
        import pandas.core.groupby.generic
        return SeriesGroupBy(obj = obj, keys = by, grouper = grouper, group_keys = group_keys)
    if None(obj, DataFrame):
        DataFrameGroupBy = DataFrameGroupBy
        import pandas.core.groupby.generic
        return DataFrameGroupBy(obj = obj, keys = by, grouper = grouper, group_keys = group_keys)
    raise None(f'''invalid type: {obj}''')


def _insert_quantile_level(idx = None, qs = None):
    """
    Insert the sequence 'qs' of quantiles as the inner-most level of a MultiIndex.

    The quantile level in the MultiIndex is a repeated copy of 'qs'.

    Parameters
    ----------
    idx : Index
    qs : np.ndarray[float64]

    Returns
    -------
    MultiIndex
    """
    pass
# WARNING: Decompyle incomplete
