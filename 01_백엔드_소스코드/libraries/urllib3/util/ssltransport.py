# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ssltransport.pyc (Python 3.11)

from __future__ import annotations
import io
import socket
import ssl
import typing
from exceptions import ProxySchemeUnsupported
if typing.TYPE_CHECKING:
    from typing_extensions import Self
    from ssl_ import _TYPE_PEER_CERT_RET, _TYPE_PEER_CERT_RET_DICT
_WriteBuffer = typing.Union[(bytearray, memoryview)]
_ReturnValue = typing.TypeVar('_ReturnValue')
SSL_BLOCKSIZE = 16384

class SSLTransport:
    """
    The SSLTransport wraps an existing socket and establishes an SSL connection.

    Contrary to Python's implementation of SSLSocket, it allows you to chain
    multiple TLS connections together. It's particularly useful if you need to
    implement TLS within TLS.

    The class supports most of the socket API operations.
    """
    _validate_ssl_context_for_tls_in_tls = (lambda ssl_context = None: if not hasattr(ssl_context, 'wrap_bio'):
raise ProxySchemeUnsupported("TLS in TLS requires SSLContext.wrap_bio() which isn't available on non-native SSLContext"))()
    
    def __init__(self = None, socket = None, ssl_context = None, server_hostname = (None, True), suppress_ragged_eofs = ('socket', 'socket.socket', 'ssl_context', 'ssl.SSLContext', 'server_hostname', 'str | None', 'suppress_ragged_eofs', 'bool', 'return', 'None')):
        '''
        Create an SSLTransport around socket using the provided ssl_context.
        '''
        self.incoming = ssl.MemoryBIO()
        self.outgoing = ssl.MemoryBIO()
        self.suppress_ragged_eofs = suppress_ragged_eofs
        self.socket = socket
        self.sslobj = ssl_context.wrap_bio(self.incoming, self.outgoing, server_hostname = server_hostname)
        self._ssl_io_loop(self.sslobj.do_handshake)

    
    def __enter__(self = None):
        return self

    
    def __exit__(self = None, *_):
        self.close()

    
    def fileno(self = None):
        return self.socket.fileno()

    
    def read(self = None, len = None, buffer = None):
        return self._wrap_ssl_read(len, buffer)

    
    def recv(self = None, buflen = None, flags = None):
        if flags != 0:
            raise ValueError('non-zero flags not allowed in calls to recv')
        return self._wrap_ssl_read(buflen)

    
    def recv_into(self = None, buffer = None, nbytes = None, flags = (None, 0)):
        if flags != 0:
            raise ValueError('non-zero flags not allowed in calls to recv_into')
    # WARNING: Decompyle incomplete

    
    def sendall(self = None, data = None, flags = None):
        if flags != 0:
            raise ValueError('non-zero flags not allowed in calls to sendall')
        count = 0
        view = memoryview(data)
        byte_view = view.cast('B')
        amount = len(byte_view)
    # WARNING: Decompyle incomplete

    
    def send(self = None, data = None, flags = None):
        if flags != 0:
            raise ValueError('non-zero flags not allowed in calls to send')
        return self._ssl_io_loop(self.sslobj.write, data)

    
    def makefile(self = None, mode = None, buffering = None, *, encoding, errors, newline):
        """
        Python's httpclient uses makefile and buffered io when reading HTTP
        messages and we need to support it.

        This is unfortunately a copy and paste of socket.py makefile with small
        changes to point to the socket directly.
        """
        if not set(mode) <= {
            'b',
            'r',
            'w'}:
            raise ValueError(f'''invalid mode {mode!r} (only r, w, b allowed)''')
        writing = 'w' in mode
    # WARNING: Decompyle incomplete

    
    def unwrap(self = None):
        self._ssl_io_loop(self.sslobj.unwrap)

    
    def close(self = None):
        self.socket.close()

    getpeercert = (lambda self = None, binary_form = None: pass)()
    getpeercert = (lambda self = None, binary_form = None: pass)()
    
    def getpeercert(self = None, binary_form = None):
        return self.sslobj.getpeercert(binary_form)

    
    def version(self = None):
        return self.sslobj.version()

    
    def cipher(self = None):
        return self.sslobj.cipher()

    
    def selected_alpn_protocol(self = None):
        return self.sslobj.selected_alpn_protocol()

    
    def shared_ciphers(self = None):
        return self.sslobj.shared_ciphers()

    
    def compression(self = None):
        return self.sslobj.compression()

    
    def settimeout(self = None, value = None):
        self.socket.settimeout(value)

    
    def gettimeout(self = None):
        return self.socket.gettimeout()

    
    def _decref_socketios(self = None):
        self.socket._decref_socketios()

    
    def _wrap_ssl_read(self = None, len = None, buffer = None):
        
        try:
            return self._ssl_io_loop(self.sslobj.read, len, buffer)
        except ssl.SSLError:
            e = None
            if e.errno == ssl.SSL_ERROR_EOF and self.suppress_ragged_eofs:
                e = None
                del e
                return 0
            e = None
            del e


    _ssl_io_loop = (lambda self = None, func = None: pass)()
    _ssl_io_loop = (lambda self = None, func = None, arg1 = typing.overload: pass)()
    _ssl_io_loop = (lambda self = None, func = None, arg1 = typing.overload, arg2 = ('func', 'typing.Callable[[int, bytearray | None], bytes]', 'arg1', 'int', 'arg2', 'bytearray | None', 'return', 'bytes'): pass)()
    
    def _ssl_io_loop(self = None, func = None, arg1 = None, arg2 = (None, None)):
        '''Performs an I/O loop between incoming/outgoing and the socket.'''
        should_loop = True
        ret = None
    # WARNING: Decompyle incomplete
