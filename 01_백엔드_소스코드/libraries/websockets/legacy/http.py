# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

from __future__ import annotations
import asyncio
import os
import re
from datastructures import Headers
from exceptions import SecurityError
__all__ = [
    'read_request',
    'read_response']
MAX_NUM_HEADERS = int(os.environ.get('WEBSOCKETS_MAX_NUM_HEADERS', '128'))
MAX_LINE_LENGTH = int(os.environ.get('WEBSOCKETS_MAX_LINE_LENGTH', '8192'))

def d(value = None):
    '''
    Decode a bytestring for interpolating into an error message.

    '''
    return value.decode(errors = 'backslashreplace')

_token_re = re.compile(b"[-!#$%&\\'*+.^_`|~0-9a-zA-Z]+")
_value_re = re.compile(b'[\\x09\\x20-\\x7e\\x80-\\xff]*')

async def read_request(stream = None):
    """
    Read an HTTP/1.1 GET request and return ``(path, headers)``.

    ``path`` isn't URL-decoded or validated in any way.

    ``path`` and ``headers`` are expected to contain only ASCII characters.
    Other characters are represented with surrogate escapes.

    :func:`read_request` doesn't attempt to read the request body because
    WebSocket handshake requests don't have one. If the request contains a
    body, it may be read from ``stream`` after this coroutine returns.

    Args:
        stream: Input to read the request from.

    Raises:
        EOFError: If the connection is closed without a full HTTP request.
        SecurityError: If the request exceeds a security limit.
        ValueError: If the request isn't well formatted.

    """
    pass
# WARNING: Decompyle incomplete


async def read_response(stream = None):
    """
    Read an HTTP/1.1 response and return ``(status_code, reason, headers)``.

    ``reason`` and ``headers`` are expected to contain only ASCII characters.
    Other characters are represented with surrogate escapes.

    :func:`read_request` doesn't attempt to read the response body because
    WebSocket handshake responses don't have one. If the response contains a
    body, it may be read from ``stream`` after this coroutine returns.

    Args:
        stream: Input to read the response from.

    Raises:
        EOFError: If the connection is closed without a full HTTP response.
        SecurityError: If the response exceeds a security limit.
        ValueError: If the response isn't well formatted.

    """
    pass
# WARNING: Decompyle incomplete


async def read_headers(stream = None):
    '''
    Read HTTP headers from ``stream``.

    Non-ASCII characters are represented with surrogate escapes.

    '''
    pass
# WARNING: Decompyle incomplete


async def read_line(stream = None):
    '''
    Read a single line from ``stream``.

    CRLF is stripped from the return value.

    '''
    pass
# WARNING: Decompyle incomplete
