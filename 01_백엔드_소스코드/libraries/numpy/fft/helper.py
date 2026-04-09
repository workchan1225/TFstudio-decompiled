# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helper.pyc (Python 3.11)

'''
Discrete Fourier Transforms - helper.py

'''
from numpy.core import integer, empty, arange, asarray, roll
from numpy.core.overrides import array_function_dispatch, set_module
__all__ = [
    'fftshift',
    'ifftshift',
    'fftfreq',
    'rfftfreq']
integer_types = (int, integer)

def _fftshift_dispatcher(x, axes = (None,)):
    return (x,)

fftshift = (lambda x, axes = (None,): pass# WARNING: Decompyle incomplete
)()
ifftshift = (lambda x, axes = (None,): pass# WARNING: Decompyle incomplete
)()
fftfreq = (lambda n, d = (1,): if not isinstance(n, integer_types):
raise ValueError('n should be an integer')val = 1 / (n * d)results = empty(n, int)N = (n - 1) // 2 + 1p1 = arange(0, N, dtype = int)results[:N] = p1p2 = arange(-(n // 2), 0, dtype = int)results[N:] = p2results * val)()
rfftfreq = (lambda n, d = (1,): if not isinstance(n, integer_types):
raise ValueError('n should be an integer')val = 1 / (n * d)N = n // 2 + 1results = arange(0, N, dtype = int)results * val)()
