# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _calamine.pyc (Python 3.11)

from __future__ import annotations
from datetime import date, datetime, time, timedelta
from typing import TYPE_CHECKING, Any, TypeAlias
from pandas.compat._optional import import_optional_dependency
from pandas.io.excel._base import BaseExcelReader
if TYPE_CHECKING:
    from python_calamine import CalamineSheet, CalamineWorkbook
    from pandas._typing import FilePath, NaTType, ReadBuffer, Scalar, StorageOptions
_CellValue: 'TypeAlias' = int | float | str | bool | time | date | datetime | timedelta

def CalamineReader():
    '''CalamineReader'''
    pass
# WARNING: Decompyle incomplete

CalamineReader = <NODE:27>(CalamineReader, 'CalamineReader', BaseExcelReader['CalamineWorkbook'])
