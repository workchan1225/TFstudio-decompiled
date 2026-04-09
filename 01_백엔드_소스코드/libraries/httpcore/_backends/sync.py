# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: sync.pyc (Python 3.11)

from __future__ import annotations
import functools
import socket
import ssl
import sys
import typing
from _exceptions import ConnectError, ConnectTimeout, ExceptionMapping, ReadError, ReadTimeout, WriteError, WriteTimeout, map_exceptions
from _utils import is_socket_readable
from base import SOCKET_OPTION, NetworkBackend, NetworkStream

class TLSinTLSStream(NetworkStream):
    '''
    Because the standard `SSLContext.wrap_socket` method does
    not work for `SSLSocket` objects, we need this class
    to implement TLS stream using an underlying `SSLObject`
    instance in order to support TLS on top of TLS.
    '''
    TLS_RECORD_SIZE = 16384
    
    def __init__(self = None, sock = None, ssl_context = None, server_hostname = (None, None), timeout = ('sock', 'socket.socket', 'ssl_context', 'ssl.SSLContext', 'server_hostname', 'str | None', 'timeout', 'float | None')):
        self._sock = sock
        self._incoming = ssl.MemoryBIO()
        self._outgoing = ssl.MemoryBIO()
        self.ssl_obj = ssl_context.wrap_bio(incoming = self._incoming, outgoing = self._outgoing, server_hostname = server_hostname)
        self._sock.settimeout(timeout)
        self._perform_io(self.ssl_obj.do_handshake)

    
    def _perform_io(self = None, func = None):
        ret = None
        errno = None
        
        try:
            ret = func()
        except (ssl.SSLWantReadError, ssl.SSLWantWriteError):
            e = None
            errno = e.errno
            e = None
            del e
        except:
            e = None
            del e

        self._sock.sendall(self._outgoing.read())
        if errno == ssl.SSL_ERROR_WANT_READ:
            buf = self._sock.recv(self.TLS_RECORD_SIZE)
            if buf:
                self._incoming.write(buf)
            else:
                self._incoming.write_eof()
    # WARNING: Decompyle incomplete

    
    def read(self = None, max_bytes = None, timeout = None):
        exc_map = {
            OSError: ReadError,
            socket.timeout: ReadTimeout }
        map_exceptions(exc_map)
        self._sock.settimeout(timeout)
        None(None, None)
        return 
        with None:
            if not None, typing.cast(bytes, self._perform_io(functools.partial(self.ssl_obj.read, max_bytes))):
                pass

    
    def write(self = None, buffer = None, timeout = None):
        exc_map = {
            OSError: WriteError,
            socket.timeout: WriteTimeout }
        map_exceptions(exc_map)
        self._sock.settimeout(timeout)
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._sock.close()

    
    def start_tls(self = None, ssl_context = None, server_hostname = None, timeout = (None, None)):
        raise NotImplementedError()

    
    def get_extra_info(self = None, info = None):
        if info == 'ssl_object':
            return self.ssl_obj
        if None == 'client_addr':
            return self._sock.getsockname()
        if None == 'server_addr':
            return self._sock.getpeername()
        if None == 'socket':
            return self._sock
        if None == 'is_readable':
            return is_socket_readable(self._sock)



class SyncStream(NetworkStream):
    
    def __init__(self = None, sock = None):
        self._sock = sock

    
    def read(self = None, max_bytes = None, timeout = None):
        exc_map = {
            OSError: ReadError,
            socket.timeout: ReadTimeout }
        map_exceptions(exc_map)
        self._sock.settimeout(timeout)
        None(None, None)
        return 
        with None:
            if not None, self._sock.recv(max_bytes):
                pass

    
    def write(self = None, buffer = None, timeout = None):
        if not buffer:
            return None
        exc_map = {
            OSError: WriteError,
            None.timeout: WriteTimeout }
        map_exceptions(exc_map)
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._sock.close()

    
    def start_tls(self = None, ssl_context = None, server_hostname = None, timeout = (None, None)):
        exc_map = {
            OSError: ConnectError,
            socket.timeout: ConnectTimeout }
        map_exceptions(exc_map)
        if isinstance(self._sock, ssl.SSLSocket):
            None(None, None)
            return 
        None._sock.settimeout(timeout)

    
    def get_extra_info(self = None, info = None):
        if info == 'ssl_object' and isinstance(self._sock, ssl.SSLSocket):
            return self._sock._sslobj
        if None == 'client_addr':
            return self._sock.getsockname()
        if None == 'server_addr':
            return self._sock.getpeername()
        if None == 'socket':
            return self._sock
        if None == 'is_readable':
            return is_socket_readable(self._sock)



class SyncBackend(NetworkBackend):
    
    def connect_tcp(self, host = None, port = None, timeout = None, local_address = (None, None, None), socket_options = ('host', 'str', 'port', 'int', 'timeout', 'float | None', 'local_address', 'str | None', 'socket_options', 'typing.Iterable[SOCKET_OPTION] | None', 'return', 'NetworkStream')):
        pass
    # WARNING: Decompyle incomplete

    
    def connect_unix_socket(self = None, path = None, timeout = None, socket_options = (None, None)):
        if sys.platform == 'win32':
            raise RuntimeError('Attempted to connect to a UNIX socket on a Windows system.')
    # WARNING: Decompyle incomplete
