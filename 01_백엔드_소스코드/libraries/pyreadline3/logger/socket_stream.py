# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: socket_stream.pyc (Python 3.11)

from socket import AF_INET, SOCK_DGRAM, socket
from pyreadline3.unicode_helper import ensure_str

class SocketStream:
    
    def __init__(self = None, host = None, port = None):
        self._SocketStream__host = host
        self._SocketStream__port = port
        self._SocketStream__socket = socket(AF_INET, SOCK_DGRAM)

    
    def write(self = None, record = None):
        self._SocketStream__socket.sendto(ensure_str(record), (self._SocketStream__host, self._SocketStream__port))

    
    def flush(self = None):
        pass

    
    def close(self = None):
        pass
