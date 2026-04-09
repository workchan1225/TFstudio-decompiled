# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from __future__ import annotations
import os
import sys
from typing import TYPE_CHECKING
import trio
from  import _core, _subprocess
from _abc import ReceiveStream, SendStream
_wait_child_exiting_error: 'ImportError | None' = None
_create_child_pipe_error: 'ImportError | None' = None
if TYPE_CHECKING:
    
    class ClosableSendStream(SendStream):
        
        def close(self = None):
            pass


    
    class ClosableReceiveStream(ReceiveStream):
        
        def close(self = None):
            pass



async def wait_child_exiting(process = None):
    """Block until the child process managed by ``process`` is exiting.

    It is invalid to call this function if the process has already
    been waited on; that is, ``process.returncode`` must be None.

    When this function returns, it indicates that a call to
    :meth:`subprocess.Popen.wait` will immediately be able to
    return the process's exit status. The actual exit status is not
    consumed by this call, since :class:`~subprocess.Popen` wants
    to be able to do that itself.
    """
    pass
# WARNING: Decompyle incomplete


def create_pipe_to_child_stdin():
    """Create a new pipe suitable for sending data from this
    process to the standard input of a child we're about to spawn.

    Returns:
      A pair ``(trio_end, subprocess_end)`` where ``trio_end`` is a
      :class:`~trio.abc.SendStream` and ``subprocess_end`` is
      something suitable for passing as the ``stdin`` argument of
      :class:`subprocess.Popen`.
    """
    raise NotImplementedError, _create_child_pipe_error


def create_pipe_from_child_output():
    """Create a new pipe suitable for receiving data into this
    process from the standard output or error stream of a child
    we're about to spawn.

    Returns:
      A pair ``(trio_end, subprocess_end)`` where ``trio_end`` is a
      :class:`~trio.abc.ReceiveStream` and ``subprocess_end`` is
      something suitable for passing as the ``stdin`` argument of
      :class:`subprocess.Popen`.
    """
    raise NotImplementedError, _create_child_pipe_error


try:
    if sys.platform == 'win32':
        from windows import wait_child_exiting
    elif sys.platform != 'linux':
        if TYPE_CHECKING or hasattr(_core, 'wait_kevent'):
            from kqueue import wait_child_exiting
        else:
            from waitid import wait_child_exiting
    else:
        except ImportError:
            ex = None
            _wait_child_exiting_error = ex
            ex = None
            del ex
        except:
            ex = None
            del ex
        
        try:
            if TYPE_CHECKING:
                return None
            if None.name == 'posix':
                
                def create_pipe_to_child_stdin():
                    (rfd, wfd) = os.pipe()
                    return (trio.lowlevel.FdStream(wfd), rfd)

                
                def create_pipe_from_child_output():
                    (rfd, wfd) = os.pipe()
                    return (trio.lowlevel.FdStream(rfd), wfd)

                return None
            if None.name == 'nt':
                import msvcrt
                from asyncio.windows_utils import pipe as windows_pipe
                from _windows_pipes import PipeReceiveStream, PipeSendStream
                
                def create_pipe_to_child_stdin():
                    (rh, wh) = windows_pipe(overlapped = (False, True))
                    return (PipeSendStream(wh), msvcrt.open_osfhandle(rh, os.O_RDONLY))

                
                def create_pipe_from_child_output():
                    (rh, wh) = windows_pipe(overlapped = (True, False))
                    return (PipeReceiveStream(rh), msvcrt.open_osfhandle(wh, 0))

                return None
            raise ImportError('pipes not implemented on this platform')
        except ImportError:
            ex = None
            _create_child_pipe_error = ex
            ex = None
            del ex
            return None
            ex = None
            del ex
