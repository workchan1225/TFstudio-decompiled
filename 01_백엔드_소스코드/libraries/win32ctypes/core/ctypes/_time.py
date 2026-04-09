# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _time.pyc (Python 3.11)

from ctypes.wintypes import DWORD
from _util import function_factory, dlls
_GetTickCount = function_factory(dlls.kernel32.GetTickCount, None, DWORD)
