# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _util.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Hashable, Iterable, MutableMapping, Sequence
from typing import TYPE_CHECKING, Any, Literal, TypeVar, overload
from pandas.compat._optional import import_optional_dependency
from pandas.core.dtypes.common import is_integer, is_list_like
if TYPE_CHECKING:
    from pandas.io.excel._base import ExcelWriter
    ExcelWriter_t = type[ExcelWriter]
    usecols_func = TypeVar('usecols_func', bound = Callable[([
        Hashable], object)])
_writers: 'MutableMapping[str, ExcelWriter_t]' = { }

def register_writer(klass = None):
    '''
    Add engine to the excel writer registry.io.excel.

    You must use this method to integrate with ``to_excel``.

    Parameters
    ----------
    klass : ExcelWriter
    '''
    if not callable(klass):
        raise ValueError('Can only register callables as engines')
    engine_name = klass._engine
    _writers[engine_name] = klass


def get_default_engine(ext = None, mode = None):
    """
    Return the default reader/writer for the given extension.

    Parameters
    ----------
    ext : str
        The excel file extension for which to get the default engine.
    mode : str {'reader', 'writer'}
        Whether to get the default engine for reading or writing.
        Either 'reader' or 'writer'

    Returns
    -------
    str
        The default engine for the extension.
    """
    _default_readers = {
        'xlsx': 'openpyxl',
        'xlsm': 'openpyxl',
        'xlsb': 'pyxlsb',
        'xls': 'xlrd',
        'ods': 'odf' }
    _default_writers = {
        'xlsx': 'openpyxl',
        'xlsm': 'openpyxl',
        'xlsb': 'pyxlsb',
        'ods': 'odf' }
# WARNING: Decompyle incomplete


def get_writer(engine_name = None):
    
    try:
        return _writers[engine_name]
    except KeyError:
        err = None
        raise ValueError(f'''No Excel writer \'{engine_name}\''''), err
        err = None
        del err



def _excel2num(x = None):
    """
    Convert Excel column name like 'AB' to 0-based column index.

    Parameters
    ----------
    x : str
        The Excel column name to convert to a 0-based column index.

    Returns
    -------
    num : int
        The column index corresponding to the name.

    Raises
    ------
    ValueError
        Part of the Excel column name was invalid.
    """
    index = 0
    for c in x.upper().strip():
        cp = ord(c)
        if cp < ord('A') or cp > ord('Z'):
            raise ValueError(f'''Invalid column name: {x}''')
        index = (index * 26 + cp - ord('A')) + 1
        return index - 1


def _range2cols(areas = None):
    '''
    Convert comma separated list of column names and ranges to indices.

    Parameters
    ----------
    areas : str
        A string containing a sequence of column ranges (or areas).

    Returns
    -------
    cols : list
        A list of 0-based column indices.

    Examples
    --------
    >>> _range2cols("A:E")
    [0, 1, 2, 3, 4]
    >>> _range2cols("A,C,Z:AB")
    [0, 2, 25, 26, 27]
    '''
    cols = []
    for rng in areas.split(','):
        if ':' in rng:
            rngs = rng.split(':')
            cols.extend(range(_excel2num(rngs[0]), _excel2num(rngs[1]) + 1))
            continue
        cols.append(_excel2num(rng))
        return cols

maybe_convert_usecols = (lambda usecols = None: pass)()
maybe_convert_usecols = (lambda usecols = None: pass)()
maybe_convert_usecols = (lambda usecols = None: pass)()
maybe_convert_usecols = (lambda usecols = None: pass)()

def maybe_convert_usecols(usecols = None):
    '''
    Convert `usecols` into a compatible format for parsing in `parsers.py`.

    Parameters
    ----------
    usecols : object
        The use-columns object to potentially convert.

    Returns
    -------
    converted : object
        The compatible format of `usecols`.
    '''
    pass
# WARNING: Decompyle incomplete

validate_freeze_panes = (lambda freeze_panes = None: pass)()
validate_freeze_panes = (lambda freeze_panes = None: pass)()

def validate_freeze_panes(freeze_panes = None):
    pass
# WARNING: Decompyle incomplete


def fill_mi_header(row = None, control_row = None):
    '''
    Forward fill blank entries in row but only inside the same parent index.

    Used for creating headers in Multiindex.

    Parameters
    ----------
    row : list
        List of items in a single row.
    control_row : list of bool
        Helps to determine if particular column is in same parent index as the
        previous value. Used to stop propagation of empty cells between
        different indexes.

    Returns
    -------
    Returns changed row and control_row
    '''
    last = row[0]
# WARNING: Decompyle incomplete


def pop_header_name(row = None, index_col = None):
    '''
    Pop the header name for MultiIndex parsing.

    Parameters
    ----------
    row : list
        The data row to parse for the header name.
    index_col : int, list
        The index columns for our data. Assumed to be non-null.

    Returns
    -------
    header_name : str
        The extracted header name.
    trimmed_row : list
        The original data row with the header name removed.
    '''
    pass
# WARNING: Decompyle incomplete


def combine_kwargs(engine_kwargs = None, kwargs = None):
    '''
    Used to combine two sources of kwargs for the backend engine.

    Use of kwargs is deprecated, this function is solely for use in 1.3 and should
    be removed in 1.4/2.0. Also _base.ExcelWriter.__new__ ensures either engine_kwargs
    or kwargs must be None or empty respectively.

    Parameters
    ----------
    engine_kwargs: dict
        kwargs to be passed through to the engine.
    kwargs: dict
        kwargs to be psased through to the engine (deprecated)

    Returns
    -------
    engine_kwargs combined with kwargs
    '''
    pass
# WARNING: Decompyle incomplete
