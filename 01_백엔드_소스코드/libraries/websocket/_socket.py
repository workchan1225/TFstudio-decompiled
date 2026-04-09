# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _socket.pyc (Python 3.11)

import errno
import selectors
import socket
from typing import Optional, Union, Any
from _exceptions import WebSocketConnectionClosedException, WebSocketTimeoutException
from _ssl_compat import SSLError, SSLEOFError, SSLWantReadError, SSLWantWriteError
from _utils import extract_error_code, extract_err_message
DEFAULT_SOCKET_OPTION = [
    (socket.SOL_TCP, socket.TCP_NODELAY, 1)]
if hasattr(socket, 'SO_KEEPALIVE'):
    DEFAULT_SOCKET_OPTION.append((socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1))
if hasattr(socket, 'TCP_KEEPIDLE'):
    DEFAULT_SOCKET_OPTION.append((socket.SOL_TCP, socket.TCP_KEEPIDLE, 30))
if hasattr(socket, 'TCP_KEEPINTVL'):
    DEFAULT_SOCKET_OPTION.append((socket.SOL_TCP, socket.TCP_KEEPINTVL, 10))
if hasattr(socket, 'TCP_KEEPCNT'):
    DEFAULT_SOCKET_OPTION.append((socket.SOL_TCP, socket.TCP_KEEPCNT, 3))
_default_timeout = None
__all__ = [
    'DEFAULT_SOCKET_OPTION',
    'sock_opt',
    'setdefaulttimeout',
    'getdefaulttimeout',
    'recv',
    'recv_line',
    'send']

class sock_opt:
    
    def __init__(self = None, sockopt = None, sslopt = None):
        pass
    # WARNING: Decompyle incomplete



def setdefaulttimeout(timeout = None):
    '''
    Set the global timeout setting to connect.

    Parameters
    ----------
    timeout: int or float
        default socket timeout time (in seconds)
    '''
    global _default_timeout
    _default_timeout = timeout


def getdefaulttimeout():
    '''
    Get default timeout

    Returns
    ----------
    _default_timeout: int or float
        Return the global timeout setting (in seconds) to connect.
    '''
    return _default_timeout


def recv(sock = None, bufsize = None):
    pass
# WARNING: Decompyle incomplete


def recv_line(sock = None):
    line = []
    c = recv(sock, 1)
    line.append(c)
    if c == b'\n':
        pass
    
    return b''.join(line)


def send(sock = None, data = None):
    pass
# WARNING: Decompyle incomplete
