# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auth.pyc (Python 3.11)

from __future__ import annotations
import functools
import hmac
import http
from collections.abc import Awaitable, Iterable
from typing import Any, Callable, cast
from datastructures import Headers
from exceptions import InvalidHeader
from headers import build_www_authenticate_basic, parse_authorization_basic
from server import HTTPResponse, WebSocketServerProtocol
__all__ = [
    'BasicAuthWebSocketServerProtocol',
    'basic_auth_protocol_factory']
Credentials = tuple[(str, str)]

def is_credentials(value = None):
    
    try:
        (username, password) = value
        if isinstance(username, str):
            return isinstance(password, str)
        except (TypeError, ValueError):
            return False



class BasicAuthWebSocketServerProtocol(WebSocketServerProtocol):
    pass
# WARNING: Decompyle incomplete


def basic_auth_protocol_factory(realm = None, credentials = None, check_credentials = None, create_protocol = (None, None, None, None)):
    '''
    Protocol factory that enforces HTTP Basic Auth.

    :func:`basic_auth_protocol_factory` is designed to integrate with
    :func:`~websockets.legacy.server.serve` like this::

        serve(
            ...,
            create_protocol=basic_auth_protocol_factory(
                realm="my dev server",
                credentials=("hello", "iloveyou"),
            )
        )

    Args:
        realm: Scope of protection. It should contain only ASCII characters
            because the encoding of non-ASCII characters is undefined.
            Refer to section 2.2 of :rfc:`7235` for details.
        credentials: Hard coded authorized credentials. It can be a
            ``(username, password)`` pair or a list of such pairs.
        check_credentials: Coroutine that verifies credentials.
            It receives ``username`` and ``password`` arguments
            and returns a :class:`bool`. One of ``credentials`` or
            ``check_credentials`` must be provided but not both.
        create_protocol: Factory that creates the protocol. By default, this
            is :class:`BasicAuthWebSocketServerProtocol`. It can be replaced
            by a subclass.
    Raises:
        TypeError: If the ``credentials`` or ``check_credentials`` argument is
            wrong.

    '''
    pass
# WARNING: Decompyle incomplete
