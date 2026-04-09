# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _odswriter.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
import datetime
import json
from typing import TYPE_CHECKING, Any, DefaultDict, cast, overload
from pandas.io.excel._base import ExcelWriter
from pandas.io.excel._util import combine_kwargs, validate_freeze_panes
if TYPE_CHECKING:
    from odf.opendocument import OpenDocumentSpreadsheet
    from pandas._typing import ExcelWriterIfSheetExists, FilePath, StorageOptions, WriteExcelBuffer
    from pandas.io.formats.excel import ExcelCell

class ODSWriter(ExcelWriter):
    pass
# WARNING: Decompyle incomplete
