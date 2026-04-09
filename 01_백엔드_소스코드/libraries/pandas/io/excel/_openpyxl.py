# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _openpyxl.pyc (Python 3.11)

from __future__ import annotations
import mmap
from typing import TYPE_CHECKING, Any, cast
import numpy as np
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import doc
from pandas.core.shared_docs import _shared_docs
from pandas.io.excel._base import BaseExcelReader, ExcelWriter
from pandas.io.excel._util import combine_kwargs, validate_freeze_panes
if TYPE_CHECKING:
    from openpyxl import Workbook
    from openpyxl.descriptors.serialisable import Serialisable
    from openpyxl.styles import Fill
    from pandas._typing import ExcelWriterIfSheetExists, FilePath, ReadBuffer, Scalar, StorageOptions, WriteExcelBuffer

class OpenpyxlWriter(ExcelWriter):
    pass
# WARNING: Decompyle incomplete


def OpenpyxlReader():
    '''OpenpyxlReader'''
    pass
# WARNING: Decompyle incomplete

OpenpyxlReader = <NODE:27>(OpenpyxlReader, 'OpenpyxlReader', BaseExcelReader['Workbook'])
