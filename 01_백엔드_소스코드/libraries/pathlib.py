# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pathlib.pyc (Python 3.11)

import fnmatch
import functools
import io
import ntpath
import os
import posixpath
import re
import sys
import warnings
from _collections_abc import Sequence
from errno import ENOENT, ENOTDIR, EBADF, ELOOP
from operator import attrgetter
from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO
from urllib.parse import quote_from_bytes as urlquote_from_bytes
__all__ = [
    'PurePath',
    'PurePosixPath',
    'PureWindowsPath',
    'Path',
    'PosixPath',
    'WindowsPath']
_WINERROR_NOT_READY = 21
_WINERROR_INVALID_NAME = 123
_WINERROR_CANT_RESOLVE_FILENAME = 1921
_IGNORED_ERRNOS = (ENOENT, ENOTDIR, EBADF, ELOOP)
_IGNORED_WINERRORS = (_WINERROR_NOT_READY, _WINERROR_INVALID_NAME, _WINERROR_CANT_RESOLVE_FILENAME)

def _ignore_error(exception):
