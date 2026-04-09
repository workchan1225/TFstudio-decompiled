# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http.pyc (Python 3.11)

import sys
from http import HTTPStatus
from typing import Mapping, Tuple
from  import __version__
from http_exceptions import HttpProcessingError
from http_parser import HeadersParser, HttpParser, HttpRequestParser, HttpResponseParser, RawRequestMessage, RawResponseMessage
from http_websocket import WS_CLOSED_MESSAGE, WS_CLOSING_MESSAGE, WS_KEY, WebSocketError, WebSocketReader, WebSocketWriter, WSCloseCode, WSMessage, WSMsgType, ws_ext_gen, ws_ext_parse
from http_writer import HttpVersion, HttpVersion10, HttpVersion11, StreamWriter
__all__ = ('HttpProcessingError', 'RESPONSES', 'SERVER_SOFTWARE', 'StreamWriter', 'HttpVersion', 'HttpVersion10', 'HttpVersion11', 'HeadersParser', 'HttpParser', 'HttpRequestParser', 'HttpResponseParser', 'RawRequestMessage', 'RawResponseMessage', 'WS_CLOSED_MESSAGE', 'WS_CLOSING_MESSAGE', 'WS_KEY', 'WebSocketReader', 'WebSocketWriter', 'ws_ext_gen', 'ws_ext_parse', 'WSMessage', 'WebSocketError', 'WSMsgType', 'WSCloseCode')
SERVER_SOFTWARE: str = 'Python/{0[0]}.{0[1]} aiohttp/{1}'.format(sys.version_info, __version__)
RESPONSES: Mapping[(int, Tuple[(str, str)])] = HTTPStatus.__members__.values()()
