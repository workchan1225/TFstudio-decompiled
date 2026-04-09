# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _nl_support.pyc (Python 3.11)

from _util import ffi, dlls
ffi.cdef('\n\nUINT WINAPI GetACP(void);\n\n')

def _GetACP():
    return dlls.kernel32.GetACP()
