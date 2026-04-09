# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dll.pyc (Python 3.11)

from _util import ffi, check_null, check_false, dlls, HMODULE, PVOID
ffi.cdef('\n\nHMODULE WINAPI LoadLibraryExW(LPCTSTR lpFileName, HANDLE hFile, DWORD dwFlags);\nBOOL WINAPI FreeLibrary(HMODULE hModule);\n\n')

def _LoadLibraryEx(lpFilename, hFile, dwFlags):
    result = check_null(dlls.kernel32.LoadLibraryExW(str(lpFilename), ffi.NULL, dwFlags), function_name = 'LoadLibraryEx')
    return HMODULE(result)


def _FreeLibrary(hModule):
    check_false(dlls.kernel32.FreeLibrary(PVOID(hModule)), function_name = 'FreeLibrary')
