# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pivot.pyc (Python 3.11)

from __future__ import annotations
import itertools
from typing import TYPE_CHECKING, Literal, cast
import numpy as np
from pandas._libs import lib
from pandas.util._decorators import set_module
from pandas.core.dtypes.cast import maybe_downcast_to_dtype
from pandas.core.dtypes.common import is_list_like, is_nested_list_like, is_scalar
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries

common
from pandas.core.groupby import Grouper
import pandas.core.common, core
from pandas.core.indexes.api import Index, MultiIndex, get_objs_combined_axis
from pandas.core.reshape.concat import concat
from pandas.core.series import Series
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable
    from pandas._typing import AggFuncType, AggFuncTypeBase, AggFuncTypeDict, IndexLabel, SequenceNotStr
    from pandas import DataFrame
pivot_table = (lambda data, values, index, columns, aggfunc, fill_value, margins = None, dropna = None, margins_name = set_module('pandas'), observed = (None, None, None, 'mean', None, False, True, 'All', True, True), sort = ('data', 'DataFrame', 'aggfunc', 'AggFuncType', 'margins', 'bool', 'dropna', 'bool', 'margins_name', 'Hashable', 'observed', 'bool', 'sort', 'bool', 'return', 'DataFrame'): index = _convert_by(index)columns = _convert_by(columns)if isinstance(aggfunc, list):
pieces = []keys = []for func in aggfunc:
_table = __internal_pivot_table(data, values = values, index = index, columns = columns, fill_value = fill_value, aggfunc = func, margins = margins, dropna = dropna, margins_name = margins_name, observed = observed, sort = sort, kwargs = kwargs)pieces.append(_table)keys.append(getattr(func, '__name__', func))table = concat(pieces, keys = keys, axis = 1)table.__finalize__(data, method = 'pivot_table')table = __internal_pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name, observed, sort, kwargs)table.__finalize__(data, method = 'pivot_table'))()

def __internal_pivot_table(data, values, index, columns, aggfunc, fill_value, margins, dropna, margins_name = None, observed = None, sort = None, kwargs = ('data', 'DataFrame', 'aggfunc', 'AggFuncTypeBase | AggFuncTypeDict', 'margins', 'bool', 'dropna', 'bool', 'margins_name', 'Hashable', 'observed', 'bool', 'sort', 'bool', 'return', 'DataFrame')):
    '''
    Helper of :func:`pandas.pivot_table` for any non-list ``aggfunc``.
    '''
    keys = index + columns
    values_passed = values is not None
    if values_passed:
        if is_list_like(values):
            values_multi = True
            values = list(values)
        else:
            values_multi = False
            values = [
                values]
        for i in values:
            if i not in data:
                raise KeyError(i)
            to_filter = []
            for x in keys + values:
                if isinstance(x, Grouper):
                    x = x.key
                if x in data:
                    to_filter.append(x)
                except TypeError:
                    continue
                if len(to_filter) < len(data.columns):
                    data = data[to_filter]
                else:
                    values = data.columns
                    for key in keys:
                        values = values.drop(key)
                        except (TypeError, ValueError, KeyError):
                            continue
                        values = list(values)
                        grouped = data.groupby(keys, observed = observed, sort = sort, dropna = dropna)
                        if values_passed:
                            grouped = grouped[values]
# WARNING: Decompyle incomplete


def _add_margins(table, data, values, rows, cols, aggfunc, kwargs = None, observed = None, margins_name = None, fill_value = ('All', None, True), dropna = ('table', 'DataFrame | Series', 'data', 'DataFrame', 'observed', 'bool', 'margins_name', 'Hashable', 'dropna', 'bool')):
    if not isinstance(margins_name, str):
        raise ValueError('margins_name argument must be a string')
    msg = f'''Conflicting name "{margins_name}" in margins'''
    for level in table.index.names:
        if margins_name in table.index.get_level_values(level):
            raise ValueError(msg)
        grand_margin = _compute_grand_margin(data, values, aggfunc, kwargs, margins_name)
        if table.ndim == 2:
            for level in table.columns.names[1:]:
                if margins_name in table.columns.get_level_values(level):
                    raise ValueError(msg)
                if len(rows) > 1:
                    key = (margins_name,) + ('',) * (len(rows) - 1)
                else:
                    key = margins_name
    if values and isinstance(table, ABCSeries):
        return table._append_internal(table._constructor({
            key: grand_margin[margins_name] }))
    if None:
        marginal_result_set = _generate_marginal_results(table, data, values, rows, cols, aggfunc, kwargs, observed, margins_name, dropna)
        if not isinstance(marginal_result_set, tuple):
            return marginal_result_set
        (result, margin_keys, row_margin) = None
# WARNING: Decompyle incomplete


def _compute_grand_margin(data = None, values = None, aggfunc = None, kwargs = ('All',), margins_name = ('data', 'DataFrame', 'margins_name', 'Hashable')):
    pass
# WARNING: Decompyle incomplete


def _generate_marginal_results(table, data, values, rows, cols, aggfunc = None, kwargs = None, observed = None, margins_name = ('All', True), dropna = ('data', 'DataFrame', 'observed', 'bool', 'margins_name', 'Hashable', 'dropna', 'bool')):
    pass
# WARNING: Decompyle incomplete


def _generate_marginal_results_without_values(table, data, rows, cols, aggfunc = None, kwargs = None, observed = None, margins_name = ('All', True), dropna = ('table', 'DataFrame', 'data', 'DataFrame', 'observed', 'bool', 'margins_name', 'Hashable', 'dropna', 'bool')):
    pass
# WARNING: Decompyle incomplete


def _convert_by(by):
    pass
# WARNING: Decompyle incomplete

pivot = (lambda data = None, *, columns: pass# WARNING: Decompyle incomplete
)()
crosstab = (lambda index, columns, values, rownames, colnames, aggfunc = None, margins = None, margins_name = set_module('pandas'), dropna = (None, None, None, None, False, 'All', True, False), normalize = ('margins', 'bool', 'margins_name', 'Hashable', 'dropna', 'bool', 'normalize', "bool | Literal[0, 1, 'all', 'index', 'columns']", 'return', 'DataFrame'): pass# WARNING: Decompyle incomplete
)()

def _normalize(table = None, normalize = None, margins = None, margins_name = ('All',)):
    if not isinstance(normalize, (bool, str)):
        axis_subs = {
            0: 'index',
            1: 'columns' }
        
        try:
            normalize = axis_subs[normalize]
        except KeyError:
            err = None
            raise ValueError('Not a valid normalize argument'), err
            err = None
            del err

        if margins is False:
            normalizers = {
                'all': (lambda x: x / x.sum(axis = 1).sum(axis = 0)),
                'columns': (lambda x: x / x.sum()),
                'index': (lambda x: x.div(x.sum(axis = 1), axis = 0)) }
            normalizers[True] = normalizers['all']
            
            try:
                f = normalizers[normalize]
            except KeyError:
                err = None
                raise ValueError('Not a valid normalize argument'), err
                err = None
                del err

            table = f(table)
            table = table.fillna(0)
        elif margins is True:
            table_index = table.index
            table_columns = table.columns
            last_ind_or_col = table.iloc[(-1, :)].name
            if (margins_name not in last_ind_or_col) & (margins_name != last_ind_or_col):
                raise ValueError(f'''{margins_name} not in pivoted DataFrame''')
            column_margin = table.iloc[(:-1, -1)]
            index_margin = table.iloc[(-1, :-1)]
            table = table.iloc[(:-1, :-1)]
            table = _normalize(table, normalize = normalize, margins = False)
            if normalize == 'columns':
                column_margin = column_margin / column_margin.sum()
                table = concat([
                    table,
                    column_margin], axis = 1)
                table = table.fillna(0)
                table.columns = table_columns
            elif normalize == 'index':
                index_margin = index_margin / index_margin.sum()
                table = table._append_internal(index_margin, ignore_index = True)
                table = table.fillna(0)
                table.index = table_index
            elif normalize == 'all' or normalize is True:
                column_margin = column_margin / column_margin.sum()
                index_margin = index_margin / index_margin.sum()
                index_margin.loc[margins_name] = 1
                table = concat([
                    table,
                    column_margin], axis = 1)
                table = table._append_internal(index_margin, ignore_index = True)
                table = table.fillna(0)
                table.index = table_index
                table.columns = table_columns
            else:
                raise ValueError('Not a valid normalize argument')
    raise ValueError('Not a valid margins argument')
    return table


def _get_names(arrs = None, names = None, prefix = None):
    pass
# WARNING: Decompyle incomplete


def _build_names_mapper(rownames = None, colnames = None):
    """
    Given the names of a DataFrame's rows and columns, returns a set of unique row
    and column names and mappers that convert to original names.

    A row or column name is replaced if it is duplicate among the rows of the inputs,
    among the columns of the inputs or between the rows and the columns.

    Parameters
    ----------
    rownames: list[str]
    colnames: list[str]

    Returns
    -------
    Tuple(Dict[str, str], List[str], Dict[str, str], List[str])

    rownames_mapper: dict[str, str]
        a dictionary with new row names as keys and original rownames as values
    unique_rownames: list[str]
        a list of rownames with duplicate names replaced by dummy names
    colnames_mapper: dict[str, str]
        a dictionary with new column names as keys and original column names as values
    unique_colnames: list[str]
        a list of column names with duplicate names replaced by dummy names

    """
    pass
# WARNING: Decompyle incomplete
