# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: generic.pyc (Python 3.11)

'''
Define the SeriesGroupBy and DataFrameGroupBy
classes that hold the groupby interfaces (and some implementations).

These are user facing as the result of the ``df.groupby(...)`` operations,
which here returns a DataFrameGroupBy object.
'''
from __future__ import annotations
from collections import abc
from collections.abc import Callable
import dataclasses
from functools import partial
from textwrap import dedent
from typing import TYPE_CHECKING, Any, Literal, TypeAlias, TypeVar, cast
import warnings
import numpy as np
from pandas._libs import Interval
from pandas._libs.hashtable import duplicated
from pandas.errors import Pandas4Warning, SpecificationError
from pandas.util._decorators import set_module
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import ensure_int64, is_bool, is_dict_like, is_integer_dtype, is_list_like, is_numeric_dtype, is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype, IntervalDtype
from pandas.core.dtypes.inference import is_hashable
from pandas.core.dtypes.missing import isna, notna
from pandas.core import algorithms
from pandas.core.apply import GroupByApply, maybe_mangle_lambdas, reconstruct_func, validate_func_kwargs

common
from pandas.core.frame import DataFrame
import pandas.core.common, core
from pandas.core.groupby import base
from pandas.core.groupby.groupby import GroupBy, GroupByPlot
from pandas.core.indexes.api import Index, MultiIndex, all_indexes_same, default_index
from pandas.core.series import Series
from pandas.core.sorting import get_group_index
from pandas.core.util.numba_ import maybe_use_numba
from pandas.plotting import boxplot_frame_groupby
if TYPE_CHECKING:
    from collections.abc import Hashable, Sequence
    from pandas._typing import ArrayLike, BlockManager, CorrelationMethod, IndexLabel, Manager, SingleBlockManager, TakeIndexer
    from pandas import Categorical
    from pandas.core.generic import NDFrame
AggScalar: 'TypeAlias' = str | Callable[(..., Any)]
ScalarResult = TypeVar('ScalarResult')
NamedAgg = <NODE:12>()()

def SeriesGroupBy():
    '''SeriesGroupBy'''
    pass
# WARNING: Decompyle incomplete

SeriesGroupBy = <NODE:27>(SeriesGroupBy, 'SeriesGroupBy', GroupBy[Series])()

def DataFrameGroupBy():
    '''DataFrameGroupBy'''
    pass
# WARNING: Decompyle incomplete

DataFrameGroupBy = <NODE:27>(DataFrameGroupBy, 'DataFrameGroupBy', GroupBy[DataFrame])()

def _wrap_transform_general_frame(obj = dataclasses.dataclass, group = set_module('pandas.api.typing'), res = set_module('pandas.api.typing')):
    concat = concat
    import pandas
# WARNING: Decompyle incomplete
