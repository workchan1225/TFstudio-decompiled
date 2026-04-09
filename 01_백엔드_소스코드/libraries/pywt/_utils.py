# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

import inspect
from collections.abc import Iterable
import numpy as np
from _extensions._pywt import ContinuousWavelet, DiscreteContinuousWavelet, Modes, Wavelet
AxisError: type[Exception]
if np.lib.NumpyVersion(np.__version__) >= '1.25.0':
    from numpy.exceptions import AxisError
else:
    from numpy import AxisError

def _as_wavelet(wavelet):
    '''Convert wavelet name to a Wavelet object.'''
    if not isinstance(wavelet, (ContinuousWavelet, Wavelet)):
        wavelet = DiscreteContinuousWavelet(wavelet)
    if isinstance(wavelet, ContinuousWavelet):
        raise ValueError("A ContinuousWavelet object was provided, but only discrete Wavelet objects are supported by this function.  A list of all supported discrete wavelets can be obtained by running:\nprint(pywt.wavelist(kind='discrete'))")
    return wavelet


def _wavelets_per_axis(wavelet, axes):
    '''Initialize Wavelets for each axis to be transformed.

    Parameters
    ----------
    wavelet : Wavelet or tuple of Wavelets
        If a single Wavelet is provided, it will used for all axes.  Otherwise
        one Wavelet per axis must be provided.
    axes : list
        The tuple of axes to be transformed.

    Returns
    -------
    wavelets : list of Wavelet objects
        A tuple of Wavelets equal in length to ``axes``.

    '''
    axes = tuple(axes)
    if isinstance(wavelet, (str, Wavelet)):
        wavelets = [
            _as_wavelet(wavelet)] * len(axes)
    elif isinstance(wavelet, Iterable):
        if len(wavelet) == 1:
            wavelets = [
                _as_wavelet(wavelet[0])] * len(axes)
        elif len(wavelet) != len(axes):
            raise ValueError('The number of wavelets must match the number of axes to be transformed.')
        wavelets = wavelet()
    else:
        raise ValueError('wavelet must be a str, Wavelet or iterable')
    return wavelets


def _modes_per_axis(modes, axes):
    '''Initialize mode for each axis to be transformed.

    Parameters
    ----------
    modes : str or tuple of strings
        If a single mode is provided, it will used for all axes.  Otherwise
        one mode per axis must be provided.
    axes : tuple
        The tuple of axes to be transformed.

    Returns
    -------
    modes : tuple of int
        A tuple of Modes equal in length to ``axes``.

    '''
    axes = tuple(axes)
    if isinstance(modes, (int, str)):
        modes = [
            Modes.from_object(modes)] * len(axes)
    elif isinstance(modes, Iterable):
        if len(modes) == 1:
            modes = [
                Modes.from_object(modes[0])] * len(axes)
        elif len(modes) != len(axes):
            raise ValueError('The number of modes must match the number of axes to be transformed.')
        modes = modes()
    else:
        raise ValueError('modes must be a str, Mode enum or iterable')
    return modes
