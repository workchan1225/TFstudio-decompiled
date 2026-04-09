# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import logging
import math
import os
import re
import sys
import tempfile
from collections.abc import Callable, Iterable, Iterator, Sequence
from functools import partial
from hashlib import md5
from importlib.metadata import version
from typing import IO, TYPE_CHECKING, Any, TypeVar
from urllib.parse import urlsplit
if TYPE_CHECKING:
    import pathlib
    from typing import TypeGuard
    from fsspec.spec import AbstractFileSystem
DEFAULT_BLOCK_SIZE = 5242880
T = TypeVar('T')

def infer_storage_options(urlpath = None, inherit_storage_options = None):
    '''Infer storage options from URL path and merge it with existing storage
    options.

    Parameters
    ----------
    urlpath: str or unicode
        Either local absolute file path or URL (hdfs://namenode:8020/file.csv)
    inherit_storage_options: dict (optional)
        Its contents will get merged with the inferred information from the
        given path

    Returns
    -------
    Storage options dict.

    Examples
    --------
    >>> infer_storage_options(\'/mnt/datasets/test.csv\')  # doctest: +SKIP
    {"protocol": "file", "path", "/mnt/datasets/test.csv"}
    >>> infer_storage_options(
    ...     \'hdfs://username:pwd@node:123/mnt/datasets/test.csv?q=1\',
    ...     inherit_storage_options={\'extra\': \'value\'},
    ... )  # doctest: +SKIP
    {"protocol": "hdfs", "username": "username", "password": "pwd",
    "host": "node", "port": 123, "path": "/mnt/datasets/test.csv",
    "url_query": "q=1", "extra": "value"}
    '''
    pass
# WARNING: Decompyle incomplete


def update_storage_options(options = None, inherited = None):
    if not inherited:
        inherited = { }
    collisions = set(options) & set(inherited)
    if collisions:
        for collision in collisions:
            if options.get(collision) != inherited.get(collision):
                raise KeyError(f'''Collision between inferred and specified storage option:\n{collision}''')
            options.update(inherited)
            return None

compressions: 'dict[str, str]' = { }

def infer_compression(filename = None):
    '''Infer compression, if available, from filename.

    Infer a named compression type, if registered and available, from filename
    extension. This includes builtin (gz, bz2, zip) compressions, as well as
    optional compressions. See fsspec.compression.register_compression.
    '''
    extension = os.path.splitext(filename)[-1].strip('.').lower()
    if extension in compressions:
        return compressions[extension]


def build_name_function(max_int = None):
    """Returns a function that receives a single integer
    and returns it as a string padded by enough zero characters
    to align with maximum possible integer

    >>> name_f = build_name_function(57)

    >>> name_f(7)
    '07'
    >>> name_f(31)
    '31'
    >>> build_name_function(1000)(42)
    '0042'
    >>> build_name_function(999)(42)
    '042'
    >>> build_name_function(0)(0)
    '0'
    """
    pass
# WARNING: Decompyle incomplete


def seek_delimiter(file = None, delimiter = None, blocksize = None):
    """Seek current file to file start, file end, or byte after delimiter seq.

    Seeks file to next chunk delimiter, where chunks are defined on file start,
    a delimiting sequence, and file end. Use file.tell() to see location afterwards.
    Note that file start is a valid split, so must be at offset > 0 to seek for
    delimiter.

    Parameters
    ----------
    file: a file
    delimiter: bytes
        a delimiter like ``b'\\n'`` or message sentinel, matching file .read() type
    blocksize: int
        Number of bytes to read from the file at once.


    Returns
    -------
    Returns True if a delimiter was found, False if at file start or end.

    """
    if file.tell() == 0:
        return False
    last = None
    current = file.read(blocksize)
    if not current:
        return False
    full = last + current if None else current
    
    try:
        if delimiter in full:
            i = full.index(delimiter)
            file.seek((file.tell() - len(full) - i) + len(delimiter))
            return True
        if None(current) < blocksize:
            return False
    except (OSError, ValueError):
        pass

    last = full[-len(delimiter):]
    continue


def read_block(f = None, offset = None, length = None, delimiter = (None, False), split_before = ('f', 'IO[bytes]', 'offset', 'int', 'length', 'int | None', 'delimiter', 'bytes | None', 'split_before', 'bool', 'return', 'bytes')):
    """Read a block of bytes from a file

    Parameters
    ----------
    f: File
        Open file
    offset: int
        Byte offset to start read
    length: int
        Number of bytes to read, read through end of file if None
    delimiter: bytes (optional)
        Ensure reading starts and stops at delimiter bytestring
    split_before: bool (optional)
        Start/stop read *before* delimiter bytestring.


    If using the ``delimiter=`` keyword argument we ensure that the read
    starts and stops at delimiter boundaries that follow the locations
    ``offset`` and ``offset + length``.  If ``offset`` is zero then we
    start at zero, regardless of delimiter.  The bytestring returned WILL
    include the terminating delimiter string.

    Examples
    --------

    >>> from io import BytesIO  # doctest: +SKIP
    >>> f = BytesIO(b'Alice, 100\\nBob, 200\\nCharlie, 300')  # doctest: +SKIP
    >>> read_block(f, 0, 13)  # doctest: +SKIP
    b'Alice, 100\\nBo'

    >>> read_block(f, 0, 13, delimiter=b'\\n')  # doctest: +SKIP
    b'Alice, 100\\nBob, 200\\n'

    >>> read_block(f, 10, 10, delimiter=b'\\n')  # doctest: +SKIP
    b'Bob, 200\\nCharlie, 300'
    """
    pass
# WARNING: Decompyle incomplete


def tokenize(*args, **kwargs):
    """Deterministic token

    (modified from dask.base)

    >>> tokenize([1, 2, '3'])
    '9d71491b50023b06fc76928e6eddb952'

    >>> tokenize('Hello') == tokenize('Hello')
    True
    """
    if kwargs:
        args += (kwargs,)
    
    try:
        h = md5(str(args).encode())
    except ValueError:
        h = md5(str(args).encode(), usedforsecurity = False)

    return h.hexdigest()


def stringify_path(filepath = None):
    """Attempt to convert a path-like object to a string.

    Parameters
    ----------
    filepath: object to be converted

    Returns
    -------
    filepath_str: maybe a string version of the object

    Notes
    -----
    Objects supporting the fspath protocol are coerced according to its
    __fspath__ method.

    For backwards compatibility with older Python version, pathlib.Path
    objects are specially coerced.

    Any other object is passed through unchanged, which includes bytes,
    strings, buffers, or anything else that's not even path-like.
    """
    if isinstance(filepath, str):
        return filepath
    if None(filepath, '__fspath__'):
        return filepath.__fspath__()
    if None(filepath, 'path'):
        return filepath.path


def make_instance(cls = None, args = None, kwargs = None):
    pass
# WARNING: Decompyle incomplete


def common_prefix(paths = None):
    '''For a list of paths, find the shortest prefix common to all'''
    pass
# WARNING: Decompyle incomplete


def other_paths(paths = None, path2 = None, exists = None, flatten = (False, False)):
    '''In bulk file operations, construct a new file tree from a list of files

    Parameters
    ----------
    paths: list of str
        The input file tree
    path2: str or list of str
        Root to construct the new list in. If this is already a list of str, we just
        assert it has the right number of elements.
    exists: bool (optional)
        For a str destination, it is already exists (and is a dir), files should
        end up inside.
    flatten: bool (optional)
        Whether to flatten the input directory tree structure so that the output files
        are in the same directory.

    Returns
    -------
    list of str
    '''
    pass
# WARNING: Decompyle incomplete


def is_exception(obj = None):
    return isinstance(obj, BaseException)


def isfilelike(f = None):
    pass
# WARNING: Decompyle incomplete


def get_protocol(url = None):
    url = stringify_path(url)
    parts = re.split('(\\:\\:|\\://)', url, maxsplit = 1)
    if len(parts) > 1:
        return parts[0]


def get_file_extension(url = None):
    url = stringify_path(url)
    ext_parts = url.rsplit('.', 1)
    if len(ext_parts) > 1:
        return ext_parts[-1]


def can_be_local(path = None):
    '''Can the given URL be used with open_local?'''
    get_filesystem_class = get_filesystem_class
    import fsspec
    
    try:
        return getattr(get_filesystem_class(get_protocol(path)), 'local_file', False)
    except (ValueError, ImportError):
        return False



def get_package_version_without_import(name = None):
    '''For given package name, try to find the version without importing it

    Import and package.__version__ is still the backup here, so an import
    *might* happen.

    Returns either the version string, or None if the package
    or the version was not readily  found.
    '''
    if name in sys.modules:
        mod = sys.modules[name]
        if hasattr(mod, '__version__'):
            return mod.__version__
        
        try:
            return version(name)
        except:
            pass

        
        try:
            import importlib
            mod = importlib.import_module(name)
            return mod.__version__
        except (ImportError, AttributeError):
            return None



def setup_logging(logger = None, logger_name = None, level = None, clear = (None, None, 'DEBUG', True)):
    pass
# WARNING: Decompyle incomplete


def _unstrip_protocol(name = None, fs = None):
    return fs.unstrip_protocol(name)


def mirror_from(origin_name = None, methods = None):
    '''Mirror attributes and methods from the given
    origin_name attribute of the instance to the
    decorated class'''
    pass
# WARNING: Decompyle incomplete

nullcontext = (lambda obj = None: pass# WARNING: Decompyle incomplete
)()

def merge_offset_ranges(paths, starts = None, ends = None, max_gap = None, max_block = (0, None, True), sort = ('paths', 'list[str]', 'starts', 'list[int] | int', 'ends', 'list[int] | int', 'max_gap', 'int', 'max_block', 'int | None', 'sort', 'bool', 'return', 'tuple[list[str], list[int], list[int]]')):
