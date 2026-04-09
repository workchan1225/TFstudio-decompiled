# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _encode.pyc (Python 3.11)

from collections import Counter
from contextlib import suppress
from typing import NamedTuple
import numpy as np
from sklearn.utils._array_api import _isin, device, get_namespace, xpx
from sklearn.utils._missing import is_scalar_nan

def _unique(values = None, *, return_inverse, return_counts):
    '''Helper function to find unique values with support for python objects.

    Uses pure python method for object dtype, and numpy method for
    all other dtypes.

    Parameters
    ----------
    values : ndarray
        Values to check for unknowns.

    return_inverse : bool, default=False
        If True, also return the indices of the unique values.

    return_counts : bool, default=False
        If True, also return the number of times each unique item appears in
        values.

    Returns
    -------
    unique : ndarray
        The sorted unique values.

    unique_inverse : ndarray
        The indices to reconstruct the original array from the unique array.
        Only provided if `return_inverse` is True.

    unique_counts : ndarray
        The number of times each of the unique values comes up in the original
        array. Only provided if `return_counts` is True.
    '''
    if values.dtype == object:
        return _unique_python(values, return_inverse = return_inverse, return_counts = return_counts)
    return None(values, return_inverse = return_inverse, return_counts = return_counts)


def _unique_np(values, return_inverse, return_counts = (False, False)):
    '''Helper function to find unique values for numpy arrays that correctly
    accounts for nans. See `_unique` documentation for details.'''
    (xp, _) = get_namespace(values)
    (inverse, counts) = (None, None)
    if return_inverse and return_counts:
        (uniques, _, inverse, counts) = xp.unique_all(values)
    elif return_inverse:
        (uniques, inverse) = xp.unique_inverse(values)
    elif return_counts:
        (uniques, counts) = xp.unique_counts(values)
    else:
        uniques = xp.unique_values(values)
    if uniques.size and is_scalar_nan(uniques[-1]):
        nan_idx = xp.searchsorted(uniques, xp.nan)
        uniques = uniques[:nan_idx + 1]
        if return_inverse:
            inverse[inverse > nan_idx] = nan_idx
        if return_counts:
            counts[nan_idx] = xp.sum(counts[nan_idx:])
            counts = counts[:nan_idx + 1]
    ret = (uniques,)
    if return_inverse:
        ret += (inverse,)
    if return_counts:
        ret += (counts,)
    return ret[0] if len(ret) == 1 else ret


class MissingValues(NamedTuple):
    none: bool = 'Data class for missing data information'
    
    def to_list(self):
        '''Convert tuple to a list where None is always first.'''
        output = []
        if self.none:
            output.append(None)
        if self.nan:
            output.append(np.nan)
        return output



def _extract_missing(values):
    '''Extract missing values from `values`.

    Parameters
    ----------
    values: set
        Set of values to extract missing from.

    Returns
    -------
    output: set
        Set with missing values extracted.

    missing_values: MissingValues
        Object with missing value information.
    '''
    missing_values_set = values()
    if not missing_values_set:
        return (values, MissingValues(nan = False, none = False))
    if (lambda .0: pass# WARNING: Decompyle incomplete
) in missing_values_set:
        if len(missing_values_set) == 1:
            output_missing_values = MissingValues(nan = False, none = True)
        else:
            output_missing_values = MissingValues(nan = True, none = True)
    else:
        output_missing_values = MissingValues(nan = True, none = False)
    output = values - missing_values_set
    return (output, output_missing_values)


class _nandict(dict):
    pass
# WARNING: Decompyle incomplete


def _map_to_integer(values, uniques):
    '''Map values based on its position in uniques.'''
    pass
# WARNING: Decompyle incomplete


def _unique_python(values, *, return_inverse, return_counts):
    
    try:
        uniques_set = set(values)
        (uniques_set, missing_values) = _extract_missing(uniques_set)
        uniques = sorted(uniques_set)
        uniques.extend(missing_values.to_list())
        uniques = np.array(uniques, dtype = values.dtype)
    except TypeError:
        types = set((lambda .0: pass# WARNING: Decompyle incomplete
)(values())())
        raise TypeError(f'''Encoders require their input argument must be uniformly strings or numbers. Got {types}''')

    ret = (uniques,)
    if return_inverse:
        ret += (_map_to_integer(values, uniques),)
    if return_counts:
        ret += (_get_counts(values, uniques),)
    return ret[0] if len(ret) == 1 else ret


def _encode(values = None, *, uniques, check_unknown):
    '''Helper function to encode values into [0, n_uniques - 1].

    Uses pure python method for object dtype, and numpy method for
    all other dtypes.
    The numpy method has the limitation that the `uniques` need to
    be sorted. Importantly, this is not checked but assumed to already be
    the case. The calling method needs to ensure this for all non-object
    values.

    Parameters
    ----------
    values : ndarray
        Values to encode.
    uniques : ndarray
        The unique values in `values`. If the dtype is not object, then
        `uniques` needs to be sorted.
    check_unknown : bool, default=True
        If True, check for values in `values` that are not in `unique`
        and raise an error. This is ignored for object dtype, and treated as
        True in this case. This parameter is useful for
        _BaseEncoder._transform() to avoid calling _check_unknown()
        twice.

    Returns
    -------
    encoded : ndarray
        Encoded values
    '''
    (xp, _) = get_namespace(values, uniques)
    if not xp.isdtype(values.dtype, 'numeric'):
        
        try:
            return _map_to_integer(values, uniques)
        except KeyError:
            e = None
            raise ValueError(f'''y contains previously unseen labels: {e}''')
            e = None
            del e
            if check_unknown:
                diff = _check_unknown(values, uniques)
                if diff:
                    raise ValueError(f'''y contains previously unseen labels: {diff}''')
            return xp.searchsorted(uniques, values)



def _check_unknown(values, known_values, return_mask = (False,)):
    '''
    Helper function to check for unknowns in values to be encoded.

    Uses pure python method for object dtype, and numpy method for
    all other dtypes.

    Parameters
    ----------
    values : array
        Values to check for unknowns.
    known_values : array
        Known values. Must be unique.
    return_mask : bool, default=False
        If True, return a mask of the same shape as `values` indicating
        the valid values.

    Returns
    -------
    diff : list
        The unique values present in `values` and not in `know_values`.
    valid_mask : boolean array
        Additionally returned if ``return_mask=True``.

    '''
    pass
# WARNING: Decompyle incomplete


class _NaNCounter(Counter):
    pass
# WARNING: Decompyle incomplete


def _get_counts(values, uniques):
    '''Get the count of each of the `uniques` in `values`.

    The counts will use the order passed in by `uniques`. For non-object dtypes,
    `uniques` is assumed to be sorted and `np.nan` is at the end.
    '''
    if values.dtype.kind in 'OU':
        counter = _NaNCounter(values)
        output = np.zeros(len(uniques), dtype = np.int64)
        for i, item in enumerate(uniques):
            suppress(KeyError)
            output[i] = counter[item]
            None(None, None)
        with None:
            if not None:
                pass
        continue
        return output
    (unique_values, counts) = _unique_np(values, return_counts = True)
    uniques_in_values = np.isin(uniques, unique_values, assume_unique = True)
    if np.isnan(unique_values[-1]) and np.isnan(uniques[-1]):
        uniques_in_values[-1] = True
    unique_valid_indices = np.searchsorted(unique_values, uniques[uniques_in_values])
    output = np.zeros_like(uniques, dtype = np.int64)
    output[uniques_in_values] = counts[unique_valid_indices]
    return output
