# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: glob.pyc (Python 3.11)

'''Filename globbing utility.'''
import contextlib
import os
import re
import fnmatch
import itertools
import stat
import sys
__all__ = [
    'glob',
    'iglob',
    'escape']

def glob(pathname = None, *, root_dir, dir_fd, recursive, include_hidden):
    """Return a list of paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. Unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns by default.

    If `include_hidden` is true, the patterns '*', '?', '**'  will match hidden
    directories.

    If `recursive` is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    return list(iglob(pathname, root_dir = root_dir, dir_fd = dir_fd, recursive = recursive, include_hidden = include_hidden))


def iglob(pathname = None, *, root_dir, dir_fd, recursive, include_hidden):
    """Return an iterator which yields the paths matching a pathname pattern.

    The pattern may contain simple shell-style wildcards a la
    fnmatch. However, unlike fnmatch, filenames starting with a
    dot are special cases that are not matched by '*' and '?'
    patterns.

    If recursive is true, the pattern '**' will match any files and
    zero or more directories and subdirectories.
    """
    sys.audit('glob.glob', pathname, recursive)
    sys.audit('glob.glob/2', pathname, recursive, root_dir, dir_fd)
# WARNING: Decompyle incomplete


def _iglob(pathname, root_dir, dir_fd, recursive, dironly, include_hidden = (False,)):
    pass
# WARNING: Decompyle incomplete


def _glob1(dirname, pattern, dir_fd, dironly, include_hidden = (False,)):
    pass
# WARNING: Decompyle incomplete


def _glob0(dirname, basename, dir_fd, dironly, include_hidden = (False,)):
    if basename:
        if _lexists(_join(dirname, basename), dir_fd):
            return [
                basename]
    if _isdir(dirname, dir_fd):
        return [
            basename]


def glob0(dirname, pattern):
    return _glob0(dirname, pattern, None, False)


def glob1(dirname, pattern):
    return _glob1(dirname, pattern, None, False)


def _glob2(dirname, pattern, dir_fd, dironly, include_hidden = (False,)):
    pass
# WARNING: Decompyle incomplete


def _iterdir(dirname, dir_fd, dironly):
    pass
# WARNING: Decompyle incomplete


def _listdir(dirname, dir_fd, dironly):
    it = contextlib.closing(_iterdir(dirname, dir_fd, dironly))
    None(None, None)
    return 
    with None:
        if not None, list(it):
            pass


def _rlistdir(dirname, dir_fd, dironly, include_hidden = (False,)):
    pass
# WARNING: Decompyle incomplete


def _lexists(pathname, dir_fd):
    pass
# WARNING: Decompyle incomplete


def _isdir(pathname, dir_fd):
    pass
# WARNING: Decompyle incomplete


def _join(dirname, basename):
