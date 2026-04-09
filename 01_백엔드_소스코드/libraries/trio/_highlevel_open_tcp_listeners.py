# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _highlevel_open_tcp_listeners.pyc (Python 3.11)

from __future__ import annotations
import errno
import sys
from typing import TYPE_CHECKING
import trio
from trio import TaskStatus
from  import socket as tsocket
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable
if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup

def _compute_backlog(backlog = None):
    pass
# WARNING: Decompyle incomplete


async def open_tcp_listeners(port = None, *, host, backlog):
    '''Create :class:`SocketListener` objects to listen for TCP connections.

    Args:

      port (int): The port to listen on.

          If you use 0 as your port, then the kernel will automatically pick
          an arbitrary open port. But be careful: if you use this feature when
          binding to multiple IP addresses, then each IP address will get its
          own random port, and the returned listeners will probably be
          listening on different ports. In particular, this will happen if you
          use ``host=None`` – which is the default – because in this case
          :func:`open_tcp_listeners` will bind to both the IPv4 wildcard
          address (``0.0.0.0``) and also the IPv6 wildcard address (``::``).

      host (str, bytes, or None): The local interface to bind to. This is
          passed to :func:`~socket.getaddrinfo` with the ``AI_PASSIVE`` flag
          set.

          If you want to bind to the wildcard address on both IPv4 and IPv6,
          in order to accept connections on all available interfaces, then
          pass ``None``. This is the default.

          If you have a specific interface you want to bind to, pass its IP
          address or hostname here. If a hostname resolves to multiple IP
          addresses, this function will open one listener on each of them.

          If you want to use only IPv4, or only IPv6, but want to accept on
          all interfaces, pass the family-specific wildcard address:
          ``"0.0.0.0"`` for IPv4-only and ``"::"`` for IPv6-only.

      backlog (int or None): The listen backlog to use. If you leave this as
          ``None`` then Trio will pick a good default. (Currently: whatever
          your system has configured as the maximum backlog.)

    Returns:
      list of :class:`SocketListener`

    Raises:
      :class:`TypeError` if invalid arguments.

    '''
    pass
# WARNING: Decompyle incomplete


async def serve_tcp(handler = None, port = None, *, host, backlog, handler_nursery, task_status):
    '''Listen for incoming TCP connections, and for each one start a task
    running ``handler(stream)``.

    This is a thin convenience wrapper around :func:`open_tcp_listeners` and
    :func:`serve_listeners` – see them for full details.

    .. warning::

       If ``handler`` raises an exception, then this function doesn\'t do
       anything special to catch it – so by default the exception will
       propagate out and crash your server. If you don\'t want this, then catch
       exceptions inside your ``handler``, or use a ``handler_nursery`` object
       that responds to exceptions in some other way.

    When used with ``nursery.start`` you get back the newly opened listeners.
    So, for example, if you want to start a server in your test suite and then
    connect to it to check that it\'s working properly, you can use something
    like::

        from trio import SocketListener, SocketStream
        from trio.testing import open_stream_to_socket_listener

        async with trio.open_nursery() as nursery:
            listeners: list[SocketListener] = await nursery.start(serve_tcp, handler, 0)
            client_stream: SocketStream = await open_stream_to_socket_listener(listeners[0])

            # Then send and receive data on \'client_stream\', for example:
            await client_stream.send_all(b"GET / HTTP/1.0\\r\\n\\r\\n")

    This avoids several common pitfalls:

    1. It lets the kernel pick a random open port, so your test suite doesn\'t
       depend on any particular port being open.

    2. It waits for the server to be accepting connections on that port before
       ``start`` returns, so there\'s no race condition where the incoming
       connection arrives before the server is ready.

    3. It uses the Listener object to find out which port was picked, so it
       can connect to the right place.

    Args:
      handler: The handler to start for each incoming connection. Passed to
          :func:`serve_listeners`.

      port: The port to listen on. Use 0 to let the kernel pick an open port.
          Passed to :func:`open_tcp_listeners`.

      host (str, bytes, or None): The host interface to listen on; use
          ``None`` to bind to the wildcard address. Passed to
          :func:`open_tcp_listeners`.

      backlog: The listen backlog, or None to have a good default picked.
          Passed to :func:`open_tcp_listeners`.

      handler_nursery: The nursery to start handlers in, or None to use an
          internal nursery. Passed to :func:`serve_listeners`.

      task_status: This function can be used with ``nursery.start``.

    Returns:
      This function only returns when cancelled.

    '''
    pass
# WARNING: Decompyle incomplete
