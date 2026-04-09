# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _sockets.pyc (Python 3.11)

from __future__ import annotations
import errno
import os
import socket
import ssl
import stat
import sys
from collections.abc import Awaitable
from dataclasses import dataclass
from ipaddress import IPv4Address, IPv6Address, ip_address
from os import PathLike, chmod
from socket import AddressFamily, SocketKind
from typing import TYPE_CHECKING, Any, Literal, cast, overload
from  import ConnectionFailed, to_thread
from abc import ByteStreamConnectable, ConnectedUDPSocket, ConnectedUNIXDatagramSocket, IPAddressType, IPSockAddrType, SocketListener, SocketStream, UDPSocket, UNIXDatagramSocket, UNIXSocketStream
from streams.stapled import MultiListener
from streams.tls import TLSConnectable, TLSStream
from _eventloop import get_async_backend
from _resources import aclose_forcefully
from _synchronization import Event
from _tasks import create_task_group, move_on_after
if TYPE_CHECKING:
    from _typeshed import FileDescriptorLike
else:
    FileDescriptorLike = object
if sys.version_info < (3, 11):
    from exceptiongroup import ExceptionGroup
if sys.version_info >= (3, 12):
    from typing import override
else:
    from typing_extensions import override
if sys.version_info < (3, 13):
    from typing_extensions import deprecated
else:
    from warnings import deprecated
IPPROTO_IPV6 = getattr(socket, 'IPPROTO_IPV6', 41)
AnyIPAddressFamily = Literal[(AddressFamily.AF_UNSPEC, AddressFamily.AF_INET, AddressFamily.AF_INET6)]
IPAddressFamily = Literal[(AddressFamily.AF_INET, AddressFamily.AF_INET6)]
connect_tcp = (lambda remote_host = None, remote_port = None, *, local_host, ssl_context: pass# WARNING: Decompyle incomplete
)()
connect_tcp = (lambda remote_host = None, remote_port = None, *, local_host, ssl_context: pass# WARNING: Decompyle incomplete
)()
connect_tcp = (lambda remote_host = None, remote_port = None, *, local_host, tls: pass# WARNING: Decompyle incomplete
)()
connect_tcp = (lambda remote_host = None, remote_port = None, *, local_host, tls: pass# WARNING: Decompyle incomplete
)()
connect_tcp = (lambda remote_host = None, remote_port = None, *, local_host, happy_eyeballs_delay: pass# WARNING: Decompyle incomplete
)()

async def connect_tcp(remote_host = None, remote_port = None, *, local_host, tls, ssl_context, tls_standard_compatible, tls_hostname, happy_eyeballs_delay):
    '''
    Connect to a host using the TCP protocol.

    This function implements the stateless version of the Happy Eyeballs algorithm (RFC
    6555). If ``remote_host`` is a host name that resolves to multiple IP addresses,
    each one is tried until one connection attempt succeeds. If the first attempt does
    not connected within 250 milliseconds, a second attempt is started using the next
    address in the list, and so on. On IPv6 enabled systems, an IPv6 address (if
    available) is tried first.

    When the connection has been established, a TLS handshake will be done if either
    ``ssl_context`` or ``tls_hostname`` is not ``None``, or if ``tls`` is ``True``.

    :param remote_host: the IP address or host name to connect to
    :param remote_port: port on the target host to connect to
    :param local_host: the interface address or name to bind the socket to before
        connecting
    :param tls: ``True`` to do a TLS handshake with the connected stream and return a
        :class:`~anyio.streams.tls.TLSStream` instead
    :param ssl_context: the SSL context object to use (if omitted, a default context is
        created)
    :param tls_standard_compatible: If ``True``, performs the TLS shutdown handshake
        before closing the stream and requires that the server does this as well.
        Otherwise, :exc:`~ssl.SSLEOFError` may be raised during reads from the stream.
        Some protocols, such as HTTP, require this option to be ``False``.
        See :meth:`~ssl.SSLContext.wrap_socket` for details.
    :param tls_hostname: host name to check the server certificate against (defaults to
        the value of ``remote_host``)
    :param happy_eyeballs_delay: delay (in seconds) before starting the next connection
        attempt
    :return: a socket stream object if no TLS handshake was done, otherwise a TLS stream
    :raises ConnectionFailed: if the connection fails

    '''
    pass
# WARNING: Decompyle incomplete


async def connect_unix(path = None):
    '''
    Connect to the given UNIX socket.

    Not available on Windows.

    :param path: path to the socket
    :return: a socket stream object
    :raises ConnectionFailed: if the connection fails

    '''
    pass
# WARNING: Decompyle incomplete


async def create_tcp_listener(*, local_host, local_port, family, backlog, reuse_port):
    """
    Create a TCP socket listener.

    :param local_port: port number to listen on
    :param local_host: IP address of the interface to listen on. If omitted, listen on
        all IPv4 and IPv6 interfaces. To listen on all interfaces on a specific address
        family, use ``0.0.0.0`` for IPv4 or ``::`` for IPv6.
    :param family: address family (used if ``local_host`` was omitted)
    :param backlog: maximum number of queued incoming connections (up to a maximum of
        2**16, or 65536)
    :param reuse_port: ``True`` to allow multiple sockets to bind to the same
        address/port (not supported on Windows)
    :return: a multi-listener object containing one or more socket listeners
    :raises OSError: if there's an error creating a socket, or binding to one or more
        interfaces failed

    """
    pass
# WARNING: Decompyle incomplete


async def create_unix_listener(path = None, *, mode, backlog):
    '''
    Create a UNIX socket listener.

    Not available on Windows.

    :param path: path of the socket
    :param mode: permissions to set on the socket
    :param backlog: maximum number of queued incoming connections (up to a maximum of
        2**16, or 65536)
    :return: a listener object

    .. versionchanged:: 3.0
        If a socket already exists on the file system in the given path, it will be
        removed first.

    '''
    pass
# WARNING: Decompyle incomplete


async def create_udp_socket(family = None, *, local_host, local_port, reuse_port):
    '''
    Create a UDP socket.

    If ``port`` has been given, the socket will be bound to this port on the local
    machine, making this socket suitable for providing UDP based services.

    :param family: address family (``AF_INET`` or ``AF_INET6``) – automatically
        determined from ``local_host`` if omitted
    :param local_host: IP address or host name of the local interface to bind to
    :param local_port: local port to bind to
    :param reuse_port: ``True`` to allow multiple sockets to bind to the same
        address/port (not supported on Windows)
    :return: a UDP socket

    '''
    pass
# WARNING: Decompyle incomplete


async def create_connected_udp_socket(remote_host = None, remote_port = None, *, family, local_host, local_port, reuse_port):
    '''
    Create a connected UDP socket.

    Connected UDP sockets can only communicate with the specified remote host/port, an
    any packets sent from other sources are dropped.

    :param remote_host: remote host to set as the default target
    :param remote_port: port on the remote host to set as the default target
    :param family: address family (``AF_INET`` or ``AF_INET6``) – automatically
        determined from ``local_host`` or ``remote_host`` if omitted
    :param local_host: IP address or host name of the local interface to bind to
    :param local_port: local port to bind to
    :param reuse_port: ``True`` to allow multiple sockets to bind to the same
        address/port (not supported on Windows)
    :return: a connected UDP socket

    '''
    pass
# WARNING: Decompyle incomplete


async def create_unix_datagram_socket(*, local_path, local_mode):
    '''
    Create a UNIX datagram socket.

    Not available on Windows.

    If ``local_path`` has been given, the socket will be bound to this path, making this
    socket suitable for receiving datagrams from other processes. Other processes can
    send datagrams to this socket only if ``local_path`` is set.

    If a socket already exists on the file system in the ``local_path``, it will be
    removed first.

    :param local_path: the path on which to bind to
    :param local_mode: permissions to set on the local socket
    :return: a UNIX datagram socket

    '''
    pass
# WARNING: Decompyle incomplete


async def create_connected_unix_datagram_socket(remote_path = None, *, local_path, local_mode):
    '''
    Create a connected UNIX datagram socket.

    Connected datagram sockets can only communicate with the specified remote path.

    If ``local_path`` has been given, the socket will be bound to this path, making
    this socket suitable for receiving datagrams from other processes. Other processes
    can send datagrams to this socket only if ``local_path`` is set.

    If a socket already exists on the file system in the ``local_path``, it will be
    removed first.

    :param remote_path: the path to set as the default target
    :param local_path: the path on which to bind to
    :param local_mode: permissions to set on the local socket
    :return: a connected UNIX datagram socket

    '''
    pass
# WARNING: Decompyle incomplete


async def getaddrinfo(host = None, port = None, *, family, type, proto, flags):
    """
    Look up a numeric IP address given a host name.

    Internationalized domain names are translated according to the (non-transitional)
    IDNA 2008 standard.

    .. note:: 4-tuple IPv6 socket addresses are automatically converted to 2-tuples of
        (host, port), unlike what :func:`socket.getaddrinfo` does.

    :param host: host name
    :param port: port number
    :param family: socket family (`'AF_INET``, ...)
    :param type: socket type (``SOCK_STREAM``, ...)
    :param proto: protocol number
    :param flags: flags to pass to upstream ``getaddrinfo()``
    :return: list of tuples containing (family, type, proto, canonname, sockaddr)

    .. seealso:: :func:`socket.getaddrinfo`

    """
    pass
# WARNING: Decompyle incomplete


def getnameinfo(sockaddr = None, flags = None):
    '''
    Look up the host name of an IP address.

    :param sockaddr: socket address (e.g. (ipaddress, port) for IPv4)
    :param flags: flags to pass to upstream ``getnameinfo()``
    :return: a tuple of (host name, service name)

    .. seealso:: :func:`socket.getnameinfo`

    '''
    return get_async_backend().getnameinfo(sockaddr, flags)

wait_socket_readable = (lambda sock = None: get_async_backend().wait_readable(sock.fileno()))()
wait_socket_writable = (lambda sock = None: get_async_backend().wait_writable(sock.fileno()))()

def wait_readable(obj = None):
    """
    Wait until the given object has data to be read.

    On Unix systems, ``obj`` must either be an integer file descriptor, or else an
    object with a ``.fileno()`` method which returns an integer file descriptor. Any
    kind of file descriptor can be passed, though the exact semantics will depend on
    your kernel. For example, this probably won't do anything useful for on-disk files.

    On Windows systems, ``obj`` must either be an integer ``SOCKET`` handle, or else an
    object with a ``.fileno()`` method which returns an integer ``SOCKET`` handle. File
    descriptors aren't supported, and neither are handles that refer to anything besides
    a ``SOCKET``.

    On backends where this functionality is not natively provided (asyncio
    ``ProactorEventLoop`` on Windows), it is provided using a separate selector thread
    which is set to shut down when the interpreter shuts down.

    .. warning:: Don't use this on raw sockets that have been wrapped by any higher
        level constructs like socket streams!

    :param obj: an object with a ``.fileno()`` method or an integer handle
    :raises ~anyio.ClosedResourceError: if the object was closed while waiting for the
        object to become readable
    :raises ~anyio.BusyResourceError: if another task is already waiting for the object
        to become readable

    """
    return get_async_backend().wait_readable(obj)


def wait_writable(obj = None):
    """
    Wait until the given object can be written to.

    :param obj: an object with a ``.fileno()`` method or an integer handle
    :raises ~anyio.ClosedResourceError: if the object was closed while waiting for the
        object to become writable
    :raises ~anyio.BusyResourceError: if another task is already waiting for the object
        to become writable

    .. seealso:: See the documentation of :func:`wait_readable` for the definition of
       ``obj`` and notes on backend compatibility.

    .. warning:: Don't use this on raw sockets that have been wrapped by any higher
        level constructs like socket streams!

    """
    return get_async_backend().wait_writable(obj)


def notify_closing(obj = None):
    """
    Call this before closing a file descriptor (on Unix) or socket (on
    Windows). This will cause any `wait_readable` or `wait_writable`
    calls on the given object to immediately wake up and raise
    `~anyio.ClosedResourceError`.

    This doesn't actually close the object – you still have to do that
    yourself afterwards. Also, you want to be careful to make sure no
    new tasks start waiting on the object in between when you call this
    and when it's actually closed. So to close something properly, you
    usually want to do these steps in order:

    1. Explicitly mark the object as closed, so that any new attempts
       to use it will abort before they start.
    2. Call `notify_closing` to wake up any already-existing users.
    3. Actually close the object.

    It's also possible to do them in a different order if that's more
    convenient, *but only if* you make sure not to have any checkpoints in
    between the steps. This way they all happen in a single atomic
    step, so other tasks won't be able to tell what order they happened
    in anyway.

    :param obj: an object with a ``.fileno()`` method or an integer handle

    """
    get_async_backend().notify_closing(obj)


def convert_ipv6_sockaddr(sockaddr = None):
    '''
    Convert a 4-tuple IPv6 socket address to a 2-tuple (address, port) format.

    If the scope ID is nonzero, it is added to the address, separated with ``%``.
    Otherwise the flow id and scope id are simply cut off from the tuple.
    Any other kinds of socket addresses are returned as-is.

    :param sockaddr: the result of :meth:`~socket.socket.getsockname`
    :return: the converted socket address

    '''
    if isinstance(sockaddr, tuple) and len(sockaddr) == 4:
        (host, port, flowinfo, scope_id) = sockaddr
        if scope_id:
            host = host.split('%')[0]
            return (f'''{host}%{scope_id}''', port)
        return (None, port)


async def setup_unix_local_socket(path = None, mode = None, socktype = None):
    '''
    Create a UNIX local socket object, deleting the socket at the given path if it
    exists.

    Not available on Windows.

    :param path: path of the socket
    :param mode: permissions to set on the socket
    :param socktype: socket.SOCK_STREAM or socket.SOCK_DGRAM

    '''
    pass
# WARNING: Decompyle incomplete

TCPConnectable = <NODE:12>()
UNIXConnectable = <NODE:12>()

def as_connectable(remote = None, *, tls, ssl_context, tls_hostname, tls_standard_compatible):
    """
    Return a byte stream connectable from the given object.

    If a bytestream connectable is given, it is returned unchanged.
    If a tuple of (host, port) is given, a TCP connectable is returned.
    If a string or bytes path is given, a UNIX connectable is returned.

    If ``tls=True``, the connectable will be wrapped in a
    :class:`~.streams.tls.TLSConnectable`.

    :param remote: a connectable, a tuple of (host, port) or a path to a UNIX socket
    :param tls: if ``True``, wrap the plaintext connectable in a
        :class:`~.streams.tls.TLSConnectable`, using the provided TLS settings)
    :param ssl_context: if ``tls=True``, the SSLContext object to use  (if not provided,
        a secure default will be created)
    :param tls_hostname: if ``tls=True``, host name of the server to use for checking
        the server certificate (defaults to the host portion of the address for TCP
        connectables)
    :param tls_standard_compatible: if ``False`` and ``tls=True``, makes the TLS stream
        skip the closing handshake when closing the connection, so it won't raise an
        exception if the server does the same

    """
    if isinstance(remote, ByteStreamConnectable):
        return remote
# WARNING: Decompyle incomplete
