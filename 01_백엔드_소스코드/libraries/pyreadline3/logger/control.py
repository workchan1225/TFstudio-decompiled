# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: control.pyc (Python 3.11)

import os
from logging import FileHandler, Formatter, StreamHandler
from logging.handlers import DEFAULT_TCP_LOGGING_PORT
from typing import Optional
from logger import LOGGER
from socket_stream import SocketStream
_default_formatter_str = os.environ.get('PYREADLINE_FORMATTER', '%(message)s')
SOCKET_HANDLER: Optional['StreamHandler[SocketStream]'] = None
FILE_HANDLER: Optional[FileHandler] = None

def start_socket_log(host = None, port = None, formatter_str = None):
    pass
# WARNING: Decompyle incomplete


def stop_socket_log():
    pass
# WARNING: Decompyle incomplete


def start_file_log(filename = None):
    pass
# WARNING: Decompyle incomplete


def stop_file_log():
    pass
# WARNING: Decompyle incomplete


def stop_logging():
    stop_file_log()
    stop_socket_log()
