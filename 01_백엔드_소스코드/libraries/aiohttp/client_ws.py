# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: client_ws.pyc (Python 3.11)

'''WebSocket client for asyncio.'''
import asyncio
import sys
from types import TracebackType
from typing import Any, Optional, Type, cast
import attr
from _websocket.reader import WebSocketDataQueue
from client_exceptions import ClientError, ServerTimeoutError, WSMessageTypeError
from client_reqrep import ClientResponse
from helpers import calculate_timeout_when, set_result
from http import WS_CLOSED_MESSAGE, WS_CLOSING_MESSAGE, WebSocketError, WSCloseCode, WSMessage, WSMsgType
from http_websocket import _INTERNAL_RECEIVE_TYPES, WebSocketWriter
from streams import EofStream
from typedefs import DEFAULT_JSON_DECODER, DEFAULT_JSON_ENCODER, JSONDecoder, JSONEncoder
if sys.version_info >= (3, 11):
    import asyncio as async_timeout
else:
    import async_timeout
ClientWSTimeout = <NODE:12>()
DEFAULT_WS_CLIENT_TIMEOUT = ClientWSTimeout(ws_receive = None, ws_close = 10)

class ClientWebSocketResponse:
    
    def __init__(self, reader, writer, protocol = None, response = None, timeout = None, autoclose = None, autoping = {
        'heartbeat': None,
        'compress': 0,
        'client_notakeover': False }, loop = ('reader', WebSocketDataQueue, 'writer', WebSocketWriter, 'protocol', Optional[str], 'response', ClientResponse, 'timeout', ClientWSTimeout, 'autoclose', bool, 'autoping', bool, 'loop', asyncio.AbstractEventLoop, 'heartbeat', Optional[float], 'compress', int, 'client_notakeover', bool, 'return', None), *, heartbeat, compress, client_notakeover):
        self._response = response
        self._conn = response.connection
        self._writer = writer
        self._reader = reader
        self._protocol = protocol
        self._closed = False
        self._closing = False
        self._close_code = None
        self._timeout = timeout
        self._autoclose = autoclose
        self._autoping = autoping
        self._heartbeat = heartbeat
        self._heartbeat_cb = None
        self._heartbeat_when = 0
    # WARNING: Decompyle incomplete

    
    def _cancel_heartbeat(self = None):
        self._cancel_pong_response_cb()
    # WARNING: Decompyle incomplete

    
    def _cancel_pong_response_cb(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _reset_heartbeat(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _send_heartbeat(self = None):
        self._heartbeat_cb = None
        loop = self._loop
        now = loop.time()
        if now < self._heartbeat_when:
            self._heartbeat_cb = loop.call_at(self._heartbeat_when, self._send_heartbeat)
            return None
        conn = None._conn
    # WARNING: Decompyle incomplete

    
    def _ping_task_done(self = None, task = None):
        '''Callback for when the ping task completes.'''
        if not task.cancelled():
            exc = task.exception()
            if task.exception():
                self._handle_ping_pong_exception(exc)
        self._ping_task = None

    
    def _pong_not_received(self = None):
        self._handle_ping_pong_exception(ServerTimeoutError(f'''No PONG received after {self._pong_heartbeat} seconds'''))

    
    def _handle_ping_pong_exception(self = None, exc = None):
        '''Handle exceptions raised during ping/pong processing.'''
        if self._closed:
            return None
        None._set_closed()
        self._close_code = WSCloseCode.ABNORMAL_CLOSURE
        self._exception = exc
        self._response.close()
        if not self._waiting or self._closing:
            self._reader.feed_data(WSMessage(WSMsgType.ERROR, exc, None), 0)
            return None
        return None

    
    def _set_closed(self = None):
        '''Set the connection to closed.

        Cancel any heartbeat timers and set the closed flag.
        '''
        self._closed = True
        self._cancel_heartbeat()

    
    def _set_closing(self = None):
        '''Set the connection to closing.

        Cancel any heartbeat timers and set the closing flag.
        '''
        self._closing = True
        self._cancel_heartbeat()

    closed = (lambda self = None: self._closed)()
    close_code = (lambda self = None: self._close_code)()
    protocol = (lambda self = None: self._protocol)()
    compress = (lambda self = None: self._compress)()
    client_notakeover = (lambda self = None: self._client_notakeover)()
    
    def get_extra_info(self = None, name = None, default = None):
        '''extra info from connection transport'''
        conn = self._response.connection
    # WARNING: Decompyle incomplete

    
    def exception(self = None):
        return self._exception

    
    async def ping(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def pong(self = None, message = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_frame(self = None, message = None, opcode = None, compress = (None,)):
        '''Send a frame over the websocket.'''
        pass
    # WARNING: Decompyle incomplete

    
    async def send_str(self = None, data = None, compress = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_bytes(self = None, data = None, compress = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_json(self = None, data = None, compress = None, *, dumps):
        pass
    # WARNING: Decompyle incomplete

    
    async def close(self = None, *, code, message):
        pass
    # WARNING: Decompyle incomplete

    
    async def receive(self = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def receive_str(self = None, *, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    async def receive_bytes(self = None, *, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    async def receive_json(self = None, *, loads, timeout):
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aenter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def __aexit__(self = None, exc_type = None, exc_val = None, exc_tb = ('exc_type', Optional[Type[BaseException]], 'exc_val', Optional[BaseException], 'exc_tb', Optional[TracebackType], 'return', None)):
        pass
    # WARNING: Decompyle incomplete
