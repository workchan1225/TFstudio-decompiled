# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generic.pyc (Python 3.11)

from __future__ import annotations
import collections
from copy import deepcopy
import datetime as dt
from functools import partial
from json import loads
import operator
import pickle
import re
import sys
from typing import TYPE_CHECKING, Any, ClassVar, Concatenate, Literal, NoReturn, Self, cast, final, overload
import warnings
import numpy as np
from pandas._config import config
from pandas._libs import lib
from pandas._libs.lib import is_range_indexer
from pandas._libs.tslibs import Period, Timestamp, to_offset
from pandas._typing import AlignJoin, AnyArrayLike, ArrayLike, Axes, Axis, AxisInt, CompressionOptions, DtypeArg, DtypeBackend, DtypeObj, FilePath, FillnaOptions, FloatFormatType, FormattersType, Frequency, IgnoreRaise, IndexKeyFunc, IndexLabel, InterpolateOptions, IntervalClosedType, JSONSerializable, Level, ListLike, Manager, NaPosition, NDFrameT, OpenFileErrors, RandomState, ReindexMethod, Renamer, Scalar, SequenceNotStr, SortKind, StorageOptions, Suffixes, T, TimeAmbiguous, TimedeltaConvertibleTypes, TimeNonexistent, TimestampConvertibleTypes, TimeUnit, ValueKeyFunc, WriteBuffer, WriteExcelBuffer, npt
from pandas.compat import CHAINED_WARNING_DISABLED
from pandas.compat._constants import REF_COUNT_METHOD
from pandas.compat._optional import import_optional_dependency
from pandas.compat.numpy import function as nv
from pandas.errors import AbstractMethodError, ChainedAssignmentError, InvalidIndexError, Pandas4Warning
from pandas.errors.cow import _chained_assignment_method_msg
from pandas.util._decorators import deprecate_kwarg, doc
from pandas.util._exceptions import find_stack_level
from pandas.util._validators import check_dtype_backend, validate_ascending, validate_bool_kwarg, validate_inclusive
from pandas.core.dtypes.astype import astype_is_view
from pandas.core.dtypes.cast import can_hold_element
from pandas.core.dtypes.common import ensure_object, ensure_platform_int, ensure_str, is_bool, is_bool_dtype, is_dict_like, is_extension_array_dtype, is_list_like, is_number, is_numeric_dtype, is_re_compilable, is_scalar, pandas_dtype
from pandas.core.dtypes.dtypes import DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas.core.dtypes.generic import ABCDataFrame, ABCSeries
from pandas.core.dtypes.inference import is_hashable, is_nested_list_like
from pandas.core.dtypes.missing import isna, notna
from pandas.core import algorithms as algos, arraylike, common, indexing, missing, nanops, sample
from pandas.core.array_algos.replace import should_use_regex
from pandas.core.arrays import ExtensionArray
from pandas.core.base import PandasObject
from pandas.core.construction import extract_array
from pandas.core.flags import Flags
from pandas.core.indexes.api import DatetimeIndex, Index, MultiIndex, PeriodIndex, default_index, ensure_index
from pandas.core.internals import BlockManager
from pandas.core.methods.describe import describe_ndframe
from pandas.core.missing import clean_fill_method, clean_reindex_fill_method, find_valid_index
from pandas.core.reshape.concat import concat
from pandas.core.shared_docs import _shared_docs
from pandas.core.sorting import get_indexer_indexer
from pandas.core.window import Expanding, ExponentialMovingWindow, Rolling, Window
from pandas.io.formats.format import DataFrameFormatter, DataFrameRenderer
from pandas.io.formats.printing import pprint_thing
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Iterator, Mapping, Sequence
    from pandas._libs.tslibs import BaseOffset
    from pandas._typing import P
    from pandas import DataFrame, ExcelWriter, HDFStore, Series
    from pandas.core.indexers.objects import BaseIndexer
    from pandas.core.resample import Resampler
# WARNING: Decompyle incomplete
