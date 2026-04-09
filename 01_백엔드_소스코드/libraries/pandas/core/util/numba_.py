# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numba_.pyc (Python 3.11)

'''Common utilities for Numba operations'''
from __future__ import annotations
import inspect
import types
from typing import TYPE_CHECKING
import numpy as np
from pandas.compat._optional import import_optional_dependency
from pandas.errors import NumbaUtilError
if TYPE_CHECKING:
    from collections.abc import Callable
GLOBAL_USE_NUMBA: 'bool' = False

def maybe_use_numba(engine = None):
