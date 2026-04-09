# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _socket.pyc (Python 3.11)

from __future__ import annotations
import os
import select
import socket as _stdlib_socket
import sys
from operator import index
from socket import AddressFamily, SocketKind
from typing import TYPE_CHECKING, Any, Concatenate, SupportsIndex, TypeAlias, TypeVar, overload
import idna as _idna
import trio
from trio._util import wraps as _wraps
from  import _core
if TYPE_CHECKING:
    from collections.abc import Awaitable, Callable, Iterable
    from types import TracebackType
    from typing_extensions import Buffer, ParamSpec, Self
    from _abc import HostnameResolver, SocketFactory
    P = ParamSpec('P')
T = TypeVar('T')
AddressFormat: 'TypeAlias' = Any

class _try_sync:
    
    def __init__(self = None, blocking_exc_override = None):
        self._blocking_exc_override = blocking_exc_override

    
    def _is_blocking_io_error(self = None, exc = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'bool')):
        pass
    # WARNING: Decompyle incomplete


_resolver: '_core.RunVar[HostnameResolver | None]' = _core.RunVar('hostname_resolver')
_socket_factory: '_core.RunVar[SocketFactory | None]' = _core.RunVar('socket_factory')

def set_custom_hostname_resolver(hostname_resolver = None):
    """Set a custom hostname resolver.

    By default, Trio's :func:`getaddrinfo` and :func:`getnameinfo` functions
    use the standard system resolver functions. This function allows you to
    customize that behavior. The main intended use case is for testing, but it
    might also be useful for using third-party resolvers like `c-ares
    <https://c-ares.haxx.se/>`__ (though be warned that these rarely make
    perfect drop-in replacements for the system resolver). See
    :class:`trio.abc.HostnameResolver` for more details.

    Setting a custom hostname resolver affects all future calls to
    :func:`getaddrinfo` and :func:`getnameinfo` within the enclosing call to
    :func:`trio.run`. All other hostname resolution in Trio is implemented in
    terms of these functions.

    Generally you should call this function just once, right at the beginning
    of your program.

    Args:
      hostname_resolver (trio.abc.HostnameResolver or None): The new custom
          hostname resolver, or None to restore the default behavior.

    Returns:
      The previous hostname resolver (which may be None).

    """
    old = _resolver.get(None)
    _resolver.set(hostname_resolver)
    return old


def set_custom_socket_factory(socket_factory = None):
    """Set a custom socket object factory.

    This function allows you to replace Trio's normal socket class with a
    custom class. This is very useful for testing, and probably a bad idea in
    any other circumstance. See :class:`trio.abc.HostnameResolver` for more
    details.

    Setting a custom socket factory affects all future calls to :func:`socket`
    within the enclosing call to :func:`trio.run`.

    Generally you should call this function just once, right at the beginning
    of your program.

    Args:
      socket_factory (trio.abc.SocketFactory or None): The new custom
          socket factory, or None to restore the default behavior.

    Returns:
      The previous socket factory (which may be None).

    """
    old = _socket_factory.get(None)
    _socket_factory.set(socket_factory)
    return old

_NUMERIC_ONLY = _stdlib_socket.AI_NUMERICHOST
_NUMERIC_ONLY |= getattr(_stdlib_socket, 'AI_NUMERICSERV', 0)

async def getaddrinfo(host, port = None, family = None, type = None, proto = (0, 0, 0, 0), flags = ('host', 'bytes | str | None', 'port', 'bytes | str | int | None', 'family', 'int', 'type', 'int', 'proto', 'int', 'flags', 'int', 'return', 'list[tuple[AddressFamily, SocketKind, int, str, tuple[str, int] | tuple[str, int, int, int] | tuple[int, bytes]]]')):
    """Look up a numeric address given a name.

    Arguments and return values are identical to :func:`socket.getaddrinfo`,
    except that this version is async.

    Also, :func:`trio.socket.getaddrinfo` correctly uses IDNA 2008 to process
    non-ASCII domain names. (:func:`socket.getaddrinfo` uses IDNA 2003, which
    can give the wrong result in some cases and cause you to connect to a
    different host than the one you intended; see `bpo-17305
    <https://bugs.python.org/issue17305>`__.)

    This function's behavior can be customized using
    :func:`set_custom_hostname_resolver`.

    """
    pass
# WARNING: Decompyle incomplete


async def getnameinfo(sockaddr = None, flags = None):
    """Look up a name given a numeric address.

    Arguments and return values are identical to :func:`socket.getnameinfo`,
    except that this version is async.

    This function's behavior can be customized using
    :func:`set_custom_hostname_resolver`.

    """
    pass
# WARNING: Decompyle incomplete


async def getprotobyname(name = None):
    '''Look up a protocol number by name. (Rarely used.)

    Like :func:`socket.getprotobyname`, but async.

    '''
    pass
# WARNING: Decompyle incomplete


def from_stdlib_socket(sock = None):
    '''Convert a standard library :class:`socket.socket` object into a Trio
    socket object.

    '''
    return _SocketType(sock)

fromfd = (lambda fd = None, family = None, type = _wraps(_stdlib_socket.fromfd, assigned = (), updated = ()), proto = (_stdlib_socket.AF_INET, _stdlib_socket.SOCK_STREAM, 0): (family, type_, proto) = _sniff_sockopts_for_fileno(family, type, proto, index(fd))from_stdlib_socket(_stdlib_socket.fromfd(fd, family, type_, proto)))()
if (sys.platform == 'win32' or TYPE_CHECKING) and hasattr(_stdlib_socket, 'fromshare'):
    fromshare = (lambda info = None: from_stdlib_socket(_stdlib_socket.fromshare(info)))()
if sys.platform == 'win32':
    FamilyT: 'TypeAlias' = int
    TypeT: 'TypeAlias' = int
    FamilyDefault = _stdlib_socket.AF_INET
else:
    FamilyDefault: 'None' = None
    FamilyT: 'TypeAlias' = int | AddressFamily | None
    TypeT: 'TypeAlias' = _stdlib_socket.socket | int
socketpair = (lambda family = None, type = None, proto = _wraps(_stdlib_socket.socketpair, assigned = (), updated = ()): (left, right) = _stdlib_socket.socketpair(family, type, proto)(from_stdlib_socket(left), from_stdlib_socket(right)))()
socket = (lambda family = None, type = None, proto = _wraps(_stdlib_socket.socket, assigned = (), updated = ()), fileno = (_stdlib_socket.AF_INET, _stdlib_socket.SOCK_STREAM, 0, None): pass# WARNING: Decompyle incomplete
)()

def _sniff_sockopts_for_fileno(family = None, type_ = None, proto = None, fileno = ('family', 'AddressFamily | int', 'type_', 'SocketKind | int', 'proto', 'int', 'fileno', 'int | None', 'return', 'tuple[AddressFamily | int, SocketKind | int, int]')):
    '''Correct SOCKOPTS for given fileno, falling back to provided values.'''
    if sys.platform != 'linux':
        return (family, type_, proto)
    SO_DOMAIN = SO_DOMAIN
    SO_PROTOCOL = SO_PROTOCOL
    SO_TYPE = SO_TYPE
    SOL_SOCKET = SOL_SOCKET
    import socket
    sockobj = _stdlib_socket.socket(family, type_, proto, fileno = fileno)
    
    try:
        family = sockobj.getsockopt(SOL_SOCKET, SO_DOMAIN)
        proto = sockobj.getsockopt(SOL_SOCKET, SO_PROTOCOL)
        type_ = sockobj.getsockopt(SOL_SOCKET, SO_TYPE)
        sockobj.detach()
    except:
        sockobj.detach()

    return (family, type_, proto)

_SOCK_TYPE_MASK = ~(getattr(_stdlib_socket, 'SOCK_NONBLOCK', 0) | getattr(_stdlib_socket, 'SOCK_CLOEXEC', 0))

def _make_simple_sock_method_wrapper(fn = None, wait_fn = None, maybe_avail = None):
    pass
# WARNING: Decompyle incomplete


async def _resolve_address_nocp(type_ = None, family = None, proto = None, *, ipv6_v6only, address, local):
    pass
# WARNING: Decompyle incomplete


class SocketType:
    pass
# WARNING: Decompyle incomplete

for name, obj in SocketType.__dict__.items():
    if name.startswith('__') or obj.__doc__:
        continue
    for stdlib_type in (_stdlib_socket.socket, _stdlib_socket.SocketType):
        stdlib_obj = getattr(stdlib_type, name, None)
        if stdlib_obj and stdlib_obj.__doc__:
            pass
        
        obj.__doc__ = stdlib_obj.__doc__
        
        class _SocketType(SocketType):
            
            def __init__(self = None, sock = None):
                if type(sock) is not _stdlib_socket.socket:
                    raise TypeError(f'''expected object of type \'socket.socket\', not \'{type(sock).__name__}\'''')
                self._sock = sock
                self._sock.setblocking(False)
                self._did_shutdown_SHUT_WR = False

            
            def detach(self = None):
                return self._sock.detach()

            
            def fileno(self = None):
                return self._sock.fileno()

            
            def getpeername(self = None):
                return self._sock.getpeername()

            
            def getsockname(self = None):
                return self._sock.getsockname()

            getsockopt = (lambda self = None, level = None, optname = overload: pass)()
            getsockopt = (lambda self = None, level = None, optname = overload, buflen = ('level', 'int', 'optname', 'int', 'buflen', 'int', 'return', 'bytes'): pass)()
            
            def getsockopt(self = None, level = None, optname = None, buflen = (None,)):
                pass
            # WARNING: Decompyle incomplete

            setsockopt = (lambda self = None, level = None, optname = overload, value = ('level', 'int', 'optname', 'int', 'value', 'int | Buffer', 'return', 'None'): pass)()
            setsockopt = (lambda self, level = None, optname = None, value = overload, optlen = ('level', 'int', 'optname', 'int', 'value', 'None', 'optlen', 'int', 'return', 'None'): pass)()
            
            def setsockopt(self = None, level = None, optname = None, value = (None,), optlen = ('level', 'int', 'optname', 'int', 'value', 'int | Buffer | None', 'optlen', 'int | None', 'return', 'None')):
                pass
            # WARNING: Decompyle incomplete

            
            def listen(self = None, backlog = None):
                return self._sock.listen(backlog)

            
            def get_inheritable(self = None):
                return self._sock.get_inheritable()

            
            def set_inheritable(self = None, inheritable = None):
                return self._sock.set_inheritable(inheritable)

            if (sys.platform == 'win32' or TYPE_CHECKING) and hasattr(_stdlib_socket.socket, 'share'):
                
                def share(self = None, process_id = None):
                    return self._sock.share(process_id)

            
            def __enter__(self = None):
                return self

            
            def __exit__(self = None, exc_type = None, exc_value = None, traceback = ('exc_type', 'type[BaseException] | None', 'exc_value', 'BaseException | None', 'traceback', 'TracebackType | None', 'return', 'None')):
                return self._sock.__exit__(exc_type, exc_value, traceback)

            family = (lambda self = None: self._sock.family)()
            type = (lambda self = None: self._sock.type)()
            proto = (lambda self = None: self._sock.proto)()
            did_shutdown_SHUT_WR = (lambda self = None: self._did_shutdown_SHUT_WR)()
            
            def __repr__(self = None):
                return repr(self._sock).replace('socket.socket', 'trio.socket.socket')

            
            def dup(self = None):
                '''Same as :meth:`socket.socket.dup`.'''
                return _SocketType(self._sock.dup())

            
            def close(self = None):
                if self._sock.fileno() != -1:
                    trio.lowlevel.notify_closing(self._sock)
                    self._sock.close()
                    return None

            
            async def bind(self = None, address = None):
                pass
            # WARNING: Decompyle incomplete

            
            def shutdown(self = None, flag = None):
                self._sock.shutdown(flag)
                if flag in (_stdlib_socket.SHUT_WR, _stdlib_socket.SHUT_RDWR):
                    self._did_shutdown_SHUT_WR = True
                    return None

            
            def is_readable(self = None):
                if sys.platform == 'win32':
                    (rready, _, _) = select.select([
                        self._sock], [], [], 0)
                    return bool(rready)
                p = None.poll()
                p.register(self._sock, select.POLLIN)
                return bool(p.poll(0))

            
            async def wait_writable(self = None):
                pass
            # WARNING: Decompyle incomplete

            
            async def _resolve_address_nocp(self = None, address = None, *, local):
                pass
            # WARNING: Decompyle incomplete

            
            async def _nonblocking_helper(self = None, wait_fn = None, fn = None, *args, **kwargs):
                pass
            # WARNING: Decompyle incomplete

            _accept = _make_simple_sock_method_wrapper(_stdlib_socket.socket.accept, _core.wait_readable)
            
            async def accept(self = None):
                '''Like :meth:`socket.socket.accept`, but async.'''
                pass
            # WARNING: Decompyle incomplete

            
            async def connect(self = None, address = None):
                pass
            # WARNING: Decompyle incomplete

            if TYPE_CHECKING:
                
                def recv(self = None, buflen = None, flags = None):
                    pass

            recv = _make_simple_sock_method_wrapper(_stdlib_socket.socket.recv, _core.wait_readable)
            if TYPE_CHECKING:
                
                def recv_into(self = None, buffer = None, nbytes = None, flags = (0, 0)):
                    pass

            recv_into = _make_simple_sock_method_wrapper(_stdlib_socket.socket.recv_into, _core.wait_readable)
            if TYPE_CHECKING:
                
                def recvfrom(self = None, bufsize = None, flags = None):
                    pass

            recvfrom = _make_simple_sock_method_wrapper(_stdlib_socket.socket.recvfrom, _core.wait_readable)
            if TYPE_CHECKING:
                
                def recvfrom_into(self = None, buffer = None, nbytes = None, flags = (0, 0)):
                    pass

            recvfrom_into = _make_simple_sock_method_wrapper(_stdlib_socket.socket.recvfrom_into, _core.wait_readable)
            if (sys.platform != 'win32' or TYPE_CHECKING) and hasattr(_stdlib_socket.socket, 'recvmsg'):
                if TYPE_CHECKING:
                    
                    def recvmsg(self = None, bufsize = None, ancbufsize = None, flags = (0, 0)):
                        pass

                recvmsg = _make_simple_sock_method_wrapper(_stdlib_socket.socket.recvmsg, _core.wait_readable, maybe_avail = True)
            if (sys.platform != 'win32' or TYPE_CHECKING) and hasattr(_stdlib_socket.socket, 'recvmsg_into'):
                if TYPE_CHECKING:
                    
                    def recvmsg_into(self = None, buffers = None, ancbufsize = None, flags = (0, 0)):
                        pass

                recvmsg_into = _make_simple_sock_method_wrapper(_stdlib_socket.socket.recvmsg_into, _core.wait_readable, maybe_avail = True)
            if TYPE_CHECKING:
                
                def send(self = None, bytes = None, flags = None):
                    pass

            send = _make_simple_sock_method_wrapper(_stdlib_socket.socket.send, _core.wait_writable)
            sendto = (lambda self = None, data = None, address = overload: pass# WARNING: Decompyle incomplete
)()
            sendto = (lambda self = None, data = None, flags = overload, address = ('data', 'Buffer', 'flags', 'int', 'address', 'tuple[object, ...] | str | Buffer', 'return', 'int'): pass# WARNING: Decompyle incomplete
)()
            sendto = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
            if sys.platform != 'win32' or TYPE_CHECKING or hasattr(_stdlib_socket.socket, 'sendmsg'):
                sendmsg = (lambda self = None, buffers = None, ancdata = _wraps(_stdlib_socket.socket.sendmsg, assigned = (), updated = ()), flags = ((), 0, None), address = ('buffers', 'Iterable[Buffer]', 'ancdata', 'Iterable[tuple[int, int, Buffer]]', 'flags', 'int', 'address', 'AddressFormat | None', 'return', 'int'): pass# WARNING: Decompyle incomplete
)()
                return None
            return None

        return None
