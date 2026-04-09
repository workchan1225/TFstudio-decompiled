# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _file_io.pyc (Python 3.11)

from __future__ import annotations
import io
from collections.abc import Callable, Iterable
from functools import partial
from typing import IO, TYPE_CHECKING, Any, AnyStr, BinaryIO, Generic, Literal, TypeVar, Union, overload
import trio
from _util import async_wraps
from abc import AsyncResource
if TYPE_CHECKING:
    from _typeshed import OpenBinaryMode, OpenBinaryModeReading, OpenBinaryModeUpdating, OpenBinaryModeWriting, OpenTextMode, StrOrBytesPath
    from _sync import CapacityLimiter
_FILE_SYNC_ATTRS: 'set[str]' = {
    'raw',
    'mode',
    'name',
    'buffer',
    'closed',
    'errors',
    'fileno',
    'isatty',
    'closefd',
    'encoding',
    'getvalue',
    'newlines',
    'readable',
    'seekable',
    'writable',
    'getbuffer',
    'line_buffering'}
_FILE_ASYNC_METHODS: 'set[str]' = {
    'peek',
    'read',
    'seek',
    'tell',
    'flush',
    'read1',
    'write',
    'readall',
    'readinto',
    'readline',
    'truncate',
    'readinto1',
    'readlines',
    'writelines'}
FileT = TypeVar('FileT')
FileT_co = TypeVar('FileT_co', covariant = True)
T = TypeVar('T')
T_co = TypeVar('T_co', covariant = True)
T_contra = TypeVar('T_contra', contravariant = True)
AnyStr_co = TypeVar('AnyStr_co', str, bytes, covariant = True)
AnyStr_contra = TypeVar('AnyStr_contra', str, bytes, contravariant = True)
if TYPE_CHECKING:
    from typing_extensions import Buffer, Protocol
    
    class _HasClosed(Protocol):
        closed = (lambda self = None: pass)()

    
    class _HasEncoding(Protocol):
        encoding = (lambda self = None: pass)()

    
    class _HasErrors(Protocol):
        errors = (lambda self = None: pass)()

    
    class _HasFileNo(Protocol):
        
        def fileno(self = None):
            pass


    
    class _HasIsATTY(Protocol):
        
        def isatty(self = None):
            pass


    
    def _HasNewlines():
        '''_HasNewlines'''
        newlines = (lambda self = None: pass)()

    _HasNewlines = <NODE:27>(_HasNewlines, '_HasNewlines', Protocol[T_co])
    
    class _HasReadable(Protocol):
        
        def readable(self = None):
            pass


    
    class _HasSeekable(Protocol):
        
        def seekable(self = None):
            pass


    
    class _HasWritable(Protocol):
        
        def writable(self = None):
            pass


    
    class _HasBuffer(Protocol):
        buffer = (lambda self = None: pass)()

    
    class _HasRaw(Protocol):
        raw = (lambda self = None: pass)()

    
    class _HasLineBuffering(Protocol):
        line_buffering = (lambda self = None: pass)()

    
    class _HasCloseFD(Protocol):
        closefd = (lambda self = None: pass)()

    
    class _HasName(Protocol):
        name = (lambda self = None: pass)()

    
    class _HasMode(Protocol):
        mode = (lambda self = None: pass)()

    
    def _CanGetValue():
        '''_CanGetValue'''
        
        def getvalue(self = None):
            pass


    _CanGetValue = <NODE:27>(_CanGetValue, '_CanGetValue', Protocol[AnyStr_co])
    
    class _CanGetBuffer(Protocol):
        
        def getbuffer(self = None):
            pass


    
    class _CanFlush(Protocol):
        
        def flush(self = None):
            pass


    
    def _CanRead():
        '''_CanRead'''
        
        def read(self = None, size = None):
            pass


    _CanRead = <NODE:27>(_CanRead, '_CanRead', Protocol[AnyStr_co])
    
    class _CanRead1(Protocol):
        
        def read1(self = None, size = None):
            pass


    
    def _CanReadAll():
        '''_CanReadAll'''
        
        def readall(self = None):
            pass


    _CanReadAll = <NODE:27>(_CanReadAll, '_CanReadAll', Protocol[AnyStr_co])
    
    class _CanReadInto(Protocol):
        
        def readinto(self = None, buf = None):
            pass


    
    class _CanReadInto1(Protocol):
        
        def readinto1(self = None, buffer = None):
            pass


    
    def _CanReadLine():
        '''_CanReadLine'''
        
        def readline(self = None, size = None):
            pass


    _CanReadLine = <NODE:27>(_CanReadLine, '_CanReadLine', Protocol[AnyStr_co])
    
    def _CanReadLines():
        '''_CanReadLines'''
        
        def readlines(self = None, hint = None):
            pass


    _CanReadLines = <NODE:27>(_CanReadLines, '_CanReadLines', Protocol[AnyStr])
    
    class _CanSeek(Protocol):
        
        def seek(self = None, target = None, whence = None):
            pass


    
    class _CanTell(Protocol):
        
        def tell(self = None):
            pass


    
    class _CanTruncate(Protocol):
        
        def truncate(self = None, size = None):
            pass


    
    def _CanWrite():
        '''_CanWrite'''
        
        def write(self = None, data = None):
            pass


    _CanWrite = <NODE:27>(_CanWrite, '_CanWrite', Protocol[T_contra])
    
    def _CanWriteLines():
        '''_CanWriteLines'''
        
        def writelines(self = None, lines = None):
            pass


    _CanWriteLines = <NODE:27>(_CanWriteLines, '_CanWriteLines', Protocol[T_contra])
    
    def _CanPeek():
        '''_CanPeek'''
        
        def peek(self = None, size = None):
            pass


    _CanPeek = <NODE:27>(_CanPeek, '_CanPeek', Protocol[AnyStr_co])
    
    def _CanDetach():
        '''_CanDetach'''
        
        def detach(self = None):
            pass


    _CanDetach = <NODE:27>(_CanDetach, '_CanDetach', Protocol[T_co])
    
    class _CanClose(Protocol):
        
        def close(self = None):
            pass



def AsyncIOWrapper():
    '''AsyncIOWrapper'''
    pass
# WARNING: Decompyle incomplete

AsyncIOWrapper = <NODE:27>(AsyncIOWrapper, 'AsyncIOWrapper', AsyncResource, Generic[FileT_co])
_OpenFile = Union[('StrOrBytesPath', int)]
_Opener = Callable[([
    str,
    int], int)]
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = ('r', -1, None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'OpenTextMode', 'buffering', 'int', 'encoding', 'str | None', 'errors', 'str | None', 'newline', 'str | None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[io.TextIOWrapper]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'OpenBinaryMode', 'buffering', 'Literal[0]', 'encoding', 'None', 'errors', 'None', 'newline', 'None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[io.FileIO]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (-1, None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'OpenBinaryModeUpdating', 'buffering', 'Literal[-1, 1]', 'encoding', 'None', 'errors', 'None', 'newline', 'None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[io.BufferedRandom]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (-1, None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'OpenBinaryModeWriting', 'buffering', 'Literal[-1, 1]', 'encoding', 'None', 'errors', 'None', 'newline', 'None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[io.BufferedWriter]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (-1, None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'OpenBinaryModeReading', 'buffering', 'Literal[-1, 1]', 'encoding', 'None', 'errors', 'None', 'newline', 'None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[io.BufferedReader]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'OpenBinaryMode', 'buffering', 'int', 'encoding', 'None', 'errors', 'None', 'newline', 'None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[BinaryIO]'): pass# WARNING: Decompyle incomplete
)()
open_file = (lambda file, mode, buffering, encoding = None, errors = None, newline = overload, closefd = (-1, None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'str', 'buffering', 'int', 'encoding', 'str | None', 'errors', 'str | None', 'newline', 'str | None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[IO[Any]]'): pass# WARNING: Decompyle incomplete
)()

async def open_file(file, mode, buffering, encoding = None, errors = None, newline = None, closefd = ('r', -1, None, None, None, True, None), opener = ('file', '_OpenFile', 'mode', 'str', 'buffering', 'int', 'encoding', 'str | None', 'errors', 'str | None', 'newline', 'str | None', 'closefd', 'bool', 'opener', '_Opener | None', 'return', 'AsyncIOWrapper[object]')):
    '''Asynchronous version of :func:`open`.

    Returns:
        An :term:`asynchronous file object`

    Example::

        async with await trio.open_file(filename) as f:
            async for line in f:
                pass

        assert f.closed

    See also:
      :func:`trio.Path.open`

    '''
    pass
# WARNING: Decompyle incomplete


def wrap_file(file = None):
    """This wraps any file object in a wrapper that provides an asynchronous
    file object interface.

    Args:
        file: a :term:`file object`

    Returns:
        An :term:`asynchronous file object` that wraps ``file``

    Example::

        async_file = trio.wrap_file(StringIO('asdf'))

        assert await async_file.read() == 'asdf'

    """
    pass
# WARNING: Decompyle incomplete
