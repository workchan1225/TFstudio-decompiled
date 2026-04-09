# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

'''Principal Component Analysis Base Classes'''
from abc import ABCMeta, abstractmethod
import numpy as np
from scipy import linalg
from sklearn.base import BaseEstimator, ClassNamePrefixFeaturesOutMixin, TransformerMixin
from sklearn.utils._array_api import _add_to_diagonal, device, get_namespace
from sklearn.utils.validation import check_array, check_is_fitted, validate_data

def _BasePCA():
    '''_BasePCA'''
    __doc__ = 'Base class for PCA methods.\n\n    Warning: This class should not be used directly.\n    Use derived classes instead.\n    '
    
    def get_covariance(self):
        '''Compute data covariance with the generative model.

        ``cov = components_.T * S**2 * components_ + sigma2 * eye(n_features)``
        where S**2 contains the explained variances, and sigma2 contains the
        noise variances.

        Returns
        -------
        cov : array of shape=(n_features, n_features)
            Estimated covariance of data.
        '''
        (xp, _) = get_namespace(self.components_)
        components_ = self.components_
        exp_var = self.explained_variance_
        if self.whiten:
            components_ = components_ * xp.sqrt(exp_var[(:, np.newaxis)])
        exp_var_diff = exp_var - self.noise_variance_
        exp_var_diff = xp.where(exp_var > self.noise_variance_, exp_var_diff, xp.asarray(0, device = device(exp_var), dtype = exp_var.dtype))
        cov = components_.T * exp_var_diff @ components_
        _add_to_diagonal(cov, self.noise_variance_, xp)
        return cov

    
    def get_precision(self):
        '''Compute data precision matrix with the generative model.

        Equals the inverse of the covariance but computed with
        the matrix inversion lemma for efficiency.

        Returns
        -------
        precision : array, shape=(n_features, n_features)
            Estimated precision of data.
        '''
        (xp, is_array_api_compliant) = get_namespace(self.components_)
        n_features = self.components_.shape[1]
        if self.n_components_ == 0:
            return xp.eye(n_features) / self.noise_variance_
        if None:
            linalg_inv = xp.linalg.inv
        else:
            linalg_inv = linalg.inv
        if self.noise_variance_ == 0:
            return linalg_inv(self.get_covariance())
        components_ = None.components_
        exp_var = self.explained_variance_
        if self.whiten:
            components_ = components_ * xp.sqrt(exp_var[(:, np.newaxis)])
        exp_var_diff = exp_var - self.noise_variance_
        exp_var_diff = xp.where(exp_var > self.noise_variance_, exp_var_diff, xp.asarray(0, device = device(exp_var)))
        precision = (components_ @ components_.T) / self.noise_variance_
        _add_to_diagonal(precision, 1 / exp_var_diff, xp)
        precision = components_.T @ linalg_inv(precision) @ components_
        precision /= -self.noise_variance_ ** 2
        _add_to_diagonal(precision, 1 / self.noise_variance_, xp)
        return precision

    fit = (lambda self, X, y = (None,): pass)()
    
    def transform(self, X):
        '''Apply dimensionality reduction to X.

        X is projected on the first principal components previously extracted
        from a training set.

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            New data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        Returns
        -------
        X_new : array-like of shape (n_samples, n_components)
            Projection of X in the first principal components, where `n_samples`
            is the number of samples and `n_components` is the number of the components.
        '''
        (xp, _) = get_namespace(X, self.components_, self.explained_variance_)
        check_is_fitted(self)
        X = validate_data(self, X, dtype = [
            xp.float64,
            xp.float32], accept_sparse = ('csr', 'csc'), reset = False)
        return self._transform(X, xp = xp, x_is_centered = False)

    
    def _transform(self, X, xp, x_is_centered = (False,)):
        X_transformed = X @ self.components_.T
        if not x_is_centered:
            X_transformed -= xp.reshape(self.mean_, (1, -1)) @ self.components_.T
        if self.whiten:
            scale = xp.sqrt(self.explained_variance_)
            min_scale = xp.finfo(scale.dtype).eps
            scale[scale < min_scale] = min_scale
            X_transformed /= scale
        return X_transformed

    
    def inverse_transform(self, X):
        '''Transform data back to its original space.

        In other words, return an input `X_original` whose transform would be X.

        Parameters
        ----------
        X : array-like of shape (n_samples, n_components)
            New data, where `n_samples` is the number of samples
            and `n_components` is the number of components.

        Returns
        -------
        X_original : array-like of shape (n_samples, n_features)
            Original data, where `n_samples` is the number of samples
            and `n_features` is the number of features.

        Notes
        -----
        If whitening is enabled, inverse_transform will compute the
        exact inverse operation, which includes reversing whitening.
        '''
        (xp, _) = get_namespace(X, self.components_, self.explained_variance_)
        check_is_fitted(self)
        X = check_array(X, input_name = 'X', dtype = [
            xp.float64,
            xp.float32])
        if self.whiten:
            scaled_components = xp.sqrt(self.explained_variance_[(:, np.newaxis)]) * self.components_
            return (X @ scaled_components) + self.mean_
        return (None @ self.components_) + self.mean_

    _n_features_out = (lambda self: self.components_.shape[0])()

_BasePCA = <NODE:27>(_BasePCA, '_BasePCA', ClassNamePrefixFeaturesOutMixin, TransformerMixin, BaseEstimator, metaclass = ABCMeta)
