# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: transpose.pyc (Python 3.11)

from numba import cuda
from numba.cuda.cudadrv.driver import driver
import math
from numba.np import numpy_support as nps

def transpose(a, b = (None,)):
    """Compute the transpose of 'a' and store it into 'b', if given,
    and return it. If 'b' is not given, allocate a new array
    and return that.

    This implements the algorithm documented in
    http://devblogs.nvidia.com/parallelforall/efficient-matrix-transpose-cuda-cc/

    :param a: an `np.ndarray` or a `DeviceNDArrayBase` subclass. If already on
        the device its stream will be used to perform the transpose (and to copy
        `b` to the device if necessary).
    """
    pass
# WARNING: Decompyle incomplete
