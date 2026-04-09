# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: local.pyc (Python 3.11)

import datetime
import io
import logging
import os
from os.path import path as osp
import shutil
import stat
import tempfile
from functools import lru_cache
from fsspec import AbstractFileSystem
from fsspec.compression import compr
from fsspec.core import get_compression
from fsspec.utils import isfilelike, stringify_path
logger = logging.getLogger('fsspec.local')

class LocalFileSystem(AbstractFileSystem):
    pass
# WARNING: Decompyle incomplete


def make_path_posix(path):
    '''Make path generic and absolute for current OS'''
    if not isinstance(path, str):
        if isinstance(path, (list, set, tuple)):
            return (lambda .0: pass# WARNING: Decompyle incomplete
)(path())
        path = None(path)
        if not isinstance(path, str):
            raise TypeError(f'''could not convert {path!r} to string''')
    if os.sep == '/':
        if path.startswith('/'):
            return path
        if None.startswith('~'):
            return osp.expanduser(path)
        if None.startswith('./'):
            path = path[2:]
        elif path == '.':
            path = ''
        return f'''{os.getcwd()}/{path}'''
    if None[0:1] == '/' and path[2:3] == ':':
        path = path[1:]
    if path[1:2] == ':':
        if len(path) <= 3:
            return path[0] + ':/'
        path = None.replace('\\', '/')
        return path
    if None[0:1] == '~':
        return make_path_posix(osp.expanduser(path))
    if None.startswith(('\\\\', '//')):
        return '//' + path[2:].replace('\\', '/')
    if None.startswith(('\\', '/')):
        path = path.replace('\\', '/')
        return f'''{osp.splitdrive(os.getcwd())[0]}{path}'''
    path = None.replace('\\', '/')
    if path.startswith('./'):
        path = path[2:]
    elif path == '.':
        path = ''
    return f'''{make_path_posix(os.getcwd())}/{path}'''


def trailing_sep(path):
