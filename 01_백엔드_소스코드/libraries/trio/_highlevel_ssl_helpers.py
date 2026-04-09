# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _highlevel_ssl_helpers.pyc (Python 3.11)

from __future__ import annotations
import ssl
from typing import TYPE_CHECKING, NoReturn, TypeVar
import trio
from _highlevel_open_tcp_stream import DEFAULT_DELAY
T = TypeVar('T')
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable
    from _highlevel_socket import SocketStream

async def open_ssl_over_tcp_stream(host = None, port = None, *, https_compatible, ssl_context, happy_eyeballs_delay):
    """Make a TLS-encrypted Connection to the given host and port over TCP.

    This is a convenience wrapper that calls :func:`open_tcp_stream` and
    wraps the result in an :class:`~trio.SSLStream`.

    This function does not perform the TLS handshake; you can do it
    manually by calling :meth:`~trio.SSLStream.do_handshake`, or else
    it will be performed automatically the first time you send or receive
    data.

    Args:
      host (bytes or str): The host to connect to. We require the server
          to have a TLS certificate valid for this hostname.
      port (int): The port to connect to.
      https_compatible (bool): Set this to True if you're connecting to a web
          server. See :class:`~trio.SSLStream` for details. Default:
          False.
      ssl_context (:class:`~ssl.SSLContext` or None): The SSL context to
          use. If None (the default), :func:`ssl.create_default_context`
          will be called to create a context.
      happy_eyeballs_delay (float): See :func:`open_tcp_stream`.

    Returns:
      trio.SSLStream: the encrypted connection to the server.

    """
    pass
# WARNING: Decompyle incomplete


async def open_ssl_over_tcp_listeners(port = None, ssl_context = None, *, host, https_compatible, backlog):
    '''Start listening for SSL/TLS-encrypted TCP connections to the given port.

    Args:
      port (int): The port to listen on. See :func:`open_tcp_listeners`.
      ssl_context (~ssl.SSLContext): The SSL context to use for all incoming
          connections.
      host (str, bytes, or None): The address to bind to; use ``None`` to bind
          to the wildcard address. See :func:`open_tcp_listeners`.
      https_compatible (bool): See :class:`~trio.SSLStream` for details.
      backlog (int or None): See :func:`open_tcp_listeners` for details.

    '''
    pass
# WARNING: Decompyle incomplete


async def serve_ssl_over_tcp(handler = None, port = None, ssl_context = None, *, host, https_compatible, backlog, handler_nursery, task_status):
    '''Listen for incoming TCP connections, and for each one start a task
    running ``handler(stream)``.

    This is a thin convenience wrapper around
    :func:`open_ssl_over_tcp_listeners` and :func:`serve_listeners` – see them
    for full details.

    .. warning::

       If ``handler`` raises an exception, then this function doesn\'t do
       anything special to catch it – so by default the exception will
       propagate out and crash your server. If you don\'t want this, then catch
       exceptions inside your ``handler``, or use a ``handler_nursery`` object
       that responds to exceptions in some other way.

    When used with ``nursery.start`` you get back the newly opened listeners.
    See the documentation for :func:`serve_tcp` for an example where this is
    useful.

    Args:
      handler: The handler to start for each incoming connection. Passed to
          :func:`serve_listeners`.

      port (int): The port to listen on. Use 0 to let the kernel pick
          an open port. Ultimately passed to :func:`open_tcp_listeners`.

      ssl_context (~ssl.SSLContext): The SSL context to use for all incoming
          connections. Passed to :func:`open_ssl_over_tcp_listeners`.

      host (str, bytes, or None): The address to bind to; use ``None`` to bind
          to the wildcard address. Ultimately passed to
          :func:`open_tcp_listeners`.

      https_compatible (bool): Set this to True if you want to use
          "HTTPS-style" TLS. See :class:`~trio.SSLStream` for details.

      backlog (int or None): See :class:`~trio.SSLStream` for details.

      handler_nursery: The nursery to start handlers in, or None to use an
          internal nursery. Passed to :func:`serve_listeners`.

      task_status: This function can be used with ``nursery.start``.

    Returns:
      This function only returns when cancelled.

    '''
    pass
# WARNING: Decompyle incomplete
