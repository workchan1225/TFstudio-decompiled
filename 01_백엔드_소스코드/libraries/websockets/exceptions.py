# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

'''
:mod:`websockets.exceptions` defines the following hierarchy of exceptions.

* :exc:`WebSocketException`
    * :exc:`ConnectionClosed`
        * :exc:`ConnectionClosedOK`
        * :exc:`ConnectionClosedError`
    * :exc:`InvalidURI`
    * :exc:`InvalidProxy`
    * :exc:`InvalidHandshake`
        * :exc:`SecurityError`
        * :exc:`ProxyError`
            * :exc:`InvalidProxyMessage`
            * :exc:`InvalidProxyStatus`
        * :exc:`InvalidMessage`
        * :exc:`InvalidStatus`
        * :exc:`InvalidStatusCode` (legacy)
        * :exc:`InvalidHeader`
            * :exc:`InvalidHeaderFormat`
            * :exc:`InvalidHeaderValue`
            * :exc:`InvalidOrigin`
            * :exc:`InvalidUpgrade`
        * :exc:`NegotiationError`
            * :exc:`DuplicateParameter`
            * :exc:`InvalidParameterName`
            * :exc:`InvalidParameterValue`
        * :exc:`AbortHandshake` (legacy)
        * :exc:`RedirectHandshake` (legacy)
    * :exc:`ProtocolError` (Sans-I/O)
    * :exc:`PayloadTooBig` (Sans-I/O)
    * :exc:`InvalidState` (Sans-I/O)
    * :exc:`ConcurrencyError`

'''
from __future__ import annotations
import warnings
from imports import lazy_import
__all__ = [
    'WebSocketException',
    'ConnectionClosed',
    'ConnectionClosedOK',
    'ConnectionClosedError',
    'InvalidURI',
    'InvalidProxy',
    'InvalidHandshake',
    'SecurityError',
    'ProxyError',
    'InvalidProxyMessage',
    'InvalidProxyStatus',
    'InvalidMessage',
    'InvalidStatus',
    'InvalidHeader',
    'InvalidHeaderFormat',
    'InvalidHeaderValue',
    'InvalidOrigin',
    'InvalidUpgrade',
    'NegotiationError',
    'DuplicateParameter',
    'InvalidParameterName',
    'InvalidParameterValue',
    'ProtocolError',
    'PayloadTooBig',
    'InvalidState',
    'ConcurrencyError']

class WebSocketException(Exception):
    '''
    Base class for all exceptions defined by websockets.

    '''
    pass


class ConnectionClosed(WebSocketException):
    '''
    Raised when trying to interact with a closed connection.

    Attributes:
        rcvd: If a close frame was received, its code and reason are available
            in ``rcvd.code`` and ``rcvd.reason``.
        sent: If a close frame was sent, its code and reason are available
            in ``sent.code`` and ``sent.reason``.
        rcvd_then_sent: If close frames were received and sent, this attribute
            tells in which order this happened, from the perspective of this
            side of the connection.

    '''
    
    def __init__(self = None, rcvd = None, sent = None, rcvd_then_sent = (None,)):
        self.rcvd = rcvd
        self.sent = sent
        self.rcvd_then_sent = rcvd_then_sent
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete

    code = (lambda self = None: warnings.warn('ConnectionClosed.code is deprecated; use Protocol.close_code or ConnectionClosed.rcvd.code', DeprecationWarning)# WARNING: Decompyle incomplete
)()
    reason = (lambda self = None: warnings.warn('ConnectionClosed.reason is deprecated; use Protocol.close_reason or ConnectionClosed.rcvd.reason', DeprecationWarning)# WARNING: Decompyle incomplete
)()


class ConnectionClosedOK(ConnectionClosed):
    '''
    Like :exc:`ConnectionClosed`, when the connection terminated properly.

    A close code with code 1000 (OK) or 1001 (going away) or without a code was
    received and sent.

    '''
    pass


class ConnectionClosedError(ConnectionClosed):
    """
    Like :exc:`ConnectionClosed`, when the connection terminated with an error.

    A close frame with a code other than 1000 (OK) or 1001 (going away) was
    received or sent, or the closing handshake didn't complete properly.

    """
    pass


class InvalidURI(WebSocketException):
    """
    Raised when connecting to a URI that isn't a valid WebSocket URI.

    """
    
    def __init__(self = None, uri = None, msg = None):
        self.uri = uri
        self.msg = msg

    
    def __str__(self = None):
        return f'''{self.uri} isn\'t a valid URI: {self.msg}'''



class InvalidProxy(WebSocketException):
    """
    Raised when connecting via a proxy that isn't valid.

    """
    
    def __init__(self = None, proxy = None, msg = None):
        self.proxy = proxy
        self.msg = msg

    
    def __str__(self = None):
        return f'''{self.proxy} isn\'t a valid proxy: {self.msg}'''



class InvalidHandshake(WebSocketException):
    '''
    Base class for exceptions raised when the opening handshake fails.

    '''
    pass


class SecurityError(InvalidHandshake):
    '''
    Raised when a handshake request or response breaks a security rule.

    Security limits can be configured with :doc:`environment variables
    <../reference/variables>`.

    '''
    pass


class ProxyError(InvalidHandshake):
    '''
    Raised when failing to connect to a proxy.

    '''
    pass


class InvalidProxyMessage(ProxyError):
    '''
    Raised when an HTTP proxy response is malformed.

    '''
    pass


class InvalidProxyStatus(ProxyError):
    '''
    Raised when an HTTP proxy rejects the connection.

    '''
    
    def __init__(self = None, response = None):
        self.response = response

    
    def __str__(self = None):
        return f'''proxy rejected connection: HTTP {self.response.status_code:d}'''



class InvalidMessage(InvalidHandshake):
    '''
    Raised when a handshake request or response is malformed.

    '''
    pass


class InvalidStatus(InvalidHandshake):
    '''
    Raised when a handshake response rejects the WebSocket upgrade.

    '''
    
    def __init__(self = None, response = None):
        self.response = response

    
    def __str__(self = None):
        return f'''server rejected WebSocket connection: HTTP {self.response.status_code:d}'''



class InvalidHeader(InvalidHandshake):
    """
    Raised when an HTTP header doesn't have a valid format or value.

    """
    
    def __init__(self = None, name = None, value = None):
        self.name = name
        self.value = value

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete



class InvalidHeaderFormat(InvalidHeader):
    pass
# WARNING: Decompyle incomplete


class InvalidHeaderValue(InvalidHeader):
    """
    Raised when an HTTP header has a wrong value.

    The format of the header is correct but the value isn't acceptable.

    """
    pass


class InvalidOrigin(InvalidHeader):
    pass
# WARNING: Decompyle incomplete


class InvalidUpgrade(InvalidHeader):
    """
    Raised when the Upgrade or Connection header isn't correct.

    """
    pass


class NegotiationError(InvalidHandshake):
    '''
    Raised when negotiating an extension or a subprotocol fails.

    '''
    pass


class DuplicateParameter(NegotiationError):
    '''
    Raised when a parameter name is repeated in an extension header.

    '''
    
    def __init__(self = None, name = None):
        self.name = name

    
    def __str__(self = None):
        return f'''duplicate parameter: {self.name}'''



class InvalidParameterName(NegotiationError):
    '''
    Raised when a parameter name in an extension header is invalid.

    '''
    
    def __init__(self = None, name = None):
        self.name = name

    
    def __str__(self = None):
        return f'''invalid parameter name: {self.name}'''



class InvalidParameterValue(NegotiationError):
    '''
    Raised when a parameter value in an extension header is invalid.

    '''
    
    def __init__(self = None, name = None, value = None):
        self.name = name
        self.value = value

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete



class ProtocolError(WebSocketException):
    '''
    Raised when receiving or sending a frame that breaks the protocol.

    The Sans-I/O implementation raises this exception when:

    * receiving or sending a frame that contains invalid data;
    * receiving or sending an invalid sequence of frames.

    '''
    pass


class PayloadTooBig(WebSocketException):
    """
    Raised when parsing a frame with a payload that exceeds the maximum size.

    The Sans-I/O layer uses this exception internally. It doesn't bubble up to
    the I/O layer.

    The :meth:`~websockets.extensions.Extension.decode` method of extensions
    must raise :exc:`PayloadTooBig` if decoding a frame would exceed the limit.

    """
    
    def __init__(self = None, size_or_message = None, max_size = None, cur_size = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def set_current_size(self = None, cur_size = None):
        pass
    # WARNING: Decompyle incomplete



class InvalidState(AssertionError, WebSocketException):
    '''
    Raised when sending a frame is forbidden in the current state.

    Specifically, the Sans-I/O layer raises this exception when:

    * sending a data frame to a connection in a state other
      :attr:`~websockets.protocol.State.OPEN`;
    * sending a control frame to a connection in a state other than
      :attr:`~websockets.protocol.State.OPEN` or
      :attr:`~websockets.protocol.State.CLOSING`.

    '''
    pass


class ConcurrencyError(RuntimeError, WebSocketException):
    '''
    Raised when receiving or sending messages concurrently.

    WebSocket is a connection-oriented protocol. Reads must be serialized; so
    must be writes. However, reading and writing concurrently is possible.

    '''
    pass

from  import frames, http11
lazy_import(globals(), deprecated_aliases = {
    'AbortHandshake': '.legacy.exceptions',
    'InvalidStatusCode': '.legacy.exceptions',
    'RedirectHandshake': '.legacy.exceptions',
    'WebSocketProtocolError': '.legacy.exceptions' })
