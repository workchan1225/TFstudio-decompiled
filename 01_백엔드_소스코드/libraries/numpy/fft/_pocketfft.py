# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _pocketfft.pyc (Python 3.11)

'''
Discrete Fourier Transforms

Routines in this module:

fft(a, n=None, axis=-1, norm="backward")
ifft(a, n=None, axis=-1, norm="backward")
rfft(a, n=None, axis=-1, norm="backward")
irfft(a, n=None, axis=-1, norm="backward")
hfft(a, n=None, axis=-1, norm="backward")
ihfft(a, n=None, axis=-1, norm="backward")
fftn(a, s=None, axes=None, norm="backward")
ifftn(a, s=None, axes=None, norm="backward")
rfftn(a, s=None, axes=None, norm="backward")
irfftn(a, s=None, axes=None, norm="backward")
fft2(a, s=None, axes=(-2,-1), norm="backward")
ifft2(a, s=None, axes=(-2, -1), norm="backward")
rfft2(a, s=None, axes=(-2,-1), norm="backward")
irfft2(a, s=None, axes=(-2, -1), norm="backward")

i = inverse transform
r = transform of purely real data
h = Hermite transform
n = n-dimensional transform
2 = 2-dimensional transform
(Note: 2D routines are just nD routines with different default
behavior.)

'''
__all__ = [
    'fft',
    'ifft',
    'rfft',
    'irfft',
    'hfft',
    'ihfft',
    'rfftn',
    'irfftn',
    'rfft2',
    'irfft2',
    'fft2',
    'ifft2',
    'fftn',
    'ifftn']
import functools
from numpy.core import asarray, zeros, swapaxes, conjugate, take, sqrt
from  import _pocketfft_internal as pfi
from numpy.core.multiarray import normalize_axis_index
from numpy.core import overrides
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy.fft')

def _raw_fft(a, n, axis, is_real, is_forward, inv_norm):
    axis = normalize_axis_index(axis, a.ndim)
# WARNING: Decompyle incomplete


def _get_forward_norm(n, norm):
    if n < 1:
        raise ValueError(f'''Invalid number of FFT data points ({n}) specified.''')
# WARNING: Decompyle incomplete


def _get_backward_norm(n, norm):
    if n < 1:
        raise ValueError(f'''Invalid number of FFT data points ({n}) specified.''')
# WARNING: Decompyle incomplete

_SWAP_DIRECTION_MAP = {
    'backward': 'forward',
    None: 'forward',
    'ortho': 'ortho',
    'forward': 'backward' }

def _swap_direction(norm):
    
    try:
        return _SWAP_DIRECTION_MAP[norm]
    except KeyError:
        raise ValueError(f'''Invalid norm value {norm}; should be "backward", "ortho" or "forward".'''), None



def _fft_dispatcher(a, n, axis, norm = (None, None, None)):
    return (a,)

fft = (lambda a, n, axis, norm = (None, -1, None): a = asarray(a)# WARNING: Decompyle incomplete
)()
ifft = (lambda a, n, axis, norm = (None, -1, None): a = asarray(a)# WARNING: Decompyle incomplete
)()
rfft = (lambda a, n, axis, norm = (None, -1, None): a = asarray(a)# WARNING: Decompyle incomplete
)()
irfft = (lambda a, n, axis, norm = (None, -1, None): a = asarray(a)# WARNING: Decompyle incomplete
)()
hfft = (lambda a, n, axis, norm = (None, -1, None): a = asarray(a)# WARNING: Decompyle incomplete
)()
ihfft = (lambda a, n, axis, norm = (None, -1, None): a = asarray(a)# WARNING: Decompyle incomplete
)()

def _cook_nd_args(a, s, axes, invreal = (None, None, 0)):
    pass
# WARNING: Decompyle incomplete


def _raw_fftnd(a, s, axes, function, norm = (None, None, fft, None)):
    a = asarray(a)
    (s, axes) = _cook_nd_args(a, s, axes)
    itl = list(range(len(axes)))
    itl.reverse()
    for ii in itl:
        a = function(a, n = s[ii], axis = axes[ii], norm = norm)
        return a


def _fftn_dispatcher(a, s, axes, norm = (None, None, None)):
    return (a,)

fftn = (lambda a, s, axes, norm = (None, None, None): _raw_fftnd(a, s, axes, fft, norm))()
ifftn = (lambda a, s, axes, norm = (None, None, None): _raw_fftnd(a, s, axes, ifft, norm))()
fft2 = (lambda a, s, axes, norm = (None, (-2, -1), None): _raw_fftnd(a, s, axes, fft, norm))()
ifft2 = (lambda a, s, axes, norm = (None, (-2, -1), None): _raw_fftnd(a, s, axes, ifft, norm))()
rfftn = (lambda a, s, axes, norm = (None, None, None): a = asarray(a)(s, axes) = _cook_nd_args(a, s, axes)a = rfft(a, s[-1], axes[-1], norm)for ii in range(len(axes) - 1):
a = fft(a, s[ii], axes[ii], norm)a)()
rfft2 = (lambda a, s, axes, norm = (None, (-2, -1), None): rfftn(a, s, axes, norm))()
irfftn = (lambda a, s, axes, norm = (None, None, None): a = asarray(a)(s, axes) = _cook_nd_args(a, s, axes, invreal = 1)for ii in range(len(axes) - 1):
a = ifft(a, s[ii], axes[ii], norm)a = irfft(a, s[-1], axes[-1], norm)a)()
irfft2 = (lambda a, s, axes, norm = (None, (-2, -1), None): irfftn(a, s, axes, norm))()
