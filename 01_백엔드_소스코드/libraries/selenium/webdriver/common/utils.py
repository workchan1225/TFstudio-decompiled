# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''Utility functions.'''
import json
import socket
import urllib.request as urllib
from collections.abc import Iterable
from selenium.webdriver.common.keys import Keys
_is_connectable_exceptions = (socket.error, ConnectionResetError)

def free_port():
    """Determines a free port using sockets.

    First try IPv4, but use IPv6 if it can't bind (IPv6-only system).
    """
    free_socket = None
    
    try:
        free_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        free_socket.bind(('127.0.0.1', 0))
    except OSError:
        if free_socket:
            free_socket.close()
        free_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        free_socket.bind(('::1', 0))
    except OSError:
        if free_socket:
            free_socket.close()
        raise RuntimeError("Can't find free port (Unable to bind to IPv4 or IPv6)")



def find_connectable_ip(host = None, port = None):
    """Resolve a hostname to an IP, preferring IPv4 addresses.

    We prefer IPv4 so that we don't change behavior from previous IPv4-only
    implementations, and because some drivers (e.g., FirefoxDriver) do not
    support IPv6 connections.

    If the optional port number is provided, only IPs that listen on the given
    port are considered.

    Args:
        host: hostname
        port: port number

    Returns:
        A single IP address, as a string. If any IPv4 address is found, one is
        returned. Otherwise, if any IPv6 address is found, one is returned. If
        neither, then None is returned.
    """
    
    try:
        addrinfos = socket.getaddrinfo(host, None)
    except socket.gaierror:
        return None

    ip = None
    for family, _, _, _, sockaddr in addrinfos:
        connectable = True
        if port:
            connectable = is_connectable(port, str(sockaddr[0]))
        if connectable and family == socket.AF_INET:
            
            return None, str(sockaddr[0])
        if None and ip and family == socket.AF_INET6:
            pass
        return ip


def join_host_port(host = None, port = None):
    """Joins a hostname and port together.

    This is a minimal implementation intended to cope with IPv6 literals. For
    example, _join_host_port('::1', 80) == '[::1]:80'.

    Args:
        host: hostname or IP
        port: port number
    """
    if not ':' in host and host.startswith('['):
        return f'''[{host}]:{port}'''
    return f'''{None}:{port}'''


def is_connectable(port = None, host = None):
