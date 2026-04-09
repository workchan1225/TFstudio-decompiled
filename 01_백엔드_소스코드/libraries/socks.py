# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: socks.pyc (Python 3.11)

from base64 import b64encode

try:
    from collections.abc import Callable
except ImportError:
    from collections import Callable

from errno import EOPNOTSUPP, EINVAL, EAGAIN
import functools
from io import BytesIO
import logging
import os
from os import SEEK_CUR
import socket
import struct
import sys
__version__ = '1.7.1'
if os.name == 'nt' and sys.version_info < (3, 0):
    
    try:
        import win_inet_pton
    except ImportError:
        raise ImportError('To run PySocks on Windows you must install win_inet_pton')

    log = logging.getLogger(__name__)
    PROXY_TYPE_SOCKS4 = 1
    SOCKS4 = 1
    PROXY_TYPE_SOCKS5 = 2
    SOCKS5 = 2
    PROXY_TYPE_HTTP = 3
    HTTP = 3
    PROXY_TYPES = {
        'SOCKS4': SOCKS4,
        'SOCKS5': SOCKS5,
        'HTTP': HTTP }
    PRINTABLE_PROXY_TYPES = dict(zip(PROXY_TYPES.values(), PROXY_TYPES.keys()))
    _orgsocket = socket.socket
    _orig_socket = socket.socket
    
    def set_self_blocking(function):
        pass
    # WARNING: Decompyle incomplete

    
    class ProxyError(IOError):
        '''Socket_err contains original socket.error exception.'''
        
        def __init__(self, msg, socket_err = (None,)):
            self.msg = msg
            self.socket_err = socket_err
            if socket_err:
                return None

        
        def __str__(self):
            return self.msg


    
    class GeneralProxyError(ProxyError):
        pass

    
    class ProxyConnectionError(ProxyError):
        pass

    
    class SOCKS5AuthError(ProxyError):
        pass

    
    class SOCKS5Error(ProxyError):
        pass

    
    class SOCKS4Error(ProxyError):
        pass

    
    class HTTPError(ProxyError):
        pass

    SOCKS4_ERRORS = {
        91: 'Request rejected or failed',
        92: 'Request rejected because SOCKS server cannot connect to identd on the client',
        93: 'Request rejected because the client program and identd report different user-ids' }
    SOCKS5_ERRORS = {
        1: 'General SOCKS server failure',
        2: 'Connection not allowed by ruleset',
        3: 'Network unreachable',
        4: 'Host unreachable',
        5: 'Connection refused',
        6: 'TTL expired',
        7: 'Command not supported, or protocol error',
        8: 'Address type not supported' }
    DEFAULT_PORTS = {
        HTTP: 8080,
        SOCKS5: 1080,
        SOCKS4: 1080 }
    
    def set_default_proxy(proxy_type, addr, port, rdns, username, password = (None, None, None, True, None, None)):
        '''Sets a default proxy.

    All further socksocket objects will use the default unless explicitly
    changed. All parameters are as for socket.set_proxy().'''
        socksocket.default_proxy = (proxy_type, addr, port, rdns, username.encode() if username else None, password.encode() if password else None)

    
    def setdefaultproxy(*args, **kwargs):
        if 'proxytype' in kwargs:
            kwargs['proxy_type'] = kwargs.pop('proxytype')
    # WARNING: Decompyle incomplete

    
    def get_default_proxy():
        '''Returns the default proxy, set by set_default_proxy.'''
        return socksocket.default_proxy

    getdefaultproxy = get_default_proxy
    
    def wrap_module(module):
        """Attempts to replace a module's socket library with a SOCKS socket.

    Must set a default proxy using set_default_proxy(...) first. This will
    only work on modules that import socket directly into the namespace;
    most of the Python Standard Library falls into this category."""
        if socksocket.default_proxy:
            module.socket.socket = socksocket
            return None
        raise None('No default proxy specified')

    wrapmodule = wrap_module
    
    def create_connection(dest_pair, timeout, source_address, proxy_type, proxy_addr, proxy_port, proxy_rdns, proxy_username, proxy_password, socket_options = (None, None, None, None, None, True, None, None, None)):
        '''create_connection(dest_pair, *[, timeout], **proxy_args) -> socket object

    Like socket.create_connection(), but connects to proxy
    before returning the socket object.

    dest_pair - 2-tuple of (IP/hostname, port).
    **proxy_args - Same args passed to socksocket.set_proxy() if present.
    timeout - Optional socket timeout value, in seconds.
    source_address - tuple (host, port) for the socket to bind to as its source
    address before connecting (only for compatibility)
    '''
        (remote_host, remote_port) = dest_pair
        if remote_host.startswith('['):
            remote_host = remote_host.strip('[]')
        if proxy_addr and proxy_addr.startswith('['):
            proxy_addr = proxy_addr.strip('[]')
        err = None
    # WARNING: Decompyle incomplete

    
    class _BaseSocket(socket.socket):
        '''Allows Python 2 delegated methods such as send() to be overridden.'''
        
        def __init__(self, *pos, **kw):
            pass
        # WARNING: Decompyle incomplete

        _savenames = list()

    
    def _makemethod(name):
        pass
    # WARNING: Decompyle incomplete

    for name in ('sendto', 'send', 'recvfrom', 'recv'):
        method = getattr(_BaseSocket, name, None)
        if not isinstance(method, Callable):
            _BaseSocket._savenames.append(name)
            setattr(_BaseSocket, name, _makemethod(name))
        
        class socksocket(_BaseSocket):
            pass
        # WARNING: Decompyle incomplete

        return None
