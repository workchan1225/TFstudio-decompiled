# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: kernels.pyc (Python 3.11)

'''A set of kernels that can be combined by operators and used in Gaussian processes.'''
import math
import warnings
from abc import ABCMeta, abstractmethod
from collections import namedtuple
from inspect import signature
import numpy as np
from scipy.spatial.distance import cdist, pdist, squareform
from scipy.special import gamma, kv
from sklearn.base import clone
from sklearn.exceptions import ConvergenceWarning
from sklearn.metrics.pairwise import pairwise_kernels
from sklearn.utils.validation import _num_samples

def _check_length_scale(X, length_scale):
    length_scale = np.squeeze(length_scale).astype(float)
    if np.ndim(length_scale) > 1:
        raise ValueError('length_scale cannot be of dimension greater than 1')
    if np.ndim(length_scale) == 1 and X.shape[1] != length_scale.shape[0]:
        raise ValueError('Anisotropic kernel must have the same number of dimensions as data (%d!=%d)' % (length_scale.shape[0], X.shape[1]))
    return length_scale


def Hyperparameter():
    '''Hyperparameter'''
    pass
# WARNING: Decompyle incomplete

Hyperparameter = <NODE:27>(Hyperparameter, 'Hyperparameter', namedtuple('Hyperparameter', ('name', 'value_type', 'bounds', 'n_elements', 'fixed')))

def Kernel():
    '''Kernel'''
    __doc__ = 'Base class for all kernels.\n\n    .. versionadded:: 0.18\n\n    Examples\n    --------\n    >>> from sklearn.gaussian_process.kernels import Kernel, RBF\n    >>> import numpy as np\n    >>> class CustomKernel(Kernel):\n    ...     def __init__(self, length_scale=1.0):\n    ...         self.length_scale = length_scale\n    ...     def __call__(self, X, Y=None):\n    ...         if Y is None:\n    ...             Y = X\n    ...         return np.inner(X, X if Y is None else Y) ** 2\n    ...     def diag(self, X):\n    ...         return np.ones(X.shape[0])\n    ...     def is_stationary(self):\n    ...         return True\n    >>> kernel = CustomKernel(length_scale=2.0)\n    >>> X = np.array([[1, 2], [3, 4]])\n    >>> print(kernel(X))\n    [[ 25 121]\n     [121 625]]\n    '
    
    def get_params(self, deep = (True,)):
        '''Get parameters of this kernel.

        Parameters
        ----------
        deep : bool, default=True
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : dict
            Parameter names mapped to their values.
        '''
        params = dict()
        cls = self.__class__
        init = getattr(cls.__init__, 'deprecated_original', cls.__init__)
        init_sign = signature(init)
        varargs = []
        args = []
        for parameter in init_sign.parameters.values():
            if parameter.kind != parameter.VAR_KEYWORD and parameter.name != 'self':
                args.append(parameter.name)
            if parameter.kind == parameter.VAR_POSITIONAL:
                varargs.append(parameter.name)
            if len(varargs) != 0:
                raise RuntimeError(f'''scikit-learn kernels should always specify their parameters in the signature of their __init__ (no varargs). {cls!s} doesn\'t follow this convention.''')
            for arg in args:
                params[arg] = getattr(self, arg)
                return params

    
    def set_params(self, **params):
        """Set the parameters of this kernel.

        The method works on simple kernels as well as on nested kernels.
        The latter have parameters of the form ``<component>__<parameter>``
        so that it's possible to update each component of a nested object.

        Returns
        -------
        self
        """
        if not params:
            return self
        valid_params = None.get_params(deep = True)
    # WARNING: Decompyle incomplete

    
    def clone_with_theta(self, theta):
        '''Returns a clone of self with given hyperparameters theta.

        Parameters
        ----------
        theta : ndarray of shape (n_dims,)
            The hyperparameters
        '''
        cloned = clone(self)
        cloned.theta = theta
        return cloned

    n_dims = (lambda self: self.theta.shape[0])()
    hyperparameters = (lambda self: pass# WARNING: Decompyle incomplete
)()
    theta = (lambda self: theta = []params = self.get_params()for hyperparameter in self.hyperparameters:
if not hyperparameter.fixed:
theta.append(params[hyperparameter.name])if len(theta) > 0:
np.log(np.hstack(theta))None.array([]))()
    theta = (lambda self, theta: params = self.get_params()i = 0# WARNING: Decompyle incomplete
)()
    bounds = (lambda self: bounds = self.hyperparameters()if len(bounds) > 0:
np.log(np.vstack(bounds))(lambda .0: pass# WARNING: Decompyle incomplete
).array([])
)()
    
    def __add__(self, b):
        if not isinstance(b, Kernel):
            return Sum(self, ConstantKernel(b))
        return None(self, b)

    
    def __radd__(self, b):
        if not isinstance(b, Kernel):
            return Sum(ConstantKernel(b), self)
        return None(b, self)

    
    def __mul__(self, b):
        if not isinstance(b, Kernel):
            return Product(self, ConstantKernel(b))
        return None(self, b)

    
    def __rmul__(self, b):
        if not isinstance(b, Kernel):
            return Product(ConstantKernel(b), self)
        return None(b, self)

    
    def __pow__(self, b):
        return Exponentiation(self, b)

    
    def __eq__(self, b):
        if type(self) != type(b):
            return False
        params_a = None.get_params()
        params_b = b.get_params()
        for key in set(list(params_a.keys()) + list(params_b.keys())):
            if np.any(params_a.get(key, None) != params_b.get(key, None)):
                return False
            return True

    
    def __repr__(self):
        return '{0}({1})'.format(self.__class__.__name__, ', '.join(map('{0:.3g}'.format, self.theta)))

    __call__ = (lambda self, X, Y, eval_gradient = (None, False): pass)()
    diag = (lambda self, X: pass)()
    is_stationary = (lambda self: pass)()
    requires_vector_input = (lambda self: True)()
    
    def _check_bounds_params(self):
        '''Called after fitting to warn if bounds may have been too tight.'''
        list_close = np.isclose(self.bounds, np.atleast_2d(self.theta).T)
        idx = 0
        for hyp in self.hyperparameters:
            if hyp.fixed:
                continue
            for dim in range(hyp.n_elements):
                if list_close[(idx, 0)]:
                    warnings.warn(f'''The optimal value found for dimension {dim!s} of parameter {hyp.name!s} is close to the specified lower bound {hyp.bounds[dim][0]!s}. Decreasing the bound and calling fit again may find a better value.''', ConvergenceWarning)
                elif list_close[(idx, 1)]:
                    warnings.warn(f'''The optimal value found for dimension {dim!s} of parameter {hyp.name!s} is close to the specified upper bound {hyp.bounds[dim][1]!s}. Increasing the bound and calling fit again may find a better value.''', ConvergenceWarning)
                idx += 1
                return None


Kernel = <NODE:27>(Kernel, 'Kernel', metaclass = ABCMeta)

class NormalizedKernelMixin:
    '''Mixin for kernels which are normalized: k(X, X)=1.

    .. versionadded:: 0.18
    '''
    
    def diag(self, X):
        '''Returns the diagonal of the kernel k(X, X).

        The result of this method is identical to np.diag(self(X)); however,
        it can be evaluated more efficiently since only the diagonal is
        evaluated.

        Parameters
        ----------
        X : ndarray of shape (n_samples_X, n_features)
            Left argument of the returned kernel k(X, Y)

        Returns
        -------
        K_diag : ndarray of shape (n_samples_X,)
            Diagonal of kernel k(X, X)
        '''
        return np.ones(X.shape[0])



class StationaryKernelMixin:
    '''Mixin for kernels which are stationary: k(X, Y)= f(X-Y).

    .. versionadded:: 0.18
    '''
    
    def is_stationary(self):
        '''Returns whether the kernel is stationary.'''
        return True



class GenericKernelMixin:
    '''Mixin for kernels which operate on generic objects such as variable-
    length sequences, trees, and graphs.

    .. versionadded:: 0.22
    '''
    requires_vector_input = (lambda self: False)()


class CompoundKernel(Kernel):
    '''Kernel which is composed of a set of other kernels.

    .. versionadded:: 0.18

    Parameters
    ----------
    kernels : list of Kernels
        The other kernels

    Examples
    --------
    >>> from sklearn.gaussian_process.kernels import WhiteKernel
    >>> from sklearn.gaussian_process.kernels import RBF
    >>> from sklearn.gaussian_process.kernels import CompoundKernel
    >>> kernel = CompoundKernel(
    ...     [WhiteKernel(noise_level=3.0), RBF(length_scale=2.0)])
    >>> print(kernel.bounds)
    [[-11.51292546  11.51292546]
     [-11.51292546  11.51292546]]
    >>> print(kernel.n_dims)
    2
    >>> print(kernel.theta)
    [1.09861229 0.69314718]
    '''
    
    def __init__(self, kernels):
        self.kernels = kernels

    
    def get_params(self, deep = (True,)):
        '''Get parameters of this kernel.

        Parameters
        ----------
        deep : bool, default=True
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : dict
            Parameter names mapped to their values.
        '''
        return dict(kernels = self.kernels)

    theta = (lambda self: (lambda .0: [ kernel.theta for kernel in .0 ])(self.kernels())
)()
    theta = (lambda self, theta: k_dims = self.k1.n_dimsfor i, kernel in enumerate(self.kernels):
kernel.theta = theta[i * k_dims:(i + 1) * k_dims]None)()
    bounds = (lambda self: (lambda .0: [ kernel.bounds for kernel in .0 ])(self.kernels())
)()
    
    def __call__(self, X, Y, eval_gradient = (None, False)):
        '''Return the kernel k(X, Y) and optionally its gradient.

        Note that this compound kernel returns the results of all simple kernel
        stacked along an additional axis.

        Parameters
        ----------
        X : array-like of shape (n_samples_X, n_features) or list of object,             default=None
            Left argument of the returned kernel k(X, Y)

        Y : array-like of shape (n_samples_X, n_features) or list of object,             default=None
            Right argument of the returned kernel k(X, Y). If None, k(X, X)
            is evaluated instead.

        eval_gradient : bool, default=False
            Determines whether the gradient with respect to the log of the
            kernel hyperparameter is computed.

        Returns
        -------
        K : ndarray of shape (n_samples_X, n_samples_Y, n_kernels)
            Kernel k(X, Y)

        K_gradient : ndarray of shape                 (n_samples_X, n_samples_X, n_dims, n_kernels), optional
            The gradient of the kernel k(X, X) with respect to the log of the
            hyperparameter of the kernel. Only returned when `eval_gradient`
            is True.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, b):
        pass
    # WARNING: Decompyle incomplete

    
    def is_stationary(self):
        '''Returns whether the kernel is stationary.'''
        return (lambda .0: [ kernel.is_stationary() for kernel in .0 ])(self.kernels())

    requires_vector_input = (lambda self: (lambda .0: [ kernel.requires_vector_input for kernel in .0 ])(self.kernels())
)()
    
    def diag(self, X):
        '''Returns the diagonal of the kernel k(X, X).

        The result of this method is identical to `np.diag(self(X))`; however,
        it can be evaluated more efficiently since only the diagonal is
        evaluated.

        Parameters
        ----------
        X : array-like of shape (n_samples_X, n_features) or list of object
            Argument to the kernel.

        Returns
        -------
        K_diag : ndarray of shape (n_samples_X, n_kernels)
            Diagonal of kernel k(X, X)
        '''
        pass
    # WARNING: Decompyle incomplete



class KernelOperator(Kernel):
    '''Base class for all kernel operators.

    .. versionadded:: 0.18
    '''
    
    def __init__(self, k1, k2):
        self.k1 = k1
        self.k2 = k2

    
    def get_params(self, deep = (True,)):
        '''Get parameters of this kernel.

        Parameters
        ----------
        deep : bool, default=True
            If True, will return the parameters for this estimator and
            contained subobjects that are estimators.

        Returns
        -------
        params : dict
            Parameter names mapped to their values.
        '''
        params = dict(k1 = self.k1, k2 = self.k2)
        if deep:
            deep_items = self.k1.get_params().items()
            (lambda .0: pass# WARNING: Decompyle incomplete
)(deep_items())
            deep_items = self.k2.get_params().items()
            (lambda .0: pass# WARNING: Decompyle incomplete
)(deep_items())
        return params

    hyperparameters = (lambda self: r = self.k1.hyperparameters()for hyperparameter in self.k2.hyperparameters:
r.append(Hyperparameter('k2__' + hyperparameter.name, hyperparameter.value_type, hyperparameter.bounds, hyperparameter.n_elements))r)()
    theta = (lambda self: np.append(self.k1.theta, self.k2.theta))()
    theta = (lambda self, theta: k1_dims = self.k1.n_dimsself.k1.theta = theta[:k1_dims]self.k2.theta = theta[k1_dims:])()
    bounds = (lambda self: if self.k1.bounds.size == 0:
self.k2.boundsif None.k2.bounds.size == 0:
self.k1.boundsNone.vstack((self.k1.bounds, self.k2.bounds)))()
    
    def __eq__(self, b):
