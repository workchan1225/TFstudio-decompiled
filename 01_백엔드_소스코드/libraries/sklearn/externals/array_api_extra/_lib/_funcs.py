# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _funcs.pyc (Python 3.11)

'''Array-agnostic implementations for the public API.'''
import math
import warnings
from collections.abc import Callable, Sequence
from types import ModuleType, NoneType
from typing import Literal, cast, overload
from _at import at
from _utils import _compat, _helpers
from _utils._compat import array_namespace, is_dask_namespace, is_jax_array
from _utils._helpers import asarrays, capabilities, eager_shape, meta_namespace, ndindex
from _utils._typing import Array, Device, DType
__all__ = [
    'apply_where',
    'atleast_nd',
    'broadcast_shapes',
    'cov',
    'create_diagonal',
    'expand_dims',
    'kron',
    'nunique',
    'pad',
    'setdiff1d',
    'sinc']
apply_where = (lambda cond = None, args = None, f1 = None, f2 = overload, *, xp,
