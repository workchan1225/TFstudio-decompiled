# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_protocol.pyc (Python 3.11)

import asyncio
import asyncio.streams as asyncio
import sys
import traceback
import warnings
from collections import deque
from contextlib import suppress
from html import escape as html_escape
from http import HTTPStatus
from logging import Logger
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Deque, Optional, Sequence, Tuple, Type, Union, cast
import attr
import yarl
from propcache import under_cached_property
from abc import AbstractAccessLogger, AbstractStreamWriter
from base_protocol import BaseProtocol
from helpers import ceil_timeout
from http import HttpProcessingError, HttpRequestParser, HttpVersion10, RawRequestMessage, StreamWriter
from http_exceptions import BadHttpMethod
from log import access_logger, server_logger
from streams import EMPTY_PAYLOAD, StreamReader
from tcp_helpers import tcp_keepalive
from web_exceptions import HTTPException, HTTPInternalServerError
from web_log import AccessLogger
from web_request import BaseRequest
from web_response import Response, StreamResponse
__all__ = ('RequestHandler', 'RequestPayloadError', 'PayloadAccessError')
if TYPE_CHECKING:
    import ssl
    from web_server import Server
_RequestFactory = Callable[([
    RawRequestMessage,
    StreamReader,
    'RequestHandler',
    AbstractStreamWriter,
    'asyncio.Task[None]'], BaseRequest)]
_RequestHandler = Callable[([
    BaseRequest], Awaitable[StreamResponse])]
ERROR = RawRequestMessage('UNKNOWN', '/', HttpVersion10, { }, { }, True, None, False, False, yarl.URL('/'))

class RequestPayloadError(Exception):
    '''Payload parsing error.'''
    pass


class PayloadAccessError(Exception):
    '''Payload was accessed after response was sent.'''
    pass

_PAYLOAD_ACCESS_ERROR = PayloadAccessError()
_ErrInfo = <NODE:12>()
_MsgType = Tuple[(Union[(RawRequestMessage, _ErrInfo)], StreamReader)]

class RequestHandler(BaseProtocol):
    pass
# WARNING: Decompyle incomplete
