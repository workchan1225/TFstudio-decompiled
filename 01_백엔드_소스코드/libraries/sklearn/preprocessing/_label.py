# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _label.pyc (Python 3.11)

import array
import itertools
import warnings
from collections import defaultdict
from numbers import Integral
import numpy as np
from scipy.sparse import sparse as sp
from sklearn.base import BaseEstimator, TransformerMixin, _fit_context
from sklearn.utils import column_or_1d
from sklearn.utils._array_api import _convert_to_numpy, _find_matching_floating_dtype, _is_numpy_namespace, _isin, device, get_namespace, get_namespace_and_device, indexing_dtype, xpx
from sklearn.utils._encode import _encode, _unique
from sklearn.utils._param_validation import Interval, validate_params
from sklearn.utils.multiclass import type_of_target, unique_labels
from sklearn.utils.sparsefuncs import min_max_axis
from sklearn.utils.validation import _num_samples, check_array, check_is_fitted
__all__ = [
    'LabelBinarizer',
    'LabelEncoder',
    'MultiLabelBinarizer',
    'label_binarize']

def LabelEncoder():
    '''LabelEncoder'''
    pass
# WARNING: Decompyle incomplete

LabelEncoder = <NODE:27>(LabelEncoder, 'LabelEncoder', TransformerMixin, BaseEstimator, auto_wrap_output_keys = None)

def LabelBinarizer():
    '''LabelBinarizer'''
    pass
# WARNING: Decompyle incomplete

LabelBinarizer = <NODE:27>(LabelBinarizer, 'LabelBinarizer', TransformerMixin, BaseEstimator, auto_wrap_output_keys = None)
label_binarize = (lambda y = validate_params({
    'y': [
        'array-like',
        'sparse matrix'],
    'classes': [
        'array-like'],
    'neg_label': [
        Interval(Integral, None, None, closed = 'neither')],
    'pos_label': [
        Interval(Integral, None, None, closed = 'neither')],
    'sparse_output': [
        'boolean'] }, prefer_skip_nested_validation = True), *, classes: if not isinstance(y, list):
y = check_array(y, input_name = 'y', accept_sparse = 'csr', ensure_2d = False, dtype = None)elif _num_samples(y) == 0:
raise ValueError('y has 0 samples: %r' % y)if neg_label >= pos_label:
raise ValueError('neg_label={0} must be strictly less than pos_label={1}.'.format(neg_label, pos_label))if sparse_output:
if pos_label == 0 or neg_label != 0:
raise ValueError('Sparse binarization is only supported with non zero pos_label and zero neg_label, got pos_label={0} and neg_label={1}'.format(pos_label, neg_label))pos_switch = pos_label == 0if pos_switch:
pos_label = -neg_labely_type = type_of_target(y)if 'multioutput' in y_type:
raise ValueError('Multioutput target data is not supported with label binarization')if y_type == 'unknown':
raise ValueError('The type of target data is not known')(xp, is_array_api, device_) = get_namespace_and_device(y)if not is_array_api and sparse_output and _is_numpy_namespace(xp):
raise ValueError(f'''`sparse_output=True` is not supported for array API \'namespace {xp.__name__}\'. Use `sparse_output=False` to return a dense array instead.''')try:
classes = xp.asarray(classes, device = device_)except (ValueError, TypeError):
e = Noneraise ValueError(f'''`classes` contains unsupported dtype for array API namespace \'{xp.__name__}\'.'''), ee = Nonedel en_samples = y.shape[0] if hasattr(y, 'shape') else len(y)n_classes = classes.shape[0]if hasattr(y, 'dtype') and xp.isdtype(y.dtype, 'integral'):
int_dtype_ = y.dtypeelse:
int_dtype_ = indexing_dtype(xp)if y_type == 'binary':
if n_classes == 1:
if sparse_output:
sp.csr_matrix((n_samples, 1), dtype = int)Y = None.zeros((n_samples, 1), dtype = int_dtype_)Y += neg_labelYif None >= 3:
y_type = 'multiclass'sorted_class = xp.sort(classes)if y_type == 'multilabel-indicator':
y_n_classes = y.shape[1] if hasattr(y, 'shape') else len(y[0])if n_classes != y_n_classes:
raise ValueError('classes {0} mismatch with the labels {1} found in the data'.format(classes, unique_labels(y)))if y_type in ('binary', 'multiclass'):
y = column_or_1d(y)y_in_classes = _isin(y, classes, xp = xp)y_seen = y[y_in_classes]indices = xp.searchsorted(sorted_class, y_seen)y_in_classes = xp.astype(y_in_classes, int_dtype_)indptr = xp.concat((xp.asarray([
0], device = device_), xp.cumulative_sum(y_in_classes, axis = 0)))data = xp.full_like(indices, pos_label)Y = sp.csr_matrix((_convert_to_numpy(data, xp = xp), _convert_to_numpy(indices, xp = xp), _convert_to_numpy(indptr, xp = xp)), shape = (n_samples, n_classes))if not sparse_output:
Y = xp.asarray(Y.toarray(), device = device_)elif y_type == 'multilabel-indicator':
if sparse_output:
Y = sp.csr_matrix(y)if pos_label != 1:
data = xp.full_like(Y.data, pos_label)Y.data = dataelif sp.issparse(y):
y = y.toarray()Y = xp.asarray(y, device = device_, copy = True)if pos_label != 1:
Y[Y != 0] = pos_labelelse:
raise ValueError('%s target data is not supported with label binarization' % y_type)if not sparse_output:
if neg_label != 0:
Y[Y == 0] = neg_labelif pos_switch:
Y[Y == pos_label] = 0Y = xp.astype(Y, int_dtype_, copy = False)else:
Y.data = Y.data.astype(int, copy = False)if xp.any(classes != sorted_class):
indices = xp.searchsorted(sorted_class, classes)Y = Y[(:, indices)]if y_type == 'binary':
if sparse_output:
Y = Y[(:, [
-1])]else:
Y = xp.reshape(Y[(:, -1)], (-1, 1))Y)()

def _inverse_binarize_multiclass(y, classes, xp = (None,)):
    '''Inverse label binarization transformation for multiclass.

    Multiclass uses the maximal score instead of a threshold.
    '''
    if sp.issparse(y):
        classes = np.asarray(classes)
        y = y.tocsr()
        (n_samples, n_outputs) = y.shape
        outputs = np.arange(n_outputs)
        row_max = min_max_axis(y, 1)[1]
        row_nnz = np.diff(y.indptr)
        y_data_repeated_max = np.repeat(row_max, row_nnz)
        y_i_all_argmax = np.flatnonzero(y_data_repeated_max == y.data)
        if row_max[-1] == 0:
            y_i_all_argmax = np.append(y_i_all_argmax, [
                len(y.data)])
        index_first_argmax = np.searchsorted(y_i_all_argmax, y.indptr[:-1])
        y_ind_ext = np.append(y.indices, [
            0])
        y_i_argmax = y_ind_ext[y_i_all_argmax[index_first_argmax]]
        y_i_argmax[np.where(row_nnz == 0)[0]] = 0
        samples = np.arange(n_samples)[(row_nnz > 0) & (row_max.ravel() == 0)]
        for i in samples:
            ind = y.indices[y.indptr[i]:y.indptr[i + 1]]
            y_i_argmax[i] = classes[np.setdiff1d(outputs, ind)][0]
            return classes[y_i_argmax]
            (xp, _, device_) = get_namespace_and_device(y, xp = xp)
            classes = xp.asarray(classes, device = device_)
            indices = xp.argmax(y, axis = 1)
            indices = xp.clip(indices, 0, classes.shape[0] - 1)
            return classes[indices]


def _inverse_binarize_thresholding(y, output_type, classes, threshold, xp = (None,)):
    '''Inverse label binarization transformation using thresholding.'''
    if output_type == 'binary' and y.ndim == 2 and y.shape[1] > 2:
        raise ValueError("output_type='binary', but y.shape = {0}".format(y.shape))
    (xp, _, device_) = get_namespace_and_device(y, xp = xp)
    classes = xp.asarray(classes, device = device_)
    if output_type != 'binary' and y.shape[1] != classes.shape[0]:
        raise ValueError('The number of class is not equal to the number of dimension of y.')
    dtype_ = _find_matching_floating_dtype(y, xp = xp)
    if hasattr(y, 'dtype') and xp.isdtype(y.dtype, 'integral'):
        int_dtype_ = y.dtype
    else:
        int_dtype_ = indexing_dtype(xp)
    if sp.issparse(y):
        if threshold > 0:
            if y.format not in ('csr', 'csc'):
                y = y.tocsr()
            y.data = np.array(y.data > threshold, dtype = int)
            y.eliminate_zeros()
        else:
            y = xp.asarray(y.toarray() > threshold, dtype = int_dtype_, device = device_)
    else:
        y = xp.asarray(xp.asarray(y, dtype = dtype_, device = device_) > threshold, dtype = int_dtype_, device = device_)
    if output_type == 'binary':
        if sp.issparse(y):
            y = y.toarray()
        if y.ndim == 2 and y.shape[1] == 2:
            return classes[y[(:, 1)]]
        if None.shape[0] == 1:
            return xp.repeat(classes[0], len(y))
        return None[xp.reshape(y, (-1,))]
    if None == 'multilabel-indicator':
        return y
    raise None('{0} format is not supported'.format(output_type))


def MultiLabelBinarizer():
    '''MultiLabelBinarizer'''
    pass
# WARNING: Decompyle incomplete

MultiLabelBinarizer = <NODE:27>(MultiLabelBinarizer, 'MultiLabelBinarizer', TransformerMixin, BaseEstimator, auto_wrap_output_keys = None)
