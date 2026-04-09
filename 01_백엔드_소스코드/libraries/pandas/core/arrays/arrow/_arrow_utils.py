# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _arrow_utils.pyc (Python 3.11)

from __future__ import annotations
import numpy as np
import pyarrow

def pyarrow_array_to_numpy_and_mask(arr = None, dtype = None):
    '''
    Convert a primitive pyarrow.Array to a numpy array and boolean mask based
    on the buffers of the Array.

    At the moment pyarrow.BooleanArray is not supported.

    Parameters
    ----------
    arr : pyarrow.Array
    dtype : numpy.dtype

    Returns
    -------
    (data, mask)
        Tuple of two numpy arrays with the raw data (with specified dtype) and
        a boolean mask (validity mask, so False means missing)
    '''
    dtype = np.dtype(dtype)
    if pyarrow.types.is_null(arr.type):
        data = np.empty(len(arr), dtype = dtype)
        mask = np.zeros(len(arr), dtype = bool)
        return (data, mask)
    buflist = None.buffers()
    offset = arr.offset * dtype.itemsize
    length = len(arr) * dtype.itemsize
    data_buf = buflist[1][offset:offset + length]
    data = np.frombuffer(data_buf, dtype = dtype)
    bitmask = buflist[0]
# WARNING: Decompyle incomplete
