# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''Types for aiohappyeyeballs.'''
import socket
from typing import Callable, Tuple, Union
AddrInfoType = Tuple[(Union[(int, socket.AddressFamily)], Union[(int, socket.SocketKind)], int, str, Tuple)]
SocketFactoryType = Callable[([
    AddrInfoType], socket.socket)]
