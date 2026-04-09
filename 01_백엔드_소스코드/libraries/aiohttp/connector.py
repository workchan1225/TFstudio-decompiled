# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: connector.pyc (Python 3.11)

import asyncio
import functools
import random
import socket
import sys
import traceback
import warnings
from collections import OrderedDict, defaultdict, deque
from contextlib import suppress
from http import HTTPStatus
from itertools import chain, cycle, islice
from time import monotonic
from types import TracebackType
from typing import TYPE_CHECKING, Any, Awaitable, Callable, DefaultDict, Deque, Dict, Iterator, List, Literal, Optional, Sequence, Set, Tuple, Type, Union, cast
import aiohappyeyeballs
from aiohappyeyeballs import AddrInfoType, SocketFactoryType
from  import hdrs, helpers
from abc import AbstractResolver, ResolveResult
from client_exceptions import ClientConnectionError, ClientConnectorCertificateError, ClientConnectorDNSError, ClientConnectorError, ClientConnectorSSLError, ClientHttpProxyError, ClientProxyConnectionError, ServerFingerprintMismatch, UnixClientConnectorError, cert_errors, ssl_errors
from client_proto import ResponseHandler
from client_reqrep import ClientRequest, Fingerprint, _merge_ssl_params
from helpers import _SENTINEL, ceil_timeout, is_ip_address, noop, sentinel, set_exception, set_result
from log import client_logger
from resolver import DefaultResolver
if sys.version_info >= (3, 12):
    from collections.abc import Buffer
else:
    Buffer = Union[(bytes, bytearray, 'memoryview[int]', 'memoryview[bytes]')]

class _DeprecationWaiter:
    __slots__ = ('_awaitable', '_awaited')
    
    def __init__(self = None, awaitable = None):
        self._awaitable = awaitable
        self._awaited = False

    
    def __await__(self = None):
        self._awaited = True
        return self._awaitable.__await__()

    
    def __del__(self = None):
        if not self._awaited:
            warnings.warn('Connector.close() is a coroutine, please use await connector.close()', DeprecationWarning)
            return None



async def _wait_for_close(waiters = None):
    '''Wait for all waiters to finish closing.'''
    pass
# WARNING: Decompyle incomplete


class Connection:
    _source_traceback = None
    
    def __init__(self, connector = None, key = None, protocol = None, loop = ('connector', 'BaseConnector', 'key', 'ConnectionKey', 'protocol', ResponseHandler, 'loop', asyncio.AbstractEventLoop, 'return', None)):
        self._key = key
        self._connector = connector
        self._loop = loop
        self._protocol = protocol
        self._callbacks = []
        if loop.get_debug():
            self._source_traceback = traceback.extract_stack(sys._getframe(1))
            return None

    
    def __repr__(self = None):
        return f'''Connection<{self._key}>'''

    
    def __del__(self = None, _warnings = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        '''Force subclasses to not be falsy, to make checks simpler.'''
        return True

    loop = (lambda self = None: warnings.warn('connector.loop property is deprecated', DeprecationWarning, stacklevel = 2)self._loop)()
    transport = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    protocol = (lambda self = None: self._protocol)()
    
    def add_callback(self = None, callback = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _notify_release(self = None):
        callbacks, self._callbacks = self._callbacks[:], []
        for cb in callbacks:
            suppress(Exception)
            cb()
            None(None, None)
        with None:
            if not None:
                pass
        continue

    
    def close(self = None):
        self._notify_release()
    # WARNING: Decompyle incomplete

    
    def release(self = None):
        self._notify_release()
    # WARNING: Decompyle incomplete

    closed = (lambda self = None: if not self._protocol is None:
passnot self._protocol.is_connected())()


class _ConnectTunnelConnection(Connection):
    """Special connection wrapper for CONNECT tunnels that must never be pooled.

    This connection wraps the proxy connection that will be upgraded with TLS.
    It must never be released to the pool because:
    1. Its 'closed' future will never complete, causing session.close() to hang
    2. It represents an intermediate state, not a reusable connection
    3. The real connection (with TLS) will be created separately
    """
    
    def release(self = None):
        """Do nothing - don't pool or close the connection.

        These connections are an intermediate state during the CONNECT tunnel
        setup and will be cleaned up naturally after the TLS upgrade. If they
        were to be pooled, they would never be properly closed, causing
        session.close() to wait forever for their 'closed' future.
        """
        pass



class _TransportPlaceholder:
    '''placeholder for BaseConnector.connect function'''
    __slots__ = ('closed', 'transport')
    
    def __init__(self = None, closed_future = None):
        '''Initialize a placeholder for a transport.'''
        self.closed = closed_future
        self.transport = None

    
    def close(self = None):
        '''Close the placeholder.'''
        pass

    
    def abort(self = None):
        '''Abort the placeholder (does nothing).'''
        pass



class BaseConnector:
    """Base connector class.

    keepalive_timeout - (optional) Keep-alive timeout.
    force_close - Set to True to force close and do reconnect
        after each request (and between redirects).
    limit - The total number of simultaneous connections.
    limit_per_host - Number of simultaneous connections to one host.
    enable_cleanup_closed - Enables clean-up closed ssl transports.
                            Disabled by default.
    timeout_ceil_threshold - Trigger ceiling of timeout values when
                             it's above timeout_ceil_threshold.
    loop - Optional event loop.
    """
    _closed = True
    _source_traceback = None
    _cleanup_closed_period = 2
    allowed_protocol_schema_set = HIGH_LEVEL_SCHEMA_SET
    
    def __init__(self = None, *, keepalive_timeout, force_close, limit, limit_per_host, enable_cleanup_closed, loop, timeout_ceil_threshold):
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self = None, _warnings = None):
