# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: files.pyc (Python 3.11)

'''File wrangling.'''
from __future__ import annotations
import hashlib
import ntpath
import os
import os.path as os
import posixpath
import re
import sys
from collections.abc import Iterable
from typing import Callable
from coverage import env
from coverage.exceptions import ConfigError
from coverage.misc import human_sorted, isolate_module, join_regex
os = isolate_module(os)
RELATIVE_DIR: 'str' = ''
CANONICAL_FILENAME_CACHE: 'dict[str, str]' = { }

def set_relative_directory():
    '''Set the directory that `relative_filename` will be relative to.'''
    global RELATIVE_DIR, CANONICAL_FILENAME_CACHE
    abs_curdir = abs_file(os.curdir)
    if not abs_curdir.endswith(os.sep):
        abs_curdir = abs_curdir + os.sep
    RELATIVE_DIR = os.path.normcase(abs_curdir)
    CANONICAL_FILENAME_CACHE = { }


def relative_directory():
    '''Return the directory that `relative_filename` is relative to.'''
    return RELATIVE_DIR


def relative_filename(filename = None):
    '''Return the relative form of `filename`.

    The file name will be relative to the current directory when the
    `set_relative_directory` was called.

    '''
    fnorm = os.path.normcase(filename)
    if fnorm.startswith(RELATIVE_DIR):
        filename = filename[len(RELATIVE_DIR):]
    return filename


def canonical_filename(filename = None):
    '''Return a canonical file name for `filename`.

    An absolute path with no redundant components and normalized case.

    '''
    pass
# WARNING: Decompyle incomplete


def flat_rootname(filename = None):
    """A base for a flat file name to correspond to this file.

    Useful for writing files about the code where you want all the files in
    the same directory, but need to differentiate same-named files from
    different directories.

    For example, the file a/b/c.py will return 'z_86bbcbe134d28fd2_c_py'

    """
    (dirname, basename) = ntpath.split(filename)
    if dirname:
        fp = hashlib.new('sha3_256', dirname.encode('UTF-8'), usedforsecurity = False).hexdigest()[:16]
        prefix = f'''z_{fp}_'''
    else:
        prefix = ''
    return prefix + basename.replace('.', '_')

if env.WINDOWS:
    _ACTUAL_PATH_CACHE: 'dict[str, str]' = { }
    _ACTUAL_PATH_LIST_CACHE: 'dict[str, list[str]]' = { }
    
    def actual_path(path = None):
        '''Get the actual path of `path`, including the correct case.'''
        if path in _ACTUAL_PATH_CACHE:
            return _ACTUAL_PATH_CACHE[path]
        (head, tail) = None.path.split(path)
        if not tail:
            actpath = head.upper()
        elif not head:
            actpath = tail
        else:
            head = actual_path(head)
            if head in _ACTUAL_PATH_LIST_CACHE:
                files = _ACTUAL_PATH_LIST_CACHE[head]
            else:
                
                try:
                    files = os.listdir(head)
                except Exception:
                    files = []

                _ACTUAL_PATH_LIST_CACHE[head] = files
            normtail = os.path.normcase(tail)
            for f in files:
                if os.path.normcase(f) == normtail:
                    tail = f
                
                actpath = os.path.join(head, tail)
                _ACTUAL_PATH_CACHE[path] = actpath
                return actpath

else:
    
    def actual_path(path = None):
        '''The actual path for non-Windows platforms.'''
        return path


def abs_file(path = None):
    '''Return the absolute normalized form of `path`.'''
    return actual_path(os.path.abspath(os.path.realpath(path)))


def zip_location(filename = None):
