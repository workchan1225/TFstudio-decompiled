# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: api_util.pyc (Python 3.11)

import numpy as np

def prepare_shape_strides_dtype(shape, strides, dtype, order):
    dtype = np.dtype(dtype)
    if isinstance(shape, int):
        shape = (shape,)
    if isinstance(strides, int):
        strides = (strides,)
    elif not strides:
        strides = _fill_stride_by_order(shape, dtype, order)
        return (shape, strides, dtype)


def _fill_stride_by_order(shape, dtype, order):
    nd = len(shape)
    if nd == 0:
        return ()
    strides = [
        None] * nd
    if order == 'C':
        strides[-1] = dtype.itemsize
        for d in reversed(range(nd - 1)):
            strides[d] = strides[d + 1] * shape[d + 1]
    if order == 'F':
        strides[0] = dtype.itemsize
        for d in range(1, nd):
            strides[d] = strides[d - 1] * shape[d - 1]
    raise ValueError('must be either C/F order')
    return tuple(strides)
