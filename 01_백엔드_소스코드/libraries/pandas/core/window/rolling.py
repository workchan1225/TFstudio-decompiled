# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rolling.pyc (Python 3.11)

'''
Provide a generic structure to support window functions,
similar to how we have a Groupby object.
'''
from __future__ import annotations
import copy
from datetime import timedelta
from functools import partial
import inspect
from typing import TYPE_CHECKING, Any, Concatenate, Literal, Self, cast, final, overload
import numpy as np
from pandas._libs.tslibs import BaseOffset, Timedelta, to_offset


aggregations
from pandas.compat._optional import import_optional_dependency
import pandas._libs.window.aggregations, _libs, window
from pandas.errors import DataError
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import ensure_float64, is_bool, is_integer, is_numeric_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import ArrowDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.missing import notna
from pandas.core._numba import executor
from pandas.core.algorithms import factorize
from pandas.core.apply import ResamplerWindowApply, reconstruct_func
from pandas.core.arrays import ExtensionArray
from pandas.core.base import SelectionMixin

common
from pandas.core.indexers.objects import BaseIndexer, FixedWindowIndexer, GroupbyIndexer, VariableWindowIndexer
FixedWindowIndexer = FixedWindowIndexer
GroupbyIndexer = GroupbyIndexer
VariableWindowIndexer = VariableWindowIndexer
import pandas.core.common, core
from pandas.core.indexes.api import DatetimeIndex, Index, MultiIndex, PeriodIndex, TimedeltaIndex
from pandas.core.reshape.concat import concat
from pandas.core.util.numba_ import get_jit_arguments, maybe_use_numba, prepare_function_arguments
from pandas.core.window.common import flex_binary_moment, zsqrt
from pandas.core.window.numba_ import generate_manual_numpy_nan_agg_with_axis, generate_numba_apply_func, generate_numba_table_func
if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Hashable, Iterator, Sized
    from pandas._typing import ArrayLike, NDFrameT, QuantileInterpolation, P, TimeUnit, T, WindowingRankType, npt
    from pandas import DataFrame, Series
    from pandas.core.generic import NDFrame
    from pandas.core.groupby.ops import BaseGrouper
from pandas.core.arrays.datetimelike import dtype_to_unit

class BaseWindow(SelectionMixin):
    '''Provides utilities for performing windowing operations.'''
    _attributes: 'list[str]' = []
    _on: 'Index' = frozenset()
    
    def __init__(self, obj, window, min_periods = None, center = None, win_type = None, on = None, closed = (None, None, False, None, None, None, None, 'single'), step = {
        'selection': None }, method = ('obj', 'NDFrame', 'min_periods', 'int | None', 'center', 'bool | None', 'win_type', 'str | None', 'on', 'str | Index | None', 'closed', 'str | None', 'step', 'int | None', 'method', 'str', 'return', 'None'), *, selection):
        self.obj = obj
        self.on = on
        self.closed = closed
        self.step = step
        self.window = window
        self.min_periods = min_periods
        self.center = center
        self.win_type = win_type
        self.method = method
        self._win_freq_i8 = None
    # WARNING: Decompyle incomplete

    
    def _validate(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _check_window_bounds(self = None, start = None, end = None, num_vals = ('start', 'np.ndarray', 'end', 'np.ndarray', 'num_vals', 'int', 'return', 'None')):
        if len(start) != len(end):
            raise ValueError(f'''start ({len(start)}) and end ({len(end)}) bounds must be the same length''')
        if self.step and self.step or len(start) != (num_vals + 1 - 1) // 1:
            raise ValueError(f'''start and end bounds ({len(start)}) must be the same length as the object ({num_vals}) divided by the step ({self.step}) if given and rounded up''')

    
    def _slice_axis_for_step(self = None, index = None, result = None):
        '''
        Slices the index for a given result and the preset step.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _validate_numeric_only(self = None, name = None, numeric_only = None):
        '''
        Validate numeric_only argument, raising if invalid for the input.

        Parameters
        ----------
        name : str
            Name of the operator (kernel).
        numeric_only : bool
            Value passed by user.
        '''
        if not self._selected_obj.ndim == 1 or numeric_only or is_numeric_dtype(self._selected_obj.dtype):
            raise NotImplementedError(f'''{type(self).__name__}.{name} does not implement numeric_only''')
        return None
        return None

    
    def _make_numeric_only(self = None, obj = None):
        '''Subset DataFrame to numeric columns.

        Parameters
        ----------
        obj : DataFrame

        Returns
        -------
        obj subset to numeric-only columns.
        '''
        result = obj.select_dtypes(include = [
            'number'], exclude = [
            'timedelta'])
        return result

    
    def _create_data(self = None, obj = None, numeric_only = None):
        '''
        Split data into blocks & return conformed data.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _gotitem(self, key, ndim, subset = (None,)):
        '''
        Sub-classes to define. Return a sliced object.

        Parameters
        ----------
        key : str / list of selections
        ndim : {1, 2}
            requested ndim of result
        subset : object, default None
            subset to act on
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __getattr__(self = None, attr = None):
        if attr in self._internal_names_set:
            return object.__getattribute__(self, attr)
        if None in self.obj:
            return self[attr]
        raise None(f'''\'{type(self).__name__}\' object has no attribute \'{attr}\'''')

    
    def _dir_additions(self):
        return self.obj._dir_additions()

    
    def __repr__(self = None):
        '''
        Provide a nice str repr of our rolling object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _prep_values(self = None, values = None):
        '''Convert input to numpy arrays for Cython routines'''
        if needs_i8_conversion(values.dtype):
            raise NotImplementedError(f'''ops for {type(self).__name__} for this dtype {values.dtype} are not implemented''')
        
        try:
            if isinstance(values, ExtensionArray):
                values = values.to_numpy(np.float64, na_value = np.nan)
            else:
                values = ensure_float64(values)
        except (ValueError, TypeError):
            err = None
            raise TypeError(f'''cannot handle this type -> {values.dtype}'''), err
            err = None
            del err

        inf = np.isinf(values)
        if inf.any():
            values = np.where(inf, np.nan, values)
        return values

    
    def _insert_on_column(self = None, result = None, obj = None):
        Series = Series
        import pandas
    # WARNING: Decompyle incomplete

    _index_array = (lambda self = None: if isinstance(self._on, (PeriodIndex, DatetimeIndex, TimedeltaIndex)):
self._on.asi8if None(self._on.dtype, ArrowDtype) and self._on.dtype.kind in 'mM':
self._on.to_numpy(dtype = np.int64))()
    
    def _resolve_output(self = None, out = None, obj = None):
        '''Validate and finalize result.'''
        if out.shape[1] == 0 and obj.shape[1] > 0:
            raise DataError('No numeric types to aggregate')
        if out.shape[1] == 0:
            return obj.astype('float64')
        None._insert_on_column(out, obj)
        return out

    
    def _get_window_indexer(self = None):
        '''
        Return an indexer class that will compute the window start and end bounds
        '''
        if isinstance(self.window, BaseIndexer):
            return self.window
    # WARNING: Decompyle incomplete

    
    def _apply_series(self = None, homogeneous_func = None, name = None):
        '''
        Series version of _apply_columnwise
        '''
        obj = self._create_data(self._selected_obj)
        if name == 'count':
            obj = notna(obj).astype(int)
        
        try:
            values = self._prep_values(obj._values)
        except (TypeError, NotImplementedError):
            err = None
            raise DataError('No numeric types to aggregate'), err
            err = None
            del err

        result = homogeneous_func(values)
        index = self._slice_axis_for_step(obj.index, result)
        return obj._constructor(result, index = index, name = obj.name)

    
    def _apply_columnwise(self = None, homogeneous_func = None, name = None, numeric_only = (False,)):
        '''
        Apply the given function to the DataFrame broken down into homogeneous
        sub-frames.
        '''
        self._validate_numeric_only(name, numeric_only)
        if self._selected_obj.ndim == 1:
            return self._apply_series(homogeneous_func, name)
        obj = None._create_data(self._selected_obj, numeric_only)
        if name == 'count':
            obj = notna(obj).astype(int)
            obj._mgr = obj._mgr.consolidate()
        taker = []
        res_values = []
        for i, arr in enumerate(obj._iter_column_arrays()):
            arr = self._prep_values(arr)
        except (TypeError, NotImplementedError):
            err = None
            raise DataError(f'''Cannot aggregate non-numeric type: {arr.dtype}'''), err
            err = None
            del err
        res = homogeneous_func(arr)
        res_values.append(res)
        taker.append(i)
        continue
        index = self._slice_axis_for_step(obj.index, res_values[0] if len(res_values) > 0 else None)
        df = type(obj)._from_arrays(res_values, index = index, columns = obj.columns.take(taker), verify_integrity = False)
        return self._resolve_output(df, obj)

    
    def _apply_tablewise(self = None, homogeneous_func = None, name = None, numeric_only = (None, False)):
        '''
        Apply the given function to the DataFrame across the entire object
        '''
        if self._selected_obj.ndim == 1:
            raise ValueError("method='table' not applicable for Series objects.")
        obj = self._create_data(self._selected_obj, numeric_only)
        values = self._prep_values(obj.to_numpy())
        result = homogeneous_func(values)
        index = self._slice_axis_for_step(obj.index, result)
        columns = obj.columns if result.shape[1] == len(obj.columns) else obj.columns[::self.step]
        out = obj._constructor(result, index = index, columns = columns)
        return self._resolve_output(out, obj)

    
    def _apply_pairwise(self, target, other = None, pairwise = None, func = None, numeric_only = ('target', 'DataFrame | Series', 'other', 'DataFrame | Series | None', 'pairwise', 'bool | None', 'func', 'Callable[[DataFrame | Series, DataFrame | Series], DataFrame | Series]', 'numeric_only', 'bool', 'return', 'DataFrame | Series')):
        '''
        Apply the given pairwise function given 2 pandas objects (DataFrame/Series)
        '''
        target = self._create_data(target, numeric_only)
    # WARNING: Decompyle incomplete

    
    def _apply(self = None, func = None, name = None, numeric_only = (False, ()), numba_args = ('func', 'Callable[..., Any]', 'name', 'str', 'numeric_only', 'bool', 'numba_args', 'tuple[Any, ...]'), **kwargs):
        '''
        Rolling statistical measure using supplied function.

        Designed to be used with passed-in Cython array-based functions.

        Parameters
        ----------
        func : callable function to apply
        name : str,
        numba_args : tuple
            args to be passed when func is a numba func
        **kwargs
            additional arguments for rolling function and window function

        Returns
        -------
        y : type of input
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _numba_apply(self = None, func = None, engine_kwargs = None, **func_kwargs):
        window_indexer = self._get_window_indexer()
    # WARNING: Decompyle incomplete

    
    def aggregate(self, func = (None,), *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    agg = aggregate


class BaseWindowGroupby(BaseWindow):
    pass
# WARNING: Decompyle incomplete

Window = <NODE:12>()

class RollingAndExpandingMixin(BaseWindow):
    
    def count(self = None, numeric_only = None):
        window_func = window_aggregations.roll_sum
        return self._apply(window_func, name = 'count', numeric_only = numeric_only)

    
    def apply(self, func, raw = None, engine = None, engine_kwargs = None, args = (False, None, None, None, None), kwargs = ('func', 'Callable[..., Any]', 'raw', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None', 'args', 'tuple[Any, ...] | None', 'kwargs', 'dict[str, Any] | None')):
        pass
    # WARNING: Decompyle incomplete

    
    def _generate_cython_apply_func(self, args = None, kwargs = None, raw = None, function = ('args', 'tuple[Any, ...]', 'kwargs', 'dict[str, Any]', 'raw', 'bool | np.bool_', 'function', 'Callable[..., Any]', 'return', 'Callable[[np.ndarray, np.ndarray, np.ndarray, int], np.ndarray]')):
        pass
    # WARNING: Decompyle incomplete

    pipe = (lambda self = None, func = None: pass)()
    pipe = (lambda self = None, func = None: pass)()
    
    def pipe(self = None, func = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def sum(self = None, numeric_only = None, engine = None, engine_kwargs = (False, None, None)):
        if maybe_use_numba(engine):
            if self.method == 'table':
                func = generate_manual_numpy_nan_agg_with_axis(np.nansum)
                return self.apply(func, raw = True, engine = engine, engine_kwargs = engine_kwargs)
            sliding_sum = sliding_sum
            import pandas.core._numba.kernels
            return self._numba_apply(sliding_sum, engine_kwargs)
        window_func = None.roll_sum
        return self._apply(window_func, name = 'sum', numeric_only = numeric_only)

    
    def max(self = None, numeric_only = None, engine = None, engine_kwargs = (False, None, None)):
        if maybe_use_numba(engine):
            if self.method == 'table':
                func = generate_manual_numpy_nan_agg_with_axis(np.nanmax)
                return self.apply(func, raw = True, engine = engine, engine_kwargs = engine_kwargs)
            sliding_min_max = sliding_min_max
            import pandas.core._numba.kernels
            return self._numba_apply(sliding_min_max, engine_kwargs, is_max = True)
        window_func = None.roll_max
        return self._apply(window_func, name = 'max', numeric_only = numeric_only)

    
    def min(self = None, numeric_only = None, engine = None, engine_kwargs = (False, None, None)):
        if maybe_use_numba(engine):
            if self.method == 'table':
                func = generate_manual_numpy_nan_agg_with_axis(np.nanmin)
                return self.apply(func, raw = True, engine = engine, engine_kwargs = engine_kwargs)
            sliding_min_max = sliding_min_max
            import pandas.core._numba.kernels
            return self._numba_apply(sliding_min_max, engine_kwargs, is_max = False)
        window_func = None.roll_min
        return self._apply(window_func, name = 'min', numeric_only = numeric_only)

    
    def mean(self = None, numeric_only = None, engine = None, engine_kwargs = (False, None, None)):
        if maybe_use_numba(engine):
            if self.method == 'table':
                func = generate_manual_numpy_nan_agg_with_axis(np.nanmean)
                return self.apply(func, raw = True, engine = engine, engine_kwargs = engine_kwargs)
            sliding_mean = sliding_mean
            import pandas.core._numba.kernels
            return self._numba_apply(sliding_mean, engine_kwargs)
        window_func = None.roll_mean
        return self._apply(window_func, name = 'mean', numeric_only = numeric_only)

    
    def median(self = None, numeric_only = None, engine = None, engine_kwargs = (False, None, None)):
        if maybe_use_numba(engine):
            if self.method == 'table':
                func = generate_manual_numpy_nan_agg_with_axis(np.nanmedian)
            else:
                func = np.nanmedian
            return self.apply(func, raw = True, engine = engine, engine_kwargs = engine_kwargs)
        window_func = None.roll_median_c
        return self._apply(window_func, name = 'median', numeric_only = numeric_only)

    
    def std(self = None, ddof = None, numeric_only = None, engine = (1, False, None, None), engine_kwargs = ('ddof', 'int', 'numeric_only', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None')):
        pass
    # WARNING: Decompyle incomplete

    
    def var(self = None, ddof = None, numeric_only = None, engine = (1, False, None, None), engine_kwargs = ('ddof', 'int', 'numeric_only', 'bool', 'engine', "Literal['cython', 'numba'] | None", 'engine_kwargs', 'dict[str, bool] | None')):
        if maybe_use_numba(engine):
            if self.method == 'table':
                raise NotImplementedError("var not supported with method='table'")
            sliding_var = sliding_var
            import pandas.core._numba.kernels
            return self._numba_apply(sliding_var, engine_kwargs, ddof = ddof)
        window_func = None(window_aggregations.roll_var, ddof = ddof)
        return self._apply(window_func, name = 'var', numeric_only = numeric_only)

    
    def skew(self = None, numeric_only = None):
        window_func = window_aggregations.roll_skew
        return self._apply(window_func, name = 'skew', numeric_only = numeric_only)

    
    def sem(self = None, ddof = None, numeric_only = None):
        self._validate_numeric_only('sem', numeric_only)
        return self.std(numeric_only = numeric_only, ddof = ddof) / self.count(numeric_only = numeric_only).pow(0.5)

    
    def kurt(self = None, numeric_only = None):
        window_func = window_aggregations.roll_kurt
        return self._apply(window_func, name = 'kurt', numeric_only = numeric_only)

    
    def first(self = None, numeric_only = None):
        window_func = window_aggregations.roll_first
        return self._apply(window_func, name = 'first', numeric_only = numeric_only)

    
    def last(self = None, numeric_only = None):
        window_func = window_aggregations.roll_last
        return self._apply(window_func, name = 'last', numeric_only = numeric_only)

    
    def quantile(self = None, q = None, interpolation = None, numeric_only = ('linear', False)):
        if q == 1:
            window_func = window_aggregations.roll_max
        elif q == 0:
            window_func = window_aggregations.roll_min
        else:
            window_func = partial(window_aggregations.roll_quantile, quantile = q, interpolation = interpolation)
        return self._apply(window_func, name = 'quantile', numeric_only = numeric_only)

    
    def rank(self = None, method = None, ascending = None, pct = ('average', True, False, False), numeric_only = ('method', 'WindowingRankType', 'ascending', 'bool', 'pct', 'bool', 'numeric_only', 'bool')):
        window_func = partial(window_aggregations.roll_rank, method = method, ascending = ascending, percentile = pct)
        return self._apply(window_func, name = 'rank', numeric_only = numeric_only)

    
    def nunique(self = None, numeric_only = None):
        window_func = partial(window_aggregations.roll_nunique)
        return self._apply(window_func, name = 'nunique', numeric_only = numeric_only)

    
    def cov(self = None, other = None, pairwise = None, ddof = (None, None, 1, False), numeric_only = ('other', 'DataFrame | Series | None', 'pairwise', 'bool | None', 'ddof', 'int', 'numeric_only', 'bool')):
        pass
    # WARNING: Decompyle incomplete

    
    def corr(self = None, other = None, pairwise = None, ddof = (None, None, 1, False), numeric_only = ('other', 'DataFrame | Series | None', 'pairwise', 'bool | None', 'ddof', 'int', 'numeric_only', 'bool')):
        pass
    # WARNING: Decompyle incomplete


Rolling = <NODE:12>()
Rolling.__doc__ = Window.__doc__
RollingGroupby = <NODE:12>()
