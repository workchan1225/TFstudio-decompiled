# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ntpath.pyc (Python 3.11)

'''Common pathname manipulations, WindowsNT/95 version.

Instead of importing this module directly, import os and refer to this
module as os.path.
'''
curdir = '.'
pardir = '..'
extsep = '.'
sep = '\\'
pathsep = ';'
altsep = '/'
defpath = '.;C:\\bin'
devnull = 'nul'
import os
import sys
import stat
import genericpath
from genericpath import *
__all__ = [
    'normcase',
    'isabs',
    'join',
    'splitdrive',
    'split',
    'splitext',
    'basename',
    'dirname',
    'commonprefix',
    'getsize',
    'getmtime',
    'getatime',
    'getctime',
    'islink',
    'exists',
    'lexists',
    'isdir',
    'isfile',
    'ismount',
    'expanduser',
    'expandvars',
    'normpath',
    'abspath',
    'curdir',
    'pardir',
    'sep',
    'pathsep',
    'defpath',
    'altsep',
    'extsep',
    'devnull',
    'realpath',
    'supports_unicode_filenames',
    'relpath',
    'samefile',
    'sameopenfile',
    'samestat',
    'commonpath']

def _get_bothseps(path):
    if isinstance(path, bytes):
        return b'\\/'


try:
    from _winapi import LCMapStringEx as _LCMapStringEx, LOCALE_NAME_INVARIANT as _LOCALE_NAME_INVARIANT, LCMAP_LOWERCASE as _LCMAP_LOWERCASE
    
    def normcase(s):
        '''Normalize case of pathname.

        Makes all characters lowercase and all slashes into backslashes.
        '''
        s = os.fspath(s)
        if not s:
            return s
        if None(s, bytes):
            encoding = sys.getfilesystemencoding()
            s = s.decode(encoding, 'surrogateescape').replace('/', '\\')
            s = _LCMapStringEx(_LOCALE_NAME_INVARIANT, _LCMAP_LOWERCASE, s)
            return s.encode(encoding, 'surrogateescape')
        return None(_LOCALE_NAME_INVARIANT, _LCMAP_LOWERCASE, s.replace('/', '\\'))

except ImportError:
    
    def normcase(s):
        '''Normalize case of pathname.

        Makes all characters lowercase and all slashes into backslashes.
        '''
        s = os.fspath(s)
        if isinstance(s, bytes):
            return os.fsencode(os.fsdecode(s).replace('/', '\\').lower())
        return None.replace('/', '\\').lower()



def isabs(s):
    '''Test whether a path is absolute'''
    s = os.fspath(s)
    if isinstance(s, bytes):
        sep = b'\\'
        altsep = b'/'
        colon_sep = b':\\'
    else:
        sep = '\\'
        altsep = '/'
        colon_sep = ':\\'
    s = s[:3].replace(altsep, sep)
    if s.startswith(sep) or s.startswith(colon_sep, 1):
        return True


def join(path, *paths):
    path = os.fspath(path)
    if isinstance(path, bytes):
        sep = b'\\'
        seps = b'\\/'
        colon = b':'
    else:
        sep = '\\'
        seps = '\\/'
        colon = ':'
# WARNING: Decompyle incomplete


def splitdrive(p):
