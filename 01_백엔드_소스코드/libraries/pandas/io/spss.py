# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: spss.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from pandas._libs import lib
from pandas.compat._optional import import_optional_dependency
from pandas.util._decorators import set_module
from pandas.util._validators import check_dtype_backend
from pandas.core.dtypes.inference import is_list_like
from pandas.io.common import stringify_path
if TYPE_CHECKING:
    from collections.abc import Sequence
    from pathlib import Path
    from pandas._typing import DtypeBackend
    from pandas import DataFrame
read_spss = (lambda path = None, usecols = None, convert_categoricals = set_module('pandas'), dtype_backend = (None, True, lib.no_default): pyreadstat = import_optional_dependency('pyreadstat')check_dtype_backend(dtype_backend)# WARNING: Decompyle incomplete
)()
