# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: readers.pyc (Python 3.11)

'''
Module contains tools for processing files into DataFrames or other objects

GH#48849 provides a convenient way of deprecating keyword arguments
'''
from __future__ import annotations
from collections import abc, defaultdict
import csv
import sys
from typing import IO, TYPE_CHECKING, Any, Generic, Literal, Self, TypedDict, Unpack, cast, overload
import warnings
import numpy as np
from pandas._libs import lib
from pandas._libs.parsers import STR_NA_VALUES
from pandas.errors import AbstractMethodError, ParserWarning
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.common import is_file_like, is_float, is_integer, is_list_like, pandas_dtype
from pandas import Series
from pandas.core.frame import DataFrame
from pandas.core.indexes.api import RangeIndex
from pandas.io.common import IOHandles, get_handle, stringify_path, validate_header_arg
from pandas.io.parsers.arrow_parser_wrapper import ArrowParserWrapper
from pandas.io.parsers.base_parser import ParserBase, is_index_col, parser_defaults
from pandas.io.parsers.c_parser_wrapper import CParserWrapper
from pandas.io.parsers.python_parser import FixedWidthFieldParser, PythonParser
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
    from types import TracebackType
    from pandas._typing import CompressionOptions, CSVEngine, DtypeArg, DtypeBackend, FilePath, HashableT, IndexLabel, ReadCsvBuffer, StorageOptions, UsecolsArgType
    
    def _read_shared():
        '''_read_shared'''
        dtype_backend: 'DtypeBackend | lib.NoDefault' = '_read_shared'

    _read_shared = <NODE:27>(_read_shared, '_read_shared', TypedDict, Generic[HashableT], total = False)
else:
    _read_shared = dict

class _C_Parser_Defaults(TypedDict):
    float_precision: 'None' = '_C_Parser_Defaults'

_c_parser_defaults: '_C_Parser_Defaults' = {
    'na_filter': True,
    'low_memory': True,
    'memory_map': False,
    'float_precision': None }

class _Fwf_Defaults(TypedDict):
    widths: 'None' = '_Fwf_Defaults'

_fwf_defaults: '_Fwf_Defaults' = {
    'colspecs': 'infer',
    'infer_nrows': 100,
    'widths': None }
_c_unsupported = {
    'skipfooter'}
_python_unsupported = {
    'low_memory',
    'float_precision'}
_pyarrow_unsupported = {
    'nrows',
    'comment',
    'dialect',
    'quoting',
    'dayfirst',
    'iterator',
    'chunksize',
    'thousands',
    'converters',
    'low_memory',
    'memory_map',
    'skipfooter',
    'lineterminator',
    'float_precision',
    'skipinitialspace'}
validate_integer = (lambda name = None, val = None, min_val = overload: pass)()
validate_integer = (lambda name = None, val = None, min_val = overload: pass)()
validate_integer = (lambda name = None, val = None, min_val = overload: pass)()

def validate_integer(name = None, val = None, min_val = None):
    """
    Checks whether the 'name' parameter for parsing is either
    an integer OR float that can SAFELY be cast to an integer
    without losing accuracy. Raises a ValueError if that is
    not the case.

    Parameters
    ----------
    name : str
        Parameter name (used for error reporting)
    val : int or float
        The value to check
    min_val : int
        Minimum allowed value (val < min_val will result in a ValueError)
    """
    pass
# WARNING: Decompyle incomplete


def _validate_names(names = None):
    '''
    Raise ValueError if the `names` parameter contains duplicates or has an
    invalid data type.

    Parameters
    ----------
    names : array-like or None
        An array containing a list of the names used for the output DataFrame.

    Raises
    ------
    ValueError
        If names are not unique or are not ordered (e.g. set).
    '''
    pass
# WARNING: Decompyle incomplete


def _read(filepath_or_buffer = None, kwds = None):
    '''Generic reader of line files.'''
    pass
# WARNING: Decompyle incomplete

read_csv = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_csv = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_csv = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_csv = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_csv = (lambda filepath_or_buffer = None, *, sep: kwds = locals().copy()del kwds['filepath_or_buffer']del kwds['sep']kwds_defaults = _refine_defaults_read(dialect, delimiter, engine, sep, on_bad_lines, names, defaults = {
'delimiter': ',' }, dtype_backend = dtype_backend)kwds.update(kwds_defaults)_read(filepath_or_buffer, kwds))()
read_table = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_table = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_table = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_table = (lambda filepath_or_buffer = None, *, iterator: pass)()
read_table = (lambda filepath_or_buffer = None, *, sep: kwds = locals().copy()del kwds['filepath_or_buffer']del kwds['sep']kwds_defaults = _refine_defaults_read(dialect, delimiter, engine, sep, on_bad_lines, names, defaults = {
'delimiter': '\t' }, dtype_backend = dtype_backend)kwds.update(kwds_defaults)_read(filepath_or_buffer, kwds))()
read_fwf = (lambda filepath_or_buffer = None, *, colspecs: pass)()
read_fwf = (lambda filepath_or_buffer = None, *, colspecs: pass)()
read_fwf = (lambda filepath_or_buffer = None, *, colspecs: pass)()
read_fwf = (lambda filepath_or_buffer = None, *, colspecs: pass# WARNING: Decompyle incomplete
)()

class TextFileReader(abc.Iterator):
    '''

    Passed dialect overrides any of the related parser options

    '''
    
    def __init__(self = None, f = None, engine = None, **kwds):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_options_with_defaults(self = None, engine = None):
        kwds = self.orig_options
        options = { }
        for argname, default in parser_defaults.items():
            value = kwds.get(argname, default)
            if engine == 'pyarrow' and argname in _pyarrow_unsupported and value != default and value != getattr(value, 'value', default):
                raise ValueError(f'''The {argname!r} option is not supported with the \'pyarrow\' engine''')
            options[argname] = value
            for argname, default in _c_parser_defaults.items():
                if argname in kwds:
                    value = kwds[argname]
                    if engine != 'c' and value != default:
                        if 'python' in engine and argname not in _python_unsupported:
                            pass
                        elif 'pyarrow' in engine and argname not in _pyarrow_unsupported:
                            pass
                        else:
                            raise ValueError(f'''The {argname!r} option is not supported with the {engine!r} engine''')
                    else:
                        value = default
                options[argname] = value
                if engine == 'python-fwf':
                    for argname, default in _fwf_defaults.items():
                        options[argname] = kwds.get(argname, default)
                        return options

    
    def _check_file_or_buffer(self = None, f = None, engine = None):
        if not is_file_like(f) and engine != 'c' and hasattr(f, '__iter__'):
            raise ValueError("The 'python' engine cannot iterate through this file buffer.")
        if hasattr(f, 'encoding'):
            file_encoding = f.encoding
            orig_reader_enc = self.orig_options.get('encoding', None)
            if not file_encoding is None:
                any_none = orig_reader_enc is None
                if not file_encoding != orig_reader_enc or any_none:
                    file_path = getattr(f, 'name', None)
                    raise ValueError(f'''The specified reader encoding {orig_reader_enc} is different from the encoding {file_encoding} of file {file_path}.''')
                return None
            return file_encoding is None

    
    def _clean_options(self = None, options = None, engine = None):
        result = options.copy()
        fallback_reason = None
        if engine == 'c' and options['skipfooter'] > 0:
            fallback_reason = "the 'c' engine does not support skipfooter"
            engine = 'python'
        sep = options['delimiter']
    # WARNING: Decompyle incomplete

    
    def __next__(self = None):
        
        try:
            return self.get_chunk()
        except StopIteration:
            self.close()
            raise 


    
    def _make_engine(self = None, f = None, engine = None):
        mapping = {
            'c': CParserWrapper,
            'python': PythonParser,
            'pyarrow': ArrowParserWrapper,
            'python-fwf': FixedWidthFieldParser }
        if engine not in mapping:
            raise ValueError(f'''Unknown engine: {engine} (valid options are {mapping.keys()})''')
    # WARNING: Decompyle incomplete

    
    def _failover_to_python(self = None):
        raise AbstractMethodError(self)

    
    def read(self = None, nrows = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_chunk(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self.close()



def TextParser(*args, **kwds):
    """
    Converts lists of lists/tuples into DataFrames with proper type inference
    and optional (e.g. string to datetime) conversion. Also enables iterating
    lazily over chunks of large files

    Parameters
    ----------
    data : file-like object or list
    delimiter : separator character to use
    dialect : str or csv.Dialect instance, optional
        Ignored if delimiter is longer than 1 character
    names : sequence, default
    header : int, default 0
        Row to use to parse column labels. Defaults to the first row. Prior
        rows will be discarded
    index_col : int or list, optional
        Column or columns to use as the (possibly hierarchical) index
    has_index_names: bool, default False
        True if the cols defined in index_col have an index name and are
        not in the header.
    na_values : scalar, str, list-like, or dict, optional
        Additional strings to recognize as NA/NaN.
    keep_default_na : bool, default True
    thousands : str, optional
        Thousands separator
    comment : str, optional
        Comment out remainder of line
    parse_dates : bool, default False
    date_format : str or dict of column -> format, default ``None``

        .. versionadded:: 2.0.0
    skiprows : list of integers
        Row numbers to skip
    skipfooter : int
        Number of line at bottom of file to skip
    converters : dict, optional
        Dict of functions for converting values in certain columns. Keys can
        either be integers or column labels, values are functions that take one
        input argument, the cell (not column) content, and return the
        transformed content.
    encoding : str, optional
        Encoding to use for UTF when reading/writing (ex. 'utf-8')
    float_precision : str, optional
        Specifies which converter the C engine should use for floating-point
        values. The options are `None` or `high` for the ordinary converter,
        `legacy` for the original lower precision pandas converter, and
        `round_trip` for the round-trip converter.
    """
    kwds['engine'] = 'python'
# WARNING: Decompyle incomplete


def _clean_na_values(na_values = None, keep_default_na = None, floatify = None):
    pass
# WARNING: Decompyle incomplete


def _floatify_na_values(na_values = None):
    result = set()
    for v in na_values:
        v = float(v)
        if not np.isnan(v):
            result.add(v)
        except (TypeError, ValueError, OverflowError):
            continue
        return result


def _stringify_na_values(na_values = None, floatify = None):
    '''return a stringified and numeric for these values'''
    result = []
    for x in na_values:
        result.append(str(x))
        result.append(x)
        v = float(x)
        if v == int(v):
            v = int(v)
            result.append(f'''{v}.0''')
            result.append(str(v))
        return set(result)


def _refine_defaults_read(dialect, delimiter, engine, sep, on_bad_lines = None, names = None, defaults = None, dtype_backend = ('dialect', 'str | csv.Dialect | None', 'delimiter', 'str | None | lib.NoDefault', 'engine', 'CSVEngine | None', 'sep', 'str | None | lib.NoDefault', 'on_bad_lines', 'str | Callable', 'names', 'Sequence[Hashable] | None | lib.NoDefault', 'defaults', 'dict[str, Any]', 'dtype_backend', 'DtypeBackend | lib.NoDefault')):
    """Validate/refine default values of input parameters of read_csv, read_table.

    Parameters
    ----------
    dialect : str or csv.Dialect
        If provided, this parameter will override values (default or not) for the
        following parameters: `delimiter`, `doublequote`, `escapechar`,
        `skipinitialspace`, `quotechar`, and `quoting`. If it is necessary to
        override values, a ParserWarning will be issued. See csv.Dialect
        documentation for more details.
    delimiter : str or object
        Alias for sep.
    engine : {{'c', 'python'}}
        Parser engine to use. The C engine is faster while the python engine is
        currently more feature-complete.
    sep : str or object
        A delimiter provided by the user (str) or a sentinel value, i.e.
        pandas._libs.lib.no_default.
    on_bad_lines : str, callable
        An option for handling bad lines or a sentinel value(None).
    names : array-like, optional
        List of column names to use. If the file contains a header row,
        then you should explicitly pass ``header=0`` to override the column names.
        Duplicates in this list are not allowed.
    defaults: dict
        Default values of input parameters.

    Returns
    -------
    kwds : dict
        Input parameters with correct values.
    """
    delim_default = defaults['delimiter']
    kwds = { }
# WARNING: Decompyle incomplete


def _extract_dialect(kwds = None):
    '''
    Extract concrete csv dialect instance.

    Returns
    -------
    csv.Dialect or None
    '''
    pass
# WARNING: Decompyle incomplete

MANDATORY_DIALECT_ATTRS = ('delimiter', 'doublequote', 'escapechar', 'skipinitialspace', 'quotechar', 'quoting')

def _validate_dialect(dialect = None):
    '''
    Validate csv dialect instance.

    Raises
    ------
    ValueError
        If incorrect dialect is provided.
    '''
    for param in MANDATORY_DIALECT_ATTRS:
        if not hasattr(dialect, param):
            raise ValueError(f'''Invalid dialect {dialect} provided''')
        return None


def _merge_with_dialect_properties(dialect = None, defaults = None):
    '''
    Merge default kwargs in TextFileReader with dialect parameters.

    Parameters
    ----------
    dialect : csv.Dialect
        Concrete csv dialect. See csv.Dialect documentation for more details.
    defaults : dict
        Keyword arguments passed to TextFileReader.

    Returns
    -------
    kwds : dict
        Updated keyword arguments, merged with dialect parameters.
    '''
    kwds = defaults.copy()
    for param in MANDATORY_DIALECT_ATTRS:
        dialect_val = getattr(dialect, param)
        parser_default = parser_defaults[param]
        provided = kwds.get(param, parser_default)
        conflict_msgs = []
        if provided not in (parser_default, dialect_val):
            msg = f'''Conflicting values for \'{param}\': \'{provided}\' was provided, but the dialect specifies \'{dialect_val}\'. Using the dialect-specified value.'''
            if not param == 'delimiter' or kwds.pop('sep_override', False):
                conflict_msgs.append(msg)
        if conflict_msgs:
            warnings.warn('\n\n'.join(conflict_msgs), ParserWarning, stacklevel = find_stack_level())
        kwds[param] = dialect_val
        return kwds


def _validate_skipfooter(kwds = None):
    '''
    Check whether skipfooter is compatible with other kwargs in TextFileReader.

    Parameters
    ----------
    kwds : dict
        Keyword arguments passed to TextFileReader.

    Raises
    ------
    ValueError
        If skipfooter is not compatible with other parameters.
    '''
    if kwds.get('skipfooter'):
        if kwds.get('iterator') or kwds.get('chunksize'):
            raise ValueError("'skipfooter' not supported for iteration")
        if kwds.get('nrows'):
            raise ValueError("'skipfooter' not supported with 'nrows'")
    return None
