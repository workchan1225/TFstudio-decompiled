# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _authentication.pyc (Python 3.11)

from weakref import WeakKeyDictionary
from win32ctypes.core.compat import is_text
from _util import ffi, check_false, dlls
from _nl_support import _GetACP
from _common import _PyBytes_FromStringAndSize
ffi.cdef('\n\ntypedef struct _FILETIME {\n  DWORD dwLowDateTime;\n  DWORD dwHighDateTime;\n} FILETIME, *PFILETIME;\n\ntypedef struct _CREDENTIAL_ATTRIBUTE {\n  LPWSTR Keyword;\n  DWORD  Flags;\n  DWORD  ValueSize;\n  LPBYTE Value;\n} CREDENTIAL_ATTRIBUTE, *PCREDENTIAL_ATTRIBUTE;\n\ntypedef struct _CREDENTIAL {\n  DWORD                 Flags;\n  DWORD                 Type;\n  LPWSTR                TargetName;\n  LPWSTR                Comment;\n  FILETIME              LastWritten;\n  DWORD                 CredentialBlobSize;\n  LPBYTE                CredentialBlob;\n  DWORD                 Persist;\n  DWORD                 AttributeCount;\n  PCREDENTIAL_ATTRIBUTE Attributes;\n  LPWSTR                TargetAlias;\n  LPWSTR                UserName;\n} CREDENTIAL, *PCREDENTIAL;\n\n\nBOOL WINAPI CredReadW(\n    LPCWSTR TargetName, DWORD Type, DWORD Flags, PCREDENTIAL *Credential);\nBOOL WINAPI CredWriteW(PCREDENTIAL Credential, DWORD);\nVOID WINAPI CredFree(PVOID Buffer);\nBOOL WINAPI CredDeleteW(LPCWSTR TargetName, DWORD Type, DWORD Flags);\nBOOL WINAPI CredEnumerateW(\n    LPCWSTR Filter, DWORD Flags, DWORD *Count, PCREDENTIAL **Credential);\n')
_keep_alive = WeakKeyDictionary()
SUPPORTED_CREDKEYS = set(('Type', 'TargetName', 'Persist', 'UserName', 'Comment', 'CredentialBlob'))

def make_unicode(password):
    ''' Convert the input string to unicode.

    '''
    if is_text(password):
        return password
    code_page = None()
    return password.decode(encoding = str(code_page), errors = 'strict')


class _CREDENTIAL(object):
    
    def __call__(self):
        return ffi.new('PCREDENTIAL')[0]

    fromdict = (lambda cls, credential, flag = (0,): unsupported = set(credential.keys()) - SUPPORTED_CREDKEYSif len(unsupported):
raise ValueError('Unsupported keys: {0}'.format(unsupported))if flag != 0:
raise ValueError('flag != 0 not yet supported')factory = cls()c_creds = factory()values = []# WARNING: Decompyle incomplete
)()

CREDENTIAL = _CREDENTIAL()

def PCREDENTIAL(value = (None,)):
    pass
# WARNING: Decompyle incomplete


def PPCREDENTIAL(value = (None,)):
    pass
# WARNING: Decompyle incomplete


def PPPCREDENTIAL(value = (None,)):
    pass
# WARNING: Decompyle incomplete


def credential2dict(pc_creds):
    credentials = { }
    for key in SUPPORTED_CREDKEYS:
        if key == 'CredentialBlob':
            data = _PyBytes_FromStringAndSize(pc_creds.CredentialBlob, pc_creds.CredentialBlobSize)
        elif key in ('Type', 'Persist'):
            data = int(getattr(pc_creds, key))
        else:
            string_pointer = getattr(pc_creds, key)
            if string_pointer == ffi.NULL:
                data = None
            else:
                data = ffi.string(string_pointer)
        credentials[key] = data
        return credentials


def _CredRead(TargetName, Type, Flags, ppCredential):
    target = make_unicode(TargetName)
    return check_false(dlls.advapi32.CredReadW(target, Type, Flags, ppCredential), 'CredRead')


def _CredWrite(Credential, Flags):
    return check_false(dlls.advapi32.CredWriteW(Credential, Flags), 'CredWrite')


def _CredDelete(TargetName, Type, Flags):
    return check_false(dlls.advapi32.CredDeleteW(make_unicode(TargetName), Type, Flags), 'CredDelete')


def _CredEnumerate(Filter, Flags, Count, pppCredential):
    pass
# WARNING: Decompyle incomplete

_CredFree = dlls.advapi32.CredFree
