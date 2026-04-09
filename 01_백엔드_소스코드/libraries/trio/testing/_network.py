# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _network.pyc (Python 3.11)

from  import socket as tsocket
from _highlevel_socket import SocketListener, SocketStream

async def open_stream_to_socket_listener(socket_listener = None):
    '''Connect to the given :class:`~trio.SocketListener`.

    This is particularly useful in tests when you want to let a server pick
    its own port, and then connect to it::

        listeners = await trio.open_tcp_listeners(0)
        client = await trio.testing.open_stream_to_socket_listener(listeners[0])

    Args:
      socket_listener (~trio.SocketListener): The
          :class:`~trio.SocketListener` to connect to.

    Returns:
      SocketStream: a stream connected to the given listener.

    '''
    pass
# WARNING: Decompyle incomplete
