# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _search_successive_halving.pyc (Python 3.11)

from abc import abstractmethod
from math import ceil, floor, log
from numbers import Integral, Real
import numpy as np
from sklearn.base import _fit_context, is_classifier
from sklearn.metrics._scorer import get_scorer_names
from sklearn.model_selection import ParameterGrid, ParameterSampler
from sklearn.model_selection._search import BaseSearchCV
from sklearn.model_selection._split import _yields_constant_splits, check_cv
from sklearn.utils import resample
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import _num_samples, validate_data
__all__ = [
    'HalvingGridSearchCV',
    'HalvingRandomSearchCV']

class _SubsampleMetaSplitter:
    '''Splitter that subsamples a given fraction of the dataset'''
    
    def __init__(self, *, base_cv, fraction, subsample_test, random_state):
        self.base_cv = base_cv
        self.fraction = fraction
        self.subsample_test = subsample_test
        self.random_state = random_state

    
    def split(self, X, y, **kwargs):
        pass
    # WARNING: Decompyle incomplete



def _top_k(results, k, itr):
    (iteration, mean_test_score, params) = (results['iter'], results['mean_test_score'], results['params'])()
    iter_indices = np.flatnonzero(iteration == itr)
    scores = mean_test_score[iter_indices]
    sorted_indices = np.roll(np.argsort(scores), np.count_nonzero(np.isnan(scores)))
    return np.array(params[iter_indices][sorted_indices[-k:]])


class BaseSuccessiveHalving(BaseSearchCV):
    pass
# WARNING: Decompyle incomplete


class HalvingGridSearchCV(BaseSuccessiveHalving):
    pass
# WARNING: Decompyle incomplete


class HalvingRandomSearchCV(BaseSuccessiveHalving):
    pass
# WARNING: Decompyle incomplete
