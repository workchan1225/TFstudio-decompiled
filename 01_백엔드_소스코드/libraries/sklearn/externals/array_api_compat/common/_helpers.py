# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _helpers.pyc (Python 3.11)

'''
Various helper functions which are not part of the spec.

Functions which start with an underscore are for internal use only but helpers
that are in __all__ are intended as additional helper functions for use by end
users of the compat library.
'''
from __future__ import annotations
import inspect
import math
import sys
import warnings
from collections.abc import Collection, Hashable
from functools import lru_cache
from typing import TYPE_CHECKING, Any, Final, Literal, SupportsIndex, TypeAlias, TypeGuard, TypeVar, cast, overload
from _typing import Array, Device, HasShape, Namespace, SupportsArrayNamespace
if TYPE_CHECKING:
    from dask.array import array as da
    import jax
    import ndonnx as ndx
    import numpy as np
    from numpy.typing import typing as npt
    import sparse
    import torch
    from typing_extensions import TypeIs, TypeVar
    _SizeT = TypeVar('_SizeT', bound = int | None)
    _ZeroGradientArray: 'TypeAlias' = npt.NDArray[np.void]
    _CupyArray: 'TypeAlias' = Any
    _ArrayApiObj: 'TypeAlias' = npt.NDArray[Any] | da.Array | jax.Array | ndx.Array | sparse.SparseArray | torch.Tensor | SupportsArrayNamespace[Any] | _CupyArray
_API_VERSIONS_OLD: 'Final' = frozenset({
    '2021.12',
    '2022.12',
    '2023.12'})
_API_VERSIONS: 'Final' = _API_VERSIONS_OLD | frozenset({
    '2024.12'})
_issubclass_fast = (lambda cls = None, modname = None, clsname = lru_cache(100): try:
mod = sys.modules[modname]except KeyError:
Falseparent_cls = getattr(mod, clsname)issubclass(cls, parent_cls))()

def _is_jax_zero_gradient_array(x = None):
    '''Return True if `x` is a zero-gradient array.

    These arrays are a design quirk of Jax that may one day be removed.
    See https://github.com/google/jax/issues/20620.
    '''
    
    try:
        dtype = x.dtype
    except AttributeError:
        return False

    cls = cast(Hashable, type(dtype))
    if not _issubclass_fast(cls, 'numpy.dtypes', 'VoidDType'):
        return False
    if None not in sys.modules:
        return False
    import jax
    return dtype == jax.float0


def is_numpy_array(x = None):
