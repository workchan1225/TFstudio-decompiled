# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arrow_parser_wrapper.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
import warnings
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.errors import Pandas4Warning, ParserError, ParserWarning
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import pandas_dtype
from pandas.core.dtypes.inference import is_integer
from pandas.io._util import arrow_table_to_pandas
from pandas.io.parsers.base_parser import ParserBase
if TYPE_CHECKING:
    import pyarrow as pa
    from pandas._typing import ReadBuffer
    from pandas import DataFrame

class ArrowParserWrapper(ParserBase):
    pass
# WARNING: Decompyle incomplete
