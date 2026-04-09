# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: common.pyc (Python 3.11)

'''Common I/O API utilities'''
from __future__ import annotations
from abc import ABC, abstractmethod
import codecs
from collections import defaultdict
from collections.abc import Hashable, Mapping, Sequence
import dataclasses
import functools
import gzip
from io import BufferedIOBase, BytesIO, RawIOBase, StringIO, TextIOBase, TextIOWrapper
import mmap
import os
from pathlib import Path
import re
import tarfile
from typing import IO, TYPE_CHECKING, Any, AnyStr, DefaultDict, Generic, Literal, TypeVar, cast, overload
from urllib.parse import urljoin, urlparse as parse_url, uses_netloc, uses_params, uses_relative
import warnings
import zipfile
from pandas._typing import BaseBuffer, ReadCsvBuffer
from pandas.compat._optional import import_optional_dependency
from pandas.util._exceptions import find_stack_level
from pandas.core.dtypes.common import is_bool, is_file_like, is_integer, is_list_like
from pandas.core.dtypes.generic import ABCMultiIndex
_VALID_URLS = set(uses_relative + uses_netloc + uses_params)
_VALID_URLS.discard('')
_FSSPEC_URL_PATTERN = re.compile('^[A-Za-z][A-Za-z0-9+\\-+.]*(::[A-Za-z0-9+\\-+.]+)*://')
BaseBufferT = TypeVar('BaseBufferT', bound = BaseBuffer)
if TYPE_CHECKING:
    from types import TracebackType
    from pandas._typing import CompressionDict, CompressionOptions, FilePath, ReadBuffer, StorageOptions, WriteBuffer
    from pandas import MultiIndex
IOArgs = <NODE:12>()

def IOHandles():
    '''IOHandles'''
    compression: 'CompressionDict' = '\n    Return value of io/common.py:get_handle\n\n    Can be used as a context manager.\n\n    This is used to easily close created buffers and to handle corner cases when\n    TextIOWrapper is inserted.\n\n    handle: The file handle to be used.\n    created_handles: All file handles that are created by get_handle\n    is_wrapped: Whether a TextIOWrapper needs to be detached.\n    '
    created_handles: 'list[IO[bytes] | IO[str]]' = dataclasses.field(default_factory = list)
    is_wrapped: 'bool' = False
    
    def close(self = None):
        '''
        Close all created buffers.

        Note: If a TextIOWrapper was inserted, it is flushed and detached to
        avoid closing the potentially user-created buffer.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
        self.close()


IOHandles = <NODE:27>(IOHandles, 'IOHandles', Generic[AnyStr])()

def is_url(url = None):
    '''
    Check to see if a URL has a valid protocol.

    Parameters
    ----------
    url : str or unicode

    Returns
    -------
    isurl : bool
        If `url` has a valid protocol return True otherwise False.
    '''
    if not isinstance(url, str):
        return False
    return None(url).scheme in _VALID_URLS

_expand_user = (lambda filepath_or_buffer = None: pass)()
_expand_user = (lambda filepath_or_buffer = None: pass)()

def _expand_user(filepath_or_buffer = None):
    """
    Return the argument with an initial component of ~ or ~user
    replaced by that user's home directory.

    Parameters
    ----------
    filepath_or_buffer : object to be converted if possible

    Returns
    -------
    expanded_filepath_or_buffer : an expanded filepath or the
                                  input if not expandable
    """
    if isinstance(filepath_or_buffer, str):
        return os.path.expanduser(filepath_or_buffer)


def validate_header_arg(header = None):
    pass
# WARNING: Decompyle incomplete

stringify_path = (lambda filepath_or_buffer = None, convert_file_like = None: pass)()
stringify_path = (lambda filepath_or_buffer = None, convert_file_like = None: pass)()

def stringify_path(filepath_or_buffer = None, convert_file_like = None):
    """
    Attempt to convert a path-like object to a string.

    Parameters
    ----------
    filepath_or_buffer : object to be converted

    Returns
    -------
    str_filepath_or_buffer : maybe a string version of the object

    Notes
    -----
    Objects supporting the fspath protocol are coerced
    according to its __fspath__ method.

    Any other object is passed through unchanged, which includes bytes,
    strings, buffers, or anything else that's not even path-like.
    """
    if convert_file_like and is_file_like(filepath_or_buffer):
        return cast(BaseBufferT, filepath_or_buffer)
    if None(filepath_or_buffer, os.PathLike):
        filepath_or_buffer = filepath_or_buffer.__fspath__()
    return _expand_user(filepath_or_buffer)


def urlopen(*args, **kwargs):
    '''
    Lazy-import wrapper for stdlib urlopen, as that imports a big chunk of
    the stdlib.
    '''
    import urllib.request as urllib
# WARNING: Decompyle incomplete


def is_fsspec_url(url = None):
