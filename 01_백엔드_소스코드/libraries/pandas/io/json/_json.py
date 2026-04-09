# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _json.pyc (Python 3.11)

from __future__ import annotations
from abc import ABC, abstractmethod
from collections import abc
from itertools import islice
from typing import TYPE_CHECKING, Any, Generic, Literal, Self, TypeVar, final, overload
import warnings
import numpy as np
from pandas._config import option_context
from pandas._libs import lib
from pandas._libs.json import ujson_dumps, ujson_loads
from pandas._libs.tslibs import iNaT
from pandas.compat._optional import import_optional_dependency
from pandas.errors import AbstractMethodError, OutOfBoundsDatetime
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.common import ensure_str, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import PeriodDtype
from pandas import ArrowDtype, DataFrame, Index, MultiIndex, Series, isna, notna, to_datetime
from pandas.core.reshape.concat import concat
from pandas.io._util import arrow_table_to_pandas
from pandas.io.common import IOHandles, dedup_names, get_handle, is_potential_multi_index, stringify_path
from pandas.io.json._normalize import convert_to_line_delimits
from pandas.io.json._table_schema import build_table_schema, parse_table_schema, set_default_names
from pandas.io.parsers.readers import validate_integer
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Mapping
    from types import TracebackType
    from pandas._typing import CompressionOptions, DtypeArg, DtypeBackend, FilePath, IndexLabel, JSONEngine, JSONSerializable, ReadBuffer, StorageOptions, WriteBuffer
    from pandas.core.generic import NDFrame
FrameSeriesStrT = TypeVar('FrameSeriesStrT', bound = Literal[('frame', 'series')])
to_json = (lambda path_or_buf, obj, orient, date_format, double_precision, force_ascii, date_unit, default_handler, lines, compression = None, index = None, indent = overload, storage_options = (..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ...), mode = ('path_or_buf', 'FilePath | WriteBuffer[str] | WriteBuffer[bytes]', 'obj', 'NDFrame', 'orient', 'str | None', 'date_format', 'str', 'double_precision', 'int', 'force_ascii', 'bool', 'date_unit', 'str', 'default_handler', 'Callable[[Any], JSONSerializable] | None', 'lines', 'bool', 'compression', 'CompressionOptions', 'index', 'bool | None', 'indent', 'int', 'storage_options', 'StorageOptions', 'mode', "Literal['a', 'w']", 'return', 'None'): pass)()
to_json = (lambda path_or_buf, obj, orient, date_format, double_precision, force_ascii, date_unit, default_handler, lines, compression = None, index = None, indent = overload, storage_options = (..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ...), mode = ('path_or_buf', 'None', 'obj', 'NDFrame', 'orient', 'str | None', 'date_format', 'str', 'double_precision', 'int', 'force_ascii', 'bool', 'date_unit', 'str', 'default_handler', 'Callable[[Any], JSONSerializable] | None', 'lines', 'bool', 'compression', 'CompressionOptions', 'index', 'bool | None', 'indent', 'int', 'storage_options', 'StorageOptions', 'mode', "Literal['a', 'w']", 'return', 'str'): pass)()

def to_json(path_or_buf, obj, orient, date_format, double_precision, force_ascii, date_unit, default_handler, lines, compression = None, index = None, indent = None, storage_options = (None, 'epoch', 10, True, 'ms', None, False, 'infer', None, 0, None, 'w'), mode = ('path_or_buf', 'FilePath | WriteBuffer[str] | WriteBuffer[bytes] | None', 'obj', 'NDFrame', 'orient', 'str | None', 'date_format', 'str', 'double_precision', 'int', 'force_ascii', 'bool', 'date_unit', 'str', 'default_handler', 'Callable[[Any], JSONSerializable] | None', 'lines', 'bool', 'compression', 'CompressionOptions', 'index', 'bool | None', 'indent', 'int', 'storage_options', 'StorageOptions | None', 'mode', "Literal['a', 'w']", 'return', 'str | None')):
    if orient in ('records', 'values') and index is True:
        raise ValueError("'index=True' is only valid when 'orient' is 'split', 'table', 'index', or 'columns'.")
    if orient in ('index', 'columns') and index is False:
        raise ValueError("'index=False' is only valid when 'orient' is 'split', 'table', 'records', or 'values'.")
# WARNING: Decompyle incomplete


class Writer(ABC):
    _default_orient: 'str' = 'Writer'
    
    def __init__(self, obj, orient, date_format, double_precision, ensure_ascii = None, date_unit = None, index = None, default_handler = (None, 0), indent = ('obj', 'NDFrame', 'orient', 'str | None', 'date_format', 'str', 'double_precision', 'int', 'ensure_ascii', 'bool', 'date_unit', 'str', 'index', 'bool', 'default_handler', 'Callable[[Any], JSONSerializable] | None', 'indent', 'int', 'return', 'None')):
        self.obj = obj
    # WARNING: Decompyle incomplete

    
    def _format_axes(self = None):
        raise AbstractMethodError(self)

    
    def write(self = None):
        iso_dates = self.date_format == 'iso'
        return ujson_dumps(self.obj_to_write, orient = self.orient, double_precision = self.double_precision, ensure_ascii = self.ensure_ascii, date_unit = self.date_unit, iso_dates = iso_dates, default_handler = self.default_handler, indent = self.indent)

    obj_to_write = (lambda self = None: pass)()()


class SeriesWriter(Writer):
    _default_orient = 'index'
    obj_to_write = (lambda self = None: if self.index and self.orient == 'split':
{
'name': self.obj.name,
'data': self.obj.values }None.obj)()
    
    def _format_axes(self = None):
        if self.obj.index.is_unique or self.orient == 'index':
            raise ValueError(f'''Series index must be unique for orient=\'{self.orient}\'''')
        return None



class FrameWriter(Writer):
    _default_orient = 'columns'
    obj_to_write = (lambda self = None: if self.index and self.orient == 'split':
obj_to_write = self.obj.to_dict(orient = 'split')del obj_to_write['index']else:
obj_to_write = self.objobj_to_write)()
    
    def _format_axes(self = None):
        '''
        Try to format axes if they are datelike.
        '''
        if self.obj.index.is_unique and self.orient in ('index', 'columns'):
            raise ValueError(f'''DataFrame index must be unique for orient=\'{self.orient}\'.''')
        if self.obj.columns.is_unique or self.orient in ('index', 'columns', 'records'):
            raise ValueError(f'''DataFrame columns must be unique for orient=\'{self.orient}\'.''')
        return None



class JSONTableWriter(FrameWriter):
    pass
# WARNING: Decompyle incomplete

read_json = (lambda path_or_buf = None, *, orient: pass)()
read_json = (lambda path_or_buf = None, *, orient: pass)()
read_json = (lambda path_or_buf = None, *, orient: pass)()
read_json = (lambda path_or_buf = None, *, orient: pass)()
read_json = (lambda path_or_buf = None, *, orient: if orient == 'table' and dtype:
raise ValueError("cannot pass both dtype and orient='table'")if orient == 'table' and convert_axes:
raise ValueError("cannot pass both convert_axes and orient='table'")check_dtype_backend(dtype_backend)# WARNING: Decompyle incomplete
)()

def JsonReader():
    '''JsonReader'''
    __doc__ = '\n    JsonReader provides an interface for reading in a JSON file.\n\n    If initialized with ``lines=True`` and ``chunksize``, can be iterated over\n    ``chunksize`` lines at a time. Otherwise, calling ``read`` reads in the\n    whole document.\n    '
    
    def __init__(self, filepath_or_buffer, orient, typ, dtype, convert_axes, convert_dates, keep_default_dates, precise_float, date_unit, encoding, lines, chunksize, compression, nrows = None, storage_options = None, encoding_errors = None, dtype_backend = (None, 'strict', lib.no_default, 'ujson'), engine = ('typ', 'FrameSeriesStrT', 'convert_axes', 'bool | None', 'keep_default_dates', 'bool', 'precise_float', 'bool', 'lines', 'bool', 'chunksize', 'int | None', 'compression', 'CompressionOptions', 'nrows', 'int | None', 'storage_options', 'StorageOptions | None', 'encoding_errors', 'str | None', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'engine', 'JSONEngine', 'return', 'None')):
        self.orient = orient
        self.typ = typ
        self.dtype = dtype
        self.convert_axes = convert_axes
        self.convert_dates = convert_dates
        self.keep_default_dates = keep_default_dates
        self.precise_float = precise_float
        self.date_unit = date_unit
        self.encoding = encoding
        self.engine = engine
        self.compression = compression
        self.storage_options = storage_options
        self.lines = lines
        self.chunksize = chunksize
        self.nrows_seen = 0
        self.nrows = nrows
        self.encoding_errors = encoding_errors
        self.handles = None
        self.dtype_backend = dtype_backend
        if self.engine not in frozenset({'ujson', 'pyarrow'}):
            raise ValueError(f'''The engine type {self.engine} is currently not supported.''')
    # WARNING: Decompyle incomplete

    
    def _get_data_from_filepath(self, filepath_or_buffer):
        '''
        The function read_json accepts three input types:
            1. filepath (string-like)
            2. file-like object (e.g. open file object, StringIO)
        '''
        filepath_or_buffer = stringify_path(filepath_or_buffer)
        
        try:
            self.handles = get_handle(filepath_or_buffer, 'r', encoding = self.encoding, compression = self.compression, storage_options = self.storage_options, errors = self.encoding_errors)
        except OSError:
            err = None
            raise FileNotFoundError(f'''File {filepath_or_buffer} does not exist'''), err
            err = None
            del err

        filepath_or_buffer = self.handles.handle
        return filepath_or_buffer

    
    def _combine_lines(self = None, lines = None):
        '''
        Combines a list of JSON objects into one JSON object.
        '''
        return f'''{(lambda .0: pass# WARNING: Decompyle incomplete
)(lines()())}]'''

    read = (lambda self = None: pass)()
    read = (lambda self = None: pass)()
    read = (lambda self = None: pass)()
    
    def read(self = None):
        '''
        Read the whole JSON input into a pandas object.
        '''
        self
        if self.engine == 'pyarrow':
            obj = self._read_pyarrow()
        elif self.engine == 'ujson':
            obj = self._read_ujson()
        None(None, None)

    
    def _read_pyarrow(self = None):
        '''
        Read JSON using the pyarrow engine.
        '''
        pyarrow_json = import_optional_dependency('pyarrow.json')
        options = None
        if isinstance(self.dtype, dict):
            pa = import_optional_dependency('pyarrow')
            fields = []
            for field, dtype in self.dtype.items():
                pd_dtype = pandas_dtype(dtype)
                if isinstance(pd_dtype, ArrowDtype):
                    fields.append((field, pd_dtype.pyarrow_dtype))
                schema = pa.schema(fields)
                options = pyarrow_json.ParseOptions(explicit_schema = schema, unexpected_field_behavior = 'infer')
                pa_table = pyarrow_json.read_json(self.data, parse_options = options)
                df = arrow_table_to_pandas(pa_table, dtype_backend = self.dtype_backend)
                return df

    
    def _read_ujson(self = None):
        '''
        Read JSON using the ujson engine.
        '''
        if self.lines:
            if self.chunksize:
                obj = concat(self)
            elif self.nrows:
                lines = list(islice(self.data, self.nrows))
                lines_json = self._combine_lines(lines)
                obj = self._get_object_parser(lines_json)
            else:
                data = ensure_str(self.data)
                data_lines = data.split('\n')
                obj = self._get_object_parser(self._combine_lines(data_lines))
        else:
            obj = self._get_object_parser(self.data)
        if self.dtype_backend is not lib.no_default:
            option_context('future.distinguish_nan_and_na', False)
            None(None, None)
            return 
        with None:
            if not None:
                pass
        return None
        return obj

    
    def _get_object_parser(self = None, json = None):
        '''
        Parses a json document into a pandas object.
        '''
        typ = self.typ
        dtype = self.dtype
        kwargs = {
            'orient': self.orient,
            'dtype': self.dtype,
            'convert_axes': self.convert_axes,
            'convert_dates': self.convert_dates,
            'keep_default_dates': self.keep_default_dates,
            'precise_float': self.precise_float,
            'date_unit': self.date_unit,
            'dtype_backend': self.dtype_backend }
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        '''
        If we opened a stream earlier, in _get_data_from_filepath, we should
        close it.

        If an open stream or file was passed, we leave it open.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self = None):
        return self

    __next__ = (lambda self = None: pass)()
    __next__ = (lambda self = None: pass)()
    __next__ = (lambda self = None: pass)()
    
    def __next__(self = None):
        if self.nrows and self.nrows_seen >= self.nrows:
            self.close()
            raise StopIteration
        lines = list(islice(self.data, self.chunksize))
        if not lines:
            self.close()
            raise StopIteration
        
        try:
            lines_json = self._combine_lines(lines)
            obj = self._get_object_parser(lines_json)
            obj.index = range(self.nrows_seen, self.nrows_seen + len(obj))
        except Exception:
            None = None
            self.close()
            raise ex
            ex = None
            del ex

        if self.dtype_backend is not lib.no_default:
            option_context('future.distinguish_nan_and_na', False)
            None(None, None)
            return 
        with None:
            if not self, self.nrows_seen += len(obj), .nrows_seen:
                pass
        return None
        return obj

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self.close()


JsonReader = <NODE:27>(JsonReader, 'JsonReader', abc.Iterator, Generic[FrameSeriesStrT])()

class Parser:
    _default_orient: 'str' = 'Parser'
    _STAMP_UNITS = ('s', 'ms', 'us', 'ns')
    json: 'str' = {
        's': 31536000,
        'ms': 0x757B12C00,
        'us': 0x1CAE8C13E000,
        'ns': 0x7009D32DA30000 }
    
    def __init__(self, json, orient, dtype, convert_axes, convert_dates = None, keep_default_dates = None, precise_float = None, date_unit = (None, True, True, False, False, None, lib.no_default), dtype_backend = ('json', 'str', 'dtype', 'DtypeArg | None', 'convert_axes', 'bool', 'convert_dates', 'bool | list[str]', 'keep_default_dates', 'bool', 'precise_float', 'bool', 'dtype_backend', 'DtypeBackend | lib.NoDefault', 'return', 'None')):
        self.json = json
    # WARNING: Decompyle incomplete

    check_keys_split = (lambda self = None, decoded = None: bad_keys = set(decoded.keys()).difference(set(self._split_keys))if bad_keys:
bad_keys_joined = ', '.join(bad_keys)raise ValueError(f'''JSON data had unexpected key(s): {bad_keys_joined}'''))()
    parse = (lambda self = None: obj = self._parse()if self.convert_axes:
obj = self._convert_axes(obj)obj = self._try_convert_types(obj)obj)()
    
    def _parse(self = None):
        raise AbstractMethodError(self)

    _convert_axes = (lambda self = None, obj = None: for axis_name in obj._AXIS_ORDERS:
ax = obj._get_axis(axis_name)ser = Series(ax, dtype = ax.dtype, copy = False)(new_ser, result) = self._try_convert_data(name = axis_name, data = ser, use_dtypes = False, convert_dates = True, is_axis = True)if result:
new_axis = Index(new_ser, dtype = new_ser.dtype, copy = False)setattr(obj, axis_name, new_axis)obj)()
    
    def _try_convert_types(self, obj):
        raise AbstractMethodError(self)

    _try_convert_data = (lambda self, name = None, data = None, use_dtypes = final, convert_dates = (True, True, False), is_axis = ('name', 'Hashable', 'data', 'Series', 'use_dtypes', 'bool', 'convert_dates', 'bool | list[str]', 'is_axis', 'bool', 'return', 'tuple[Series, bool]'): org_data = data# WARNING: Decompyle incomplete
)()
    _try_convert_to_date = (lambda self = None, data = None: if not len(data):
datanew_data = Noneif new_data.dtype == 'object' or new_data.dtype == 'string':
try:
new_data = data.astype('int64')except OverflowError:
except (TypeError, ValueError):
passif not issubclass(new_data.dtype.type, np.number) and in_range.all():
dataif (isna(new_data._values) | (new_data > self.min_stamp) | (new_data._values == iNaT)).dtype == 'string':
warnings.catch_warnings()warnings.simplefilter('ignore', UserWarning)for None in (None, 'iso8601', 'mixed'):
None(None, None)except Exception:
continueNone(None, None)with None:
if not None:
passelif self.date_unit:
passfor None in date_units:
data = to_datetime(new_data, errors = 'raise', unit = date_unit)_ = data.dt.as_unit('ns')(self.date_unit,)except OutOfBoundsDatetime:
continueexcept (ValueError, OverflowError, TypeError):
continuedata)()


class SeriesParser(Parser):
    _default_orient = 'index'
    _split_keys = ('name', 'index', 'data')
    
    def _parse(self = None):
        data = ujson_loads(self.json, precise_float = self.precise_float)
    # WARNING: Decompyle incomplete

    
    def _try_convert_types(self = None, obj = None):
        (obj, _) = self._try_convert_data('data', obj, convert_dates = self.convert_dates)
        return obj



class FrameParser(Parser):
    _default_orient = 'columns'
    _split_keys = ('columns', 'index', 'data')
    
    def _parse(self = None):
        json = self.json
        orient = self.orient
    # WARNING: Decompyle incomplete

    
    def _try_convert_types(self = None, obj = None):
        arrays = []
        for col_label, series in obj.items():
            (result, _) = self._try_convert_data(col_label, series, convert_dates = _should_convert_dates(self.convert_dates, keep_default_dates = self.keep_default_dates, col = col_label))
            arrays.append(result.array)
            return DataFrame._from_arrays(arrays, obj.columns, obj.index, verify_integrity = False)



def _should_convert_dates(convert_dates = None, keep_default_dates = None, col = None):
    '''
    Return bool whether a DataFrame column should be cast to datetime.
    '''
    if convert_dates is False:
        return False
    if None(convert_dates, bool) and col in set(convert_dates):
        return True
    if not None:
        return False
    if not None(col, str):
        return False
    col_lower = None.lower()
    if col_lower.endswith(('_at', '_time')) and col_lower in frozenset({'date', 'datetime', 'modified'}) or col_lower.startswith('timestamp'):
        return True
