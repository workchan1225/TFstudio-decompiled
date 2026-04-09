# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _io_windows.pyc (Python 3.11)

from __future__ import annotations
import enum
import itertools
import socket
import sys
from contextlib import contextmanager
from typing import TYPE_CHECKING, Literal, Protocol, TypeAlias, TypeVar, cast
import attrs
from outcome import Value
from  import _core
from _io_common import wake_all
from _run import _public
from _windows_cffi import INVALID_HANDLE_VALUE, AFDPollFlags, CData, CompletionModes, CType, ErrorCodes, FileFlags, Handle, IoControlCodes, WSAIoctls, _handle, _Overlapped, ffi, kernel32, ntdll, raise_winerror, ws2_32
if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    from typing_extensions import Buffer
    from _file_io import _HasFileNo
    from _traps import Abort, RaiseCancelT
    from _unbounded_queue import UnboundedQueue
EventResult: 'TypeAlias' = int
T = TypeVar('T')

class CKeys(enum.IntEnum):
    AFD_POLL = 0
    WAIT_OVERLAPPED = 1
    LATE_CANCEL = 2
    FORCE_WAKEUP = 3
    USER_DEFINED = 4

READABLE_FLAGS = AFDPollFlags.AFD_POLL_RECEIVE | AFDPollFlags.AFD_POLL_ACCEPT | AFDPollFlags.AFD_POLL_DISCONNECT | AFDPollFlags.AFD_POLL_ABORT | AFDPollFlags.AFD_POLL_LOCAL_CLOSE
WRITABLE_FLAGS = AFDPollFlags.AFD_POLL_SEND | AFDPollFlags.AFD_POLL_CONNECT_FAIL | AFDPollFlags.AFD_POLL_ABORT | AFDPollFlags.AFD_POLL_LOCAL_CLOSE
AFDWaiters = <NODE:12>()

class _AFDHandle(Protocol):
    Events: 'int' = '_AFDHandle'


class _AFDPollInfo(Protocol):
    Handles: 'list[_AFDHandle]' = '_AFDPollInfo'

AFDPollOp = <NODE:12>()
MAX_AFD_GROUP_SIZE = 500
AFDGroup = <NODE:12>()
# WARNING: Decompyle incomplete
