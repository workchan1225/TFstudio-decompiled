# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: var_.pyc (Python 3.11)

'''
Numba 1D var kernels that can be shared by
* Dataframe / Series
* groupby
* rolling / expanding

Mirrors pandas/_libs/window/aggregation.pyx
'''
from __future__ import annotations
from typing import TYPE_CHECKING
import numba
import numpy as np
if TYPE_CHECKING:
    from pandas._typing import npt
from pandas.core._numba.kernels.shared import is_monotonic_increasing
add_var = (lambda val, nobs, mean_x, ssqdm_x = None, compensation = None, num_consecutive_same_value = numba.jit(nopython = True, nogil = True, parallel = False), prev_value = ('val', 'float', 'nobs', 'int', 'mean_x', 'float', 'ssqdm_x', 'float', 'compensation', 'float', 'num_consecutive_same_value', 'int', 'prev_value', 'float', 'return', 'tuple[int, float, float, float, int, float]'): if not np.isnan(val):
if val == prev_value:
num_consecutive_same_value += 1else:
num_consecutive_same_value = 1prev_value = valnobs += 1prev_mean = mean_x - compensationy = val - compensationt = y - mean_xcompensation = t + mean_x - ydelta = tif nobs:
mean_x += delta / nobselse:
mean_x = 0ssqdm_x += (val - prev_mean) * (val - mean_x)(nobs, mean_x, ssqdm_x, compensation, num_consecutive_same_value, prev_value))()
remove_var = (lambda val, nobs = None, mean_x = None, ssqdm_x = numba.jit(nopython = True, nogil = True, parallel = False), compensation = ('val', 'float', 'nobs', 'int', 'mean_x', 'float', 'ssqdm_x', 'float', 'compensation', 'float', 'return', 'tuple[int, float, float, float]'): if not np.isnan(val):
nobs -= 1if nobs:
prev_mean = mean_x - compensationy = val - compensationt = y - mean_xcompensation = t + mean_x - ydelta = tmean_x -= delta / nobsssqdm_x -= (val - prev_mean) * (val - mean_x)else:
mean_x = 0ssqdm_x = 0(nobs, mean_x, ssqdm_x, compensation))()
sliding_var = (lambda values, result_dtype = None, start = None, end = numba.jit(nopython = True, nogil = True, parallel = False), min_periods = (1,), ddof = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'start', 'np.ndarray', 'end', 'np.ndarray', 'min_periods', 'int', 'ddof', 'int', 'return', 'tuple[np.ndarray, list[int]]'): N = len(start)nobs = 0mean_x = 0ssqdm_x = 0compensation_add = 0compensation_remove = 0min_periods = max(min_periods, 1)if is_monotonic_increasing(start):
is_monotonic_increasing_bounds = is_monotonic_increasing(end)output = np.empty(N, dtype = result_dtype)for i in range(N):
s = start[i]e = end[i]if not i == 0 or is_monotonic_increasing_bounds:
prev_value = values[s]num_consecutive_same_value = 0for j in range(s, e):
val = values[j](nobs, mean_x, ssqdm_x, compensation_add, num_consecutive_same_value, prev_value) = add_var(val, nobs, mean_x, ssqdm_x, compensation_add, num_consecutive_same_value, prev_value)for j in range(start[i - 1], s):
val = values[j](nobs, mean_x, ssqdm_x, compensation_remove) = remove_var(val, nobs, mean_x, ssqdm_x, compensation_remove)for j in range(end[i - 1], e):
val = values[j](nobs, mean_x, ssqdm_x, compensation_add, num_consecutive_same_value, prev_value) = add_var(val, nobs, mean_x, ssqdm_x, compensation_add, num_consecutive_same_value, prev_value)if nobs >= min_periods and nobs > ddof:
if nobs == 1 or num_consecutive_same_value >= nobs:
result = 0else:
result = ssqdm_x / (nobs - ddof)else:
result = np.nanoutput[i] = resultif not is_monotonic_increasing_bounds:
nobs = 0mean_x = 0ssqdm_x = 0compensation_remove = 0na_pos = range(0)()(output, na_pos))()
grouped_var = (lambda values, result_dtype, labels = None, ngroups = None, min_periods = numba.jit(nopython = True, nogil = True, parallel = False), ddof = (1, True), skipna = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'labels', 'npt.NDArray[np.intp]', 'ngroups', 'int', 'min_periods', 'int', 'ddof', 'int', 'skipna', 'bool', 'return', 'tuple[np.ndarray, list[int]]'): N = len(labels)nobs_arr = np.zeros(ngroups, dtype = np.int64)comp_arr = np.zeros(ngroups, dtype = values.dtype)consecutive_counts = np.zeros(ngroups, dtype = np.int64)prev_vals = np.zeros(ngroups, dtype = values.dtype)output = np.zeros(ngroups, dtype = result_dtype)means = np.zeros(ngroups, dtype = result_dtype)for i in range(N):
lab = labels[i]val = values[i]if lab < 0 or np.isnan(output[lab]):
continueif skipna and np.isnan(val):
output[lab] = np.nancontinuemean_x = means[lab]ssqdm_x = output[lab]nobs = nobs_arr[lab]compensation_add = comp_arr[lab]num_consecutive_same_value = consecutive_counts[lab]prev_value = prev_vals[lab](nobs, mean_x, ssqdm_x, compensation_add, num_consecutive_same_value, prev_value) = add_var(val, nobs, mean_x, ssqdm_x, compensation_add, num_consecutive_same_value, prev_value)output[lab] = ssqdm_xmeans[lab] = mean_xconsecutive_counts[lab] = num_consecutive_same_valueprev_vals[lab] = prev_valuecomp_arr[lab] = compensation_addnobs_arr[lab] = nobsfor lab in range(ngroups):
nobs = nobs_arr[lab]num_consecutive_same_value = consecutive_counts[lab]ssqdm_x = output[lab]if nobs >= min_periods and nobs > ddof:
if nobs == 1 or num_consecutive_same_value >= nobs:
result = 0else:
result = ssqdm_x / (nobs - ddof)else:
result = np.nanoutput[lab] = resultna_pos = range(0)()(output, na_pos))()
