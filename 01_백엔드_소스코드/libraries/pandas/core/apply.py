# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: apply.pyc (Python 3.11)

from __future__ import annotations
import abc
from collections import defaultdict
from collections.abc import Callable
import functools
from functools import partial
import inspect
from typing import TYPE_CHECKING, Any, Literal, TypeAlias, cast
import numpy as np
from pandas._libs.internals import BlockValuesRefs
from pandas._typing import AggFuncType, AggFuncTypeBase, AggFuncTypeDict, AggObjType, Axis, AxisInt, NDFrameT, npt
from pandas.compat._optional import import_optional_dependency
from pandas.errors import SpecificationError
from pandas.util._decorators import cache_readonly, set_module
from pandas.core.dtypes.cast import is_nested_object
from pandas.core.dtypes.common import is_dict_like, is_extension_array_dtype, is_list_like, is_numeric_dtype, is_sequence
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCNDFrame, ABCSeries
from pandas.core._numba.executor import generate_apply_looper

common
from pandas.core.construction import ensure_wrapped_if_datetimelike
import pandas.core.common, core
from pandas.core.util.numba_ import get_jit_arguments, prepare_function_arguments
if TYPE_CHECKING:
    from collections.abc import Generator, Hashable, Iterable, MutableMapping, Sequence
    from pandas import DataFrame, Index, Series
    from pandas.core.groupby import GroupBy
    from pandas.core.resample import Resampler
    from pandas.core.window.rolling import BaseWindow
ResType: 'TypeAlias' = dict[(int, Any)]
BaseExecutionEngine = <NODE:12>()

def frame_apply(obj, func, axis, raw, result_type, by_row = None, engine = None, engine_kwargs = set_module('pandas.api.executors'), args = (0, False, None, 'compat', 'python', None, None, None), kwargs = ('obj', 'DataFrame', 'func', 'AggFuncType', 'axis', 'Axis', 'raw', 'bool', 'result_type', 'str | None', 'by_row', "Literal[False, 'compat']", 'engine', 'str', 'engine_kwargs', 'dict[str, bool] | None', 'return', 'FrameApply')):
    '''construct and return a row or column based frame apply object'''
    pass
# WARNING: Decompyle incomplete


def Apply():
    '''Apply'''
    axis: 'AxisInt' = 'Apply'
    
    def __init__(self = None, obj = None, func = None, raw = None, result_type = {
        'by_row': 'compat',
        'engine': 'python',
        'engine_kwargs': None }, *, by_row, engine, engine_kwargs, args, kwargs):
        self.obj = obj
        self.raw = raw
    # WARNING: Decompyle incomplete

    apply = (lambda self = None: pass)()
    agg_or_apply_list_like = (lambda self = None, op_name = None: pass)()
    agg_or_apply_dict_like = (lambda self = None, op_name = None: pass)()
    
    def agg(self = None):
        '''
        Provide an implementation for the aggregators.

        Returns
        -------
        Result of aggregation, or None if agg cannot be performed by
        this method.
        '''
        func = self.func
        if isinstance(func, str):
            return self.apply_str()
        if None(func):
            return self.agg_dict_like()
        if None(func):
            return self.agg_list_like()

    
    def transform(self = None):
        '''
        Transform a DataFrame or Series.

        Returns
        -------
        DataFrame or Series
            Result of applying ``func`` along the given axis of the
            Series or DataFrame.

        Raises
        ------
        ValueError
            If the transform function fails or does not transform.
        '''
        obj = self.obj
        func = self.func
        axis = self.axis
        args = self.args
        kwargs = self.kwargs
        is_series = obj.ndim == 1
    # WARNING: Decompyle incomplete

    
    def transform_dict_like(self = None, func = None):
        '''
        Compute transform in the case of a dict-like func
        '''
        concat = concat
        import pandas.core.reshape.concat
        obj = self.obj
        args = self.args
        kwargs = self.kwargs
    # WARNING: Decompyle incomplete

    
    def transform_str_or_callable(self = None, func = None):
        '''
        Compute transform in the case of a string or callable func
        '''
        obj = self.obj
        args = self.args
        kwargs = self.kwargs
    # WARNING: Decompyle incomplete

    
    def agg_list_like(self = None):
        '''
        Compute aggregation in the case of a list-like argument.

        Returns
        -------
        Result of aggregation.
        '''
        return self.agg_or_apply_list_like(op_name = 'agg')

    
    def compute_list_like(self = None, op_name = None, selected_obj = None, kwargs = ('op_name', "Literal['agg', 'apply']", 'selected_obj', 'Series | DataFrame', 'kwargs', 'dict[str, Any]', 'return', 'tuple[list[Hashable] | Index, list[Any]]')):
        '''
        Compute agg/apply results for like-like input.

        Parameters
        ----------
        op_name : {"agg", "apply"}
            Operation being performed.
        selected_obj : Series or DataFrame
            Data to perform operation on.
        kwargs : dict
            Keyword arguments to pass to the functions.

        Returns
        -------
        keys : list[Hashable] or Index
            Index labels for result.
        results : list
            Data for result. When aggregating with a Series, this can contain any
            Python objects.
        '''
        func = cast(list[AggFuncTypeBase], self.func)
        obj = self.obj
        results = []
        keys = []
    # WARNING: Decompyle incomplete

    
    def wrap_results_list_like(self = None, keys = None, results = None):
        concat = concat
        import pandas.core.reshape.concat
        obj = self.obj
        
        try:
            return concat(results, keys = keys, axis = 1, sort = False)
        except TypeError:
            err = None
            Series = Series
            import pandas
            result = Series(results, index = keys, name = obj.name)
            if is_nested_object(result):
                raise ValueError('cannot combine transform and aggregation operations'), err
            del err
            return None
            None = 
            del err


    
    def agg_dict_like(self = None):
        '''
        Compute aggregation in the case of a dict-like argument.

        Returns
        -------
        Result of aggregation.
        '''
        return self.agg_or_apply_dict_like(op_name = 'agg')

    
    def compute_dict_like(self, op_name = None, selected_obj = None, selection = None, kwargs = ('op_name', "Literal['agg', 'apply']", 'selected_obj', 'Series | DataFrame', 'selection', 'Hashable | Sequence[Hashable]', 'kwargs', 'dict[str, Any]', 'return', 'tuple[list[Hashable], list[Any]]')):
        '''
        Compute agg/apply results for dict-like input.

        Parameters
        ----------
        op_name : {"agg", "apply"}
            Operation being performed.
        selected_obj : Series or DataFrame
            Data to perform operation on.
        selection : hashable or sequence of hashables
            Used by GroupBy, Window, and Resample if selection is applied to the object.
        kwargs : dict
            Keyword arguments to pass to the functions.

        Returns
        -------
        keys : list[hashable]
            Index labels for result.
        results : list
            Data for result. When aggregating with a Series, this can contain any
            Python object.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def wrap_results_dict_like(self = None, selected_obj = None, result_index = None, result_data = ('selected_obj', 'Series | DataFrame', 'result_index', 'list[Hashable]', 'result_data', 'list')):
        Index = Index
        import pandas
        concat = concat
        import pandas.core.reshape.concat
        obj = self.obj
        is_ndframe = result_data()
        if all(is_ndframe):
            results = result_data()
            keys_to_use = zip(result_index, result_data, strict = True)()
            if keys_to_use == []:
                keys_to_use = result_index
                results = result_data
            if selected_obj.ndim == 2:
                ktu = Index(keys_to_use)
                ktu._set_names(selected_obj.columns.names)
                keys_to_use = ktu
            axis = 0 if isinstance(obj, ABCSeries) else 1
            result = concat(results, axis = axis, keys = keys_to_use, sort = False)
        elif any(is_ndframe):
            raise ValueError('cannot perform both aggregation and transformation operations simultaneously')
        Series = Series
        import pandas
        result = Series(result_data, index = result_index, name = name)
        return result

    
    def apply_str(self = None):
