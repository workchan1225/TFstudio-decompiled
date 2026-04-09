# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _regression.pyc (Python 3.11)

'''Nearest Neighbor Regression.'''
import warnings
import numpy as np
from sklearn.base import RegressorMixin, _fit_context
from sklearn.metrics import DistanceMetric
from sklearn.neighbors._base import KNeighborsMixin, NeighborsBase, RadiusNeighborsMixin, _get_weights
from sklearn.utils._param_validation import StrOptions

class KNeighborsRegressor(NeighborsBase, RegressorMixin, KNeighborsMixin):
    pass
# WARNING: Decompyle incomplete


class RadiusNeighborsRegressor(NeighborsBase, RegressorMixin, RadiusNeighborsMixin):
    pass
# WARNING: Decompyle incomplete
