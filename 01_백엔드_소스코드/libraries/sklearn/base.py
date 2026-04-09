# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Base classes for all estimators and various utility functions.'''
import copy
import functools
import inspect
import platform
import re
import warnings
from collections import defaultdict
import numpy as np
from sklearn import __version__
from sklearn._config import config_context, get_config
from sklearn.exceptions import InconsistentVersionWarning
from sklearn.utils._metadata_requests import _MetadataRequester, _routing_enabled
from sklearn.utils._missing import is_pandas_na, is_scalar_nan
from sklearn.utils._param_validation import validate_parameter_constraints
from sklearn.utils._repr_html.base import ReprHTMLMixin, _HTMLDocumentationLinkMixin
from sklearn.utils._repr_html.estimator import estimator_html_repr
from sklearn.utils._repr_html.params import ParamsDict
from sklearn.utils._set_output import _SetOutputMixin
from sklearn.utils._tags import ClassifierTags, RegressorTags, Tags, TargetTags, TransformerTags, get_tags
from sklearn.utils.fixes import _IS_32BIT
from sklearn.utils.validation import _check_feature_names_in, _generate_get_feature_names_out, _is_fitted, check_array, check_is_fitted

def clone(estimator = None, *, safe):
    '''Construct a new unfitted estimator with the same parameters.

    Clone does a deep copy of the model in an estimator
    without actually copying attached data. It returns a new estimator
    with the same parameters that has not been fitted on any data.

    .. versionchanged:: 1.3
        Delegates to `estimator.__sklearn_clone__` if the method exists.

    Parameters
    ----------
    estimator : {list, tuple, set} of estimator instance or a single             estimator instance
        The estimator or group of estimators to be cloned.
    safe : bool, default=True
        If safe is False, clone will fall back to a deep copy on objects
        that are not estimators. Ignored if `estimator.__sklearn_clone__`
        exists.

    Returns
    -------
    estimator : object
        The deep copy of the input, an estimator if input is an estimator.

    Notes
    -----
    If the estimator\'s `random_state` parameter is an integer (or if the
    estimator doesn\'t have a `random_state` parameter), an *exact clone* is
    returned: the clone and the original estimator will give the exact same
    results. Otherwise, *statistical clone* is returned: the clone might
    return different results from the original estimator. More details can be
    found in :ref:`randomness`.

    Examples
    --------
    >>> from sklearn.base import clone
    >>> from sklearn.linear_model import LogisticRegression
    >>> X = [[-1, 0], [0, 1], [0, -1], [1, 0]]
    >>> y = [0, 0, 1, 1]
    >>> classifier = LogisticRegression().fit(X, y)
    >>> cloned_classifier = clone(classifier)
    >>> hasattr(classifier, "classes_")
    True
    >>> hasattr(cloned_classifier, "classes_")
    False
    >>> classifier is cloned_classifier
    False
    '''
    if not hasattr(estimator, '__sklearn_clone__') and inspect.isclass(estimator):
        return estimator.__sklearn_clone__()
    return None(estimator, safe = safe)


def _clone_parametrized(estimator = None, *, safe):
    '''Default implementation of clone. See :func:`sklearn.base.clone` for details.'''
    pass
# WARNING: Decompyle incomplete


class BaseEstimator(_MetadataRequester, _HTMLDocumentationLinkMixin, ReprHTMLMixin):
    pass
# WARNING: Decompyle incomplete


class ClassifierMixin:
    pass
# WARNING: Decompyle incomplete


class RegressorMixin:
    pass
# WARNING: Decompyle incomplete


class ClusterMixin:
    pass
# WARNING: Decompyle incomplete


class BiclusterMixin:
    '''Mixin class for all bicluster estimators in scikit-learn.

    This mixin defines the following functionality:

    - `biclusters_` property that returns the row and column indicators;
    - `get_indices` method that returns the row and column indices of a bicluster;
    - `get_shape` method that returns the shape of a bicluster;
    - `get_submatrix` method that returns the submatrix corresponding to a bicluster.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.base import BaseEstimator, BiclusterMixin
    >>> class DummyBiClustering(BiclusterMixin, BaseEstimator):
    ...     def fit(self, X, y=None):
    ...         self.rows_ = np.ones(shape=(1, X.shape[0]), dtype=bool)
    ...         self.columns_ = np.ones(shape=(1, X.shape[1]), dtype=bool)
    ...         return self
    >>> X = np.array([[1, 1], [2, 1], [1, 0],
    ...               [4, 7], [3, 5], [3, 6]])
    >>> bicluster = DummyBiClustering().fit(X)
    >>> hasattr(bicluster, "biclusters_")
    True
    >>> bicluster.get_indices(0)
    (array([0, 1, 2, 3, 4, 5]), array([0, 1]))
    '''
    biclusters_ = (lambda self: (self.rows_, self.columns_))()
    
    def get_indices(self, i):
        """Row and column indices of the `i`'th bicluster.

        Only works if ``rows_`` and ``columns_`` attributes exist.

        Parameters
        ----------
        i : int
            The index of the cluster.

        Returns
        -------
        row_ind : ndarray, dtype=np.intp
            Indices of rows in the dataset that belong to the bicluster.
        col_ind : ndarray, dtype=np.intp
            Indices of columns in the dataset that belong to the bicluster.
        """
        rows = self.rows_[i]
        columns = self.columns_[i]
        return (np.nonzero(rows)[0], np.nonzero(columns)[0])

    
    def get_shape(self, i):
        """Shape of the `i`'th bicluster.

        Parameters
        ----------
        i : int
            The index of the cluster.

        Returns
        -------
        n_rows : int
            Number of rows in the bicluster.

        n_cols : int
            Number of columns in the bicluster.
        """
        indices = self.get_indices(i)
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(indices())

    
    def get_submatrix(self, i, data):
        '''Return the submatrix corresponding to bicluster `i`.

        Parameters
        ----------
        i : int
            The index of the cluster.
        data : array-like of shape (n_samples, n_features)
            The data.

        Returns
        -------
        submatrix : ndarray of shape (n_rows, n_cols)
            The submatrix corresponding to bicluster `i`.

        Notes
        -----
        Works with sparse matrices. Only works if ``rows_`` and
        ``columns_`` attributes exist.
        '''
        data = check_array(data, accept_sparse = 'csr')
        (row_ind, col_ind) = self.get_indices(i)
        return data[(row_ind[(:, np.newaxis)], col_ind)]



class TransformerMixin(_SetOutputMixin):
    pass
# WARNING: Decompyle incomplete


class OneToOneFeatureMixin:
    """Provides `get_feature_names_out` for simple transformers.

    This mixin assumes there's a 1-to-1 correspondence between input features
    and output features, such as :class:`~sklearn.preprocessing.StandardScaler`.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.base import OneToOneFeatureMixin, BaseEstimator
    >>> class MyEstimator(OneToOneFeatureMixin, BaseEstimator):
    ...     def fit(self, X, y=None):
    ...         self.n_features_in_ = X.shape[1]
    ...         return self
    >>> X = np.array([[1, 2], [3, 4]])
    >>> MyEstimator().fit(X).get_feature_names_out()
    array(['x0', 'x1'], dtype=object)
    """
    
    def get_feature_names_out(self, input_features = (None,)):
        '''Get output feature names for transformation.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Input features.

            - If `input_features` is `None`, then `feature_names_in_` is
              used as feature names in. If `feature_names_in_` is not defined,
              then the following input feature names are generated:
              `["x0", "x1", ..., "x(n_features_in_ - 1)"]`.
            - If `input_features` is an array-like, then `input_features` must
              match `feature_names_in_` if `feature_names_in_` is defined.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Same as input features.
        '''
        check_is_fitted(self, attributes = 'n_features_in_')
        return _check_feature_names_in(self, input_features)



class ClassNamePrefixFeaturesOutMixin:
    '''Mixin class for transformers that generate their own names by prefixing.

    This mixin is useful when the transformer needs to generate its own feature
    names out, such as :class:`~sklearn.decomposition.PCA`. For example, if
    :class:`~sklearn.decomposition.PCA` outputs 3 features, then the generated feature
    names out are: `["pca0", "pca1", "pca2"]`.

    This mixin assumes that a `_n_features_out` attribute is defined when the
    transformer is fitted. `_n_features_out` is the number of output features
    that the transformer will return in `transform` of `fit_transform`.

    Examples
    --------
    >>> import numpy as np
    >>> from sklearn.base import ClassNamePrefixFeaturesOutMixin, BaseEstimator
    >>> class MyEstimator(ClassNamePrefixFeaturesOutMixin, BaseEstimator):
    ...     def fit(self, X, y=None):
    ...         self._n_features_out = X.shape[1]
    ...         return self
    >>> X = np.array([[1, 2], [3, 4]])
    >>> MyEstimator().fit(X).get_feature_names_out()
    array([\'myestimator0\', \'myestimator1\'], dtype=object)
    '''
    
    def get_feature_names_out(self, input_features = (None,)):
        '''Get output feature names for transformation.

        The feature names out will prefixed by the lowercased class name. For
        example, if the transformer outputs 3 features, then the feature names
        out are: `["class_name0", "class_name1", "class_name2"]`.

        Parameters
        ----------
        input_features : array-like of str or None, default=None
            Only used to validate feature names with the names seen in `fit`.

        Returns
        -------
        feature_names_out : ndarray of str objects
            Transformed feature names.
        '''
        check_is_fitted(self, '_n_features_out')
        return _generate_get_feature_names_out(self, self._n_features_out, input_features = input_features)



class DensityMixin:
    pass
# WARNING: Decompyle incomplete


class OutlierMixin:
    pass
# WARNING: Decompyle incomplete


class MetaEstimatorMixin:
    """Mixin class for all meta estimators in scikit-learn.

    This mixin is empty, and only exists to indicate that the estimator is a
    meta-estimator.

    .. versionchanged:: 1.6
        The `_required_parameters` is now removed and is unnecessary since tests are
        refactored and don't use this anymore.

    Examples
    --------
    >>> from sklearn.base import MetaEstimatorMixin
    >>> from sklearn.datasets import load_iris
    >>> from sklearn.linear_model import LogisticRegression
    >>> class MyEstimator(MetaEstimatorMixin):
    ...     def __init__(self, *, estimator=None):
    ...         self.estimator = estimator
    ...     def fit(self, X, y=None):
    ...         if self.estimator is None:
    ...             self.estimator_ = LogisticRegression()
    ...         else:
    ...             self.estimator_ = self.estimator
    ...         return self
    >>> X, y = load_iris(return_X_y=True)
    >>> estimator = MyEstimator().fit(X, y)
    >>> estimator.estimator_
    LogisticRegression()
    """
    pass


class MultiOutputMixin:
    pass
# WARNING: Decompyle incomplete


class _UnstableArchMixin:
    pass
# WARNING: Decompyle incomplete


def is_classifier(estimator):
    '''Return True if the given estimator is (probably) a classifier.

    Parameters
    ----------
    estimator : estimator instance
        Estimator object to test.

    Returns
    -------
    out : bool
        True if estimator is a classifier and False otherwise.

    Examples
    --------
    >>> from sklearn.base import is_classifier
    >>> from sklearn.cluster import KMeans
    >>> from sklearn.svm import SVC, SVR
    >>> classifier = SVC()
    >>> regressor = SVR()
    >>> kmeans = KMeans()
    >>> is_classifier(classifier)
    True
    >>> is_classifier(regressor)
    False
    >>> is_classifier(kmeans)
    False
    '''
    return get_tags(estimator).estimator_type == 'classifier'


def is_regressor(estimator):
    '''Return True if the given estimator is (probably) a regressor.

    Parameters
    ----------
    estimator : estimator instance
        Estimator object to test.

    Returns
    -------
    out : bool
        True if estimator is a regressor and False otherwise.

    Examples
    --------
    >>> from sklearn.base import is_regressor
    >>> from sklearn.cluster import KMeans
    >>> from sklearn.svm import SVC, SVR
    >>> classifier = SVC()
    >>> regressor = SVR()
    >>> kmeans = KMeans()
    >>> is_regressor(classifier)
    False
    >>> is_regressor(regressor)
    True
    >>> is_regressor(kmeans)
    False
    '''
    return get_tags(estimator).estimator_type == 'regressor'


def is_clusterer(estimator):
    '''Return True if the given estimator is (probably) a clusterer.

    .. versionadded:: 1.6

    Parameters
    ----------
    estimator : estimator instance
        Estimator object to test.

    Returns
    -------
    out : bool
        True if estimator is a clusterer and False otherwise.

    Examples
    --------
    >>> from sklearn.base import is_clusterer
    >>> from sklearn.cluster import KMeans
    >>> from sklearn.svm import SVC, SVR
    >>> classifier = SVC()
    >>> regressor = SVR()
    >>> kmeans = KMeans()
    >>> is_clusterer(classifier)
    False
    >>> is_clusterer(regressor)
    False
    >>> is_clusterer(kmeans)
    True
    '''
    return get_tags(estimator).estimator_type == 'clusterer'


def is_outlier_detector(estimator):
    '''Return True if the given estimator is (probably) an outlier detector.

    Parameters
    ----------
    estimator : estimator instance
        Estimator object to test.

    Returns
    -------
    out : bool
        True if estimator is an outlier detector and False otherwise.
    '''
    return get_tags(estimator).estimator_type == 'outlier_detector'


def _fit_context(*, prefer_skip_nested_validation):
    """Decorator to run the fit methods of estimators within context managers.

    Parameters
    ----------
    prefer_skip_nested_validation : bool
        If True, the validation of parameters of inner estimators or functions
        called during fit will be skipped.

        This is useful to avoid validating many times the parameters passed by the
        user from the public facing API. It's also useful to avoid validating
        parameters that we pass internally to inner functions that are guaranteed to
        be valid by the test suite.

        It should be set to True for most estimators, except for those that receive
        non-validated objects as parameters, such as meta-estimators that are given
        estimator objects.

    Returns
    -------
    decorated_fit : method
        The decorated fit method.
    """
    pass
# WARNING: Decompyle incomplete
