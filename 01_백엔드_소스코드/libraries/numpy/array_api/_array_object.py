# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _array_object.pyc (Python 3.11)

'''
Wrapper class around the ndarray object for the array API standard.

The array API standard defines some behaviors differently than ndarray, in
particular, type promotion rules are different (the standard has no
value-based casting). The standard also specifies a more limited subset of
array methods and functionalities than are implemented on ndarray. Since the
goal of the array_api namespace is to be a minimal implementation of the array
API standard, we need to define a separate wrapper class for the array_api
namespace.

The standard compliant class is only a wrapper class. It is *not* a subclass
of ndarray.
'''
from __future__ import annotations
import operator
from enum import IntEnum
from _creation_functions import asarray
from _dtypes import _all_dtypes, _boolean_dtypes, _integer_dtypes, _integer_or_boolean_dtypes, _floating_dtypes, _complex_floating_dtypes, _numeric_dtypes, _result_type, _dtype_categories
from typing import TYPE_CHECKING, Optional, Tuple, Union, Any, SupportsIndex
import types
if TYPE_CHECKING:
    from _typing import Any, PyCapsule, Device, Dtype
    from numpy.typing import typing as npt
import numpy as np
from numpy import array_api

class Array:
    pass
# WARNING: Decompyle incomplete
