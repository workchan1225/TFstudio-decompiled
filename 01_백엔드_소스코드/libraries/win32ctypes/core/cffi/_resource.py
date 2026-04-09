# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _resource.pyc (Python 3.11)

from _util import ffi, check_null, check_zero, check_false, HMODULE, PVOID, RESOURCE, resource, dlls
ffi.cdef('\n\ntypedef int WINBOOL;\ntypedef WINBOOL (__stdcall *ENUMRESTYPEPROC) (HANDLE, LPTSTR, LONG_PTR);\ntypedef WINBOOL (__stdcall *ENUMRESNAMEPROC) (HANDLE, LPCTSTR, LPTSTR, LONG_PTR);\ntypedef WINBOOL (__stdcall *ENUMRESLANGPROC) (HANDLE, LPCTSTR, LPCTSTR, WORD, LONG_PTR);\n\nBOOL WINAPI EnumResourceTypesW(\n    HMODULE hModule, ENUMRESTYPEPROC lpEnumFunc, LONG_PTR lParam);\nBOOL WINAPI EnumResourceNamesW(\n    HMODULE hModule, LPCTSTR lpszType,\n    ENUMRESNAMEPROC lpEnumFunc, LONG_PTR lParam);\nBOOL WINAPI EnumResourceLanguagesW(\n    HMODULE hModule, LPCTSTR lpType,\n    LPCTSTR lpName, ENUMRESLANGPROC lpEnumFunc, LONG_PTR lParam);\nHRSRC WINAPI FindResourceExW(\n    HMODULE hModule, LPCTSTR lpType, LPCTSTR lpName, WORD wLanguage);\nDWORD WINAPI SizeofResource(HMODULE hModule, HRSRC hResInfo);\nHGLOBAL WINAPI LoadResource(HMODULE hModule, HRSRC hResInfo);\nLPVOID WINAPI LockResource(HGLOBAL hResData);\n\nHANDLE WINAPI BeginUpdateResourceW(LPCTSTR pFileName, BOOL bDeleteExistingResources);\nBOOL WINAPI EndUpdateResourceW(HANDLE hUpdate, BOOL fDiscard);\nBOOL WINAPI UpdateResourceW(HANDLE hUpdate, LPCTSTR lpType, LPCTSTR lpName, WORD wLanguage, LPVOID lpData, DWORD cbData);\n\n')

def ENUMRESTYPEPROC(callback):
    pass
# WARNING: Decompyle incomplete


def ENUMRESNAMEPROC(callback):
    pass
# WARNING: Decompyle incomplete


def ENUMRESLANGPROC(callback):
    pass
# WARNING: Decompyle incomplete


def _EnumResourceTypes(hModule, lpEnumFunc, lParam):
    callback = ffi.callback('ENUMRESTYPEPROC', lpEnumFunc)
    check_false(dlls.kernel32.EnumResourceTypesW(PVOID(hModule), callback, lParam), function_name = 'EnumResourceTypes')


def _EnumResourceNames(hModule, lpszType, lpEnumFunc, lParam):
    callback = ffi.callback('ENUMRESNAMEPROC', lpEnumFunc)
    check_false(dlls.kernel32.EnumResourceNamesW(PVOID(hModule), RESOURCE(lpszType), callback, lParam), function_name = 'EnumResourceNames')


def _EnumResourceLanguages(hModule, lpType, lpName, lpEnumFunc, lParam):
    callback = ffi.callback('ENUMRESLANGPROC', lpEnumFunc)
    check_false(dlls.kernel32.EnumResourceLanguagesW(PVOID(hModule), RESOURCE(lpType), RESOURCE(lpName), callback, lParam), function_name = 'EnumResourceLanguages')


def _FindResourceEx(hModule, lpType, lpName, wLanguage):
    return check_null(dlls.kernel32.FindResourceExW(PVOID(hModule), RESOURCE(lpType), RESOURCE(lpName), wLanguage), function_name = 'FindResourceEx')


def _SizeofResource(hModule, hResInfo):
    return check_zero(dlls.kernel32.SizeofResource(PVOID(hModule), hResInfo), function_name = 'SizeofResource')


def _LoadResource(hModule, hResInfo):
    return check_null(dlls.kernel32.LoadResource(PVOID(hModule), hResInfo), function_name = 'LoadResource')


def _LockResource(hResData):
    return check_null(dlls.kernel32.LockResource(hResData), function_name = 'LockResource')


def _BeginUpdateResource(pFileName, bDeleteExistingResources):
    result = check_null(dlls.kernel32.BeginUpdateResourceW(str(pFileName), bDeleteExistingResources))
    return HMODULE(result)


def _EndUpdateResource(hUpdate, fDiscard):
    check_false(dlls.kernel32.EndUpdateResourceW(PVOID(hUpdate), fDiscard), function_name = 'EndUpdateResource')


def _UpdateResource(hUpdate, lpType, lpName, wLanguage, cData, cbData):
    lpData = ffi.from_buffer(cData)
    check_false(dlls.kernel32.UpdateResourceW(PVOID(hUpdate), RESOURCE(lpType), RESOURCE(lpName), wLanguage, PVOID(lpData), cbData), function_name = 'UpdateResource')
