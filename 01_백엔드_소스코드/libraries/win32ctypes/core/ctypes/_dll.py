# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dll.pyc (Python 3.11)

from ctypes.wintypes import BOOL, DWORD, HANDLE, HMODULE, LPCWSTR
from _util import check_null, check_false, function_factory, dlls
_LoadLibraryEx = function_factory(dlls.kernel32.LoadLibraryExW, [
    LPCWSTR,
    HANDLE,
    DWORD], HMODULE, check_null)
_FreeLibrary = function_factory(dlls.kernel32.FreeLibrary, [
    HMODULE], BOOL, check_false)
