# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

import http
from  import datastructures
from exceptions import InvalidHandshake, InvalidMessage, ProtocolError as WebSocketProtocolError
from typing import StatusLike

class InvalidStatusCode(InvalidHandshake):
    '''
    Raised when a handshake response status code is invalid.

    '''
    
    def __init__(self = None, status_code = None, headers = None):
        self.status_code = status_code
        self.headers = headers

    
    def __str__(self = None):
        return f'''server rejected WebSocket connection: HTTP {self.status_code}'''



class AbortHandshake(InvalidHandshake):
    '''
    Raised to abort the handshake on purpose and return an HTTP response.

    This exception is an implementation detail.

    The public API is
    :meth:`~websockets.legacy.server.WebSocketServerProtocol.process_request`.

    Attributes:
        status (~http.HTTPStatus): HTTP status code.
        headers (Headers): HTTP response headers.
        body (bytes): HTTP response body.
    '''
    
    def __init__(self = None, status = None, headers = None, body = (b'',)):
        self.status = http.HTTPStatus(status)
        self.headers = datastructures.Headers(headers)
        self.body = body

    
    def __str__(self = None):
        return f'''HTTP {self.status:d}, {len(self.headers)} headers, {len(self.body)} bytes'''



class RedirectHandshake(InvalidHandshake):
    '''
    Raised when a handshake gets redirected.

    This exception is an implementation detail.

    '''
    
    def __init__(self = None, uri = None):
        self.uri = uri

    
    def __str__(self = None):
        return f'''redirect to {self.uri}'''
