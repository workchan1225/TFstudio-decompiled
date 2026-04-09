# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: min_max_.pyc (Python 3.11)

'''
Numba 1D min/max kernels that can be shared by
* Dataframe / Series
* groupby
* rolling / expanding

Mirrors pandas/_libs/window/aggregation.pyx
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import numba
import numpy as np
if TYPE_CHECKING:
    from pandas._typing import npt
bisect_left = (lambda a = None, x = None, lo = numba.njit(nogil = True, parallel = False), hi = (0, -1): if hi == -1:
hi = len(a)# WARNING: Decompyle incomplete
)()
sliding_min_max = (lambda values, result_dtype, start = None, end = None, min_periods = numba.jit(nopython = True, nogil = True, parallel = False), is_max = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'start', 'np.ndarray', 'end', 'np.ndarray', 'min_periods', 'int', 'is_max', 'bool', 'return', 'tuple[np.ndarray, list[int]]'): N = len(start)na_pos = []output = np.empty(N, dtype = result_dtype)
def cmp(a = None, b = None, is_max = None):
if is_max:
a >= bNone <= bcandidates = []dominators = []if min_periods < 1:
min_periods = 1# WARNING: Decompyle incomplete
)()
grouped_min_max = (lambda values, result_dtype, labels = None, ngroups = None, min_periods = numba.jit(nopython = True, nogil = True, parallel = False), is_max = (True,), skipna = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'labels', 'npt.NDArray[np.intp]', 'ngroups', 'int', 'min_periods', 'int', 'is_max', 'bool', 'skipna', 'bool', 'return', 'tuple[np.ndarray, list[int]]'): N = len(labels)nobs = np.zeros(ngroups, dtype = np.int64)na_pos = []output = np.empty(ngroups, dtype = result_dtype)for i in range(N):
lab = labels[i]val = values[i]if (lab < 0 or skipna) and nobs[lab] >= 1 and np.isnan(output[lab]):
continueif not values.dtype.kind == 'i' or np.isnan(val):
passelif not skipna:
np.nan = Noneif nobs[lab] == 1:
output[lab] = valcontinueif is_max:
if val > output[lab]:
output[lab] = valcontinueif val < output[lab]:
output[lab] = valfor lab, count in enumerate(nobs):
if count < min_periods:
na_pos.append(lab)(output, na_pos))()
