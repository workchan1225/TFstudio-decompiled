# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from numba import runtests
from numba.core import config
if config.ENABLE_CUDASIM:
    from simulator_init import *
else:
    from device_init import *
    from device_init import _auto_device
from numba.cuda.compiler import compile, compile_for_current_device, compile_ptx, compile_ptx_for_current_device
implementation = 'Built-in'

def test(*args, **kwargs):
    if not is_available():
        raise cuda_error()
# WARNING: Decompyle incomplete
