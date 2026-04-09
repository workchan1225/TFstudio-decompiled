# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _system_information.pyc (Python 3.11)

from _util import ffi, dlls
MAX_PATH = 260
MAX_PATH_BUF = 'wchar_t[{0}]'.format(MAX_PATH)
ffi.cdef('\n\nBOOL WINAPI Beep(DWORD dwFreq, DWORD dwDuration);\nUINT WINAPI GetWindowsDirectoryW(LPTSTR lpBuffer, UINT uSize);\nUINT WINAPI GetSystemDirectoryW(LPTSTR lpBuffer, UINT uSize);\n\n')

def _GetWindowsDirectory():
    buffer = ffi.new(MAX_PATH_BUF)
    directory = dlls.kernel32.GetWindowsDirectoryW(buffer, MAX_PATH)
    return ffi.unpack(buffer, directory)


def _GetSystemDirectory():
    buffer = ffi.new(MAX_PATH_BUF)
    directory = dlls.kernel32.GetSystemDirectoryW(buffer, MAX_PATH)
    return ffi.unpack(buffer, directory)
