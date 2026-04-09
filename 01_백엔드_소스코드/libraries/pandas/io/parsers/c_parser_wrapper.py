# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: c_parser_wrapper.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
from typing import TYPE_CHECKING
import warnings
import numpy as np
from pandas._libs import lib, parsers
from pandas.compat._optional import import_optional_dependency
from pandas.errors import DtypeWarning
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import pandas_dtype
from pandas.core.dtypes.concat import concat_compat, union_categoricals
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.indexes.api import ensure_index_from_sequences
from pandas.io.common import dedup_names, is_potential_multi_index
from pandas.io.parsers.base_parser import ParserBase, ParserError, date_converter, evaluate_callable_usecols, is_index_col, validate_parse_dates_presence
if TYPE_CHECKING:
    from collections.abc import Hashable, Mapping, Sequence
    from pandas._typing import AnyArrayLike, ArrayLike, DtypeArg, DtypeObj, ReadCsvBuffer, SequenceT
    from pandas import Index, MultiIndex

class CParserWrapper(ParserBase):
    pass
# WARNING: Decompyle incomplete


def _filter_usecols(usecols = None, names = None):
    pass
# WARNING: Decompyle incomplete


def _concatenate_chunks(chunks = None, column_names = None):
    '''
    Concatenate chunks of data read with low_memory=True.

    The tricky part is handling Categoricals, where different chunks
    may have different inferred categories.
    '''
    pass
# WARNING: Decompyle incomplete


def ensure_dtype_objs(dtype = None):
    '''
    Ensure we have either None, a dtype object, or a dictionary mapping to
    dtype objects.
    '''
    pass
# WARNING: Decompyle incomplete
