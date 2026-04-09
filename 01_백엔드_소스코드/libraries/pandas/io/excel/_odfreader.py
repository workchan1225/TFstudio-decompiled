# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _odfreader.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, cast
import numpy as np
from pandas._typing import FilePath, ReadBuffer, Scalar, StorageOptions
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import doc
import pandas as pd
from pandas.core.shared_docs import _shared_docs
from pandas.io.excel._base import BaseExcelReader
if TYPE_CHECKING:
    from odf.opendocument import OpenDocument
    from pandas._libs.tslibs.nattype import NaTType

def ODFReader():
    '''ODFReader'''
    pass
# WARNING: Decompyle incomplete

ODFReader = <NODE:27>(ODFReader, 'ODFReader', BaseExcelReader['OpenDocument'])()
