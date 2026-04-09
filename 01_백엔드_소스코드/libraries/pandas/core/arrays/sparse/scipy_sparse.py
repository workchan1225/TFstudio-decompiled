# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: scipy_sparse.pyc (Python 3.11)

'''
Interaction with scipy.sparse matrices.

Currently only includes to_coo helpers.
'''
from __future__ import annotations
from typing import TYPE_CHECKING
from pandas._libs import lib
from pandas.core.dtypes.missing import notna
from pandas.core.algorithms import factorize
from pandas.core.indexes.api import MultiIndex
from pandas.core.series import Series
if TYPE_CHECKING:
    from collections.abc import Iterable
    import numpy as np
    import scipy.sparse as scipy
    from pandas._typing import IndexLabel, npt

def _check_is_partition(parts = None, whole = None):
    whole = set(whole)
    parts = parts()
# WARNING: Decompyle incomplete


def _levels_to_axis(ss = None, levels = None, valid_ilocs = None, sort_labels = (False,)):
    """
    For a MultiIndexed sparse Series `ss`, return `ax_coords` and `ax_labels`,
    where `ax_coords` are the coordinates along one of the two axes of the
    destination sparse matrix, and `ax_labels` are the labels from `ss`' Index
    which correspond to these coordinates.

    Parameters
    ----------
    ss : Series
    levels : tuple/list
    valid_ilocs : numpy.ndarray
        Array of integer positions of valid values for the sparse matrix in ss.
    sort_labels : bool, default False
        Sort the axis labels before forming the sparse matrix. When `levels`
        refers to a single level, set to True for a faster execution.

    Returns
    -------
    ax_coords : numpy.ndarray (axis coordinates)
    ax_labels : list (axis labels)
    """
    pass
# WARNING: Decompyle incomplete


def _to_ijv(ss = None, row_levels = None, column_levels = None, sort_labels = ((0,), (1,), False)):
    '''
    For an arbitrary MultiIndexed sparse Series return (v, i, j, ilabels,
    jlabels) where (v, (i, j)) is suitable for passing to scipy.sparse.coo
    constructor, and ilabels and jlabels are the row and column labels
    respectively.

    Parameters
    ----------
    ss : Series
    row_levels : tuple/list
    column_levels : tuple/list
    sort_labels : bool, default False
        Sort the row and column labels before forming the sparse matrix.
        When `row_levels` and/or `column_levels` refer to a single level,
        set to `True` for a faster execution.

    Returns
    -------
    values : numpy.ndarray
        Valid values to populate a sparse matrix, extracted from
        ss.
    i_coords : numpy.ndarray (row coordinates of the values)
    j_coords : numpy.ndarray (column coordinates of the values)
    i_labels : list (row labels)
    j_labels : list (column labels)
    '''
    _check_is_partition([
        row_levels,
        column_levels], range(ss.index.nlevels))
    sp_vals = ss.array.sp_values
    na_mask = notna(sp_vals)
    values = sp_vals[na_mask]
    valid_ilocs = ss.array.sp_index.indices[na_mask]
    (i_coords, i_labels) = _levels_to_axis(ss, row_levels, valid_ilocs, sort_labels = sort_labels)
    (j_coords, j_labels) = _levels_to_axis(ss, column_levels, valid_ilocs, sort_labels = sort_labels)
    return (values, i_coords, j_coords, i_labels, j_labels)


def sparse_series_to_coo(ss = None, row_levels = None, column_levels = None, sort_labels = ((0,), (1,), False)):
    '''
    Convert a sparse Series to a scipy.sparse.coo_matrix using index
    levels row_levels, column_levels as the row and column
    labels respectively. Returns the sparse_matrix, row and column labels.
    '''
    pass
# WARNING: Decompyle incomplete


def coo_to_sparse_series(A = None, dense_index = None):
    '''
    Convert a scipy.sparse.coo_matrix to a Series with type sparse.

    Parameters
    ----------
    A : scipy.sparse.coo_matrix
    dense_index : bool, default False

    Returns
    -------
    Series

    Raises
    ------
    TypeError if A is not a coo_matrix
    '''
    SparseDtype = SparseDtype
    import pandas
    
    try:
        ser = Series(A.data, MultiIndex.from_arrays((A.row, A.col)), copy = False)
    except AttributeError:
        err = None
        raise TypeError(f'''Expected coo_matrix. Got {type(A).__name__} instead.'''), err
        err = None
        del err

    ser = ser.sort_index()
    ser = ser.astype(SparseDtype(ser.dtype))
    if dense_index:
        ind = MultiIndex.from_product([
            A.row,
            A.col])
        ser = ser.reindex(ind)
    return ser
