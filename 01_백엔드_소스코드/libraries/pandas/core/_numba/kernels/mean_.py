# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mean_.pyc (Python 3.11)

'''
Numba 1D mean kernels that can be shared by
* Dataframe / Series
* groupby
* rolling / expanding

Mirrors pandas/_libs/window/aggregation.pyx
'''
from __future__ import annotations
from typing import TYPE_CHECKING
import numba
import numpy as np
from pandas.core._numba.kernels.shared import is_monotonic_increasing
from pandas.core._numba.kernels.sum_ import grouped_kahan_sum
if TYPE_CHECKING:
    from pandas._typing import npt
add_mean = (lambda val, nobs, sum_x, neg_ct = None, compensation = None, num_consecutive_same_value = numba.jit(nopython = True, nogil = True, parallel = False), prev_value = ('val', 'float', 'nobs', 'int', 'sum_x', 'float', 'neg_ct', 'int', 'compensation', 'float', 'num_consecutive_same_value', 'int', 'prev_value', 'float', 'return', 'tuple[int, float, int, float, int, float]'): if not np.isnan(val):
nobs += 1y = val - compensationt = sum_x + ycompensation = t - sum_x - ysum_x = tif val < 0:
neg_ct += 1if val == prev_value:
num_consecutive_same_value += 1else:
num_consecutive_same_value = 1prev_value = val(nobs, sum_x, neg_ct, compensation, num_consecutive_same_value, prev_value))()
remove_mean = (lambda val, nobs = None, sum_x = None, neg_ct = numba.jit(nopython = True, nogil = True, parallel = False), compensation = ('val', 'float', 'nobs', 'int', 'sum_x', 'float', 'neg_ct', 'int', 'compensation', 'float', 'return', 'tuple[int, float, int, float]'): if not np.isnan(val):
nobs -= 1y = -val - compensationt = sum_x + ycompensation = t - sum_x - ysum_x = tif val < 0:
neg_ct -= 1(nobs, sum_x, neg_ct, compensation))()
sliding_mean = (lambda values, result_dtype = None, start = None, end = numba.jit(nopython = True, nogil = True, parallel = False), min_periods = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'start', 'np.ndarray', 'end', 'np.ndarray', 'min_periods', 'int', 'return', 'tuple[np.ndarray, list[int]]'): N = len(start)nobs = 0sum_x = 0neg_ct = 0compensation_add = 0compensation_remove = 0if is_monotonic_increasing(start):
is_monotonic_increasing_bounds = is_monotonic_increasing(end)output = np.empty(N, dtype = result_dtype)for i in range(N):
s = start[i]e = end[i]if not i == 0 or is_monotonic_increasing_bounds:
prev_value = values[s]num_consecutive_same_value = 0for j in range(s, e):
val = values[j](nobs, sum_x, neg_ct, compensation_add, num_consecutive_same_value, prev_value) = add_mean(val, nobs, sum_x, neg_ct, compensation_add, num_consecutive_same_value, prev_value)for j in range(start[i - 1], s):
val = values[j](nobs, sum_x, neg_ct, compensation_remove) = remove_mean(val, nobs, sum_x, neg_ct, compensation_remove)for j in range(end[i - 1], e):
val = values[j](nobs, sum_x, neg_ct, compensation_add, num_consecutive_same_value, prev_value) = add_mean(val, nobs, sum_x, neg_ct, compensation_add, num_consecutive_same_value, prev_value)if nobs >= min_periods and nobs > 0:
result = sum_x / nobsif num_consecutive_same_value >= nobs:
result = prev_valueelif neg_ct == 0 and result < 0:
result = 0elif neg_ct == nobs and result > 0:
result = 0else:
result = np.nanoutput[i] = resultif not is_monotonic_increasing_bounds:
nobs = 0sum_x = 0neg_ct = 0compensation_remove = 0na_pos = range(0)()(output, na_pos))()
grouped_mean = (lambda values, result_dtype, labels = None, ngroups = None, min_periods = numba.jit(nopython = True, nogil = True, parallel = False), skipna = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'labels', 'npt.NDArray[np.intp]', 'ngroups', 'int', 'min_periods', 'int', 'skipna', 'bool', 'return', 'tuple[np.ndarray, list[int]]'): (output, nobs_arr, comp_arr, consecutive_counts, prev_vals) = grouped_kahan_sum(values, result_dtype, labels, ngroups, skipna)for lab in range(ngroups):
nobs = nobs_arr[lab]num_consecutive_same_value = consecutive_counts[lab]prev_value = prev_vals[lab]sum_x = output[lab]if nobs >= min_periods:
if num_consecutive_same_value >= nobs:
result = prev_value * nobselse:
result = sum_xelse:
result = np.nanresult /= nobsoutput[lab] = resultna_pos = range(0)()(output, na_pos))()
