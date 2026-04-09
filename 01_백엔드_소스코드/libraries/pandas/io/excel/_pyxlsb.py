# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pyxlsb.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from pandas.compat._optional import import_optional_dependency
from pandas.io.excel._base import BaseExcelReader
if TYPE_CHECKING:
    from pyxlsb import Workbook
    from pandas._typing import FilePath, ReadBuffer, Scalar, StorageOptions

def PyxlsbReader():
    '''PyxlsbReader'''
    pass
# WARNING: Decompyle incomplete

PyxlsbReader = <NODE:27>(PyxlsbReader, 'PyxlsbReader', BaseExcelReader['Workbook'])
