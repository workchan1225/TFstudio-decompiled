# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: linalg.pyc (Python 3.11)

from __future__ import annotations
from typing import Literal
from dask.array import array as da
from dask.array import matmul, outer, tensordot
from dask.array.linalg import *
from _internal import get_xp
from common import _linalg
from common._typing import Array as _Array
from _aliases import matrix_transpose, vecdot
_n = { }
exec('from dask.array.linalg import *', _n)
for k in ('__builtins__', 'annotations', 'operator', 'warnings', 'Array'):
    _n.pop(k, None)
    linalg_all = list(_n)
    del _n
    del k
    EighResult = _linalg.EighResult
    QRResult = _linalg.QRResult
    SlogdetResult = _linalg.SlogdetResult
    SVDResult = _linalg.SVDResult
    
    def qr(x = None, mode = None, **kwargs):
        if mode != 'reduced':
            raise ValueError("dask arrays only support using mode='reduced'")
    # WARNING: Decompyle incomplete

    trace = get_xp(da)(_linalg.trace)
    cholesky = get_xp(da)(_linalg.cholesky)
    matrix_rank = get_xp(da)(_linalg.matrix_rank)
    matrix_norm = get_xp(da)(_linalg.matrix_norm)
    
    def svd(x = None, full_matrices = None, **kwargs):
        if full_matrices:
            raise ValueError('full_matrics=True is not supported by dask.')
    # WARNING: Decompyle incomplete

    
    def svdvals(x = None):
        (_, s, _) = svd(x)
        return s

    vector_norm = get_xp(da)(_linalg.vector_norm)
    diagonal = get_xp(da)(_linalg.diagonal)
    __all__ = linalg_all + [
        'trace',
        'outer',
        'matmul',
        'tensordot',
        'matrix_transpose',
        'vecdot',
        'EighResult',
        'QRResult',
        'SlogdetResult',
        'SVDResult',
        'qr',
        'cholesky',
        'matrix_rank',
        'matrix_norm',
        'svdvals',
        'vector_norm',
        'diagonal']
    _all_ignore = [
        'get_xp',
        'da',
        'linalg_all',
        'warnings']
    return None
