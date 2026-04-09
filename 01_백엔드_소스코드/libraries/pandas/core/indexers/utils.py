# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''
Low-dependency indexing utilities.
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import numpy as np
from pandas._libs import lib
from pandas.util._decorators import set_module
from pandas.core.dtypes.common import is_array_like, is_bool_dtype, is_integer, is_integer_dtype, is_list_like
from pandas.core.dtypes.dtypes import ExtensionDtype
from pandas.core.dtypes.generic import ABCIndex, ABCSeries
if TYPE_CHECKING:
    from pandas._typing import AnyArrayLike
    from pandas.core.frame import DataFrame
    from pandas.core.indexes.base import Index

def is_valid_positional_slice(slc = None):
