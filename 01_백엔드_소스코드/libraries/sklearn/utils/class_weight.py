# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: class_weight.pyc (Python 3.11)

'''Utilities for handling weights based on class labels.'''
import numpy as np
from scipy import sparse
from sklearn.utils._param_validation import StrOptions, validate_params
from sklearn.utils.validation import _check_sample_weight
compute_class_weight = (lambda class_weight = validate_params({
    'class_weight': [
        dict,
        StrOptions({
            'balanced'}),
        None],
    'classes': [
        np.ndarray],
    'y': [
        'array-like'],
    'sample_weight': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), *, classes: LabelEncoder = LabelEncoderimport sklearn.preprocessingif set(y) - set(classes):
raise ValueError('classes should include all valid labels that can be in y')# WARNING: Decompyle incomplete
)()
compute_sample_weight = (lambda class_weight = validate_params({
    'class_weight': [
        dict,
        list,
        StrOptions({
            'balanced'}),
        None],
    'y': [
        'array-like',
        'sparse matrix'],
    'indices': [
        'array-like',
        None] }, prefer_skip_nested_validation = True), y = {
    'indices': None }, *, indices, n_outputs = None: if not sparse.issparse(y):
y = np.atleast_1d(y)if y.ndim == 1:
y = np.reshape(y, (-1, 1))n_outputs = y.shape[1]# WARNING: Decompyle incomplete
)()
