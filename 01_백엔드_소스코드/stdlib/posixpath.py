# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: posixpath.pyc (Python 3.11)

'''Common operations on Posix pathnames.

Instead of importing this module directly, import os and refer to
this module as os.path.  The "os.path" name is an alias for this
module on Posix systems; on other systems (e.g. Windows),
os.path provides the same operations in a manner specific to that
platform, and is an alias to another module (e.g. ntpath).

Some of this can actually be useful on non-Posix systems too, e.g.
for manipulation of the pathname component of URLs.
'''
curdir = '.'
pardir = '..'
extsep = '.'
sep = '/'
pathsep = ':'
defpath = '/bin:/usr/bin'
altsep = None
devnull = '/dev/null'
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
    'samefile',
    'sameopenfile',
    'samestat',
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
    'commonpath']

def _get_sep(path):
    if isinstance(path, bytes):
        return b'/'


def normcase(s):
    '''Normalize case of pathname.  Has no effect under Posix'''
    return os.fspath(s)


def isabs(s):
    '''Test whether a path is absolute'''
    s = os.fspath(s)
    sep = _get_sep(s)
    return s.startswith(sep)


def join(a, *p):
    """Join two or more pathname components, inserting '/' as needed.
    If any component is an absolute path, all previous path components
    will be discarded.  An empty last part will result in a path that
    ends with a separator."""
    a = os.fspath(a)
    sep = _get_sep(a)
    path = a
# WARNING: Decompyle incomplete


def split(p):
    '''Split a pathname.  Returns tuple "(head, tail)" where "tail" is
    everything after the final slash.  Either part may be empty.'''
    p = os.fspath(p)
    sep = _get_sep(p)
    i = p.rfind(sep) + 1
    tail = p[i:]
    head = p[:i]
    if head and head != sep * len(head):
        head = head.rstrip(sep)
    return (head, tail)


def splitext(p):
    p = os.fspath(p)
    if isinstance(p, bytes):
        sep = b'/'
        extsep = b'.'
    else:
        sep = '/'
        extsep = '.'
    return genericpath._splitext(p, sep, None, extsep)

splitext.__doc__ = genericpath._splitext.__doc__

def splitdrive(p):
    '''Split a pathname into drive and path. On Posix, drive is always
    empty.'''
    p = os.fspath(p)
    return (p[:0], p)


def basename(p):
    '''Returns the final component of a pathname'''
    p = os.fspath(p)
    sep = _get_sep(p)
    i = p.rfind(sep) + 1
    return p[i:]


def dirname(p):
    '''Returns the directory component of a pathname'''
    p = os.fspath(p)
    sep = _get_sep(p)
    i = p.rfind(sep) + 1
    head = p[:i]
    if head and head != sep * len(head):
        head = head.rstrip(sep)
    return head


def islink(path):
    '''Test whether a path is a symbolic link'''
    
    try:
        st = os.lstat(path)
    except (OSError, ValueError, AttributeError):
        return False

    return stat.S_ISLNK(st.st_mode)


def lexists(path):
    '''Test whether a path exists.  Returns True for broken symbolic links'''
    
    try:
        os.lstat(path)
    except (OSError, ValueError):
        return False

    return True


def ismount(path):
    '''Test whether a path is a mount point'''
    
    try:
        s1 = os.lstat(path)
        if stat.S_ISLNK(s1.st_mode):
            return False
    except (OSError, ValueError):
        return False
        path = os.fspath(path)
        parent = realpath(parent)
        
        try:
            s2 = os.lstat(parent)
        except (OSError, ValueError):
            return False

        dev1 = s1.st_dev
        dev2 = s2.st_dev
        if dev1 != dev2:
            return True
        ino1 = None.st_ino
        ino2 = s2.st_ino
        if ino1 == ino2:
            return True
        return None



def expanduser(path):
    '''Expand ~ and ~user constructions.  If user or $HOME is unknown,
    do nothing.'''
    path = os.fspath(path)
    if isinstance(path, bytes):
        tilde = b'~'
    else:
        tilde = '~'
    if not path.startswith(tilde):
        return path
    sep = None(path)
    i = path.find(sep, 1)
    if i < 0:
        i = len(path)
# WARNING: Decompyle incomplete

_varprog = None
_varprogb = None

def expandvars(path):
    '''Expand shell variables of form $var and ${var}.  Unknown variables
    are left unchanged.'''
    global _varprogb, _varprog
    path = os.fspath(path)
    if isinstance(path, bytes):
        if b'$' not in path:
            return path
        if not None:
            import re
            _varprogb = re.compile(b'\\$(\\w+|\\{[^}]*\\})', re.ASCII)
        search = _varprogb.search
        start = b'{'
        end = b'}'
        environ = getattr(os, 'environb', None)
    elif '$' not in path:
        return path
    if not _varprog:
        import re
        _varprog = re.compile('\\$(\\w+|\\{[^}]*\\})', re.ASCII)
    search = _varprog.search
    start = '{'
    end = '}'
    environ = os.environ
    i = 0
    m = search(path, i)
    if not m:
        pass
# WARNING: Decompyle incomplete


try:
    from posix import _path_normpath
    
    def normpath(path):
