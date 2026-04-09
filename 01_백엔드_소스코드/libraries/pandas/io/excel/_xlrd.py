# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _xlrd.pyc (Python 3.11)

from __future__ import annotations
from datetime import time
import math
from typing import TYPE_CHECKING
import numpy as np
from pandas.compat._optional import import_optional_dependency
from pandas.io.excel._base import BaseExcelReader
if TYPE_CHECKING:
    from xlrd import Book
    from pandas._typing import Scalar, StorageOptions

def XlrdReader():
    '''XlrdReader'''
    pass
# WARNING: Decompyle incomplete

XlrdReader = <NODE:27>(XlrdReader, 'XlrdReader', BaseExcelReader['Book'])
