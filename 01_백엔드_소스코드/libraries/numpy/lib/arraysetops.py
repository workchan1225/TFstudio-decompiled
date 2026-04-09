# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: arraysetops.pyc (Python 3.11)

'''
Set operations for arrays based on sorting.

Notes
-----

For floating point arrays, inaccurate results may appear due to usual round-off
and floating point comparison issues.

Speed could be gained in some operations by an implementation of
`numpy.sort`, that can provide directly the permutation vectors, thus avoiding
calls to `numpy.argsort`.

Original author: Robert Cimrman

'''
import functools
import numpy as np
from numpy.core import overrides
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
__all__ = [
    'ediff1d',
    'intersect1d',
    'setxor1d',
    'union1d',
    'setdiff1d',
    'unique',
    'in1d',
    'isin']

def _ediff1d_dispatcher(ary, to_end, to_begin = (None, None)):
    return (ary, to_end, to_begin)

ediff1d = (lambda ary, to_end, to_begin = (None, None): ary = np.asanyarray(ary).ravel()dtype_req = ary.dtype# WARNING: Decompyle incomplete
)()

def _unpack_tuple(x):
    ''' Unpacks one-element tuples for use as return values '''
    if len(x) == 1:
        return x[0]


def _unique_dispatcher(ar, return_index, return_inverse = array_function_dispatch(_ediff1d_dispatcher), return_counts = (None, None, None, None), axis = {
    'equal_nan': None }, *, equal_nan):
    return (ar,)

unique = (lambda ar, return_index, return_inverse = array_function_dispatch(_unique_dispatcher), return_counts = (False, False, False, None), axis = {
    'equal_nan': True }, *, equal_nan, ret = None, dtype = None, consolidated = None, e = None: pass# WARNING: Decompyle incomplete
)()

def _unique1d(ar, return_index = None, return_inverse = (False, False, False), return_counts = {
    'equal_nan': True }, *, equal_nan):
    '''
    Find the unique elements of an array, ignoring shape.
    '''
    ar = np.asanyarray(ar).flatten()
    if not return_index:
        optional_indices = return_inverse
        if optional_indices:
            perm = ar.argsort(kind = 'mergesort' if return_index else 'quicksort')
            aux = ar[perm]
        else:
            ar.sort()
            aux = ar
    mask = np.empty(aux.shape, dtype = np.bool_)
    mask[:1] = True
    if equal_nan and aux.shape[0] > 0 and aux.dtype.kind in 'cfmM' and np.isnan(aux[-1]):
        if aux.dtype.kind == 'c':
            aux_firstnan = np.searchsorted(np.isnan(aux), True, side = 'left')
        else:
            aux_firstnan = np.searchsorted(aux, aux[-1], side = 'left')
        if aux_firstnan > 0:
            mask[1:aux_firstnan] = aux[1:aux_firstnan] != aux[:aux_firstnan - 1]
        mask[aux_firstnan] = True
        mask[aux_firstnan + 1:] = False
    else:
        mask[1:] = aux[1:] != aux[:-1]
    ret = (aux[mask],)
    if return_index:
        ret += (perm[mask],)
    if return_inverse:
        imask = np.cumsum(mask) - 1
        inv_idx = np.empty(mask.shape, dtype = np.intp)
        inv_idx[perm] = imask
        ret += (inv_idx,)
    if return_counts:
        idx = np.concatenate(np.nonzero(mask) + ([
            mask.size],))
        ret += (np.diff(idx),)
    return ret


def _intersect1d_dispatcher(ar1, ar2, assume_unique, return_indices = (None, None)):
    return (ar1, ar2)

intersect1d = (lambda ar1, ar2, assume_unique, return_indices = (False, False): ar1 = np.asanyarray(ar1)ar2 = np.asanyarray(ar2)if not assume_unique:
if return_indices:
(ar1, ind1) = unique(ar1, return_index = True)(ar2, ind2) = unique(ar2, return_index = True)else:
ar1 = unique(ar1)ar2 = unique(ar2)else:
ar1 = ar1.ravel()ar2 = ar2.ravel()aux = np.concatenate((ar1, ar2))if return_indices:
aux_sort_indices = np.argsort(aux, kind = 'mergesort')aux = aux[aux_sort_indices]else:
aux.sort()mask = aux[1:] == aux[:-1]int1d = aux[:-1][mask]if return_indices:
ar1_indices = aux_sort_indices[:-1][mask]ar2_indices = aux_sort_indices[1:][mask] - ar1.sizeif not assume_unique:
ar1_indices = ind1[ar1_indices]ar2_indices = ind2[ar2_indices](int1d, ar1_indices, ar2_indices))()

def _setxor1d_dispatcher(ar1, ar2, assume_unique = (None,)):
    return (ar1, ar2)

setxor1d = (lambda ar1, ar2, assume_unique = (False,): if not assume_unique:
ar1 = unique(ar1)ar2 = unique(ar2)aux = np.concatenate((ar1, ar2))if aux.size == 0:
auxNone.sort()flag = np.concatenate(([
True], aux[1:] != aux[:-1], [
True]))aux[flag[1:] & flag[:-1]])()

def _in1d_dispatcher(ar1, ar2 = array_function_dispatch(_setxor1d_dispatcher), assume_unique = (None, None), invert = {
    'kind': None }, *, kind):
    return (ar1, ar2)

in1d = (lambda ar1, ar2 = array_function_dispatch(_in1d_dispatcher), assume_unique = (False, False), invert = {
    'kind': None }, *, kind, is_int_arrays = None, use_table_method = None, ar2_min = None: ar1 = np.asarray(ar1).ravel()ar2 = np.asarray(ar2).ravel()if ar2.dtype == object:
ar2 = ar2.reshape(-1, 1)if kind not in frozenset({None, 'sort', 'table'}):
raise ValueError(f'''Invalid kind: \'{kind}\'. Please use None, \'sort\' or \'table\'.''')is_int_arrays = (lambda .0: pass# WARNING: Decompyle incomplete
)((ar1, ar2)())
    if is_int_arrays:
        use_table_method = kind in frozenset({None, 'table'})
        if use_table_method:
            if ar2.size == 0:
                if invert:
                    return np.ones_like(ar1, dtype = bool)
                return all.zeros_like(ar1, dtype = bool)
            if all.dtype == bool:
                ar1 = ar1.astype(np.uint8)
            if ar2.dtype == bool:
                ar2 = ar2.astype(np.uint8)
            ar2_min = np.min(ar2)
            ar2_max = np.max(ar2)
            ar2_range = int(ar2_max) - int(ar2_min)
            below_memory_constraint = ar2_range <= 6 * (ar1.size + ar2.size)
            range_safe_from_overflow = ar2_range <= np.iinfo(ar2.dtype).max
            if ar1.size > 0:
                ar1_min = np.min(ar1)
                ar1_max = np.max(ar1)
                ar1_upper = min(int(ar1_max), int(ar2_max))
                ar1_lower = max(int(ar1_min), int(ar2_min))
                range_safe_from_overflow &= all((ar1_upper - int(ar2_min) <= np.iinfo(ar1.dtype).max, ar1_lower - int(ar2_min) >= np.iinfo(ar1.dtype).min))
            if range_safe_from_overflow:
                if below_memory_constraint or kind == 'table':
                    if invert:
                        outgoing_array = np.ones_like(ar1, dtype = bool)
                    else:
                        outgoing_array = np.zeros_like(ar1, dtype = bool)
                    if invert:
                        isin_helper_ar = np.ones(ar2_range + 1, dtype = bool)
                        isin_helper_ar[ar2 - ar2_min] = 0
                    else:
                        isin_helper_ar = np.zeros(ar2_range + 1, dtype = bool)
                        isin_helper_ar[ar2 - ar2_min] = 1
                    basic_mask = (ar1 <= ar2_max) & (ar1 >= ar2_min)
                    outgoing_array[basic_mask] = isin_helper_ar[ar1[basic_mask] - ar2_min]
                    return outgoing_array
                if None == 'table':
                    raise RuntimeError("You have specified kind='table', but the range of values in `ar2` or `ar1` exceed the maximum integer of the datatype. Please set `kind` to None or 'sort'.")
            elif kind == 'table':
                raise ValueError("The 'table' method is only supported for boolean or integer arrays. Please select 'sort' or None for kind.")
    if not ar1.dtype.hasobject:
        contains_object = ar2.dtype.hasobject
        if len(ar2) < 10 * len(ar1) ** 0.145 or contains_object:
            if invert:
                mask = np.ones(len(ar1), dtype = bool)
                for a in ar2:
                    mask &= (ar1 != a)
            mask = np.zeros(len(ar1), dtype = bool)
            for a in ar2:
                mask |= (ar1 == a)
                return mask
                if not assume_unique:
                    (ar1, rev_idx) = np.unique(ar1, return_inverse = True)
                    ar2 = np.unique(ar2)
    ar = np.concatenate((ar1, ar2))
    order = ar.argsort(kind = 'mergesort')
    sar = ar[order]
    if invert:
        bool_ar = sar[1:] != sar[:-1]
    else:
        bool_ar = sar[1:] == sar[:-1]
    flag = np.concatenate((bool_ar, [
        invert]))
    ret = np.empty(ar.shape, dtype = bool)
    ret[order] = flag
    if assume_unique:
        return ret[:len(ar1)]
    return None[rev_idx]
)()

def _isin_dispatcher(element, test_elements = array_function_dispatch(_intersect1d_dispatcher), assume_unique = (None, None), invert = {
    'kind': None }, *, kind):
    return (element, test_elements)

isin = (lambda element, test_elements = array_function_dispatch(_isin_dispatcher), assume_unique = (False, False), invert = {
    'kind': None }, *, kind,
