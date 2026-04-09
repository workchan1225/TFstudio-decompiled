# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: trsock.pyc (Python 3.11)

import socket

class TransportSocket:
    '''A socket-like wrapper for exposing real transport sockets.

    These objects can be safely returned by APIs like
    `transport.get_extra_info(\'socket\')`.  All potentially disruptive
    operations (like "socket.close()") are banned.
    '''
    __slots__ = ('_sock',)
    
    def __init__(self = None, sock = None):
        self._sock = sock

    family = (lambda self: self._sock.family)()
    type = (lambda self: self._sock.type)()
    proto = (lambda self: self._sock.proto)()
    
    def __repr__(self):
