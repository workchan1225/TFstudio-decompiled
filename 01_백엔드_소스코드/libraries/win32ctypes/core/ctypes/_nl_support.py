# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _nl_support.pyc (Python 3.11)

from ctypes.wintypes import UINT
from _util import function_factory, dlls
_GetACP = function_factory(dlls.kernel32.GetACP, None, UINT)
