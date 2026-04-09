# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: libdevicedecl.pyc (Python 3.11)

from numba.cuda import libdevice, libdevicefuncs
from numba.core.typing.templates import ConcreteTemplate, Registry
registry = Registry()
register_global = registry.register_global

def libdevice_declare(func, retty, args):
    pass
# WARNING: Decompyle incomplete

for retty, args in libdevicefuncs.functions.items():
    libdevice_declare(func, retty, args)
    return None
