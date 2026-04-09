# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fft.pyc (Python 3.11)

from dask.array.fft import *
_n = { }
exec('from dask.array.fft import *', _n)
for k in ('__builtins__', 'Sequence', 'annotations', 'warnings'):
    _n.pop(k, None)
    fft_all = list(_n)
    del _n
    del k
    from common import _fft
    from _internal import get_xp
    from dask.array import array as da
    fftfreq = get_xp(da)(_fft.fftfreq)
    rfftfreq = get_xp(da)(_fft.rfftfreq)
    __all__ = fft_all + [
        'fftfreq',
        'rfftfreq']
    _all_ignore = [
        'da',
        'fft_all',
        'get_xp',
        'warnings']
    return None
