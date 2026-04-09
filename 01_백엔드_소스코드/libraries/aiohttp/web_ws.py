# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_ws.pyc (Python 3.11)

import asyncio
import base64
import binascii
import hashlib
import json
import sys
from typing import Any, Final, Iterable, Optional, Tuple, Union, cast
import attr
from multidict import CIMultiDict
from  import hdrs
from _websocket.reader import WebSocketDataQueue
from _websocket.writer import DEFAULT_LIMIT
from abc import AbstractStreamWriter
from client_exceptions import WSMessageTypeError
from helpers import calculate_timeout_when, set_exception, set_result
from http import WS_CLOSED_MESSAGE, WS_CLOSING_MESSAGE, WS_KEY, WebSocketError, WebSocketReader, WebSocketWriter, WSCloseCode, WSMessage, WSMsgType, ws_ext_gen, ws_ext_parse
from http_websocket import _INTERNAL_RECEIVE_TYPES
from log import ws_logger
from streams import EofStream
from typedefs import JSONDecoder, JSONEncoder
from web_exceptions import HTTPBadRequest, HTTPException
from web_request import BaseRequest
from web_response import StreamResponse
if sys.version_info >= (3, 11):
    import asyncio as async_timeout
else:
    import async_timeout
__all__ = ('WebSocketResponse', 'WebSocketReady', 'WSMsgType')
THRESHOLD_CONNLOST_ACCESS: Final[int] = 5
WebSocketReady = <NODE:12>()

class WebSocketResponse(StreamResponse):
    pass
# WARNING: Decompyle incomplete
