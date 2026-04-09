# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _highlevel_socket.pyc (Python 3.11)

from __future__ import annotations
import errno
from contextlib import contextmanager, suppress
from typing import TYPE_CHECKING, overload
import trio
from  import socket as tsocket
from _util import ConflictDetector, final
from abc import HalfCloseableStream, Listener
if TYPE_CHECKING:
    from collections.abc import Generator
    from _socket import SocketType
import sys
if sys.version_info >= (3, 12):
    from collections.abc import Buffer
elif TYPE_CHECKING:
    from typing_extensions import Buffer
DEFAULT_RECEIVE_SIZE = 65536
_closed_stream_errnos = {
    errno.EBADF,
    errno.ENOTSOCK}
_translate_socket_errors_to_stream_errors = (lambda : pass# WARNING: Decompyle incomplete
)()
SocketStream = <NODE:12>()
_ignorable_accept_errno_names = [
    'EPERM',
    'ECONNABORTED',
    'EPROTO',
    'ENETDOWN',
    'ENOPROTOOPT',
    'EHOSTDOWN',
    'ENONET',
    'EHOSTUNREACH',
    'EOPNOTSUPP',
    'ENETUNREACH',
    'ENOSR',
    'ESOCKTNOSUPPORT',
    'EPROTONOSUPPORT',
    'ETIMEDOUT',
    'ECONNRESET']
_ignorable_accept_errnos: 'set[int]' = set()
for name in _ignorable_accept_errno_names:
    suppress(AttributeError)
    _ignorable_accept_errnos.add(getattr(errno, name))
    None(None, None)
with None:
    if not final:
        pass
continue

def SocketListener():
    '''SocketListener'''
    __doc__ = 'A :class:`~trio.abc.Listener` that uses a listening socket to accept\n    incoming connections as :class:`SocketStream` objects.\n\n    Args:\n      socket: The Trio socket object to wrap. Must have type ``SOCK_STREAM``,\n          and be listening.\n\n    Note that the :class:`SocketListener` "takes ownership" of the given\n    socket; closing the :class:`SocketListener` will also close the socket.\n\n    .. attribute:: socket\n\n       The Trio socket object that this stream wraps.\n\n    '
    
    def __init__(self = None, socket = None):
        if not isinstance(socket, tsocket.SocketType):
            raise TypeError('SocketListener requires a Trio socket object')
        if socket.type != tsocket.SOCK_STREAM:
            raise ValueError('SocketListener requires a SOCK_STREAM socket')
        
        try:
            listening = socket.getsockopt(tsocket.SOL_SOCKET, tsocket.SO_ACCEPTCONN)
            if not listening:
                raise ValueError('SocketListener requires a listening socket')
        except OSError:
            pass

        self.socket = socket

    
    async def accept(self = None):
        '''Accept an incoming connection.

        Returns:
          :class:`SocketStream`

        Raises:
          OSError: if the underlying call to ``accept`` raises an unexpected
              error.
          ClosedResourceError: if you already closed the socket.

        This method handles routine errors like ``ECONNABORTED``, but passes
        other errors on to its caller. In particular, it does *not* make any
        special effort to handle resource exhaustion errors like ``EMFILE``,
        ``ENFILE``, ``ENOBUFS``, ``ENOMEM``.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        '''Close this listener and its underlying socket.'''
        pass
    # WARNING: Decompyle incomplete


SocketListener = <NODE:27>(SocketListener, 'SocketListener', Listener[SocketStream])()
