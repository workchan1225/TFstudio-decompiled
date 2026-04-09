# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grouper.pyc (Python 3.11)

'''
Provide user facing operators for doing the split part of the
split-apply-combine paradigm.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, final
import numpy as np
from pandas._libs import algos as libalgos
from pandas._libs.tslibs import OutOfBoundsDatetime
from pandas.errors import InvalidIndexError
from pandas.util._decorators import cache_readonly, set_module
from pandas.core.dtypes.common import ensure_int64, ensure_platform_int, is_list_like, is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core import algorithms
from pandas.core.arrays import Categorical, ExtensionArray

common
from pandas.core.frame import DataFrame
import pandas.core.common, core
from pandas.core.groupby import ops
from pandas.core.groupby.categorical import recode_for_groupby
from pandas.core.indexes.api import Index, MultiIndex, default_index
from pandas.core.series import Series
from pandas.io.formats.printing import PrettyDict, pprint_thing
if TYPE_CHECKING:
    from collections.abc import Hashable, Iterator
    from pandas._typing import ArrayLike, NDFrameT, npt
    from pandas.core.generic import NDFrame
Grouper = <NODE:12>()
Grouping = <NODE:12>()

def get_grouper(obj, key, level = None, sort = set_module('pandas'), observed = final, validate = (None, None, True, False, True, True), dropna = ('obj', 'NDFrameT', 'sort', 'bool', 'observed', 'bool', 'validate', 'bool', 'dropna', 'bool', 'return', 'tuple[ops.BaseGrouper, frozenset[Hashable], NDFrameT]')):
    """
    Create and return a BaseGrouper, which is an internal
    mapping of how to create the grouper indexers.
    This may be composed of multiple Grouping objects, indicating
    multiple groupers

    Groupers are ultimately index mappings. They can originate as:
    index mappings, keys to columns, functions, or Groupers

    Groupers enable local references to level,sort, while
    the passed in level, and sort are 'global'.

    This routine tries to figure out what the passing in references
    are and then creates a Grouping for each one, combined into
    a BaseGrouper.

    If observed & we have a categorical grouper, only show the observed
    values.

    If validate, then check for key/level overlaps.

    """
    pass
# WARNING: Decompyle incomplete


def _is_label_like(val = None):
