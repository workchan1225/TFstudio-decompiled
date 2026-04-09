# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _classes.pyc (Python 3.11)

from numbers import Integral, Real
import numpy as np
from sklearn.base import BaseEstimator, OutlierMixin, RegressorMixin, _fit_context
from sklearn.linear_model._base import LinearClassifierMixin, LinearModel, SparseCoefMixin
from sklearn.svm._base import BaseLibSVM, BaseSVC, _fit_liblinear, _get_liblinear_solver_type
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.multiclass import check_classification_targets
from sklearn.utils.validation import _num_samples, validate_data

def _validate_dual_parameter(dual, loss, penalty, multi_class, X):
    '''Helper function to assign the value of dual parameter.'''
    if dual == 'auto':
        if X.shape[0] < X.shape[1]:
            
            try:
                _get_liblinear_solver_type(multi_class, penalty, loss, True)
                return True
            except ValueError:
                return False
                
                try:
                    _get_liblinear_solver_type(multi_class, penalty, loss, False)
                    return False
                except ValueError:
                    return True
                    return dual




class LinearSVC(BaseEstimator, SparseCoefMixin, LinearClassifierMixin):
    pass
# WARNING: Decompyle incomplete


class LinearSVR(LinearModel, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class SVC(BaseSVC):
    pass
# WARNING: Decompyle incomplete


class NuSVC(BaseSVC):
    pass
# WARNING: Decompyle incomplete


class SVR(BaseLibSVM, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class NuSVR(BaseLibSVM, RegressorMixin):
    pass
# WARNING: Decompyle incomplete


class OneClassSVM(BaseLibSVM, OutlierMixin):
    pass
# WARNING: Decompyle incomplete
