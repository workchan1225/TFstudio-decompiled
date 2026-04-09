# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: histograms.pyc (Python 3.11)

'''
Histogram-related functions
'''
import contextlib
import functools
import operator
import warnings
import numpy as np
from numpy.core import overrides
__all__ = [
    'histogram',
    'histogramdd',
    'histogram_bin_edges']
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')
_range = range

def _ptp(x):
    """Peak-to-peak value of x.

    This implementation avoids the problem of signed integer arrays having a
    peak-to-peak value that cannot be represented with the array's data type.
    This function returns an unsigned value for signed integer arrays.
    """
    return _unsigned_subtract(x.max(), x.min())


def _hist_bin_sqrt(x, range):
    '''
    Square root histogram bin estimator.

    Bin width is inversely proportional to the data size. Used by many
    programs for its simplicity.

    Parameters
    ----------
    x : array_like
        Input data that is to be histogrammed, trimmed to range. May not
        be empty.

    Returns
    -------
    h : An estimate of the optimal bin width for the given data.
    '''
    del range
    return _ptp(x) / np.sqrt(x.size)


def _hist_bin_sturges(x, range):
    '''
    Sturges histogram bin estimator.

    A very simplistic estimator based on the assumption of normality of
    the data. This estimator has poor performance for non-normal data,
    which becomes especially obvious for large data sets. The estimate
    depends only on size of the data.

    Parameters
    ----------
    x : array_like
        Input data that is to be histogrammed, trimmed to range. May not
        be empty.

    Returns
    -------
    h : An estimate of the optimal bin width for the given data.
    '''
    del range
    return _ptp(x) / (np.log2(x.size) + 1)


def _hist_bin_rice(x, range):
    '''
    Rice histogram bin estimator.

    Another simple estimator with no normality assumption. It has better
    performance for large data than Sturges, but tends to overestimate
    the number of bins. The number of bins is proportional to the cube
    root of data size (asymptotically optimal). The estimate depends
    only on size of the data.

    Parameters
    ----------
    x : array_like
        Input data that is to be histogrammed, trimmed to range. May not
        be empty.

    Returns
    -------
    h : An estimate of the optimal bin width for the given data.
    '''
    del range
    return _ptp(x) / (2 * x.size ** 0.333333)


def _hist_bin_scott(x, range):
    '''
    Scott histogram bin estimator.

    The binwidth is proportional to the standard deviation of the data
    and inversely proportional to the cube root of data size
    (asymptotically optimal).

    Parameters
    ----------
    x : array_like
        Input data that is to be histogrammed, trimmed to range. May not
        be empty.

    Returns
    -------
    h : An estimate of the optimal bin width for the given data.
    '''
    del range
    return (24 * np.pi ** 0.5 / x.size) ** 0.333333 * np.std(x)


def _hist_bin_stone(x, range):
    """
    Histogram bin estimator based on minimizing the estimated integrated squared error (ISE).

    The number of bins is chosen by minimizing the estimated ISE against the unknown true distribution.
    The ISE is estimated using cross-validation and can be regarded as a generalization of Scott's rule.
    https://en.wikipedia.org/wiki/Histogram#Scott.27s_normal_reference_rule

    This paper by Stone appears to be the origination of this rule.
    http://digitalassets.lib.berkeley.edu/sdtr/ucb/text/34.pdf

    Parameters
    ----------
    x : array_like
        Input data that is to be histogrammed, trimmed to range. May not
        be empty.
    range : (float, float)
        The lower and upper range of the bins.

    Returns
    -------
    h : An estimate of the optimal bin width for the given data.
    """
    pass
# WARNING: Decompyle incomplete


def _hist_bin_doane(x, range):
