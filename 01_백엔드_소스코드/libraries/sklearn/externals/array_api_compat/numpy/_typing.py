# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typing.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Literal, TypeAlias
import numpy as np
Device: 'TypeAlias' = Literal['cpu']
if TYPE_CHECKING:
    DType: 'TypeAlias' = np.dtype[np.bool_ | np.integer[Any] | np.float32 | np.float64 | np.complex64 | np.complex128]
    Array: 'TypeAlias' = np.ndarray[(Any, DType)]
else:
    DType: 'TypeAlias' = np.dtype
    Array: 'TypeAlias' = np.ndarray
__all__ = [
    'Array',
    'DType',
    'Device']
_all_ignore = [
    'np']

def __dir__():
    return __all__
