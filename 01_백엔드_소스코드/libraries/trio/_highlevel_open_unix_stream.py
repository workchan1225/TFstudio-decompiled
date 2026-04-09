# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _highlevel_open_unix_stream.pyc (Python 3.11)

from __future__ import annotations
import os
from contextlib import contextmanager
from typing import TYPE_CHECKING, Protocol, TypeVar
import trio
from trio.socket import SOCK_STREAM, socket
if TYPE_CHECKING:
    from collections.abc import Generator

class Closable(Protocol):
    
    def close(self = None):
        pass


CloseT = TypeVar('CloseT', bound = Closable)

try:
    from trio.socket import AF_UNIX
    has_unix = True
except ImportError:
    has_unix = False

close_on_error = (lambda obj = None: pass# WARNING: Decompyle incomplete
)()

async def open_unix_socket(filename = None):
    '''Opens a connection to the specified
    `Unix domain socket <https://en.wikipedia.org/wiki/Unix_domain_socket>`__.

    You must have read/write permission on the specified file to connect.

    Args:
      filename (str or bytes): The filename to open the connection to.

    Returns:
      SocketStream: a :class:`~trio.abc.Stream` connected to the given file.

    Raises:
      OSError: If the socket file could not be connected to.
      RuntimeError: If AF_UNIX sockets are not supported.
    '''
    pass
# WARNING: Decompyle incomplete
