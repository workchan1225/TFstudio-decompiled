# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

from __future__ import annotations
import sys
from collections.abc import Generator
from textwrap import dedent
from typing import Any
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup

class BrokenResourceError(Exception):
    '''
    Raised when trying to use a resource that has been rendered unusable due to external
    causes (e.g. a send stream whose peer has disconnected).
    '''
    pass


class BrokenWorkerProcess(Exception):
    '''
    Raised by :meth:`~anyio.to_process.run_sync` if the worker process terminates abruptly or
    otherwise misbehaves.
    '''
    pass


class BrokenWorkerInterpreter(Exception):
    pass
# WARNING: Decompyle incomplete


class BusyResourceError(Exception):
    pass
# WARNING: Decompyle incomplete


class ClosedResourceError(Exception):
    '''Raised when trying to use a resource that has been closed.'''
    pass


class ConnectionFailed(OSError):
    '''
    Raised when a connection attempt fails.

    .. note:: This class inherits from :exc:`OSError` for backwards compatibility.
    '''
    pass


def iterate_exceptions(exception = None):
    pass
# WARNING: Decompyle incomplete


class DelimiterNotFound(Exception):
    pass
# WARNING: Decompyle incomplete


class EndOfStream(Exception):
    '''
    Raised when trying to read from a stream that has been closed from the other end.
    '''
    pass


class IncompleteRead(Exception):
    pass
# WARNING: Decompyle incomplete


class TypedAttributeLookupError(LookupError):
    '''
    Raised by :meth:`~anyio.TypedAttributeProvider.extra` when the given typed attribute
    is not found and no default value has been given.
    '''
    pass


class WouldBlock(Exception):
    '''Raised by ``X_nowait`` functions if ``X()`` would block.'''
    pass


class NoEventLoopError(RuntimeError):
    '''
    Raised by :func:`.from_thread.run` and :func:`.from_thread.run_sync` if
    not calling from an AnyIO worker thread, and no ``token`` was passed.
    '''
    pass


class RunFinishedError(RuntimeError):
    pass
# WARNING: Decompyle incomplete
