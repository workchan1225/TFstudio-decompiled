# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _time.pyc (Python 3.11)

from _util import ffi, dlls
ffi.cdef('\n\nDWORD WINAPI GetTickCount(void);\n\n')

def _GetTickCount():
    return dlls.kernel32.GetTickCount()
