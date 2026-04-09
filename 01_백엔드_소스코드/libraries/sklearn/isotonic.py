# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: isotonic.pyc (Python 3.11)

'''Isotonic regression for obtaining monotonic fit to data.'''
import math
import warnings
from numbers import Real
import numpy as np
from scipy import interpolate, optimize
from scipy.stats import spearmanr
from sklearn._isotonic import _inplace_contiguous_isotonic_regression, _make_unique
from sklearn.base import BaseEstimator, RegressorMixin, TransformerMixin, _fit_context
from sklearn.utils import check_array, check_consistent_length, metadata_routing
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.fixes import parse_version, sp_base_version
from sklearn.utils.validation import _check_sample_weight, check_is_fitted
__all__ = [
    'IsotonicRegression',
    'check_increasing',
    'isotonic_regression']
check_increasing = (lambda x, y: (rho, _) = spearmanr(x, y)increasing_bool = rho >= 0if rho not in (-1, 1) and len(x) > 3:
F = 0.5 * math.log((1 + rho) / (1 - rho))F_se = 1 / math.sqrt(len(x) - 3)rho_0 = math.tanh(F - 1.96 * F_se)rho_1 = math.tanh(F + 1.96 * F_se)if np.sign(rho_0) != np.sign(rho_1):
warnings.warn('Confidence interval of the Spearman correlation coefficient spans zero. Determination of ``increasing`` may be suspect.')increasing_bool)()
isotonic_regression = (lambda y = validate_params({
    'y': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None],
    'y_min': [
        Interval(Real, None, None, closed = 'both'),
        None],
    'y_max': [
        Interval(Real, None, None, closed = 'both'),
        None],
    'increasing': [
        'boolean'] }, prefer_skip_nested_validation = True), *, sample_weight: y = check_array(y, ensure_2d = False, input_name = 'y', dtype = [
np.float64,
np.float32])if sp_base_version >= parse_version('1.12.0'):
res = optimize.isotonic_regression(y = y, weights = sample_weight, increasing = increasing)y = np.asarray(res.x, dtype = y.dtype)elif increasing:
passorder = np.s_[::-1]y = np.array(y[order], dtype = y.dtype)sample_weight = _check_sample_weight(sample_weight, y, dtype = y.dtype, copy = True)sample_weight = np.ascontiguousarray(sample_weight[order])_inplace_contiguous_isotonic_regression(y, sample_weight)y = y[order]# WARNING: Decompyle incomplete
)()

class IsotonicRegression(BaseEstimator, TransformerMixin, RegressorMixin):
    pass
# WARNING: Decompyle incomplete
