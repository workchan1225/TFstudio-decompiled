# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libdeviceimpl.pyc (Python 3.11)

from llvmlite import ir
from numba.core import cgutils, types
from numba.core.imputils import Registry
from numba.cuda import libdevice, libdevicefuncs
registry = Registry()
lower = registry.lower

def libdevice_implement(func, retty, nbargs):
    pass
# WARNING: Decompyle incomplete


def libdevice_implement_multiple_returns(func, retty, prototype_args):
    pass
# WARNING: Decompyle incomplete

for retty, args in libdevicefuncs.functions.items():
    if (lambda .0: [ arg.is_ptr for arg in .0 ])(args()):
        libdevice_implement_multiple_returns(func, retty, args)
        continue
    libdevice_implement(func, retty, args)
    return None
