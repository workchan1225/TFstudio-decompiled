# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: array.pyc (Python 3.11)

from __future__ import annotations
from datetime import date, datetime
import functools
import operator
from pathlib import Path
import re
import textwrap
from typing import TYPE_CHECKING, Any, Literal, Self, cast, overload
import unicodedata
import warnings
import numpy as np
from pandas._config import is_nan_na
from pandas._libs import lib
from pandas._libs.missing import is_pdna_or_none
from pandas._libs.tslibs import Timedelta, Timestamp, timezones
from pandas.compat import HAS_PYARROW, PYARROW_MIN_VERSION, pa_version_under21p0
from pandas.errors import Pandas4Warning
from pandas.util._decorators import doc, set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.cast import can_hold_element, construct_1d_object_array_from_listlike, infer_dtype_from_scalar
from pandas.core.dtypes.common import is_array_like, is_bool_dtype, is_float_dtype, is_integer, is_list_like, is_numeric_dtype, is_scalar, is_string_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype
from pandas.core.dtypes.missing import isna
from pandas.core import algorithms as algos, missing, ops, roperator
from pandas.core.algorithms import map_array
from pandas.core.arraylike import OpsMixin
from pandas.core.arrays._arrow_string_mixins import ArrowStringArrayMixin
from pandas.core.arrays._utils import to_numpy_dtype_inference
from pandas.core.arrays.base import ExtensionArray, ExtensionArraySupportsAnyAll
from pandas.core.arrays.masked import BaseMaskedArray
from pandas.core.arrays.string_ import StringDtype

common
from pandas.core.construction import extract_array
import pandas.core.common, core
from pandas.core.indexers import check_array_indexer, getitem_returns_view, unpack_tuple_and_ellipses, validate_indices
from pandas.core.nanops import check_below_min_count
from pandas.io._util import _arrow_dtype_mapping
from pandas.tseries.frequencies import to_offset
# WARNING: Decompyle incomplete
