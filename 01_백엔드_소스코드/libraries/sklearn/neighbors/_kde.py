# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _kde.pyc (Python 3.11)

'''
Kernel Density Estimation
-------------------------
'''
import itertools
from numbers import Integral, Real
import numpy as np
from scipy.special import gammainc
from sklearn.base import BaseEstimator, _fit_context
from sklearn.neighbors._ball_tree import BallTree
from sklearn.neighbors._base import VALID_METRICS
from sklearn.neighbors._kd_tree import KDTree
from sklearn.utils import check_random_state
from sklearn.utils._param_validation import Interval, StrOptions
from sklearn.utils.extmath import row_norms
from sklearn.utils.validation import _check_sample_weight, check_is_fitted, validate_data
VALID_KERNELS = [
    'gaussian',
    'tophat',
    'epanechnikov',
    'exponential',
    'linear',
    'cosine']
TREE_DICT = {
    'ball_tree': BallTree,
    'kd_tree': KDTree }

class KernelDensity(BaseEstimator):
    __module__ = __name__
    __qualname__ = 'KernelDensity'
    __doc__ = 'Kernel Density Estimation.\n\n    Read more in the :ref:`User Guide <kernel_density>`.\n\n    Parameters\n    ----------\n    bandwidth : float or {"scott", "silverman"}, default=1.0\n        The bandwidth of the kernel. If bandwidth is a float, it defines the\n        bandwidth of the kernel. If bandwidth is a string, one of the estimation\n        methods is implemented.\n\n    algorithm : {\'kd_tree\', \'ball_tree\', \'auto\'}, default=\'auto\'\n        The tree algorithm to use.\n\n    kernel : {\'gaussian\', \'tophat\', \'epanechnikov\', \'exponential\', \'linear\',                  \'cosine\'}, default=\'gaussian\'\n        The kernel to use.\n\n    metric : str, default=\'euclidean\'\n        Metric to use for distance computation. See the\n        documentation of `scipy.spatial.distance\n        <https://docs.scipy.org/doc/scipy/reference/spatial.distance.html>`_ and\n        the metrics listed in\n        :class:`~sklearn.metrics.pairwise.distance_metrics` for valid metric\n        values.\n\n        Not all metrics are valid with all algorithms: refer to the\n        documentation of :class:`BallTree` and :class:`KDTree`. Note that the\n        normalization of the density output is correct only for the Euclidean\n        distance metric.\n\n    atol : float, default=0\n        The desired absolute tolerance of the result.  A larger tolerance will\n        generally lead to faster execution.\n\n    rtol : float, default=0\n        The desired relative tolerance of the result.  A larger tolerance will\n        generally lead to faster execution.\n\n    breadth_first : bool, default=True\n        If true (default), use a breadth-first approach to the problem.\n        Otherwise use a depth-first approach.\n\n    leaf_size : int, default=40\n        Specify the leaf size of the underlying tree.  See :class:`BallTree`\n        or :class:`KDTree` for details.\n\n    metric_params : dict, default=None\n        Additional parameters to be passed to the tree for use with the\n        metric.  For more information, see the documentation of\n        :class:`BallTree` or :class:`KDTree`.\n\n    Attributes\n    ----------\n    n_features_in_ : int\n        Number of features seen during :term:`fit`.\n\n        .. versionadded:: 0.24\n\n    tree_ : ``BinaryTree`` instance\n        The tree algorithm for fast generalized N-point problems.\n\n    feature_names_in_ : ndarray of shape (`n_features_in_`,)\n        Names of features seen during :term:`fit`. Defined only when `X`\n        has feature names that are all strings.\n\n    bandwidth_ : float\n        Value of the bandwidth, given directly by the bandwidth parameter or\n        estimated using the \'scott\' or \'silverman\' method.\n\n        .. versionadded:: 1.0\n\n    See Also\n    --------\n    sklearn.neighbors.KDTree : K-dimensional tree for fast generalized N-point\n        problems.\n    sklearn.neighbors.BallTree : Ball tree for fast generalized N-point\n        problems.\n\n    Examples\n    --------\n    Compute a gaussian kernel density estimate with a fixed bandwidth.\n\n    >>> from sklearn.neighbors import KernelDensity\n    >>> import numpy as np\n    >>> rng = np.random.RandomState(42)\n    >>> X = rng.random_sample((100, 3))\n    >>> kde = KernelDensity(kernel=\'gaussian\', bandwidth=0.5).fit(X)\n    >>> log_density = kde.score_samples(X[:3])\n    >>> log_density\n    array([-1.52955942, -1.51462041, -1.60244657])\n    '
# WARNING: Decompyle incomplete
