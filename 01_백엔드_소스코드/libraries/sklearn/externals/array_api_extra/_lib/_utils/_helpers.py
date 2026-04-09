# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _helpers.pyc (Python 3.11)

'''Helper functions used by `array_api_extra/_funcs.py`.'''
from __future__ import annotations
import io
import math
import pickle
import types
from collections.abc import Callable, Generator, Iterable
from functools import wraps
from types import ModuleType
from typing import TYPE_CHECKING, Any, ClassVar, Generic, Literal, ParamSpec, TypeAlias, TypeVar, cast
from  import _compat
from _compat import array_namespace, is_array_api_obj, is_dask_namespace, is_jax_namespace, is_numpy_array, is_pydata_sparse_namespace, is_torch_namespace
from _typing import Array, Device
if TYPE_CHECKING:
    from typing_extensions import TypeIs, override
else:
    
    def override(func):
        return func

P = ParamSpec('P')
T = TypeVar('T')
__all__ = [
    'asarrays',
    'capabilities',
    'eager_shape',
    'in1d',
    'is_python_scalar',
    'jax_autojit',
    'mean',
    'meta_namespace',
    'pickle_flatten',
    'pickle_unflatten']

def in1d(x1 = None, x2 = None, *, assume_unique, invert, xp):
    '''
    Check whether each element of an array is also present in a second array.

    Returns a boolean array the same length as `x1` that is True
    where an element of `x1` is in `x2` and False otherwise.

    This function has been adapted using the original implementation
    present in numpy:
    https://github.com/numpy/numpy/blob/v1.26.0/numpy/lib/arraysetops.py#L524-L758
    '''
    pass
# WARNING: Decompyle incomplete


def mean(x = None, *, axis, keepdims, xp):
    '''
    Complex mean, https://github.com/data-apis/array-api/issues/846.
    '''
    pass
# WARNING: Decompyle incomplete


def is_python_scalar(x = None):
