# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _wavelab_signals.pyc (Python 3.11)

import numpy as np
__all__ = [
    'demo_signal']
_implemented_signals = [
    'Blocks',
    'Bumps',
    'HeaviSine',
    'Doppler',
    'Ramp',
    'HiSine',
    'LoSine',
    'LinChirp',
    'TwoChirp',
    'QuadChirp',
    'MishMash',
    'WernerSorrows',
    'HypChirps',
    'LinChirps',
    'Chirps',
    'Gabor',
    'sineoneoverx',
    'Piece-Regular',
    'Piece-Polynomial',
    'Riemann']

def demo_signal(name, n = ('Bumps', None)):
    """Simple 1D wavelet test functions.

    This function can generate a number of common 1D test signals used in
    papers by David Donoho and colleagues (e.g. [1]_) as well as the wavelet
    book by Stéphane Mallat [2]_.

    Parameters
    ----------
    name : {'Blocks', 'Bumps', 'HeaviSine', 'Doppler', ...}
        The type of test signal to generate (`name` is case-insensitive). If
        `name` is set to `'list'`, a list of the available test functions is
        returned.
    n : int or None
        The length of the test signal. This should be provided for all test
        signals except `'Gabor'` and `'sineoneoverx'` which have a fixed
        length.

    Returns
    -------
    f : np.ndarray
        Array of length ``n`` corresponding to the specified test signal type.

    References
    ----------
    .. [1] D.L. Donoho and I.M. Johnstone.  Ideal spatial adaptation by
           wavelet shrinkage. Biometrika, vol. 81, pp. 425–455, 1994.
    .. [2] S. Mallat. A Wavelet Tour of Signal Processing: The Sparse Way.
           Academic Press. 2009.

    Notes
    -----
    This function is a partial reimplementation of the `MakeSignal` function
    from the [Wavelab](https://statweb.stanford.edu/~wavelab/) toolbox. These
    test signals are provided with permission of Dr. Donoho to encourage
    reproducible research.

    Examples
    --------
    >>> import pywt
    >>> camera = pywt.data.camera()
    >>> doppler = pywt.data.demo_signal('doppler', 1024)
    >>> available_signals = pywt.data.demo_signal('list')
    >>> print(available_signals)
    ['Blocks', 'Bumps', 'HeaviSine', 'Doppler', 'Ramp', 'HiSine', 'LoSine', 'LinChirp',
     'TwoChirp', 'QuadChirp', 'MishMash', 'WernerSorrows', 'HypChirps', 'LinChirps',
     'Chirps', 'Gabor', 'sineoneoverx', 'Piece-Regular', 'Piece-Polynomial', 'Riemann']

    """
    if name.lower() == 'list':
        return _implemented_signals
# WARNING: Decompyle incomplete
