# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tcp_helpers.pyc (Python 3.11)

'''Helper methods to tune a TCP connection'''
import asyncio
import socket
from contextlib import suppress
from typing import Optional
__all__ = ('tcp_keepalive', 'tcp_nodelay')
if hasattr(socket, 'SO_KEEPALIVE'):
    
    def tcp_keepalive(transport = None):
        sock = transport.get_extra_info('socket')
    # WARNING: Decompyle incomplete

else:
    
    def tcp_keepalive(transport = None):
        pass


def tcp_nodelay(transport = None, value = None):
    sock = transport.get_extra_info('socket')
# WARNING: Decompyle incomplete
