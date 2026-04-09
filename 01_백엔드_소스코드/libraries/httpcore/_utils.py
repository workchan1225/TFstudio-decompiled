# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _utils.pyc (Python 3.11)

from __future__ import annotations
import select
import socket
import sys

def is_socket_readable(sock = None):
    '''
    Return whether a socket, as identifed by its file descriptor, is readable.
    "A socket is readable" means that the read buffer isn\'t empty, i.e. that calling
    .recv() on it would immediately return some data.
    '''
    pass
# WARNING: Decompyle incomplete
