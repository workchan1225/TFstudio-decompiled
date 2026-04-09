# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

from __future__ import annotations
import io
import logging
import os
import re
from glob import has_magic
from pathlib import Path
from fsspec.caching import BaseCache, BlockCache, BytesCache, MMapCache, ReadAheadCache, caches
from fsspec.compression import compr
from fsspec.config import conf
from fsspec.registry import available_protocols, filesystem, get_filesystem_class
from fsspec.utils import _unstrip_protocol, build_name_function, infer_compression, stringify_path
logger = logging.getLogger('fsspec')

class OpenFile:
    """
    File-like object to be used in a context

    Can layer (buffered) text-mode and compression over any file-system, which
    are typically binary-only.

    These instances are safe to serialize, as the low-level file object
    is not created until invoked using ``with``.

    Parameters
    ----------
    fs: FileSystem
        The file system to use for opening the file. Should be a subclass or duck-type
        with ``fsspec.spec.AbstractFileSystem``
    path: str
        Location to open
    mode: str like 'rb', optional
        Mode of the opened file
    compression: str or None, optional
        Compression to apply
    encoding: str or None, optional
        The encoding to use if opened in text mode.
    errors: str or None, optional
        How to handle encoding errors if opened in text mode.
    newline: None or str
        Passed to TextIOWrapper in text mode, how to handle line endings.
    autoopen: bool
        If True, calls open() immediately. Mostly used by pickle
    pos: int
        If given and autoopen is True, seek to this location immediately
    """
    
    def __init__(self, fs, path, mode, compression, encoding, errors, newline = ('rb', None, None, None, None)):
        self.fs = fs
        self.path = path
        self.mode = mode
        self.compression = get_compression(path, compression)
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.fobjects = []

    
    def __reduce__(self):
        return (OpenFile, (self.fs, self.path, self.mode, self.compression, self.encoding, self.errors, self.newline))

    
    def __repr__(self):
        return f'''<OpenFile \'{self.path}\'>'''

    
    def __enter__(self):
        mode = self.mode.replace('t', '').replace('b', '') + 'b'
        
        try:
            f = self.fs.open(self.path, mode = mode)
        except FileNotFoundError:
            e = None
            if has_magic(self.path):
                raise FileNotFoundError("%s not found. The URL contains glob characters: you maybe needed\nto pass expand=True in fsspec.open() or the storage_options of \nyour library. You can also set the config value 'open_expand'\nbefore import, or fsspec.core.DEFAULT_EXPAND at runtime, to True.", self.path), e
            raise 
            e = None
            del e

        self.fobjects = [
            f]
    # WARNING: Decompyle incomplete

    
    def __exit__(self, *args):
        self.close()

    full_name = (lambda self: _unstrip_protocol(self.path, self.fs))()
    
    def open(self):
        '''Materialise this as a real open file without context

        The OpenFile object should be explicitly closed to avoid enclosed file
        instances persisting. You must, therefore, keep a reference to the OpenFile
        during the life of the file-like it generates.
        '''
        return self.__enter__()

    
    def close(self):
        '''Close all encapsulated file objects'''
        for f in reversed(self.fobjects):
            if not 'r' not in self.mode and f.closed:
                f.flush()
            f.close()
            self.fobjects.clear()
            return None



class OpenFiles(list):
    pass
# WARNING: Decompyle incomplete


def open_files(urlpath, mode, compression, encoding, errors, name_function, num, protocol, newline, auto_mkdir, expand = ('rb', None, 'utf8', None, None, 1, None, None, True, True), **kwargs):
    '''Given a path or paths, return a list of ``OpenFile`` objects.

    For writing, a str path must contain the "*" character, which will be filled
    in by increasing numbers, e.g., "part*" ->  "part1", "part2" if num=2.

    For either reading or writing, can instead provide explicit list of paths.

    Parameters
    ----------
    urlpath: string or list
        Absolute or relative filepath(s). Prefix with a protocol like ``s3://``
        to read from alternative filesystems. To read from multiple files you
        can pass a globstring or a list of paths, with the caveat that they
        must all have the same protocol.
    mode: \'rb\', \'wt\', etc.
    compression: string or None
        If given, open file using compression codec. Can either be a compression
        name (a key in ``fsspec.compression.compr``) or "infer" to guess the
        compression from the filename suffix.
    encoding: str
        For text mode only
    errors: None or str
        Passed to TextIOWrapper in text mode
    name_function: function or None
        if opening a set of files for writing, those files do not yet exist,
        so we need to generate their names by formatting the urlpath for
        each sequence number
    num: int [1]
        if writing mode, number of files we expect to create (passed to
        name+function)
    protocol: str or None
        If given, overrides the protocol found in the URL.
    newline: bytes or None
        Used for line terminator in text mode. If None, uses system default;
        if blank, uses no translation.
    auto_mkdir: bool (True)
        If in write mode, this will ensure the target directory exists before
        writing, by calling ``fs.mkdirs(exist_ok=True)``.
    expand: bool
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        host, port, username, password, etc.

    Examples
    --------
    >>> files = open_files(\'2015-*-*.csv\')  # doctest: +SKIP
    >>> files = open_files(
    ...     \'s3://bucket/2015-*-*.csv.gz\', compression=\'gzip\'
    ... )  # doctest: +SKIP

    Returns
    -------
    An ``OpenFiles`` instance, which is a list of ``OpenFile`` objects that can
    be used as a single context

    Notes
    -----
    For a full list of the available protocols and the implementations that
    they map across to see the latest online documentation:

    - For implementations built into ``fsspec`` see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations
    - For implementations in separate packages see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#other-known-implementations
    '''
    pass
# WARNING: Decompyle incomplete


def _un_chain(path, kwargs):
    pass
# WARNING: Decompyle incomplete


def url_to_fs(url, **kwargs):
    '''
    Turn fully-qualified and potentially chained URL into filesystem instance

    Parameters
    ----------
    url : str
        The fsspec-compatible URL
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        host, port, username, password, etc.

    Returns
    -------
    filesystem : FileSystem
        The new filesystem discovered from ``url`` and created with
        ``**kwargs``.
    urlpath : str
        The file-systems-specific URL for ``url``.
    '''
    pass
# WARNING: Decompyle incomplete

DEFAULT_EXPAND = conf.get('open_expand', False)

def open(urlpath, mode, compression, encoding, errors, protocol, newline, expand = ('rb', None, 'utf8', None, None, None, None), **kwargs):
    '''Given a path or paths, return one ``OpenFile`` object.

    Parameters
    ----------
    urlpath: string or list
        Absolute or relative filepath. Prefix with a protocol like ``s3://``
        to read from alternative filesystems. Should not include glob
        character(s).
    mode: \'rb\', \'wt\', etc.
    compression: string or None
        If given, open file using compression codec. Can either be a compression
        name (a key in ``fsspec.compression.compr``) or "infer" to guess the
        compression from the filename suffix.
    encoding: str
        For text mode only
    errors: None or str
        Passed to TextIOWrapper in text mode
    protocol: str or None
        If given, overrides the protocol found in the URL.
    newline: bytes or None
        Used for line terminator in text mode. If None, uses system default;
        if blank, uses no translation.
    expand: bool or None
        Whether to regard file paths containing special glob characters as needing
        expansion (finding the first match) or absolute. Setting False allows using
        paths which do embed such characters. If None (default), this argument
        takes its value from the DEFAULT_EXPAND module variable, which takes
        its initial value from the "open_expand" config value at startup, which will
        be False if not set.
    **kwargs: dict
        Extra options that make sense to a particular storage connection, e.g.
        host, port, username, password, etc.

    Examples
    --------
    >>> openfile = open(\'2015-01-01.csv\')  # doctest: +SKIP
    >>> openfile = open(
    ...     \'s3://bucket/2015-01-01.csv.gz\', compression=\'gzip\'
    ... )  # doctest: +SKIP
    >>> with openfile as f:
    ...     df = pd.read_csv(f)  # doctest: +SKIP
    ...

    Returns
    -------
    ``OpenFile`` object.

    Notes
    -----
    For a full list of the available protocols and the implementations that
    they map across to see the latest online documentation:

    - For implementations built into ``fsspec`` see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#built-in-implementations
    - For implementations in separate packages see
      https://filesystem-spec.readthedocs.io/en/latest/api.html#other-known-implementations
    '''
    pass
# WARNING: Decompyle incomplete


def open_local(url = None, mode = None, **storage_options):
    '''Open file(s) which can be resolved to local

    For files which either are local, or get downloaded upon open
    (e.g., by file caching)

    Parameters
    ----------
    url: str or list(str)
    mode: str
        Must be read mode
    storage_options:
        passed on to FS for or used by open_files (e.g., compression)
    '''
    if 'r' not in mode:
        raise ValueError('Can only ensure local files when reading')
# WARNING: Decompyle incomplete


def get_compression(urlpath, compression):
    if compression == 'infer':
        compression = infer_compression(urlpath)
# WARNING: Decompyle incomplete


def split_protocol(urlpath):
