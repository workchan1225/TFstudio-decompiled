# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: timeout.pyc (Python 3.11)

from __future__ import annotations
import time
import typing
from enum import Enum
from socket import getdefaulttimeout
from exceptions import TimeoutStateError
if typing.TYPE_CHECKING:
    from typing import Final

class _TYPE_DEFAULT(Enum):
    token = -1

_DEFAULT_TIMEOUT: 'Final[_TYPE_DEFAULT]' = _TYPE_DEFAULT.token
_TYPE_TIMEOUT = typing.Optional[typing.Union[(float, _TYPE_DEFAULT)]]

class Timeout:
    '''Timeout configuration.

    Timeouts can be defined as a default for a pool:

    .. code-block:: python

        import urllib3

        timeout = urllib3.util.Timeout(connect=2.0, read=7.0)

        http = urllib3.PoolManager(timeout=timeout)

        resp = http.request("GET", "https://example.com/")

        print(resp.status)

    Or per-request (which overrides the default for the pool):

    .. code-block:: python

       response = http.request("GET", "https://example.com/", timeout=Timeout(10))

    Timeouts can be disabled by setting all the parameters to ``None``:

    .. code-block:: python

       no_timeout = Timeout(connect=None, read=None)
       response = http.request("GET", "https://example.com/", timeout=no_timeout)


    :param total:
        This combines the connect and read timeouts into one; the read timeout
        will be set to the time leftover from the connect attempt. In the
        event that both a connect timeout and a total are specified, or a read
        timeout and a total are specified, the shorter timeout will be applied.

        Defaults to None.

    :type total: int, float, or None

    :param connect:
        The maximum amount of time (in seconds) to wait for a connection
        attempt to a server to succeed. Omitting the parameter will default the
        connect timeout to the system default, probably `the global default
        timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout for connection attempts.

    :type connect: int, float, or None

    :param read:
        The maximum amount of time (in seconds) to wait between consecutive
        read operations for a response from the server. Omitting the parameter
        will default the read timeout to the system default, probably `the
        global default timeout in socket.py
        <http://hg.python.org/cpython/file/603b4d593758/Lib/socket.py#l535>`_.
        None will set an infinite timeout.

    :type read: int, float, or None

    .. note::

        Many factors can affect the total amount of time for urllib3 to return
        an HTTP response.

        For example, Python\'s DNS resolver does not obey the timeout specified
        on the socket. Other factors that can affect total request time include
        high CPU load, high swap, the program running at a low priority level,
        or other behaviors.

        In addition, the read and total timeouts only measure the time between
        read operations on the socket connecting the client and the server,
        not the total amount of time for the request to return a complete
        response. For most requests, the timeout is raised because the server
        has not sent the first byte in the specified time. This is not always
        the case; if a server streams one byte every fifteen seconds, a timeout
        of 20 seconds will not trigger, even though the request will take
        several minutes to complete.
    '''
    DEFAULT_TIMEOUT: '_TYPE_TIMEOUT' = _DEFAULT_TIMEOUT
    
    def __init__(self = None, total = None, connect = None, read = (None, _DEFAULT_TIMEOUT, _DEFAULT_TIMEOUT)):
        self._connect = self._validate_timeout(connect, 'connect')
        self._read = self._validate_timeout(read, 'read')
        self.total = self._validate_timeout(total, 'total')
        self._start_connect = None

    
    def __repr__(self = None):
        return f'''{type(self).__name__}(connect={self._connect!r}, read={self._read!r}, total={self.total!r})'''

    __str__ = __repr__
    resolve_default_timeout = (lambda timeout = None: getdefaulttimeout() if timeout is _DEFAULT_TIMEOUT else timeout)()
    _validate_timeout = (lambda cls = None, value = None, name = classmethod: pass# WARNING: Decompyle incomplete
)()
    from_float = (lambda cls = None, timeout = None: Timeout(read = timeout, connect = timeout))()
    
    def clone(self = None):
        '''Create a copy of the timeout object

        Timeout properties are stored per-pool but each request needs a fresh
        Timeout object to ensure each one has its own start/stop configured.

        :return: a copy of the timeout object
        :rtype: :class:`Timeout`
        '''
        return Timeout(connect = self._connect, read = self._read, total = self.total)

    
    def start_connect(self = None):
        '''Start the timeout clock, used during a connect() attempt

        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to start a timer that has been started already.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def get_connect_duration(self = None):
        """Gets the time elapsed since the call to :meth:`start_connect`.

        :return: Elapsed time in seconds.
        :rtype: float
        :raises urllib3.exceptions.TimeoutStateError: if you attempt
            to get duration for a timer that hasn't been started.
        """
        pass
    # WARNING: Decompyle incomplete

    connect_timeout = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    read_timeout = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
