# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _search.pyc (Python 3.11)

'''
The :mod:`sklearn.model_selection._search` includes utilities to fine-tune the
parameters of an estimator.
'''
import numbers
import operator
import time
import warnings
from abc import ABCMeta, abstractmethod
from collections import defaultdict
from collections.abc import Iterable, Mapping, Sequence
from copy import deepcopy
from functools import partial, reduce
from inspect import signature
from itertools import product
import numpy as np
from numpy.ma import MaskedArray
from scipy.stats import rankdata
from sklearn.base import BaseEstimator, MetaEstimatorMixin, _fit_context, clone, is_classifier
from sklearn.exceptions import NotFittedError
from sklearn.metrics import check_scoring
from sklearn.metrics._scorer import _check_multimetric_scoring, _MultimetricScorer, get_scorer_names
from sklearn.model_selection._split import check_cv
from sklearn.model_selection._validation import _aggregate_score_dicts, _fit_and_score, _insert_error_scores, _normalize_score_results, _warn_or_raise_about_fit_failures
from sklearn.utils import Bunch, check_random_state
from sklearn.utils._array_api import xpx
from sklearn.utils._param_validation import HasMethods, Interval, StrOptions
from sklearn.utils._repr_html.estimator import _VisualBlock
from sklearn.utils._tags import get_tags
from sklearn.utils.metadata_routing import MetadataRouter, MethodMapping, _raise_for_params, _routing_enabled, process_routing
from sklearn.utils.metaestimators import available_if
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.random import sample_without_replacement
from sklearn.utils.validation import _check_method_params, check_is_fitted, indexable
__all__ = [
    'GridSearchCV',
    'ParameterGrid',
    'ParameterSampler',
    'RandomizedSearchCV']

class ParameterGrid:
    """Grid of parameters with a discrete number of values for each.

    Can be used to iterate over parameter value combinations with the
    Python built-in function iter.
    The order of the generated parameter combinations is deterministic.

    Read more in the :ref:`User Guide <grid_search>`.

    Parameters
    ----------
    param_grid : dict of str to sequence, or sequence of such
        The parameter grid to explore, as a dictionary mapping estimator
        parameters to sequences of allowed values.

        An empty dict signifies default parameters.

        A sequence of dicts signifies a sequence of grids to search, and is
        useful to avoid exploring parameter combinations that make no sense
        or have no effect. See the examples below.

    Examples
    --------
    >>> from sklearn.model_selection import ParameterGrid
    >>> param_grid = {'a': [1, 2], 'b': [True, False]}
    >>> list(ParameterGrid(param_grid)) == (
    ...    [{'a': 1, 'b': True}, {'a': 1, 'b': False},
    ...     {'a': 2, 'b': True}, {'a': 2, 'b': False}])
    True

    >>> grid = [{'kernel': ['linear']}, {'kernel': ['rbf'], 'gamma': [1, 10]}]
    >>> list(ParameterGrid(grid)) == [{'kernel': 'linear'},
    ...                               {'kernel': 'rbf', 'gamma': 1},
    ...                               {'kernel': 'rbf', 'gamma': 10}]
    True
    >>> ParameterGrid(grid)[1] == {'kernel': 'rbf', 'gamma': 1}
    True

    See Also
    --------
    GridSearchCV : Uses :class:`ParameterGrid` to perform a full parallelized
        parameter search.
    """
    
    def __init__(self, param_grid):
        if not isinstance(param_grid, (Mapping, Iterable)):
            raise TypeError(f'''Parameter grid should be a dict or a list, got: {param_grid!r} of type {type(param_grid).__name__}''')
        if isinstance(param_grid, Mapping):
            param_grid = [
                param_grid]
        for grid in param_grid:
            if not isinstance(grid, dict):
                raise TypeError(f'''Parameter grid is not a dict ({grid!r})''')
            for key, value in grid.items():
                if isinstance(value, np.ndarray) and value.ndim > 1:
                    raise ValueError(f'''Parameter array for {key!r} should be one-dimensional, got: {value!r} with shape {value.shape}''')
                if not isinstance(value, str) or isinstance(value, (np.ndarray, Sequence)):
                    raise TypeError(f'''Parameter grid for parameter {key!r} needs to be a list or a numpy array, but got {value!r} (of type {type(value).__name__}) instead. Single values need to be wrapped in a list with one element.''')
                if len(value) == 0:
                    raise ValueError(f'''Parameter grid for parameter {key!r} need to be a non-empty sequence, got: {value!r}''')
                self.param_grid = param_grid
                return None

    
    def __iter__(self):
        '''Iterate over the points in the grid.

        Returns
        -------
        params : iterator over dict of str to any
            Yields dictionaries mapping each estimator parameter to one of its
            allowed values.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        '''Number of points on the grid.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __getitem__(self, ind):
        '''Get the parameters that would be ``ind``th in iteration

        Parameters
        ----------
        ind : int
            The iteration index

        Returns
        -------
        params : dict of str to any
            Equal to list(self)[ind]
        '''
        pass
    # WARNING: Decompyle incomplete



class ParameterSampler:
    """Generator on parameters sampled from given distributions.

    Non-deterministic iterable over random candidate combinations for hyper-
    parameter search. If all parameters are presented as a list,
    sampling without replacement is performed. If at least one parameter
    is given as a distribution, sampling with replacement is used.
    It is highly recommended to use continuous distributions for continuous
    parameters.

    Read more in the :ref:`User Guide <grid_search>`.

    Parameters
    ----------
    param_distributions : dict
        Dictionary with parameters names (`str`) as keys and distributions
        or lists of parameters to try. Distributions must provide a ``rvs``
        method for sampling (such as those from scipy.stats.distributions).
        If a list is given, it is sampled uniformly.
        If a list of dicts is given, first a dict is sampled uniformly, and
        then a parameter is sampled using that dict as above.

    n_iter : int
        Number of parameter settings that are produced.

    random_state : int, RandomState instance or None, default=None
        Pseudo random number generator state used for random uniform sampling
        from lists of possible values instead of scipy.stats distributions.
        Pass an int for reproducible output across multiple
        function calls.
        See :term:`Glossary <random_state>`.

    Returns
    -------
    params : dict of str to any
        **Yields** dictionaries mapping each estimator parameter to
        as sampled value.

    Examples
    --------
    >>> from sklearn.model_selection import ParameterSampler
    >>> from scipy.stats.distributions import expon
    >>> import numpy as np
    >>> rng = np.random.RandomState(0)
    >>> param_grid = {'a':[1, 2], 'b': expon()}
    >>> param_list = list(ParameterSampler(param_grid, n_iter=4,
    ...                                    random_state=rng))
    >>> rounded_list = [dict((k, round(v, 6)) for (k, v) in d.items())
    ...                 for d in param_list]
    >>> rounded_list == [{'b': 0.89856, 'a': 1},
    ...                  {'b': 0.923223, 'a': 1},
    ...                  {'b': 1.878964, 'a': 2},
    ...                  {'b': 1.038159, 'a': 2}]
    True
    """
    
    def __init__(self, param_distributions = None, n_iter = {
        'random_state': None }, *, random_state):
        if not isinstance(param_distributions, (Mapping, Iterable)):
            raise TypeError(f'''Parameter distribution is not a dict or a list, got: {param_distributions!r} of type {type(param_distributions).__name__}''')
        if isinstance(param_distributions, Mapping):
            param_distributions = [
                param_distributions]
        for dist in param_distributions:
            if not isinstance(dist, dict):
                raise TypeError('Parameter distribution is not a dict ({!r})'.format(dist))
            for key in dist:
                if not isinstance(dist[key], Iterable) and hasattr(dist[key], 'rvs'):
                    raise TypeError(f'''Parameter grid for parameter {key!r} is not iterable or a distribution (value={dist[key]})''')
                self.n_iter = n_iter
                self.random_state = random_state
                self.param_distributions = param_distributions
                return None

    
    def _is_all_lists(self):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.param_distributions())

    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        '''Number of points that will be sampled.'''
        if self._is_all_lists():
            grid_size = len(ParameterGrid(self.param_distributions))
            return min(self.n_iter, grid_size)
        return None.n_iter



def _check_refit(search_cv, attr):
    if not search_cv.refit:
        raise AttributeError(f'''This {type(search_cv).__name__} instance was initialized with `refit=False`. {attr} is available only after refitting on the best parameters. You can refit an estimator manually using the `best_params_` attribute''')


def _search_estimator_has(attr):
    '''Check if we can delegate a method to the underlying estimator.

    Calling a prediction method will only be available if `refit=True`. In
    such case, we check first the fitted best estimator. If it is not
    fitted, we check the unfitted estimator.

    Checking the unfitted estimator allows to use `hasattr` on the `SearchCV`
    instance even before calling `fit`.
    '''
    pass
# WARNING: Decompyle incomplete


def _yield_masked_array_for_each_param(candidate_params):
    '''
    Yield a masked array for each candidate param.

    `candidate_params` is a sequence of params which were used in
    a `GridSearchCV`. We use masked arrays for the results, as not
    all params are necessarily present in each element of
    `candidate_params`. For example, if using `GridSearchCV` with
    a `SVC` model, then one might search over params like:

        - kernel=["rbf"], gamma=[0.1, 1]
        - kernel=["poly"], degree=[1, 2]

    and then param `\'gamma\'` would not be present in entries of
    `candidate_params` corresponding to `kernel=\'poly\'`.
    '''
    pass
# WARNING: Decompyle incomplete


def BaseSearchCV():
    '''BaseSearchCV'''
    pass
# WARNING: Decompyle incomplete

BaseSearchCV = <NODE:27>(BaseSearchCV, 'BaseSearchCV', MetaEstimatorMixin, BaseEstimator, metaclass = ABCMeta)

class GridSearchCV(BaseSearchCV):
    pass
# WARNING: Decompyle incomplete


class RandomizedSearchCV(BaseSearchCV):
    pass
# WARNING: Decompyle incomplete
