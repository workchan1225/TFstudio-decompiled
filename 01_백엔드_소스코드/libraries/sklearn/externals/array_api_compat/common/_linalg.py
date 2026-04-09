# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _linalg.pyc (Python 3.11)

from __future__ import annotations
import math
from typing import Literal, NamedTuple, cast
import numpy as np
if np.__version__[0] == '2':
    from numpy.lib.array_utils import normalize_axis_tuple
else:
    from numpy.core.numeric import normalize_axis_tuple
from _internal import get_xp
from _aliases import isdtype, matmul, matrix_transpose, tensordot, vecdot
from _typing import Array, DType, JustFloat, JustInt, Namespace

def cross(x1 = None, x2 = None, xp = None, *, axis, **kwargs):
    pass
# WARNING: Decompyle incomplete


def outer(x1 = None, x2 = None, xp = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


class EighResult(NamedTuple):
    eigenvectors: 'Array' = 'EighResult'


class QRResult(NamedTuple):
    R: 'Array' = 'QRResult'


class SlogdetResult(NamedTuple):
    logabsdet: 'Array' = 'SlogdetResult'


class SVDResult(NamedTuple):
    Vh: 'Array' = 'SVDResult'


def eigh(x = None, xp = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def qr(x = None, xp = None, *, mode, **kwargs):
    pass
# WARNING: Decompyle incomplete


def slogdet(x = None, xp = None, **kwargs):
    pass
# WARNING: Decompyle incomplete


def svd(x = None, xp = None, *, full_matrices, **kwargs):
    pass
# WARNING: Decompyle incomplete


def cholesky(x = None, xp = None, *, upper, **kwargs):
    pass
# WARNING: Decompyle incomplete


def matrix_rank(x = None, xp = None, *, rtol, **kwargs):
    if x.ndim < 2:
        raise xp.linalg.LinAlgError('1-dimensional array given. Array must be at least two-dimensional')
# WARNING: Decompyle incomplete


def pinv(x = None, xp = None, *, rtol, **kwargs):
    pass
# WARNING: Decompyle incomplete


def matrix_norm(x = None, xp = None, *, keepdims, ord):
    return xp.linalg.norm(x, axis = (-2, -1), keepdims = keepdims, ord = ord)


def svdvals(x = None, xp = None):
    return xp.linalg.svd(x, compute_uv = False)


def vector_norm(x = None, xp = None, *, axis, keepdims, ord):
    pass
# WARNING: Decompyle incomplete


def diagonal(x = None, xp = None, *, offset, **kwargs):
    pass
# WARNING: Decompyle incomplete


def trace(x = None, xp = None, *, offset, dtype, **kwargs):
    pass
# WARNING: Decompyle incomplete

__all__ = [
    'cross',
    'matmul',
    'outer',
    'tensordot',
    'EighResult',
    'QRResult',
    'SlogdetResult',
    'SVDResult',
    'eigh',
    'qr',
    'slogdet',
    'svd',
    'cholesky',
    'matrix_rank',
    'pinv',
    'matrix_norm',
    'matrix_transpose',
    'svdvals',
    'vecdot',
    'vector_norm',
    'diagonal',
    'trace']
_all_ignore = [
    'math',
    'normalize_axis_tuple',
    'get_xp',
    'np',
    'isdtype']

def __dir__():
    return __all__
