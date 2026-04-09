# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: disk.pyc (Python 3.11)

'''
Disk management utilities.
'''
import errno
import os
import shutil
import sys
import time
from multiprocessing import util

try:
    WindowsError
except NameError:
    WindowsError = OSError


def disk_used(path):
    '''Return the disk usage in a directory.'''
    size = 0
    for file in os.listdir(path) + [
        '.']:
        stat = os.stat(os.path.join(path, file))
        if hasattr(stat, 'st_blocks'):
            size += stat.st_blocks * 512
            continue
        size += (stat.st_size // 512 + 1) * 512
        return int(size / 1024)


def memstr_to_bytes(text):
    '''Convert a memory text to its value in bytes.'''
    kilo = 1024
    units = dict(K = kilo, M = kilo ** 2, G = kilo ** 3)
    
    try:
        size = int(units[text[-1]] * float(text[:-1]))
    except (KeyError, ValueError):
        e = None
        raise ValueError(f'''Invalid literal for size give: {text!s} (type {type(text)!s}) should be alike \'10G\', \'500M\', \'50K\'.'''), e
        e = None
        del e

    return size


def mkdirp(d):
    '''Ensure directory d exists (like mkdir -p on Unix)
    No guarantee that the directory is writable.
    '''
    
    try:
        os.makedirs(d)
        return None
    except OSError:
        e = None
        if e.errno != errno.EEXIST:
            raise 
        e = None
        del e
        return None
        e = None
        del e


RM_SUBDIRS_RETRY_TIME = 0.1
RM_SUBDIRS_N_RETRY = 10

def rm_subdirs(path, onerror = (None,)):
    '''Remove all subdirectories in this path.

    The directory indicated by `path` is left in place, and its subdirectories
    are erased.

    If onerror is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is os.listdir, os.remove, or os.rmdir;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info(). If onerror is None,
    an exception is raised.
    '''
    names = []
# WARNING: Decompyle incomplete


def delete_folder(folder_path, onerror, allow_non_empty = (None, True)):
    '''Utility function to cleanup a temporary folder if it still exists.'''
    pass
# WARNING: Decompyle incomplete
