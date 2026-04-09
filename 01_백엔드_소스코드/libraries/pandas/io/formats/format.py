# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: format.pyc (Python 3.11)

'''
Internal module for formatting output data in csv, html, xml,
and latex files. This module also applies to display formatting.
'''
from __future__ import annotations
from collections.abc import Callable, Generator, Hashable, Mapping, Sequence
from contextlib import contextmanager
from csv import QUOTE_NONE
from decimal import Decimal
from functools import partial
from io import StringIO
import math
import re
from shutil import get_terminal_size
from typing import TYPE_CHECKING, Any, Final, cast
import numpy as np
from pandas._config.config import get_option, set_option
from pandas._libs import lib
from pandas._libs.missing import NA
from pandas._libs.tslibs import NaT, Timedelta, Timestamp
from pandas._libs.tslibs.nattype import NaTType
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_complex_dtype, is_float, is_integer, is_list_like, is_numeric_dtype, is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype
from pandas.core.dtypes.missing import isna, notna
from pandas.core.arrays import Categorical, DatetimeArray, ExtensionArray, TimedeltaArray
from pandas.core.base import PandasObject

common
from pandas.core.indexes.api import Index, MultiIndex, PeriodIndex, ensure_index
MultiIndex = MultiIndex
PeriodIndex = PeriodIndex
ensure_index = ensure_index
import pandas.core.common, core
from pandas.core.indexes.datetimes import DatetimeIndex
from pandas.core.indexes.timedeltas import TimedeltaIndex
from pandas.io.common import check_parent_directory, stringify_path
from pandas.io.formats import printing
if TYPE_CHECKING:
    from pandas._typing import ArrayLike, Axes, ColspaceArgType, ColspaceType, CompressionOptions, FilePath, FloatFormatType, FormattersType, IndexLabel, SequenceNotStr, StorageOptions, WriteBuffer
    from pandas import DataFrame, Series
common_docstring: 'Final' = "\n        Parameters\n        ----------\n        buf : str, Path or StringIO-like, optional, default None\n            Buffer to write to. If None, the output is returned as a string.\n        columns : array-like, optional, default None\n            The subset of columns to write. Writes all columns by default.\n        col_space : %(col_space_type)s, optional\n            %(col_space)s\n        header : %(header_type)s, optional\n            %(header)s.\n        index : bool, optional, default True\n            Whether to print index (row) labels.\n        na_rep : str, optional, default 'NaN'\n            String representation of ``NaN`` to use.\n        formatters : list, tuple or dict of one-param. functions, optional\n            Formatter functions to apply to columns' elements by position or\n            name.\n            The result of each function must be a unicode string.\n            List/tuple must be of length equal to the number of columns.\n        float_format : one-parameter function, optional, default None\n            Formatter function to apply to columns' elements if they are\n            floats. This function must return a unicode string and will be\n            applied only to the non-``NaN`` elements, with ``NaN`` being\n            handled by ``na_rep``.\n        sparsify : bool, optional, default True\n            Set to False for a DataFrame with a hierarchical index to print\n            every multiindex key at each row.\n        index_names : bool, optional, default True\n            Prints the names of the indexes.\n        justify : str, default None\n            How to justify the column labels. If None uses the option from\n            the print configuration (controlled by set_option), 'right' out\n            of the box. Valid values are\n\n            * left\n            * right\n            * center\n            * justify\n            * justify-all\n            * start\n            * end\n            * inherit\n            * match-parent\n            * initial\n            * unset.\n        max_rows : int, optional\n            Maximum number of rows to display in the console.\n        max_cols : int, optional\n            Maximum number of columns to display in the console.\n        show_dimensions : bool, default False\n            Display DataFrame dimensions (number of rows by number of columns).\n        decimal : str, default '.'\n            Character recognized as decimal separator, e.g. ',' in Europe.\n    "
VALID_JUSTIFY_PARAMETERS = ('left', 'right', 'center', 'justify', 'justify-all', 'start', 'end', 'inherit', 'match-parent', 'initial', 'unset')
return_docstring: 'Final' = '\n        Returns\n        -------\n        str or None\n            If buf is None, returns the result as a string. Otherwise returns\n            None.\n    '

class SeriesFormatter:
    '''
    Implement the main logic of Series.to_string, which underlies
    Series.__repr__.
    '''
    
    def __init__(self = None, series = None, *, length, header, index, na_rep, name, float_format, dtype, max_rows, min_rows):
        self.series = series
        self.buf = StringIO()
        self.name = name
        self.na_rep = na_rep
        self.header = header
        self.length = length
        self.index = index
        self.max_rows = max_rows
        self.min_rows = min_rows
    # WARNING: Decompyle incomplete

    
    def _chk_truncate(self = None):
        self
        min_rows = self.min_rows
        max_rows = self.max_rows
        if max_rows:
            pass
        is_truncated_vertically = len(self.series) > max_rows
        series = self.series
        if is_truncated_vertically:
            max_rows = cast(int, max_rows)
            if min_rows:
                max_rows = min(min_rows, max_rows)
            if max_rows == 1:
                row_num = max_rows
                series = series.iloc[:max_rows]
            else:
                row_num = max_rows // 2
                _len = len(series)
                _slice = np.hstack([
                    np.arange(row_num),
                    np.arange(_len - row_num, _len)])
                series = series.iloc[_slice]
            self.tr_row_num = row_num
        else:
            self.tr_row_num = None
        self.tr_series = series
        self.is_truncated_vertically = is_truncated_vertically

    
    def _get_footer(self = None):
        name = self.series.name
        footer = ''
        index = self.series.index
    # WARNING: Decompyle incomplete

    
    def _get_formatted_values(self = None):
        return format_array(self.tr_series._values, None, float_format = self.float_format, na_rep = self.na_rep, leading_space = self.index)

    
    def to_string(self = None):
        series = self.tr_series
        footer = self._get_footer()
        if len(series) == 0:
            return f'''{type(self.series).__name__}([], {footer})'''
        index = None.index
        have_header = _has_names(index)
    # WARNING: Decompyle incomplete



def get_dataframe_repr_params():
    '''Get the parameters used to repr(dataFrame) calls using DataFrame.to_string.

    Supplying these parameters to DataFrame.to_string is equivalent to calling
    ``repr(DataFrame)``. This is useful if you want to adjust the repr output.

    Example
    -------
    >>> import pandas as pd
    >>>
    >>> df = pd.DataFrame([[1, 2], [3, 4]])
    >>> repr_params = pd.io.formats.format.get_dataframe_repr_params()
    >>> repr(df) == df.to_string(**repr_params)
    True
    '''
    console = console
    import pandas.io.formats
    if get_option('display.expand_frame_repr'):
        (line_width, _) = console.get_console_size()
    else:
        line_width = None
    return {
        'max_rows': get_option('display.max_rows'),
        'min_rows': get_option('display.min_rows'),
        'max_cols': get_option('display.max_columns'),
        'max_colwidth': get_option('display.max_colwidth'),
        'show_dimensions': get_option('display.show_dimensions'),
        'line_width': line_width }


def get_series_repr_params():
    '''Get the parameters used to repr(Series) calls using Series.to_string.

    Supplying these parameters to Series.to_string is equivalent to calling
    ``repr(series)``. This is useful if you want to adjust the series repr output.

    Example
    -------
    >>> import pandas as pd
    >>>
    >>> ser = pd.Series([1, 2, 3, 4])
    >>> repr_params = pd.io.formats.format.get_series_repr_params()
    >>> repr(ser) == ser.to_string(**repr_params)
    True
    '''
    (width, height) = get_terminal_size()
    max_rows_opt = get_option('display.max_rows')
    max_rows = height if max_rows_opt == 0 else max_rows_opt
    min_rows = height if max_rows_opt == 0 else get_option('display.min_rows')
    return {
        'name': True,
        'dtype': True,
        'min_rows': min_rows,
        'max_rows': max_rows,
        'length': get_option('display.show_dimensions') }


class DataFrameFormatter:
    '''
    Class for processing dataframe formatting options and data.

    Used by DataFrame.to_string, which backs DataFrame.__repr__.
    '''
    __doc__ = __doc__ if __doc__ else ''
    __doc__ += common_docstring + return_docstring
    
    def __init__(self, frame, columns, col_space, header, index, na_rep, formatters, justify, float_format, sparsify, index_names, max_rows, min_rows, max_cols = None, show_dimensions = None, decimal = None, bold_rows = (None, None, True, True, 'NaN', None, None, None, None, True, None, None, None, False, '.', False, True), escape = ('frame', 'DataFrame', 'columns', 'Axes | None', 'col_space', 'ColspaceArgType | None', 'header', 'bool | SequenceNotStr[str]', 'index', 'bool', 'na_rep', 'str', 'formatters', 'FormattersType | None', 'justify', 'str | None', 'float_format', 'FloatFormatType | None', 'sparsify', 'bool | None', 'index_names', 'bool', 'max_rows', 'int | None', 'min_rows', 'int | None', 'max_cols', 'int | None', 'show_dimensions', 'bool | str', 'decimal', 'str', 'bold_rows', 'bool', 'escape', 'bool', 'return', 'None')):
        self.frame = frame
        self.columns = self._initialize_columns(columns)
        self.col_space = self._initialize_colspace(col_space)
        self.header = header
        self.index = index
        self.na_rep = na_rep
        self.formatters = self._initialize_formatters(formatters)
        self.justify = self._initialize_justify(justify)
        self.float_format = self._validate_float_format(float_format)
        self.sparsify = self._initialize_sparsify(sparsify)
        self.show_index_names = index_names
        self.decimal = decimal
        self.bold_rows = bold_rows
        self.escape = escape
        self.max_rows = max_rows
        self.min_rows = min_rows
        self.max_cols = max_cols
        self.show_dimensions = show_dimensions
        self.max_cols_fitted = self._calc_max_cols_fitted()
        self.max_rows_fitted = self._calc_max_rows_fitted()
        self.tr_frame = self.frame
        self.truncate()
        self.adj = printing.get_adjustment()

    
    def get_strcols(self = None):
        '''
        Render a DataFrame to a list of columns (as lists of strings).
        '''
        strcols = self._get_strcols_without_index()
        if self.index:
            str_index = self._get_formatted_index(self.tr_frame)
            strcols.insert(0, str_index)
        return strcols

    should_show_dimensions = (lambda self = None:
