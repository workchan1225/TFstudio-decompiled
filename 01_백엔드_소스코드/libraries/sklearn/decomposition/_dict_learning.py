# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dict_learning.pyc (Python 3.11)

'''Dictionary learning.'''
import itertools
import sys
import time
from numbers import Integral, Real
import numpy as np
from joblib import effective_n_jobs
from scipy import linalg
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin, _fit_context
from sklearn.linear_model import Lars, Lasso, LassoLars, orthogonal_mp_gram
from sklearn.utils import check_array, check_random_state, gen_batches, gen_even_slices
from sklearn.utils._param_validation import Interval, StrOptions, validate_params
from sklearn.utils.extmath import _randomized_svd, row_norms, svd_flip
from sklearn.utils.parallel import Parallel, delayed
from sklearn.utils.validation import check_is_fitted, validate_data

def _check_positive_coding(method, positive):
    if positive or method in ('omp', 'lars'):
        raise ValueError("Positive constraint not supported for '{}' coding method.".format(method))
    return None


def _sparse_encode_precomputed(X = None, dictionary = {
    'gram': None,
    'cov': None,
    'algorithm': 'lasso_lars',
    'regularization': None,
    'copy_cov': True,
    'init': None,
    'max_iter': 1000,
    'verbose': 0,
    'positive': False }, *, gram, cov, algorithm, regularization, copy_cov, init, max_iter, verbose, positive):
    """Generic sparse coding with precomputed Gram and/or covariance matrices.

    Each row of the result is the solution to a Lasso problem.

    Parameters
    ----------
    X : ndarray of shape (n_samples, n_features)
        Data matrix.

    dictionary : ndarray of shape (n_components, n_features)
        The dictionary matrix against which to solve the sparse coding of
        the data. Some of the algorithms assume normalized rows.

    gram : ndarray of shape (n_components, n_components), default=None
        Precomputed Gram matrix, `dictionary * dictionary'`
        gram can be `None` if method is 'threshold'.

    cov : ndarray of shape (n_components, n_samples), default=None
        Precomputed covariance, `dictionary * X'`.

    algorithm : {'lasso_lars', 'lasso_cd', 'lars', 'omp', 'threshold'},             default='lasso_lars'
        The algorithm used:

        * `'lars'`: uses the least angle regression method
          (`linear_model.lars_path`);
        * `'lasso_lars'`: uses Lars to compute the Lasso solution;
        * `'lasso_cd'`: uses the coordinate descent method to compute the
          Lasso solution (`linear_model.Lasso`). lasso_lars will be faster if
          the estimated components are sparse;
        * `'omp'`: uses orthogonal matching pursuit to estimate the sparse
          solution;
        * `'threshold'`: squashes to zero all coefficients less than
          regularization from the projection `dictionary * data'`.

    regularization : int or float, default=None
        The regularization parameter. It corresponds to alpha when
        algorithm is `'lasso_lars'`, `'lasso_cd'` or `'threshold'`.
        Otherwise it corresponds to `n_nonzero_coefs`.

    init : ndarray of shape (n_samples, n_components), default=None
        Initialization value of the sparse code. Only used if
        `algorithm='lasso_cd'`.

    max_iter : int, default=1000
        Maximum number of iterations to perform if `algorithm='lasso_cd'` or
        `'lasso_lars'`.

    copy_cov : bool, default=True
        Whether to copy the precomputed covariance matrix; if `False`, it may
        be overwritten.

    verbose : int, default=0
        Controls the verbosity; the higher, the more messages.

    positive: bool, default=False
        Whether to enforce a positivity constraint on the sparse code.

        .. versionadded:: 0.20

    Returns
    -------
    code : ndarray of shape (n_components, n_features)
        The sparse codes.
    """
    (n_samples, n_features) = X.shape
    n_components = dictionary.shape[0]
# WARNING: Decompyle incomplete

sparse_encode = (lambda X = validate_params({
    'X': [
        'array-like'],
    'dictionary': [
        'array-like'],
    'gram': [
        'array-like',
        None],
    'cov': [
        'array-like',
        None],
    'algorithm': [
        StrOptions({
            'omp',
            'lars',
            'lasso_cd',
            'threshold',
            'lasso_lars'})],
    'n_nonzero_coefs': [
        Interval(Integral, 1, None, closed = 'left'),
        None],
    'alpha': [
        Interval(Real, 0, None, closed = 'left'),
        None],
    'copy_cov': [
        'boolean'],
    'init': [
        'array-like',
        None],
    'max_iter': [
        Interval(Integral, 0, None, closed = 'left')],
    'n_jobs': [
        Integral,
        None],
    'check_input': [
        'boolean'],
    'verbose': [
        'verbose'],
    'positive': [
        'boolean'] }, prefer_skip_nested_validation = True), dictionary = {
    'gram': None,
    'cov': None,
    'algorithm': 'lasso_lars',
    'n_nonzero_coefs': None,
    'alpha': None,
    'copy_cov': True,
    'init': None,
    'max_iter': 1000,
    'n_jobs': None,
    'check_input': True,
    'verbose': 0,
    'positive': False }, *, gram, cov: if check_input:
order = 'C' if algorithm == 'lasso_cd' else Nonedictionary = check_array(dictionary, order = order, dtype = [
np.float64,
np.float32])X = check_array(X, order = order, dtype = [
np.float64,
np.float32])if dictionary.shape[1] != X.shape[1]:
raise ValueError('Dictionary and X have different numbers of features:dictionary.shape: {} X.shape{}'.format(dictionary.shape, X.shape))_check_positive_coding(algorithm, positive)_sparse_encode(X, dictionary, gram = gram, cov = cov, algorithm = algorithm, n_nonzero_coefs = n_nonzero_coefs, alpha = alpha, copy_cov = copy_cov, init = init, max_iter = max_iter, n_jobs = n_jobs, verbose = verbose, positive = positive))()

def _sparse_encode(X = None, dictionary = {
    'gram': None,
    'cov': None,
    'algorithm': 'lasso_lars',
    'n_nonzero_coefs': None,
    'alpha': None,
    'copy_cov': True,
    'init': None,
    'max_iter': 1000,
    'n_jobs': None,
    'verbose': 0,
    'positive': False }, *, gram, cov, algorithm, n_nonzero_coefs, alpha, copy_cov, init, max_iter, n_jobs, verbose, positive):
    '''Sparse coding without input/parameter validation.'''
    pass
# WARNING: Decompyle incomplete


def _update_dict(dictionary, Y, code, A, B, verbose, random_state, positive = (None, None, False, None, False)):
    '''Update the dense dictionary factor in place.

    Parameters
    ----------
    dictionary : ndarray of shape (n_components, n_features)
        Value of the dictionary at the previous iteration.

    Y : ndarray of shape (n_samples, n_features)
        Data matrix.

    code : ndarray of shape (n_samples, n_components)
        Sparse coding of the data against which to optimize the dictionary.

    A : ndarray of shape (n_components, n_components), default=None
        Together with `B`, sufficient stats of the online model to update the
        dictionary.

    B : ndarray of shape (n_features, n_components), default=None
        Together with `A`, sufficient stats of the online model to update the
        dictionary.

    verbose: bool, default=False
        Degree of output the procedure will print.

    random_state : int, RandomState instance or None, default=None
        Used for randomly initializing the dictionary. Pass an int for
        reproducible results across multiple function calls.
        See :term:`Glossary <random_state>`.

    positive : bool, default=False
        Whether to enforce positivity when finding the dictionary.

        .. versionadded:: 0.20
    '''
    (n_samples, n_components) = code.shape
    random_state = check_random_state(random_state)
# WARNING: Decompyle incomplete


def _dict_learning(X, n_components, *, alpha, max_iter, tol, method, n_jobs, dict_init, code_init, callback, verbose, random_state, return_n_iter, positive_dict, positive_code, method_max_iter):
    '''Main dictionary learning algorithm'''
    t0 = time.time()
# WARNING: Decompyle incomplete

dict_learning_online = (lambda X = validate_params({
    'X': [
        'array-like'],
    'return_code': [
        'boolean'],
    'method': [
        StrOptions({
            'cd',
            'lars'})],
    'method_max_iter': [
        Interval(Integral, 0, None, closed = 'left')] }, prefer_skip_nested_validation = False), n_components = (2,), *, alpha, max_iter: transform_algorithm = 'lasso_' + method# WARNING: Decompyle incomplete
)()
dict_learning = (lambda X = validate_params({
    'X': [
        'array-like'],
    'method': [
        StrOptions({
            'lars',
            'cd'})],
    'return_n_iter': [
        'boolean'],
    'method_max_iter': [
        Interval(Integral, 0, None, closed = 'left')] }, prefer_skip_nested_validation = False), n_components = {
    'max_iter': 100,
    'tol': 1e-08,
    'method': 'lars',
    'n_jobs': None,
    'dict_init': None,
    'code_init': None,
    'callback': None,
    'verbose': False,
    'random_state': None,
    'return_n_iter': False,
    'positive_dict': False,
    'positive_code': False,
    'method_max_iter': 1000 }, *, alpha, max_iter: estimator = DictionaryLearning(n_components = n_components, alpha = alpha, max_iter = max_iter, tol = tol, fit_algorithm = method, n_jobs = n_jobs, dict_init = dict_init, callback = callback, code_init = code_init, verbose = verbose, random_state = random_state, positive_code = positive_code, positive_dict = positive_dict, transform_max_iter = method_max_iter).set_output(transform = 'default')code = estimator.fit_transform(X)if return_n_iter:
(code, estimator.components_, estimator.error_, estimator.n_iter_)(None, estimator.components_, estimator.error_))()

class _BaseSparseCoding(TransformerMixin, ClassNamePrefixFeaturesOutMixin):
    '''Base class from SparseCoder and DictionaryLearning algorithms.'''
    
    def __init__(self, transform_algorithm, transform_n_nonzero_coefs, transform_alpha, split_sign, n_jobs, positive_code, transform_max_iter):
        self.transform_algorithm = transform_algorithm
        self.transform_n_nonzero_coefs = transform_n_nonzero_coefs
        self.transform_alpha = transform_alpha
        self.transform_max_iter = transform_max_iter
        self.split_sign = split_sign
        self.n_jobs = n_jobs
        self.positive_code = positive_code

    
    def _transform(self, X, dictionary):
        '''Private method allowing to accommodate both DictionaryLearning and
        SparseCoder.'''
        X = validate_data(self, X, reset = False)
    # WARNING: Decompyle incomplete

    
    def transform(self, X):
        '''Encode the data as a sparse combination of the dictionary atoms.

        Coding method is determined by the object parameter
        `transform_algorithm`.

        Parameters
        ----------
        X : ndarray of shape (n_samples, n_features)
            Test data to be transformed, must have the same number of
            features as the data used to train the model.

        Returns
        -------
        X_new : ndarray of shape (n_samples, n_components)
            Transformed data.
        '''
        check_is_fitted(self)
        return self._transform(X, self.components_)

    
    def _inverse_transform(self, code, dictionary):
        '''Private method allowing to accommodate both DictionaryLearning and
        SparseCoder.'''
        code = check_array(code)
        expected_n_components = dictionary.shape[0]
        if self.split_sign:
            expected_n_components += expected_n_components
        if not code.shape[1] == expected_n_components:
            raise ValueError(f'''The number of components in the code is different from the number of components in the dictionary.Expected {expected_n_components}, got {code.shape[1]}.''')
        if self.split_sign:
            (n_samples, n_features) = code.shape
            n_features //= 2
            code = code[(:, :n_features)] - code[(:, n_features:)]
        return code @ dictionary

    
    def inverse_transform(self, X):
        '''Transform data back to its original space.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_components)
            Data to be transformed back. Must have the same number of
            components as the data used to train the model.

        Returns
        -------
        X_original : ndarray of shape (n_samples, n_features)
            Transformed data.
        '''
        check_is_fitted(self)
        return self._inverse_transform(X, self.components_)



class SparseCoder(BaseEstimator, _BaseSparseCoding):
    pass
# WARNING: Decompyle incomplete


class DictionaryLearning(BaseEstimator, _BaseSparseCoding):
    pass
# WARNING: Decompyle incomplete


class MiniBatchDictionaryLearning(BaseEstimator, _BaseSparseCoding):
    pass
# WARNING: Decompyle incomplete
