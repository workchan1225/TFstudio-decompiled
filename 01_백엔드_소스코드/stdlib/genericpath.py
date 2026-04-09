# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: genericpath.pyc (Python 3.11)

'''
Path operations common to more than one OS
Do not use directly.  The OS specific modules import the appropriate
functions from this module themselves.
'''
import os
import stat
__all__ = [
    'commonprefix',
    'exists',
    'getatime',
    'getctime',
    'getmtime',
    'getsize',
    'isdir',
    'isfile',
    'samefile',
    'sameopenfile',
    'samestat']

def exists(path):
    '''Test whether a path exists.  Returns False for broken symbolic links'''
    
    try:
        os.stat(path)
    except (OSError, ValueError):
        return False

    return True


def isfile(path):
    '''Test whether a path is a regular file'''
    
    try:
        st = os.stat(path)
    except (OSError, ValueError):
        return False

    return stat.S_ISREG(st.st_mode)


def isdir(s):
    '''Return true if the pathname refers to an existing directory.'''
    
    try:
        st = os.stat(s)
    except (OSError, ValueError):
        return False

    return stat.S_ISDIR(st.st_mode)


def getsize(filename):
    '''Return the size of a file, reported by os.stat().'''
    return os.stat(filename).st_size


def getmtime(filename):
    '''Return the last modification time of a file, reported by os.stat().'''
    return os.stat(filename).st_mtime


def getatime(filename):
    '''Return the last access time of a file, reported by os.stat().'''
    return os.stat(filename).st_atime


def getctime(filename):
    '''Return the metadata change time of a file, reported by os.stat().'''
    return os.stat(filename).st_ctime


def commonprefix(m):
    '''Given a list of pathnames, returns the longest common leading component'''
    if not m:
        return ''
    if not None(m[0], (list, tuple)):
        m = tuple(map(os.fspath, m))
    s1 = min(m)
    s2 = max(m)
    for i, c in enumerate(s1):
        if c != s2[i]:
            
            return None, s1[:i]
        return s1


def samestat(s1, s2):
