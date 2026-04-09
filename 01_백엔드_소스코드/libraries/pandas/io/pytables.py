# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pytables.pyc (Python 3.11)

'''
High level interface to PyTables for reading and writing pandas data structures
to disk
'''
from __future__ import annotations
from contextlib import suppress
import copy
from datetime import date, tzinfo
import itertools
import os
import re
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Final, Literal, Self, TypeAlias, cast, overload
import warnings
import numpy as np
from pandas._config import config, get_option, using_string_dtype
from pandas._libs import lib, writers as libwriters
from pandas._libs.lib import is_string_array
from pandas._libs.tslibs import timezones
from pandas.compat import HAS_PYARROW
from pandas.compat._optional import import_optional_dependency
from pandas.compat.pickle_compat import patch_pickle
from pandas.errors import AttributeConflictWarning, ClosedFileError, IncompatibilityWarning, PerformanceWarning, PossibleDataLossError
from pandas.util._decorators import cache_readonly, set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import ensure_object, is_bool_dtype, is_complex_dtype, is_list_like, is_string_dtype, needs_i8_conversion
from pandas.core.dtypes.dtypes import CategoricalDtype, DatetimeTZDtype, ExtensionDtype, PeriodDtype
from pandas.core.dtypes.missing import array_equivalent
from pandas import DataFrame, DatetimeIndex, Index, MultiIndex, PeriodIndex, RangeIndex, Series, StringDtype, TimedeltaIndex, concat, isna
from pandas.core.arrays import Categorical, DatetimeArray, PeriodArray
from pandas.core.arrays.datetimes import tz_to_dtype
from pandas.core.arrays.string_ import BaseStringArray

common
from pandas.core.computation.pytables import PyTablesExpr, maybe_expression
maybe_expression = maybe_expression
import pandas.core.common, core
from pandas.core.construction import array as pd_array, extract_array
from pandas.core.indexes.api import ensure_index
from pandas.io.common import stringify_path
from pandas.io.formats.printing import adjoin, pprint_thing
if TYPE_CHECKING:
    from collections.abc import Callable, Hashable, Iterator, Sequence
    from types import ModuleType, TracebackType
    from tables import Col, File, Node
    from pandas._typing import AnyArrayLike, ArrayLike, AxisInt, DtypeArg, FilePath, TimeUnit, npt
    from pandas.core.internals import Block
_version = '0.15.2'
_default_encoding = 'UTF-8'

def _ensure_encoding(encoding = None):
    pass
# WARNING: Decompyle incomplete


def _ensure_str(name):
    '''
    Ensure that an index / column name is a str (python 3); otherwise they
    may be np.string dtype. Non-string dtypes are passed through unchanged.

    https://github.com/pandas-dev/pandas/issues/13492
    '''
    if isinstance(name, str):
        name = str(name)
    return name

Term: 'TypeAlias' = PyTablesExpr

def _ensure_term(where = None, scope_level = None):
    '''
    Ensure that the where is a Term or a list of Term.

    This makes sure that we are capturing the scope of variables that are
    passed create the terms here with a frame_level=2 (we are 2 levels down)
    '''
    pass
# WARNING: Decompyle incomplete

incompatibility_doc: 'Final' = '\nwhere criteria is being ignored as this version [%s] is too old (or\nnot-defined), read the file in and write it out to a new file to upgrade (with\nthe copy_to method)\n'
attribute_conflict_doc: 'Final' = '\nthe [%s] attribute of the existing index is [%s] which conflicts with the new\n[%s], resetting the attribute to None\n'
performance_doc: 'Final' = '\nyour performance may suffer as PyTables will pickle object types that it cannot\nmap directly to c-types [inferred_type->%s,key->%s] [items->%s]\n'
_FORMAT_MAP = {
    'f': 'fixed',
    'fixed': 'fixed',
    't': 'table',
    'table': 'table' }
_AXES_MAP = {
    DataFrame: [
        0] }
dropna_doc: 'Final' = '\n: boolean\n    drop ALL nan rows when appending to a table\n'
format_doc: 'Final' = "\n: format\n    default format writing format, if None, then\n    put will default to 'fixed' and append will default to 'table'\n"
config.config_prefix('io.hdf')
config.register_option('dropna_table', False, dropna_doc, validator = config.is_bool)
config.register_option('default_format', None, format_doc, validator = config.is_one_of_factory([
    'fixed',
    'table',
    None]))
None(None, None)
