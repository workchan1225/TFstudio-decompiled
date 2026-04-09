# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _windows_cffi.pyc (Python 3.11)

from __future__ import annotations
import enum
from typing import TYPE_CHECKING, NewType, NoReturn, Protocol, TypeAlias, cast
if TYPE_CHECKING:
    import cffi
    CData: 'TypeAlias' = cffi.api.FFI.CData
    CType: 'TypeAlias' = cffi.api.FFI.CType
from _generated_windows_ffi import ffi
if not TYPE_CHECKING:
    CData: 'TypeAlias' = ffi.CData
    CType: 'TypeAlias' = ffi.CType
AlwaysNull: 'TypeAlias' = CData
Handle = NewType('Handle', CData)
HandleArray = NewType('HandleArray', CData)

class _Kernel32(Protocol):
    '''Statically typed version of the kernel32.dll functions we use.'''
    
    def CreateIoCompletionPort(self, FileHandle = None, ExistingCompletionPort = None, CompletionKey = None, NumberOfConcurrentThreads = ('FileHandle', 'Handle', 'ExistingCompletionPort', 'CData | AlwaysNull', 'CompletionKey', 'int', 'NumberOfConcurrentThreads', 'int', 'return', 'Handle')):
        pass

    
    def CreateEventA(self, lpEventAttributes = None, bManualReset = None, bInitialState = None, lpName = ('lpEventAttributes', 'AlwaysNull', 'bManualReset', 'bool', 'bInitialState', 'bool', 'lpName', 'AlwaysNull', 'return', 'Handle')):
        pass

    
    def SetFileCompletionNotificationModes(self = None, handle = None, flags = None):
        pass

    
    def PostQueuedCompletionStatus(self, CompletionPort = None, dwNumberOfBytesTransferred = None, dwCompletionKey = None, lpOverlapped = ('CompletionPort', 'Handle', 'dwNumberOfBytesTransferred', 'int', 'dwCompletionKey', 'int', 'lpOverlapped', 'CData | AlwaysNull', 'return', 'bool')):
        pass

    
    def CancelIoEx(self = None, hFile = None, lpOverlapped = None):
        pass

    
    def WriteFile(self, hFile, lpBuffer = None, nNumberOfBytesToWrite = None, lpNumberOfBytesWritten = None, lpOverlapped = ('hFile', 'Handle', 'lpBuffer', 'CData', 'nNumberOfBytesToWrite', 'int', 'lpNumberOfBytesWritten', 'AlwaysNull', 'lpOverlapped', '_Overlapped', 'return', 'bool')):
        pass

    
    def ReadFile(self, hFile, lpBuffer = None, nNumberOfBytesToRead = None, lpNumberOfBytesRead = None, lpOverlapped = ('hFile', 'Handle', 'lpBuffer', 'CData', 'nNumberOfBytesToRead', 'int', 'lpNumberOfBytesRead', 'AlwaysNull', 'lpOverlapped', '_Overlapped', 'return', 'bool')):
        pass

    
    def GetQueuedCompletionStatusEx(self, CompletionPort, lpCompletionPortEntries, ulCount = None, ulNumEntriesRemoved = None, dwMilliseconds = None, fAlertable = ('CompletionPort', 'Handle', 'lpCompletionPortEntries', 'CData', 'ulCount', 'int', 'ulNumEntriesRemoved', 'CData', 'dwMilliseconds', 'int', 'fAlertable', 'bool | int', 'return', 'CData')):
        pass

    
    def CreateFileW(self, lpFileName, dwDesiredAccess, dwShareMode, lpSecurityAttributes = None, dwCreationDisposition = None, dwFlagsAndAttributes = None, hTemplateFile = ('lpFileName', 'CData', 'dwDesiredAccess', 'FileFlags', 'dwShareMode', 'FileFlags', 'lpSecurityAttributes', 'AlwaysNull', 'dwCreationDisposition', 'FileFlags', 'dwFlagsAndAttributes', 'FileFlags', 'hTemplateFile', 'AlwaysNull', 'return', 'Handle')):
        pass

    
    def WaitForSingleObject(self = None, hHandle = None, dwMilliseconds = None):
        pass

    
    def WaitForMultipleObjects(self, nCount = None, lpHandles = None, bWaitAll = None, dwMilliseconds = ('nCount', 'int', 'lpHandles', 'HandleArray', 'bWaitAll', 'bool', 'dwMilliseconds', 'int', 'return', 'ErrorCodes')):
        pass

    
    def SetEvent(self = None, handle = None):
        pass

    
    def CloseHandle(self = None, handle = None):
        pass

    
    def DeviceIoControl(self, hDevice, dwIoControlCode, lpInBuffer, nInBufferSize, lpOutBuffer = None, nOutBufferSize = None, lpBytesReturned = None, lpOverlapped = ('hDevice', 'Handle', 'dwIoControlCode', 'int', 'lpInBuffer', 'AlwaysNull', 'nInBufferSize', 'int', 'lpOutBuffer', 'AlwaysNull', 'nOutBufferSize', 'int', 'lpBytesReturned', 'AlwaysNull', 'lpOverlapped', 'CData', 'return', 'bool')):
        pass



class _Nt(Protocol):
    '''Statically typed version of the dtdll.dll functions we use.'''
    
    def RtlNtStatusToDosError(self = None, status = None):
        pass



class _Ws2(Protocol):
    '''Statically typed version of the ws2_32.dll functions we use.'''
    
    def WSAGetLastError(self = None):
        pass

    
    def WSAIoctl(self, socket, dwIoControlCode, lpvInBuffer, cbInBuffer, lpvOutBuffer, cbOutBuffer = None, lpcbBytesReturned = None, lpOverlapped = None, lpCompletionRoutine = ('socket', 'CData', 'dwIoControlCode', 'WSAIoctls', 'lpvInBuffer', 'AlwaysNull', 'cbInBuffer', 'int', 'lpvOutBuffer', 'CData', 'cbOutBuffer', 'int', 'lpcbBytesReturned', 'CData', 'lpOverlapped', 'AlwaysNull', 'lpCompletionRoutine', 'AlwaysNull', 'return', 'int')):
        pass



class _DummyStruct(Protocol):
    OffsetHigh: 'int' = '_DummyStruct'


class _DummyUnion(Protocol):
    Pointer: 'object' = '_DummyUnion'


class _Overlapped(Protocol):
    hEvent: 'Handle' = '_Overlapped'

kernel32 = cast('_Kernel32', ffi.dlopen('kernel32.dll'))
ntdll = cast('_Nt', ffi.dlopen('ntdll.dll'))
ws2_32 = cast('_Ws2', ffi.dlopen('ws2_32.dll'))
INVALID_HANDLE_VALUE = Handle(ffi.cast('HANDLE', -1))

class ErrorCodes(enum.IntEnum):
    STATUS_TIMEOUT = 258
    WAIT_TIMEOUT = 258
    WAIT_ABANDONED = 128
    WAIT_OBJECT_0 = 0
    WAIT_FAILED = 0xFFFFFFFF
    ERROR_IO_PENDING = 997
    ERROR_OPERATION_ABORTED = 995
    ERROR_ABANDONED_WAIT_0 = 735
    ERROR_INVALID_HANDLE = 6
    ERROR_INVALID_PARAMETER = 87
    ERROR_NOT_FOUND = 1168
    ERROR_NOT_SOCKET = 10038


class FileFlags(enum.IntFlag):
    GENERIC_READ = 0x80000000
    SYNCHRONIZE = 1048576
    FILE_FLAG_OVERLAPPED = 1073741824
    FILE_SHARE_READ = 1
    FILE_SHARE_WRITE = 2
    FILE_SHARE_DELETE = 4
    CREATE_NEW = 1
    CREATE_ALWAYS = 2
    OPEN_EXISTING = 3
    OPEN_ALWAYS = 4
    TRUNCATE_EXISTING = 5


class AFDPollFlags(enum.IntFlag):
    AFD_POLL_RECEIVE = 1
    AFD_POLL_RECEIVE_EXPEDITED = 2
    AFD_POLL_SEND = 4
    AFD_POLL_DISCONNECT = 8
    AFD_POLL_ABORT = 16
    AFD_POLL_LOCAL_CLOSE = 32
    AFD_POLL_CONNECT = 64
    AFD_POLL_ACCEPT = 128
    AFD_POLL_CONNECT_FAIL = 256
    AFD_POLL_QOS = 512
    AFD_POLL_GROUP_QOS = 1024
    AFD_POLL_ROUTING_INTERFACE_CHANGE = 2048
    AFD_POLL_EVENT_ADDRESS_LIST_CHANGE = 4096


class WSAIoctls(enum.IntEnum):
    SIO_BASE_HANDLE = 1207959586
    SIO_BSP_HANDLE_SELECT = 1207959580
    SIO_BSP_HANDLE_POLL = 1207959581


class CompletionModes(enum.IntFlag):
    FILE_SKIP_COMPLETION_PORT_ON_SUCCESS = 1
    FILE_SKIP_SET_EVENT_ON_HANDLE = 2


class IoControlCodes(enum.IntEnum):
    IOCTL_AFD_POLL = 73764


def _handle(obj = None):
    if isinstance(obj, int):
        return Handle(ffi.cast('HANDLE', obj))
    return None(obj)


def handle_array(count = None):
    '''Make an array of handles.'''
    return HandleArray(ffi.new(f'''HANDLE[{count}]'''))


def raise_winerror(winerror = None, *, filename, filename2):
    pass
# WARNING: Decompyle incomplete
