# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Hashable, Iterable, Mapping, Sequence
import datetime
from decimal import Decimal
from functools import partial
import os
from typing import IO, TYPE_CHECKING, Any, Generic, Literal, Self, TypeVar, Union, cast, overload
import warnings
import zipfile
from pandas._config import config
from pandas._libs import lib
from pandas.compat._optional import get_version, import_optional_dependency
from pandas.errors import EmptyDataError
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.common import is_bool, is_decimal, is_file_like, is_float, is_integer, is_list_like
from pandas.core.frame import DataFrame
from pandas.util.version import Version
from pandas.io.common import IOHandles, get_handle, stringify_path, validate_header_arg
from pandas.io.excel._util import fill_mi_header, get_default_engine, get_writer, maybe_convert_usecols, pop_header_name
from pandas.io.parsers import TextParser
from pandas.io.parsers.readers import validate_integer
if TYPE_CHECKING:
    from types import TracebackType
    from pandas._typing import DtypeArg, DtypeBackend, ExcelWriterIfSheetExists, FilePath, HashableT, IntStrT, ReadBuffer, SequenceNotStr, StorageOptions, WriteExcelBuffer
read_excel = (lambda io = None, sheet_name = None, *, header, names: pass)()
read_excel = (lambda io = None, sheet_name = None, *, header, names: pass)()
read_excel = (lambda io = None, sheet_name = None, *, header, names: check_dtype_backend(dtype_backend)should_close = False# WARNING: Decompyle incomplete
)()
_WorkbookT = TypeVar('_WorkbookT')

def BaseExcelReader():
    '''BaseExcelReader'''
    book: '_WorkbookT' = 'BaseExcelReader'
    
    def __init__(self = None, filepath_or_buffer = None, storage_options = None, engine_kwargs = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    _workbook_class = (lambda self = None: raise NotImplementedError)()
    
    def load_workbook(self = None, filepath_or_buffer = None, engine_kwargs = None):
        raise NotImplementedError

    
    def close(self = None):
        if hasattr(self, 'book'):
            if hasattr(self.book, 'close'):
                self.book.close()
            elif hasattr(self.book, 'release_resources'):
                self.book.release_resources()
        self.handles.close()

    sheet_names = (lambda self = None: raise NotImplementedError)()
    
    def get_sheet_by_name(self = None, name = None):
        raise NotImplementedError

    
    def get_sheet_by_index(self = None, index = None):
        raise NotImplementedError

    
    def get_sheet_data(self = None, sheet = None, rows = None):
        raise NotImplementedError

    
    def raise_if_bad_sheet_by_index(self = None, index = None):
        n_sheets = len(self.sheet_names)
        if index >= n_sheets:
            raise ValueError(f'''Worksheet index {index} is invalid, {n_sheets} worksheets found''')

    
    def raise_if_bad_sheet_by_name(self = None, name = None):
        if name not in self.sheet_names:
            raise ValueError(f'''Worksheet named \'{name}\' not found''')

    
    def _check_skiprows_func(self = None, skiprows = None, rows_to_use = None):
        '''
        Determine how many file rows are required to obtain `nrows` data
        rows when `skiprows` is a function.

        Parameters
        ----------
        skiprows : function
            The function passed to read_excel by the user.
        rows_to_use : int
            The number of rows that will be needed for the header and
            the data.

        Returns
        -------
        int
        '''
        i = 0
        rows_used_so_far = 0
    # WARNING: Decompyle incomplete

    
    def _calc_rows(self, header = None, index_col = None, skiprows = None, nrows = ('header', 'int | Sequence[int] | None', 'index_col', 'int | Sequence[int] | None', 'skiprows', 'Sequence[int] | int | Callable[[int], object] | None', 'nrows', 'int | None', 'return', 'int | None')):
        '''
        If nrows specified, find the number of rows needed from the
        file, otherwise return None.


        Parameters
        ----------
        header : int, list of int, or None
            See read_excel docstring.
        index_col : int, str, list of int, or None
            See read_excel docstring.
        skiprows : list-like, int, callable, or None
            See read_excel docstring.
        nrows : int or None
            See read_excel docstring.

        Returns
        -------
        int or None
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def parse(self, sheet_name, header, names, index_col, usecols, dtype, true_values, false_values, skiprows, nrows, na_values, verbose, parse_dates, date_format, thousands = None, decimal = None, comment = None, skipfooter = (0, 0, None, None, None, None, None, None, None, None, None, False, False, None, None, '.', None, 0, lib.no_default), dtype_backend = ('sheet_name', 'str | int | list[int] | list[str] | None', 'header', 'int | Sequence[int] | None', 'names', 'SequenceNotStr[Hashable] | range | None', 'index_col', 'int | Sequence[int] | None', 'dtype', 'DtypeArg | None', 'true_values', 'Iterable[Hashable] | None', 'false_values', 'Iterable[Hashable] | None', 'skiprows', 'Sequence[int] | int | Callable[[int], object] | None', 'nrows', 'int | None', 'verbose', 'bool', 'parse_dates', 'list | dict | bool', 'date_format', 'dict[Hashable, str] | str | None', 'thousands', 'str | None', 'decimal', 'str', 'comment', 'str | None', 'skipfooter', 'int', 'dtype_backend', 'DtypeBackend | lib.NoDefault'), **kwds):
        validate_header_arg(header)
        validate_integer('nrows', nrows)
        ret_dict = False
        if isinstance(sheet_name, list):
            sheets = sheet_name
            ret_dict = True
    # WARNING: Decompyle incomplete

    
    def _parse_sheet(self, data, output, asheetname, header, names, index_col, usecols, dtype, skiprows, nrows, true_values, false_values, na_values, parse_dates, date_format, thousands = None, decimal = None, comment = None, skipfooter = (None, 0, None, None, None, None, None, None, None, None, None, False, None, None, '.', None, 0, lib.no_default), dtype_backend = ('data', 'list', 'output', 'dict', 'asheetname', 'str | int | None', 'header', 'int | Sequence[int] | None', 'names', 'SequenceNotStr[Hashable] | range | None', 'index_col', 'int | Sequence[int] | None', 'dtype', 'DtypeArg | None', 'skiprows', 'Sequence[int] | int | Callable[[int], object] | None', 'nrows', 'int | None', 'true_values', 'Iterable[Hashable] | None', 'false_values', 'Iterable[Hashable] | None', 'parse_dates', 'list | dict | bool', 'date_format', 'dict[Hashable, str] | str | None', 'thousands', 'str | None', 'decimal', 'str', 'comment', 'str | None', 'skipfooter', 'int', 'dtype_backend', 'DtypeBackend | lib.NoDefault'), **kwds):
        pass
    # WARNING: Decompyle incomplete


BaseExcelReader = <NODE:27>(BaseExcelReader, 'BaseExcelReader', Generic[_WorkbookT])

def ExcelWriter():
    '''ExcelWriter'''
    _supported_extensions: 'tuple[str, ...]' = '\n    Class for writing DataFrame objects into excel sheets.\n\n    Default is to use:\n\n    * `xlsxwriter <https://pypi.org/project/XlsxWriter/>`__ for xlsx files if xlsxwriter\n      is installed otherwise `openpyxl <https://pypi.org/project/openpyxl/>`__\n    * `odf <https://pypi.org/project/odfpy/>`__ for ods files\n\n    See :meth:`DataFrame.to_excel` for typical usage.\n\n    The writer should be used as a context manager. Otherwise, call `close()` to save\n    and close any opened file handles.\n\n    Parameters\n    ----------\n    path : str or typing.BinaryIO\n        Path to xls or xlsx or ods file.\n    engine : str (optional)\n        Engine to use for writing. If None, defaults to\n        ``io.excel.<extension>.writer``.  NOTE: can only be passed as a keyword\n        argument.\n    date_format : str, default None\n        Format string for dates written into Excel files (e.g. \'YYYY-MM-DD\').\n    datetime_format : str, default None\n        Format string for datetime objects written into Excel files.\n        (e.g. \'YYYY-MM-DD HH:MM:SS\').\n    mode : {{\'w\', \'a\'}}, default \'w\'\n        File mode to use (write or append). Append does not work with fsspec URLs.\n    storage_options : dict, optional\n        Extra options that make sense for a particular storage connection, e.g.\n        host, port, username, password, etc. For HTTP(S) URLs the key-value pairs\n        are forwarded to ``urllib.request.Request`` as header options. For other\n        URLs (e.g. starting with "s3://", and "gcs://") the key-value pairs are\n        forwarded to ``fsspec.open``. Please see ``fsspec`` and ``urllib`` for more\n        details, and for more examples on storage options refer `here\n        <https://pandas.pydata.org/docs/user_guide/io.html?\n        highlight=storage_options#reading-writing-remote-files>`_.\n\n    if_sheet_exists : {{\'error\', \'new\', \'replace\', \'overlay\'}}, default \'error\'\n        How to behave when trying to write to a sheet that already\n        exists (append mode only).\n\n        * error: raise a ValueError.\n        * new: Create a new sheet, with a name determined by the engine.\n        * replace: Delete the contents of the sheet before writing to it.\n        * overlay: Write contents to the existing sheet without first removing,\n          but possibly over top of, the existing contents.\n\n    engine_kwargs : dict, optional\n        Keyword arguments to be passed into the engine. These will be passed to\n        the following functions of the respective engines:\n\n        * xlsxwriter: ``xlsxwriter.Workbook(file, **engine_kwargs)``\n        * openpyxl (write mode): ``openpyxl.Workbook(**engine_kwargs)``\n        * openpyxl (append mode): ``openpyxl.load_workbook(file, **engine_kwargs)``\n        * odf: ``odf.opendocument.OpenDocumentSpreadsheet(**engine_kwargs)``\n\n    See Also\n    --------\n    read_excel : Read an Excel sheet values (xlsx) file into DataFrame.\n    read_csv : Read a comma-separated values (csv) file into DataFrame.\n    read_fwf : Read a table of fixed-width formatted lines into DataFrame.\n\n    Notes\n    -----\n    For compatibility with CSV writers, ExcelWriter serializes lists\n    and dicts to strings before writing.\n\n    Examples\n    --------\n    Default usage:\n\n    >>> df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  # doctest: +SKIP\n    >>> with pd.ExcelWriter("path_to_file.xlsx") as writer:\n    ...     df.to_excel(writer)  # doctest: +SKIP\n\n    To write to separate sheets in a single file:\n\n    >>> df1 = pd.DataFrame([["AAA", "BBB"]], columns=["Spam", "Egg"])  # doctest: +SKIP\n    >>> df2 = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  # doctest: +SKIP\n    >>> with pd.ExcelWriter("path_to_file.xlsx") as writer:\n    ...     df1.to_excel(writer, sheet_name="Sheet1")  # doctest: +SKIP\n    ...     df2.to_excel(writer, sheet_name="Sheet2")  # doctest: +SKIP\n\n    You can set the date format or datetime format:\n\n    >>> from datetime import date, datetime  # doctest: +SKIP\n    >>> df = pd.DataFrame(\n    ...     [\n    ...         [date(2014, 1, 31), date(1999, 9, 24)],\n    ...         [datetime(1998, 5, 26, 23, 33, 4), datetime(2014, 2, 28, 13, 5, 13)],\n    ...     ],\n    ...     index=["Date", "Datetime"],\n    ...     columns=["X", "Y"],\n    ... )  # doctest: +SKIP\n    >>> with pd.ExcelWriter(\n    ...     "path_to_file.xlsx",\n    ...     date_format="YYYY-MM-DD",\n    ...     datetime_format="YYYY-MM-DD HH:MM:SS",\n    ... ) as writer:\n    ...     df.to_excel(writer)  # doctest: +SKIP\n\n    You can also append to an existing Excel file:\n\n    >>> with pd.ExcelWriter("path_to_file.xlsx", mode="a", engine="openpyxl") as writer:\n    ...     df.to_excel(writer, sheet_name="Sheet3")  # doctest: +SKIP\n\n    Here, the `if_sheet_exists` parameter can be set to replace a sheet if it\n    already exists:\n\n    >>> with pd.ExcelWriter(\n    ...     "path_to_file.xlsx",\n    ...     mode="a",\n    ...     engine="openpyxl",\n    ...     if_sheet_exists="replace",\n    ... ) as writer:\n    ...     df.to_excel(writer, sheet_name="Sheet1")  # doctest: +SKIP\n\n    You can also write multiple DataFrames to a single sheet. Note that the\n    ``if_sheet_exists`` parameter needs to be set to ``overlay``:\n\n    >>> with pd.ExcelWriter(\n    ...     "path_to_file.xlsx",\n    ...     mode="a",\n    ...     engine="openpyxl",\n    ...     if_sheet_exists="overlay",\n    ... ) as writer:\n    ...     df1.to_excel(writer, sheet_name="Sheet1")\n    ...     df2.to_excel(writer, sheet_name="Sheet1", startcol=3)  # doctest: +SKIP\n\n    You can store Excel file in RAM:\n\n    >>> import io\n    >>> df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])\n    >>> buffer = io.BytesIO()\n    >>> with pd.ExcelWriter(buffer) as writer:\n    ...     df.to_excel(writer)\n\n    You can pack Excel file into zip archive:\n\n    >>> import zipfile  # doctest: +SKIP\n    >>> df = pd.DataFrame([["ABC", "XYZ"]], columns=["Foo", "Bar"])  # doctest: +SKIP\n    >>> with zipfile.ZipFile("path_to_file.zip", "w") as zf:\n    ...     with zf.open("filename.xlsx", "w") as buffer:\n    ...         with pd.ExcelWriter(buffer) as writer:\n    ...             df.to_excel(writer)  # doctest: +SKIP\n\n    You can specify additional arguments to the underlying engine:\n\n    >>> with pd.ExcelWriter(\n    ...     "path_to_file.xlsx",\n    ...     engine="xlsxwriter",\n    ...     engine_kwargs={{"options": {{"nan_inf_to_errors": True}}}},\n    ... ) as writer:\n    ...     df.to_excel(writer)  # doctest: +SKIP\n\n    In append mode, ``engine_kwargs`` are passed through to\n    openpyxl\'s ``load_workbook``:\n\n    >>> with pd.ExcelWriter(\n    ...     "path_to_file.xlsx",\n    ...     engine="openpyxl",\n    ...     mode="a",\n    ...     engine_kwargs={{"keep_vba": True}},\n    ... ) as writer:\n    ...     df.to_excel(writer, sheet_name="Sheet2")  # doctest: +SKIP\n    '
    
    def __new__(cls, path, engine, date_format, datetime_format = None, mode = None, storage_options = None, if_sheet_exists = (None, None, None, 'w', None, None, None), engine_kwargs = ('path', 'FilePath | WriteExcelBuffer | ExcelWriter', 'engine', 'str | None', 'date_format', 'str | None', 'datetime_format', 'str | None', 'mode', 'str', 'storage_options', 'StorageOptions | None', 'if_sheet_exists', 'ExcelWriterIfSheetExists | None', 'engine_kwargs', 'dict | None', 'return', 'Self')):
        pass
    # WARNING: Decompyle incomplete

    supported_extensions = (lambda self = None: self._supported_extensions)()
    engine = (lambda self = None: self._engine)()
    sheets = (lambda self = None: raise NotImplementedError)()
    book = (lambda self = None: raise NotImplementedError)()
    
    def _write_cells(self, cells, sheet_name = None, startrow = None, startcol = None, freeze_panes = (None, 0, 0, None, None), autofilter_range = ('sheet_name', 'str | None', 'startrow', 'int', 'startcol', 'int', 'freeze_panes', 'tuple[int, int] | None', 'autofilter_range', 'str | None', 'return', 'None')):
        '''
        Write given formatted cells into Excel an excel sheet

        Parameters
        ----------
        cells : generator
            cell of formatted data to save to Excel sheet
        sheet_name : str, default None
            Name of Excel sheet, if None, then use self.cur_sheet
        startrow : upper left cell row to dump data frame
        startcol : upper left cell column to dump data frame
        freeze_panes: int tuple of length 2
            contains the bottom-most row and right-most column to freeze
        autofilter_range: str, default None
            column ranges to add automatic filters to, for example "A1:D5"
        '''
        raise NotImplementedError

    
    def _save(self = None):
        '''
        Save workbook to disk.
        '''
        raise NotImplementedError

    
    def __init__(self, path, engine, date_format, datetime_format = None, mode = None, storage_options = None, if_sheet_exists = (None, None, None, 'w', None, None, None), engine_kwargs = ('path', 'FilePath | WriteExcelBuffer | ExcelWriter', 'engine', 'str | None', 'date_format', 'str | None', 'datetime_format', 'str | None', 'mode', 'str', 'storage_options', 'StorageOptions | None', 'if_sheet_exists', 'ExcelWriterIfSheetExists | None', 'engine_kwargs', 'dict[str, Any] | None', 'return', 'None')):
        if isinstance(path, str):
            ext = os.path.splitext(path)[-1]
            self.check_extension(ext)
        if 'b' not in mode:
            mode += 'b'
        mode = mode.replace('a', 'r+')
        if if_sheet_exists not in (None, 'error', 'new', 'replace', 'overlay'):
            raise ValueError(f'''\'{if_sheet_exists}\' is not valid for if_sheet_exists. Valid options are \'error\', \'new\', \'replace\' and \'overlay\'.''')
        if if_sheet_exists and 'r+' not in mode:
            raise ValueError("if_sheet_exists is only valid in append mode (mode='a')")
    # WARNING: Decompyle incomplete

    date_format = (lambda self = None: self._date_format)()
    datetime_format = (lambda self = None: self._datetime_format)()
    if_sheet_exists = (lambda self = None: self._if_sheet_exists)()
    
    def __fspath__(self = None):
        return getattr(self._handles.handle, 'name', '')

    
    def _get_sheet_name(self = None, sheet_name = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _value_with_fmt(self = None, val = None):
        '''
        Convert numpy types to Python types for the Excel writers.

        Parameters
        ----------
        val : object
            Value to be written into cells

        Returns
        -------
        Tuple with the first element being the converted value and the second
            being an optional format
        '''
        fmt = None
        if is_integer(val):
            val = int(val)
        elif is_float(val):
            val = float(val)
        elif is_bool(val):
            val = bool(val)
        elif is_decimal(val):
            val = Decimal(val)
        elif isinstance(val, datetime.datetime):
            fmt = self._datetime_format
        elif isinstance(val, datetime.date):
            fmt = self._date_format
        elif isinstance(val, datetime.timedelta):
            val = val.total_seconds() / 86400
            fmt = '0'
        else:
            val = str(val)
            if len(val) > 32767:
                warnings.warn(f'''Cell contents too long ({len(val)}), truncated to 32767 characters''', UserWarning, stacklevel = find_stack_level())
        return (val, fmt)

    check_extension = (lambda cls = None, ext = None: pass# WARNING: Decompyle incomplete
)()
    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self.close()

    
    def close(self = None):
        '''synonym for save, to make it more file-like'''
        self._save()
        self._handles.close()


ExcelWriter = <NODE:27>(ExcelWriter, 'ExcelWriter', Generic[_WorkbookT])()
XLS_SIGNATURES = (b'\t\x00\x04\x00\x07\x00\x10\x00', b'\t\x02\x06\x00\x00\x00\x10\x00', b'\t\x04\x06\x00\x00\x00\x10\x00', b'\xd0\xcf\x11\xe0\xa1\xb1\x1a\xe1')
ZIP_SIGNATURE = b'PK\x03\x04'
# WARNING: Decompyle incomplete
