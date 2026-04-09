# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _split.pyc (Python 3.11)

'''
The :mod:`sklearn.model_selection._split` module includes classes and
functions to split the data based on a preset strategy.
'''
import numbers
import warnings
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from collections.abc import Iterable
from inspect import signature
from itertools import chain, combinations
from math import ceil, floor
import numpy as np
from scipy.special import comb
from sklearn.utils import _safe_indexing, check_random_state, indexable, metadata_routing
from sklearn.utils._array_api import _convert_to_numpy, get_namespace, get_namespace_and_device, move_to
from sklearn.utils._param_validation import Interval, RealNotInt, validate_params
from sklearn.utils.extmath import _approximate_mode
from sklearn.utils.metadata_routing import _MetadataRequester
from sklearn.utils.multiclass import type_of_target
from sklearn.utils.validation import _num_samples, check_array, column_or_1d
__all__ = [
    'BaseCrossValidator',
    'GroupKFold',
    'GroupShuffleSplit',
    'KFold',
    'LeaveOneGroupOut',
    'LeaveOneOut',
    'LeavePGroupsOut',
    'LeavePOut',
    'PredefinedSplit',
    'RepeatedKFold',
    'RepeatedStratifiedKFold',
    'ShuffleSplit',
    'StratifiedGroupKFold',
    'StratifiedKFold',
    'StratifiedShuffleSplit',
    'check_cv',
    'train_test_split']

class _UnsupportedGroupCVMixin:
    pass
# WARNING: Decompyle incomplete


class GroupsConsumerMixin(_MetadataRequester):
    '''A Mixin to ``groups`` by default.

    This Mixin makes the object to request ``groups`` by default as ``True``.

    .. versionadded:: 1.3
    '''
    __metadata_request__split = {
        'groups': True }


def BaseCrossValidator():
    '''BaseCrossValidator'''
    __doc__ = 'Base class for all cross-validators.\n\n    Implementations must define `_iter_test_masks` or `_iter_test_indices`.\n    '
    __metadata_request__split = {
        'groups': metadata_routing.UNUSED }
    
    def split(self, X, y, groups = (None, None)):
        '''Generate indices to split data into training and test set.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,)
            The target variable for supervised learning problems.

        groups : array-like of shape (n_samples,), default=None
            Group labels for the samples used while splitting the dataset into
            train/test set.

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_test_masks(self, X, y, groups = (None, None, None)):
        '''Generates boolean masks corresponding to test sets.

        By default, delegates to _iter_test_indices(X, y, groups)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_test_indices(self, X, y, groups = (None, None, None)):
        '''Generates integer indices corresponding to test sets.'''
        raise NotImplementedError

    get_n_splits = (lambda self, X, y, groups = (None, None, None): pass)()
    
    def __repr__(self):
        return _build_repr(self)


BaseCrossValidator = <NODE:27>(BaseCrossValidator, 'BaseCrossValidator', _MetadataRequester, metaclass = ABCMeta)

class LeaveOneOut(BaseCrossValidator, _UnsupportedGroupCVMixin):
    '''Leave-One-Out cross-validator.

    Provides train/test indices to split data in train/test sets. Each
    sample is used once as a test set (singleton) while the remaining
    samples form the training set.

    Note: ``LeaveOneOut()`` is equivalent to ``KFold(n_splits=n)`` and
    ``LeavePOut(p=1)`` where ``n`` is the number of samples.

    Due to the high number of test sets (which is the same as the
    number of samples) this cross-validation method can be very costly.
    For large datasets one should favor :class:`KFold`, :class:`ShuffleSplit`
    or :class:`StratifiedKFold`.

    Read more in the :ref:`User Guide <leave_one_out>`.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.model_selection import LeaveOneOut
    >>> X = np.array([[1, 2], [3, 4]])
    >>> y = np.array([1, 2])
    >>> loo = LeaveOneOut()
    >>> loo.get_n_splits(X)
    2
    >>> print(loo)
    LeaveOneOut()
    >>> for i, (train_index, test_index) in enumerate(loo.split(X)):
    ...     print(f"Fold {i}:")
    ...     print(f"  Train: index={train_index}")
    ...     print(f"  Test:  index={test_index}")
    Fold 0:
      Train: index=[1]
      Test:  index=[0]
    Fold 1:
      Train: index=[0]
      Test:  index=[1]

    See Also
    --------
    LeaveOneGroupOut : For splitting the data according to explicit,
        domain-specific stratification of the dataset.
    GroupKFold : K-fold iterator variant with non-overlapping groups.
    '''
    
    def _iter_test_indices(self, X, y, groups = (None, None)):
        n_samples = _num_samples(X)
        if n_samples <= 1:
            raise ValueError('Cannot perform LeaveOneOut with n_samples={}.'.format(n_samples))
        return range(n_samples)

    
    def get_n_splits(self, X, y, groups = (None, None)):
        '''Returns the number of splitting iterations in the cross-validator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Returns
        -------
        n_splits : int
            Returns the number of splitting iterations in the cross-validator.
        '''
        pass
    # WARNING: Decompyle incomplete



class LeavePOut(BaseCrossValidator, _UnsupportedGroupCVMixin):
    '''Leave-P-Out cross-validator.

    Provides train/test indices to split data in train/test sets. This results
    in testing on all distinct samples of size p, while the remaining n - p
    samples form the training set in each iteration.

    Note: ``LeavePOut(p)`` is NOT equivalent to
    ``KFold(n_splits=n_samples // p)`` which creates non-overlapping test sets.

    Due to the high number of iterations which grows combinatorically with the
    number of samples this cross-validation method can be very costly. For
    large datasets one should favor :class:`KFold`, :class:`StratifiedKFold`
    or :class:`ShuffleSplit`.

    Read more in the :ref:`User Guide <leave_p_out>`.

    Parameters
    ----------
    p : int
        Size of the test sets. Must be strictly less than the number of
        samples.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.model_selection import LeavePOut
    >>> X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    >>> y = np.array([1, 2, 3, 4])
    >>> lpo = LeavePOut(2)
    >>> lpo.get_n_splits(X)
    6
    >>> print(lpo)
    LeavePOut(p=2)
    >>> for i, (train_index, test_index) in enumerate(lpo.split(X)):
    ...     print(f"Fold {i}:")
    ...     print(f"  Train: index={train_index}")
    ...     print(f"  Test:  index={test_index}")
    Fold 0:
      Train: index=[2 3]
      Test:  index=[0 1]
    Fold 1:
      Train: index=[1 3]
      Test:  index=[0 2]
    Fold 2:
      Train: index=[1 2]
      Test:  index=[0 3]
    Fold 3:
      Train: index=[0 3]
      Test:  index=[1 2]
    Fold 4:
      Train: index=[0 2]
      Test:  index=[1 3]
    Fold 5:
      Train: index=[0 1]
      Test:  index=[2 3]
    '''
    
    def __init__(self, p):
        self.p = p

    
    def _iter_test_indices(self, X, y, groups = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def get_n_splits(self, X, y, groups = (None, None)):
        '''Returns the number of splitting iterations in the cross-validator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.
        '''
        pass
    # WARNING: Decompyle incomplete



def _BaseKFold():
    '''_BaseKFold'''
    pass
# WARNING: Decompyle incomplete

_BaseKFold = <NODE:27>(_BaseKFold, '_BaseKFold', BaseCrossValidator, metaclass = ABCMeta)

class KFold(_BaseKFold, _UnsupportedGroupCVMixin):
    pass
# WARNING: Decompyle incomplete


class GroupKFold(_BaseKFold, GroupsConsumerMixin):
    pass
# WARNING: Decompyle incomplete


class StratifiedKFold(_BaseKFold):
    pass
# WARNING: Decompyle incomplete


class StratifiedGroupKFold(_BaseKFold, GroupsConsumerMixin):
    pass
# WARNING: Decompyle incomplete


class TimeSeriesSplit(_BaseKFold):
    pass
# WARNING: Decompyle incomplete


class LeaveOneGroupOut(BaseCrossValidator, GroupsConsumerMixin):
    pass
# WARNING: Decompyle incomplete


class LeavePGroupsOut(BaseCrossValidator, GroupsConsumerMixin):
    pass
# WARNING: Decompyle incomplete


def _RepeatedSplits():
    '''_RepeatedSplits'''
    __doc__ = 'Repeated splits for an arbitrary randomized CV splitter.\n\n    Repeats splits for cross-validators n times with different randomization\n    in each repetition.\n\n    Parameters\n    ----------\n    cv : callable\n        Cross-validator class.\n\n    n_repeats : int, default=10\n        Number of times cross-validator needs to be repeated.\n\n    random_state : int, RandomState instance or None, default=None\n        Passes `random_state` to the arbitrary repeating cross validator.\n        Pass an int for reproducible output across multiple function calls.\n        See :term:`Glossary <random_state>`.\n\n    **cvargs : additional params\n        Constructor parameters for cv. Must not contain random_state\n        and shuffle.\n    '
    _RepeatedSplits__metadata_request__split = {
        'groups': metadata_routing.UNUSED }
    
    def __init__(self = None, cv = {
        'n_repeats': 10,
        'random_state': None }, *, n_repeats, random_state, **cvargs):
        pass
    # WARNING: Decompyle incomplete

    
    def split(self, X, y, groups = (None, None)):
        '''Generates indices to split data into training and test set.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,)
            The target variable for supervised learning problems.

        groups : array-like of shape (n_samples,), default=None
            Group labels for the samples used while splitting the dataset into
            train/test set.

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_n_splits(self, X, y, groups = (None, None, None)):
        '''Returns the number of splitting iterations as set with the `n_splits` param
        when instantiating the cross-validator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default=None
            Always ignored, exists for API compatibility.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Returns
        -------
        n_splits : int
            Returns the number of splitting iterations in the cross-validator.
        '''
        rng = check_random_state(self.random_state)
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return _build_repr(self)


_RepeatedSplits = <NODE:27>(_RepeatedSplits, '_RepeatedSplits', _MetadataRequester, metaclass = ABCMeta)

class RepeatedKFold(_RepeatedSplits, _UnsupportedGroupCVMixin):
    pass
# WARNING: Decompyle incomplete


class RepeatedStratifiedKFold(_RepeatedSplits, _UnsupportedGroupCVMixin):
    pass
# WARNING: Decompyle incomplete


def BaseShuffleSplit():
    '''BaseShuffleSplit'''
    __doc__ = 'Base class for *ShuffleSplit.\n\n    Parameters\n    ----------\n    n_splits : int, default=10\n        Number of re-shuffling & splitting iterations.\n\n    test_size : float or int, default=None\n        If float, should be between 0.0 and 1.0 and represent the proportion\n        of the dataset to include in the test split. If int, represents the\n        absolute number of test samples. If None, the value is set to the\n        complement of the train size. If ``train_size`` is also None, it will\n        be set to 0.1.\n\n    train_size : float or int, default=None\n        If float, should be between 0.0 and 1.0 and represent the\n        proportion of the dataset to include in the train split. If\n        int, represents the absolute number of train samples. If None,\n        the value is automatically set to the complement of the test size.\n\n    random_state : int, RandomState instance or None, default=None\n        Controls the randomness of the training and testing indices produced.\n        Pass an int for reproducible output across multiple function calls.\n        See :term:`Glossary <random_state>`.\n    '
    __metadata_request__split = {
        'groups': metadata_routing.UNUSED }
    
    def __init__(self = None, n_splits = (10,), *, test_size, train_size, random_state):
        self.n_splits = n_splits
        self.test_size = test_size
        self.train_size = train_size
        self.random_state = random_state
        self._default_test_size = 0.1

    
    def split(self, X, y, groups = (None, None)):
        '''Generate indices to split data into training and test set.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            Training data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        y : array-like of shape (n_samples,)
            The target variable for supervised learning problems.

        groups : array-like of shape (n_samples,), default=None
            Group labels for the samples used while splitting the dataset into
            train/test set.

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.

        Notes
        -----
        Randomized CV splitters may return different results for each call of
        split. You can make the results identical by setting `random_state`
        to an integer.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_indices(self, X, y, groups = (None, None)):
        '''Generate (train, test) indices'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_n_splits(self, X, y, groups = (None, None, None)):
        '''Returns the number of splitting iterations as set with the `n_splits` param
        when instantiating the cross-validator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default=None
            Always ignored, exists for API compatibility.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Returns
        -------
        n_splits : int
            Returns the number of splitting iterations in the cross-validator.
        '''
        return self.n_splits

    
    def __repr__(self):
        return _build_repr(self)


BaseShuffleSplit = <NODE:27>(BaseShuffleSplit, 'BaseShuffleSplit', _MetadataRequester, metaclass = ABCMeta)

class ShuffleSplit(BaseShuffleSplit, _UnsupportedGroupCVMixin):
    pass
# WARNING: Decompyle incomplete


class GroupShuffleSplit(BaseShuffleSplit, GroupsConsumerMixin):
    pass
# WARNING: Decompyle incomplete


class StratifiedShuffleSplit(BaseShuffleSplit):
    pass
# WARNING: Decompyle incomplete


def _validate_shuffle_split(n_samples, test_size, train_size, default_test_size = (None,)):
    '''
    Validation helper to check if the train/test sizes are meaningful w.r.t. the
    size of the data (n_samples).
    '''
    pass
# WARNING: Decompyle incomplete


class PredefinedSplit(BaseCrossValidator):
    '''Predefined split cross-validator.

    Provides train/test indices to split data into train/test sets using a
    predefined scheme specified by the user with the ``test_fold`` parameter.

    Read more in the :ref:`User Guide <predefined_split>`.

    .. versionadded:: 0.16

    Parameters
    ----------
    test_fold : array-like of shape (n_samples,)
        The entry ``test_fold[i]`` represents the index of the test set that
        sample ``i`` belongs to. It is possible to exclude sample ``i`` from
        any test set (i.e. include sample ``i`` in every training set) by
        setting ``test_fold[i]`` equal to -1.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.model_selection import PredefinedSplit
    >>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
    >>> y = np.array([0, 0, 1, 1])
    >>> test_fold = [0, 1, -1, 1]
    >>> ps = PredefinedSplit(test_fold)
    >>> ps.get_n_splits()
    2
    >>> print(ps)
    PredefinedSplit(test_fold=array([ 0,  1, -1,  1]))
    >>> for i, (train_index, test_index) in enumerate(ps.split()):
    ...     print(f"Fold {i}:")
    ...     print(f"  Train: index={train_index}")
    ...     print(f"  Test:  index={test_index}")
    Fold 0:
      Train: index=[1 2 3]
      Test:  index=[0]
    Fold 1:
      Train: index=[0 2]
      Test:  index=[1 3]
    '''
    
    def __init__(self, test_fold):
        self.test_fold = np.array(test_fold, dtype = int)
        self.test_fold = column_or_1d(self.test_fold)
        self.unique_folds = np.unique(self.test_fold)
        self.unique_folds = self.unique_folds[self.unique_folds != -1]

    
    def split(self, X, y, groups = (None, None, None)):
        '''Generate indices to split data into training and test set.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default=None
            Always ignored, exists for API compatibility.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _split(self):
        '''Generate indices to split data into training and test set.

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _iter_test_masks(self):
        '''Generates boolean masks corresponding to test sets.'''
        pass
    # WARNING: Decompyle incomplete

    
    def get_n_splits(self, X, y, groups = (None, None, None)):
        '''Returns the number of splitting iterations in the cross-validator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default=None
            Always ignored, exists for API compatibility.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Returns
        -------
        n_splits : int
            Returns the number of splitting iterations in the cross-validator.
        '''
        return len(self.unique_folds)



class _CVIterableWrapper(BaseCrossValidator):
    '''Wrapper class for old style cv objects and iterables.'''
    
    def __init__(self, cv):
        self.cv = list(cv)

    
    def get_n_splits(self, X, y, groups = (None, None, None)):
        '''Returns the number of splitting iterations in the cross-validator.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default=None
            Always ignored, exists for API compatibility.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Returns
        -------
        n_splits : int
            Returns the number of splitting iterations in the cross-validator.
        '''
        return len(self.cv)

    
    def split(self, X, y, groups = (None, None, None)):
        '''Generate indices to split data into training and test set.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_features), default=None
            Always ignored, exists for API compatibility.

        y : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        groups : array-like of shape (n_samples,), default=None
            Always ignored, exists for API compatibility.

        Yields
        ------
        train : ndarray
            The training set indices for that split.

        test : ndarray
            The testing set indices for that split.
        '''
        pass
    # WARNING: Decompyle incomplete



def check_cv(cv = None, y = (5, None), *, classifier):
    '''Input checker utility for building a cross-validator.

    Parameters
    ----------
    cv : int, cross-validation generator, iterable or None, default=5
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:
        - None, to use the default 5-fold cross validation,
        - integer, to specify the number of folds.
        - :term:`CV splitter`,
        - An iterable that generates (train, test) splits as arrays of indices.

        For integer/None inputs, if classifier is True and ``y`` is either
        binary or multiclass, :class:`StratifiedKFold` is used. In all other
        cases, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

        .. versionchanged:: 0.22
            ``cv`` default value changed from 3-fold to 5-fold.

    y : array-like, default=None
        The target variable for supervised learning problems.

    classifier : bool, default=False
        Whether the task is a classification task, in which case
        stratified KFold will be used.

    Returns
    -------
    checked_cv : a cross-validator instance.
        The return value is a cross-validator which generates the train/test
        splits via the ``split`` method.

    Examples
    --------
    >>> from sklearn.model_selection import check_cv
    >>> check_cv(cv=5, y=None, classifier=False)
    KFold(...)
    >>> check_cv(cv=5, y=[1, 1, 0, 0, 0, 0], classifier=True)
    StratifiedKFold(...)
    '''
    pass
# WARNING: Decompyle incomplete

train_test_split = (lambda *: pass# WARNING: Decompyle incomplete
)()
setattr(train_test_split, '__test__', False)

def _pprint(params, offset, printer = (0, repr)):
    """Pretty print the dictionary 'params'

    Parameters
    ----------
    params : dict
        The dictionary to pretty print

    offset : int, default=0
        The offset in characters to add at the begin of each line.

    printer : callable, default=repr
        The function to convert entries to strings, typically
        the builtin str or repr

    """
    options = np.get_printoptions()
    np.set_printoptions(precision = 5, threshold = 64, edgeitems = 2)
    params_list = list()
    this_line_length = offset
    line_sep = ',\n' + (1 + offset // 2) * ' '
# WARNING: Decompyle incomplete


def _build_repr(self):
    cls = self.__class__
    init = getattr(cls.__init__, 'deprecated_original', cls.__init__)
    init_signature = signature(init)
    class_name = self.__class__.__name__
    params = dict()
# WARNING: Decompyle incomplete


def _yields_constant_splits(cv):
