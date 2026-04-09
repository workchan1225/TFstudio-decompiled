# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _bounds.pyc (Python 3.11)

'''Determination of parameter bounds'''
from numbers import Real
import numpy as np
from sklearn.preprocessing import LabelBinarizer
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.extmath import safe_sparse_dot
from sklearn.utils.validation import check_array, check_consistent_length
l1_min_c = (lambda X = validate_params({
    'X': [
        'array-like',
        'sparse matrix'],
    'y': [
        'array-like'],
    'loss': [
        StrOptions({
            'squared_hinge',
            'log'})],
    'fit_intercept': [
        'boolean'],
    'intercept_scaling': [
        Interval(Real, 0, None, closed = 'neither')] }, prefer_skip_nested_validation = True), y = {
    'loss': 'squared_hinge',
    'fit_intercept': True,
    'intercept_scaling': 1 }, *, loss, fit_intercept: X = check_array(X, accept_sparse = 'csc')check_consistent_length(X, y)Y = LabelBinarizer(neg_label = -1).fit_transform(y).Tden = np.max(np.abs(safe_sparse_dot(Y, X)))if fit_intercept:
bias = np.full((np.size(y), 1), intercept_scaling, dtype = np.array(intercept_scaling).dtype)den = max(den, abs(np.dot(Y, bias)).max())if den == 0:
raise ValueError('Ill-posed l1_min_c calculation: l1 will always select zero coefficients for this data')if loss == 'squared_hinge':
0.5 / denNone / den)()
