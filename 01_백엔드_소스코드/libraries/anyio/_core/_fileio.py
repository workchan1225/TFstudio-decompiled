# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _fileio.pyc (Python 3.11)

from __future__ import annotations
import os
import pathlib
import sys
from collections.abc import AsyncIterator, Callable, Iterable, Iterator, Sequence
from dataclasses import dataclass
from functools import partial
from os import PathLike
from typing import IO, TYPE_CHECKING, Any, AnyStr, ClassVar, Final, Generic, overload
from  import to_thread
from abc import AsyncResource
if TYPE_CHECKING:
    from types import ModuleType
    from _typeshed import OpenBinaryMode, OpenTextMode, ReadableBuffer, WriteableBuffer
else:
    ReadableBuffer = object
    OpenBinaryMode = object
    OpenTextMode = object
    WriteableBuffer = object

def AsyncFile():
    '''AsyncFile'''
    __doc__ = '\n    An asynchronous file object.\n\n    This class wraps a standard file object and provides async friendly versions of the\n    following blocking methods (where available on the original file object):\n\n    * read\n    * read1\n    * readline\n    * readlines\n    * readinto\n    * readinto1\n    * write\n    * writelines\n    * truncate\n    * seek\n    * tell\n    * flush\n\n    All other methods are directly passed through.\n\n    This class supports the asynchronous context manager protocol which closes the\n    underlying file at the end of the context block.\n\n    This class also supports asynchronous iteration::\n\n        async with await open_file(...) as f:\n            async for line in f:\n                print(line)\n    '
    
    def __init__(self = None, fp = None):
        self._fp = fp

    
    def __getattr__(self = None, name = None):
        return getattr(self._fp, name)

    wrapped = (lambda self = None: self._fp)()
    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def read(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def read1(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def readline(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def readlines(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def readinto(self = None, b = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def readinto1(self = None, b = None):
        pass
    # WARNING: Decompyle incomplete

    write = (lambda self = None, b = None: pass# WARNING: Decompyle incomplete
)()
    write = (lambda self = None, b = None: pass# WARNING: Decompyle incomplete
)()
    
    async def write(self = None, b = None):
        pass
    # WARNING: Decompyle incomplete

    writelines = (lambda self = None, lines = None: pass# WARNING: Decompyle incomplete
)()
    writelines = (lambda self = None, lines = None: pass# WARNING: Decompyle incomplete
)()
    
    async def writelines(self = None, lines = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def truncate(self = None, size = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def seek(self = None, offset = None, whence = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def tell(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def flush(self = None):
        pass
    # WARNING: Decompyle incomplete


AsyncFile = <NODE:27>(AsyncFile, 'AsyncFile', AsyncResource, Generic[AnyStr])
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (..., ..., ..., ..., ..., ...), opener = ('file', 'str | PathLike[str] | int', 'mode', 'OpenBinaryMode', 'buffering', 'int', 'encoding', 'str | None', 'errors', 'str | None', 'newline', 'str | None', 'closefd', 'bool', 'opener', 'Callable[[str, int], int] | None', 'return', 'AsyncFile[bytes]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (..., ..., ..., ..., ..., ..., ...), opener = ('file', 'str | PathLike[str] | int', 'mode', 'OpenTextMode', 'buffering', 'int', 'encoding', 'str | None', 'errors', 'str | None', 'newline', 'str | None', 'closefd', 'bool', 'opener', 'Callable[[str, int], int] | None', 'return', 'AsyncFile[str]'): pass# WARNING: Decompyle incomplete
)()

async def open_file(file, mode, buffering, encoding = None, errors = None, newline = None, closefd = ('r', -1, None, None, None, True, None), opener = ('file', 'str | PathLike[str] | int', 'mode', 'str', 'buffering', 'int', 'encoding', 'str | None', 'errors', 'str | None', 'newline', 'str | None', 'closefd', 'bool', 'opener', 'Callable[[str, int], int] | None', 'return', 'AsyncFile[Any]')):
    '''
    Open a file asynchronously.

    The arguments are exactly the same as for the builtin :func:`open`.

    :return: an asynchronous file object

    '''
    pass
# WARNING: Decompyle incomplete


def wrap_file(file = None):
    '''
    Wrap an existing file as an asynchronous file.

    :param file: an existing file-like object
    :return: an asynchronous file object

    '''
    return AsyncFile(file)


def _PathIterator():
    '''_PathIterator'''
    iterator: 'Iterator[PathLike[str]]' = '_PathIterator'
    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete


_PathIterator = <NODE:27>(_PathIterator, '_PathIterator', AsyncIterator['Path'])()

class Path:
