# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: describe.pyc (Python 3.11)

'''
Module responsible for execution of NDFrame.describe() method.

Method NDFrame.describe() delegates actual execution to function describe_ndframe().
'''
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, cast
import numpy as np
from pandas._typing import DtypeObj, NDFrameT, npt
from pandas.util._validators import validate_percentile
from pandas.core.dtypes.common import is_bool_dtype, is_numeric_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, DatetimeTZDtype, ExtensionDtype
from pandas.core.arrays.floating import Float64Dtype
from pandas.core.reshape.concat import concat
from pandas.io.formats.format import format_percentiles
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Sequence
    from pandas import DataFrame, Series

def describe_ndframe(*, obj, include, exclude, percentiles):
    """Describe series or dataframe.

    Called from pandas.core.generic.NDFrame.describe()

    Parameters
    ----------
    obj: DataFrame or Series
        Either dataframe or series to be described.
    include : 'all', list-like of dtypes or None (default), optional
        A white list of data types to include in the result. Ignored for ``Series``.
    exclude : list-like of dtypes or None (default), optional,
        A black list of data types to omit from the result. Ignored for ``Series``.
    percentiles : list-like of numbers, optional
        The percentiles to include in the output. All should fall between 0 and 1.
        The default is ``[.25, .5, .75]``, which returns the 25th, 50th, and
        75th percentiles.

    Returns
    -------
    Dataframe or series description.
    """
    percentiles = _refine_percentiles(percentiles)
    if obj.ndim == 1:
        describer = SeriesDescriber(obj = cast('Series', obj))
    else:
        describer = DataFrameDescriber(obj = cast('DataFrame', obj), include = include, exclude = exclude)
    result = describer.describe(percentiles = percentiles)
    return cast(NDFrameT, result)


class NDFrameDescriberAbstract(ABC):
    '''Abstract class for describing dataframe or series.

    Parameters
    ----------
    obj : Series or DataFrame
        Object to be described.
    '''
    
    def __init__(self = None, obj = None):
        self.obj = obj

    describe = (lambda self = None, percentiles = None: pass)()


class SeriesDescriber(NDFrameDescriberAbstract):
    obj: 'Series' = 'Class responsible for creating series description.'
    
    def describe(self = None, percentiles = None):
        describe_func = select_describe_func(self.obj)
        return describe_func(self.obj, percentiles)



class DataFrameDescriber(NDFrameDescriberAbstract):
    pass
# WARNING: Decompyle incomplete


def reorder_columns(ldesc = None):
    '''Set a convenient order for rows for display.'''
    names = []
    seen_names = set()
    ldesc_indexes = (lambda .0: pass# WARNING: Decompyle incomplete
)(ldesc(), key = len)
    for idxnames in ldesc_indexes:
        for name in idxnames:
            if name not in seen_names:
                seen_names.add(name)
                names.append(name)
            return names


def describe_numeric_1d(series = None, percentiles = None):
    '''Describe series containing numerical data.

    Parameters
    ----------
    series : Series
        Series to be described.
    percentiles : list-like of numbers
        The percentiles to include in the output.
    '''
    Series = Series
    import pandas
    formatted_percentiles = format_percentiles(percentiles)
    if len(percentiles) == 0:
        quantiles = []
    else:
        quantiles = series.quantile(percentiles).tolist()
    stat_index = None['max']
    d = None[series.max()]
    if isinstance(series.dtype, ExtensionDtype):
        if isinstance(series.dtype, ArrowDtype):
            if series.dtype.kind == 'm':
                dtype = None
            else:
                import pyarrow as pa
                dtype = ArrowDtype(pa.float64())
        else:
            dtype = Float64Dtype()
    elif series.dtype.kind in 'iufb':
        dtype = np.dtype('float')
    else:
        dtype = None
    return Series(d, index = stat_index, name = series.name, dtype = dtype)


def describe_categorical_1d(data = None, percentiles_ignored = None):
    '''Describe series containing categorical data.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles_ignored : list-like of numbers
        Ignored, but in place to unify interface.
    '''
    names = [
        'count',
        'unique',
        'top',
        'freq']
    objcounts = data.value_counts()
    count_unique = len(objcounts[objcounts != 0])
    if count_unique > 0:
        freq = objcounts.iloc[0]
        top = objcounts.index[0]
        dtype = None
    else:
        freq = np.nan
        top = np.nan
        dtype = 'object'
    result = [
        data.count(),
        count_unique,
        top,
        freq]
    Series = Series
    import pandas
    return Series(result, index = names, name = data.name, dtype = dtype)


def describe_timestamp_1d(data = None, percentiles = None):
    '''Describe series containing datetime64 dtype.

    Parameters
    ----------
    data : Series
        Series to be described.
    percentiles : list-like of numbers
        The percentiles to include in the output.
    '''
    Series = Series
    import pandas
    formatted_percentiles = format_percentiles(percentiles)
    stat_index = None['max']
    d = None[data.max()]
    return Series(d, index = stat_index, name = data.name)


def select_describe_func(data = None):
    '''Select proper function for describing series based on data type.

    Parameters
    ----------
    data : Series
        Series to be described.
    '''
    if is_bool_dtype(data.dtype):
        return describe_categorical_1d
    if None(data):
        return describe_numeric_1d
    if None.dtype.kind == 'M' or isinstance(data.dtype, DatetimeTZDtype):
        return describe_timestamp_1d
    if None.dtype.kind == 'm':
        return describe_numeric_1d


def _refine_percentiles(percentiles = None):
    '''
    Ensure that percentiles are unique and sorted.

    Parameters
    ----------
    percentiles : list-like of numbers, optional
        The percentiles to include in the output.
    '''
    pass
# WARNING: Decompyle incomplete
