# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: csvs.pyc (Python 3.11)

'''
Module for formatting output data into CSV files.
'''
from __future__ import annotations
from collections.abc import Hashable, Iterable, Iterator, Sequence
import csv as csvlib
import os
from typing import TYPE_CHECKING, Any, cast
import numpy as np
from pandas._libs import writers as libwriters
from pandas._typing import SequenceNotStr
from pandas.util._decorators import cache_readonly
from pandas.core.dtypes.generic import ABCDatetimeIndex, ABCIndex, ABCMultiIndex, ABCPeriodIndex
from pandas.core.dtypes.missing import notna
from pandas.core.indexes.api import Index
from pandas.io.common import get_handle
if TYPE_CHECKING:
    from pandas._typing import CompressionOptions, FilePath, FloatFormatType, IndexLabel, StorageOptions, WriteBuffer, npt
    from pandas.io.formats.format import DataFrameFormatter
_DEFAULT_CHUNKSIZE_CELLS = 100000

class CSVFormatter:
    cols: 'npt.NDArray[np.object_]' = 'CSVFormatter'
    
    def __init__(self, formatter, path_or_buf, sep, cols, index_label, mode, encoding, errors, compression, quoting, lineterminator, chunksize, quotechar = None, date_format = None, doublequote = None, escapechar = ('', ',', None, None, 'w', None, 'strict', 'infer', None, '\n', None, '"', None, True, None, None), storage_options = ('formatter', 'DataFrameFormatter', 'path_or_buf', 'FilePath | WriteBuffer[str] | WriteBuffer[bytes]', 'sep', 'str', 'cols', 'Sequence[Hashable] | None', 'index_label', 'IndexLabel | None', 'mode', 'str', 'encoding', 'str | None', 'errors', 'str', 'compression', 'CompressionOptions', 'quoting', 'int | None', 'lineterminator', 'str | None', 'chunksize', 'int | None', 'quotechar', 'str | None', 'date_format', 'str | None', 'doublequote', 'bool', 'escapechar', 'str | None', 'storage_options', 'StorageOptions | None', 'return', 'None')):
