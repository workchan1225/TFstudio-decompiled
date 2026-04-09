# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linalg.pyc (Python 3.11)

from __future__ import annotations
import torch
from typing import Optional, Union, Tuple
from torch.linalg import *
from torch import linalg as torch_linalg
linalg_all = dir(torch_linalg)()
from torch import outer
from _aliases import _fix_promotion, sum
from _aliases import matmul, matrix_transpose, tensordot
from _typing import Array, DType
from common._typing import JustInt, JustFloat

def cross(x1 = None, x2 = None, *, axis):
    (x1, x2) = _fix_promotion(x1, x2, only_scalar = False)
    if not  <= -min(x1.ndim, x2.ndim), axis or -min(x1.ndim, x2.ndim), axis < max(x1.ndim, x2.ndim):
        pass
    
    raise ValueError(f'''axis {axis} out of bounds for cross product of arrays with shapes {x1.shape} and {x2.shape}''')
    if not  == x1.shape[axis], x2.shape[axis] or x1.shape[axis], x2.shape[axis] == 3:
        pass
    
    raise ValueError(f'''cross product axis must have size 3, got {x1.shape[axis]} and {x2.shape[axis]}''')
    (x1, x2) = torch.broadcast_tensors(x1, x2)
    return torch_linalg.cross(x1, x2, dim = axis)


def vecdot(x1 = None, x2 = None, *, axis, **kwargs):
    isdtype = isdtype
    import _aliases
    (x1, x2) = _fix_promotion(x1, x2, only_scalar = False)
    if x1.shape[axis] != x2.shape[axis]:
        raise ValueError('x1 and x2 must have the same size along the given axis')
    if isdtype(x1.dtype, 'integral') or isdtype(x2.dtype, 'integral'):
        if kwargs:
            raise RuntimeError('vecdot kwargs not supported for integral dtypes')
        x1_ = torch.moveaxis(x1, axis, -1)
        x2_ = torch.moveaxis(x2, axis, -1)
        (x1_, x2_) = torch.broadcast_tensors(x1_, x2_)
        res = x1_[(..., None, :)] @ x2_[(..., None)]
        return res[(..., 0, 0)]
# WARNING: Decompyle incomplete


def solve(x1 = None, x2 = None, **kwargs):
    (x1, x2) = _fix_promotion(x1, x2, only_scalar = False)
    if x2.ndim != 1 and x1.ndim - 1 == x2.ndim and x1.shape[:-1] == x2.shape:
        x2 = x2[None]
# WARNING: Decompyle incomplete


def trace(x = None, *, offset, dtype):
    return sum(torch.diagonal(x, offset = offset, dim1 = -2, dim2 = -1), axis = -1, dtype = dtype)


def vector_norm(x = None, *, axis, keepdims, ord, **kwargs):
    pass
# WARNING: Decompyle incomplete

__all__ = linalg_all + [
    'outer',
    'matmul',
    'matrix_transpose',
    'tensordot',
    'cross',
    'vecdot',
    'solve',
    'trace',
    'vector_norm']
_all_ignore = [
    'torch_linalg',
    'sum']
del linalg_all

def __dir__():
    return __all__
