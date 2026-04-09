# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _sockets.pyc (Python 3.11)

from __future__ import annotations
import errno
import socket
import sys
from abc import abstractmethod
from collections.abc import Callable, Collection, Mapping
from contextlib import AsyncExitStack
from io import IOBase
from ipaddress import IPv4Address, IPv6Address
from socket import AddressFamily
from typing import Any, TypeVar, Union
from _core._eventloop import get_async_backend
from _core._typedattr import TypedAttributeProvider, TypedAttributeSet, typed_attribute
from _streams import ByteStream, Listener, UnreliableObjectStream
from _tasks import TaskGroup
if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias
IPAddressType: 'TypeAlias' = Union[(str, IPv4Address, IPv6Address)]
IPSockAddrType: 'TypeAlias' = tuple[(str, int)]
SockAddrType: 'TypeAlias' = Union[(IPSockAddrType, str)]
UDPPacketType: 'TypeAlias' = tuple[(bytes, IPSockAddrType)]
UNIXDatagramPacketType: 'TypeAlias' = tuple[(bytes, str)]
T_Retval = TypeVar('T_Retval')

def _validate_socket(sock_or_fd = None, sock_type = None, addr_family = None, *, require_connected, require_bound):
    if isinstance(sock_or_fd, int):
        
        try:
            sock = socket.socket(fileno = sock_or_fd)
        except OSError:
            exc = None
            if exc.errno == errno.ENOTSOCK:
                raise ValueError('the file descriptor does not refer to a socket'), exc
            if require_connected:
                raise ValueError('the socket must be connected'), exc
            if require_bound:
                raise ValueError('the socket must be bound to a local address'), exc
            raise 
            exc = None
            del exc
            if isinstance(sock_or_fd, socket.socket):
                sock = sock_or_fd
            else:
                raise TypeError(f'''expected an int or socket, got {type(sock_or_fd).__qualname__} instead''')

        
        try:
            if require_connected:
                
                try:
                    sock.getpeername()
                    
                    try:
                        pass
                    except OSError:
                        exc = None
                        raise ValueError('the socket must be connected'), exc
                        exc = None
                        del exc

                    
                    try:
                        if require_bound:
                            
                            try:
                                if sock.family in (socket.AF_INET, socket.AF_INET6):
                                    bound_addr = sock.getsockname()[1]
                                else:
                                    bound_addr = sock.getsockname()
                                    
                                    try:
                                        pass
                                    except OSError:
                                        bound_addr = None
                                        
                                        try:
                                            pass
                                        try:
                                            if not bound_addr:
                                                raise ValueError('the socket must be bound to a local address')
                                            if addr_family != socket.AF_UNSPEC and sock.family != addr_family:
                                                raise ValueError(f'''address family mismatch: expected {addr_family.name}, got {sock.family.name}''')
                                            if sock.type != sock_type:
                                                raise ValueError(f'''socket type mismatch: expected {sock_type.name}, got {sock.type.name}''')
                                        except BaseException:
                                            if isinstance(sock_or_fd, int):
                                                sock.detach()
                                            raise 

                                        sock.setblocking(False)
                                        return sock







class SocketAttribute(TypedAttributeSet):
    '''
    .. attribute:: family
        :type: socket.AddressFamily

        the address family of the underlying socket

    .. attribute:: local_address
        :type: tuple[str, int] | str

        the local address the underlying socket is connected to

    .. attribute:: local_port
        :type: int

        for IP based sockets, the local port the underlying socket is bound to

    .. attribute:: raw_socket
        :type: socket.socket

        the underlying stdlib socket object

    .. attribute:: remote_address
        :type: tuple[str, int] | str

        the remote address the underlying socket is connected to

    .. attribute:: remote_port
        :type: int

        for IP based sockets, the remote port the underlying socket is connected to
    '''
    family: 'AddressFamily' = typed_attribute()
    local_address: 'SockAddrType' = typed_attribute()
    local_port: 'int' = typed_attribute()
    raw_socket: 'socket.socket' = typed_attribute()
    remote_address: 'SockAddrType' = typed_attribute()
    remote_port: 'int' = typed_attribute()


class _SocketProvider(TypedAttributeProvider):
    extra_attributes = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _raw_socket = (lambda self = None: pass)()()


class SocketStream(_SocketProvider, ByteStream):
    '''
    Transports bytes over a socket.

    Supports all relevant extra attributes from :class:`~SocketAttribute`.
    '''
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()


class UNIXSocketStream(SocketStream):
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()
    send_fds = (lambda self = None, message = None, fds = abstractmethod: pass# WARNING: Decompyle incomplete
)()
    receive_fds = (lambda self = None, msglen = None, maxfds = abstractmethod: pass# WARNING: Decompyle incomplete
)()


def SocketListener():
    '''SocketListener'''
    __doc__ = '\n    Listens to incoming socket connections.\n\n    Supports all relevant extra attributes from :class:`~SocketAttribute`.\n    '
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()
    accept = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    async def serve(self = None, handler = None, task_group = None):
        pass
    # WARNING: Decompyle incomplete


SocketListener = <NODE:27>(SocketListener, 'SocketListener', Listener[SocketStream], _SocketProvider)

def UDPSocket():
    '''UDPSocket'''
    __doc__ = '\n    Represents an unconnected UDP socket.\n\n    Supports all relevant extra attributes from :class:`~SocketAttribute`.\n    '
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()
    
    async def sendto(self = None, data = None, host = None, port = ('data', 'bytes', 'host', 'str', 'port', 'int', 'return', 'None')):
        '''
        Alias for :meth:`~.UnreliableObjectSendStream.send` ((data, (host, port))).

        '''
        pass
    # WARNING: Decompyle incomplete


UDPSocket = <NODE:27>(UDPSocket, 'UDPSocket', UnreliableObjectStream[UDPPacketType], _SocketProvider)

def ConnectedUDPSocket():
    '''ConnectedUDPSocket'''
    __doc__ = '\n    Represents an connected UDP socket.\n\n    Supports all relevant extra attributes from :class:`~SocketAttribute`.\n    '
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()

ConnectedUDPSocket = <NODE:27>(ConnectedUDPSocket, 'ConnectedUDPSocket', UnreliableObjectStream[bytes], _SocketProvider)

def UNIXDatagramSocket():
    '''UNIXDatagramSocket'''
    __doc__ = '\n    Represents an unconnected Unix datagram socket.\n\n    Supports all relevant extra attributes from :class:`~SocketAttribute`.\n    '
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()
    
    async def sendto(self = None, data = None, path = None):
        '''Alias for :meth:`~.UnreliableObjectSendStream.send` ((data, path)).'''
        pass
    # WARNING: Decompyle incomplete


UNIXDatagramSocket = <NODE:27>(UNIXDatagramSocket, 'UNIXDatagramSocket', UnreliableObjectStream[UNIXDatagramPacketType], _SocketProvider)

def ConnectedUNIXDatagramSocket():
    '''ConnectedUNIXDatagramSocket'''
    __doc__ = '\n    Represents a connected Unix datagram socket.\n\n    Supports all relevant extra attributes from :class:`~SocketAttribute`.\n    '
    from_socket = (lambda cls = None, sock_or_fd = None: pass# WARNING: Decompyle incomplete
)()

ConnectedUNIXDatagramSocket = <NODE:27>(ConnectedUNIXDatagramSocket, 'ConnectedUNIXDatagramSocket', UnreliableObjectStream[bytes], _SocketProvider)
