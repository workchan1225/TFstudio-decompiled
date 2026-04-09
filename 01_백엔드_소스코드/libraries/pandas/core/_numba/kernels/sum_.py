# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sum_.pyc (Python 3.11)

'''
Numba 1D sum kernels that can be shared by
* Dataframe / Series
* groupby
* rolling / expanding

Mirrors pandas/_libs/window/aggregation.pyx
'''
from __future__ import annotations
from typing import TYPE_CHECKING, Any
import numba
from numba.extending import register_jitable
import numpy as np
if TYPE_CHECKING:
    from pandas._typing import npt
from pandas.core._numba.kernels.shared import is_monotonic_increasing
add_sum = (lambda val, nobs, sum_x = None, compensation = None, num_consecutive_same_value = numba.jit(nopython = True, nogil = True, parallel = False), prev_value = ('val', 'Any', 'nobs', 'int', 'sum_x', 'Any', 'compensation', 'Any', 'num_consecutive_same_value', 'int', 'prev_value', 'Any', 'return', 'tuple[int, Any, Any, int, Any]'): if not np.isnan(val):
nobs += 1y = val - compensationt = sum_x + ycompensation = t - sum_x - ysum_x = tif val == prev_value:
num_consecutive_same_value += 1else:
num_consecutive_same_value = 1prev_value = val(nobs, sum_x, compensation, num_consecutive_same_value, prev_value))()
remove_sum = (lambda val = None, nobs = None, sum_x = numba.jit(nopython = True, nogil = True, parallel = False), compensation = ('val', 'Any', 'nobs', 'int', 'sum_x', 'Any', 'compensation', 'Any', 'return', 'tuple[int, Any, Any]'): if not np.isnan(val):
nobs -= 1y = -val - compensationt = sum_x + ycompensation = t - sum_x - ysum_x = t(nobs, sum_x, compensation))()
sliding_sum = (lambda values, result_dtype = None, start = None, end = numba.jit(nopython = True, nogil = True, parallel = False), min_periods = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'start', 'np.ndarray', 'end', 'np.ndarray', 'min_periods', 'int', 'return', 'tuple[np.ndarray, list[int]]'): dtype = values.dtypena_val = np.nanif dtype.kind == 'i':
na_val = 0N = len(start)nobs = 0sum_x = 0compensation_add = 0compensation_remove = 0na_pos = []if is_monotonic_increasing(start):
is_monotonic_increasing_bounds = is_monotonic_increasing(end)output = np.empty(N, dtype = result_dtype)for i in range(N):
s = start[i]e = end[i]if not i == 0 or is_monotonic_increasing_bounds:
prev_value = values[s]num_consecutive_same_value = 0for j in range(s, e):
val = values[j](nobs, sum_x, compensation_add, num_consecutive_same_value, prev_value) = add_sum(val, nobs, sum_x, compensation_add, num_consecutive_same_value, prev_value)for j in range(start[i - 1], s):
val = values[j](nobs, sum_x, compensation_remove) = remove_sum(val, nobs, sum_x, compensation_remove)for j in range(end[i - 1], e):
val = values[j](nobs, sum_x, compensation_add, num_consecutive_same_value, prev_value) = add_sum(val, nobs, sum_x, compensation_add, num_consecutive_same_value, prev_value)if  == nobs, 0 or nobs, 0 == min_periods:
passoutput[i] = resultif not is_monotonic_increasing_bounds:
nobs = 0sum_x = 0compensation_remove = 0(output, na_pos))()
grouped_kahan_sum = (lambda values, result_dtype = None, labels = None, ngroups = register_jitable, skipna = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'labels', 'npt.NDArray[np.intp]', 'ngroups', 'int', 'skipna', 'bool', 'return', 'tuple[np.ndarray, npt.NDArray[np.int64], np.ndarray, npt.NDArray[np.int64], np.ndarray]'): N = len(labels)nobs_arr = np.zeros(ngroups, dtype = np.int64)comp_arr = np.zeros(ngroups, dtype = values.dtype)consecutive_counts = np.zeros(ngroups, dtype = np.int64)prev_vals = np.zeros(ngroups, dtype = values.dtype)output = np.zeros(ngroups, dtype = result_dtype)for i in range(N):
lab = labels[i]val = values[i]if lab < 0 or np.isnan(output[lab]):
continueif skipna and np.isnan(val):
output[lab] = np.nannp.nan = Noneconsecutive_counts[lab] = 1prev_vals[lab] = np.nancontinuesum_x = output[lab]nobs = nobs_arr[lab]compensation_add = comp_arr[lab]num_consecutive_same_value = consecutive_counts[lab]prev_value = prev_vals[lab](nobs, sum_x, compensation_add, num_consecutive_same_value, prev_value) = add_sum(val, nobs, sum_x, compensation_add, num_consecutive_same_value, prev_value)output[lab] = sum_xconsecutive_counts[lab] = num_consecutive_same_valueprev_vals[lab] = prev_valuecomp_arr[lab] = compensation_addnobs_arr[lab] = nobs(output, nobs_arr, comp_arr, consecutive_counts, prev_vals))()
grouped_sum = (lambda values, result_dtype, labels = None, ngroups = None, min_periods = numba.jit(nopython = True, nogil = True, parallel = False), skipna = ('values', 'np.ndarray', 'result_dtype', 'np.dtype', 'labels', 'npt.NDArray[np.intp]', 'ngroups', 'int', 'min_periods', 'int', 'skipna', 'bool', 'return', 'tuple[np.ndarray, list[int]]'): na_pos = [](output, nobs_arr, comp_arr, consecutive_counts, prev_vals) = grouped_kahan_sum(values, result_dtype, labels, ngroups, skipna)for lab in range(ngroups):
nobs = nobs_arr[lab]num_consecutive_same_value = consecutive_counts[lab]prev_value = prev_vals[lab]sum_x = output[lab]if nobs >= min_periods:
if num_consecutive_same_value >= nobs:
result = prev_value * nobselse:
result = sum_xelse:
result = sum_xna_pos.append(lab)output[lab] = result(output, na_pos))()
