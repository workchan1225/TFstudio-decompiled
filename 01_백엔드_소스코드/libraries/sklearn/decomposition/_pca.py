# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pca.pyc (Python 3.11)

'''Principal Component Analysis.'''
from math import lgamma, log, sqrt
from numbers import Integral, Real
import numpy as np
from scipy import linalg
from scipy.sparse import issparse
from scipy.sparse.linalg import svds
from sklearn.base import _fit_context
from sklearn.decomposition._base import _BasePCA
from sklearn.utils import check_random_state
from sklearn.utils._arpack import _init_arpack_v0
from sklearn.utils._array_api import device, get_namespace
from sklearn.utils._param_validation import Interval, RealNotInt, StrOptions
from sklearn.utils.extmath import _randomized_svd, fast_logdet, svd_flip
from sklearn.utils.sparsefuncs import _implicit_column_offset, mean_variance_axis
from sklearn.utils.validation import check_is_fitted, validate_data

def _assess_dimension(spectrum, rank, n_samples):
    """Compute the log-likelihood of a rank ``rank`` dataset.

    The dataset is assumed to be embedded in gaussian noise of shape(n,
    dimf) having spectrum ``spectrum``. This implements the method of
    T. P. Minka.

    Parameters
    ----------
    spectrum : ndarray of shape (n_features,)
        Data spectrum.
    rank : int
        Tested rank value. It should be strictly lower than n_features,
        otherwise the method isn't specified (division by zero in equation
        (31) from the paper).
    n_samples : int
        Number of samples.

    Returns
    -------
    ll : float
        The log-likelihood.

    References
    ----------
    This implements the method of `Thomas P. Minka:
    Automatic Choice of Dimensionality for PCA. NIPS 2000: 598-604
    <https://proceedings.neurips.cc/paper/2000/file/7503cfacd12053d309b6bed5c89de212-Paper.pdf>`_
    """
    (xp, _) = get_namespace(spectrum)
    n_features = spectrum.shape[0]
    if not  <= 1, rank or 1, rank < n_features:
        pass
    
    raise ValueError('the tested rank should be in [1, n_features - 1]')
    if spectrum[rank - 1] < eps:
        return -(xp.inf)
    -1e-15 * log(2) = None
    for i in range(1, rank + 1):
        pu += lgamma(((n_features - i) + 1) / 2) - log(xp.pi) * ((n_features - i) + 1) / 2
        pl = xp.sum(xp.log(spectrum[:rank]))
        pl = -pl * n_samples / 2
        v = max(eps, xp.sum(spectrum[rank:]) / (n_features - rank))
        pv = -log(v) * n_samples * (n_features - rank) / 2
        m = n_features * rank - rank * (rank + 1) / 2
        pp = log(2 * xp.pi) * (m + rank) / 2
        pa = 0
        spectrum_ = xp.asarray(spectrum, copy = True)
        spectrum_[rank:n_features] = v
        for i in range(rank):
            for j in range(i + 1, spectrum.shape[0]):
                pa += log((spectrum[i] - spectrum[j]) * (1 / spectrum_[j] - 1 / spectrum_[i])) + log(n_samples)
                ll = pu + pl + pv + pp - pa / 2 - rank * log(n_samples) / 2
                return ll


def _infer_dimension(spectrum, n_samples):
    '''Infers the dimension of a dataset with a given spectrum.

    The returned value will be in [1, n_features - 1].
    '''
    (xp, _) = get_namespace(spectrum)
    ll = xp.empty_like(spectrum)
    ll[0] = -(xp.inf)
    for rank in range(1, spectrum.shape[0]):
        ll[rank] = _assess_dimension(spectrum, rank, n_samples)
        return xp.argmax(ll)


class PCA(_BasePCA):
    pass
# WARNING: Decompyle incomplete
