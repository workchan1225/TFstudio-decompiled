# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: accessor.pyc (Python 3.11)

from __future__ import annotations
import codecs
from functools import wraps
import re
from typing import TYPE_CHECKING, Literal, cast
import warnings
import numpy as np
from pandas._config import using_string_dtype
from pandas._libs import lib
from pandas._typing import AlignJoin, DtypeObj, F, Scalar, npt
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import ensure_object, is_bool_dtype, is_extension_array_dtype, is_integer, is_list_like, is_numeric_dtype, is_object_dtype, is_re, is_string_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, CategoricalDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCIndex, ABCMultiIndex, ABCSeries
from pandas.core.dtypes.missing import isna
from pandas.core.arrays import ExtensionArray
from pandas.core.base import NoNewAttributesMixin
from pandas.core.construction import extract_array
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Iterator
    from pandas._typing import NpDtype
    from pandas import DataFrame, Index, Series
_cpython_optimized_encoders = ('utf-8', 'utf8', 'latin-1', 'latin1', 'iso-8859-1', 'mbcs', 'ascii')
# WARNING: Decompyle incomplete
