# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

import contextlib
import typing
ExceptionMapping = typing.Mapping[(typing.Type[Exception], typing.Type[Exception])]
map_exceptions = (lambda map = None: pass# WARNING: Decompyle incomplete
)()

class ConnectionNotAvailable(Exception):
    pass


class ProxyError(Exception):
    pass


class UnsupportedProtocol(Exception):
    pass


class ProtocolError(Exception):
    pass


class RemoteProtocolError(ProtocolError):
    pass


class LocalProtocolError(ProtocolError):
    pass


class TimeoutException(Exception):
    pass


class PoolTimeout(TimeoutException):
    pass


class ConnectTimeout(TimeoutException):
    pass


class ReadTimeout(TimeoutException):
    pass


class WriteTimeout(TimeoutException):
    pass


class NetworkError(Exception):
    pass


class ConnectError(NetworkError):
    pass


class ReadError(NetworkError):
    pass


class WriteError(NetworkError):
    pass
