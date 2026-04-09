# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: metaestimators.pyc (Python 3.11)

'''Utilities for meta-estimators.'''
from abc import ABCMeta, abstractmethod
from contextlib import suppress
import numpy as np
from sklearn.base import BaseEstimator
from sklearn.utils import _safe_indexing
from sklearn.utils._available_if import available_if
from sklearn.utils._tags import get_tags
__all__ = [
    'available_if']

def _BaseComposition():
    '''_BaseComposition'''
    pass
# WARNING: Decompyle incomplete

_BaseComposition = <NODE:27>(_BaseComposition, '_BaseComposition', BaseEstimator, metaclass = ABCMeta)

def _safe_split(estimator, X, y, indices, train_indices = (None,)):
    '''Create subset of dataset and properly handle kernels.

    Slice X, y according to indices for cross-validation, but take care of
    precomputed kernel-matrices or pairwise affinities / distances.

    If ``estimator._pairwise is True``, X needs to be square and
    we slice rows and columns. If ``train_indices`` is not None,
    we slice rows using ``indices`` (assumed the test set) and columns
    using ``train_indices``, indicating the training set.

    Labels y will always be indexed only along the first axis.

    Parameters
    ----------
    estimator : object
        Estimator to determine whether we should slice only rows or rows and
        columns.

    X : array-like, sparse matrix or iterable
        Data to be indexed. If ``estimator._pairwise is True``,
        this needs to be a square array-like or sparse matrix.

    y : array-like, sparse matrix or iterable
        Targets to be indexed.

    indices : array of int
        Rows to select from X and y.
        If ``estimator._pairwise is True`` and ``train_indices is None``
        then ``indices`` will also be used to slice columns.

    train_indices : array of int or None, default=None
        If ``estimator._pairwise is True`` and ``train_indices is not None``,
        then ``train_indices`` will be use to slice the columns of X.

    Returns
    -------
    X_subset : array-like, sparse matrix or list
        Indexed data.

    y_subset : array-like, sparse matrix or list
        Indexed targets.

    '''
    pass
# WARNING: Decompyle incomplete
