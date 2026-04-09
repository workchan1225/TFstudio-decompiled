# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connection.pyc (Python 3.11)

from __future__ import annotations
import socket
import typing
from exceptions import LocationParseError
from timeout import _DEFAULT_TIMEOUT, _TYPE_TIMEOUT
_TYPE_SOCKET_OPTIONS = list[tuple[(int, int, typing.Union[(int, bytes)])]]
if typing.TYPE_CHECKING:
    from _base_connection import BaseHTTPConnection

def is_connection_dropped(conn = None):
    '''
    Returns True if the connection is dropped and should be closed.
    :param conn: :class:`urllib3.connection.HTTPConnection` object.
    '''
    return not (conn.is_connected)


def create_connection(address = None, timeout = None, source_address = None, socket_options = (_DEFAULT_TIMEOUT, None, None)):
    """Connect to *address* and return the socket object.

    Convenience function.  Connect to *address* (a 2-tuple ``(host,
    port)``) and return the socket object.  Passing the optional
    *timeout* parameter will set the timeout on the socket instance
    before attempting to connect.  If no *timeout* is supplied, the
    global default timeout setting returned by :func:`socket.getdefaulttimeout`
    is used.  If *source_address* is set it must be a tuple of (host, port)
    for the socket to bind as a source address before making the connection.
    An host of '' or port 0 tells the OS to use the default.
    """
    (host, port) = address
    if host.startswith('['):
        host = host.strip('[]')
    err = None
    family = allowed_gai_family()
    
    try:
        host.encode('idna')
    except UnicodeError:
        raise LocationParseError(f'''\'{host}\', label empty or too long'''), None

# WARNING: Decompyle incomplete


def _set_socket_options(sock = None, options = None):
    pass
# WARNING: Decompyle incomplete


def allowed_gai_family():
    '''This function is designed to work in the context of
    getaddrinfo, where family=socket.AF_UNSPEC is the default and
    will perform a DNS search for both IPv6 and IPv4 records.'''
    family = socket.AF_INET
    if HAS_IPV6:
        family = socket.AF_UNSPEC
    return family


def _has_ipv6(host = None):
    '''Returns True if the system can bind an IPv6 address.'''
    sock = None
    has_ipv6 = False
    if socket.has_ipv6:
        
        try:
            sock = socket.socket(socket.AF_INET6)
            sock.bind((host, 0))
            has_ipv6 = True
        except Exception:
            pass

        if sock:
            sock.close()
    return has_ipv6

HAS_IPV6 = _has_ipv6('::1')
