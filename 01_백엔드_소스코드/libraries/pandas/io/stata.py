# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stata.pyc (Python 3.11)

'''
Module contains tools for processing Stata files into DataFrames

The StataReader below was originally written by Joe Presbrey as part of PyDTA.
It has been extended and improved by Skipper Seabold from the Statsmodels
project who also developed the StataWriter and was finally added to pandas in
a once again improved version.

You can find more information on http://presbrey.mit.edu/PyDTA and
https://www.statsmodels.org/devel/
'''
from __future__ import annotations
from collections import abc
from datetime import datetime, timedelta
from io import BytesIO
import os
import struct
import sys
from typing import IO, TYPE_CHECKING, AnyStr, Final, Self, cast
import warnings
import numpy as np
from pandas._libs import lib
from pandas._libs.lib import infer_dtype
from pandas._libs.writers import max_len_string_array
from pandas.errors import CategoricalConversionWarning, InvalidColumnName, Pandas4Warning, PossiblePrecisionLoss, ValueLabelTypeMismatch
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.base import ExtensionDtype
from pandas.core.dtypes.common import ensure_object, is_numeric_dtype, is_string_dtype
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas import Categorical, DatetimeIndex, NaT, Timestamp, isna, to_datetime
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import Index
from pandas.core.indexes.range import RangeIndex
from pandas.core.series import Series
from pandas.core.shared_docs import _shared_docs
from pandas.io.common import get_handle
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Sequence
    from types import TracebackType
    from typing import Literal
    from pandas._typing import CompressionOptions, FilePath, ReadBuffer, StorageOptions, WriteBuffer
_version_error = 'Version of given Stata file is {version}. pandas supports importing versions 102, 103, 104, 105, 108, 110 (Stata 7), 111 (Stata 7SE),  113 (Stata 8/9), 114 (Stata 10/11), 115 (Stata 12), 117 (Stata 13), 118 (Stata 14/15/16), and 119 (Stata 15/16, over 32,767 variables).'
_statafile_processing_params1 = 'convert_dates : bool, default True\n    Convert date variables to DataFrame time values.\nconvert_categoricals : bool, default True\n    Read value labels and convert columns to Categorical/Factor variables.'
_statafile_processing_params2 = 'index_col : str, optional\n    Column to set as index.\nconvert_missing : bool, default False\n    Flag indicating whether to convert missing values to their Stata\n    representations.  If False, missing values are replaced with nan.\n    If True, columns containing missing values are returned with\n    object data types and missing values are represented by\n    StataMissingValue objects.\npreserve_dtypes : bool, default True\n    Preserve Stata datatypes. If False, numeric data are upcast to pandas\n    default types for foreign data (float64 or int64).\ncolumns : list or None\n    Columns to retain.  Columns will be returned in the given order.  None\n    returns all columns.\norder_categoricals : bool, default True\n    Flag indicating whether converted categorical data are ordered.'
_chunksize_params = 'chunksize : int, default None\n    Return StataReader object for iterations, returns chunks with\n    given number of lines.'
_reader_notes = 'Notes\n-----\nCategorical variables read through an iterator may not have the same\ncategories and dtype. This occurs when  a variable stored in a DTA\nfile is associated to an incomplete set of value labels that only\nlabel a strict subset of the values.'
_stata_reader_doc = f'''Class for reading Stata dta files.\n\nParameters\n----------\npath_or_buf : path (string), buffer or path object\n    string, pathlib.Path or object\n    implementing a binary read() functions.\n{_statafile_processing_params1}\n{_statafile_processing_params2}\n{_chunksize_params}\n{_shared_docs['decompression_options']}\n{_shared_docs['storage_options']}\n\n{_reader_notes}\n'''
_date_formats = [
    '%tc',
    '%tC',
    '%td',
    '%d',
    '%tw',
    '%tm',
    '%tq',
    '%th',
    '%ty']
stata_epoch: 'Final' = datetime(1960, 1, 1)
unix_epoch: 'Final' = datetime(1970, 1, 1)

def _stata_elapsed_date_to_datetime_vec(dates = None, fmt = None):
    '''
    Convert from SIF to datetime. https://www.stata.com/help.cgi?datetime

    Parameters
    ----------
    dates : Series
        The Stata Internal Format date to convert to datetime according to fmt
    fmt : str
        The format to convert to. Can be, tc, td, tw, tm, tq, th, ty
        Returns

    Returns
    -------
    converted : Series
        The converted dates

    Examples
    --------
    >>> dates = pd.Series([52])
    >>> _stata_elapsed_date_to_datetime_vec(dates, "%tw")
    0   1961-01-01
    dtype: datetime64[s]

    Notes
    -----
    datetime/c - tc
        milliseconds since 01jan1960 00:00:00.000, assuming 86,400 s/day
    datetime/C - tC - NOT IMPLEMENTED
        milliseconds since 01jan1960 00:00:00.000, adjusted for leap seconds
    date - td
        days since 01jan1960 (01jan1960 = 0)
    weekly date - tw
        weeks since 1960w1
        This assumes 52 weeks in a year, then adds 7 * remainder of the weeks.
        The datetime value is the start of the week in terms of days in the
        year, not ISO calendar weeks.
    monthly date - tm
        months since 1960m1
    quarterly date - tq
        quarters since 1960q1
    half-yearly date - th
        half-years since 1960h1 yearly
    date - ty
        years since 0000
    '''
    if fmt.startswith(('%tc', 'tc')):
        td = np.timedelta64(stata_epoch - unix_epoch, 'ms')
        res = np.array(dates._values, dtype = 'M8[ms]') + td
        return Series(res, index = dates.index)
    if None.startswith(('%td', 'td', '%d', 'd')):
        td = np.timedelta64(stata_epoch - unix_epoch, 'D')
        res = np.array(dates._values, dtype = 'M8[D]') + td
        return Series(res, index = dates.index)
    if None.startswith(('%tm', 'tm')):
        ordinals = dates + (stata_epoch.year - unix_epoch.year) * 12
        res = np.array(ordinals, dtype = 'M8[M]').astype('M8[s]')
        return Series(res, index = dates.index)
    if None.startswith(('%tq', 'tq')):
        ordinals = dates + (stata_epoch.year - unix_epoch.year) * 4
        res = np.array(ordinals, dtype = 'M8[3M]').astype('M8[s]')
        return Series(res, index = dates.index)
    if None.startswith(('%th', 'th')):
        ordinals = dates + (stata_epoch.year - unix_epoch.year) * 2
        res = np.array(ordinals, dtype = 'M8[6M]').astype('M8[s]')
        return Series(res, index = dates.index)
    if None.startswith(('%ty', 'ty')):
        ordinals = dates - 1970
        res = np.array(ordinals, dtype = 'M8[Y]').astype('M8[s]')
        return Series(res, index = dates.index)
    bad_locs = None.isnan(dates)
    has_bad_values = False
    if bad_locs.any():
        has_bad_values = True
        dates._values[bad_locs] = 1
    dates = dates.astype(np.int64)
    if fmt.startswith(('%tC', 'tC')):
        warnings.warn('Encountered %tC format. Leaving in Stata Internal Format.', stacklevel = find_stack_level())
        conv_dates = Series(dates, dtype = object)
        if has_bad_values:
            conv_dates[bad_locs] = NaT
        return conv_dates
    if None.startswith(('%tw', 'tw')):
        year = stata_epoch.year + dates // 52
        days = (dates % 52) * 7
        per_y = (year - 1970).array.view('Period[Y]')
        per_d = per_y.asfreq('D', how = 'S')
        per_d_shifted = per_d + days._values
        per_s = per_d_shifted.asfreq('s', how = 'S')
        conv_dates_arr = per_s.view('M8[s]')
        conv_dates = Series(conv_dates_arr, index = dates.index)
    else:
        raise ValueError(f'''Date fmt {fmt} not understood''')
    if has_bad_values:
        conv_dates[bad_locs] = NaT
    return conv_dates


def _datetime_to_stata_elapsed_vec(dates = None, fmt = None):
    '''
    Convert from datetime to SIF. https://www.stata.com/help.cgi?datetime

    Parameters
    ----------
    dates : Series
        Series or array containing datetime or datetime64[ns] to
        convert to the Stata Internal Format given by fmt
    fmt : str
        The format to convert to. Can be, tc, td, tw, tm, tq, th, ty
    '''
    pass
# WARNING: Decompyle incomplete

excessive_string_length_error: 'Final' = "\nFixed width strings in Stata .dta files are limited to 244 (or fewer)\ncharacters.  Column '{0}' does not satisfy this restriction. Use the\n'version=117' parameter to write the newer (Stata 13 and later) format.\n"
precision_loss_doc: 'Final' = '\nColumn converted from {0} to {1}, and some data are outside of the lossless\nconversion range. This may result in a loss of precision in the saved data.\n'
value_label_mismatch_doc: 'Final' = '\nStata value labels (pandas categories) must be strings. Column {0} contains\nnon-string labels which will be converted to strings.  Please check that the\nStata data file created has not lost information due to duplicate labels.\n'
invalid_name_doc: 'Final' = '\nNot all pandas column names were valid Stata variable names.\nThe following replacements have been made:\n\n    {0}\n\nIf this is not what you expect, please make sure you have Stata-compliant\ncolumn names in your DataFrame (strings only, max 32 characters, only\nalphanumerics and underscores, no Stata reserved words)\n'
categorical_conversion_warning: 'Final' = '\nOne or more series with value labels are not fully labeled. Reading this\ndataset with an iterator results in categorical variable with different\ncategories. This occurs since it is not possible to know all possible values\nuntil the entire dataset has been read. To avoid this warning, you can either\nread dataset without an iterator, or manually convert categorical data by\n``convert_categoricals`` to False and then accessing the variable labels\nthrough the value_labels method of the reader.\n'

def _cast_to_stata_types(data = None):
    '''
    Checks the dtypes of the columns of a pandas DataFrame for
    compatibility with the data types and ranges supported by Stata, and
    converts if necessary.

    Parameters
    ----------
    data : DataFrame
        The DataFrame to check and convert

    Notes
    -----
    Numeric columns in Stata must be one of int8, int16, int32, float32 or
    float64, with some additional value restrictions.  int8 and int16 columns
    are checked for violations of the value restrictions and upcast if needed.
    int64 data is not usable in Stata, and so it is downcast to int32 whenever
    the value are in the int32 range, and sidecast to float64 when larger than
    this range.  If the int64 values are outside of the range of those
    perfectly representable as float64 values, a warning is raised.

    bool columns are cast to int8.  uint columns are converted to int of the
    same size if there is no loss in precision, otherwise are upcast to a
    larger type.  uint64 is currently not supported since it is concerted to
    object in a DataFrame.
    '''
    ws = ''
    conversion_data = ((np.bool_, np.int8, np.int8), (np.uint8, np.int8, np.int16), (np.uint16, np.int16, np.int32), (np.uint32, np.int32, np.int64), (np.uint64, np.int64, np.float64))
    float32_max = struct.unpack('<f', b'\xff\xff\xff~')[0]
    float64_max = struct.unpack('<d', b'\xff\xff\xff\xff\xff\xff\xdf\x7f')[0]
# WARNING: Decompyle incomplete


class StataValueLabel:
    '''
    Parse a categorical column and prepare formatted output

    Parameters
    ----------
    catarray : Series
        Categorical Series to encode
    encoding : {"latin-1", "utf-8"}
        Encoding to use for value labels.
    '''
    
    def __init__(self = None, catarray = None, encoding = None):
        if encoding not in ('latin-1', 'utf-8'):
            raise ValueError('Only latin-1 and utf-8 are supported.')
        self.labname = catarray.name
        self._encoding = encoding
        categories = catarray.cat.categories
        self.value_labels = enumerate(categories)
        self._prepare_value_labels()

    
    def _prepare_value_labels(self = None):
        '''Encode value labels.'''
        self.text_len = 0
        self.txt = []
        self.n = 0
        self.off = np.array([], dtype = np.int32)
        self.val = np.array([], dtype = np.int32)
        self.len = 0
        offsets = []
        values = []
        for vl in self.value_labels:
            category = vl[1]
            if not isinstance(category, str):
                category = str(category)
                warnings.warn(value_label_mismatch_doc.format(self.labname), ValueLabelTypeMismatch, stacklevel = find_stack_level())
            category = category.encode(self._encoding)
            offsets.append(self.text_len)
            values.append(vl[0])
            self.txt.append(category)
            np.array(offsets, dtype = np.int32) = self, self.n += 1, .n
            self.val = np.array(values, dtype = np.int32)
            self.len = 8 + 4 * self.n + 4 * self.n + self.text_len
            return None

    
    def generate_value_label(self = None, byteorder = None):
        '''
        Generate the binary representation of the value labels.

        Parameters
        ----------
        byteorder : str
            Byte order of the output

        Returns
        -------
        value_label : bytes
            Bytes containing the formatted value label
        '''
        encoding = self._encoding
        bio = BytesIO()
        null_byte = b'\x00'
        bio.write(struct.pack(byteorder + 'i', self.len))
        labname = str(self.labname)[:32].encode(encoding)
        lab_len = 32 if encoding not in ('utf-8', 'utf8') else 128
        labname = _pad_bytes(labname, lab_len + 1)
        bio.write(labname)
        for i in range(3):
            bio.write(struct.pack('c', null_byte))
            bio.write(struct.pack(byteorder + 'i', self.n))
            bio.write(struct.pack(byteorder + 'i', self.text_len))
            for offset in self.off:
                bio.write(struct.pack(byteorder + 'i', offset))
                for value in self.val:
                    bio.write(struct.pack(byteorder + 'i', value))
                    for text in self.txt:
                        bio.write(text + null_byte)
                        return bio.getvalue()



class StataNonCatValueLabel(StataValueLabel):
    '''
    Prepare formatted version of value labels

    Parameters
    ----------
    labname : str
        Value label name
    value_labels: Dictionary
        Mapping of values to labels
    encoding : {"latin-1", "utf-8"}
        Encoding to use for value labels.
    '''
    
    def __init__(self = None, labname = None, value_labels = None, encoding = ('latin-1',)):
        if encoding not in ('latin-1', 'utf-8'):
            raise ValueError('Only latin-1 and utf-8 are supported.')
        self.labname = labname
        self._encoding = encoding
        self.value_labels = sorted(value_labels.items(), key = (lambda x: x[0]))
        self._prepare_value_labels()



class StataMissingValue:
    """
    An observation's missing value.

    Parameters
    ----------
    value : {int, float}
        The Stata missing value code

    Notes
    -----
    More information: <https://www.stata.com/help.cgi?missing>

    Integer missing values make the code '.', '.a', ..., '.z' to the ranges
    101 ... 127 (for int8), 32741 ... 32767  (for int16) and 2147483621 ...
    2147483647 (for int32).  Missing values for floating point data types are
    more complex but the pattern is simple to discern from the following table.

    np.float32 missing values (float in Stata)
    0000007f    .
    0008007f    .a
    0010007f    .b
    ...
    00c0007f    .x
    00c8007f    .y
    00d0007f    .z

    np.float64 missing values (double in Stata)
    000000000000e07f    .
    000000000001e07f    .a
    000000000002e07f    .b
    ...
    000000000018e07f    .x
    000000000019e07f    .y
    00000000001ae07f    .z
    """
    MISSING_VALUES: 'dict[float, str]' = { }
    bases: 'Final' = (101, 32741, 2147483621)
    for b in bases:
        MISSING_VALUES[b] = '.'
        for i in range(1, 27):
            MISSING_VALUES[i + b] = '.' + chr(96 + i)
            float32_base: 'bytes' = b'\x00\x00\x00\x7f'
            increment_32: 'int' = struct.unpack('<i', b'\x00\x08\x00\x00')[0]
            for i in range(27):
                key = struct.unpack('<f', float32_base)[0]
                MISSING_VALUES[key] = '.'
                if i > 0:
                    pass
                struct.unpack('<i', struct.pack('<f', key))[0] + increment_32 = None
                float32_base = struct.pack('<i', int_value)
                float64_base: 'bytes' = b'\x00\x00\x00\x00\x00\x00\xe0\x7f'
                increment_64 = struct.unpack('q', b'\x00\x00\x00\x00\x00\x01\x00\x00')[0]
                for i in range(27):
                    key = struct.unpack('<d', float64_base)[0]
                    MISSING_VALUES[key] = '.'
                    if i > 0:
                        pass
                    struct.unpack('q', struct.pack('<d', key))[0] + increment_64 = None
                    float64_base = struct.pack('q', int_value)
                    BASE_MISSING_VALUES: 'Final' = {
                        'int8': 101,
                        'int16': 32741,
                        'int32': 2147483621,
                        'float32': struct.unpack('<f', float32_base)[0],
                        'float64': struct.unpack('<d', float64_base)[0] }
                    
                    def __init__(self = None, value = None):
                        self._value = value
                        value = int(value) if value < 0x80000000 else float(value)
                        self._str = self.MISSING_VALUES[value]

                    string = (lambda self = None: self._str)()
                    value = (lambda self = None: self._value)()
                    
                    def __str__(self = None):
                        return self.string

                    
                    def __repr__(self = None):
                        return f'''{type(self)}({self})'''

                    
                    def __eq__(self = None, other = None):
