# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _classification.pyc (Python 3.11)

'''Nearest Neighbor Classification'''
import warnings
from numbers import Integral
import numpy as np
from sklearn.base import ClassifierMixin, _fit_context
from sklearn.metrics._pairwise_distances_reduction import ArgKminClassMode, RadiusNeighborsClassMode
from sklearn.neighbors._base import KNeighborsMixin, NeighborsBase, RadiusNeighborsMixin, _check_precomputed, _get_weights
from sklearn.utils._param_validation import StrOptions
from sklearn.utils.arrayfuncs import _all_with_any_reduction_axis_1
from sklearn.utils.extmath import weighted_mode
from sklearn.utils.fixes import _mode
from sklearn.utils.validation import _is_arraylike, _num_samples, check_is_fitted, validate_data

def _adjusted_metric(metric, metric_kwargs, p = (None,)):
    if not metric_kwargs:
        metric_kwargs = { }
        if metric == 'minkowski':
            metric_kwargs['p'] = p
            if p == 2:
                metric = 'euclidean'
    return (metric, metric_kwargs)


class KNeighborsClassifier(NeighborsBase, ClassifierMixin, KNeighborsMixin):
    pass
# WARNING: Decompyle incomplete


class RadiusNeighborsClassifier(NeighborsBase, ClassifierMixin, RadiusNeighborsMixin):
    pass
# WARNING: Decompyle incomplete
