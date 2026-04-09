# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: multiclass.pyc (Python 3.11)

'''Utilities to handle multiclass/multioutput target in classifiers.'''
import warnings
from collections.abc import Sequence
from itertools import chain
import numpy as np
from scipy.sparse import issparse
from sklearn.utils._array_api import get_namespace
from sklearn.utils._unique import attach_unique, cached_unique
from sklearn.utils.fixes import VisibleDeprecationWarning
from sklearn.utils.validation import _assert_all_finite, _num_samples, check_array

def _unique_multiclass(y, xp = (None,)):
    (xp, is_array_api_compliant) = get_namespace(y, xp = xp)
    if hasattr(y, '__array__') or is_array_api_compliant:
        return cached_unique(xp.asarray(y), xp = xp)
    return None(y)


def _unique_indicator(y, xp = (None,)):
    (xp, _) = get_namespace(y, xp = xp)
    return xp.arange(check_array(y, input_name = 'y', accept_sparse = [
        'csr',
        'csc',
        'coo']).shape[1])

_FN_UNIQUE_LABELS = {
    'binary': _unique_multiclass,
    'multiclass': _unique_multiclass,
    'multilabel-indicator': _unique_indicator }

def unique_labels(*ys):
    '''Extract an ordered array of unique labels.

    We don\'t allow:
        - mix of multilabel and multiclass (single label) targets
        - mix of label indicator matrix and anything else,
          because there are no explicit labels)
        - mix of label indicator matrices of different sizes
        - mix of string and integer labels

    At the moment, we also don\'t allow "multiclass-multioutput" input type.

    Parameters
    ----------
    *ys : array-likes
        Label values.

    Returns
    -------
    out : ndarray of shape (n_unique_labels,)
        An ordered array of unique labels.

    Examples
    --------
    >>> from sklearn.utils.multiclass import unique_labels
    >>> unique_labels([3, 5, 5, 5, 7, 7])
    array([3, 5, 7])
    >>> unique_labels([1, 2, 3, 4], [2, 2, 3, 4])
    array([1, 2, 3, 4])
    >>> unique_labels([1, 2, 10], [5, 11])
    array([ 1,  2,  5, 10, 11])
    '''
    pass
# WARNING: Decompyle incomplete


def _is_integral_float(y):
    (xp, is_array_api_compliant) = get_namespace(y)
    if xp.isdtype(y.dtype, 'real floating'):
        pass
    return bool(xp.all(xp.astype(xp.astype(y, xp.int64), y.dtype) == y))


def is_multilabel(y):
    '''Check if ``y`` is in a multilabel format.

    Parameters
    ----------
    y : ndarray of shape (n_samples,)
        Target values.

    Returns
    -------
    out : bool
        Return ``True``, if ``y`` is in a multilabel format, else ``False``.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.utils.multiclass import is_multilabel
    >>> is_multilabel([0, 1, 0, 1])
    False
    >>> is_multilabel([[1], [0, 2], []])
    False
    >>> is_multilabel(np.array([[1, 0], [0, 0]]))
    True
    >>> is_multilabel(np.array([[1], [0], [0]]))
    False
    >>> is_multilabel(np.array([[1, 0, 0]]))
    True
    '''
    (xp, is_array_api_compliant) = get_namespace(y)
# WARNING: Decompyle incomplete


def check_classification_targets(y):
    """Ensure that target y is of a non-regression type.

    Only the following target types (as defined in type_of_target) are allowed:
        'binary', 'multiclass', 'multiclass-multioutput',
        'multilabel-indicator', 'multilabel-sequences'

    Parameters
    ----------
    y : array-like
        Target values.
    """
    y_type = type_of_target(y, input_name = 'y')
    if y_type not in ('binary', 'multiclass', 'multiclass-multioutput', 'multilabel-indicator', 'multilabel-sequences'):
        raise ValueError(f'''Unknown label type: {y_type}. Maybe you are trying to fit a classifier, which expects discrete classes on a regression target with continuous values.''')
    if 'multiclass' in y_type:
        n_samples = _num_samples(y)
        if n_samples > 20 or cached_unique(y).shape[0] > round(0.5 * n_samples):
            warnings.warn('The number of unique classes is greater than 50% of the number of samples. `y` could represent a regression problem, not a classification problem.', UserWarning, stacklevel = 2)
            return None
        return None
    return None


def type_of_target(y, input_name, raise_unknown = ('', False)):
    '''Determine the type of data indicated by the target.

    Note that this type is the most specific type that can be inferred.
    For example:

    * ``binary`` is more specific but compatible with ``multiclass``.
    * ``multiclass`` of integers is more specific but compatible with ``continuous``.
    * ``multilabel-indicator`` is more specific but compatible with
      ``multiclass-multioutput``.

    Parameters
    ----------
    y : {array-like, sparse matrix}
        Target values. If a sparse matrix, `y` is expected to be a
        CSR/CSC matrix.

    input_name : str, default=""
        The data name used to construct the error message.

        .. versionadded:: 1.1.0

    raise_unknown : bool, default=False
        If `True`, raise an error when the type of target returned by
        :func:`~sklearn.utils.multiclass.type_of_target` is `"unknown"`.

        .. versionadded:: 1.6

    Returns
    -------
    target_type : str
        One of:

        * \'continuous\': `y` is an array-like of floats that are not all
          integers, and is 1d or a column vector.
        * \'continuous-multioutput\': `y` is a 2d array of floats that are
          not all integers, and both dimensions are of size > 1.
        * \'binary\': `y` contains <= 2 discrete values and is 1d or a column
          vector.
        * \'multiclass\': `y` contains more than two discrete values, is not a
          sequence of sequences, and is 1d or a column vector.
        * \'multiclass-multioutput\': `y` is a 2d array that contains more
          than two discrete values, is not a sequence of sequences, and both
          dimensions are of size > 1.
        * \'multilabel-indicator\': `y` is a label indicator matrix, an array
          of two dimensions with at least two columns, and at most 2 unique
          values.
        * \'unknown\': `y` is array-like but none of the above, such as a 3d
          array, sequence of sequences, or an array of non-sequence objects.

    Examples
    --------
    >>> from sklearn.utils.multiclass import type_of_target
    >>> import numpy as np
    >>> type_of_target([0.1, 0.6])
    \'continuous\'
    >>> type_of_target([1, -1, -1, 1])
    \'binary\'
    >>> type_of_target([\'a\', \'b\', \'a\'])
    \'binary\'
    >>> type_of_target([1.0, 2.0])
    \'binary\'
    >>> type_of_target([1, 0, 2])
    \'multiclass\'
    >>> type_of_target([1.0, 0.0, 3.0])
    \'multiclass\'
    >>> type_of_target([\'a\', \'b\', \'c\'])
    \'multiclass\'
    >>> type_of_target(np.array([[1, 2], [3, 1]]))
    \'multiclass-multioutput\'
    >>> type_of_target([[1, 2]])
    \'multilabel-indicator\'
    >>> type_of_target(np.array([[1.5, 2.0], [3.0, 1.6]]))
    \'continuous-multioutput\'
    >>> type_of_target(np.array([[0, 1], [1, 1]]))
    \'multilabel-indicator\'
    '''
    pass
# WARNING: Decompyle incomplete


def _check_partial_fit_first_call(clf, classes = (None,)):
    '''Private helper function for factorizing common classes param logic.

    Estimators that implement the ``partial_fit`` API need to be provided with
    the list of possible classes at the first call to partial_fit.

    Subsequent calls to partial_fit should check that ``classes`` is still
    consistent with a previous value of ``clf.classes_`` when provided.

    This function returns True if it detects that this was the first call to
    ``partial_fit`` on ``clf``. In that case the ``classes_`` attribute is also
    set on ``clf``.

    '''
    pass
# WARNING: Decompyle incomplete


def class_distribution(y, sample_weight = (None,)):
    '''Compute class priors from multioutput-multiclass target data.

    Parameters
    ----------
    y : {array-like, sparse matrix} of size (n_samples, n_outputs)
        The labels for each example.

    sample_weight : array-like of shape (n_samples,), default=None
        Sample weights.

    Returns
    -------
    classes : list of size n_outputs of ndarray of size (n_classes,)
        List of classes for each column.

    n_classes : list of int of size n_outputs
        Number of classes in each column.

    class_prior : list of size n_outputs of ndarray of size (n_classes,)
        Class distribution of each column.
    '''
    classes = []
    n_classes = []
    class_prior = []
    (n_samples, n_outputs) = y.shape
# WARNING: Decompyle incomplete


def _ovr_decision_function(predictions, confidences, n_classes):
    '''Compute a continuous, tie-breaking OvR decision function from OvO.

    It is important to include a continuous value, not only votes,
    to make computing AUC or calibration meaningful.

    Parameters
    ----------
    predictions : array-like of shape (n_samples, n_classifiers)
        Predicted classes for each binary classifier.

    confidences : array-like of shape (n_samples, n_classifiers)
        Decision functions or predicted probabilities for positive class
        for each binary classifier.

    n_classes : int
        Number of classes. n_classifiers must be
        ``n_classes * (n_classes - 1 ) / 2``.
    '''
    n_samples = predictions.shape[0]
    votes = np.zeros((n_samples, n_classes))
    sum_of_confidences = np.zeros((n_samples, n_classes))
    k = 0
    for i in range(n_classes):
        for j in range(i + 1, n_classes):
            k += 1 = None
            transformed_confidences = sum_of_confidences / (3 * (np.abs(sum_of_confidences) + 1))
            return votes + transformed_confidences
