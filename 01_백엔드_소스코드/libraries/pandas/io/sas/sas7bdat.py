# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sas7bdat.pyc (Python 3.11)

'''
Read SAS7BDAT files

Based on code written by Jared Hobbs:
  https://bitbucket.org/jaredhobbs/sas7bdat

See also:
  https://github.com/BioStatMatt/sas7bdat

Partial documentation of the file format:
  https://cran.r-project.org/package=sas7bdat/vignettes/sas7bdat.pdf

Reference for binary data compression:
  http://collaboration.cmc.ec.gc.ca/science/rpn/biblio/ddj/Website/articles/CUJ/1992/9210/ross/ross.htm
'''
from __future__ import annotations
from datetime import datetime
import sys
from typing import TYPE_CHECKING
import numpy as np
from pandas._config import using_string_dtype
from pandas._libs.byteswap import read_double_with_byteswap, read_float_with_byteswap, read_uint16_with_byteswap, read_uint32_with_byteswap, read_uint64_with_byteswap
from pandas._libs.sas import Parser, get_subheader_index
from pandas._libs.tslibs.conversion import cast_from_unit_vectorized
from pandas.errors import EmptyDataError
import pandas as pd
from pandas import DataFrame, Timestamp
from pandas.io.common import get_handle


sas_constants
from pandas.io.sas.sasreader import SASReader
import pandas.io.sas.sas_constants, io, sas
if TYPE_CHECKING:
    from pandas._typing import CompressionOptions, FilePath, ReadBuffer
_unix_origin = Timestamp('1970-01-01')
_sas_origin = Timestamp('1960-01-01')

def _convert_datetimes(sas_datetimes = None, unit = None):
    '''
    Convert to Timestamp if possible, otherwise to datetime.datetime.
    SAS float64 lacks precision for more than ms resolution so the fit
    to datetime.datetime is ok.

    Parameters
    ----------
    sas_datetimes : {Series, Sequence[float]}
       Dates or datetimes in SAS
    unit : {\'d\', \'s\'}
       "d" if the floats represent dates, "s" for datetimes

    Returns
    -------
    Series
       Series of datetime64 dtype or datetime.datetime.
    '''
    td = (_sas_origin - _unix_origin).as_unit('s')
    if unit == 's':
        millis = cast_from_unit_vectorized(sas_datetimes._values, unit = 's', out_unit = 'ms')
        dt64ms = millis.view('M8[ms]') + td
        return pd.Series(dt64ms, index = sas_datetimes.index, copy = False)
    vals = None.array(sas_datetimes, dtype = 'M8[D]') + td
    return pd.Series(vals, dtype = 'M8[s]', index = sas_datetimes.index, copy = False)


class _Column:
    length: 'int' = '_Column'
    
    def __init__(self, col_id, name, label = None, format = None, ctype = None, length = ('col_id', 'int', 'name', 'str | bytes', 'label', 'str | bytes', 'format', 'str | bytes', 'ctype', 'bytes', 'length', 'int', 'return', 'None')):
        self.col_id = col_id
        self.name = name
        self.label = label
        self.format = format
        self.ctype = ctype
        self.length = length



class SAS7BDATReader(SASReader):
    _cached_page: 'bytes | None' = "\n    Read SAS files in SAS7BDAT format.\n\n    Parameters\n    ----------\n    path_or_buf : path name or buffer\n        Name of SAS file or file-like object pointing to SAS file\n        contents.\n    index : column identifier, defaults to None\n        Column to use as index.\n    convert_dates : bool, defaults to True\n        Attempt to convert dates to Pandas datetime values.  Note that\n        some rarely used SAS date formats may be unsupported.\n    blank_missing : bool, defaults to True\n        Convert empty strings to missing values (SAS uses blanks to\n        indicate missing character variables).\n    chunksize : int, defaults to None\n        Return SAS7BDATReader object for iterations, returns chunks\n        with given number of lines.\n    encoding : str, 'infer', defaults to None\n        String encoding acc. to Python standard encodings,\n        encoding='infer' tries to detect the encoding from the file header,\n        encoding=None will leave the data in binary format.\n    convert_text : bool, defaults to True\n        If False, text variables are left as raw bytes.\n    convert_header_text : bool, defaults to True\n        If False, header text, including column names, are left as raw\n        bytes.\n    "
    
    def __init__(self, path_or_buf, index, convert_dates, blank_missing, chunksize = None, encoding = None, convert_text = None, convert_header_text = (None, True, True, None, None, True, True, 'infer'), compression = ('path_or_buf', 'FilePath | ReadBuffer[bytes]', 'convert_dates', 'bool', 'blank_missing', 'bool', 'chunksize', 'int | None', 'encoding', 'str | None', 'convert_text', 'bool', 'convert_header_text', 'bool', 'compression', 'CompressionOptions', 'return', 'None')):
        self.index = index
        self.convert_dates = convert_dates
        self.blank_missing = blank_missing
        self.chunksize = chunksize
        self.encoding = encoding
        self.convert_text = convert_text
        self.convert_header_text = convert_header_text
        self.default_encoding = 'latin-1'
        self.compression = b''
        self.column_names_raw = []
        self.column_names = []
        self.column_formats = []
        self.columns = []
        self._current_page_data_subheader_pointers = []
        self._cached_page = None
        self._column_data_lengths = []
        self._column_data_offsets = []
        self._column_types = []
        self._current_row_in_file_index = 0
        self._current_row_on_page_index = 0
        self._current_row_in_file_index = 0
        self.handles = get_handle(path_or_buf, 'rb', is_text = False, compression = compression)
        self._path_or_buf = self.handles.handle
        self._subheader_processors = [
            self._process_rowsize_subheader,
            self._process_columnsize_subheader,
            self._process_subheader_counts,
            self._process_columntext_subheader,
            self._process_columnname_subheader,
            self._process_columnattributes_subheader,
            self._process_format_subheader,
            self._process_columnlist_subheader,
            None]
        
        try:
            self._get_properties()
            self._parse_metadata()
            return None
        except Exception:
            self.close()
            raise 


    
    def column_data_lengths(self = None):
        '''Return a numpy int64 array of the column data lengths'''
        return np.asarray(self._column_data_lengths, dtype = np.int64)

    
    def column_data_offsets(self = None):
        '''Return a numpy int64 array of the column offsets'''
        return np.asarray(self._column_data_offsets, dtype = np.int64)

    
    def column_types(self = None):
        '''
        Returns a numpy character array of the column types:
           s (string) or d (double)
        '''
        return np.asarray(self._column_types, dtype = np.dtype('S1'))

    
    def close(self = None):
        self.handles.close()

    
    def _get_properties(self = None):
        self._path_or_buf.seek(0)
        self._cached_page = self._path_or_buf.read(288)
        if self._cached_page[0:len(const.magic)] != const.magic:
            raise ValueError('magic number mismatch (not a SAS file?)')
        buf = self._read_bytes(const.align_1_offset, const.align_1_length)
        if buf == const.u64_byte_checker_value:
            self.U64 = True
            self._int_length = 8
            self._page_bit_offset = const.page_bit_offset_x64
            self._subheader_pointer_length = const.subheader_pointer_length_x64
        else:
            self.U64 = False
            self._page_bit_offset = const.page_bit_offset_x86
            self._subheader_pointer_length = const.subheader_pointer_length_x86
            self._int_length = 4
        buf = self._read_bytes(const.align_2_offset, const.align_2_length)
        if buf == const.align_1_checker_value:
            align1 = const.align_2_value
        else:
            align1 = 0
        buf = self._read_bytes(const.endianness_offset, const.endianness_length)
        if buf == b'\x01':
            self.byte_order = '<'
            self.need_byteswap = sys.byteorder == 'big'
        else:
            self.byte_order = '>'
            self.need_byteswap = sys.byteorder == 'little'
        buf = self._read_bytes(const.encoding_offset, const.encoding_length)[0]
        if buf in const.encoding_names:
            self.inferred_encoding = const.encoding_names[buf]
            if self.encoding == 'infer':
                self.encoding = self.inferred_encoding
            else:
                self.inferred_encoding = f'''unknown (code={buf})'''
        epoch = datetime(1960, 1, 1)
        x = self._read_float(const.date_created_offset + align1, const.date_created_length)
        self.date_created = epoch + pd.to_timedelta(x, unit = 's')
        x = self._read_float(const.date_modified_offset + align1, const.date_modified_length)
        self.date_modified = epoch + pd.to_timedelta(x, unit = 's')
        self.header_length = self._read_uint(const.header_size_offset + align1, const.header_size_length)
        buf = self._path_or_buf.read(self.header_length - 288)
        if len(self._cached_page) != self.header_length:
            raise ValueError('The SAS7BDAT file appears to be truncated.')
        self._read_uint(const.page_size_offset + align1, const.page_size_length) = self, self._cached_page += buf, ._cached_page

    
    def __next__(self = None):
