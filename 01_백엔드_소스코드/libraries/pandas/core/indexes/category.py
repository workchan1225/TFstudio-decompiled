# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: category.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal, Self, cast
import numpy as np
from pandas._libs import index as libindex
from pandas.util._decorators import cache_readonly, set_module
from pandas.core.dtypes.common import is_scalar
from pandas.core.dtypes.dtypes import CategoricalDtype
from pandas.core.dtypes.missing import is_valid_na_for_dtype
from pandas.core.arrays.categorical import Categorical, contains
from pandas.core.construction import extract_array
from pandas.core.indexes.base import Index, maybe_extract_name
from pandas.core.indexes.extension import NDArrayBackedExtensionIndex, inherit_names
if TYPE_CHECKING:
    from collections.abc import Hashable
    from pandas._typing import Dtype, DtypeObj, npt
CategoricalIndex = <NODE:12>()()()
