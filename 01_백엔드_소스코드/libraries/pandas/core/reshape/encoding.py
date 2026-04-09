# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encoding.pyc (Python 3.11)

from __future__ import annotations
from collections import defaultdict
from collections.abc import Hashable, Iterable
import itertools
from typing import TYPE_CHECKING
import numpy as np
from pandas._libs import missing as libmissing
from pandas._libs.sparse import IntIndex
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_integer_dtype, is_list_like, is_object_dtype, pandas_dtype
from pandas.core.dtypes.dtypes import ArrowDtype, CategoricalDtype
from pandas.core.arrays import SparseArray
from pandas.core.arrays.categorical import factorize_from_iterable
from pandas.core.arrays.string_ import StringDtype
from pandas.core.frame import DataFrame
from pandas.core.indexes.api import Index, default_index
from pandas.core.series import Series
if TYPE_CHECKING:
    from pandas._typing import NpDtype
get_dummies = (lambda data, prefix, prefix_sep, dummy_na = None, columns = None, sparse = set_module('pandas'), drop_first = (None, '_', False, None, False, False, None), dtype = ('prefix_sep', 'str | Iterable[str] | dict[str, str]', 'dummy_na', 'bool', 'sparse', 'bool', 'drop_first', 'bool', 'dtype', 'NpDtype | None', 'return', 'DataFrame'): pass# WARNING: Decompyle incomplete
)()

def _get_dummies_1d(data, prefix, prefix_sep = None, dummy_na = None, sparse = None, drop_first = ('_', False, False, False, None), dtype = ('prefix_sep', 'str | Iterable[str] | dict[str, str]', 'dummy_na', 'bool', 'sparse', 'bool', 'drop_first', 'bool', 'dtype', 'NpDtype | None', 'return', 'DataFrame')):
    pass
# WARNING: Decompyle incomplete

from_dummies = (lambda data = None, sep = None, default_category = set_module('pandas'): pass# WARNING: Decompyle incomplete
)()
