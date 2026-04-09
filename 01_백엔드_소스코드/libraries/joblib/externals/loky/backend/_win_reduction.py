# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _win_reduction.pyc (Python 3.11)

import socket
from multiprocessing import connection
from multiprocessing.reduction import _reduce_socket
from reduction import register
register(socket.socket, _reduce_socket)
register(connection.Connection, connection.reduce_connection)
register(connection.PipeConnection, connection.reduce_pipe_connection)
