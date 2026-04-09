# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: exceptions.pyc (Python 3.11)

from __future__ import annotations
import difflib
import typing as t
from exceptions import BadRequest
from exceptions import HTTPException
from utils import cached_property
from utils import redirect
if t.TYPE_CHECKING:
    from _typeshed.wsgi import WSGIEnvironment
    from wrappers.request import Request
    from wrappers.response import Response
    from map import MapAdapter
    from rules import Rule

class RoutingException(Exception):
    '''Special exceptions that require the application to redirect, notifying
    about missing urls, etc.

    :internal:
    '''
    pass


class RequestRedirect(RoutingException, HTTPException):
    pass
# WARNING: Decompyle incomplete


class RequestPath(RoutingException):
    pass
# WARNING: Decompyle incomplete


class RequestAliasRedirect(RoutingException):
    pass
# WARNING: Decompyle incomplete


class BuildError(LookupError, RoutingException):
    pass
# WARNING: Decompyle incomplete


class WebsocketMismatch(BadRequest):
    '''The only matched rule is either a WebSocket and the request is
    HTTP, or the rule is HTTP and the request is a WebSocket.
    '''
    pass


class NoMatch(Exception):
    __slots__ = ('have_match_for', 'websocket_mismatch')
    
    def __init__(self = None, have_match_for = None, websocket_mismatch = None):
        self.have_match_for = have_match_for
        self.websocket_mismatch = websocket_mismatch
