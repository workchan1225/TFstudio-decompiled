# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _system_information.pyc (Python 3.11)

import ctypes
from ctypes.wintypes import LPCWSTR, UINT, LPWSTR, MAX_PATH
from _util import check_zero, function_factory, dlls

def _GetWindowsDirectory():
    buffer = ctypes.create_unicode_buffer(MAX_PATH)
    _BaseGetWindowsDirectory(buffer, MAX_PATH)
    return ctypes.cast(buffer, LPCWSTR).value


def _GetSystemDirectory():
    buffer = ctypes.create_unicode_buffer(MAX_PATH)
    _BaseGetSystemDirectory(buffer, MAX_PATH)
    return ctypes.cast(buffer, LPCWSTR).value

_BaseGetWindowsDirectory = function_factory(dlls.kernel32.GetWindowsDirectoryW, [
    LPWSTR,
    UINT], UINT, check_zero)
_BaseGetSystemDirectory = function_factory(dlls.kernel32.GetSystemDirectoryW, [
    LPWSTR,
    UINT], UINT, check_zero)
